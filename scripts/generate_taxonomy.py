#!/usr/bin/env python3
"""FeatureTree command entry point. See README.md for the authoring workflow."""

from _bootstrap import ROOT
from featuretree.generation import tree_view
from featuretree.knowledge_validation import require_valid_knowledge
from featuretree.paths import EXPORTS_DIR
from featuretree.storage import Repository, write_json

if __name__ == "__main__":
    repo = Repository()
    knowledge, paths = repo.knowledge()
    features, config = repo.features(), repo.config()
    require_valid_knowledge(repo, features, knowledge, paths, config)
    write_json(repo.root / EXPORTS_DIR / "tree.json", tree_view(features, knowledge, config["platforms"]))
    print(f"Rebuilt {EXPORTS_DIR}/tree.json from authored YAML; taxonomy files preserved.")
