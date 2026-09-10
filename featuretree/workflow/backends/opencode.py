"""OpenCode CLI transport; never grants a model write access or shell access."""

import json
import hashlib
import os
import signal
import subprocess
import time

from featuretree.core.io import read_json, write_json
from featuretree.workflow.backends.processes import identity
from featuretree.workflow.backends.monitor import ExecutionInterrupted, wait_for_model
from featuretree.workflow.backends.errors import MissingStructuredAnswer, ResponseFormatError, has_repairable_answer
from featuretree.workflow.backends.provider_errors import provider_error
from featuretree.workflow.backends.runtime import prepare_runtime


def parse_events(lines):
    messages = {}
    session_id = None
    completed = False
    usage = []
    for line in lines:
        if not line.strip():
            continue
        event = json.loads(line)
        if event.get("type") in ("error", "session.error"):
            raise ValueError(f"OpenCode reported an error: {event.get('error', event.get('properties'))}")
        part = event.get("part", {})
        session_id = event.get("sessionID") or part.get("sessionID") or session_id
        if part.get("type") == "text":
            message = part.get("messageID", "final")
            messages.setdefault(message, {})[part.get("id", "text")] = part["text"]
        if part.get("type") == "step-start":
            completed = False
        if part.get("type") == "step-finish":
            completed = part.get("reason") == "stop"
            usage.append({k: part[k] for k in ("cost", "tokens", "reason") if k in part})
            if part.get("reason") in ("length", "error", "content-filter"):
                raise ValueError(f"Incomplete model output: {part.get('reason')}")
    if not completed or not messages:
        raise ValueError("OpenCode returned no completed final response")
    final = "\n".join(list(messages.values())[-1].values()).strip()
    # Accept a single fenced object; never heuristically extract a substring from prose.
    if final.startswith("```json\n") and final.endswith("\n```"):
        final = final[8:-4]
    elif final.startswith("```\n") and final.endswith("\n```"):
        final = final[4:-4]
    return final, {"session_id": session_id, "usage": usage}


class OpenCodeBackend:
    def __init__(self, executable="opencode", runtime_directory=None):
        self.executable = executable
        self.runtime_directory = runtime_directory

    def execute(self, root, agent, packet, folder, timeout, model, variant):
        runtime = prepare_runtime(self.executable, self.runtime_directory, root) if self.runtime_directory else {}
        args = [self.executable, "run", "--pure", "--agent", agent, "--format", "json"]
        if model:
            args.extend(["--model", model])
        if variant:
            args.extend(["--variant", variant])
        prompt = ("执行工作单。只输出符合 output_schema 的 JSON 信封，input_hash 原样回传。"
                  "reviewed_hash 使用下方给定值（如有）。不要修改文件。\n" +
                  json.dumps(packet, ensure_ascii=False))
        if packet.get("response_repair"):
            prompt = ("本次只修复 response_repair 中的 JSON 格式，禁止重新检索或修改研究结论。"
                      "使用当前信封 input_hash，直接输出 JSON，不加说明句或 Markdown。\n" + prompt)
        started = time.monotonic()
        environment = dict(os.environ)
        environment["OPENCODE_CONFIG_DIR"] = str(root / ".opencode")
        environment["FEATURETREE_PACKET"] = str(root / "task.json")
        # Only this attempt's read-only source tool is authorized. Provider credentials
        # remain in the user's configuration and are never copied into run artifacts.
        environment["OPENCODE_CONFIG_CONTENT"] = json.dumps({
            "permission": {"*": "deny", "source_catalog": "allow"},
            "tools": {"*": False, "source_catalog": True}, "share": "disabled"})
        with (folder / "events.jsonl").open("w") as stdout, (folder / "stderr.log").open("w") as stderr:
            process = subprocess.Popen(args, cwd=root, stdin=subprocess.PIPE, stdout=stdout,
                                       stderr=stderr, text=True, start_new_session=True, env=environment)
            try:
                write_json(folder / "process.json", {"pid": process.pid, "identity": identity(process.pid)})
                timing = wait_for_model(process, prompt, folder / "events.jsonl", timeout,
                                        packet.get("limits", {}).get("first_response_timeout", 120))
            except BaseException as exc:
                try:
                    os.killpg(process.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
                try:
                    process.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                exc.metadata = {"elapsed_seconds": round(time.monotonic() - started, 3),
                                "model": model, "input_chars": len(prompt), "error_type": type(exc).__name__}
                write_json(folder / "metadata.json", exc.metadata)
                raise
        if process.returncode < 0:
            error = ExecutionInterrupted(f"OpenCode terminated by signal {-process.returncode}; automatic retry stopped")
            error.metadata = {"elapsed_seconds": round(time.monotonic() - started, 3), "model": model,
                              "error_type": "ExecutionInterrupted"}
            write_json(folder / "metadata.json", error.metadata)
            raise error
        lines = (folder / "events.jsonl").read_text().splitlines()
        error = provider_error(lines)
        if error:
            error.metadata = {"model": model, "provider_status": error.status_code,
                              "elapsed_seconds": round(time.monotonic() - started, 3), **runtime}
            write_json(folder / "metadata.json", error.metadata)
            raise error
        if process.returncode:
            raise ValueError(f"OpenCode exited {process.returncode}; inspect {folder / 'stderr.log'}")
        final, metadata = parse_events(lines)
        (folder / "response.json").write_text(final, encoding="utf-8")
        metadata.update(**timing, elapsed_seconds=round(time.monotonic() - started, 3),
                        **runtime,
                        input_chars=len(prompt), output_chars=len(final),
                        model=model or "OpenCode configured default", variant=variant,
                        recovery="format_repair" if packet.get("response_repair") else None)
        try:
            result = read_json(folder / "response.json")
        except json.JSONDecodeError as exc:
            if has_repairable_answer(final):
                error = ResponseFormatError(f"Completed answer is not valid JSON: {exc}. Repair retained response only.")
            else:
                error = MissingStructuredAnswer("No complete structured answer was produced; inspect scope/tool budget before retrying")
            metadata.update(error_type=type(error).__name__, response_sha256=hashlib.sha256(final.encode()).hexdigest())
            error.metadata = metadata
            write_json(folder / "metadata.json", metadata)
            raise error from exc
        return result, metadata
