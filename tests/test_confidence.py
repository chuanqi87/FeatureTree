"""Synthetic tests only: never assign confidence to the repository's platform facts."""

import copy
import hashlib
from pathlib import Path
import tempfile
import unittest

from featuretree.comparison import new_knowledge
from featuretree.confidence import assessment_input_hash, claim_rows, device_state, fingerprint, quality_summary
from featuretree.evidence import validate_knowledge_evidence
from featuretree.review_scope import build_scope
from featuretree.storage import ROOT
from featuretree.validation import schema_validators
from tests.test_comparison import FIXTURE_BODY, confirmed_doc, feature


class ConfidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.doc = confirmed_doc()
        self.claim = self.doc["presence"]["android"]
        self.validator = schema_validators(ROOT)["knowledge"]
        for source in self.doc["evidence"]:
            path = self.root / source["local_path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(FIXTURE_BODY)

    def errors(self):
        schema = list(self.validator.iter_errors(self.doc))
        return [e.message for e in schema] if schema else validate_knowledge_evidence(
            {"sample": feature()}, {"sample": self.doc}, self.doc["presence"], self.root)

    def regrade(self):
        self.claim["assessment"]["input_hash"] = assessment_input_hash(feature(), self.doc, self.claim, ["android"])

    def plan(self):
        review = {"requirement": "required", "reason": "Synthetic hardware-sensitive behavior.", "cases": [{
            "id": "phone-a", "platform": "android", "context": copy.deepcopy(self.claim["context"]),
            "device_model": "Fixture physical phone A", "os_build": "fixture-build-1",
            "conditions": ["Test account and default permission state"], "steps": ["Perform the fixture operation"],
            "expected": "Observe the fixture event"}]}
        self.claim["assessment"]["device_review"] = review
        return review

    def record(self, outcome="pass"):
        review = self.plan()
        artifact = self.root / "output/research/device-reviews/fixture.txt"
        artifact.parent.mkdir(parents=True)
        artifact.write_bytes(b"Synthetic test record only; no real device was tested.")
        review["results"] = [{"case_id": "phone-a", "plan_hash": fingerprint(review["cases"][0]),
            "claim_hash": assessment_input_hash(feature(), self.doc, self.claim, ["android"]),
            "outcome": outcome, "observed": "Fixture observation", "method": "human_physical_device",
            "tested_by": "fixture-human", "tested_at": "2026-09-05T00:00:00Z",
            "artifact_path": artifact.relative_to(self.root).as_posix(),
            "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest()}]
        return review

    def test_old_documents_and_missing_slots_remain_unassessed(self):
        doc = new_knowledge(feature(), ["android", "ios"])
        rows = claim_rows(feature(), doc, doc["presence"])
        summary = quality_summary(rows)
        self.assertEqual(summary["total"], 3)
        self.assertEqual(summary["counts"]["unassessed"], 3)
        self.assertTrue(all(r["device_state"] == "unassessed" for r in rows))
        self.assertNotIn("assessment", doc["presence"]["android"])

    def test_high_document_confidence_can_still_need_physical_review(self):
        self.plan()
        self.assertFalse(self.errors())
        row = claim_rows(feature(), self.doc, self.doc["presence"])[0]
        self.assertEqual((row["confidence"], row["device_state"], row["priority"]), ("high", "pending", 1))

    def test_high_cannot_replace_confirmation_or_missing_evidence(self):
        self.claim["verification"] = "in_review"
        self.regrade()
        self.assertTrue(any("High confidence requires confirmed" in e for e in self.errors()))
        self.claim["assessment"]["confidence"] = "medium"
        self.assertFalse(self.errors())
        self.claim["evidence_refs"] = []
        self.regrade()
        self.assertTrue(any("evidence for android" in e for e in self.errors()))

    def test_confirmed_claim_requires_grade_and_reason(self):
        del self.claim["assessment"]
        self.assertTrue(any("requires confidence" in e for e in self.errors()))
        self.claim["assessment"] = {"confidence": "high"}
        self.assertTrue(self.errors())

    def test_unknown_cannot_be_high_or_medium(self):
        self.claim.update(status="unknown", verification="in_review")
        self.claim["assessment"]["confidence"] = "medium"
        self.regrade()
        self.assertTrue(any("Unknown conclusion" in e for e in self.errors()))

    def test_high_cannot_hide_evidence_gaps(self):
        self.claim["missing_requirements"] = ["Unverified condition"]
        self.regrade()
        self.assertTrue(any("cannot hide" in e for e in self.errors()))

    def test_claim_sources_and_context_changes_invalidate_grading(self):
        self.doc["evidence"][0]["revision"] = "sdk-2.0"
        self.assertTrue(any("assessment input changed" in e for e in self.errors()))

    def test_required_review_needs_plan_and_all_platforms(self):
        review = self.plan()
        review["cases"] = []
        self.assertTrue(self.errors())
        review = self.plan()
        self.doc["comparisons"][0]["assessment"]["device_review"] = review
        self.assertTrue(any("exactly the claim platforms" in e for e in self.errors()))

    def test_results_require_human_artifact_and_current_case(self):
        review = self.record()
        self.assertFalse(self.errors())
        self.assertEqual(device_state(review), "passed")
        review["cases"][0]["steps"].append("Changed operation")
        self.assertTrue(any("changed device case" in e for e in self.errors()))

    def test_regrading_does_not_reuse_tests_for_a_different_claim(self):
        self.record()
        self.claim["rationale"] = "Changed claim meaning"
        self.regrade()
        self.assertTrue(any("another claim" in e for e in self.errors()))

    def test_simulator_missing_or_tampered_artifact_cannot_pass(self):
        review = self.record()
        result = review["results"][0]
        result["method"] = "simulator"
        self.assertTrue(self.errors())
        result["method"] = "human_physical_device"
        result["sha256"] = "0" * 64
        self.assertTrue(any("artifact hash mismatch" in e for e in self.errors()))
        result["artifact_path"] = "../../private.txt"
        self.assertTrue(any("artifact unavailable" in e for e in self.errors()))

    def test_one_pass_does_not_close_uncovered_samples(self):
        review = self.record()
        other = {**review["cases"][0], "id": "phone-b", "device_model": "Fixture physical phone B"}
        review["cases"].append(other)
        self.assertFalse(self.errors())
        self.assertEqual(device_state(review), "pending")

    def test_device_conflict_requires_downgrade_and_takes_triage_priority(self):
        self.record("fail")
        self.assertTrue(any("require low confidence" in e for e in self.errors()))
        self.claim["assessment"]["confidence"] = "low"
        self.assertFalse(self.errors())
        rows = claim_rows(feature(), self.doc, self.doc["presence"])
        self.assertEqual(quality_summary(rows)["level"], "low")
        self.assertEqual(rows[0]["priority"], 0)

    def test_pass_does_not_raise_confidence_automatically(self):
        self.record()
        self.claim["assessment"]["confidence"] = "low"
        self.assertFalse(self.errors())
        row = claim_rows(feature(), self.doc, self.doc["presence"])[0]
        self.assertEqual((row["confidence"], row["device_state"]), ("low", "passed"))

    def test_missing_grade_cannot_be_averaged_away(self):
        self.doc["comparisons"] = []
        summary = quality_summary(claim_rows(feature(), self.doc, self.doc["presence"]))
        self.assertEqual(summary["level"], "unassessed")
        self.assertEqual(summary["counts"], {"high": 2, "medium": 0, "low": 0, "unassessed": 1})

    def test_scope_filters_same_claim_and_respects_budget_and_empty_results(self):
        self.plan()
        self.claim["assessment"]["confidence"] = "low"
        args = ({"sample": feature()}, {"sample": self.doc}, self.doc["presence"])
        self.assertEqual(build_scope(*args, confidence="high", device_review="required")["selected_claims"], 0)
        scope = build_scope(*args, limit=1)
        self.assertEqual(scope["claims"][0]["claim_id"], "support:android")
        self.assertEqual((scope["selected_claims"], scope["omitted_claims"]), (1, 2))
        self.assertEqual(build_scope(*args, role="rollup")["feature_ids"], [])
        with self.assertRaises(ValueError):
            build_scope(*args, domain="missing")
        with self.assertRaises(ValueError):
            build_scope(*args, limit=0)
