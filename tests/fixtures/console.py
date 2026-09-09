"""Isolated synthetic workspace and model backend for console browser checks."""

from pathlib import Path
import shutil
import tempfile
import threading

from featuretree.knowledge.initialization import create_missing_knowledge
from featuretree.core.storage import ROOT, Repository, write_yaml
from featuretree.taxonomy.authoring import feature
from featuretree.console.server import create_server
from featuretree.console.service import WorkflowConsole
from featuretree.workflow.engine import execute_run
from tests.fixtures.workflow import FixtureBackend


def workspace(root):
    root = root.resolve()
    shutil.copytree(ROOT / "config", root / "config")
    shutil.copytree(ROOT / ".opencode", root / ".opencode")
    (root / "AGENTS.md").write_text("Synthetic console fixture. No actual platform research.")
    nodes = [feature("sample", parent=None, level="L1", zh="测试领域", en="Fixture domain", definition="Synthetic root", includes=["fixture"]),
             feature("sample.branch", parent="sample", level="L2", zh="测试分支", en="Fixture branch", definition="Synthetic branch", includes=["fixture"], sibling_axis="synthetic task category"),
             feature("sample.branch.item", parent="sample.branch", level="L3", zh="测试能力", en="Fixture capability", definition="Synthetic capability", includes=["fixture"], sibling_axis="synthetic task category", granularity="atomic")]
    other = feature("other", parent=None, level="L1", zh="其他测试域", en="Other fixture", definition="Synthetic root", includes=["other"])
    write_yaml(root / "taxonomy/sample.yaml", {"domain": "sample", "features": nodes})
    write_yaml(root / "taxonomy/other.yaml", {"domain": "other", "features": [other]})
    create_missing_knowledge(Repository(root))
    return root


class BrowserFixtureLauncher:
    def __init__(self):
        self.threads = {}

    def available(self):
        return True

    def active(self, folder):
        thread = self.threads.get(folder.name)
        return bool(thread and thread.is_alive())

    def start(self, root, run_id):
        thread = threading.Thread(target=execute_run, args=(root, run_id, FixtureBackend(), lambda _: None), daemon=True)
        self.threads[run_id] = thread
        thread.start()


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as directory:
        root = workspace(Path(directory))
        console = WorkflowConsole(root, launcher=BrowserFixtureLauncher())
        server = create_server(Repository(root), ROOT / "web/dist", port=0, workflow=console)
        print(f"Synthetic console: http://127.0.0.1:{server.server_port}", flush=True)
        try:
            server.serve_forever()
        finally:
            server.server_close()
