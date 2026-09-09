#!/usr/bin/env python3
"""Stable command entry point; implementation: featuretree.cli.console."""

import _bootstrap  # noqa: F401
from featuretree.cli.console import main

if __name__ == "__main__":
    raise SystemExit(main())
