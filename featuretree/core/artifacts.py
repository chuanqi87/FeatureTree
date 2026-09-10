"""Content-addressed business objects; callers own all domain validation."""

from pathlib import Path
from typing import Protocol

from featuretree.core.content import content_hash, digest
from featuretree.core.io import IntegrityError, read_json, write_json


class ArtifactStore(Protocol):
    def put(self, value: dict) -> str: ...
    def get(self, reference: str) -> dict: ...
    def verify(self, reference: str) -> None: ...


class FileArtifactStore:
    def __init__(self, directory: Path):
        self.directory = Path(directory)

    def path(self, reference):
        content_hash(reference)
        return self.directory / reference[:2] / f"{reference}.json"

    def put(self, value):
        reference = digest(value)
        write_json(self.path(reference), value, immutable=True)
        return reference

    def get(self, reference):
        value = read_json(self.path(reference))
        if digest(value) != reference:
            raise IntegrityError(f"Object hash mismatch: {reference}")
        return value

    def verify(self, reference):
        self.get(reference)
