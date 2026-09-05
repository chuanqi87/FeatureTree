#!/usr/bin/env python3
"""Export a filtered claim-level review scope, without running research."""

from _bootstrap import ROOT
from featuretree.review_scope import main

if __name__ == "__main__":
    raise SystemExit(main())
