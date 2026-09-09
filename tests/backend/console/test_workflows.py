"""HTTP commands and lifecycle tests without invoking paid model services."""

import json
from pathlib import Path
import tempfile
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from featuretree.core.storage import ROOT, Repository
from featuretree.console.server import create_server
from featuretree.console.service import WorkflowConsole
from featuretree.workflow.engine import execute_run
from tests.fixtures.console import workspace
from tests.fixtures.workflow import FixtureBackend


class SpyLauncher:
    def __init__(self):
        self.calls = []
        self.running = set()

    def available(self):
        return True

    def active(self, folder):
        return folder.name in self.running

    def start(self, root, run_id):
        self.calls.append(run_id)
        self.running.add(run_id)


class WorkflowConsoleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = workspace(Path(self.temp.name))
        self.launcher = SpyLauncher()
        self.console = WorkflowConsole(self.root, self.launcher)
        self.server = create_server(Repository(self.root), ROOT / "web/dist", port=0, workflow=self.console)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.origin = f"http://127.0.0.1:{self.server.server_port}"
        self.token = self.get("config")[1]["csrf_token"]

    def get(self, path, headers=None):
        return self.request(Request(self.origin + "/api/workflow/" + path, headers=headers or {}))

    def post(self, path, body, headers=None):
        base = {"Content-Type": "application/json", "Origin": self.origin, "X-Workflow-Token": self.token}
        base.update(headers or {})
        return self.request(Request(self.origin + "/api/workflow/" + path,
                                   data=json.dumps(body).encode(), headers=base, method="POST"))

    def request(self, request):
        try:
            response = urlopen(request, timeout=10)
        except HTTPError as error:
            response = error
        with response:
            return response.status, json.load(response)

    def body(self, **changes):
        return {"nodes": ["sample.branch"], "action": "drilldown", "source_node": "sample.branch",
                "baseline_id": "design-unknown", "request_id": "fixture-request-0001", **changes}

    def test_reads_are_side_effect_free(self):
        self.assertEqual(self.get("runs")[1], {"runs": []})
        self.assertEqual(self.launcher.calls, [])
        self.assertFalse((self.root / ".workflow").exists())
        self.assertEqual(self.get("config")[1]["baselines"][0]["baseline"]["platforms"]["android"]["status"], "unknown")

    def test_node_trigger_is_idempotent_and_root_is_resolved_on_server(self):
        body = self.body(nodes=["sample.branch.item"], action="root")
        status, run = self.post("runs", body)
        self.assertEqual(status, 202)
        self.assertEqual(run["nodes"], ["sample"])
        self.assertEqual(run["status"], "running")
        self.assertEqual(self.post("runs", body)[1]["id"], run["id"])
        self.assertEqual(len(self.launcher.calls), 1)
        self.assertEqual(self.post("runs", {**body, "request_id": "fixture-request-0002"})[0], 409)
        self.assertEqual(self.post("runs", {**body, "depth": 1})[0], 409)
        self.assertEqual(len(Repository(self.root).features()), 4)

    def test_cross_site_or_missing_token_requests_cannot_start_work(self):
        for headers in ({"X-Workflow-Token": ""}, {"Origin": "https://attacker.example"}, {"Host": "attacker.example"}):
            self.assertEqual(self.post("runs", self.body(), headers)[0], 403)
        self.assertEqual(self.get("config", {"Host": "attacker.example"})[0], 403)
        self.assertEqual(self.post("runs", self.body(), {"Content-Type": "text/plain"})[0], 400)
        self.assertFalse(self.launcher.calls)

    def test_invalid_scope_and_parameters_do_not_launch(self):
        for changes in ({"nodes": ["missing"]}, {"nodes": ["sample.branch.item"]}, {"depth": True},
                        {"workers": -1}, {"action": "shell"}, {"command": "echo bad"},
                        {"baseline_id": "../../outside"}, {"model": "--help"},
                        {"nodes": ["sample", "sample.branch"]}):
            status, result = self.post("runs", self.body(**changes))
            self.assertEqual(status, 400, result)
        self.assertFalse(self.launcher.calls)

    def test_capacity_is_shared_between_node_runs(self):
        self.assertEqual(self.post("runs", self.body(workers=4))[0], 202)
        self.assertEqual(self.post("runs", self.body(nodes=["other"], workers=4, request_id="fixture-request-0002"))[0], 409)
        self.assertEqual(len(self.launcher.calls), 1)

    def test_stale_runs_remain_readable_but_cannot_execute(self):
        _, run = self.post("runs", self.body())
        self.launcher.running.clear()
        (self.root / "AGENTS.md").write_text("Changed rules")
        status, detail = self.get("runs/" + run["id"])
        self.assertEqual(status, 200)
        self.assertTrue(detail["stale_rules"])
        self.assertFalse(any(detail["actions"].values()))
        self.assertEqual(self.post(f"runs/{run['id']}/start", {})[0], 409)

    def test_http_results_and_publish_use_real_workflow_gates(self):
        _, run = self.post("runs", self.body())
        self.launcher.running.clear()
        execute_run(self.root, run["id"], FixtureBackend(), lambda _: None)
        status, detail = self.get("runs/" + run["id"])
        self.assertEqual(status, 200)
        self.assertEqual(detail["status"], "completed")
        self.assertEqual(len(detail["nodes_proposed"]), 2)
        self.assertTrue(detail["actions"]["publish"])
        status, published = self.post(f"runs/{run['id']}/publish", {})
        self.assertEqual(status, 202, published)
        self.assertEqual(published["status"], "published")
        self.assertEqual(len(Repository(self.root).features()), 6)

    def test_http_rejected_review_can_only_be_revised_with_explicit_nodes(self):
        _, run = self.post("runs", self.body())
        self.launcher.running.clear()
        execute_run(self.root, run["id"], FixtureBackend(reject_once="review"), lambda _: None)
        self.assertEqual(self.get("runs/" + run["id"])[1]["status"], "blocked")
        self.assertEqual(self.post(f"runs/{run['id']}/revise", {})[0], 400)
        self.assertEqual(self.post(f"runs/{run['id']}/revise", {"nodes": ["sample.branch"]})[0], 202)
        self.assertEqual(len(self.launcher.calls), 2)
