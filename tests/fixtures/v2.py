"""Deterministic public-domain fixtures; never imported by production code."""

from pathlib import Path

from featuretree.core.artifacts import FileArtifactStore
from featuretree.core.contracts import SchemaRegistry
from featuretree.core.versions import VersionStore

PROJECT = Path(__file__).resolve().parents[2]


def stores(root):
    artifacts = FileArtifactStore(root / "data/objects")
    return artifacts, VersionStore(root / "data", artifacts)


def schemas():
    return SchemaRegistry(PROJECT / "config/v2/schemas")
