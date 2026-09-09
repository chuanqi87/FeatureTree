"""Claim-level confidence and device-review projections; no IO or automatic grading."""

from collections import Counter
import hashlib
import json

from featuretree.knowledge.comparison import comparison_slots, finding_key, subject_hash

LEVELS = ("high", "medium", "low", "unassessed")


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     default=str, separators=(",", ":")).encode()).hexdigest()


def assessment_input_hash(feature, doc, claim, platforms):
    """Changing the subject, claim, cited sources or runtime invalidates its grading."""
    return fingerprint({
        "subject_hash": subject_hash(feature),
        "claim": {k: v for k, v in claim.items() if k != "assessment"},
        "contexts": {p: doc.get("presence", {}).get(p, {}).get("context") for p in sorted(platforms)},
        "evidence": sorted((e for e in doc.get("evidence", [])
                            if e["id"] in claim.get("evidence_refs", [])), key=lambda e: e["id"]),
    })


def claim_slots(feature, doc, platforms):
    """Include missing comparisons in the denominator; prose is never a graded fact."""
    for platform in sorted(platforms):
        yield f"support:{platform}", "support", "availability", [platform], doc["presence"].get(platform, {})
    findings = {finding_key(f): f for f in doc.get("comparisons", [])}
    for dimension, pair in comparison_slots(feature, platforms):
        yield f"comparison:{dimension}:{':'.join(pair)}", "comparison", dimension, list(pair), findings.get((dimension, pair), {})
    for fact in sorted(doc.get("facts", []), key=lambda f: f["id"]):
        yield f"fact:{fact['id']}", "fact", fact["dimension"], [fact["platform"]], fact


def device_state(review):
    requirement = review.get("requirement", "unassessed")
    if requirement in ("unassessed", "not_required"):
        return requirement
    results = {r["case_id"]: r["outcome"] for r in review.get("results", [])}
    if "fail" in results.values():
        return "failed"
    cases = review.get("cases", [])
    if cases and all(results.get(case["id"]) == "pass" for case in cases):
        return "passed"
    return "pending"


def quality_fields(claim):
    assessment = claim.get("assessment", {})
    review = assessment.get("device_review", {})
    return {"confidence": assessment.get("confidence", "unassessed"),
            "confidence_rationale": assessment.get("rationale", "尚未逐条评估证据和适用范围"),
            "device_requirement": review.get("requirement", "unassessed"),
            "device_state": device_state(review)}


def review_priority(row):
    """An explicit triage order, not an estimate of business impact or correctness."""
    if row["device_state"] == "failed":
        return 0
    if row["device_state"] == "pending":
        return 1 if row["device_requirement"] == "required" else 2
    if row["confidence"] in ("low", "unassessed") or row["device_requirement"] == "unassessed":
        return 3
    return 4


def claim_rows(feature, doc, platforms):
    rows = []
    evidence = {e["id"]: e for e in doc.get("evidence", [])}
    for key, kind, dimension, scope, claim in claim_slots(feature, doc, platforms):
        assessment = claim.get("assessment", {})
        row = {"feature_id": feature["id"], "name_zh": feature["name"]["zh"],
               "role": feature["knowledge_role"], "knowledge_path": feature["knowledge_path"],
               "claim_id": key, "kind": kind, "dimension": dimension, "platforms": scope,
               "statement": claim.get("statement", claim.get("rationale", "尚未形成已核实结论")),
               "scope": claim.get("scope", feature["comparison_scope"]),
               "basis": claim.get("basis"),
               "assessed_by": assessment.get("assessed_by"), "assessed_at": assessment.get("assessed_at"),
               "result": claim.get("status", claim.get("result", "stated" if kind == "fact" else "unknown")),
               "verification": claim.get("verification", "unreviewed"), **quality_fields(claim),
               "contexts": {p: doc["presence"].get(p, {}).get("context") for p in scope},
               "missing_requirements": claim.get("missing_requirements", []),
               "device_review": assessment.get("device_review", {}),
               "evidence": [evidence[r] for r in claim.get("evidence_refs", []) if r in evidence],
               "input_hash": assessment_input_hash(feature, doc, claim, scope)}
        row["priority"] = review_priority(row)
        rows.append(row)
    return rows


def quality_summary(rows):
    counts = {level: sum(r["confidence"] == level for r in rows) for level in LEVELS}
    return {"level": next((level for level in reversed(LEVELS) if counts[level]), "unassessed"),
            "counts": counts, "total": len(rows),
            "device_states": dict(Counter(r["device_state"] for r in rows)),
            "required_pending": sum(r["device_requirement"] == "required" and r["device_state"] == "pending" for r in rows),
            "recommended_pending": sum(r["device_requirement"] == "recommended" and r["device_state"] == "pending" for r in rows)}


def matches_review(row, confidence="", device_review=""):
    if confidence and row["confidence"] != confidence:
        return False
    if device_review in ("required", "recommended"):
        return row["device_requirement"] == device_review and row["device_state"] == "pending"
    return not device_review or row["device_state"] == device_review
