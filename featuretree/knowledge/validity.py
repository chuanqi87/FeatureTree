"""Version dependency checks; cosmetic node changes do not stale research."""

from featuretree.core.content import digest
from featuretree.taxonomy.model import semantic_hash
from featuretree.taxonomy.routes import binding_hash


def stale_reasons(article, feature, bindings, freeze, baseline_ref, source_ids, catalog=None):
    reasons = []
    key = article["feature_id"]
    if feature is None:
        return ["feature_removed"]
    if freeze["semantic_hashes"].get(key) != semantic_hash(feature):
        reasons.append("feature_semantics_changed")
    if freeze["binding_hashes"].get(key) != binding_hash(bindings, key):
        reasons.append("implementation_bindings_changed")
    if article["baseline_ref"] != baseline_ref:
        reasons.append("baseline_changed")
    if article["snapshot_id"] not in source_ids:
        reasons.append("source_snapshot_changed")
    active_source = bindings["snapshot_id"]
    if active_source != article["snapshot_id"]:
        if catalog is None:
            reasons.append("source_dependencies_need_revalidation")
        else:
            try:
                for evidence in article["evidence"]:
                    current = catalog.get(active_source, "documents", evidence["document_id"])
                    if current["status"] != "verified" or current["body_sha256"] != evidence["body_sha256"]:
                        reasons.append("evidence_content_changed")
                        break
                api_ids = {row["declaration_id"] for row in bindings["bindings"] if row["feature_id"] == key}
                if any(digest(catalog.get(active_source, "declarations", api)) !=
                       digest(catalog.get(article["snapshot_id"], "declarations", api)) for api in api_ids):
                    reasons.append("api_declaration_changed")
            except KeyError:
                reasons.append("source_dependency_removed")
    return reasons
