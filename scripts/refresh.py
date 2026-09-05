#!/usr/bin/env python3
"""FeatureTree command entry point. See README.md for the authoring workflow."""

from _bootstrap import ROOT
from featuretree.audit import main as audit_main
from featuretree.generation import create_missing_knowledge, export_views
from featuretree.storage import Repository

if __name__ == "__main__":
    repo = Repository()
    print(f"Created {len(create_missing_knowledge(repo))} missing knowledge files.")
    export_views(repo)
    raise SystemExit(audit_main())
