"""Diagnostic probes validate delivery and provenance without upgrading knowledge."""

from copy import deepcopy
import json
import unittest

from featuretree.corpus.context import build_contexts
from featuretree.corpus.extract import Content
from featuretree.corpus.store import Corpus
from featuretree.research_probe import check_probe, prepare_probe
from featuretree.research_probe_validation import response_errors
from featuretree.storage import write_json, write_text
from tests import test_readiness


class ResearchProbeTests(unittest.TestCase):
    def setUp(self):
        test_readiness.ReadinessTests.setUp(self)
        self.corpus = Corpus(self.root / "docs-raw/official")
        self.addCleanup(self.corpus.close)
        self.url = "https://developer.android.com/reference/fixture"
        self.corpus.add(self.url)
        self.corpus.save(self.corpus.get(self.url), b"raw test data",
                         Content("Sample", "# Sample\n\nSynthetic source observation.\nOnly a fixture.\n"), self.url)
        build_contexts(self.corpus, self.repo, self.root / "output/contexts")
        self.spec = {"feature_id": "sample", "questions": [
            {"id": "q1", "platform": "android", "question": "Describe this fixture", "source_ids": ["s1"]}],
            "sources": [{"id": "s1", "url": self.url, "ranges": [[1, 4]]}]}
        self.path, self.bundle = prepare_probe(self.repo, self.corpus, self.spec, "p/m", "2026-09-06")
        self.answer = {"probe_id": self.bundle["probe_id"], "answers": [{
            "question_id": "q1", "observation": "Synthetic observation, not actual research",
            "conditions": ["Test only"], "not_established": ["No platform behavior proven"],
            "missing_requirements": ["Real-world sources and baseline"], "confidence": "low",
            "confidence_reason": "Synthetic fixture",
            "citations": [{"source_id": "s1", "locator": "Sample", "start_line": 3, "end_line": 4}],
            "device_review": {"requirement": "not_required", "reason": "Synthetic static fixture", "cases": []}}]}

    def save_answer(self):
        write_json(self.path.parent / "response.json", self.answer)

    def test_metadata_and_excerpt_are_machine_assembled_not_confirmed(self):
        original = (self.root / "knowledge/sample.yaml").read_bytes()
        self.save_answer()
        result = check_probe(self.repo, self.path)
        self.assertTrue(result["response_contract_valid"])
        self.assertFalse(result["semantic_review_passed"])
        self.assertFalse(result["production_accepted"])
        record = json.loads((self.root / result["normalized_output"]).read_text())
        citation = record["answers"][0]["citations"][0]
        self.assertEqual(citation["excerpt"], "Synthetic source observation.\nOnly a fixture.")
        self.assertEqual(citation["source"]["url"], self.url)
        self.assertFalse(citation["source"]["version_verified"])
        self.assertEqual(original, (self.root / "knowledge/sample.yaml").read_bytes())

    def test_same_packet_is_idempotent_and_changed_question_gets_new_id(self):
        path, _ = prepare_probe(self.repo, self.corpus, self.spec, "p/m", "2026-09-06")
        self.assertEqual(path, self.path)
        spec = deepcopy(self.spec)
        spec["questions"][0]["question"] = "Different fixture question"
        path, _ = prepare_probe(self.repo, self.corpus, spec, "p/m", "2026-09-06")
        self.assertNotEqual(path, self.path)

    def test_scope_id_missing_and_duplicate_answers_rejected(self):
        for case in (dict(self.answer, probe_id="wrong"), dict(self.answer, answers=[]),
                     dict(self.answer, answers=self.answer["answers"] * 2)):
            self.assertTrue(response_errors(self.bundle, case))

    def test_unassigned_source_outside_range_and_blank_citation_rejected(self):
        for citation in ({"source_id": "other", "start_line": 3, "end_line": 4},
                         {"source_id": "s1", "start_line": 1, "end_line": 5},
                         {"source_id": "s1", "start_line": 4, "end_line": 3},
                         {"source_id": "s1", "start_line": 2, "end_line": 2}):
            answer = deepcopy(self.answer)
            answer["answers"][0]["citations"][0].update(citation)
            self.assertTrue(response_errors(self.bundle, answer))

    def test_unearned_confidence_and_test_results_rejected(self):
        for level in ("high", "medium"):
            self.answer["answers"][0]["confidence"] = level
            self.assertTrue(response_errors(self.bundle, self.answer))
        self.answer["answers"][0]["confidence"] = "low"
        self.answer["answers"][0]["device_review"]["results"] = [{"outcome": "pass"}]
        self.assertTrue(response_errors(self.bundle, self.answer))

    def test_required_device_review_needs_plan(self):
        review = self.answer["answers"][0]["device_review"]
        review["requirement"] = "required"
        self.assertTrue(response_errors(self.bundle, self.answer))
        review["cases"] = [{"device_model": "待选手机", "os_build": "待选正式构建",
                            "conditions": ["Fixture"], "steps": ["Fixture step"], "expected": "Fixture"}]
        self.assertFalse(response_errors(self.bundle, self.answer))

    def test_corrupt_snapshot_and_stale_rules_fail(self):
        self.save_answer()
        record = self.bundle["sources"][0]["source"]
        write_text(self.root / record["local_path"], "# Sample\n\nTampered.\nOnly a fixture.\n")
        self.assertFalse(check_probe(self.repo, self.path)["response_contract_valid"])
        write_text(self.root / "docs/research-runbook.md", "Changed rule\n")
        with self.assertRaisesRegex(ValueError, "inputs changed"):
            check_probe(self.repo, self.path)

    def test_missing_response_and_duplicate_json_keys_fail(self):
        with self.assertRaises(OSError):
            check_probe(self.repo, self.path)
        write_text(self.path.parent / "response.json", '{"probe_id":"one","probe_id":"two"}')
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            check_probe(self.repo, self.path)

    def test_tampered_packet_cross_platform_and_overlapping_ranges_fail(self):
        packet = deepcopy(self.bundle)
        packet["questions"][0]["question"] = "Altered"
        write_json(self.path, packet)
        with self.assertRaisesRegex(ValueError, "identity"):
            check_probe(self.repo, self.path)
        for field, value in (("platform", "ios"), ("source_ids", ["missing"])):
            spec = deepcopy(self.spec)
            spec["questions"][0][field] = value
            with self.assertRaisesRegex(ValueError, "platform mismatch"):
                prepare_probe(self.repo, self.corpus, spec, "p/m", "2026-09-06")
        spec = deepcopy(self.spec)
        spec["sources"][0]["ranges"] = [[1, 3], [3, 4]]
        with self.assertRaisesRegex(ValueError, "line range"):
            prepare_probe(self.repo, self.corpus, spec, "p/m", "2026-09-06")

    def test_changed_question_or_range_is_not_silently_reused(self):
        self.save_answer()
        first = check_probe(self.repo, self.path)
        self.answer["answers"][0]["observation"] += " revised"
        self.save_answer()
        second = check_probe(self.repo, self.path)
        self.assertNotEqual(first["normalized_output"], second["normalized_output"])
        self.assertTrue((self.root / first["normalized_output"]).exists())
