"""Pure validation of independent review coverage and actionable revisions."""

from datetime import datetime

from jsonschema import Draft202012Validator


def _object(properties):
    return {"type": "object", "properties": properties, "required": list(properties), "additionalProperties": False}


TEXT = {"type": "string", "pattern": r"\S"}
CHECK = _object({"target_id": TEXT, "criterion_id": TEXT, "status": {"enum": ["pending", "pass", "fail"]},
                 "explanation": {"type": "string"}, "evidence_refs": {"type": "array", "items": TEXT}})
ISSUE = _object({"id": TEXT, "target_id": TEXT, "criterion_id": TEXT,
                "status": {"enum": ["open", "resolved"]}, "problem": TEXT, "location": TEXT,
                "required_change": TEXT, "expected_evidence": TEXT})
REVIEW_SCHEMA = _object({
    "schema_version": {"const": 1}, "binding": {"type": "object"}, "author_id": TEXT, "reviewer_id": TEXT,
    "reviewed_at": {"type": ["null", "string"]}, "decision": {"enum": ["pending", "pass", "revise", "blocked"]},
    "checks": {"type": "array", "items": CHECK, "minItems": 1},
    "issues": {"type": "array", "items": ISSUE}})


def review_template(binding, contract, author_id, reviewer_id):
    if not author_id.strip() or not reviewer_id.strip() or author_id.strip().casefold() == reviewer_id.strip().casefold():
        raise ValueError("Record distinct, actual author and independent reviewer identities")
    return {"schema_version": 1, "binding": binding, "author_id": author_id, "reviewer_id": reviewer_id,
            "reviewed_at": None, "decision": "pending",
            "checks": [{"target_id": target, "criterion_id": criterion["id"], "status": "pending",
                        "explanation": "", "evidence_refs": []}
                       for target in contract["scope"]["target_ids"] for criterion in contract["criteria"]],
            "issues": []}


def review_errors(review, binding, contract):
    errors = [f"{list(error.path)}: {error.message}" for error in
              Draft202012Validator(REVIEW_SCHEMA).iter_errors(review)]
    if errors:
        return errors
    if review["binding"] != binding:
        errors.append("Review binding is stale or belongs to another submission")
    if review["author_id"].strip().casefold() == review["reviewer_id"].strip().casefold():
        errors.append("Independent author/reviewer identities required; self-review cannot accept")
    decision = review["decision"]
    if decision != "pending":
        try:
            reviewed_at = datetime.fromisoformat(review["reviewed_at"].replace("Z", "+00:00"))
            if reviewed_at.tzinfo is None:
                raise ValueError("timezone required")
        except (TypeError, AttributeError, ValueError):
            errors.append("Completed review needs an actual timezone-aware reviewed_at")
    expected = {(target, criterion["id"]) for target in contract["scope"]["target_ids"]
                for criterion in contract["criteria"]}
    checks = review["checks"]
    keys = [(row["target_id"], row["criterion_id"]) for row in checks]
    if len(keys) != len(set(keys)) or set(keys) != expected:
        errors.append("Review must cover each selected target and every criterion exactly once")
    for row in checks:
        if row["status"] != "pending" and (not row["explanation"].strip() or not row["evidence_refs"]):
            errors.append("Reviewed criterion needs explanation and specific evidence references")
    issues = review["issues"]
    issue_ids = [issue["id"] for issue in issues]
    if len(issue_ids) != len(set(issue_ids)):
        errors.append("Duplicate issue IDs")
    for issue in issues:
        if (issue["target_id"], issue["criterion_id"]) not in expected:
            errors.append("Revision issue outside assigned scope")
    failed = {(row["target_id"], row["criterion_id"]) for row in checks if row["status"] == "fail"}
    open_issues = {(issue["target_id"], issue["criterion_id"]) for issue in issues if issue["status"] == "open"}
    if failed - open_issues:
        errors.append("Each failed criterion needs an actionable open revision issue")
    if decision == "pass" and (any(row["status"] != "pass" for row in checks) or open_issues):
        errors.append("Cannot pass pending/failed checks or unresolved issues; no average-score acceptance")
    if decision == "revise" and not open_issues:
        errors.append("Revision decision needs actionable open issues")
    if decision == "blocked" and not open_issues:
        errors.append("Blocked decision needs a specific missing input and next action")
    return errors
