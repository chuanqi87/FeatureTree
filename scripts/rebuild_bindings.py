#!/usr/bin/env python3
"""FeatureTree command entry point. See README.md for the authoring workflow."""

from _bootstrap import ROOT
from featuretree.bindings import build_index
from featuretree.paths import EXPORTS_DIR
from featuretree.storage import Repository, write_json

if __name__ == "__main__":
    repo = Repository()
    index = build_index(repo.features(), repo.inventory())
    write_json(repo.root / EXPORTS_DIR / "index.json", index)
    print(f"Rebuilt {len(index)} complete binding associations.")
