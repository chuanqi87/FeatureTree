"""OpenCode CLI transport; never grants a model write access or shell access."""

import json
import os
import signal
import subprocess
import time

from featuretree.workflow.state import read_json
from featuretree.core.storage import write_json
from featuretree.workflow.backends.processes import identity


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
    def __init__(self, executable="opencode"):
        self.executable = executable

    def execute(self, root, agent, packet, folder, timeout, model, variant):
        args = [self.executable, "run", "--pure", "--agent", agent, "--format", "json"]
        if model:
            args.extend(["--model", model])
        if variant:
            args.extend(["--variant", variant])
        prompt = ("执行工作单。只输出符合 output_schema 的 JSON 信封，input_hash 原样回传。"
                  "reviewed_hash 使用下方给定值（如有）。不要修改文件。\n" +
                  json.dumps(packet, ensure_ascii=False))
        started = time.monotonic()
        with (folder / "events.jsonl").open("w") as stdout, (folder / "stderr.log").open("w") as stderr:
            process = subprocess.Popen(args, cwd=root, stdin=subprocess.PIPE, stdout=stdout,
                                       stderr=stderr, text=True, start_new_session=True)
            try:
                write_json(folder / "process.json", {"pid": process.pid, "identity": identity(process.pid)})
                process.communicate(prompt, timeout=timeout)
            except BaseException:
                try:
                    os.killpg(process.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
                try:
                    process.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                raise
        if process.returncode:
            raise ValueError(f"OpenCode exited {process.returncode}; inspect {folder / 'stderr.log'}")
        final, metadata = parse_events((folder / "events.jsonl").read_text().splitlines())
        (folder / "response.json").write_text(final, encoding="utf-8")
        result = read_json(folder / "response.json")
        return result, {**metadata, "elapsed_seconds": round(time.monotonic() - started, 3),
                        "model": model or "OpenCode configured default", "variant": variant}
