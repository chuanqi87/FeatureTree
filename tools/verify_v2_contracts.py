"""Rebuild synthetic agent examples through the real runner in a disposable repository."""

import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from featuretree.core.io import read_json
from tests.fixtures.v2_application import application, publishable


def main():
    destination = ROOT / "docs/examples/v2-agents"
    destination.mkdir(parents=True, exist_ok=True)
    examples = {}
    with tempfile.TemporaryDirectory() as directory:
        app, snapshot, baseline = application(Path(directory))
        publishable(app, snapshot, baseline)
        for state in app.runs.list():
            for task in state["tasks"].values():
                if task["stage_id"] in ("ft-check", "fk-assemble"):
                    continue
                attempt = task["attempts"][-1]
                folder = app.runs.folder(state["run_id"]) / attempt["folder"]
                examples[task["stage_id"]] = {
                    "notice": "Synthetic fixture, NOT platform evidence, actual model execution, human approval or production knowledge. References exist only in this disposable test repository.",
                    "agent": task["stage_id"], "input": read_json(folder / "input.json"),
                    "output": app.artifacts.get(task["result_ref"])}
    if len(examples) != 17:
        raise ValueError("Expected all seventeen named deliveries")
    for name, example in examples.items():
        (destination / f"{name}.json").write_text(json.dumps(example, ensure_ascii=False, indent=2) + "\n")
    print("Validated and generated seventeen synthetic agent contracts; production data untouched.")


if __name__ == "__main__":
    main()
