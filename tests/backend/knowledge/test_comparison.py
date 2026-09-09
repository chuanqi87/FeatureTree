"""tests.backend.knowledge.test_comparison."""

import copy
from pathlib import Path
import tempfile
import unittest
from featuretree.knowledge.comparison import new_knowledge, progress
from featuretree.knowledge.evidence import validate_knowledge_evidence
from featuretree.core.storage import ROOT
from featuretree.core.schemas import schema_validators
from tests.fixtures.knowledge import FIXTURE_BODY, confirmed_doc, feature


class ComparisonTests(unittest.TestCase):
    def setUp(self):
        self.validator = schema_validators(ROOT)["knowledge"]
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for source in confirmed_doc()["evidence"]:
            path = self.root / source["local_path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(FIXTURE_BODY)

    def test_same_support_does_not_infer_same_behavior(self):
        doc = confirmed_doc()
        doc["comparisons"] = []
        self.assertEqual(progress(feature(), doc, doc["presence"])["conclusion"], "unknown")

    def test_reviewed_article_does_not_confirm_comparisons(self):
        doc = new_knowledge(feature(), ["android", "ios"])
        doc["status"] = "reviewed"
        self.assertEqual(progress(feature(), doc, doc["presence"])["state"], "not_started")

    def test_tentative_difference_is_not_a_confirmed_difference(self):
        doc = confirmed_doc()
        doc["comparisons"][0].update(result="different", verification="in_review")
        result = progress(feature(), doc, doc["presence"])
        self.assertEqual(result["conclusion"], "unknown")
        self.assertEqual(result["state"], "in_progress")

    def test_complete_same_requires_every_dimension_and_platform(self):
        doc = confirmed_doc()
        self.assertEqual(progress(feature(), doc, doc["presence"])["conclusion"], "confirmed_same")
        f = feature()
        f["comparison_dimensions"].append("permissions_privacy")
        self.assertEqual(progress(f, doc, doc["presence"])["conclusion"], "unknown")

    def test_unknown_cannot_be_confirmed(self):
        doc = confirmed_doc()
        doc["presence"]["ios"]["status"] = "unknown"
        self.assertTrue(list(self.validator.iter_errors(doc)))

    def test_confirmed_conditional_support_requires_conditions(self):
        doc = confirmed_doc()
        doc["presence"]["ios"]["status"] = "conditional"
        self.assertTrue(list(self.validator.iter_errors(doc)))
        doc["presence"]["ios"]["conditions"] = ["运行于指定设备"]
        self.assertFalse(list(self.validator.iter_errors(doc)))

    def test_confirmation_requires_both_platform_sources(self):
        doc = confirmed_doc()
        doc["comparisons"][0]["evidence_refs"] = ["android"]
        errors = validate_knowledge_evidence({"sample": feature()}, {"sample": doc}, doc["presence"], self.root)
        self.assertTrue(any("evidence for ios" in e for e in errors))

    def test_fixed_context_and_evidence_version_must_match(self):
        doc = confirmed_doc()
        doc["presence"]["ios"]["context"]["sdk"] = "2.0"
        errors = validate_knowledge_evidence({"sample": feature()}, {"sample": doc}, doc["presence"], self.root)
        self.assertTrue(any("context mismatch" in e for e in errors))

    def test_master_revision_cannot_confirm_claim(self):
        doc = confirmed_doc()
        doc["evidence"][0]["revision"] = "master"
        errors = validate_knowledge_evidence({"sample": feature()}, {"sample": doc}, doc["presence"], self.root)
        self.assertTrue(any("Unpinned source" in e for e in errors))

    def test_duplicate_pair_reversed_order_is_rejected(self):
        doc = confirmed_doc()
        other = copy.deepcopy(doc["comparisons"][0])
        other["platforms"].reverse()
        doc["comparisons"].append(other)
        errors = validate_knowledge_evidence({"sample": feature()}, {"sample": doc}, doc["presence"], self.root)
        self.assertTrue(any("Duplicate comparison" in e for e in errors))

    def test_complete_valid_claim_passes(self):
        doc = confirmed_doc()
        self.assertFalse(list(self.validator.iter_errors(doc)))
        self.assertFalse(validate_knowledge_evidence({"sample": feature()}, {"sample": doc}, doc["presence"], self.root))

    def test_changed_capability_scope_invalidates_old_confirmation(self):
        doc = confirmed_doc()
        changed = feature()
        changed["comparison_scope"]["includes"].append("新增能力要求")
        errors = validate_knowledge_evidence({"sample": changed}, {"sample": doc}, doc["presence"], self.root)
        self.assertTrue(any("subject changed" in e for e in errors))

    def test_fourth_platform_needs_no_schema_change(self):
        doc = new_knowledge(feature(), ["android", "ios", "harmonyos", "web"])
        self.assertFalse(list(self.validator.iter_errors(doc)))
        self.assertEqual(progress(feature(), doc, doc["presence"])["total_comparisons"], 6)
