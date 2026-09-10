"""Scope-bounded structural edits preserve unrelated identities and API uses."""

from featuretree.taxonomy.model import subtree_ids, validate_tree


def scope_ids(tree, roots):
    nodes = validate_tree(tree)
    if nodes and not roots:
        raise ValueError("Existing trees require explicit scope_root_ids for structural work")
    return set(subtree_ids(nodes, roots)) if nodes else set()


def apply_proposal(base, proposal, roots):
    existing = validate_tree(base)
    allowed = scope_ids(base, roots)
    features = {row["id"]: row for row in proposal["features"]}
    removed, lineage, replacement_roots = set(), list(base["lineage"]), set()
    if len(features) != len(proposal["features"]):
        raise ValueError("Duplicate proposed feature identity")
    for key, feature in features.items():
        if key in existing and key not in allowed and feature != existing[key]:
            raise ValueError("Structural proposal changes a node outside its scope")
    for change in proposal["changes"]:
        if not set(change["subject_ids"]) <= allowed:
            raise ValueError("Structural change targets an identity outside its scope")
        if change["operation"] in ("split", "merge"):
            removed.update(change["subject_ids"])
            if set(change["subject_ids"]) & set(roots):
                replacement_roots.update(change["candidate_ids"])
            lineage.append({"operation": change["operation"], "old_ids": change["subject_ids"],
                            "new_ids": change["candidate_ids"], "reason": change["reason"]})
    if removed & set(features):
        raise ValueError("Split/merge cannot retain the replaced identity")
    merged = {key: row for key, row in existing.items() if key not in removed}
    merged.update(features)
    result = {"schema_version": 3, "features": list(merged.values()), "lineage": lineage}
    validate_tree(result)
    # New nodes must attach inside the selected domain, unless constructing a new skeleton.
    for key in set(merged) - set(existing):
        current = key
        while current is not None and current not in existing:
            if current in replacement_roots:
                break
            current = merged[current]["parent_id"]
        if existing and current not in allowed and current not in replacement_roots:
            raise ValueError("New feature must descend from the assigned domain")
    touched = allowed | (set(merged) - set(existing))
    return result, touched


def merge_binding_scope(previous, proposed, replaced_features):
    """A shared API retains other domains' uses; the local ledger stays in ft-check."""
    retained = [row for row in previous.get("bindings", []) if row["feature_id"] not in replaced_features]
    bindings = retained + proposed["bindings"]
    declarations = {row["id"]: row for row in previous.get("declarations", [])}
    declarations.update({row["id"]: row for row in proposed["api_dispositions"]})
    for api_id in {row["declaration_id"] for row in retained}:
        uses = [row for row in bindings if row["declaration_id"] == api_id]
        row = declarations[api_id]
        status = "assigned" if any(use["role"] == "core" for use in uses) else "supporting"
        declarations[api_id] = {**row, "status": status,
            "reason": "Aggregated documented uses across preserved and revised domains",
            "rule": "binding-role-conservation",
            "evidence_refs": sorted({ref for use in uses for ref in use["evidence_refs"]})}
    topics = {row["id"]: row for row in previous.get("topics", [])}
    for row in proposed["topic_dispositions"]:
        old = topics.get(row["id"])
        if old and old["status"] in ("assigned", "supporting") and row["status"] == "excluded":
            continue
        topics[row["id"]] = row
    routes = [row for row in previous.get("routes", []) if row["feature_id"] not in replaced_features] + proposed.get("routes", [])
    return {"bindings": bindings, "routes": routes, "declarations": list(declarations.values()), "topics": list(topics.values())}
