from copy import deepcopy
from pathlib import Path
import tempfile
import unittest

from tests.fixtures.v2_application import application, run


class PlanningGateTests(unittest.TestCase):
    def test_generic_entrypoint_cannot_bypass_formal_approval_or_freeze(self):
        with tempfile.TemporaryDirectory() as directory:
            app, snapshot, baseline = application(Path(directory))
            scope = {"definition": "Unapproved", "snapshot_id": snapshot["id"], "selection": {},
                     "mode": "formal", "inputs": {"baseline_ref": baseline}}
            for pipeline, message in (("taxonomy", "calibration approval"), ("knowledge", "validated domain freeze")):
                with self.assertRaisesRegex(ValueError, message):
                    app.planner.create({"pipeline": pipeline, "model": "test/substitute", "scopes": [scope]}, pipeline)
            self.assertEqual([], app.runner.executor.backend.calls)

    def test_same_scope_cannot_be_structurally_revised_twice_in_one_run(self):
        with tempfile.TemporaryDirectory() as directory:
            app, snapshot, baseline = application(Path(directory))
            _, check = run(app, snapshot, {"baseline_ref": baseline}, "base")
            tree = app.artifacts.get(check["tree_ref"])
            scope = {"definition": "Conflicting ownership", "snapshot_id": snapshot["id"], "selection": {},
                     "scope_root_ids": [tree["features"][0]["id"]],
                     "inputs": {"baseline_ref": baseline, "tree_ref": check["tree_ref"], "bindings_ref": check["bindings_ref"]}}
            with self.assertRaisesRegex(ValueError, "scopes overlap"):
                app.planner.create({"pipeline": "taxonomy", "model": "test/substitute", "scopes": [scope, deepcopy(scope)]}, "overlap")
