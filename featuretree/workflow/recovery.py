"""Retry failed stages and revise rejected candidates under the run lock."""

from featuretree.workflow.state import artifact, load_run, lock, run_path, save_state
from featuretree.workflow.stages import PLATFORMS


def upstream_stages(feedback, node):
    stages = set()
    for review in feedback.values():
        for issue in review["issues"]:
            owner = issue.get("node_id")
            target = issue.get("target_stage")
            if (issue["severity"] == "blocking" and target in PLATFORMS
                    and (owner is None or owner == node or owner.startswith(node + "."))):
                stages.add(target)
    return stages


def reset_tasks(root, run_id, nodes=None):
    folder = run_path(root, run_id)
    with lock(folder / "run.lock"):
        folder, state = load_run(root, run_id)
        if state.get("published") or (folder / "publication.json").exists():
            raise ValueError("Cannot revise or retry a publishing/published run")
        if nodes is None:
            for task in state["tasks"].values():
                if task["status"] == "failed":
                    task.update(status="pending", allowance=len(task["attempts"]) + state["max_attempts"])
        else:
            if not nodes or len(set(nodes)) != len(nodes) or not set(nodes) <= set(state["nodes"]):
                raise ValueError("Select unique nodes in this run")
            if any(state["revisions"][n] >= state["max_revisions"] for n in nodes):
                raise ValueError("Revision limit reached; create a more focused plan")
            feedback = {t["id"]: artifact(folder, t)["payload"] for t in state["tasks"].values()
                        if t["status"] == "blocked"}
            if not feedback:
                raise ValueError("No rejected review to revise; use retry for execution failures")
            for n in nodes:
                state["revisions"][n] += 1
                synth = state["tasks"][f"{n}/synthesize"]
                synth["feedback"] = {"reviews": feedback, "previous_proposal": artifact(folder, synth)["payload"]}
                upstream = upstream_stages(feedback, n)
                for stage in upstream:
                    task = state["tasks"][f"{n}/{stage}"]
                    task["feedback"] = {"reviews": feedback, "previous_result": artifact(folder, task)["payload"]}
                for stage in (*sorted(upstream), *(("scope",) if upstream else ()), "synthesize", "review", "anchors"):
                    task = state["tasks"][f"{n}/{stage}"]
                    task.update(status="pending", allowance=len(task["attempts"]) + state["max_attempts"])
            task = state["tasks"]["batch/integrate"]
            task.update(status="pending", allowance=len(task["attempts"]) + state["max_attempts"])
        save_state(folder, state)
        return state
