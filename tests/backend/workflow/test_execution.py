"""Synthetic workflow tests: these fixtures make no claims about real platforms."""

from copy import deepcopy
from contextlib import closing
import json
import hashlib
from pathlib import Path
import shutil
import sys
import sqlite3
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from featuretree.core.storage import ROOT, Repository, read_yaml, write_json, write_yaml
from featuretree.taxonomy.authoring import feature
from featuretree.workflow.stages import PLATFORMS
from featuretree.workflow.state import digest, load_run, lock, read_json
from featuretree.workflow.engine import execute_run
from featuretree.workflow.recovery import reset_tasks
from featuretree.workflow.gates import validate_proposal
from featuretree.workflow.backends.opencode import OpenCodeBackend, parse_events
from featuretree.workflow.planning import make_plan, work_order
from featuretree.workflow.publication import publish, report
from featuretree.workflow.backends.processes import identity, terminate_recorded
from featuretree.workflow.sources import detect_anchors
from featuretree.taxonomy.validation import validate_tree
from tests.fixtures.workflow import FixtureBackend, fixture_proposal


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "config", self.root / "config")
        shutil.copytree(ROOT / ".opencode", self.root / ".opencode")
        (self.root / "AGENTS.md").write_text("Synthetic test repository")
        for fid in ("sample", "other"):
            node = feature(fid, parent=None, level="L1", zh=fid, en=fid, definition="Fixture root", includes=[fid])
            write_yaml(self.root / "taxonomy" / f"{fid}.yaml", {"domain": fid, "features": [node]})
        self.baseline = read_json(ROOT / "config/workflow/baseline.example.json")

    def plan(self, nodes=None, **kwargs):
        return make_plan(self.root, nodes or ["sample"], self.baseline, **kwargs)["id"]

    def run_batch(self, backend=None, nodes=None, **kwargs):
        run_id = self.plan(nodes, **kwargs)
        backend = backend or FixtureBackend()
        execute_run(self.root, run_id, backend, lambda _: None)
        return run_id, backend

    def test_plan_has_fixed_snapshot_and_no_model_side_effect(self):
        run_id = self.plan(["sample", "other"])
        folder, state = load_run(self.root, run_id)
        self.assertEqual(len(state["tasks"]), 15)
        self.assertEqual(len(Repository(self.root).features()), 2)
        self.assertEqual(digest(read_json(folder / "snapshot.json")), state["snapshot_hash"])

    def test_reject_unknown_atomic_duplicate_and_overlapping_nodes(self):
        for nodes in (["missing"], ["sample", "sample"]):
            with self.assertRaises(ValueError):
                self.plan(nodes)
        doc = read_yaml(self.root / "taxonomy/sample.yaml")
        child = fixture_proposal({"node_id": "sample", "subtree": {"sample": doc["features"][0]}})["nodes"][0]
        doc["features"].append(child)
        write_yaml(self.root / "taxonomy/sample.yaml", doc)
        with self.assertRaisesRegex(ValueError, "overlap"):
            self.plan(["sample", "sample.first"])

    def test_parallel_pipeline_does_not_write_tree_until_publish(self):
        original = (self.root / "taxonomy/sample.yaml").read_bytes()
        run_id, backend = self.run_batch(nodes=["sample", "other"], workers=3)
        status = report(self.root, run_id)
        self.assertTrue(status["ready_to_publish"])
        self.assertGreaterEqual(backend.peak, 2)
        self.assertLessEqual(backend.peak, 3)
        self.assertEqual((self.root / "taxonomy/sample.yaml").read_bytes(), original)
        self.assertEqual(status["additions"]["branches"], 4)
        self.assertEqual(status["additions"]["atomic_leaves"], 0)
        self.assertEqual(status["anchor_counts"]["failed"], 4)
        self.assertEqual(status["baseline_unverified"], list(PLATFORMS))

    def test_transient_retry_and_successful_stage_reuse(self):
        run_id, backend = self.run_batch(FixtureBackend(fail_once="android"))
        self.assertEqual(backend.calls.count("sample/android"), 2)
        calls = len(backend.calls)
        execute_run(self.root, run_id, backend, lambda _: None)
        self.assertEqual(len(backend.calls), calls)
        self.assertTrue(report(self.root, run_id)["ready_to_publish"])

    def test_invalid_envelope_is_bounded_and_blocks_dependents(self):
        run_id, backend = self.run_batch(FixtureBackend(mutate=lambda r: r.update(input_hash="wrong")))
        state = report(self.root, run_id)
        self.assertEqual(len(backend.calls), 2)
        self.assertFalse(state["ready_to_publish"])
        with self.assertRaises(ValueError):
            publish(self.root, run_id)
        reset_tasks(self.root, run_id)
        execute_run(self.root, run_id, FixtureBackend(), lambda _: None)
        self.assertTrue(report(self.root, run_id)["ready_to_publish"])

    def test_rejected_review_requires_revision_without_repeating_scouts(self):
        run_id, backend = self.run_batch(FixtureBackend(reject_once="review"))
        self.assertEqual(report(self.root, run_id)["state_counts"]["blocked"], 1)
        reset_tasks(self.root, run_id, ["sample"])
        execute_run(self.root, run_id, backend, lambda _: None)
        self.assertTrue(report(self.root, run_id)["ready_to_publish"])
        self.assertEqual(backend.calls.count("sample/synthesize"), 2)
        self.assertEqual(backend.calls.count("sample/android"), 1)

    def test_global_rejection_can_revise_only_affected_node(self):
        run_id, backend = self.run_batch(FixtureBackend(reject_once="integrate"), nodes=["sample", "other"])
        reset_tasks(self.root, run_id, ["sample"])
        execute_run(self.root, run_id, backend, lambda _: None)
        self.assertTrue(report(self.root, run_id)["ready_to_publish"])
        self.assertEqual(backend.calls.count("other/synthesize"), 1)
        self.assertEqual(backend.calls.count("batch/integrate"), 2)

    def test_publish_is_idempotent_and_creates_unknown_stubs(self):
        run_id, _ = self.run_batch()
        receipt = publish(self.root, run_id)
        self.assertEqual(publish(self.root, run_id), receipt)
        repo = Repository(self.root)
        features = repo.features()
        docs, paths = repo.knowledge()
        self.assertEqual(features["sample.first"]["anchor_status"], "failed")
        self.assertEqual(docs["sample.first"]["status"], "stub")
        self.assertTrue(all(p["status"] == "unknown" for p in docs["sample.first"]["presence"].values()))
        self.assertEqual(validate_tree(features, docs, paths, repo.config()), [])

    def test_changed_tree_or_comments_prevent_publication(self):
        run_id, _ = self.run_batch()
        path = self.root / "taxonomy/other.yaml"
        path.write_text(path.read_text() + "\n# Another author changed this file\n")
        with self.assertRaisesRegex(ValueError, "changed since planning"):
            publish(self.root, run_id)
        self.assertEqual(len(Repository(self.root).features()), 2)

    def test_partial_publish_recovers_and_external_edits_block_recovery(self):
        run_id, _ = self.run_batch()
        from featuretree.workflow import publication
        original = publication.write_text
        written = []
        def interrupt(path, content):
            original(path, content)
            written.append(path)
            raise OSError("Synthetic interruption after file replacement")
        with patch.object(publication, "write_text", interrupt), self.assertRaises(OSError):
            publish(self.root, run_id)
        self.assertEqual(len(written), 1)
        old = written[0].read_text()
        written[0].write_text(old + "\n# External edit\n")
        with self.assertRaisesRegex(ValueError, "conflict"):
            publish(self.root, run_id)
        written[0].write_text(old)
        self.assertTrue(publish(self.root, run_id))
        self.assertEqual(len(Repository(self.root).features()), 4)

    def test_snapshot_artifact_and_rule_drift_are_rejected(self):
        run_id, _ = self.run_batch()
        folder, state = load_run(self.root, run_id)
        target = folder / state["tasks"]["sample/scope"]["result_path"]
        value = read_json(target)
        value["payload"]["axis"] = "Tampered"
        write_json(target, value)
        with self.assertRaisesRegex(ValueError, "Artifact changed"):
            publish(self.root, run_id)
        (self.root / "AGENTS.md").write_text("Changed rule")
        with self.assertRaisesRegex(ValueError, "rules or agents changed"):
            load_run(self.root, run_id)

    def test_scope_and_disposition_validation(self):
        run_id = self.plan()
        folder, state = load_run(self.root, run_id)
        snapshot = read_json(folder / "snapshot.json")
        work = work_order(snapshot, state, "sample")
        proposal = fixture_proposal(work)
        scouts = [{"candidates": [{"id": p + ":candidate"}]} for p in PLATFORMS]
        validate_proposal(self.root, snapshot, work, proposal, scouts)
        for mutate in (
            lambda p: p["nodes"][0].update(parent="other"),
            lambda p: p["nodes"][0].update(knowledge_path="../outside.yaml"),
            lambda p: p["nodes"][0].update(bindings={}),
            lambda p: p["nodes"][0].update(anchor_status="symbol_ok"),
            lambda p: p["dispositions"].pop(),
        ):
            value = deepcopy(proposal)
            mutate(value)
            with self.assertRaises(ValueError):
                validate_proposal(self.root, snapshot, work, value, scouts)

    def test_run_lock_prevents_multiple_coordinators(self):
        run_id = self.plan()
        with lock(self.root / ".workflow/runs" / run_id / "run.lock"):
            with self.assertRaisesRegex(ValueError, "coordinator"):
                execute_run(self.root, run_id, FixtureBackend(), lambda _: None)

    def test_anchor_detection_checks_body_hash_and_symbol_boundaries(self):
        folder = self.root / "docs-raw/official"
        folder.mkdir(parents=True)
        body = b"# FixtureApiExtra\n"
        (folder / "body.md").write_bytes(body)
        with closing(sqlite3.connect(folder / "corpus.sqlite")) as conn:
            conn.execute("CREATE TABLE documents(url, status, body_path, body_sha256, fetched_at)")
            conn.execute("INSERT INTO documents VALUES(?,?,?,?,?)", (
                "https://developer.android.com/reference/fixture", "ready", "body.md",
                hashlib.sha256(body).hexdigest(), "fixture-time"))
            conn.commit()
        work = {"node_id": "sample", "subtree": Repository(self.root).features()}
        nodes = fixture_proposal(work)["nodes"]
        result = detect_anchors(self.root, nodes)
        self.assertEqual(result["results"][0]["anchor_status"], "body_ok")
        (folder / "body.md").write_bytes(b"# FixtureApi\n")
        result = detect_anchors(self.root, nodes)
        self.assertEqual(result["results"][0]["anchor_status"], "failed")
        self.assertIn("hash mismatch", result["results"][0]["bindings"][0]["reason"])
        with closing(sqlite3.connect(folder / "corpus.sqlite")) as conn:
            conn.execute("UPDATE documents SET body_sha256=?", (hashlib.sha256(b"# FixtureApi\n").hexdigest(),))
            conn.commit()
        self.assertEqual(detect_anchors(self.root, nodes)["results"][0]["anchor_status"], "symbol_ok")

    def test_unsafe_run_id_is_rejected_before_creating_lock(self):
        with self.assertRaisesRegex(ValueError, "Invalid run ID"):
            execute_run(self.root, "../../escape", FixtureBackend(), lambda _: None)
        self.assertFalse((self.root / "escape").exists())

    def test_interrupted_running_attempt_resumes_with_history(self):
        run_id = self.plan()
        folder, state = load_run(self.root, run_id)
        task = state["tasks"]["sample/scope"]
        task.update(status="running", attempts=[{"number": 1, "status": "running"}])
        write_json(folder / "state.json", state)
        execute_run(self.root, run_id, FixtureBackend(), lambda _: None)
        _, state = load_run(self.root, run_id)
        self.assertEqual(state["tasks"]["sample/scope"]["attempts"][0]["status"], "interrupted")
        self.assertTrue(report(self.root, run_id)["ready_to_publish"])


class OpenCodeProtocolTests(unittest.TestCase):
    def test_recorded_process_is_reaped_but_wrong_identity_is_not(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "process.json"
            child = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"], start_new_session=True)
            try:
                write_json(path, {"pid": child.pid, "identity": "not-this-process"})
                terminate_recorded(path)
                self.assertIsNone(child.poll())
                write_json(path, {"pid": child.pid, "identity": identity(child.pid)})
                terminate_recorded(path)
                self.assertNotEqual(child.wait(timeout=5), 0)
            finally:
                if child.poll() is None:
                    child.kill()
                    child.wait()

    def events(self, reason="stop", text='{"ok": true}'):
        return [json.dumps({"type": "text", "sessionID": "fixture-session", "part": {
                    "type": "text", "messageID": "m", "id": "p", "text": text}}),
                json.dumps({"type": "step_finish", "part": {"type": "step-finish", "reason": reason}})]

    def test_protocol_and_incomplete_outputs(self):
        result, metadata = parse_events(self.events())
        self.assertEqual(json.loads(result), {"ok": True})
        self.assertEqual(metadata["session_id"], "fixture-session")
        for events in (self.events("length"), self.events("tool-calls"), ["garbage"]):
            with self.assertRaises(ValueError):
                parse_events(events)

    def test_adapter_passes_prompt_via_stdin_and_uses_named_agent(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            script = folder / "fake-opencode"
            script.write_text(f"#!{sys.executable}\nimport sys,json\n" +
                "assert sys.argv[1:] == ['run','--pure','--agent','ft-scope','--format','json']\n" +
                "assert 'only-test' in sys.stdin.read()\n" +
                "print(" + repr(self.events()[0]) + ")\nprint(" + repr(self.events()[1]) + ")\n")
            script.chmod(0o755)
            result, _ = OpenCodeBackend(str(script)).execute(folder, "ft-scope", {"only-test": True}, folder, 5, None, None)
            self.assertEqual(result, {"ok": True})
