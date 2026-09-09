"""Scope queries stay bounded, diverse and traceable to intact source bytes."""

import hashlib
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import patch

from featuretree.workflow.retrieval import build_context, research_queries, select_sources


def row(url, title, body_hash, metadata=None):
    return {"url": url, "title": title, "body_sha256": body_hash, "metadata": metadata or {},
            "retrieval_score": 1, "body_path": "body.md"}


class RetrievalTests(unittest.TestCase):
    def test_scope_plan_overrides_ambiguous_domain_terms(self):
        work = {"node_id": "sample", "subtree": {"sample": {"name": {"en": "Print and Scan", "zh": "打印扫描"},
                "comparison_scope": {"includes": ["打印、扫描"]}}}}
        self.assertEqual(research_queries(work, "android", {"research_queries": {"android": ["android.print"]}}), ["android.print"])

    def test_queries_share_budget_and_exact_modules_outrank_change_logs(self):
        rows = [row("https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changes", "Changes", "one"),
                row("https://developer.huawei.com/consumer/cn/doc/harmonyos-references/print", "@ohos.print", "two")]
        scan = row("https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan", "@ohos.scan", "three")
        with patch("featuretree.workflow.retrieval.search", side_effect=[rows, [scan]]):
            chosen, _ = select_sources(None, ["@ohos.print", "@ohos.scan"], "harmonyos", limit=2)
        self.assertEqual([item[1]["title"] for item in chosen], ["@ohos.print", "@ohos.scan"])

    def test_non_ios_sources_are_excluded_and_corrupt_bodies_become_gaps(self):
        work = {"node_id": "sample", "subtree": {"sample": {"name": {"en": "print", "zh": "打印"}, "comparison_scope": {"includes": []}}}}
        mac = row("https://developer.apple.com/documentation/appkit/printing", "Printing", "mac", {"platforms": ["macOS"]})
        ios = row("https://developer.apple.com/documentation/uikit/printing", "Printing", hashlib.sha256(b"expected").hexdigest())
        with tempfile.TemporaryDirectory() as directory:
            corpus = SimpleNamespace(root=Path(directory))
            (corpus.root / "body.md").write_text("modified")
            with patch("featuretree.workflow.retrieval.search", return_value=[mac, ios]):
                context = build_context(corpus, work, "ios", {"research_queries": {"ios": ["printing"]}})
            self.assertEqual(context["sources"], [])
            self.assertEqual(len(context["exclusions"]), 1)
            self.assertIn("Body hash mismatch", context["gaps"][0])

    def test_verbose_real_queries_reduce_to_specific_search_keys(self):
        from featuretree.workflow.queries import compact_query
        self.assertEqual(compact_query('UIPrintInteractionController UIPrintInfo UIPrintFormatter UIKit printing API reference'), 'UIPrintInteractionController')
        self.assertEqual(compact_query('HarmonyOS PrintKit 打印框架 @ohos.print 打印任务'), '@ohos.print')
        self.assertEqual(compact_query('HarmonyOS 文档扫描 Vision Kit 文档扫描能力 扫描参数 API'), '文档扫描')
        self.assertEqual(compact_query('Android document scanner API Google Play services Document Scanner ML Kit public API'), 'document scanner')
        self.assertEqual(compact_query('custom document printing'), 'custom document printing')

    def test_empty_query_match_records_a_gap(self):
        gaps = []
        with patch('featuretree.workflow.retrieval.search', return_value=[]):
            selected, _ = select_sources(None, ['MissingPublicSymbol'], 'android', gaps=gaps)
        self.assertEqual(selected, [])
        self.assertIn('does not imply unsupported', gaps[0])
