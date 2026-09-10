"""Version dependency checks; cosmetic node changes do not stale research."""

from featuretree.core.content import digest
from featuretree.taxonomy.model import semantic_hash


def stale_reasons(article, feature, bindings, freeze, baseline_ref, source_ids):
    reasons = []
    key = article["feature_id"]
    if feature is None:
        return ["feature_removed"]
    if freeze["semantic_hashes"].get(key) != semantic_hash(feature):
        reasons.append("feature_semantics_changed")
    if freeze["binding_hashes"].get(key) != digest([row for row in bindings["bindings"] if row["feature_id"] == key]):
        reasons.append("implementation_bindings_changed")
    if article["baseline_ref"] != baseline_ref:
        reasons.append("baseline_changed")
    if article["snapshot_id"] not in source_ids:
        reasons.append("source_snapshot_changed")
    return reasons
