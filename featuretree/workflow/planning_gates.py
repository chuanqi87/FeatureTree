"""Reject unapproved formal work before consuming any model budget."""

from featuretree.taxonomy.model import semantic_hash, subtree_ids, validate_tree


def validate_scope(pipeline, scope, artifacts, schemas, freeze_validator):
    inputs, mode = scope.get("inputs", {}), scope.get("mode", "calibration")
    if mode not in ("calibration", "formal"):
        raise ValueError("Work mode must be calibration or formal")
    baseline = artifacts.get(inputs["baseline_ref"])
    schemas.validate("https://featuretree.local/schema/business/v3/baseline", baseline)
    if mode != "formal":
        return
    if pipeline == "knowledge":
        if not freeze_validator or not inputs.get("freeze_ref"):
            raise ValueError("Formal knowledge requires a validated domain freeze")
        frozen = freeze_validator(artifacts.get(inputs["freeze_ref"]))
        if any(inputs.get(key) != frozen[key] for key in ("tree_ref", "bindings_ref", "baseline_ref")) or scope["snapshot_id"] != frozen["snapshot_id"]:
            raise ValueError("Formal knowledge inputs differ from its frozen domain")
        feature = artifacts.get(inputs["feature_ref"])
        if feature["id"] not in frozen["leaf_ids"] or semantic_hash(feature) != frozen["semantic_hashes"][feature["id"]]:
            raise ValueError("Knowledge leaf is outside the frozen semantic scope")
    elif pipeline == "taxonomy":
        if not inputs.get("approval_ref") or not inputs.get("tree_ref"):
            raise ValueError("Automatic expansion requires the user's concrete calibration approval and tree")
        approval = artifacts.get(inputs["approval_ref"])
        schemas.validate("https://featuretree.local/schema/business/v3/calibration-approval", approval)
        approved = validate_tree(artifacts.get(approval["tree_ref"]))
        current = validate_tree(artifacts.get(inputs["tree_ref"]))
        if any(key not in current or semantic_hash(row) != semantic_hash(current[key]) for key, row in approved.items()):
            raise ValueError("Approved skeleton or representative leaves changed")
        if not set(scope.get("scope_root_ids", [])) <= set(subtree_ids(current, approval["scope_ids"])):
            raise ValueError("Expansion scope exceeds the user's calibration approval")


def validate_work_boundaries(pipeline, works, artifacts):
    if pipeline != "taxonomy":
        return
    base_refs = {work["inputs"].get("tree_ref") for work in works}
    if len(base_refs) > 1:
        raise ValueError("A taxonomy run must share one base tree for global integration")
    if not next(iter(base_refs)):
        return
    tree = validate_tree(artifacts.get(next(iter(base_refs))))
    assigned = set()
    for work in works:
        selected = set(subtree_ids(tree, work["scope_root_ids"]))
        if assigned & selected:
            raise ValueError("Concurrent structural scopes overlap, including ancestor/descendant work")
        assigned.update(selected)
