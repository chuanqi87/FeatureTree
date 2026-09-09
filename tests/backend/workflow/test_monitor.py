"""Unresponsive providers release capacity without burning automatic retry budgets."""

import json
from pathlib import Path
import sys
import tempfile
import unittest

from featuretree.workflow.backends.monitor import EventActivity, ExecutionInterrupted, NoResponseTimeout
from featuretree.workflow.backends.opencode import OpenCodeBackend
from featuretree.workflow.backends.processes import identity
from featuretree.workflow.engine import execute_run
from featuretree.workflow.planning import make_plan
from featuretree.core.storage import ROOT
from featuretree.workflow.state import read_json
from tests.fixtures.console import workspace


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
                OpenCodeBackend(str(executable)).execute(root, "ft-scope", packet, root, 5, None, None)
            process = read_json(root / "process.json")
            self.assertIsNone(identity(process["pid"]))
            self.assertEqual(read_json(root / "metadata.json")["error_type"], "NoResponseTimeout")

    def test_unresponsive_provider_does_not_automatically_retry(self):
        class SilentBackend:
            calls = 0

            def execute(self, *args):
                self.calls += 1
                raise NoResponseTimeout("fixture no response")

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workspace(root)
            state = make_plan(root, ["sample"], read_json(ROOT / "config/workflow/baseline.example.json"), max_attempts=3)
            backend = SilentBackend()
            result = execute_run(root, state["id"], backend, lambda _: None)
            self.assertEqual(backend.calls, 1)
            self.assertEqual(result["tasks"]["sample/scope"]["status"], "failed")
            self.assertFalse(result["tasks"]["sample/scope"]["attempts"][0]["retryable"])

    def test_signal_termination_is_not_retryable(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            executable = root / "fake-opencode"
            executable.write_text(f"#!{sys.executable}\nimport os,signal\nos.kill(os.getpid(),signal.SIGTERM)\n")
            executable.chmod(0o755)
            with self.assertRaises(ExecutionInterrupted) as stopped:
                OpenCodeBackend(str(executable)).execute(root, "ft-scope", {}, root, 5, None, None)
            self.assertFalse(stopped.exception.retryable)

    def test_total_timeout_does_not_repeat_an_exhausted_research_budget(self):
        from featuretree.workflow.backends.monitor import StageTimeout

        class ExhaustedBackend:
            calls = 0

            def execute(self, *args):
                self.calls += 1
                raise StageTimeout('fake-opencode', 600)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workspace(root)
            state = make_plan(root, ['sample'], read_json(ROOT / 'config/workflow/baseline.example.json'), max_attempts=3)
            backend = ExhaustedBackend()
            result = execute_run(root, state['id'], backend, lambda _: None)
            self.assertEqual(backend.calls, 1)
            self.assertEqual(result['tasks']['sample/scope']['status'], 'failed')
