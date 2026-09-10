"""Directed invalidation retains every old artifact and attempt."""


def revise_tasks(state, registry, pipeline, work_id, target_stage, feedback):
    if target_stage not in registry.pipelines[pipeline]:
        raise ValueError("Revision target is outside this pipeline; create a linked structure/source revision")
    affected = [target_stage, *registry.descendants(target_stage, pipeline)]
    for stage_id in affected:
        task = state["tasks"][work_id + "--" + stage_id]
        if task["result_ref"]:
            task["history"].append({"result_ref": task["result_ref"], "revision": task["revision"]})
        task.update(status="waiting", result_ref=None, outcome=None, revision=task["revision"] + 1)
        if stage_id == target_stage:
            task["feedback"] = feedback
    return affected
