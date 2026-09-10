"""Bounded input, checkpoint recovery, cancellation and merged author provenance."""

import json
from pathlib import Path
import tempfile
import unittest

from featuretree.core.io import IntegrityError
from tests.fixtures.v2_batches import BatchModel, batched_application


TASK = "w_0000--ft-android"


class BatchExecutionTests(unittest.TestCase):
    def test_inputs_are_bounded_and_retry_reuses_only_valid_completed_batches(self):
        with tempfile.TemporaryDirectory() as directory:
            backend = BatchModel(fail_index=1)
            app, initial = batched_application(Path(directory), backend)
            run_id = initial["run_id"]
            state = app.runner.run(run_id)
            self.assertEqual("failed", state["tasks"][TASK]["status"])
            self.assertEqual(1, app.runs.batch_progress(state)[TASK]["completed"])
            app.runner.action(run_id, "retry", task_id=TASK)
            state = app.runner.run(run_id)
            self.assertEqual("completed", state["tasks"][TASK]["status"])
            progress = app.run_detail(run_id)["batch_progress"][TASK]
            self.assertEqual((3, 3, 1), (progress["total"], progress["completed"], progress["reused"]))
            self.assertEqual(2, len(state["tasks"][TASK]["attempts"][-1]["metadata"]["usage"]))
            calls = [packet for packet in backend.calls if packet["stage_id"] == "ft-android"]
            self.assertEqual([0, 1, 1, 2], [packet["batch"]["index"] for packet in calls])
            for packet in calls:
                self.assertLessEqual(len(packet["work"]["api_ids"]) + len(packet["work"]["topic_ids"]), 2)
                self.assertEqual(packet["work"]["api_ids"], packet["work"]["selection"]["ids"])
                self.assertEqual(packet["work"]["api_ids"], packet["source_access"]["api_ids"])
            reference = state["tasks"][TASK]["result_ref"]
            result, packet = app.provenance.require(reference, "ft-android")
            self.assertEqual(set(packet["work"]["api_ids"]), {row["id"] for row in result["payload"]["api_dispositions"]})
            facts = result["payload"]["facts"]
            self.assertEqual(len(facts), len({fact["id"] for fact in facts}))
            # The aggregate cannot lose its child author receipts and still pass provenance.
            state["tasks"][TASK]["attempts"][-1]["metadata"].pop("batch_receipts")
            app.runs.save(state)
            with self.assertRaises(IntegrityError):
                app.provenance.require(reference, "ft-android")

    def test_semantic_revision_does_not_reuse_old_research(self):
        with tempfile.TemporaryDirectory() as directory:
            backend = BatchModel()
            app, state = batched_application(Path(directory), backend)
            run_id = state["run_id"]
            app.runner.run(run_id)
            before = [p["input_hash"] for p in backend.calls if p["stage_id"] == "ft-android"]
            app.runner.action(run_id, "revise", task_id=TASK, feedback=[{"reason": "Changed research requirements"}])
            state = app.runner.run(run_id)
            after = [p["input_hash"] for p in backend.calls if p["stage_id"] == "ft-android"][3:]
            self.assertEqual(3, len(after))
            self.assertFalse(set(before) & set(after))
            self.assertEqual(0, app.runs.batch_progress(state)[TASK]["reused"])

    def test_corrupted_checkpoint_cannot_be_reused(self):
        with tempfile.TemporaryDirectory() as directory:
            backend = BatchModel(fail_index=1)
            app, state = batched_application(Path(directory), backend)
            run_id = state["run_id"]
            app.runner.run(run_id)
            path = next((app.runs.folder(run_id) / "batch-checkpoints" / TASK).glob("*.json"))
            record = json.loads(path.read_text())
            record["input_hash"] = "0" * 64
            path.write_text(json.dumps(record))
            count = len(backend.calls)
            app.runner.action(run_id, "retry", task_id=TASK)
            state = app.runner.run(run_id)
            self.assertEqual(count, len(backend.calls))
            self.assertEqual("failed", state["tasks"][TASK]["status"])

    def test_cancellation_keeps_the_finished_batch_and_starts_no_next_batch(self):
        with tempfile.TemporaryDirectory() as directory:
            backend = BatchModel(cancel=True)
            app, state = batched_application(Path(directory), backend)
            state = app.runner.run(state["run_id"])
            self.assertEqual("cancelled", state["status"])
            self.assertEqual(1, len(backend.calls))
            self.assertEqual(1, app.runs.batch_progress(state)[TASK]["completed"])
