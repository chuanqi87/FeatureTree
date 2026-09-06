"""Validate preliminary coverage and citations, not semantic correctness."""

from jsonschema import Draft202012Validator


def obj(properties):
    return {"type": "object", "properties": properties, "required": list(properties), "additionalProperties": False}


TEXT = {"type": "string", "pattern": r"\S", "maxLength": 1600}
TEXTS = {"type": "array", "items": TEXT, "minItems": 1, "maxItems": 5}
CITATION = obj({"source_id": TEXT, "locator": TEXT,
                "start_line": {"type": "integer", "minimum": 1},
                "end_line": {"type": "integer", "minimum": 1}})
CITATIONS = {"type": "array", "items": CITATION, "maxItems": 6}
PLATFORM = obj({
    "platform": TEXT, "signal": {"enum": ["documented_mechanism", "possible_mapping", "unknown"]},
    "observation": TEXT, "version_scope": TEXT, "conditions": TEXTS, "gaps": TEXTS,
    "confidence": {"const": "low"}, "evidence_strength": {"enum": ["direct", "indirect", "missing"]},
    "citations": CITATIONS,
    "device_review": obj({"requirement": {"enum": ["required", "recommended", "not_required", "unassessed"]},
                          "reason": TEXT})})
DIFFERENCE = obj({"dimension": TEXT, "statement": TEXT,
                  "platforms": {"type": "array", "items": TEXT, "minItems": 2, "maxItems": 3, "uniqueItems": True},
                  "kind": {"const": "hypothesis"}, "confidence": {"const": "low"},
                  "citations": CITATIONS, "open_questions": TEXTS})
RESPONSE_SCHEMA = obj({
    "task_id": TEXT, "feature_id": TEXT, "stage": {"const": "first_pass"},
    "summary": TEXT, "platforms": {"type": "array", "items": PLATFORM, "minItems": 1, "maxItems": 3},
    "difference_hypotheses": {"type": "array", "items": DIFFERENCE, "maxItems": 3},
    "scope_gaps": TEXTS,
    "followup_priority": obj({"level": {"enum": ["P1", "P2", "P3"]}, "reason": TEXT})})


def response_errors(task, response):
    errors = [f"{list(e.path)}: {e.message}" for e in Draft202012Validator(RESPONSE_SCHEMA).iter_errors(response)]
    if errors:
        return errors
    if response["task_id"] != task["task_id"] or response["feature_id"] != task["feature"]["id"]:
        errors.append("Response belongs to another task/node")
    platforms = [p["platform"] for p in response["platforms"]]
    if len(platforms) != len(set(platforms)) or set(platforms) != set(task["platforms"]):
        errors.append("Answer every assigned platform exactly once")
    sources = {s["id"]: s for s in task["sources"]}

    def citations_cover(citations, required_platforms):
        covered = set()
        for citation in citations:
            source = sources.get(citation["source_id"])
            if not source or source["platform"] not in required_platforms:
                errors.append("Citation outside assigned source/platform scope")
            elif not 1 <= citation["start_line"] <= citation["end_line"] <= source["total_lines"]:
                errors.append("Citation outside source line bounds")
            else:
                covered.add(source["platform"])
        return covered

    for row in response["platforms"]:
        covered = citations_cover(row["citations"], {row["platform"]})
        if row["signal"] != "unknown" and (not covered or row["evidence_strength"] == "missing"):
            errors.append("Non-unknown preliminary signal requires actual cited evidence")
        if row["evidence_strength"] != "missing" and not covered:
            errors.append("Evidence strength requires a source, not model memory")
        if row["evidence_strength"] == "missing" and row["signal"] != "unknown":
            errors.append("Missing evidence must remain unknown")
    for row in response["difference_hypotheses"]:
        if row["dimension"] not in task["feature"]["comparison_dimensions"]:
            errors.append("Difference outside assigned dimensions")
        if not set(row["platforms"]) <= set(task["platforms"]):
            errors.append("Difference outside assigned platforms")
        if citations_cover(row["citations"], set(row["platforms"])) != set(row["platforms"]):
            errors.append("Difference hypothesis needs evidence for every compared platform")
    return errors
