"""Versioned replanning reuses only compatible accepted deliveries, with origin receipts."""

from copy import deepcopy
from jsonschema import Draft202012Validator

from featuretree.core.io import ConflictError, file_lock, read_json, write_json
from featuretree.workflow.packaging import build_packet, envelope
from featuretree.workflow.registry import PipelineRegistry


class ReplanService:
    def __init__(self, planner, runs, artifacts, handlers, provenance):
        self.planner, self.runs, self.artifacts = planner, runs, artifacts
        self.handlers, self.provenance = handlers, provenance

    def create(self, run_id, request, key):
        original, original_state = self.runs.load(run_id)
        fresh = set(request.get("fresh_stages", []))
        if not fresh or not fresh <= set(original["pipeline_stages"]):
            raise ValueError("Replanning must identify registered stages requiring new deliveries")
        reason = request.get("reason", "")
        if not reason:
            raise ValueError("An explicit compatibility/revision reason is required")
        scopes = [{"definition": work["scope"], "snapshot_id": work["snapshot_id"],
            "selection": {"ids": work["api_ids"]}, "topic_selection": {"ids": work["topic_ids"]},
            "scope_root_ids": work.get("scope_root_ids", []), "inputs": work["inputs"],
            "mode": work["mode"], "work_type": work["work_type"], "source_round": work.get("source_round", 0),
            "enumeration_complete": work["enumeration_complete"],
            "revision_of": {"run_id": run_id, "work_id": work["id"], "reason": reason}} for work in original["works"]]
        new_request = {"pipeline": original["pipeline"], "model": request.get("model", original["model"]),
                       "variant": request.get("variant", original["variant"]),
                       "budget": {**original["budget"], **request.get("budget", {})}, "scopes": scopes,
                       "reuse_request": request, "parent_run_id": run_id}
        state = self.planner.create(new_request, key)
        folder = self.runs.folder(state["run_id"])
        with file_lock(folder / "run.lock", blocking=False):
            plan, state = self.runs.load(state["run_id"])
            if state.get("replan_initialized"):
                return state
            if state["status"] != "planned" or any(task["attempts"] for task in state["tasks"].values()):
                raise ConflictError("Replacement run started before compatibility initialization")
            registry = PipelineRegistry(plan["registry"])
            excluded = fresh | {child for stage in fresh for child in registry.descendants(stage, plan["pipeline"])}
            for work in plan["works"]:
                identity_path = self.runs.folder(run_id) / f"{work['id']}-identities.json"
                if identity_path.exists():
                    identities = read_json(identity_path)
                    write_json(folder / identity_path.name, identities)
                    state.setdefault("inherited_identity_refs", {})[work["id"]] = self.artifacts.put(identities)
                for stage in plan["pipeline_stages"]:
                    task = state["tasks"][work["id"] + "--" + stage]
                    if task.get("reuse_ref"):
                        continue
                    prior = original_state["tasks"].get(task["id"])
                    if stage in fresh:
                        feedback = {"origin": "versioned_replan", "reason": reason}
                        retained = prior.get("result_ref") if prior else None
                        if not retained and prior:
                            retained = next((row.get("result_ref") for row in reversed(prior["attempts"]) if row["status"] == "success"), None)
                        if retained:
                            feedback["retained_response_ref"] = retained
                        if feedback not in task["feedback"]:
                            task["feedback"].append(feedback)
                    if stage in excluded or not prior or prior["status"] != "completed" or prior["outcome"] not in ("pass", "completed_with_gaps"):
                        continue
                    before, after = original["stage_configs"][stage], plan["stage_configs"][stage]
                    if before["fingerprint"] != after["fingerprint"]:
                        continue
                    pinned = before.get("implementation_files", {})
                    if pinned != after["implementation_files"] and not (not pinned and work["mode"] == "calibration"
                                                                         and request.get("allow_unpinned_calibration") is True):
                        continue
                    response, source_packet = self.provenance.require(prior["result_ref"], stage)
                    try:
                        packet = build_packet(plan, task, state, registry, self.artifacts)
                    except (ValueError, KeyError):
                        continue
                    if packet["upstream_refs"] != source_packet["upstream_refs"]:
                        continue
                    checked = envelope(packet, deepcopy(response["payload"]), response["outcome"], response["issues"])
                    checked["source_requests"] = response["source_requests"]
                    Draft202012Validator(packet["output_schema"]).validate(checked)
                    self.handlers.validate(stage, checked, packet)
                    receipt = {"origin_run_id": response["run_id"], "origin_task_id": response["task_id"],
                        "result_ref": prior["result_ref"], "new_input_hash": packet["input_hash"],
                        "reason": reason, "compatibility": "same_scope_source_rules_and_upstream; current_machine_validation_passed",
                        "unpinned_calibration_input": not bool(pinned)}
                    task.update(status="completed", outcome=prior["outcome"], result_ref=prior["result_ref"])
                    task["reuse_ref"] = self.artifacts.put(receipt)
                    self.runs.event(state, "artifact_reused", {"task_id": task["id"], **receipt})
            state["replan_initialized"] = True
            self.runs.event(state, "replan_initialized", {"parent_run_id": run_id, "fresh_stages": sorted(fresh), "reason": reason})
            return state
