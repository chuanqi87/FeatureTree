"""Work-package isolation and launch gating are enforced, not just prompted."""

from copy import deepcopy
import unittest

from featuretree.research_contract import methodology_hash
from featuretree.research_tasks import candidate_errors, check_task, load_task, prepare_task
from featuretree.storage import write_json, write_text, write_yaml
from tests import test_readiness


class ResearchTaskTests(unittest.TestCase):
    def setUp(self):
        test_readiness.ReadinessTests.setUp(self)
        write_json(self.root / "output/contexts/sample.json", {"feature_id": "sample"})
        self.path, self.task = prepare_task(self.repo, "sample", "volcengine/glm-5.3", "2026-09-06")

    def test_explicit_model_and_existing_node_required(self):
        for fid, model in (("missing", "p/m"), ("sample", "glm5.3")):
            with self.assertRaises(ValueError):
                prepare_task(self.repo, fid, model, "2026-09-06")

    def test_same_input_is_idempotent_and_not_production_authorized(self):
        path, task = prepare_task(self.repo, "sample", "volcengine/glm-5.3", "2026-09-06")
        self.assertEqual(path, self.path)
        self.assertEqual(task, self.task)
        self.assertFalse(task["production_write_authorized"])
        self.assertEqual(task["mode"], "diagnostic_pilot")

    def test_other_feature_and_cross_task_path_cannot_be_submitted(self):
        changed = deepcopy(self.doc)
        changed["feature_id"] = "another"
        self.assertIn("different feature", " ".join(candidate_errors(self.repo, self.task, changed)))
        self.task["candidate_path"] = "knowledge/sample.yaml"
        write_json(self.path, self.task)
        with self.assertRaises(ValueError):
            load_task(self.repo, self.path)

    def test_model_identity_tampering_fails(self):
        self.task["model"] = "other/model"
        write_json(self.path, self.task)
        with self.assertRaisesRegex(ValueError, "identity"):
            load_task(self.repo, self.path)

    def test_rule_changes_invalidate_tasks(self):
        previous = methodology_hash(self.root)
        write_text(self.root / "docs/research-runbook.md", "Changed rules\n")
        self.assertNotEqual(previous, methodology_hash(self.root))
        self.assertIn("Task inputs changed", " ".join(candidate_errors(self.repo, self.task, self.doc)))

    def test_knowledge_changes_invalidate_tasks(self):
        changed = deepcopy(self.doc)
        changed["definition"] += " revised"
        write_yaml(self.root / "knowledge/sample.yaml", changed)
        self.assertIn("Task inputs changed", " ".join(candidate_errors(self.repo, self.task, self.doc)))

    def test_missing_baseline_cannot_confirm_even_valid_fixture_evidence(self):
        errors = candidate_errors(self.repo, self.task, self.doc)
        self.assertIn("unresolved launch baseline", " ".join(errors))

    def test_check_never_promotes_or_writes_production(self):
        original = (self.root / "knowledge/sample.yaml").read_bytes()
        write_yaml(self.root / self.task["candidate_path"], self.doc)
        write_text(self.root / self.task["report_path"], "Fixture report\n")
        result = check_task(self.repo, self.path)
        self.assertFalse(result["production_accepted"])
        self.assertFalse(result["semantic_review_passed"])
        self.assertEqual(original, (self.root / "knowledge/sample.yaml").read_bytes())

    def test_missing_report_is_rejected(self):
        write_yaml(self.root / self.task["candidate_path"], self.doc)
        self.assertIn("Worker report missing", check_task(self.repo, self.path)["errors"])

    def test_task_outside_staging_is_rejected(self):
        with self.assertRaises(ValueError):
            load_task(self.repo, self.root / "knowledge/sample.yaml")
