"""Read-only run projections for the management console, including stale runs."""

import fcntl

from featuretree.workflow.state import artifact, read_json, run_path
from featuretree.workflow.gates import counts
from featuretree.workflow.backends.processes import identity
from featuretree.workflow.metrics import execution_metrics, task_metrics
from featuretree.workflow.api_inventory import assess_allocations
from featuretree.workflow.packets import node_inputs
from featuretree.workflow.stages import PLATFORMS


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
            "workers": state["workers"], "timeout": state["timeout"], "max_nodes": state["max_nodes"], "model": state["model"],
            "metrics": execution_metrics(state, active),
            "first_response_timeout": state.get("first_response_timeout"),
            "actions": {"start": mutable and status in ("planned", "interrupted"),
                        "retry": mutable and status == "failed" and not publication_started,
                        "revise": mutable and status == "blocked" and all(
                            state["revisions"][n] < state["max_revisions"] for n in state["nodes"]),
                        "publish": mutable and status in ("completed", "publishing_interrupted")}}


def details(folder, state, summary):
    snapshot = read_json(folder / "snapshot.json")
    tasks = []
    additions = []
    assessments = []
    for task in state["tasks"].values():
        payload, error = None, None
        if task.get("result_path") and task["status"] in ("succeeded", "blocked"):
            try:
                payload = artifact(folder, task)["payload"]
            except (ValueError, OSError) as exc:
                error = str(exc)
        if task["stage"] == "synthesize" and payload:
            additions.extend(payload["nodes"])
            if "api_allocations" in payload:
                inputs = node_inputs(folder, state, task["node"])
                assessments.extend(assess_allocations(payload, [inputs[p] for p in PLATFORMS]))
        tasks.append({"id": task["id"], "node": task["node"], "stage": task["stage"],
                      "status": task["status"], "attempts": task["attempts"],
                      "metrics": task_metrics(task, summary["active"]),
                      "payload": payload, "artifact_error": error})
    marker = folder / "console-error.json"
    return {**summary, "tasks": tasks, "baseline": snapshot["baseline"],
            "additions": counts([n for n in additions if n["id"] not in snapshot["features"]]),
            "updated_nodes": [n["id"] for n in additions if n["id"] in snapshot["features"]],
            "nodes_proposed": additions, "api_assessments": assessments,
            "next_work_orders": [r for r in assessments if r["next_action"] == "analyze"],
            "execution_error": read_json(marker).get("error") if marker.exists() else None,
            "published": state.get("published")}
