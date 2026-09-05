"""Fingerprint the research rules as well as data; never reuse stale reviews."""

import hashlib

from .research_profile import fingerprint


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def methodology_hash(root):
    paths = [root / "AGENTS.md"]
    for directory, pattern in (("docs", "*.md"), ("config/schema", "*.json"),
                               ("featuretree", "*.py"), ("scripts", "*.py")):
        paths.extend((root / directory).rglob(pattern))
    return fingerprint({p.relative_to(root).as_posix(): file_hash(p) for p in sorted(paths)})
