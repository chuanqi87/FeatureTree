"""Guard dependency direction so business modules cannot drift back into entrypoints."""

import ast
from pathlib import Path
import unittest

from featuretree.core.storage import ROOT


ALLOWED = {
    "core": set(),
    "taxonomy": {"core"},
    "knowledge": {"core", "taxonomy"},
    "corpus": {"core", "knowledge"},
    "reporting": {"core", "taxonomy", "knowledge"},
    "workflow": {"core", "taxonomy", "knowledge", "corpus"},
    "console": {"core", "taxonomy", "knowledge", "reporting", "workflow"},
    "cli": {"core", "taxonomy", "knowledge", "corpus", "reporting", "workflow", "console"},
}


def imports(path):
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.ImportFrom):
            yield node.module or ""
        elif isinstance(node, ast.Import):
            yield from (alias.name for alias in node.names)


class ArchitectureTests(unittest.TestCase):
    def test_backend_dependencies_point_toward_domain_and_core(self):
        for path in (ROOT / "featuretree").rglob("*.py"):
            relative = path.relative_to(ROOT / "featuretree")
            if len(relative.parts) < 2:
                continue
            owner = relative.parts[0]
            self.assertIn(owner, ALLOWED, str(relative))
            self.assertTrue(all(node.level == 0 for node in ast.walk(ast.parse(path.read_text()))
                                if isinstance(node, ast.ImportFrom)), str(relative))
            for dependency in imports(path):
                self.assertFalse(dependency.startswith(("scripts", "tests")), (relative, dependency))
                if dependency.startswith("featuretree."):
                    target = dependency.split(".")[1]
                    self.assertIn(target, ALLOWED[owner] | {owner}, (relative, dependency))

    def test_backend_has_no_module_import_cycles(self):
        graph = {".".join(p.relative_to(ROOT).with_suffix("").parts):
                 {name for name in imports(p) if name.startswith("featuretree.")}
                 for p in (ROOT / "featuretree").rglob("*.py")}
        visited, active = set(), []

        def visit(name):
            self.assertNotIn(name, active, " -> ".join([*active, name]))
            if name in visited:
                return
            active.append(name)
            for dependency in graph.get(name, set()):
                visit(dependency)
            active.pop()
            visited.add(name)

        for name in graph:
            visit(name)

    def test_scripts_only_bootstrap_and_delegate(self):
        for path in (ROOT / "scripts").glob("*.py"):
            if path.name == "_bootstrap.py":
                continue
            tree = ast.parse(path.read_text())
            self.assertFalse(any(isinstance(n, (ast.FunctionDef, ast.ClassDef)) for n in tree.body), path)
            self.assertTrue(any(name.startswith("featuretree.cli.") for name in imports(path)), path)

    def test_fixtures_do_not_depend_on_test_suites(self):
        for path in (ROOT / "tests").rglob("*.py"):
            for dependency in imports(path):
                self.assertFalse(dependency.startswith("tests.backend"), (path, dependency))

    def test_frontend_shared_code_does_not_import_features_or_app(self):
        import re
        for path in (ROOT / "web/src/shared").rglob("*"):
            if path.suffix not in (".js", ".jsx"):
                continue
            for reference in re.findall(r'(?:from\s*|import\s*)[\'"](\.[^\'"]+)', path.read_text()):
                target = (path.parent / reference).resolve()
                self.assertTrue(target.is_relative_to(ROOT / "web/src/shared"), (path, reference))
