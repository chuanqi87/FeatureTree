"""Validated pipeline descriptions; execution behavior is provided by typed handlers."""

from dataclasses import dataclass

from featuretree.core.content import digest
from featuretree.core.io import read_json


@dataclass(frozen=True)
class Stage:
    id: str
    agent_name: str | None
    executor: str
    dependencies: tuple[str, ...]
    output_schema: str
    accepts_gaps: bool
    rules: tuple[str, ...]
    platform: str | None
    dependency_scope: str = "work"
    validation_failure_target: str | None = None


class PipelineRegistry:
    def __init__(self, configuration):
        if configuration["protocol_version"] != 2:
            raise ValueError("Only workflow protocol v2 is supported")
        self.configuration = configuration
        self.stages = {}
        for row in configuration["stages"]:
            stage = Stage(row["stage_id"], row["agent_name"], row["executor"],
                          tuple(row["dependencies"]), row["output_schema"], row["accepts_gaps"],
                          tuple(row["rules"]), row["platform"], row.get("dependency_scope", "work"), row.get("validation_failure_target"))
            if stage.dependency_scope not in ("work", "run"):
                raise ValueError("Unknown stage dependency scope")
            if stage.id in self.stages:
                raise ValueError("Duplicate pipeline stage")
            self.stages[stage.id] = stage
        self.pipelines = configuration["pipelines"]
        for name, stages in self.pipelines.items():
            seen = set()
            for key in stages:
                if key in seen or key not in self.stages:
                    raise ValueError(f"Invalid stage in pipeline {name}: {key}")
                if not set(self.stages[key].dependencies) <= seen:
                    raise ValueError(f"Pipeline order has missing dependency or cycle: {key}")
                seen.add(key)
        self.routing = configuration["issue_routes"]
        if not set(self.routing.values()) <= set(self.stages):
            raise ValueError("Invalid rework routing target")

    @classmethod
    def load(cls, path):
        return cls(read_json(path))

    def ancestors(self, stage_id):
        result = set()
        for dependency in self.stages[stage_id].dependencies:
            result.add(dependency)
            result.update(self.ancestors(dependency))
        return result

    def descendants(self, stage_id, pipeline):
        return [key for key in self.pipelines[pipeline] if stage_id in self.ancestors(key)]

    def fingerprint(self, stage_id, agent_text, schemas, rules):
        stage = self.stages[stage_id]
        return digest({"stage": stage.__dict__, "agent": agent_text,
                       "schema": schemas.expanded(stage.output_schema), "rules": rules,
                       "executor_version": self.configuration["executor_version"]})
