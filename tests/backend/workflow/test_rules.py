"""Nested policy changes must invalidate saved work after package reorganization."""

from pathlib import Path
import tempfile
import unittest

from featuretree.workflow.state import rule_hash


class RuleFingerprintTests(unittest.TestCase):
    def test_nested_rules_and_baselines_are_hashed_but_outputs_are_not(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            previous = rule_hash(root)
            for relative in ("docs/workflow/design.md", "config/workflow/baselines/verified.json", "config/comparison.yaml"):
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("fixture rule")
                current = rule_hash(root)
                self.assertNotEqual(previous, current, relative)
                previous = current
            (root / "output").mkdir()
            (root / "output/report.md").write_text("generated")
            self.assertEqual(previous, rule_hash(root))

