"""Verify that an artifact was accepted by a recorded independent stage invocation."""

from featuretree.core.content import digest
from featuretree.core.io import IntegrityError, read_json
from featuretree.workflow.batch_packets import research_batches, merge_research
from featuretree.workflow.batch_execution import verify_receipt


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
        batches = research_batches(packet)
        if batches:
            receipts = attempt.get("metadata", {}).get("batch_receipts", [])
            if len(receipts) != len(batches):
                raise IntegrityError("Merged stage lacks its complete batch execution receipts")
            deliveries = [verify_receipt(receipt, batch, self.artifacts)
                          for receipt, batch in zip(receipts, batches)]
            if digest(merge_research(packet, deliveries)) != reference:
                raise IntegrityError("Merged stage differs from its accepted batch deliveries")
        return response, packet
