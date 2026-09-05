"""Adversarial checks for launch inputs and confirmation boundaries."""

import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from featuretree.context_checks import context_errors
from featuretree.corpus.context import build_contexts, candidates, context_input_hash
from featuretree.corpus.extract import Content, parse
from featuretree.corpus.http import request_proxies
from featuretree.corpus.store import Corpus
from featuretree.corpus.urls import platform as source_platform
from featuretree.evidence import validate_knowledge_evidence
from featuretree.generation import export_views
from featuretree.pilot_review import pilot_errors
from featuretree.research_profile import fingerprint
from featuretree.run_baseline import baseline_errors
from featuretree.source_policy import official_source_error
from featuretree.storage import Repository, write_json, write_yaml
from featuretree.viewer import build_snapshot
from tests.test_comparison import FIXTURE_BODY, confirmed_doc, feature


class ReadinessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = Repository(self.root)
        self.config = {"platforms": {"android": {}, "ios": {}}, "dimensions": {"availability": "支持范围"}}
        self.policy = {"primary_device_forms": ["phone"]}
        write_yaml(self.root / "config/comparison.yaml", self.config)
        write_yaml(self.root / "config/research.yaml", self.policy)
        write_yaml(self.root / "taxonomy/sample.yaml", {"features": [feature()]})
        self.doc = confirmed_doc()
        for source in self.doc["evidence"]:
            path = self.root / source["local_path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(FIXTURE_BODY)
        write_yaml(self.root / "knowledge/sample.yaml", self.doc)

    def errors(self, doc):
        return validate_knowledge_evidence({"sample": feature()}, {"sample": doc}, self.config["platforms"], self.root)

    def test_unread_sources_fabricated_excerpts_and_platform_confusion_fail(self):
        changes = [("local_path", None, "needs local_path"),
                   ("excerpt", "Not in the source.", "excerpt not found"),
                   ("url", "https://developer.apple.com/documentation/sample", "not an allowed official source")]
        for key, value, expected in changes:
            with self.subTest(key=key):
                doc = copy.deepcopy(self.doc)
                if value is None:
                    del doc["evidence"][0][key]
                else:
                    doc["evidence"][0][key] = value
                self.assertTrue(any(expected in error for error in self.errors(doc)))

    def test_negative_and_equivalence_claims_need_scope_coverage(self):
        self.doc["presence"]["ios"]["status"] = "unsupported"
        self.assertTrue(any("coverage_note" in error for error in self.errors(self.doc)))
        doc = confirmed_doc()
        del doc["comparisons"][0]["coverage_note"]
        self.assertTrue(any("coverage_note" in error for error in self.errors(doc)))

    def test_openharmony_does_not_confirm_harmonyos(self):
        url = "https://github.com/openharmony/docs/blob/" + "a" * 40 + "/reference.md"
        self.assertIn("cannot confirm", official_source_error(url, "harmonyos", "HarmonyOS"))
        self.assertIsNone(official_source_error(url, "harmonyos", "OpenHarmony"))
        self.assertIn("non-Android", official_source_error("https://firebase.google.com/docs/cloud-messaging/ios/client", "android", "Android"))
        self.assertIsNone(official_source_error("https://firebase.google.com/docs/cloud-messaging/ios/client", "ios", "iOS"))
        self.assertEqual(source_platform("https://firebase.google.com/docs/cloud-messaging/ios/client"), "ios")
        self.assertEqual(source_platform("https://developers.google.com/maps/documentation/ios-sdk/overview"), "ios")

    def test_viewer_and_export_reject_invalid_confirmations_before_publishing(self):
        self.doc["presence"]["ios"]["subject_hash"] = "0" * 64
        write_yaml(self.root / "knowledge/sample.yaml", self.doc)
        with self.assertRaisesRegex(ValueError, "subject changed"):
            build_snapshot(self.repo)
        with self.assertRaisesRegex(ValueError, "subject changed"):
            export_views(self.repo)
        self.assertFalse((self.root / "output/exports/tree.json").exists())

    def test_confirmed_fact_requires_its_platform_evidence(self):
        self.doc["facts"] = [{"id": "one", "platform": "android", "dimension": "availability",
                              "statement": "Fixture fact", "verification": "confirmed", "basis": "official_statement",
                              "rationale": "Fixture", "verified_by": "fixture", "verified_at": "2026-09-05",
                              "subject_hash": self.doc["presence"]["android"]["subject_hash"], "evidence_refs": ["ios"]}]
        self.assertTrue(any("evidence for android" in error for error in self.errors(self.doc)))

    def test_baseline_requires_official_sources_and_matching_run_date(self):
        self.assertTrue(baseline_errors(self.repo, self.config, self.policy, "2026-09-05"))
        baseline = {"run_date": "2026-09-05", "policy_hash": fingerprint(self.policy), "platforms": {}}
        for platform, presence in self.doc["presence"].items():
            baseline["platforms"][platform] = {"context": presence["context"], "verified_at": "2026-09-05",
                "verified_by": "fixture", "release_channel": "stable", "latest_stable_rationale": "Synthetic test baseline",
                "evidence": [e for e in self.doc["evidence"] if e["platform"] == platform]}
        write_json(self.root / "output/research/baseline.json", baseline)
        self.assertFalse(baseline_errors(self.repo, self.config, self.policy, "2026-09-05"))
        self.assertTrue(baseline_errors(self.repo, self.config, self.policy, "2026-09-06"))
        self.doc["presence"]["android"]["context"]["release"] = "2.0"
        write_yaml(self.root / "knowledge/sample.yaml", self.doc)
        self.assertTrue(any("does not match" in error for error in baseline_errors(self.repo, self.config, self.policy, "2026-09-05")))

    def test_pilot_accepts_explicit_unknown_but_not_uninvestigated_slots(self):
        review = {"sample": {"input_hash": "input", "verified_by": "fixture", "verified_at": "2026-09-05",
                             "scope_review": "Fixture scope", "evidence_review": "Fixture sources"}}
        write_json(self.root / "output/research/pilot-review.json", review)
        row = {"feature_id": "sample", "pilot": True, "input_hash": "input"}
        self.doc["presence"]["ios"].update(status="unknown", verification="in_review", missing_requirements=["Need version-specific proof"])
        errors, pending = pilot_errors(self.repo, [row], {"sample": self.doc}, {"sample": feature()}, self.config, "2026-09-05")
        self.assertFalse(errors)
        self.assertFalse(pending)
        self.doc["comparisons"] = []
        self.assertTrue(pilot_errors(self.repo, [row], {"sample": self.doc}, {"sample": feature()}, self.config, "2026-09-05")[0])


class ContextReadinessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.corpus = Corpus(self.root / "docs-raw/official")
        self.addCleanup(self.corpus.close)

    def save(self, url, metadata=None, body=None):
        self.corpus.add(url)
        body = body or "# Sample\n\nSample capability; test-only evidence."
        self.corpus.save(self.corpus.get(url), body.encode(), Content("Sample", body, metadata=metadata or {}), url)

    def test_explicit_non_ios_availability_excluded_but_unknown_retained(self):
        self.save("https://developer.apple.com/documentation/mac", {"availability": ["macOS: 15.0 -"]})
        self.save("https://developer.apple.com/documentation/mobile", {"availability": []}, "# Sample\nSample mobile candidate.")
        result = candidates(self.corpus, feature(), "ios", 5)
        self.assertEqual([d["url"].split("/")[-1] for d in result["documents"]], ["mobile"])
        self.assertEqual(result["applicability_exclusions"][0]["reason"], "explicitly_non_ios")
        self.assertEqual(result["documents"][0]["applicability"], "unknown")

    def test_duplicate_body_does_not_fill_multiple_candidate_slots(self):
        for name in ("one", "two"):
            self.save("https://developer.android.com/reference/" + name)
        self.assertEqual(len(candidates(self.corpus, feature(), "android", 5)["documents"]), 1)

    def test_late_download_failure_does_not_remove_newly_saved_body(self):
        url = "https://developer.android.com/reference/sample"
        self.corpus.add(url)
        queued = self.corpus.get(url)
        self.save(url)
        self.corpus.fail(queued, "Late failing request", 503)
        current = self.corpus.get(url)
        self.assertEqual(current["status"], "ready")
        self.assertIn("Sample capability", self.corpus.body(current))

    def test_ai_generated_page_summary_excluded_from_body_and_discovery(self):
        raw = b'''<h1>Sample</h1><div class="devsite-article-body">
          <devsite-key-takeaways-panel><h2 data-tooltip="Generated with AI">Page Summary</h2>
          <p>GENERATED CLAIM</p><a href="/reference/generated">Generated link</a></devsite-key-takeaways-panel>
          <p>Actual official API documentation.</p></div>'''
        content = parse(raw, "https://developer.android.com/reference/sample", "text/html")
        self.assertNotIn("GENERATED CLAIM", content.body)
        self.assertNotIn("https://developer.android.com/reference/generated", content.links)
        self.assertIn("Actual official", content.body)
        self.assertEqual(content.metadata["excluded_generated_summaries"], 1)

    def test_policy_binding_and_candidate_source_changes_invalidate_package(self):
        repo = Repository(self.root)
        config = {"platforms": {"android": {}, "ios": {}}, "dimensions": {"availability": "支持"}}
        policy = {"primary_device_forms": ["phone"]}
        write_yaml(self.root / "config/comparison.yaml", config)
        write_yaml(self.root / "config/research.yaml", policy)
        write_yaml(self.root / "taxonomy/sample.yaml", {"features": [feature()]})
        self.save("https://developer.android.com/reference/sample")
        output = self.root / "contexts"
        build_contexts(self.corpus, repo, output, limit=5)
        bundle = json.loads((output / "sample.json").read_text())
        self.assertFalse(context_errors(bundle, feature(), config, policy, self.corpus, {}))
        changed = {**feature(), "bindings": {"android": [{"id": "different"}]}}
        self.assertNotEqual(context_input_hash(feature(), config, policy), context_input_hash(changed, config, policy))
        self.assertTrue(context_errors(bundle, feature(), config, {"primary_device_forms": ["tablet"]}, self.corpus, {}))
        bundle["platforms"]["android"]["documents"][0]["excerpts"][0]["text"] = "fabricated"
        self.assertTrue(any("excerpt" in error for error in context_errors(bundle, feature(), config, policy, self.corpus, {})))


class ProxyTests(unittest.TestCase):
    def test_no_proxy_only_environment_does_not_hide_system_proxy(self):
        with patch.dict("os.environ", {"NO_PROXY": "localhost"}, clear=True), \
             patch("featuretree.corpus.http.request.proxy_bypass", return_value=False), \
             patch("featuretree.corpus.http.request.getproxies", return_value={"no": "localhost"}), \
             patch("featuretree.corpus.http.request.proxy_bypass_macosx_sysconf", return_value=False, create=True), \
             patch("featuretree.corpus.http.request.getproxies_macosx_sysconf", return_value={"https": "http://proxy.test:8080"}, create=True):
            self.assertEqual(request_proxies("https://developer.android.com/reference/sample"), {"https": "http://proxy.test:8080"})

    def test_explicit_proxy_and_bypass_are_preserved(self):
        with patch.dict("os.environ", {"HTTPS_PROXY": "http://chosen.test:8080"}, clear=True), \
             patch("featuretree.corpus.http.request.proxy_bypass", return_value=False), \
             patch("featuretree.corpus.http.request.getproxies", return_value={"https": "http://chosen.test:8080"}):
            self.assertEqual(request_proxies("https://developer.android.com/reference/sample"), {"https": "http://chosen.test:8080"})
        with patch("featuretree.corpus.http.request.proxy_bypass", return_value=True):
            self.assertEqual(request_proxies("https://localhost/sample"), {})
