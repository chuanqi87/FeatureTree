"""Explicit input enumeration and immutable stage configuration snapshots."""

from featuretree.core.content import digest, identifier, timestamp
from featuretree.core.io import read_json, write_json
from featuretree.workflow.implementation import implementation_files
from featuretree.workflow.planning_gates import validate_scope, validate_work_boundaries
from featuretree.workflow.attempt_tools import configure_agent


class Planner:
    def __init__(self, root, registry, schemas, artifacts, catalog, runs, freeze_validator=None):
        self.root, self.registry, self.schemas = root, registry, schemas
        self.artifacts, self.catalog, self.runs = artifacts, catalog, runs
        self.freeze_validator = freeze_validator

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
            api_records = self.catalog.enumerate_records(snapshot_id, selection)
            topic_records = self.catalog.enumerate_records(snapshot_id, scope.get("topic_selection", selection), "topics")
            api_ids = sorted(row["id"] for row in api_records)
            topics = sorted(row["id"] for row in topic_records)
            groups = {"declarations": {platform: sorted(row["id"] for row in api_records if row["platform"] == platform)
                                       for platform in ("android", "ios", "harmonyos")},
                      "topics": {platform: sorted(row["id"] for row in topic_records if row["platform"] == platform)
                                 for platform in ("android", "ios", "harmonyos")}}
            # Keep a complete manifest even if the payload exceeds a single model context.
            inputs = scope.get("inputs", {})
            if not inputs.get("baseline_ref"):
                raise ValueError("Every work scope must pin an explicit comparison baseline, including historical calibration")
            for reference in inputs.values():
                if reference is not None:
                    self.artifacts.verify(reference)
            validate_scope(pipeline, scope, self.artifacts, self.schemas, self.freeze_validator)
            roots = scope.get("scope_root_ids", [])
            if pipeline == "taxonomy" and inputs.get("tree_ref"):
                from featuretree.taxonomy.revisions import scope_ids
                scope_ids(self.artifacts.get(inputs["tree_ref"]), roots)
                if not inputs.get("bindings_ref"):
                    raise ValueError("Existing-tree revisions must pin bindings to preserve other domains")
            works.append({"id": f"w_{index:04d}", "scope": scope["definition"],
                          "snapshot_id": snapshot_id, "selection": selection,
                          "api_ids": api_ids, "topic_ids": topics, "inputs": inputs,
                          "source_groups": groups,
                          "research_order": {platform: [row["id"] for row in sorted(
                              (row for row in api_records if row["platform"] == platform),
                              key=lambda row: (row.get("qualified_name", ""), row["id"]))]
                              for platform in ("android", "ios", "harmonyos")},
                          "scope_root_ids": roots,
                          "enumeration_complete": scope.get("enumeration_complete", False),
                          "source_round": scope.get("source_round", 0),
                          "work_type": scope.get("work_type", "refine"),
                          "mode": scope.get("mode", "calibration"),
                          "revision_of": scope.get("revision_of")})
        if not works:
            raise ValueError("A run requires at least one explicitly scoped work unit")
        validate_work_boundaries(pipeline, works, self.artifacts)
        if any(self.registry.stages[key].dependency_scope == "run" for key in self.registry.pipelines[pipeline]):
            if len({work["snapshot_id"] for work in works}) != 1 or len({work["inputs"].get("baseline_ref") for work in works}) != 1:
                raise ValueError("Cross-domain integration requires one shared source snapshot and comparison baseline")
        stage_configs = {}
        for stage_id in self.registry.pipelines[pipeline]:
            stage = self.registry.stages[stage_id]
            agent_text = (self.root / ".opencode/agents" / f"{stage.agent_name}.md").read_text() if stage.agent_name else ""
            if agent_text:
                agent_text = configure_agent(agent_text, budget["max_agent_steps"])
            rules = {name: read_json(self.root / "config/v2/rules" / f"{name}.json") for name in stage.rules}
            stage_configs[stage_id] = {"definition": stage.__dict__, "agent_text": agent_text,
                                      "implementation_files": implementation_files(stage_id),
                                      "rules": rules, "output_schema": self.schemas.expanded(stage.output_schema),
                                      "fingerprint": self.registry.fingerprint(stage_id, agent_text, self.schemas, rules)}
        plan = {"protocol_version": 2, "run_id": run_id, "created_at": timestamp(),
                "request_hash": digest(request), "pipeline": pipeline,
                "pipeline_stages": self.registry.pipelines[pipeline],
                "registry": self.registry.configuration, "stage_configs": stage_configs,
                "model": model, "variant": request.get("variant"), "budget": budget, "works": works}
        return self.runs.create(plan)
