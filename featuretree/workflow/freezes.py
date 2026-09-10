"""Domain freeze use case; approval, enumeration and independent reviews are all required."""

from featuretree.core.content import digest, timestamp
from featuretree.core.io import read_json, write_json
from featuretree.taxonomy.model import semantic_hash, subtree_ids, validate_tree
from featuretree.taxonomy.coverage import disposition_report
from featuretree.taxonomy.routes import binding_hash


class FreezeService:
    def __init__(self, artifacts, schemas, snapshots, catalog, provenance, directory):
        self.artifacts, self.schemas, self.snapshots = artifacts, schemas, snapshots
        self.catalog, self.provenance = catalog, provenance
        self.directory = directory

    def validate_inputs(self, request):
        tree = self.artifacts.get(request["tree_ref"])
        bindings = self.artifacts.get(request["bindings_ref"])
        baseline = self.artifacts.get(request["baseline_ref"])
        approval = self.artifacts.get(request["approval_ref"])
        for name, value in (("tree", tree), ("bindings", bindings), ("baseline", baseline), ("calibration-approval", approval)):
            self.schemas.validate(f"https://featuretree.local/schema/business/v3/{name}", value)
        nodes = validate_tree(tree)
        approved_nodes = validate_tree(self.artifacts.get(approval["tree_ref"]))
        if not approval["sample_article_refs"] or any(key not in nodes or semantic_hash(row) != semantic_hash(nodes[key])
                                                        for key, row in approved_nodes.items()):
            raise ValueError("The approved skeleton or representative leaf boundaries changed; calibration needs review")
        if not set(request["root_ids"]) <= set(subtree_ids(nodes, approval["scope_ids"])):
            raise ValueError("Freeze scope exceeds the user's calibration approval")
        for reference in approval["sample_article_refs"]:
            sample = self.artifacts.get(reference)
            if not sample["draft"] or sample["candidate_tree_ref"] != approval["tree_ref"]:
                raise ValueError("Approval sample does not match the fixed calibration tree")
        for name in ("granularity_policy_ref", "confidence_policy_ref"):
            self.artifacts.verify(approval[name])
        if any(row["status"] != "verified_stable" or not row["evidence_refs"] for row in baseline["platforms"].values()):
            raise ValueError("Three officially verified stable release/SDK baselines are required")
        from featuretree.corpus.baselines import validate_baseline
        validate_baseline(baseline, self.artifacts, self.catalog)
        snapshot = self.snapshots.verify(request["snapshot_id"])
        if snapshot["status"] != "verified" or snapshot["baseline_ref"] != request["baseline_ref"]:
            raise ValueError("Historical or incomplete source snapshots cannot freeze a formal domain")
        if any(row["status"] not in ("extracted", "excluded") for row in snapshot["files"]) or snapshot["gaps"]:
            raise ValueError("Source extraction gaps remain unresolved")
        if bindings["tree_ref"] != request["tree_ref"] or bindings["snapshot_id"] != request["snapshot_id"]:
            raise ValueError("Bindings do not belong to this tree/source version")
        scope = subtree_ids(nodes, request["root_ids"])
        leaves = [key for key in scope if nodes[key]["node_type"] == "leaf"]
        from featuretree.corpus.baselines import validate_declaration_baseline
        bound_ids = sorted({row["declaration_id"] for row in bindings["bindings"] if row["feature_id"] in leaves})
        validate_declaration_baseline((self.catalog.get(request["snapshot_id"], "declarations", key) for key in bound_ids), baseline)
        for document_id in sorted({ref for row in bindings["bindings"] if row["feature_id"] in leaves for ref in row["evidence_refs"]}):
            self.catalog.read_body(request["snapshot_id"], document_id, 0, 1)
        if not leaves or any(nodes[key]["node_type"] == "branch" and not any(
                node["parent_id"] == key for node in nodes.values()) for key in scope):
            raise ValueError("An empty branch is still awaiting expansion")
        checked_stages = set()
        for reference in request["review_refs"]:
            response = self.artifacts.get(reference)
            stage = response["stage_id"]
            response, packet = self.provenance.require(reference, stage)
            if not packet.get("implementation_files"):
                raise ValueError("Unpinned development executions cannot certify a formal freeze")
            for upstream_stage, upstream_ref in packet["upstream_refs"].items():
                _, upstream_packet = self.provenance.require(upstream_ref, upstream_stage)
                if not upstream_packet.get("implementation_files"):
                    raise ValueError("Freeze depends on unpinned development deliveries; replan formal research")
            if stage not in ("ft-granularity", "ft-coverage", "ft-review", "ft-integrate"):
                raise ValueError("Unexpected freeze review stage")
            report = packet["upstream"].get("ft-check")
            if not report or report["tree_ref"] != request["tree_ref"] or report["bindings_ref"] != request["bindings_ref"]:
                raise ValueError("Review targets a different candidate tree or binding version")
            reviewed_leaves = {report["identity_mapping"].get(key, key) for key in report["leaf_ids"]}
            if not set(leaves) <= reviewed_leaves:
                raise ValueError("Freeze scope includes leaves outside the independently reviewed work scope")
            if packet["work"]["snapshot_id"] != request["snapshot_id"] or not packet["work"]["enumeration_complete"]:
                raise ValueError("Review lacks a complete enumeration of the fixed source scope")
            if response["outcome"] != "pass" or any(issue["severity"] == "blocking" for issue in response["issues"]):
                raise ValueError("Freeze review has unresolved issues")
            if not report["api_coverage"]["complete"] or not report["topic_coverage"]["complete"]:
                raise ValueError("API or official topic ledger is incomplete")
            if report["missing_public_realization"]:
                raise ValueError("A leaf lacks a verified public implementation")
            if stage == "ft-granularity" and any(row["verdict"] != "appropriate" for row in response["payload"]["decisions"]):
                raise ValueError("Unresolved granularity decisions prevent freezing")
            if stage == "ft-integrate" and response["payload"]["freeze_recommendation"] != "eligible":
                raise ValueError("Cross-domain integration did not recommend freezing")
            checked_stages.add(stage)
        if checked_stages != {"ft-granularity", "ft-coverage", "ft-review", "ft-integrate"}:
            raise ValueError("All four independent review deliveries are required")
        return {"schema_version": 3, "root_ids": request["root_ids"], "leaf_ids": sorted(leaves),
                  "tree_ref": request["tree_ref"], "bindings_ref": request["bindings_ref"],
                  "baseline_ref": request["baseline_ref"], "snapshot_id": request["snapshot_id"],
                  "semantic_hashes": {key: semantic_hash(nodes[key]) for key in leaves},
                  "binding_hashes": {key: binding_hash(bindings, key) for key in leaves},
                  "approval_ref": request["approval_ref"], "review_refs": request["review_refs"]}

    def prepare(self, request):
        frozen = {**self.validate_inputs(request), "created_at": timestamp()}
        frozen["id"] = "freeze_" + digest(frozen)
        self.schemas.validate("https://featuretree.local/schema/business/v3/freeze", frozen)
        reference = self.artifacts.put(frozen)
        write_json(self.directory / f"{reference}.json", {"freeze_ref": reference}, immutable=True)
        return {"freeze_ref": reference, "freeze": frozen}

    def list(self):
        return [{**read_json(path), "freeze": self.artifacts.get(read_json(path)["freeze_ref"])}
                for path in sorted(self.directory.glob("*.json"))]

    def validate(self, frozen):
        self.schemas.validate("https://featuretree.local/schema/business/v3/freeze", frozen)
        verified = self.validate_inputs(frozen)
        if any(frozen[key] != value for key, value in verified.items()):
            raise ValueError("Frozen semantic, binding or scope fingerprint does not match its reviewed inputs")
        if frozen["id"] != "freeze_" + digest({key: value for key, value in frozen.items() if key != "id"}):
            raise ValueError("Freeze identity does not match its content")
        return frozen
