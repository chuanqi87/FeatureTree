"""Application assembly for stage checks, separate from the scheduling loop."""

from featuretree.workflow.knowledge_handlers import KnowledgeHandlers
from featuretree.workflow.tree_handlers import TreeHandlers


class StageHandlers:
    def __init__(self, artifacts, catalog):
        tree, knowledge = TreeHandlers(artifacts, catalog), KnowledgeHandlers(artifacts, catalog)
        self.executors = {"ft-check": tree.check, "fk-assemble": knowledge.assemble}
        self.validators = {name: tree.validate for name in (
            "ft-android", "ft-ios", "ft-harmonyos", "ft-align", "ft-design", "ft-bind",
            "ft-granularity", "ft-coverage", "ft-review", "ft-integrate", "ft-check")}
        self.validators.update({name: knowledge.validate for name in (
            "fk-scope", "fk-android", "fk-ios", "fk-harmonyos", "fk-compare", "fk-review",
            "fk-confidence", "fk-assemble")})

    def execute(self, executor, packet, folder):
        return self.executors[executor](packet, folder)

    def validate(self, stage, response, packet):
        return self.validators[stage](stage, response, packet)
