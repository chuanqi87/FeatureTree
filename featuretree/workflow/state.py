"""Artifact identities and process-local coordination, without model logic."""

from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
from pathlib import Path
from featuretree.core.storage import write_json


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique)


@contextmanager
def lock(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise ValueError(f"Another coordinator holds {path}") from exc
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def rule_hash(root):
    """Fingerprint nested rules and the implementation actually executing this run."""
    paths = [root / "AGENTS.md", *sorted((root / ".opencode/agents").glob("ft-*.md")),
             *sorted((root / "config").rglob("*.json")),
             *sorted((root / "config").rglob("*.yaml")),
             *sorted((root / "docs").rglob("*.md"))]
    rules = {str(p.relative_to(root)): p.read_text() for p in paths if p.is_file()}
    package = Path(__file__).resolve().parents[1]
    implementation = {str(p.relative_to(package)): p.read_text()
                      for name in ("core", "taxonomy", "knowledge", "corpus", "workflow")
                      for p in sorted((package / name).rglob("*.py"))}
    implementation["cli/workflow.py"] = (package / "cli/workflow.py").read_text()
    return digest({"rules": rules, "implementation": implementation})


def run_path(root, run_id):
    if not run_id or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-_" for c in run_id):
        raise ValueError("Invalid run ID")
    return root / ".workflow/runs" / run_id


def load_run(root, run_id):
    folder = run_path(root, run_id)
    state = read_json(folder / "state.json")
    if state["root"] != str(root.resolve()):
        raise ValueError("Run belongs to a different repository root")
    if state["rule_hash"] != rule_hash(root):
        raise ValueError("Workflow rules or agents changed; create a new plan")
    return folder, state


def artifact(folder, task):
    value = read_json(folder / task["result_path"])
    if digest(value) != task["result_hash"]:
        raise ValueError(f"Artifact changed: {task['id']}")
    return value


def save_state(folder, state):
    write_json(folder / "state.json", state)
