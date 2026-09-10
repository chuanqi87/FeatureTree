"""Exercise provider diagnostics and isolated workspaces without paid model calls."""

import json
from pathlib import Path
import sys
import tempfile
import unittest

from featuretree.core.io import ConflictError, read_json
from featuretree.workflow.backends.opencode import OpenCodeBackend
from featuretree.workflow.backends.provider_errors import ProviderError, provider_error
from featuretree.workflow.backends.runtime import prepare_runtime


class ProviderRuntimeTests(unittest.TestCase):
    def test_account_failure_keeps_status_and_does_not_retry(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            executable = root / "fake-opencode"
            event = {"type": "error", "error": {"data": {"statusCode": 402,
                     "message": "Insufficient Balance", "isRetryable": True}}}
            executable.write_text(f"#!{sys.executable}\nimport sys\nsys.stdin.read()\nprint({json.dumps(event)!r})\nsys.exit(1)\n")
            executable.chmod(0o755)
            with self.assertRaisesRegex(ProviderError, "402.*Insufficient Balance") as failure:
                OpenCodeBackend(str(executable)).execute(root, "fk-scope", {}, root, 5, "test/provider", None)
            self.assertFalse(failure.exception.retryable)
            self.assertEqual(402, read_json(root / "metadata.json")["provider_status"])

    def test_provider_diagnostic_redacts_credentials(self):
        error = provider_error([json.dumps({"type": "error", "error": {"data": {
            "statusCode": 401, "message": "Rejected Bearer sk-private-value"}}})])
        self.assertNotIn("private-value", str(error))

    def test_pinned_runtime_shares_only_dependencies_and_rejects_version_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            runtime = root / "runtime"
            plugin = runtime / "node_modules/@opencode-ai/plugin"
            plugin.mkdir(parents=True)
            (runtime / "package.json").write_text(json.dumps({"dependencies": {"@opencode-ai/plugin": "1.2.3"}}))
            (runtime / "package-lock.json").write_text('{}')
            (plugin / "package.json").write_text('{"version":"1.2.3"}')
            executable = root / "opencode"
            executable.write_text(f"#!{sys.executable}\nprint('1.2.3')\n")
            executable.chmod(0o755)
            first = prepare_runtime(str(executable), runtime, root / "attempt-a")
            second = prepare_runtime(str(executable), runtime, root / "attempt-b")
            self.assertEqual(first, second)
            self.assertTrue((root / "attempt-a/.opencode/node_modules").is_symlink())
            self.assertFalse((root / "attempt-a/.opencode/package.json").is_symlink())
            (root / 'deep/workspaces').mkdir(parents=True)
            alias = root / 'alias'
            alias.symlink_to(root / 'deep/workspaces', target_is_directory=True)
            prepare_runtime(str(executable), runtime, alias / 'attempt')
            self.assertEqual((runtime / 'node_modules').resolve(), (alias / 'attempt/.opencode/node_modules').resolve())
            executable.write_text(f"#!{sys.executable}\nprint('1.2.4')\n")
            with self.assertRaises(ConflictError):
                prepare_runtime(str(executable), runtime, root / "attempt-c")
