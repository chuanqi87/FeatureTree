"""OpenCode process transport with source reads and attempt-local delivery writes."""

import json
import os
import signal
import subprocess
import time

from featuretree.core.io import write_json
from featuretree.workflow.backends.processes import identity
from featuretree.workflow.backends.monitor import wait_for_model
from featuretree.workflow.backends.delivery import delivery_prompt
from featuretree.workflow.backends.results import collect_result
from featuretree.workflow.backends.events import parse_events, event_summary
from featuretree.workflow.backends.runtime import prepare_runtime


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
        limits = packet.get("limits", {})
        prompt = (delivery_prompt() + "执行工作单。交付文件须符合 output_schema，固定身份由工具填入。"
                  "reviewed_hash 使用下方给定值（如有）。仅通过交付工具写文件。\n" +
                  json.dumps(packet, ensure_ascii=False))
        if packet.get("batch"):
            prompt = ("本次仅研究工作单中列出的这一小批 API 和主题；不要枚举或研究整个领域。"
                      "其他批次由执行器独立运行并汇总。及时通过 submit_payload 保存本批结果，"
                      "完成本批后调用 finish_payload。\n" + prompt)
        if packet.get("response_repair"):
            prompt = ("本次只修复 response_repair 中的 JSON 格式，禁止重新检索或修改研究结论。"
                      "使用当前工作单，通过交付工具写修复后的文件，不复述正文。\n" + prompt)
        started = time.monotonic()
        environment = dict(os.environ)
        environment["OPENCODE_CONFIG_DIR"] = str(root / ".opencode")
        environment["FEATURETREE_PACKET"] = str(root / "task.json")
        if limits.get("max_output_tokens", 32000) is not None:
            environment["OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX"] = str(limits.get("max_output_tokens", 32000))
        else:
            environment.pop("OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX", None)
        # Only source reads and immutable attempt-local payload writes are authorized. Provider credentials
        # remain in the user's configuration and are never copied into run artifacts.
        environment["OPENCODE_CONFIG_CONTENT"] = json.dumps({
            "permission": {"*": "deny", "source_catalog": "allow", "submit_payload": "allow", "finish_payload": "allow"},
            "tools": {"*": False, "source_catalog": True, "submit_payload": True, "finish_payload": True}, "share": "disabled"})
        with (folder / "events.jsonl").open("w") as stdout, (folder / "stderr.log").open("w") as stderr:
            process = subprocess.Popen(args, cwd=root, stdin=subprocess.PIPE, stdout=stdout,
                                       stderr=stderr, text=True, start_new_session=True, env=environment)
            try:
                write_json(folder / "process.json", {"pid": process.pid, "identity": identity(process.pid)})
                timing = wait_for_model(process, prompt, folder / "events.jsonl", timeout,
                                        packet.get("limits", {}).get("first_response_timeout", 120),
                                        root / "delivery/completed.json")
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
                exc.metadata = {"elapsed_seconds": round(time.monotonic() - started, 3), "limits": limits,
                                "model": model, "input_chars": len(prompt), "error_type": type(exc).__name__,
                                **event_summary((folder / "events.jsonl").read_text().splitlines())}
                write_json(folder / "metadata.json", exc.metadata)
                raise
        metadata = {**timing, **runtime, "model": model, "variant": variant, "limits": limits,
                    "elapsed_seconds": round(time.monotonic() - started, 3), "input_chars": len(prompt)}
        return collect_result(root, folder, packet, process.returncode, metadata)
