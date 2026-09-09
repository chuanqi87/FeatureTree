#!/usr/bin/env python3
"""Stable command entry point; implementation: featuretree.cli.tree_lint."""

import _bootstrap  # noqa: F401
from featuretree.cli.tree_lint import main

if __name__ == "__main__":
    raise SystemExit(main())
