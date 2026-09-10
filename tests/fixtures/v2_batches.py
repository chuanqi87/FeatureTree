"""Synthetic multi-batch source inventory and controllable model failures."""

from copy import deepcopy

from featuretree.core.io import write_json
from featuretree.workflow.packaging import envelope
from tests.fixtures.v2_application import application


def batched_application(root, backend):
    app, snapshot, baseline = application(root)
    records = {kind: app.catalog.enumerate_records(snapshot["id"], {}, kind)
               for kind in snapshot["records"]}
    original = next(row for row in records["declarations"] if row["platform"] == "android")
    for index in range(4):
        row = deepcopy(original)
        row.update(id=f"api_extra_{index}_android", qualified_name=f"Example.member{index}")
        records["declarations"].append(row)
    snapshot = app.snapshots.seal(records, files=[], status="verified", baseline_ref=baseline)
    app.runner.executor.backend = backend
    request = {"pipeline": "taxonomy", "model": "test/batches",
               "budget": {"source_batch_size": 2, "workers": 1},
               "scopes": [{"definition": "Synthetic batch test", "snapshot_id": snapshot["id"],
                           "selection": {}, "topic_selection": {}, "inputs": {"baseline_ref": baseline},
                           "mode": "calibration", "enumeration_complete": False}]}
    state = app.planner.create(request, "batch-test")
    return app, state


class BatchModel:
    def __init__(self, fail_index=None, cancel=False):
        self.fail_index, self.cancel = fail_index, cancel
        self.failed = False
        self.calls = []

    def execute(self, root, agent, packet, folder, timeout, model, variant):
        if agent not in ("ft-android", "ft-ios", "ft-harmonyos"):
            raise RuntimeError("Synthetic test intentionally ends after platform research")
        self.calls.append(packet)
        if agent == "ft-android" and packet.get("batch", {}).get("index") == self.fail_index and not self.failed:
            self.failed = True
            raise TimeoutError("Synthetic interrupted batch")
        if self.cancel and agent == "ft-android":
            run = next(parent for parent in folder.parents if (parent / "plan.json").exists())
            write_json(run / "CANCEL.json", {"test": True})
        platform = packet["source_access"]["platform"]
        apis, topics = packet["work"]["api_ids"], packet["work"]["topic_ids"]
        disposition = lambda key: {"id": key, "status": "assigned", "reason": "Fixture only",
                                   "rule": "test", "evidence_refs": ["doc_" + platform]}
        facts = [{"id": "fact_" + platform, "api_ids": apis, "goal": "Synthetic goal", "statement": "Synthetic fact",
                  "conditions": [], "implementation_steps": [], "evidence_refs": ["doc_" + platform], "gaps": []}] if apis else []
        return envelope(packet, {"platform": platform, "facts": facts,
            "api_dispositions": [disposition(key) for key in apis],
            "topic_dispositions": [disposition(key) for key in topics]}), {"model": model,
                "usage": [{"tokens": {"output": 1}, "reason": "stop"}]}
