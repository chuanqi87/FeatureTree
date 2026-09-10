"""Stage-specific executable fingerprints exclude unrelated docs, UI and tests."""

from pathlib import Path
from featuretree.core.content import file_digest
from featuretree.core.io import ConflictError


def implementation_files(stage_id):
    package = Path(__file__).resolve().parents[1]
    names = ["workflow/implementation.py", "workflow/packaging.py", "workflow/execution.py", "workflow/handlers.py",
             "workflow/source_tool.py", "corpus/catalog.py", "corpus/snapshots.py", "corpus/source_policy.py"]
    names += [str(path.relative_to(package)) for path in (package / "core").glob("*.py")]
    names += [str(path.relative_to(package)) for path in (package / "workflow/backends").glob("*.py")]
    names += ["../tools/opencode/package.json", "../tools/opencode/package-lock.json"]
    names += ["workflow/tree_handlers.py"] if stage_id.startswith("ft-") else ["workflow/knowledge_handlers.py"]
    domains = ("taxonomy",) if stage_id.startswith("ft-") else ("taxonomy", "knowledge")
    for domain in domains:
        names += [str(path.relative_to(package)) for path in (package / domain).glob("*.py")]
    return {name: file_digest(package / name) for name in sorted(set(names))}


def verify_implementation(stage_id, expected):
    if expected and implementation_files(stage_id) != expected:
        raise ConflictError("Stage implementation changed after planning; create a versioned replacement run")
