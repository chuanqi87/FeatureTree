"""Acceptance cannot substitute checkboxes or stale reviews for current evidence."""

from copy import deepcopy
import unittest

from featuretree.research_acceptance import check_acceptance, initialize_review, inspect_submission
from featuretree.research_profile import fingerprint
from featuretree.research_review import review_errors, review_template
from featuretree.research_tasks import prepare_task
from featuretree.storage import read_yaml, write_json, write_text
from tests import test_readiness


class ResearchAcceptanceTests(unittest.TestCase):
    def setUp(self):
        test_readiness.ReadinessTests.setUp(self)
        write_json(self.root / "output/contexts/sample.json", {"feature_id": "sample"})
        self.package, task = prepare_task(self.repo, "sample", "p/m", "2026-09-06",
                                          stage="evidence", claim_ids=["support:android"])
        self.report = self.root / task["report_path"]
        write_text(self.report, "Synthetic report only; does not establish platform behavior.\n")
        self.binding, self.contract = inspect_submission(self.repo, self.package)
        self.path = initialize_review(self.repo, self.package, "fixture-author", "fixture-reviewer")
        self.review = read_yaml(self.path)

    def complete_review(self):
        self.review["decision"] = "pass"
        self.review["reviewed_at"] = "2026-09-06T10:00:00+08:00"
        for row in self.review["checks"]:
            row.update(status="pass", explanation="Synthetic validator fixture, not a real semantic review.",
                       evidence_refs=["worker-report.md:1; synthetic fixture only"])

    def add_issue(self):
        row = self.review["checks"][0]
        row.update(status="fail", explanation="Synthetic missing qualifier.", evidence_refs=["worker-report.md:1"])
        issue = {"id": "r1", "target_id": row["target_id"], "criterion_id": row["criterion_id"], "status": "open",
                 "problem": "Fixture qualifier lacks support", "location": "worker-report.md:1",
                 "required_change": "Provide supporting body or keep unknown",
                 "expected_evidence": "Direct official paragraph and revised claim citation"}
        self.review["issues"].append(issue)
        return issue

    def errors(self):
        return review_errors(self.review, self.binding, self.contract)

    def check(self):
        write_json(self.path, self.review)
        return check_acceptance(self.repo, self.package, self.path)

    def test_pending_is_not_accepted_and_matrix_covers_every_target(self):
        result = self.check()
        self.assertTrue(result["review_record_valid"])
        self.assertEqual(result["state"], "awaiting_review")
        self.assertFalse(result["content_accepted"])
        contract = deepcopy(self.contract)
        contract["scope"]["target_ids"].append("support:ios")
        review = review_template(self.binding, contract, "author", "reviewer")
        self.assertEqual(len(review["checks"]), 14)
        self.assertFalse(review_errors(review, self.binding, contract))

    def test_content_acceptance_never_changes_production(self):
        original = (self.root / "knowledge/sample.yaml").read_bytes()
        self.complete_review()
        result = self.check()
        self.assertTrue(result["content_accepted"], result["errors"])
        self.assertFalse(result["production_accepted"])
        self.assertEqual(original, (self.root / "knowledge/sample.yaml").read_bytes())

    def test_self_review_and_invalid_review_time_are_rejected(self):
        self.complete_review()
        self.review["reviewer_id"] = " Fixture-Author "
        self.assertIn("self-review", " ".join(self.errors()))
        with self.assertRaises(ValueError):
            review_template(self.binding, self.contract, "AUTHOR", "author")
        self.review["reviewer_id"] = "fixture-reviewer"
        for timestamp in (None, "yesterday", "2026-09-06T10:00:00"):
            self.review["reviewed_at"] = timestamp
            self.assertIn("reviewed_at", " ".join(self.errors()))

    def test_missing_duplicate_or_foreign_checks_cannot_pass(self):
        self.complete_review()
        valid = deepcopy(self.review)
        for variant in ("missing", "duplicate", "foreign"):
            self.review = deepcopy(valid)
            if variant == "missing":
                self.review["checks"].pop()
            elif variant == "duplicate":
                self.review["checks"].append(deepcopy(self.review["checks"][0]))
            else:
                self.review["checks"][0]["target_id"] = "another"
            self.assertIn("exactly once", " ".join(self.errors()))

    def test_pending_or_failed_criterion_cannot_be_averaged_away(self):
        self.complete_review()
        self.review["checks"][0]["status"] = "pending"
        self.assertIn("no average-score", " ".join(self.errors()))
        self.add_issue()
        self.assertIn("no average-score", " ".join(self.errors()))
        self.review["decision"] = "revise"
        result = self.check()
        self.assertFalse(result["content_accepted"])
        self.assertEqual(result["state"], "needs_revision")

    def test_explanation_and_references_are_required(self):
        self.complete_review()
        self.review["checks"][0]["explanation"] = "  "
        self.assertTrue(self.errors())
        self.review["checks"][0]["explanation"] = "Fixture"
        self.review["checks"][0]["evidence_refs"] = []
        self.assertTrue(self.errors())

    def test_failed_check_needs_actionable_issue(self):
        self.complete_review()
        self.review["decision"] = "revise"
        self.review["checks"][0]["status"] = "fail"
        self.assertIn("actionable open revision issue", " ".join(self.errors()))
        self.add_issue()
        self.assertFalse(self.errors())
        valid = deepcopy(self.review)
        for field in ("problem", "location", "required_change", "expected_evidence"):
            self.review = deepcopy(valid)
            self.review["issues"][0][field] = ""
            self.assertTrue(self.errors())

    def test_issues_cannot_escape_scope_or_duplicate_ids(self):
        self.complete_review()
        self.review["decision"] = "revise"
        issue = self.add_issue()
        issue["target_id"] = "not-assigned"
        self.assertIn("outside assigned scope", " ".join(self.errors()))
        issue["target_id"] = "support:android"
        self.review["issues"].append(deepcopy(issue))
        self.assertIn("Duplicate issue", " ".join(self.errors()))

    def test_open_issue_blocks_acceptance_even_when_all_checks_pass(self):
        self.complete_review()
        self.add_issue()
        self.review["checks"][0]["status"] = "pass"
        self.assertFalse(self.check()["content_accepted"])

    def test_blocked_requires_specific_problem_and_next_action(self):
        self.complete_review()
        self.review["decision"] = "blocked"
        self.assertIn("specific missing input", " ".join(self.errors()))
        self.add_issue()
        self.assertEqual(self.check()["state"], "blocked")

    def test_malformed_records_fail_closed(self):
        for invalid in (None, [], {}, dict(self.review, checks=[None]), dict(self.review, issues=[{}]),
                        dict(self.review, checks="pass"), dict(self.review, production_accepted=True)):
            with self.subTest(invalid=invalid):
                self.assertTrue(review_errors(invalid, self.binding, self.contract))

    def test_changed_submission_invalidates_review_and_archives_original(self):
        self.complete_review()
        self.assertTrue(self.check()["content_accepted"])
        original = self.report.read_bytes()
        write_text(self.report, "Changed fixture; requires a fresh review.\n")
        result = self.check()
        self.assertFalse(result["content_accepted"])
        self.assertIn("stale", " ".join(result["errors"]))
        path = initialize_review(self.repo, self.package, "fixture-author", "fixture-reviewer")
        self.assertNotEqual(path, self.path)
        self.assertEqual(read_yaml(path)["decision"], "pending")
        archive = self.root / "output/research/acceptance/submissions" / fingerprint(self.binding)
        self.assertEqual((archive / "worker-report.md").read_bytes(), original)

    def test_repeat_init_preserves_review_and_check_history(self):
        self.check()
        self.complete_review()
        self.check()
        self.assertEqual(initialize_review(self.repo, self.package, "fixture-author", "fixture-reviewer"), self.path)
        self.assertEqual(read_yaml(self.path)["decision"], "pass")
        histories = list((self.path.parent / "checks").glob("*/review.json"))
        self.assertEqual({read_yaml(path)["decision"] for path in histories}, {"pending", "pass"})

    def test_missing_empty_or_stale_delivery_cannot_start_review(self):
        write_text(self.report, "  \n")
        with self.assertRaisesRegex(ValueError, "Machine checks failed"):
            initialize_review(self.repo, self.package, "author", "reviewer")
        write_text(self.report, "Synthetic fixture\n")
        write_text(self.root / "docs/research-acceptance.md", "Changed review rules\n")
        with self.assertRaisesRegex(ValueError, "Machine checks failed"):
            check_acceptance(self.repo, self.package, self.path)

    def test_review_path_cannot_write_into_formal_knowledge(self):
        with self.assertRaises(ValueError):
            check_acceptance(self.repo, self.package, self.root / "knowledge/sample.yaml")

    def test_archive_tampering_is_not_silently_repaired(self):
        archive = self.root / "output/research/acceptance/submissions" / fingerprint(self.binding)
        write_text(archive / "worker-report.md", "Tampered history\n")
        with self.assertRaisesRegex(ValueError, "Archived submission was altered"):
            initialize_review(self.repo, self.package, "fixture-author", "fixture-reviewer")
