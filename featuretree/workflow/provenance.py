"""Verify that an artifact was accepted by a recorded independent stage invocation."""

from featuretree.core.content import digest
from featuretree.core.io import IntegrityError, read_json


class ExecutionProvenance:
    def __init__(self, artifacts, runs):
        self.artifacts, self.runs = artifacts, runs

    def require(self, reference, expected_stage):
        response = self.artifacts.get(reference)
        if response["stage_id"] != expected_stage:
            raise ValueError("Wrong authoring/review stage")
        _, state = self.runs.load(response["run_id"])
        task = state["tasks"][response["task_id"]]
        attempt = next((row for row in task["attempts"] if row.get("result_ref") == reference
                        and row["status"] == "success"), None)
        if attempt is None:
            raise IntegrityError("Artifact is not backed by an accepted stage attempt")
        packet = read_json(self.runs.folder(response["run_id"]) / attempt["folder"] / "input.json")
        if digest({key: value for key, value in packet.items() if key != "input_hash"}) != response["input_hash"]:
            raise IntegrityError("Stage input fingerprint does not match recorded response")
        return response, packet
