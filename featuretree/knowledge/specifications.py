"""Research scope is fixed before facts are produced; mandatory dimensions cannot vanish."""

from itertools import combinations

PLATFORMS = ("android", "ios", "harmonyos")
DIMENSIONS = ("capability_result", "programming_model", "lifecycle_background",
              "permissions_privacy", "limits_precision", "device_forms", "api_surface")


def question_key(question):
    return question["kind"], tuple(sorted(question["platforms"])), question["dimension"]


def validate_spec(spec, feature):
    if spec["feature_id"] != feature["id"] or feature["node_type"] != "leaf":
        raise ValueError("Knowledge specification must target the fixed leaf")
    if bool(spec["freeze_ref"]) == bool(spec["candidate_tree_ref"]):
        raise ValueError("Specification needs exactly one frozen or candidate input")
    dimensions = set(feature["comparison_dimensions"]) | {"capability_result", "api_surface"}
    if not dimensions <= set(DIMENSIONS):
        raise ValueError("Unregistered comparison dimension")
    expected = {("support", (platform,), "availability") for platform in PLATFORMS}
    expected |= {("comparison", tuple(sorted(pair)), dimension)
                 for pair in combinations(PLATFORMS, 2) for dimension in dimensions}
    ids, required = set(), set()
    for question in spec["questions"]:
        if question["id"] in ids:
            raise ValueError("Duplicate question identity")
        ids.add(question["id"])
        if not question["applicability_reason"] or not question["success_criteria"]:
            raise ValueError("Every question needs applicability reasoning and success criteria")
        key = question_key(question)
        if key in required:
            raise ValueError("Duplicate mandatory research slot")
        if question["required"]:
            required.add(key)
    if not expected <= required:
        raise ValueError(f"Mandatory support/comparison questions missing: {sorted(expected-required)}")
    return {question["id"]: question for question in spec["questions"]}
