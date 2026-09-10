"""Durable v2 plans, attempts, events and scoped revision state."""

from featuretree.core.content import digest, identifier, timestamp
from featuretree.core.io import IntegrityError, read_json, write_json


class RunStore:
    def __init__(self, directory):
        self.directory = directory

    def folder(self, run_id):
        return self.directory / identifier(run_id)

    def load(self, run_id):
        folder = self.folder(run_id)
        plan = read_json(folder / "plan.json")
        state = read_json(folder / "state.json")
        if plan["protocol_version"] != 2 or state["plan_hash"] != digest(plan):
            raise IntegrityError("Run protocol or immutable plan fingerprint mismatch")
        return plan, state

    def create(self, plan):
        folder = self.folder(plan["run_id"])
        write_json(folder / "plan.json", plan, immutable=True)
        state_path = folder / "state.json"
        if state_path.exists():
            return self.load(plan["run_id"])[1]
        tasks = {}
        for work in plan["works"]:
            for stage in plan["pipeline_stages"]:
                task_id = work["id"] + "--" + stage
                tasks[task_id] = {"id": task_id, "work_id": work["id"], "stage_id": stage,
                                  "status": "waiting", "outcome": None, "result_ref": None,
                                  "revision": 0, "attempts": [], "history": [], "feedback": []}
        state = {"protocol_version": 2, "run_id": plan["run_id"], "plan_hash": digest(plan),
                 "status": "planned", "tasks": tasks, "semantic_rounds": {}, "source_rounds": {},
                 "events": 0, "updated_at": timestamp()}
        self.save(state)
        return state

    def save(self, state):
        state["updated_at"] = timestamp()
        write_json(self.folder(state["run_id"]) / "state.json", state)

    def event(self, state, kind, details):
        state["events"] += 1
        record = {"sequence": state["events"], "type": kind, "details": details,
                  "created_at": timestamp()}
        folder = self.folder(state["run_id"]) / "events"
        # State writes may lag after a crash; retain previously appended sequence numbers.
        while (folder / f"{record['sequence']:012d}.json").exists():
            state["events"] += 1
            record["sequence"] = state["events"]
        write_json(folder / f"{record['sequence']:012d}.json", record, immutable=True)
        self.save(state)

    def list(self):
        return [self.load(path.parent.name)[1] for path in sorted(self.directory.glob("*/state.json"))]
