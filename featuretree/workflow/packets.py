"""Build immutable stage inputs and review packets from verified run artifacts."""

import json
from featuretree.taxonomy.structure import lint_features
from featuretree.workflow.stages import PLATFORMS
from featuretree.workflow.state import artifact, digest, read_json
from featuretree.workflow.contracts import output_schema
from featuretree.workflow.gates import validate_proposal
from featuretree.workflow.planning import work_order
from featuretree.workflow.sources import source_context


def snapshot_for(folder, state):
    snapshot = read_json(folder / "snapshot.json")
    if digest(snapshot) != state["snapshot_hash"]:
        raise ValueError("Input snapshot was modified")
    return snapshot


def node_inputs(folder, state, node):
    return {t["stage"]: artifact(folder, t)["payload"] for t in state["tasks"].values()
            if t["node"] == node and t["status"] == "succeeded"}


def make_packet(root, folder, state, task, snapshot):
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
              "snapshot_path": str((folder / "snapshot.json").resolve())}
    if "feedback" in task:
        packet["revision_feedback"] = task["feedback"]
    if task["attempts"] and task["attempts"][-1].get("error"):
        packet["previous_error"] = task["attempts"][-1]["error"]
    if stage in PLATFORMS:
        packet["sources"] = source_context(root, work, stage)
    if stage == "review":
        packet["inputs"]["structural_gate"] = validate_proposal(
            root, snapshot, work, inputs["synthesize"], [inputs[p] for p in PLATFORMS])
    if stage != "anchors":
        packet["output_schema"] = output_schema(root, stage)
        if stage == "synthesize":
            packet["feature_schema"] = read_json(root / "config/schema/feature.schema.json")
    if stage in ("review", "integrate"):
        packet["reviewed_hash"] = digest(packet["inputs"])
    packet["input_hash"] = digest(packet)
    if len(json.dumps(packet, ensure_ascii=False)) > state["max_input_chars"]:
        raise ValueError("Input exceeds max_input_chars; select a smaller/deeper work order or split the batch")
    return packet
