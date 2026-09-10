"""Transport port. Model execution is injectable and isolated from business decisions."""

from pathlib import Path
from typing import Protocol


class AgentBackend(Protocol):
    def execute(self, root: Path, agent: str, packet: dict, folder: Path,
                timeout: int, model: str, variant: str | None) -> tuple[dict, dict]: ...
