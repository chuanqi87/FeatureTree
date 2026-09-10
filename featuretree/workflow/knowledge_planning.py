"""Create complete leaf research inputs from a pinned freeze or candidate tree."""

from featuretree.taxonomy.model import validate_tree


class KnowledgePlanningService:
    def __init__(self, artifacts, freezes, planner):
        self.artifacts, self.freezes, self.planner = artifacts, freezes, planner

    def create(self, request, key):
        if request.get("freeze_ref"):
            frozen = self.freezes.validate(self.artifacts.get(request["freeze_ref"]))
            inputs = {name: frozen[name] for name in ("tree_ref", "bindings_ref", "baseline_ref")}
            inputs["freeze_ref"] = request["freeze_ref"]
            mode, snapshot_id = "formal", frozen["snapshot_id"]
            allowed = set(frozen["leaf_ids"])
        else:
            inputs = {name: request[name] for name in ("tree_ref", "bindings_ref", "baseline_ref")}
            mode = "calibration"
            snapshot_id = self.artifacts.get(inputs["bindings_ref"])["snapshot_id"]
            allowed = set(validate_tree(self.artifacts.get(inputs["tree_ref"])))
        tree = validate_tree(self.artifacts.get(inputs["tree_ref"]))
        bindings = self.artifacts.get(inputs["bindings_ref"])
        if bindings["tree_ref"] != inputs["tree_ref"]:
            raise ValueError("Knowledge planning tree/binding version mismatch")
        scopes = []
        for feature_id in request["feature_ids"]:
            if feature_id not in allowed or tree[feature_id]["node_type"] != "leaf":
                raise ValueError("Knowledge research requires an in-scope leaf")
            self.planner.schemas.validate("https://featuretree.local/schema/business/v3/feature", tree[feature_id])
            apis = sorted({row["declaration_id"] for row in bindings["bindings"] if row["feature_id"] == feature_id})
            leaf_inputs = {**inputs, "feature_ref": self.artifacts.put(tree[feature_id])}
            if request.get("observations_ref"):
                leaf_inputs["observations_ref"] = request["observations_ref"]
            scopes.append({"definition": tree[feature_id]["definition"], "snapshot_id": snapshot_id,
                           "selection": {"ids": apis}, "topic_selection": {"ids": []},
                           "inputs": leaf_inputs, "mode": mode, "enumeration_complete": True})
        return self.planner.create({"pipeline": "knowledge", "model": request["model"],
                                  "variant": request.get("variant"), "budget": request.get("budget", {}),
                                  "scopes": scopes}, key)
