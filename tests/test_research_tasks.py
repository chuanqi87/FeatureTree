"""Work-package isolation and launch gating are enforced, not just prompted."""

from copy import deepcopy
import unittest

from featuretree.research_contract import methodology_hash
from featuretree.research_profile import fingerprint, research_policy
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

    def test_evidence_stage_is_delivery_only_and_does_not_need_candidate(self):
        path, task = prepare_task(self.repo, "sample", "p/m", "2026-09-06", stage="evidence")
        self.assertFalse(check_task(self.repo, path)["delivery_valid"])
        write_text(self.root / task["report_path"], "Fixture evidence notes, not accepted knowledge.\n")
        result = check_task(self.repo, path)
        self.assertTrue(result["delivery_valid"])
        self.assertNotIn("structurally_valid", result)
        self.assertFalse(result["semantic_review_passed"])
        self.assertFalse(result["production_accepted"])

    def test_stage_and_scope_have_distinct_immutable_ids(self):
        _, task = prepare_task(self.repo, "sample", "p/m", "2026-09-06", claim_ids=["support:android"])
        _, report = prepare_task(self.repo, "sample", "p/m", "2026-09-06", stage="evidence")
        self.assertEqual(task["claim_ids"], ["support:android"])
        self.assertEqual(task["selection"], "claims")
        self.assertNotEqual(task["task_id"], report["task_id"])
        with self.assertRaises(ValueError):
            prepare_task(self.repo, "sample", "p/m", "2026-09-06", claim_ids=["missing"])
        with self.assertRaises(ValueError):
            prepare_task(self.repo, "sample", "p/m", "2026-09-06", claim_ids=[])

    def test_scope_cannot_change_other_claims(self):
        from featuretree.confidence import assessment_input_hash
        from tests.test_comparison import feature
        _, task = prepare_task(self.repo, "sample", "p/m", "2026-09-06", claim_ids=["support:android"])
        candidate = deepcopy(self.doc)
        claim = candidate["presence"]["ios"]
        claim["rationale"] = "Changed unselected statement"
        claim["assessment"]["input_hash"] = assessment_input_hash(feature(), candidate, claim, ["ios"])
        self.assertIn("unselected claim changed", " ".join(candidate_errors(self.repo, task, candidate)))

    def test_scope_identity_cannot_be_expanded_in_place(self):
        self.task["claim_ids"] = ["support:android"]
        write_json(self.path, self.task)
        with self.assertRaisesRegex(ValueError, "identity"):
            load_task(self.repo, self.path)

    def test_existing_fact_cannot_be_deleted_even_if_selected(self):
        self.doc["facts"] = [{"id": "existing", "platform": "android", "dimension": "availability",
                              "statement": "Unreviewed fixture fact", "verification": "unreviewed",
                              "evidence_refs": []}]
        write_yaml(self.root / "knowledge/sample.yaml", self.doc)
        candidate = deepcopy(self.doc)
        candidate["facts"] = []
        for selected in (["support:android"], ["fact:existing"]):
            with self.subTest(selected=selected):
                _, task = prepare_task(self.repo, "sample", "p/m", "2026-09-06", claim_ids=selected)
                self.assertIn("existing claim removed", " ".join(candidate_errors(self.repo, task, candidate)))

    def test_valid_pinned_partial_candidate_passes_structure_not_production(self):
        baseline = {"run_date": "2026-09-06", "policy_hash": fingerprint(research_policy(self.repo)), "platforms": {}}
        for platform, presence in self.doc["presence"].items():
            baseline["platforms"][platform] = {
                "context": presence["context"], "verified_at": "2026-09-06", "verified_by": "fixture",
                "release_channel": "stable", "latest_stable_rationale": "Synthetic fixture only",
                "evidence": [item for item in self.doc["evidence"] if item["platform"] == platform]}
        write_json(self.root / "output/research/baseline.json", baseline)
        path, task = prepare_task(self.repo, "sample", "p/m", "2026-09-06", claim_ids=["support:android"])
        write_yaml(self.root / task["candidate_path"], self.doc)
        write_text(self.root / task["report_path"], "Synthetic fixture, not actual research.\n")
        result = check_task(self.repo, path)
        self.assertTrue(result["structurally_valid"], result["errors"])
        self.assertFalse(result["production_accepted"])
