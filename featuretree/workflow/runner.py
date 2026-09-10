"""Generic DAG scheduling; semantic checks and code stages live behind handlers."""

from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
import json

from featuretree.core.content import digest, file_digest, timestamp
from featuretree.core.io import ConflictError, IntegrityError, file_lock, read_json, write_json
from featuretree.workflow.backends.processes import terminate_recorded
from featuretree.workflow.backends.errors import SemanticValidationError
from featuretree.workflow.packaging import build_packet
from featuretree.workflow.registry import PipelineRegistry
from featuretree.workflow.revisions import revise_tasks


class Runner:
    def __init__(self, runs, artifacts, executor):
        self.runs, self.artifacts, self.executor = runs, artifacts, executor

    def run(self, run_id):
        folder = self.runs.folder(run_id)
        with file_lock(folder / "run.lock", blocking=False):
            plan, state = self.runs.load(run_id)
            registry = PipelineRegistry(plan["registry"])
            if state["status"] in ("cancelled", "published"):
                return state
            self._recover_orphans(state, folder)
            state["status"] = "running"
            self.runs.event(state, "run_started", {})
            futures = {}
            with ThreadPoolExecutor(plan["budget"]["workers"]) as pool:
                while True:
                    if (folder / "CANCEL.json").exists():
                        for task in state["tasks"].values():
                            if task["status"] == "running":
                                terminate_recorded(folder / task["attempts"][-1]["folder"] / "process.json")
                        if not futures:
                            state["status"] = "cancelled"
                            break
                    else:
                        for task in state["tasks"].values():
                            if len(futures) >= plan["budget"]["workers"]:
                                break
                            if self._ready(task, state, registry):
                                try:
                                    packet = build_packet(plan, task, state, registry, self.artifacts)
                                    self._repair_input(task, packet, folder)
                                except (ValueError, KeyError, OSError) as error:
                                    task["status"] = "blocked"
                                    task["feedback"].append({"reason": str(error), "origin": "input_validation"})
                                    self.runs.event(state, "input_rejected", {"task_id": task["id"], "reason": str(error)})
                                    continue
                                attempt = {"number": len(task["attempts"]) + 1, "revision": task["revision"],
                                           "status": "running", "started_at": timestamp()}
                                attempt["folder"] = f"attempts/{task['id']}/{attempt['number']:04d}"
                                task["attempts"].append(attempt)
                                task["status"] = "running"
                                self.runs.event(state, "attempt_started", {"task_id": task["id"], **attempt})
                                future = pool.submit(self.executor.execute, plan, task.copy(), packet,
                                                     folder / attempt["folder"])
                                futures[future] = task["id"]
                    if not futures:
                        state["status"] = self._run_status(state, plan)
                        break
                    completed, _ = wait(futures, timeout=0.3, return_when=FIRST_COMPLETED)
                    for future in completed:
                        task = state["tasks"][futures.pop(future)]
                        self._finish(future, task, state, plan, registry, folder)
            self.runs.event(state, "run_stopped", {"status": state["status"]})
            return state

    def _ready(self, task, state, registry):
        if task["status"] not in ("waiting", "ready"):
            return False
        stage = registry.stages[task["stage_id"]]
        for dependency in stage.dependencies:
            relevant = [row for row in state["tasks"].values() if row["stage_id"] == dependency
                        and (stage.dependency_scope == "run" or row["work_id"] == task["work_id"])]
            for upstream in relevant:
                if upstream["status"] != "completed" or upstream["outcome"] in ("needs_sources", "revise"):
                    return False
                if upstream["outcome"] == "completed_with_gaps" and not stage.accepts_gaps:
                    return False
        return True

    def _finish(self, future, task, state, plan, registry, folder):
        attempt = task["attempts"][-1]
        attempt["finished_at"] = timestamp()
        try:
            reference, metadata = future.result()
            if (folder / "CANCEL.json").exists():
                attempt["status"], task["status"] = "cancelled", "blocked"
                return
            response = self.artifacts.get(reference)
            attempt.update(status="success", result_ref=reference, metadata=metadata)
            task.update(status="completed", result_ref=reference, outcome=response["outcome"])
            self.runs.event(state, "artifact_accepted", {"task_id": task["id"], "reference": reference,
                                                        "outcome": response["outcome"]})
            if response["outcome"] == "revise":
                issues = response["issues"]
                targets = {issue["target_stage"] for issue in issues if issue["severity"] == "blocking"}
                if not targets:
                    task["status"] = "blocked"
                for target in targets:
                    key = task["work_id"] + "--" + target
                    rounds = state["semantic_rounds"].get(key, 0)
                    if target not in plan["pipeline_stages"] or rounds >= plan["budget"]["max_semantic_rounds"]:
                        task["status"] = "blocked"
                        continue
                    if any(other["status"] == "running" and other["work_id"] == task["work_id"]
                           for other in state["tasks"].values()):
                        task["status"] = "blocked"
                        continue  # Do not invalidate an in-flight sibling; explicit revision resumes safely.
                    state["semantic_rounds"][key] = rounds + 1
                    affected = revise_tasks(state, registry, plan["pipeline"], task["work_id"], target, issues)
                    self.runs.event(state, "semantic_revision", {"target": target, "affected": affected})
        except Exception as error:
            metadata_path = folder / attempt["folder"] / "metadata.json"
            attempt.update(status="failed", error=str(error), error_type=type(error).__name__,
                           metadata=getattr(error, "metadata", None) or (read_json(metadata_path) if metadata_path.exists() else {}))
            task["status"] = "failed"
            retained = folder / attempt["folder"] / "response.json"
            if retained.exists():
                attempt["response_sha256"] = file_digest(retained)
            attempts = sum(row["revision"] == task["revision"] for row in task["attempts"])
            if getattr(error, "retryable", False) and attempts < plan["budget"]["max_attempts"]:
                task["status"] = "ready"
            if isinstance(error, SemanticValidationError):
                self._semantic_failure(error, task, state, plan, registry)
            self.runs.event(state, "attempt_failed", {"task_id": task["id"], "error": str(error),
                                                      "retry_scheduled": task["status"] == "ready"})
        finally:
            self.runs.save(state)

    def _semantic_failure(self, error, task, state, plan, registry):
        key = task["work_id"] + "--" + error.target_stage
        rounds = state["semantic_rounds"].get(key, 0)
        if error.target_stage not in plan["pipeline_stages"] or rounds >= plan["budget"]["max_semantic_rounds"]:
            return
        feedback = [{"reason": str(error), "origin": "machine_validation", "retained_response_ref": error.retained_ref}]
        try:
            affected = revise_tasks(state, registry, plan["pipeline"], task["work_id"], error.target_stage, feedback)
        except (ValueError, OSError):
            return  # An in-flight dependent must finish before explicit revision.
        state["semantic_rounds"][key] = rounds + 1
        self.runs.event(state, "machine_revision", {"target": key, "affected": affected, "reason": str(error)})

    def _repair_input(self, task, packet, folder):
        if not task["attempts"]:
            return
        previous = task["attempts"][-1]
        if previous.get("error_type") != "ResponseFormatError" or previous["revision"] != task["revision"]:
            return
        response_path = folder / previous["folder"] / "response.json"
        if response_path.exists():
            if file_digest(response_path) != previous.get("response_sha256"):
                raise IntegrityError("Retained response changed; format repair refused")
            packet.pop("input_hash")
            packet["response_repair"] = {"text": response_path.read_text(), "error": previous["error"],
                                         "source_attempt": previous["number"]}
            packet["input_hash"] = digest(packet)

    def _recover_orphans(self, state, folder):
        for task in state["tasks"].values():
            if task["status"] == "running":
                attempt = task["attempts"][-1]
                terminate_recorded(folder / attempt["folder"] / "process.json")
                attempt.update(status="interrupted", finished_at=timestamp())
                task["status"] = "failed"
                self.runs.event(state, "orphan_recovered", {"task_id": task["id"]})

    @staticmethod
    def _run_status(state, plan):
        tasks = list(state["tasks"].values())
        if any(task["outcome"] == "needs_sources" for task in tasks):
            return "waiting_sources"
        if any(task["status"] in ("failed", "blocked") or task["outcome"] == "revise" for task in tasks):
            return "waiting_revision"
        if all(task["status"] == "completed" for task in tasks):
            if plan["pipeline"] == "taxonomy" or any(work["mode"] == "calibration" for work in plan["works"]):
                return "waiting_human"
            return "ready_to_publish"
        return "waiting_revision"

    def action(self, run_id, action, *, task_id=None, feedback=()):
        folder = self.runs.folder(run_id)
        if action == "cancel":
            write_json(folder / "CANCEL.json", {"requested_at": timestamp()})
            try:
                with file_lock(folder / "run.lock", blocking=False):
                    _, state = self.runs.load(run_id)
                    if state["status"] != "published":
                        state["status"] = "cancelled"
                        self.runs.event(state, "run_cancelled", {})
                    return state
            except ConflictError:
                pass
            return {"run_id": run_id, "action": "cancel_requested"}
        with file_lock(folder / "run.lock", blocking=False):
            plan, state = self.runs.load(run_id)
            registry = PipelineRegistry(plan["registry"])
            if task_id not in state["tasks"]:
                raise ValueError("A valid task_id is required")
            task = state["tasks"][task_id]
            if action == "revalidate":
                return self._revalidate(plan, state, task, folder)
            if action == "retry" and task["status"] != "failed":
                raise ValueError("Only failed execution can be retried")
            if action not in ("retry", "revise"):
                raise ValueError("Unknown run action")
            affected = revise_tasks(state, registry, plan["pipeline"], task["work_id"], task["stage_id"], list(feedback))
            state["status"] = "planned"
            self.runs.event(state, action, {"target": task_id, "affected": affected})
            return state

    def _revalidate(self, plan, state, task, folder):
        if task["status"] != "failed" or not task["attempts"]:
            raise ValueError("Only a failed retained complete delivery can be revalidated")
        attempt = task["attempts"][-1]
        directory = folder / attempt["folder"]
        response_path = directory / "model-response.json"
        if not response_path.exists():
            response_path = directory / "response.json"
        if not response_path.exists() or file_digest(response_path) != attempt.get("response_sha256"):
            raise IntegrityError("Retained delivery changed or is absent")
        packet = read_json(directory / "input.json")
        if digest({key: value for key, value in packet.items() if key != "input_hash"}) != packet["input_hash"]:
            raise IntegrityError("Retained delivery inputs were modified")
        response = read_json(response_path)
        write_json(directory / "model-response.json", response, immutable=True)
        previous = {key: attempt[key] for key in ("status", "error", "error_type") if key in attempt}
        reference, metadata = self.executor.accept_response(plan, task, packet, response,
                        dict(attempt.get("metadata", {})), directory)
        attempt.setdefault("validation_history", []).append(previous)
        attempt.update(status="success", result_ref=reference, metadata=metadata)
        task.update(status="completed", outcome=self.artifacts.get(reference)["outcome"], result_ref=reference)
        state["status"] = "planned"
        self.runs.event(state, "retained_delivery_revalidated", {"task_id": task["id"], "reference": reference,
                                                               "issue_route_adjustments": metadata["issue_route_adjustments"]})
        return state
