"""Read-only run projections for the management console, including stale runs."""

import fcntl

from featuretree.workflow.state import artifact, read_json, run_path
from featuretree.workflow.gates import counts
from featuretree.workflow.backends.processes import identity


def active_process(folder):
    marker = folder / "console-process.json"
    if marker.exists():
        record = read_json(marker)
        if record.get("identity") and identity(record["pid"]) == record["identity"]:
            return True
    path = folder / "run.lock"
    if not path.exists():
        return False
    with path.open() as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_SH | fcntl.LOCK_NB)
            fcntl.flock(stream, fcntl.LOCK_UN)
        except BlockingIOError:
            return True
    return False


def read_state(root, run_id):
    folder = run_path(root, run_id)
    state = read_json(folder / "state.json")
    if state["root"] != str(root):
        raise ValueError("任务属于另一个项目")
    return folder, state


def summarize(folder, state, current_rules, active):
    tasks = list(state["tasks"].values())
    statuses = {s: sum(t["status"] == s for t in tasks)
                for s in ("pending", "running", "succeeded", "failed", "blocked")}
    complete = bool(tasks) and statuses["succeeded"] == len(tasks)
    publication_started = (folder / "publication.json").exists()
    status = ("published" if state.get("published") else "running" if active else
              "publishing_interrupted" if publication_started else "completed" if complete else
              "blocked" if statuses["blocked"] else "failed" if statuses["failed"] else
              "interrupted" if statuses["running"] else "planned")
    fresh = state["rule_hash"] == current_rules
    mutable = fresh and not active and not state.get("published")
    return {"id": state["id"], "nodes": state["nodes"], "created_at": state["created_at"],
            "status": status, "active": active, "stale_rules": not fresh, "state_counts": statuses,
            "total_tasks": len(tasks), "trigger": state.get("trigger"), "depth": state["depth"],
            "workers": state["workers"], "max_nodes": state["max_nodes"], "model": state["model"],
            "actions": {"start": mutable and status in ("planned", "interrupted"),
                        "retry": mutable and status == "failed" and not publication_started,
                        "revise": mutable and status == "blocked" and all(
                            state["revisions"][n] < state["max_revisions"] for n in state["nodes"]),
                        "publish": mutable and status in ("completed", "publishing_interrupted")}}


def details(folder, state, summary):
    snapshot = read_json(folder / "snapshot.json")
    tasks = []
    additions = []
    for task in state["tasks"].values():
        payload, error = None, None
        if task.get("result_path") and task["status"] in ("succeeded", "blocked"):
            try:
                payload = artifact(folder, task)["payload"]
            except (ValueError, OSError) as exc:
                error = str(exc)
        if task["stage"] == "synthesize" and payload:
            additions.extend(payload["nodes"])
        tasks.append({"id": task["id"], "node": task["node"], "stage": task["stage"],
                      "status": task["status"], "attempts": task["attempts"],
                      "payload": payload, "artifact_error": error})
    marker = folder / "console-error.json"
    return {**summary, "tasks": tasks, "baseline": snapshot["baseline"],
            "additions": counts(additions), "nodes_proposed": additions,
            "execution_error": read_json(marker).get("error") if marker.exists() else None,
            "published": state.get("published")}
