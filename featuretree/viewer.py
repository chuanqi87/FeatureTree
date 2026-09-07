"""Read-only snapshots for the authored taxonomy tree."""

import json
from datetime import date, datetime, timezone

from .generation import tree_view
from .knowledge_validation import require_valid_knowledge
from .storage import read_yaml


def json_default(value):
    """YAML evidence can contain unquoted ISO dates."""
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    raise TypeError(f"Unsupported JSON value: {type(value).__name__}")


def build_snapshot(repo):
    config = repo.config()
    features = repo.features()
    knowledge, paths = repo.knowledge()
    require_valid_knowledge(repo, features, knowledge, paths, config)
    nodes = tree_view(features, knowledge, config["platforms"])
    for node in nodes:
        node["knowledge"] = knowledge[node["id"]]
    registry = repo.root / "taxonomy/_index.yaml"
    order = [domain["id"] for domain in read_yaml(registry)["domains"]] if registry.exists() else []
    roots = [node["id"] for node in nodes if node["parent"] is None]
    roots.sort(key=lambda fid: (order.index(fid) if fid in order else len(order), fid))
    return {
        "snapshot_kind": "production",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "platforms": config["platforms"],
        "dimensions": config["dimensions"],
        "roots": roots,
        "nodes": nodes,
    }


def build_draft_snapshot(repo):
    """Retired: inventory-first draft campaigns are archived.

    Kept as a stub so `/api/draft-tree` returns a clear error instead of 500 from missing modules.
    """
    del repo
    raise FileNotFoundError(
        "Draft tree-expansion campaigns were archived; use /api/tree for authored taxonomy"
    )
