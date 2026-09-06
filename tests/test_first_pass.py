"""Preliminary research stays separate from confirmation, even in a worker pool."""

from copy import deepcopy
from datetime import datetime, timedelta, timezone
import fcntl
import unittest
from unittest.mock import patch

from featuretree.first_pass.runner import initial_state, load_manifest, queued_nodes, run_batch, update_job
from featuretree.first_pass.tasks import check_task, load_task, prepare_batch
from featuretree.first_pass.validation import response_errors
from featuretree.storage import read_yaml, write_json, write_text
from tests import test_research_probe


class FirstPassTests(unittest.TestCase):
    def setUp(self):
        test_research_probe.ResearchProbeTests.setUp(self)
        self.corpus.db.commit()
        self.deadline = (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat()
        self.manifest_path = prepare_batch(self.repo, "p/m", self.deadline)
        self.directory = self.manifest_path.parent
        self.path = self.directory / "tasks/sample/task.json"
        self.task = load_task(self.repo, self.path)
        self.response = {"task_id": self.task["task_id"], "feature_id": "sample", "stage": "first_pass",
            "summary": "Synthetic fixture only", "platforms": [
                {"platform": platform, "signal": "unknown", "observation": "Fixture has no confirmed behavior",
                 "version_scope": "Unresolved fixture baseline", "conditions": ["Fixture only"],
                 "gaps": ["Actual source/version investigation missing"], "confidence": "low",
                 "evidence_strength": "missing", "citations": [],
                 "device_review": {"requirement": "unassessed", "reason": "Static fixture without a real plan"}}
                for platform in self.task["platforms"]],
            "difference_hypotheses": [], "scope_gaps": ["Synthetic fixture not actual research"],
            "followup_priority": {"level": "P1", "reason": "Missing fixture evidence"}}

    def save(self):
        write_json(self.path.parent / "response.json", self.response)

    def cite_android(self):
        row = next(p for p in self.response["platforms"] if p["platform"] == "android")
        row.update(signal="documented_mechanism", evidence_strength="direct",
                   citations=[{"source_id": "android-1", "locator": "Sample", "start_line": 3, "end_line": 4}])
        return row

    def test_task_is_immutable_idempotent_and_has_isolated_context(self):
        self.assertEqual(prepare_batch(self.repo, "p/m", self.deadline), self.manifest_path)
        self.assertIn("--output output/research/first-pass/", (self.path.parent / "handoff.md").read_text())
        self.task["budget"]["max_attempts"] = 9
        write_json(self.path, self.task)
        with self.assertRaisesRegex(ValueError, "identity"):
            load_task(self.repo, self.path)

    def test_unknown_is_valid_but_not_confirmed_or_semantically_accepted(self):
        original = (self.root / "knowledge/sample.yaml").read_bytes()
        self.save()
        result = check_task(self.repo, self.path)
        self.assertTrue(result["delivery_valid"])
        self.assertFalse(result["production_accepted"])
        self.assertFalse(result["semantic_review_passed"])
        self.assertEqual(original, (self.root / "knowledge/sample.yaml").read_bytes())

    def test_missing_duplicate_foreign_platform_or_extra_field_fails(self):
        for value in (None, {}, dict(self.response, platforms=[]), dict(self.response, platforms=self.response["platforms"] * 2),
                      dict(self.response, production_accepted=True), dict(self.response, feature_id="other")):
            self.assertTrue(response_errors(self.task, value))

    def test_nonunknown_needs_source_and_source_strength(self):
        row = self.response["platforms"][0]
        row["signal"] = "documented_mechanism"
        self.assertTrue(response_errors(self.task, self.response))
        row["signal"] = "unknown"
        self.cite_android()
        self.assertFalse(response_errors(self.task, self.response))

    def test_high_confidence_fake_results_and_unsupported_are_rejected(self):
        valid = deepcopy(self.response)
        for key, value in (("confidence", "high"), ("confidence", "medium"), ("signal", "unsupported")):
            self.response = deepcopy(valid)
            self.response["platforms"][0][key] = value
            self.assertTrue(response_errors(self.task, self.response))
        self.response = deepcopy(valid)
        self.response["platforms"][0]["device_review"]["results"] = ["pass"]
        self.assertTrue(response_errors(self.task, self.response))

    def test_wrong_platform_range_and_missing_difference_evidence_fail(self):
        row = self.cite_android()
        row["citations"][0]["end_line"] = 99999
        self.assertTrue(response_errors(self.task, self.response))
        row["citations"][0]["end_line"] = 4
        self.response["platforms"][1]["citations"] = deepcopy(row["citations"])
        self.assertTrue(response_errors(self.task, self.response))
        self.response["platforms"][1]["citations"] = []
        self.response["difference_hypotheses"] = [{"dimension": "availability", "statement": "Fixture hypothesis",
            "platforms": ["android", "ios"], "kind": "hypothesis", "confidence": "low",
            "citations": row["citations"], "open_questions": ["Missing iOS source"]}]
        self.assertIn("every compared platform", " ".join(response_errors(self.task, self.response)))

    def test_valid_sources_are_normalized_and_snapshots_checked(self):
        self.cite_android()
        self.save()
        result = check_task(self.repo, self.path)
        self.assertTrue(result["delivery_valid"])
        normalized = read_yaml(self.root / result["check_path"].replace("check.json", "normalized.json"))
        citation = normalized["platforms"][0]["citations"][0]
        self.assertIn("Synthetic source", citation["excerpt"])
        self.assertEqual(citation["source"]["url"], self.url)
        write_text(self.root / self.task["sources"][0]["local_path"], "Tampered source\n")
        self.assertFalse(check_task(self.repo, self.path)["delivery_valid"])

    def test_missing_response_duplicate_json_and_stale_inputs_fail(self):
        with self.assertRaises(OSError):
            check_task(self.repo, self.path)
        write_text(self.path.parent / "response.json", '{"feature_id":"a","feature_id":"b"}')
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            check_task(self.repo, self.path)
        write_text(self.root / "docs/first-pass-research.md", "Changed rules\n")
        with self.assertRaisesRegex(ValueError, "inputs changed"):
            load_task(self.repo, self.path)

    def test_model_deadline_and_scope_required(self):
        for model, deadline, selected in (("unqualified", self.deadline, None), ("p/m", "2000-01-01T00:00:00Z", None),
                                           ("p/m", self.deadline, []), ("p/m", self.deadline, ["missing"])):
            with self.assertRaises(ValueError):
                prepare_batch(self.repo, model, deadline, selected)

    def test_pool_completes_once_and_preserves_denominator(self):
        self.save()
        owner = self

        class Bridge:
            launches = 0

            def launch(self, path, model):
                owner.assertEqual(model, "p/m")
                self.launches += 1
                return "fixture-job"

            def status(self, job):
                return {"status": "completed", "threadId": "fixture-session"}

        bridge = Bridge()
        result = run_batch(self.repo, self.manifest_path, bridge, poll_seconds=0)
        self.assertEqual(result["counts"], {"delivered": 1})
        self.assertEqual(result["total_nodes"], 1)
        run_batch(self.repo, self.manifest_path, bridge, poll_seconds=0)
        self.assertEqual(bridge.launches, 1)
        self.assertTrue((self.directory / "reports/sample/report.md").is_file())

    def test_queue_blocks_parents_until_leaf_attempts_finish(self):
        manifest = {"tasks": [{"feature_id": "root", "role": "rollup"}, {"feature_id": "leaf", "role": "leaf"}]}
        state = {"nodes": {"root": {"status": "pending"}, "leaf": {"status": "running"}}}
        self.assertEqual(queued_nodes(manifest, state), [])
        state["nodes"]["leaf"]["status"] = "failed"
        self.assertEqual(queued_nodes(manifest, state), [manifest["tasks"][0]])

    def test_timeout_cancels_only_owned_job_and_keeps_partial_delivery(self):
        self.save()

        class Bridge:
            cancelled = []

            def status(self, job):
                return {"status": "running"}

            def cancel(self, job):
                self.cancelled.append(job)

        bridge = Bridge()
        record = {"job_id": "owned-fixture-job", "status": "running", "launched_epoch": 0, "hard_seconds": 10}
        update_job(self.repo, self.directory, bridge, "sample", record, 20, 100)
        self.assertEqual(bridge.cancelled, ["owned-fixture-job"])
        self.assertEqual(record["status"], "delivered_partial")
        self.assertFalse(record["check"]["production_accepted"])

    def test_uncertain_launch_never_retries(self):
        class Bridge:
            launches = 0

            def launch(self, path, model):
                self.launches += 1
                raise TimeoutError("Synthetic lost receipt")

        bridge = Bridge()
        result = run_batch(self.repo, self.manifest_path, bridge, poll_seconds=0)
        self.assertEqual(result["state"], "launch_uncertain")
        run_batch(self.repo, self.manifest_path, bridge, poll_seconds=0)
        self.assertEqual(bridge.launches, 1)

    def test_resume_of_interrupted_launch_stops_instead_of_duplicating(self):
        _, manifest = load_manifest(self.repo, self.manifest_path)
        state = initial_state(manifest)
        state["nodes"]["sample"]["status"] = "launching"
        write_json(self.directory / "state.json", state)
        result = run_batch(self.repo, self.manifest_path, object(), poll_seconds=0)
        self.assertEqual(result["state"], "launch_uncertain")

    def test_failed_smoke_stops_remaining_work_and_keeps_error(self):
        class Bridge:
            def launch(self, path, model):
                return "fixture-job"

            def status(self, job):
                return {"status": "failed"}

        result = run_batch(self.repo, self.manifest_path, Bridge(), poll_seconds=0)
        self.assertEqual(result["state"], "stopped_smoke_failure")
        self.assertEqual(result["counts"], {"failed": 1})

    def test_expired_batch_does_not_launch(self):
        with patch("featuretree.first_pass.runner.time.time", return_value=datetime.now(timezone.utc).timestamp() + 100000):
            result = run_batch(self.repo, self.manifest_path, object(), poll_seconds=0)
        self.assertEqual(result["state"], "deadline_reached")
        self.assertEqual(result["counts"], {"pending": 1})

    def test_pool_ramps_four_to_eight_and_never_duplicates_nodes(self):
        rows = [{"feature_id": f"leaf-{i}", "task_id": f"leaf-{i}", "role": "leaf"} for i in range(14)]
        rows += [{"feature_id": "parent", "task_id": "parent", "role": "rollup"}]
        manifest = {"run_id": "fixture", "deadline": self.deadline, "model": "p/m", "tasks": rows,
                    "concurrency": {"smoke": 4, "steady": 8}, "smoke_features": [r["feature_id"] for r in rows[:4]]}
        owner = self

        class Bridge:
            active = set()
            launched = []
            peak = 0

            def launch(self, path, model):
                fid = path.parent.name
                owner.assertNotIn(fid, self.launched)
                if fid == "parent":
                    owner.assertEqual(len(self.launched), 14)
                    owner.assertFalse(self.active)
                self.launched.append(fid)
                self.active.add(fid)
                self.peak = max(self.peak, len(self.active))
                return fid

            def status(self, job):
                self.active.remove(job)
                return {"status": "completed"}

        bridge = Bridge()
        with patch("featuretree.first_pass.runner.load_manifest", return_value=(self.manifest_path, manifest)), \
             patch("featuretree.first_pass.runner.load_task", side_effect=lambda repo, path: {
                 "task_id": path.parent.name, "model": "p/m", "budget": {"hard_seconds": 900}}), \
             patch("featuretree.first_pass.runner.check_task", return_value={"delivery_valid": True}), \
             patch("featuretree.first_pass.runner.write_report", side_effect=lambda repo, path, manifest, state: deepcopy(state)):
            result = run_batch(self.repo, self.manifest_path, bridge, poll_seconds=0)
        self.assertEqual(bridge.peak, 8)
        self.assertEqual(len(bridge.launched), 15)
        self.assertEqual(result["status"], "completed")

    def test_resume_tracks_existing_job_without_relaunch(self):
        self.save()
        _, manifest = load_manifest(self.repo, self.manifest_path)
        state = initial_state(manifest)
        state["nodes"]["sample"].update(status="running", job_id="existing", launched_epoch=datetime.now(timezone.utc).timestamp(),
                                         hard_seconds=900, attempts=1)
        write_json(self.directory / "state.json", state)

        class Bridge:
            def status(self, job):
                return {"status": "completed"}

        self.assertEqual(run_batch(self.repo, self.manifest_path, Bridge(), poll_seconds=0)["counts"], {"delivered": 1})

    def test_second_runner_is_locked_out(self):
        with (self.directory / "runner.lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with self.assertRaises(BlockingIOError):
                run_batch(self.repo, self.manifest_path, object(), poll_seconds=0)
