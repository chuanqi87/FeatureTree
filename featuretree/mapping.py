"""Generate reviewable mapping candidates without inventing coverage."""

import re


def propose_mapping(row, feature_ids, rules):
    if row["scope"] == "excluded":
        return []
    native = row["native_id"]
    # A documentation filename may suggest its kit's catalog, never a precise API match.
    proxy = "/" in native and row["platform"] == "harmonyos"
    search = row.get("parent", "") if proxy else native
    for rule in rules:
        if rule["platform"] != row["platform"]:
            continue
        if re.search(rule["pattern"], search, re.I):
            fid = rule["feature_id"]
            if fid not in feature_ids:
                # A missing target is an invalid rule, not permission to fall back to L1.
                raise ValueError(f"Mapping rule references missing feature: {fid}")
            return [{"feature_id": fid,
                     "relationship": "catalog" if proxy else rule["relationship"],
                     "verification": "candidate", "method": "rule",
                     "rationale": f"名称规则候选：{rule['pattern']}；尚未确认能力语义与版本。"}]
    return []


def map_row(row, feature_ids, rules):
    manual = [m for m in row["mappings"] if m["method"] == "manual"]
    # A manual decision owns this record. Rule refresh never overwrites it.
    return {**row, "mappings": manual if manual else propose_mapping(row, feature_ids, rules)}


def validate_inventory(rows, features, platforms):
    errors = []
    seen = set()
    for row in rows:
        key = row["platform"], row["native_id"]
        if key in seen:
            errors.append(f"Duplicate inventory key: {key}")
        seen.add(key)
        if row["platform"] not in platforms:
            errors.append(f"Unknown inventory platform: {key}")
        if row["scope"] == "included" and (row["visibility"] != "public"
                or "系统接口" in row["title"] or "-sys.md" in row["native_id"]):
            errors.append(f"Non-public interface included: {key}")
        mapped = set()
        for mapping in row["mappings"]:
            fid = mapping["feature_id"]
            if fid not in features:
                errors.append(f"Missing mapping target: {key} -> {fid}")
            if fid in mapped:
                errors.append(f"Duplicate mapping target: {key} -> {fid}")
            mapped.add(fid)
            if mapping["verification"] == "confirmed" and row["scope"] != "included":
                errors.append(f"Confirmed mapping outside included scope: {key}")
    return errors
