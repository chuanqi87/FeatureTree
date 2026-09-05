"""Complete reverse index over authored bindings and catalog mappings."""


def build_index(features, inventory):
    index = {}

    def add(record, source):
        key = record["platform"], record["native_id"], record["feature_id"]
        item = index.setdefault(key, {"platform": key[0], "native_id": key[1],
                                      "feature_id": key[2], "sources": []})
        item["sources"].append({"origin": source, **{
            field: value for field, value in record.items()
            if field not in ("platform", "native_id", "feature_id")}})

    for fid, feature in features.items():
        for platform, bindings in feature.get("bindings", {}).items():
            for binding in bindings:
                add({"platform": platform, "native_id": binding["id"], "feature_id": fid,
                     **{k: v for k, v in binding.items() if k != "id"},
                     "verification": "candidate"}, "taxonomy")
    for row in inventory:
        for mapping in row["mappings"]:
            add({"platform": row["platform"], "native_id": row["native_id"],
                 "kind": row["kind"], "url": row["url"], "scope": row["scope"],
                 "visibility": row["visibility"], **mapping}, "inventory")
    return [index[key] for key in sorted(index)]
