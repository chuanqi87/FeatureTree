"""Thin Agent Bridge CLI adapter; no provider credential handling or hidden retries."""

import json
from pathlib import Path
import subprocess


class AgentBridge:
    def __init__(self, repo, launcher):
        self.root = repo.root
        self.launcher = Path(launcher).resolve()
        if not self.launcher.is_file():
            raise ValueError("Pass the installed Agent Bridge skill launcher via --launcher")

    def call(self, *args):
        result = subprocess.run(["node", str(self.launcher), *args, "--json"], cwd=self.root,
                                capture_output=True, text=True, timeout=45)
        if result.returncode:
            raise ValueError(f"Bridge command failed ({result.returncode}): {result.stderr[-1800:]}")
        return json.loads(result.stdout)

    def launch(self, task_path, model):
        result = self.call("task", "--backend", "opencode", "--model", model,
                           "--write", "--fresh", "--background", "--prompt-file", str(task_path.parent / "handoff.md"))
        return result["jobId"]

    def status(self, job_id):
        data = self.call("status", job_id)
        job = data["job"]
        return {key: job.get(key) for key in ("id", "status", "phase", "threadId", "startedAt", "completedAt",
                                             "errorMessage", "summary", "logFile")}

    def cancel(self, job_id):
        return self.call("cancel", job_id)
