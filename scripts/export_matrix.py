#!/usr/bin/env python3
"""FeatureTree command entry point. See README.md for the authoring workflow."""

from _bootstrap import ROOT
from featuretree.generation import export_views
from featuretree.storage import Repository

if __name__ == "__main__":
    export_views(Repository())
    print("Exported all-node support and dimension/pair comparison matrices.")
