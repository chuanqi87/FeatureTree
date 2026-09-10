"""Complete implementation routes, distinct from the steps composing each route."""

from featuretree.core.content import digest


def binding_hash(bindings, feature_id):
    return digest({key: [row for row in bindings.get(key, []) if row["feature_id"] == feature_id]
                   for key in ("bindings", "routes")})


def validate_routes(features, declarations, bindings, routes):
    indexed = {}
    for route in routes:
        key = (route["feature_id"], route["platform"], route["id"])
        if key in indexed or route["feature_id"] not in features:
            raise ValueError("Duplicate or out-of-scope implementation route")
        if route["completeness"] == "partial" and not route["gaps"]:
            raise ValueError("Partial route must identify missing implementation steps")
        if route["completeness"] == "complete" and route["gaps"]:
            raise ValueError("Route with unresolved gaps cannot be marked complete")
        used = [row for row in bindings if row["feature_id"] == key[0] and row["route_id"] == key[2]
                and declarations[row["declaration_id"]]["platform"] == key[1]]
        step_ids = {api for step in route["steps"] for api in step["api_ids"]}
        if step_ids != {row["declaration_id"] for row in used}:
            raise ValueError("Route steps must account for exactly its bound APIs on one platform")
        if route["completeness"] == "complete" and not any(row["role"] == "core" for row in used):
            raise ValueError("Supporting steps alone cannot form a complete implementation route")
        indexed[key] = route
    for row in bindings:
        if (row["feature_id"], declarations[row["declaration_id"]]["platform"], row["route_id"]) not in indexed:
            raise ValueError("Every API use needs an explicit implementation route with ordered steps")
    return indexed
