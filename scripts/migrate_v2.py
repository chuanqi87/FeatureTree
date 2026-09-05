#!/usr/bin/env python3
"""FeatureTree command entry point. See README.md for the authoring workflow."""

from _bootstrap import ROOT
from featuretree.migration import migrate_inventory, migrate_nodes
from featuretree.storage import Repository

if __name__ == "__main__":
    repo = Repository()
    print(f"Migrated {migrate_nodes(repo)} nodes; historical prose and assessments preserved.")
    print(migrate_inventory(repo))
