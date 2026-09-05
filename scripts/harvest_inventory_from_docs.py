#!/usr/bin/env python3
"""FeatureTree command entry point. See README.md for the authoring workflow."""

from _bootstrap import ROOT
from featuretree.harvest import harvest

if __name__ == "__main__":
    print(harvest())
