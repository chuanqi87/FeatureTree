import copy
import hashlib
from pathlib import Path
import tempfile
import unittest

from featuretree.comparison import new_knowledge, progress, subject_hash
from featuretree.confidence import assessment_input_hash, claim_slots
from featuretree.evidence import validate_knowledge_evidence
from featuretree.storage import ROOT
from featuretree.validation import schema_validators

FIXTURE_BODY = b"# Sample capability\n\nSynthetic evidence used only in tests.\n"


def feature():
    return {"schema_version": 2, "id": "sample", "parent": None, "level": "L1",
            "name": {"zh": "样例能力", "en": "Sample"}, "definition": "完成样例任务。",
            "knowledge_role": "leaf", "knowledge_path": "knowledge/sample.yaml",
            "comparison_scope": {"includes": ["样例任务"], "excludes": []},
            "comparison_dimensions": ["availability"]}


def confirmed_doc():
    """Synthetic claims and source metadata; no downloaded platform evidence."""
    doc = new_knowledge(feature(), ["android", "ios"])
    urls = {"android": "https://developer.android.com/reference/fixture",
            "ios": "https://developer.apple.com/documentation/fixture"}
    for platform in doc["presence"]:
        context = {"release": "1.0", "sdk": "1.0", "distribution": platform, "device_forms": ["phone"]}
        doc["presence"][platform] = {
            "status": "supported", "verification": "confirmed", "rationale": "测试用已核实能力。",
            "context": context, "evidence_refs": [platform], "verified_by": "fixture", "verified_at": "2026-09-05",
            "subject_hash": subject_hash(feature()), "basis": "official_statement"}
        doc["evidence"].append({"id": platform, "platform": platform, "title": "Fixture",
                                "url": urls[platform], "locator": "Sample capability",
                                "revision": "sdk-1.0", "applies_to": copy.deepcopy(context),
                                "local_path": f"docs-raw/fixtures/{platform}.md",
                                "sha256": hashlib.sha256(FIXTURE_BODY).hexdigest(),
                                "fetched_at": "2026-09-05T00:00:00Z",
                                "excerpt": "Synthetic evidence used only in tests.",
                                "applicability_note": "Fixture-only SDK 1.0 scope.",
                                "source_kind": "api_reference"})
    doc["comparisons"] = [{"dimension": "availability", "platforms": ["android", "ios"],
                            "result": "same", "verification": "confirmed", "scope": "样例任务",
                            "rationale": "双方在指定条件下满足任务。", "evidence_refs": ["android", "ios"],
                            "verified_by": "fixture", "verified_at": "2026-09-05", "subject_hash": subject_hash(feature()),
                            "basis": "evidence_based_analysis", "coverage_note": "Both synthetic platform fixtures checked."}]
    for _, _, _, platforms, claim in claim_slots(feature(), doc, doc["presence"]):
        claim["assessment"] = {
            "confidence": "high", "rationale": "Synthetic reviewed fixture, not platform research.",
            "assessed_by": "fixture", "assessed_at": "2026-09-05",
            "input_hash": assessment_input_hash(feature(), doc, claim, platforms),
            "device_review": {"requirement": "not_required", "reason": "Synthetic document-only fixture."}}
    return doc


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
