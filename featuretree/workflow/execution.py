"""One isolated attempt, bounded by project capacity and immutable packet configuration."""

from contextlib import contextmanager
from copy import deepcopy
import json
import time

from jsonschema import Draft202012Validator

from featuretree.core.content import canonical_bytes, digest
from featuretree.core.io import ConflictError, IntegrityError, file_lock, write_bytes, write_json
from featuretree.workflow.backends.errors import ResponseFormatError, SemanticValidationError
from featuretree.workflow.implementation import verify_implementation
from featuretree.workflow.attempt_tools import delivery_adapter
from featuretree.workflow.batch_packets import research_batches
from featuretree.workflow.batch_execution import BatchExecutor


@contextmanager
def capacity_slot(directory, timeout):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        for number in range(6):
            lock = file_lock(directory / f"slot-{number}.lock", blocking=False)
            try:
                lock.__enter__()
            except ConflictError:
                continue
            try:
                yield number
            finally:
                lock.__exit__(None, None, None)
            return
        time.sleep(0.1)
    raise TimeoutError("Project capacity budget exhausted before execution")


class AttemptExecutor:
    def __init__(self, root, artifacts, backend, handlers):
        self.root, self.artifacts, self.backend, self.handlers = root, artifacts, backend, handlers

    def execute(self, plan, task, packet, folder):
        verify_implementation(task["stage_id"], plan["stage_configs"][task["stage_id"]].get("implementation_files"))
        batches = research_batches(packet)
        if not batches:
            return self._execute_single(plan, task, packet, folder)
        folder.mkdir(parents=True, exist_ok=True)
        write_json(folder / "input.json", packet, immutable=True)
        started = time.monotonic()
        response, metadata = BatchExecutor(self.artifacts, self.handlers, self._execute_single).execute(
            plan, task, packet, batches, folder)
        write_json(folder / "model-response.json", response, immutable=True)
        return self.accept_response(plan, task, packet, response, metadata, folder, started)

    def _execute_single(self, plan, task, packet, folder):
        folder.mkdir(parents=True, exist_ok=True)
        write_json(folder / "input.json", packet, immutable=True)
        if len(canonical_bytes(packet).decode("utf-8")) > plan["budget"]["max_input_characters"]:
            raise ValueError("Complete input exceeds context budget; replan into bounded scopes. No IDs were truncated.")
        stage = plan["stage_configs"][task["stage_id"]]
        verify_implementation(task["stage_id"], stage.get("implementation_files"))
        if packet["work"]["mode"] == "formal" and not stage.get("implementation_files"):
            raise ConflictError("Formal execution requires a pinned executable fingerprint")
        started = time.monotonic()
        definition = stage["definition"]
        if definition["agent_name"]:
            workspace = folder / "workspace"
            agent_file = workspace / ".opencode/agents" / (definition["agent_name"] + ".md")
            write_bytes(agent_file, stage["agent_text"].encode(), immutable=True)
            write_bytes(workspace / ".opencode/tools/source_catalog.ts",
                        self._source_tool().encode(), immutable=True)
            write_bytes(workspace / ".opencode/tools/submit_payload.ts",
                        delivery_adapter(self.root).encode(), immutable=True)
            write_bytes(workspace / ".opencode/tools/finish_payload.ts",
                        delivery_adapter(self.root, finalize=True).encode(), immutable=True)
            write_json(workspace / "task.json", packet, immutable=True)
            with capacity_slot(self.root / ".workflow/v2/capacity", packet["limits"]["timeout_seconds"]):
                response, metadata = self.backend.execute(
                    workspace, definition["agent_name"], packet, folder,
                    packet["limits"]["timeout_seconds"], plan["model"], plan["variant"])
        else:
            response = self.handlers.execute(definition["executor"], packet, folder)
            metadata = {"executor": definition["executor"], "model": None, "usage": []}
        write_json(folder / "model-response.json", response, immutable=True)
        write_json(folder / "response.json", response)
        return self.accept_response(plan, task, packet, response, metadata, folder, started)

    def accept_response(self, plan, task, packet, response, metadata, folder, started=None):
        verify_implementation(task["stage_id"], plan["stage_configs"][task["stage_id"]].get("implementation_files"))
        response = deepcopy(response)
        adjustments = []
        for issue in response.get("issues", []):
            target = plan["registry"]["issue_routes"].get(issue["kind"])
            if target and issue["target_stage"] != target:
                adjustments.append({"issue_id": issue["id"], "submitted_target": issue["target_stage"], "resolved_target": target})
                issue["target_stage"] = target
        metadata["issue_route_adjustments"] = adjustments
        metadata.update(elapsed_seconds=round(time.monotonic() - started, 3) if started else metadata.get("elapsed_seconds"),
                        input_hash=packet["input_hash"], stage_fingerprint=packet["stage_fingerprint"],
                        implementation_files=plan["stage_configs"][task["stage_id"]].get("implementation_files", {}),
                        validation="pending")
        write_json(folder / "metadata.json", metadata)
        errors = list(Draft202012Validator(packet["output_schema"]).iter_errors(response))
        if errors:
            raise ResponseFormatError("Response schema: " + "; ".join(error.message for error in errors[:8]))
        for key in ("protocol_version", "run_id", "work_id", "task_id", "stage_id", "input_hash"):
            if response[key] != packet[key]:
                raise ValueError(f"Response envelope does not match fixed {key}")
        try:
            self.handlers.validate(task["stage_id"], response, packet)
        except (ConflictError, IntegrityError):
            raise
        except ValueError as error:
            target = plan["stage_configs"][task["stage_id"]]["definition"].get("validation_failure_target") or task["stage_id"]
            raise SemanticValidationError(target, str(error), self.artifacts.put(response)) from error
        metadata["validation"] = "accepted"
        write_json(folder / "response.json", response)
        write_json(folder / "metadata.json", metadata)
        return self.artifacts.put(response), metadata

    def _source_tool(self):
        python = str(self.root / ".venv/bin/python")
        project = str(self.root)
        return '''import { tool } from "@opencode-ai/plugin";
import { spawn } from "node:child_process";
export default tool({
  description: "Read the fixed source snapshot. apis/topics enumerate only authorized IDs; documents search official records. body returns a verified window; body with query finds bounded matching excerpts with offsets. Preserve document id and body hash for evidence_refs. Pages are stable; use next_cursor/next_offset.",
  args: { operation: tool.schema.enum(["apis","topics","documents","body"]),
    query: tool.schema.string().optional(), id: tool.schema.string().optional(),
    cursor: tool.schema.string().optional(), offset: tool.schema.number().optional(),
    limit: tool.schema.number().optional() },
  async execute(args, context) {
    if (!process.env.FEATURETREE_PACKET) throw new Error("No pinned FeatureTree packet");
    return await new Promise((resolve, reject) => {
      const child = spawn(PYTHON, ["-m","featuretree.workflow.source_tool", "--root", PROJECT,
        "--packet", process.env.FEATURETREE_PACKET], {cwd: PROJECT, stdio:["pipe","pipe","pipe"]});
      let out="", err="";
      child.stdout.on("data", chunk => {out += chunk; if(out.length>160000){child.kill();reject(new Error("Source output exceeded budget"));}});
      child.stderr.on("data", chunk => {err += chunk;});
      child.on("error", reject); child.on("close", code => code===0 ? resolve(out) : reject(new Error(err)));
      child.stdin.end(JSON.stringify(args));
    });
  }
});
'''.replace("PYTHON", json.dumps(python)).replace("PROJECT", json.dumps(project))
