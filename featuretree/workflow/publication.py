"""Revalidate artifacts, prepare a recoverable journal, and publish under a lock."""

from copy import deepcopy
import hashlib

import yaml

from featuretree.knowledge.comparison import new_knowledge
from featuretree.core.storage import Repository, contained_path, read_yaml, write_json, write_text
from featuretree.workflow.stages import PLATFORMS
from featuretree.workflow.state import artifact, digest, load_run, lock, now, read_json, run_path, save_state
from featuretree.workflow.contracts import validate_result
from featuretree.workflow.packets import node_inputs, snapshot_for
from featuretree.workflow.gates import counts, validate_proposal
from featuretree.workflow.planning import work_order


def accepted_tree(root, folder, state):
    if not all(t["status"] == "succeeded" for t in state["tasks"].values()):
        raise ValueError("Every stage, including global integration, must succeed before publication")
    snapshot = snapshot_for(folder, state)
    for task in state["tasks"].values():
        result = artifact(folder, task)
        packet = read_json(folder / task["result_path"].replace("result.json", "input.json"))
        if digest({k: v for k, v in packet.items() if k != "input_hash"}) != packet["input_hash"]:
            raise ValueError("Attempt input changed")
        if result["input_hash"] != packet["input_hash"]:
            raise ValueError("Output no longer matches its attempt")
        if task["stage"] != "anchors":
            validate_result(root, packet, result)
    merged = deepcopy(snapshot["features"])
    for node in state["nodes"]:
        inputs = node_inputs(folder, state, node)
        proposal = inputs["synthesize"]
        validate_proposal(root, snapshot, work_order(snapshot, state, node), proposal,
                          [inputs[p] for p in PLATFORMS])
        statuses = {r["id"]: r["anchor_status"] for r in inputs["anchors"]["results"]}
        for feature in proposal["nodes"]:
            if feature["id"] in merged:
                raise ValueError("Cross-work-order duplicate ID")
            feature = deepcopy(feature)
            feature["anchor_status"] = statuses[feature["id"]]
            merged[feature["id"]] = feature
    return snapshot, merged


def report(root, run_id):
    folder, state = load_run(root, run_id)
    snapshot = snapshot_for(folder, state)
    tasks = list(state["tasks"].values())
    statuses = {s: sum(t["status"] == s for t in tasks)
                for s in ("pending", "running", "succeeded", "failed", "blocked")}
    additions = [n for t in tasks if t["stage"] == "synthesize" and t["status"] == "succeeded"
                 for n in artifact(folder, t)["payload"]["nodes"]]
    anchors = [r for t in tasks if t["stage"] == "anchors" and t["status"] == "succeeded"
               for r in artifact(folder, t)["payload"]["results"]]
    issues = {t["id"]: artifact(folder, t)["payload"] for t in tasks if t["status"] == "blocked"}
    errors = {t["id"]: t["attempts"][-1].get("error") for t in tasks if t["status"] == "failed"}
    gaps = {t["id"]: artifact(folder, t)["payload"].get("gaps", []) for t in tasks
            if t["status"] == "succeeded" and t["stage"] in (*PLATFORMS, "synthesize")}
    deferred = [d for t in tasks if t["stage"] == "synthesize" and t["status"] == "succeeded"
                for d in artifact(folder, t)["payload"]["dispositions"] if d["decision"] == "deferred"]
    result = {"run_id": run_id, "state_counts": statuses, "additions": counts(additions),
              "total_tree": counts([*snapshot["features"].values(), *additions]),
              "baseline_unverified": [p for p in PLATFORMS if snapshot["baseline"]["platforms"][p]["status"] != "verified"],
              "anchor_counts": {s: sum(r["anchor_status"] == s for r in anchors)
                                for s in ("failed", "url_ok", "body_ok", "symbol_ok")},
              "attempts": sum(len(t["attempts"]) for t in tasks), "revisions": state["revisions"],
              "research_gaps": gaps, "deferred_candidates": deferred,
              "usage": {t["id"]: [a.get("metadata", {}) for a in t["attempts"]] for t in tasks},
              "errors": errors, "rejected_reviews": issues, "published": state.get("published"),
              "ready_to_publish": all(t["status"] == "succeeded" for t in tasks),
              "tree_frozen": False, "coverage": "Not measured by task or node counts"}
    if result["ready_to_publish"]:
        accepted_tree(root, folder, state)
    write_json(folder / "report.json", result)
    return result


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def yaml_text(value):
    return yaml.safe_dump(value, allow_unicode=True, sort_keys=False, width=100)


def prepare_journal(root, folder, state):
    root = root.resolve()
    snapshot, merged = accepted_tree(root, folder, state)
    current_files = {str(p.relative_to(root)): p.read_text() for p in (root / "taxonomy").glob("*.yaml")}
    if current_files != snapshot["tree_files"]:
        raise ValueError("Taxonomy changed since planning; create a new plan and repeat reviews")
    repo = Repository(root)
    targets = {}
    changed_domains = {n.split(".")[0] for n in state["nodes"]}
    for domain in changed_domains:
        path = root / "taxonomy" / f"{domain}.yaml"
        doc = read_yaml(path)
        doc["features"] = sorted([f for f in merged.values() if f["id"].split(".")[0] == domain],
                                 key=lambda f: (int(f["level"][1:]), f["id"]))
        targets[path] = yaml_text(doc)
    for fid, feature in merged.items():
        path = contained_path(root, feature["knowledge_path"], "knowledge")
        if fid not in snapshot["features"] and path.exists():
            raise ValueError(f"New knowledge path already exists: {path}")
        if path.exists():
            doc = read_yaml(path)
            if doc["feature_id"] != fid:
                raise ValueError("Existing knowledge subject mismatch")
        else:
            doc = new_knowledge(feature, repo.config()["platforms"])
        before = deepcopy(doc)
        if feature["knowledge_role"] == "rollup":
            doc["child_index"] = sorted(n["id"] for n in merged.values() if n["parent"] == fid)
        if not path.exists() or doc != before:
            targets[path] = yaml_text(doc)
    files = []
    for path, after in sorted(targets.items()):
        before = path.read_text() if path.exists() else None
        if before == after:
            continue
        files.append({"path": str(path.relative_to(root)), "before": before, "after": after,
                      "before_hash": file_hash(path), "after_hash": hashlib.sha256(after.encode()).hexdigest()})
    return {"run_id": state["id"], "prepared_at": now(), "tree_hash": digest(merged), "files": files}


def apply_journal(root, journal):
    # Preflight every file before writing any, including interrupted transactions.
    for entry in journal["files"]:
        directory = entry["path"].split("/")[0]
        if directory not in ("taxonomy", "knowledge"):
            raise ValueError("Publication journal path outside owned data")
        path = contained_path(root, entry["path"], directory)
        if file_hash(path) not in (entry["before_hash"], entry["after_hash"]):
            raise ValueError(f"Publication conflict: {entry['path']}")
    for entry in journal["files"]:
        path = root / entry["path"]
        if file_hash(path) == entry["after_hash"]:
            continue
        # Detect an external editor racing after the preflight.
        if file_hash(path) != entry["before_hash"]:
            raise ValueError(f"Publication conflict: {entry['path']}")
        write_text(path, entry["after"])


def publish(root, run_id):
    root = root.resolve()
    folder = run_path(root, run_id)
    with lock(root / ".workflow/publish.lock"), lock(folder / "run.lock"):
        folder, state = load_run(root, run_id)
        if state.get("published"):
            return state["published"]
        path = folder / "publication.json"
        if path.exists():
            journal = read_json(path)
            if state.get("publication_hash") != digest(journal):
                raise ValueError("Publication journal changed")
        else:
            journal = prepare_journal(root, folder, state)
            # Persist the identity first, then the journal. No source writes until both exist.
            state["publication_hash"] = digest(journal)
            save_state(folder, state)
            write_json(path, journal)
        apply_journal(root, journal)
        state["published"] = {"at": now(), "tree_hash": journal["tree_hash"], "files": len(journal["files"])}
        save_state(folder, state)
        return state["published"]
