"""Export an explicit, budgetable claim scope without starting research or tests."""

from featuretree.knowledge.confidence import claim_rows, fingerprint, matches_review, quality_summary


DEVICE_FILTERS = ("required", "recommended", "failed", "passed", "not_required", "unassessed")


def build_scope(features, knowledge, platforms, *, domain="", role="", confidence="", device_review="", limit=None):
    if domain and domain not in features:
        raise ValueError(f"Unknown feature subtree: {domain}")
    if limit is not None and limit < 1:
        raise ValueError("limit must be positive")
    filters = {"domain": domain, "role": role, "confidence": confidence, "device_review": device_review, "limit": limit}
    rows = []
    for fid, feature in sorted(features.items()):
        ancestor = fid
        while domain and ancestor is not None and ancestor != domain:
            ancestor = features[ancestor]["parent"]
        if (domain and ancestor is None) or (role and feature["knowledge_role"] != role):
            continue
        rows.extend(row for row in claim_rows(feature, knowledge[fid], platforms)
                    if matches_review(row, confidence, device_review))
    rows.sort(key=lambda r: (r["priority"], r["feature_id"], r["claim_id"]))
    selected = rows[:limit] if limit is not None else rows
    return {"schema_version": 1, "filters": filters, "total_matching_claims": len(rows),
            "selected_claims": len(selected), "omitted_claims": len(rows) - len(selected),
            "feature_ids": sorted({r["feature_id"] for r in selected}),
            "summary": quality_summary(selected), "claims": selected,
            "scope_hash": fingerprint({"filters": filters, "claims": selected}),
            "notice": "仅定义待分析/复核范围，不启动任务。实测通过仅限计划中的设备、版本与条件；未评估不等于无需实测。"}
