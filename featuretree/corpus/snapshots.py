"""Sealed, streaming source snapshots. Query databases are disposable projections."""

import json
import os
from pathlib import Path
import shutil
import tempfile

from featuretree.core.content import canonical_bytes, digest, file_digest, identifier, timestamp
from featuretree.core.io import IntegrityError, file_lock, read_json, sync_directory, write_json

KINDS = ("declarations", "families", "topics", "documents")


class SnapshotStore:
    def __init__(self, directory, schemas):
        self.directory = Path(directory)
        self.schemas = schemas

    def get(self, snapshot_id):
        identifier(snapshot_id)
        manifest = read_json(self.directory / snapshot_id / "manifest.json")
        expected = "s_" + digest({key: value for key, value in manifest.items() if key != "id"})
        if expected != snapshot_id:
            raise IntegrityError("Source manifest identity mismatch")
        self.schemas.validate("https://featuretree.local/schema/source/v1/snapshot", manifest)
        return manifest

    def path(self, snapshot_id, kind):
        identifier(snapshot_id)
        if kind not in KINDS:
            raise ValueError("Unknown source record kind")
        return self.directory / snapshot_id / f"{kind}.jsonl"

    def verify(self, snapshot_id):
        manifest = self.get(snapshot_id)
        for kind, expected in manifest["records"].items():
            if file_digest(self.path(snapshot_id, kind)) != expected:
                raise IntegrityError(f"Corrupt source collection: {kind}")
        return manifest

    def seal(self, collections, *, files, status="candidate", baseline_ref=None,
             extractor_versions=None, gaps=(), provenance=None):
        self.directory.mkdir(parents=True, exist_ok=True)
        staging = Path(tempfile.mkdtemp(prefix=".sealing-", dir=self.directory))
        try:
            hashes, counts = {}, {}
            for kind in KINDS:
                path = staging / f"{kind}.jsonl"
                seen = set()
                with path.open("wb") as stream:
                    for row in collections.get(kind, ()):
                        if row["id"] in seen:
                            raise ValueError(f"Duplicate {kind} identity: {row['id']}")
                        seen.add(row["id"])
                        if kind != "documents":
                            schema = {"declarations": "declaration", "families": "family", "topics": "topic"}[kind]
                            self.schemas.validate(f"https://featuretree.local/schema/source/v1/{schema}", row)
                        stream.write(canonical_bytes(row) + b"\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                hashes[kind], counts[kind] = file_digest(path), len(seen)
            manifest = {"schema_version": 1, "created_at": timestamp(), "status": status,
                        "baseline_ref": baseline_ref, "extractor_versions": extractor_versions or {},
                        "files": files, "records": hashes, "counts": counts,
                        "gaps": list(gaps), "provenance": provenance or {}}
            manifest["id"] = "s_" + digest(manifest)
            self.schemas.validate("https://featuretree.local/schema/source/v1/snapshot", manifest)
            write_json(staging / "manifest.json", manifest, immutable=True)
            with file_lock(self.directory / "seal.lock"):
                staging.rename(self.directory / manifest["id"])
                sync_directory(self.directory)
            return manifest
        finally:
            if staging.exists():
                shutil.rmtree(staging)

    def list(self):
        return [self.get(path.parent.name) for path in sorted(self.directory.glob("s_*/manifest.json"))]
