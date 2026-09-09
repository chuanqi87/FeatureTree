"""Repository IO; authored files and generated artifacts use separate paths."""

from __future__ import annotations

import json
from pathlib import Path
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[2]


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently losing an author's data."""


def _mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def read_yaml(path: Path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)


def write_yaml(path: Path, value):
    write_text(path, yaml.safe_dump(value, allow_unicode=True, sort_keys=False, width=100))


def write_json(path: Path, value):
    write_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def write_text(path: Path, content: str):
    """Avoid changing timestamps when a deterministic rebuild has no changes."""
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     prefix=path.name + ".", suffix=".tmp", delete=False) as stream:
        temporary = Path(stream.name)
        stream.write(content)
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def contained_path(root: Path, relative: str, directory: str) -> Path:
    path = (root / relative).resolve()
    if not path.is_relative_to((root / directory).resolve()):
        raise ValueError(f"Path must stay under {directory}/: {relative}")
    return path


class Repository:
    def __init__(self, root: Path = ROOT):
        self.root = root.resolve()

    def config(self):
        return read_yaml(self.root / "config/comparison.yaml")

    def features(self):
        features = {}
        for path in sorted((self.root / "taxonomy").glob("*.yaml")):
            if path.name.startswith("_"):
                continue
            for feature in read_yaml(path)["features"]:
                fid = feature["id"]
                if fid in features:
                    raise ValueError(f"Duplicate feature id: {fid} ({path})")
                if fid.split(".")[0] != path.stem:
                    raise ValueError(f"Feature in wrong domain file: {fid} ({path})")
                features[fid] = feature
        return features

    def knowledge(self):
        records = {}
        paths = {}
        for path in sorted((self.root / "knowledge").rglob("*.yaml")):
            doc = read_yaml(path)
            fid = doc["feature_id"]
            if fid in records:
                raise ValueError(f"Duplicate knowledge feature_id: {fid} ({path})")
            records[fid] = doc
            paths[fid] = path.relative_to(self.root).as_posix()
        return records, paths
