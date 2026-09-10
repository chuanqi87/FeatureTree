"""Human knowledge findings become executable, bounded taxonomy revision orders."""

from featuretree.core.content import digest
from featuretree.core.io import ConflictError


class StructureRevisionService:
    def __init__(self, artifacts, versions, planner, runs):
        self.artifacts, self.versions, self.planner, self.runs = artifacts, versions, planner, runs

    def create(self, article_ref, event_ref, decision):
        article = self.artifacts.get(article_ref)
        origin = self.artifacts.get(article["dependencies"]["fk-scope"])
        plan, _ = self.runs.load(origin["run_id"])
        current = self.versions.pin()
        if not article["draft"]:
            if current is None or current["knowledge_refs"].get(article["feature_id"]) != article_ref:
                raise ConflictError("Structural finding targets superseded formal knowledge")
            inputs = {name: current[name] for name in ("tree_ref", "bindings_ref", "baseline_ref")}
        else:
            inputs = {name: article["rating_context"]["inputs"][name] for name in ("tree_ref", "bindings_ref", "baseline_ref")}
        tree = self.artifacts.get(inputs["tree_ref"])
        feature = next((row for row in tree["features"] if row["id"] == article["feature_id"]), None)
        if feature is None:
            raise ConflictError("Feature no longer exists in the selected tree")
        bindings = self.artifacts.get(inputs["bindings_ref"])
        apis = sorted({row["declaration_id"] for row in bindings["bindings"] if row["feature_id"] == feature["id"]})
        inputs["human_revision_ref"] = self.artifacts.put({"article_ref": article_ref, "event_ref": event_ref, "decision": decision})
        scope = {"definition": f"修订能力边界：{feature['definition']}。人工问题：{decision['reason']}。保留范围外节点与 API 用途。",
            "snapshot_id": bindings["snapshot_id"], "scope_root_ids": [feature["id"]],
            "selection": {"ids": apis}, "topic_selection": {"ids": []}, "inputs": inputs,
            "work_type": "revise", "mode": "calibration", "enumeration_complete": False,
            "revision_of": {"run_id": origin["run_id"], "work_id": origin["work_id"], "event_ref": event_ref}}
        state = self.planner.create({"pipeline": "taxonomy", "model": plan["model"], "variant": plan["variant"],
                                    "budget": plan["budget"], "scopes": [scope]}, "structure_" + digest(event_ref))
        return {"run_id": state["run_id"], "task_id": "w_0000--ft-design", "status": state["status"],
                "source_article_ref": article_ref, "event_ref": event_ref, "requires_new_freeze": True}
