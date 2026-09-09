"""Traversal follows actual relationships even when identifiers are not hierarchical."""

import unittest

from featuretree.taxonomy.traversal import ancestor_chain, descendants


class TraversalTests(unittest.TestCase):
    def test_ancestry_and_descendants_follow_parent_fields(self):
        features = {"a": {"parent": None}, "b": {"parent": "a"}, "c": {"parent": "b"}}
        self.assertEqual(ancestor_chain(features, "c"), ["c", "b", "a"])
        self.assertEqual(descendants(features, "b"), {"b", "c"})

    def test_cycles_and_missing_parents_fail_without_hanging(self):
        for features in ({"a": {"parent": "b"}, "b": {"parent": "a"}}, {"a": {"parent": "missing"}}):
            with self.assertRaises(ValueError):
                ancestor_chain(features, "a")

