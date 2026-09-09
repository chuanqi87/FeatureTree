#!/usr/bin/env python3
"""Stable command entry point; implementation: featuretree.cli.evidence."""

import _bootstrap  # noqa: F401
from featuretree.cli.evidence import main

if __name__ == "__main__":
    raise SystemExit(main())
