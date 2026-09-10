"""Directed invalidation retains every old artifact and attempt."""

from featuretree.core.io import ConflictError


def revise_tasks(state, registry, pipeline, work_id, target_stage, feedback):
    if target_stage not in registry.pipelines[pipeline]:
        raise ValueError("Revision target is outside this pipeline; create a linked structure/source revision")
    affected = [target_stage, *registry.descendants(target_stage, pipeline)]
    global_stages = {key for key in affected if registry.stages[key].dependency_scope == "run"}
    global_stages |= {key for key in affected if registry.ancestors(key) & global_stages}
    tasks = [task for task in state["tasks"].values() if task["stage_id"] in affected
             and (task["work_id"] == work_id or task["stage_id"] in global_stages)]
    if any(task["status"] == "running" for task in tasks):
        raise ConflictError("An affected local or integration stage is still running; retry revision after it stops")
    for task in tasks:
        stage_id = task["stage_id"]
        if task["result_ref"]:
            task["history"].append({"result_ref": task["result_ref"], "revision": task["revision"]})
        task.update(status="waiting", result_ref=None, outcome=None, revision=task["revision"] + 1)
        if stage_id == target_stage:
            task["feedback"] = feedback
    return [task["id"] for task in tasks]
