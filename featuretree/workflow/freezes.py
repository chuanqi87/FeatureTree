"""Domain freeze use case; approval, enumeration and independent reviews are all required."""

from featuretree.core.content import digest, timestamp
from featuretree.taxonomy.model import semantic_hash, subtree_ids, validate_tree
from featuretree.taxonomy.coverage import disposition_report


class FreezeService:
    def __init__(self, artifacts, schemas, snapshots, catalog, provenance):
        self.artifacts, self.schemas, self.snapshots = artifacts, schemas, snapshots
        self.catalog, self.provenance = catalog, provenance

    def prepare(self, request):
        tree = self.artifacts.get(request["tree_ref"])
        bindings = self.artifacts.get(request["bindings_ref"])
        baseline = self.artifacts.get(request["baseline_ref"])
        approval = self.artifacts.get(request["approval_ref"])
        for name, value in (("tree", tree), ("bindings", bindings), ("baseline", baseline), ("calibration-approval", approval)):
            self.schemas.validate(f"https://featuretree.local/schema/business/v3/{name}", value)
        if approval["tree_ref"] != request["tree_ref"] or not approval["sample_article_refs"]:
            raise ValueError("User must approve this skeleton and concrete sample articles")
        if not set(request["root_ids"]) <= set(approval["scope_ids"]):
            raise ValueError("Freeze scope exceeds the user's calibration approval")
        for reference in approval["sample_article_refs"]:
            sample = self.artifacts.get(reference)
            if not sample["draft"] or sample["candidate_tree_ref"] != request["tree_ref"]:
                raise ValueError("Approval sample does not match the fixed calibration tree")
        for name in ("granularity_policy_ref", "confidence_policy_ref"):
            self.artifacts.verify(approval[name])
        if any(row["status"] != "verified_stable" or not row["evidence_refs"] for row in baseline["platforms"].values()):
            raise ValueError("Three officially verified stable release/SDK baselines are required")
        snapshot = self.snapshots.verify(request["snapshot_id"])
        if snapshot["status"] != "verified" or snapshot["baseline_ref"] != request["baseline_ref"]:
            raise ValueError("Historical or incomplete source snapshots cannot freeze a formal domain")
        if any(row["status"] not in ("extracted", "excluded") for row in snapshot["files"]) or snapshot["gaps"]:
            raise ValueError("Source extraction gaps remain unresolved")
        if bindings["tree_ref"] != request["tree_ref"] or bindings["snapshot_id"] != request["snapshot_id"]:
            raise ValueError("Bindings do not belong to this tree/source version")
        nodes = validate_tree(tree)
        scope = subtree_ids(nodes, request["root_ids"])
        leaves = [key for key in scope if nodes[key]["node_type"] == "leaf"]
        if not leaves or any(nodes[key]["node_type"] == "branch" and not any(
                node["parent_id"] == key for node in nodes.values()) for key in scope):
            raise ValueError("An empty branch is still awaiting expansion")
        checked_stages = set()
        for reference in request["review_refs"]:
            response = self.artifacts.get(reference)
            stage = response["stage_id"]
            response, packet = self.provenance.require(reference, stage)
            if stage not in ("ft-granularity", "ft-coverage", "ft-review", "ft-integrate"):
                raise ValueError("Unexpected freeze review stage")
            report = packet["upstream"].get("ft-check")
            if not report or report["tree_ref"] != request["tree_ref"] or report["bindings_ref"] != request["bindings_ref"]:
                raise ValueError("Review targets a different candidate tree or binding version")
            if response["outcome"] != "pass" or any(issue["severity"] == "blocking" for issue in response["issues"]):
                raise ValueError("Freeze review has unresolved issues")
            if not report["api_coverage"]["complete"] or not report["topic_coverage"]["complete"]:
                raise ValueError("API or official topic ledger is incomplete")
            if report["missing_public_realization"]:
                raise ValueError("A leaf lacks a verified public implementation")
            if stage == "ft-integrate" and response["payload"]["freeze_recommendation"] != "eligible":
                raise ValueError("Cross-domain integration did not recommend freezing")
            checked_stages.add(stage)
        if checked_stages != {"ft-granularity", "ft-coverage", "ft-review", "ft-integrate"}:
            raise ValueError("All four independent review deliveries are required")
        frozen = {"schema_version": 3, "root_ids": request["root_ids"], "leaf_ids": leaves,
                  "tree_ref": request["tree_ref"], "bindings_ref": request["bindings_ref"],
                  "baseline_ref": request["baseline_ref"], "snapshot_id": request["snapshot_id"],
                  "semantic_hashes": {key: semantic_hash(nodes[key]) for key in leaves},
                  "binding_hashes": {key: digest([row for row in bindings["bindings"] if row["feature_id"] == key]) for key in leaves},
                  "approval_ref": request["approval_ref"], "review_refs": request["review_refs"], "created_at": timestamp()}
        frozen["id"] = "freeze_" + digest(frozen)
        self.schemas.validate("https://featuretree.local/schema/business/v3/freeze", frozen)
        return {"freeze_ref": self.artifacts.put(frozen), "freeze": frozen}
