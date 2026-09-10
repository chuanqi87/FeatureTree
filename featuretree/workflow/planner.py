"""Explicit input enumeration and immutable stage configuration snapshots."""

from featuretree.core.content import digest, identifier, timestamp
from featuretree.core.io import read_json, write_json


class Planner:
    def __init__(self, root, registry, schemas, artifacts, catalog, runs):
        self.root, self.registry, self.schemas = root, registry, schemas
        self.artifacts, self.catalog, self.runs = artifacts, catalog, runs

    def create(self, request, key):
        identifier(key)
        run_id = "run_" + digest(key)[:24]
        folder = self.runs.folder(run_id)
        if (folder / "plan.json").exists():
            plan, state = self.runs.load(run_id)
            if plan["request_hash"] != digest(request):
                from featuretree.core.io import ConflictError
                raise ConflictError("Run key was reused with another plan")
            return state
        pipeline = request["pipeline"]
        if pipeline not in self.registry.pipelines:
            raise ValueError("Unknown registered pipeline")
        model = request.get("model")
        if not model or "/" not in model:
            raise ValueError("A resolved provider/model identifier is required for reproducible execution")
        budget = {**self.registry.configuration["defaults"], **request.get("budget", {})}
        if set(budget) != set(self.registry.configuration["defaults"]) or any(
                not isinstance(value, int) or value < 1 for value in budget.values()):
            raise ValueError("Invalid execution budget")
        if budget["workers"] > budget["project_capacity"] or budget["project_capacity"] != 6:
            raise ValueError("Project capacity is fixed at six; workers cannot exceed it")
        works = []
        for index, scope in enumerate(request["scopes"]):
            snapshot_id = scope["snapshot_id"]
            selection = scope["selection"]
            api_ids = self.catalog.enumerate_ids(snapshot_id, selection)
            topics = self.catalog.enumerate_ids(snapshot_id, scope.get("topic_selection", selection), "topics")
            # Keep a complete manifest even if the payload exceeds a single model context.
            inputs = scope.get("inputs", {})
            for reference in inputs.values():
                if reference is not None:
                    self.artifacts.verify(reference)
            works.append({"id": f"w_{index:04d}", "scope": scope["definition"],
                          "snapshot_id": snapshot_id, "selection": selection,
                          "api_ids": api_ids, "topic_ids": topics, "inputs": inputs,
                          "work_type": scope.get("work_type", "refine"),
                          "mode": scope.get("mode", "calibration"),
                          "revision_of": scope.get("revision_of")})
        if not works:
            raise ValueError("A run requires at least one explicitly scoped work unit")
        stage_configs = {}
        for stage_id in self.registry.pipelines[pipeline]:
            stage = self.registry.stages[stage_id]
            agent_text = (self.root / ".opencode/agents" / f"{stage.agent_name}.md").read_text() if stage.agent_name else ""
            rules = {name: read_json(self.root / "config/v2/rules" / f"{name}.json") for name in stage.rules}
            stage_configs[stage_id] = {"definition": stage.__dict__, "agent_text": agent_text,
                                      "rules": rules, "output_schema": self.schemas.expanded(stage.output_schema),
                                      "fingerprint": self.registry.fingerprint(stage_id, agent_text, self.schemas, rules)}
        plan = {"protocol_version": 2, "run_id": run_id, "created_at": timestamp(),
                "request_hash": digest(request), "pipeline": pipeline,
                "pipeline_stages": self.registry.pipelines[pipeline],
                "registry": self.registry.configuration, "stage_configs": stage_configs,
                "model": model, "variant": request.get("variant"), "budget": budget, "works": works}
        return self.runs.create(plan)
