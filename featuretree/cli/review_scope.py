"""Export an explicit, budgetable claim scope without starting research or tests."""

import argparse
import json
from featuretree.knowledge.confidence import LEVELS
from featuretree.knowledge.validation import require_valid_knowledge
from featuretree.core.paths import EXPORTS_DIR
from featuretree.core.storage import Repository, write_json
from featuretree.reporting.review import DEVICE_FILTERS, build_scope


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain", default="", help="Feature subtree ID, including non-root subtrees")
    parser.add_argument("--role", choices=("leaf", "rollup"), default="")
    parser.add_argument("--confidence", choices=LEVELS, default="")
    parser.add_argument("--device-review", choices=DEVICE_FILTERS, default="")
    parser.add_argument("--limit", type=int, help="Maximum claims after triage sorting; does not silently mark omitted claims complete")
    args = parser.parse_args(argv)
    repo = Repository()
    features, (knowledge, paths), config = repo.features(), repo.knowledge(), repo.config()
    require_valid_knowledge(repo, features, knowledge, paths, config)
    try:
        scope = build_scope(features, knowledge, config["platforms"], **vars(args))
    except ValueError as exc:
        parser.error(str(exc))
    path = repo.root / EXPORTS_DIR / "review-scopes" / (scope["scope_hash"] + ".json")
    write_json(path, scope)
    print(json.dumps({"path": str(path), **{k: scope[k] for k in
                     ("total_matching_claims", "selected_claims", "omitted_claims", "feature_ids")}}, ensure_ascii=False))
    return 0
