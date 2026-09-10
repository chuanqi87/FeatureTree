"""Conservation checks; processed sources, assigned APIs and covered use cases differ."""

from collections import Counter, defaultdict


RESOLVED = {"assigned", "supporting", "excluded"}


def disposition_report(expected_ids, dispositions):
    expected = set(expected_ids)
    observed = [row["id"] for row in dispositions]
    if len(observed) != len(set(observed)):
        raise ValueError("Duplicate disposition; every input gets exactly one status")
    if set(observed) != expected:
        raise ValueError(f"Disposition conservation failed: missing={len(expected-set(observed))}, extra={len(set(observed)-expected)}")
    for row in dispositions:
        if row["status"] == "excluded" and (not row["reason"] or not row["rule"] or not row["evidence_refs"]):
            raise ValueError("Exclusion requires a rule, reason and evidence")
    counts = dict(Counter(row["status"] for row in dispositions))
    return {"total": len(expected), "by_status": counts,
            "unresolved_ids": [row["id"] for row in dispositions if row["status"] not in RESOLVED],
            "complete": all(row["status"] in RESOLVED for row in dispositions)}


def validate_bindings(features, declarations, bindings, dispositions):
    report = disposition_report(declarations, dispositions)
    by_api, seen = defaultdict(list), set()
    for binding in bindings:
        identity = (binding["declaration_id"], binding["feature_id"], binding["usage"], binding["route_id"])
        if identity in seen:
            raise ValueError("Duplicate API use binding")
        seen.add(identity)
        if binding["declaration_id"] not in declarations:
            raise ValueError("Binding references API outside the fixed input scope")
        if binding["feature_id"] not in features or features[binding["feature_id"]]["node_type"] != "leaf":
            raise ValueError("Binding target must be a candidate leaf")
        if not binding["evidence_refs"] or not binding["usage"]:
            raise ValueError("Binding requires documented usage and evidence")
        by_api[binding["declaration_id"]].append(binding)
    for row in dispositions:
        roles = {binding["role"] for binding in by_api[row["id"]]}
        if row["status"] == "assigned" and "core" not in roles:
            raise ValueError("Assigned API has no core binding")
        if row["status"] == "supporting" and (not roles or "core" in roles):
            raise ValueError("Supporting disposition disagrees with binding roles")
        if row["status"] not in ("assigned", "supporting") and roles:
            raise ValueError("Unresolved/excluded API cannot silently carry a binding")
    return report


def size_report(declarations, families, bindings, *, enumeration_complete):
    family_of = {}
    for family in families:
        for api_id in family["declaration_ids"]:
            if api_id in family_of:
                raise ValueError("Declaration appears in multiple counting families")
            family_of[api_id] = family["id"]
    leaves = {}
    for binding in bindings:
        api_id = binding["declaration_id"]
        declaration = declarations[api_id]
        if api_id not in family_of:
            raise ValueError("Core API cannot be counted without an explicit family")
        leaf = leaves.setdefault(binding["feature_id"], {"all_api_ids": set(), "supporting_api_ids": set(), "routes": {}})
        leaf["all_api_ids"].add(api_id)
        if binding["role"] == "supporting":
            leaf["supporting_api_ids"].add(api_id)
        route = leaf["routes"].setdefault((declaration["platform"], binding["route_id"]), set())
        if binding["role"] == "core":
            route.add(family_of[api_id])
    return {feature_id: {"all_api_count": len(value["all_api_ids"]),
                         "supporting_api_count": len(value["supporting_api_ids"]),
                         "counts_are_lower_bounds": not enumeration_complete,
                         "routes": [{"platform": platform, "route_id": route,
                                     "core_family_count": len(ids), "family_ids": sorted(ids)}
                                    for (platform, route), ids in sorted(value["routes"].items())]}
            for feature_id, value in leaves.items()}
