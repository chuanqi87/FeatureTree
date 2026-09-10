from featuretree.core.io import read_json
"""Unresponsive providers release capacity without burning automatic retry budgets."""

import json
from pathlib import Path
import sys
import tempfile
import unittest

from featuretree.workflow.backends.monitor import EventActivity, ExecutionInterrupted, NoResponseTimeout
from featuretree.workflow.backends.opencode import OpenCodeBackend
from featuretree.workflow.backends.processes import identity


class MonitorTests(unittest.TestCase):
    def test_startup_and_partial_json_are_not_model_activity(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            path.write_text(json.dumps({"part": {"type": "step-start"}}) + "\n")
            activity = EventActivity(path)
            self.assertFalse(activity.poll())
            event = json.dumps({"part": {"type": "tool", "tool": "read"}}) + "\n"
            with path.open("a") as stream:
                stream.write(event[:10])
            self.assertFalse(activity.poll())
            with path.open("a") as stream:
                stream.write(event[10:])
            self.assertTrue(activity.poll())

    def test_unresponsive_backend_is_killed_and_records_diagnostics(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            executable = root / "fake-opencode"
            executable.write_text(f"#!{sys.executable}\nimport sys,time\nsys.stdin.read()\ntime.sleep(10)\n")
            executable.chmod(0o755)
            packet = {"limits": {"first_response_timeout": 1}}
            with self.assertRaises(NoResponseTimeout):
                OpenCodeBackend(str(executable)).execute(root, "ft-android", packet, root, 5, None, None)
            process = read_json(root / "process.json")
            self.assertIsNone(identity(process["pid"]))
            self.assertEqual(read_json(root / "metadata.json")["error_type"], "NoResponseTimeout")


    def test_signal_termination_is_not_retryable(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            executable = root / "fake-opencode"
            executable.write_text(f"#!{sys.executable}\nimport os,signal\nos.kill(os.getpid(),signal.SIGKILL)\n")
            executable.chmod(0o755)
            with self.assertRaises(ExecutionInterrupted) as stopped:
                OpenCodeBackend(str(executable)).execute(root, "ft-android", {}, root, 5, None, None)
            self.assertFalse(stopped.exception.retryable)
