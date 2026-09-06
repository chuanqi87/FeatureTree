"""Pure validation of bounded diagnostic answers, never semantic confirmation."""

from jsonschema import Draft202012Validator


def object_schema(properties, required=None):
    return {"type": "object", "properties": properties, "additionalProperties": False,
            "required": list(properties) if required is None else required}


TEXT = {"type": "string", "pattern": r"\S", "maxLength": 1800}
TEXTS = {"type": "array", "items": TEXT, "minItems": 1, "maxItems": 8, "uniqueItems": True}
CASE = object_schema({"device_model": TEXT, "os_build": TEXT, "conditions": TEXTS,
                      "steps": TEXTS, "expected": TEXT})
DEVICE_REVIEW = object_schema({
    "requirement": {"enum": ["required", "recommended", "not_required"]},
    "reason": TEXT, "cases": {"type": "array", "items": CASE, "maxItems": 3}})
CITATION = object_schema({"source_id": TEXT, "locator": TEXT,
                          "start_line": {"type": "integer", "minimum": 1},
                          "end_line": {"type": "integer", "minimum": 1}})
ANSWER = object_schema({
    "question_id": TEXT, "observation": TEXT, "conditions": TEXTS,
    "not_established": TEXTS, "missing_requirements": TEXTS,
    "confidence": {"const": "low"}, "confidence_reason": TEXT,
    "citations": {"type": "array", "items": CITATION, "minItems": 1, "maxItems": 6},
    "device_review": DEVICE_REVIEW})
RESPONSE_SCHEMA = object_schema({
    "probe_id": TEXT, "answers": {"type": "array", "items": ANSWER, "minItems": 1, "maxItems": 3}})


def response_errors(bundle, response):
    errors = [f"{list(error.path)}: {error.message}" for error in
              Draft202012Validator(RESPONSE_SCHEMA).iter_errors(response)]
    if errors:
        return errors
    if response["probe_id"] != bundle["probe_id"]:
        errors.append("Response belongs to a different probe")
    questions = {q["id"]: q for q in bundle["questions"]}
    answer_ids = [a["question_id"] for a in response["answers"]]
    if len(answer_ids) != len(set(answer_ids)) or set(answer_ids) != set(questions):
        return errors + ["Answer each selected question exactly once; do not expand scope"]
    sources = {s["id"]: s for s in bundle["sources"]}
    for answer in response["answers"]:
        question = questions[answer["question_id"]]
        for citation in answer["citations"]:
            source = sources.get(citation["source_id"])
            start, end = citation["start_line"], citation["end_line"]
            if not source or source["id"] not in question["source_ids"]:
                errors.append(f"{question['id']}: citation outside assigned sources")
            elif end < start or not any(s["start_line"] <= start <= end <= s["end_line"]
                                       for s in source["segments"]):
                errors.append(f"{question['id']}: citation outside supplied line ranges")
            elif not any(line["text"].strip() for segment in source["segments"]
                         for line in segment["lines"] if start <= line["line"] <= end):
                errors.append(f"{question['id']}: citation contains no source text")
        review = answer["device_review"]
        needs_cases = review["requirement"] != "not_required"
        if needs_cases != bool(review["cases"]):
            errors.append(f"{question['id']}: device plan must match its requirement")
    return errors
