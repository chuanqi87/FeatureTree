"""Run conventional OpenCode agents and collect their workspace artifacts."""

import json
import os
import signal
import subprocess
import time

from featuretree.core.io import write_json
from featuretree.workflow.backends.processes import identity
from featuretree.workflow.backends.monitor import wait_for_model
from featuretree.workflow.backends.prompt import execution_prompt
from featuretree.workflow.backends.results import collect_result
from featuretree.workflow.backends.events import event_summary
from featuretree.workflow.backends.runtime import prepare_runtime


class OpenCodeBackend:
    def __init__(self, executable="opencode", runtime_directory=None):
        self.executable = executable
        self.runtime_directory = runtime_directory

    def execute(self, root, agent, packet, folder, timeout, model, variant):
        runtime = prepare_runtime(self.executable, self.runtime_directory, root) if self.runtime_directory else {}
        args = [self.executable, "run", "--agent", agent, "--format", "json", "--thinking", "--auto", "--dir", str(root)]
        if model:
            args.extend(["--model", model])
        if variant:
            args.extend(["--variant", variant])
        limits = packet.get("limits", {})
        prompt = execution_prompt(packet, root)
        started = time.monotonic()
        environment = dict(os.environ)
        environment["OPENCODE_CONFIG_DIR"] = str(root / ".opencode")
        environment["FEATURETREE_PACKET"] = str(root / "task.json")
        if limits.get("max_output_tokens") is not None:
            environment["OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX"] = str(limits.get("max_output_tokens"))
        else:
            environment.pop("OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX", None)
        # Native tools remain available, as in the normal OpenCode workflow. Only
        # accepted responses enter the fact store through the executor's validators.
        environment["OPENCODE_CONFIG_CONTENT"] = json.dumps({
            "permission": {"*": "allow"}, "tools": {"*": True}, "share": "disabled"})
        with (folder / "events.jsonl").open("w") as stdout, (folder / "stderr.log").open("w") as stderr:
            process = subprocess.Popen(args, cwd=root, stdin=subprocess.PIPE, stdout=stdout,
                                       stderr=stderr, text=True, start_new_session=True, env=environment)
            try:
                write_json(folder / "process.json", {"pid": process.pid, "identity": identity(process.pid)})
                timing = wait_for_model(process, prompt, folder / "events.jsonl", timeout,
                                        packet.get("limits", {}).get("first_response_timeout"))
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
