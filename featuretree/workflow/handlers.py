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
        if response["outcome"] == "needs_sources" and not response["source_requests"]:
            raise ValueError("A source-blocked result requires an actionable source request")
        if response["outcome"] == "revise" and not any(issue["severity"] == "blocking" for issue in response["issues"]):
            raise ValueError("A revision outcome requires a blocking issue and a responsible stage")
        if response["outcome"] == "pass" and any(issue["severity"] == "blocking" for issue in response["issues"]):
            raise ValueError("A passing result cannot conceal blocking issues")
        routes = {"alignment": {"ft-align"}, "structure": {"ft-design"}, "binding": {"ft-bind"},
                  "granularity": {"ft-design"}, "specification": {"fk-scope"},
                  "comparison": {"fk-compare"}, "confidence": {"fk-confidence"},
                  "fact": {prefix + platform for prefix in ("ft-", "fk-") for platform in ("android", "ios", "harmonyos")}}
        for issue in response["issues"]:
            if issue["kind"] in routes and issue["target_stage"] not in routes[issue["kind"]]:
                raise ValueError("Issue was routed to an agent outside its responsibility")
        return self.validators[stage](stage, response, packet)
