"""Build immutable stage inputs and review packets from verified run artifacts."""

import json
from featuretree.taxonomy.structure import lint_features
from featuretree.workflow.stages import PLATFORMS
from featuretree.workflow.state import artifact, digest, read_json
from featuretree.workflow.contracts import output_schema
from featuretree.workflow.gates import validate_proposal
from featuretree.workflow.planning import work_order
from featuretree.workflow.sources import source_context
from featuretree.workflow.repairs import repair_packet


def snapshot_for(folder, state):
    snapshot = read_json(folder / "snapshot.json")
    if digest(snapshot) != state["snapshot_hash"]:
        raise ValueError("Input snapshot was modified")
    return snapshot


def node_inputs(folder, state, node):
    return {t["stage"]: artifact(folder, t)["payload"] for t in state["tasks"].values()
            if t["node"] == node and t["status"] == "succeeded"}


def make_packet(root, folder, state, task, snapshot):
    repaired = repair_packet(folder, task)
    if repaired is not None:
        return seal_packet(repaired, state)
    stage, node = task["stage"], task["node"]
    work = work_order(snapshot, state, node)
    if node:
        inputs = node_inputs(folder, state, node)
    else:
        inputs = {n: {k: v for k, v in node_inputs(folder, state, n).items()
                      if k in ("synthesize", "review", "anchors")} for n in state["nodes"]}
        proposed = [item for data in inputs.values() for item in data["synthesize"]["nodes"]]
        ids = [item["id"] for item in proposed]
        if len(ids) != len(set(ids)):
            raise ValueError("Cross-work-order duplicate feature ID")
        union = {**snapshot["features"], **{n["id"]: n for n in proposed}}
        inputs["global_lint"] = lint_features(union, set())
        if any(i["severity"] == "error" for i in inputs["global_lint"]):
            raise ValueError("Merged candidate tree fails structural lint")
    packet = {"schema_version": 1, "task_id": task["id"], "stage": stage,
              "run_id": state["id"], "work": work, "inputs": inputs,
              "limits": {"first_response_timeout": state.get("first_response_timeout", 120)},
              "snapshot_path": str((folder / "snapshot.json").resolve())}
    packet["policy_context"] = {path: (root / path).read_text() for path in
                                ("docs/knowledge/sources.md", "docs/corpus/entrypoints.md")
                                if (root / path).is_file()}
    if "feedback" in task:
        packet["revision_feedback"] = task["feedback"]
    if task["attempts"] and task["attempts"][-1].get("error"):
        packet["previous_error"] = task["attempts"][-1]["error"]
    if stage in PLATFORMS:
        packet["sources"] = source_context(root, work, stage)
    if stage == "review":
        packet["inputs"]["structural_gate"] = validate_proposal(
            root, snapshot, work, inputs["synthesize"], [inputs[p] for p in PLATFORMS])
        packet["inputs"]["source_refs"] = platform_source_refs(folder, state, node)
    if stage != "anchors":
        packet["output_schema"] = output_schema(root, stage)
        if stage == "synthesize":
            packet["feature_schema"] = read_json(root / "config/schema/feature.schema.json")
    if stage in ("review", "integrate"):
        packet["reviewed_hash"] = digest(packet["inputs"])
    return seal_packet(packet, state)


def seal_packet(packet, state):
    packet["input_hash"] = digest(packet)
    if len(json.dumps(packet, ensure_ascii=False)) > state["max_input_chars"]:
        raise ValueError("Input exceeds max_input_chars; select a smaller/deeper work order or split the batch")
    return packet


def platform_source_refs(folder, state, node):
    """Give reviewers verified source locations instead of searching other runs."""
    refs = {}
    for platform in PLATFORMS:
        task = state["tasks"][f"{node}/{platform}"]
        result = artifact(folder, task)
        packet = read_json((folder / task["result_path"]).parent / "input.json")
        expected = packet.pop("input_hash")
        if digest(packet) != expected or expected != result["input_hash"]:
            raise ValueError("Platform source input was modified")
        refs[platform] = [{key: row[key] for key in ("url", "title", "body_path", "body_sha256")}
                          for row in packet.get("sources", {}).get("sources", [])]
    return refs
