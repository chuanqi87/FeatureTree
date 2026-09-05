#!/usr/bin/env python3
"""FeatureTree command entry point. See README.md for the authoring workflow."""

from _bootstrap import ROOT
from featuretree.generation import create_missing_knowledge
from featuretree.storage import Repository

if __name__ == "__main__":
    print(f"Created {len(create_missing_knowledge(Repository()))} missing knowledge files; existing files preserved.")
