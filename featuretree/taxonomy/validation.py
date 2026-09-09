"""Validate tree relationships and ownership of attached knowledge records."""


def validate_tree(features, knowledge, paths, config):
    errors = []
    children = {fid: [] for fid in features}
    for fid, feature in features.items():
        parent = feature["parent"]
        if parent in children:
            children[parent].append(fid)
        elif parent is not None:
            errors.append(f"Missing parent: {fid} -> {parent}")
        level = int(feature["level"][1:])
        if parent is None and level != 1:
            errors.append(f"Non-L1 root: {fid}")
        if parent in features and level != int(features[parent]["level"][1:]) + 1:
            errors.append(f"Parent/child depth mismatch: {fid}")
        seen = set()
        cur = fid
        while cur in features:
            if cur in seen:
                errors.append(f"Tree cycle from {fid}: {cur}")
                break
            seen.add(cur)
            cur = features[cur]["parent"]
        if set(feature["comparison_dimensions"]) - set(config["dimensions"]):
            errors.append(f"Unknown comparison dimension: {fid}")
        for related in feature.get("related_features", []):
            if related not in features or related == fid:
                errors.append(f"Invalid related feature: {fid} -> {related}")
        if fid not in knowledge:
            errors.append(f"Missing knowledge: {fid}")
            continue
        doc = knowledge[fid]
        if feature["knowledge_path"] != paths[fid]:
            errors.append(f"Knowledge path mismatch: {fid}")
        if feature["knowledge_role"] != doc["role"]:
            errors.append(f"Knowledge role mismatch: {fid}")
        if feature["definition"] != doc["definition"]:
            errors.append(f"Comparison subject definition drift: {fid}")
        if set(doc["presence"]) != set(config["platforms"]):
            errors.append(f"Missing or unknown platform assessment: {fid}")
        for target in doc.get("permissions_privacy", {}).get("cross_ref", []):
            if target not in features:
                errors.append(f"Broken knowledge reference: {fid} -> {target}")
    for fid, feature in features.items():
        if feature["knowledge_role"] == "leaf" and children[fid]:
            errors.append(f"Leaf has children: {fid}")
        # An explicitly declared branch is a valid intermediate design artifact.
        # Its lack of children is reported by tree lint and blocks tree freeze.
        pending_branch = feature.get("granularity") == "branch" and not feature.get("leaf_at_this_level")
        if feature["knowledge_role"] == "rollup" and not children[fid] and not pending_branch:
            errors.append(f"Rollup has no children: {fid}")
        if fid in knowledge and "child_index" in knowledge[fid]:
            if set(knowledge[fid]["child_index"]) != set(children[fid]):
                errors.append(f"Stale knowledge child_index: {fid}")
    errors.extend(f"Orphan knowledge: {fid}" for fid in knowledge.keys() - features.keys())
    return errors
