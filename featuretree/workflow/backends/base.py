"""Execution port implemented by model transports and deterministic test backends."""

from pathlib import Path
from typing import Protocol


class Backend(Protocol):
    def execute(self, root: Path, agent: str, packet: dict, folder: Path,
                timeout: int, model: str | None, variant: str | None) -> tuple[dict, dict]: ...
