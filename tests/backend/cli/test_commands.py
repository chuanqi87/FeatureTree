"""Unified commands and established scripts resolve to the same implementations."""

from contextlib import redirect_stdout
import io
import subprocess
import sys
import unittest
from unittest.mock import patch

from featuretree.cli.main import COMMANDS
from featuretree.cli.refresh import main as refresh
from featuretree.core.storage import ROOT


class CommandTests(unittest.TestCase):
    def test_every_unified_command_exposes_help_without_running_work(self):
        for command in COMMANDS:
            with self.subTest(command=command):
                result = subprocess.run([sys.executable, "-m", "featuretree", command, "--help"],
                                        cwd=ROOT, capture_output=True, text=True, timeout=15)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("usage:", result.stdout)

    def test_legacy_scripts_resolve_imports_from_outside_repository(self):
        for script in (ROOT / "scripts").glob("*.py"):
            if script.name == "_bootstrap.py":
                continue
            with self.subTest(script=script.name):
                result = subprocess.run([sys.executable, str(script), "--help"], cwd=ROOT.parent,
                                        capture_output=True, text=True, timeout=15)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("usage:", result.stdout)

    def test_refresh_help_never_initializes_or_exports_data(self):
        with patch("featuretree.cli.refresh.Repository") as repository, redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit) as stopped:
                refresh(["--help"])
            self.assertEqual(stopped.exception.code, 0)
            repository.assert_not_called()
