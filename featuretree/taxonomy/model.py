"""Stable feature identity, topology and semantic fingerprints."""

from uuid import uuid4

from featuretree.core.content import digest


def validate_tree(tree):
    nodes = {}
    for feature in tree["features"]:
        if feature["id"] in nodes:
            raise ValueError(f"Duplicate feature: {feature['id']}")
        nodes[feature["id"]] = feature
        if feature["node_type"] == "leaf" and not feature["success_criteria"]:
            raise ValueError("Leaf requires independent success criteria")
    children = {key: [] for key in nodes}
    for key, feature in nodes.items():
        parent = feature["parent_id"]
        if parent is not None:
            if parent not in nodes:
                raise ValueError(f"Missing parent: {parent}")
            children[parent].append(key)
        seen, current = set(), key
        while current is not None:
            if current in seen:
                raise ValueError(f"Tree cycle: {current}")
            seen.add(current)
            if current not in nodes:
                raise ValueError(f"Missing ancestor: {current}")
            current = nodes[current]["parent_id"]
    for key, feature in nodes.items():
        if feature["node_type"] == "leaf" and children[key]:
            raise ValueError(f"Leaf has descendants: {key}")
        siblings = [nodes[child]["name"].casefold() for child in children[key]]
        if len(siblings) != len(set(siblings)):
            raise ValueError(f"Duplicate sibling names: {key}")
    for event in tree["lineage"]:
        if not event["old_ids"] or not event["new_ids"] or not event["reason"]:
            raise ValueError("Split/merge must preserve old and new identities and reason")
        if set(event["old_ids"]) & set(event["new_ids"]):
            raise ValueError("Split/merge must generate new identities")
        if not set(event["new_ids"]) <= set(nodes):
            raise ValueError("Lineage destinations missing")
    return nodes


def subtree_ids(nodes, root_ids):
    if not set(root_ids) <= set(nodes):
        raise ValueError("Unknown subtree root")
    selected = set(root_ids)
    while True:
        expanded = selected | {key for key, node in nodes.items() if node["parent_id"] in selected}
        if expanded == selected:
            return sorted(selected)
        selected = expanded


def semantic_hash(feature):
    return digest({key: value for key, value in feature.items() if key not in ("name", "parent_id")})


def assign_identities(features, mapping, existing_ids=()):
    """Caller durably stores this mapping before accepting a result; retries reuse it."""
    existing = set(existing_ids)
    result = []
    for feature in features:
        candidate = feature["id"]
        if candidate not in existing:
            mapping.setdefault(candidate, "f_" + uuid4().hex)
    for feature in features:
        parent = feature["parent_id"]
        result.append({**feature, "id": mapping.get(feature["id"], feature["id"]),
                       "parent_id": mapping.get(parent, parent)})
    return result, mapping


def change_impact(before, after):
    old, new = validate_tree(before), validate_tree(after)
    return {"added": sorted(new.keys() - old.keys()), "removed": sorted(old.keys() - new.keys()),
            "semantic_changes": sorted(key for key in old.keys() & new.keys()
                                       if semantic_hash(old[key]) != semantic_hash(new[key])),
            "presentation_changes": sorted(key for key in old.keys() & new.keys()
                                           if old[key] != new[key] and semantic_hash(old[key]) == semantic_hash(new[key]))}
