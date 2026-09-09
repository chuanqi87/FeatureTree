"""Confidence acceptance and human-device artifact integrity, separate from grading."""

import hashlib
import re

from featuretree.knowledge.confidence import assessment_input_hash, fingerprint
from featuretree.core.storage import contained_path


def device_review_errors(review, platforms, presence, root, claim_hash):
    errors = []
    cases = {case["id"]: case for case in review.get("cases", [])}
    if len(cases) != len(review.get("cases", [])):
        errors.append("Duplicate device case id")
    if review["requirement"] in ("required", "recommended"):
        if {case["platform"] for case in cases.values()} != set(platforms):
            errors.append("Device plan must cover exactly the claim platforms")
    for case in cases.values():
        if case["context"] != presence.get(case["platform"], {}).get("context"):
            errors.append(f"Device case/context mismatch: {case['id']}")
    seen = set()
    for result in review.get("results", []):
        key = result["case_id"]
        if key in seen:
            errors.append(f"Duplicate device result: {key}; retain historical runs in artifacts")
        seen.add(key)
        if result["claim_hash"] != claim_hash:
            errors.append(f"Device result belongs to another claim/context/source revision: {key}")
        case = cases.get(key)
        if not case or result["plan_hash"] != fingerprint(case):
            errors.append(f"Missing or changed device case: {key}")
        elif any(re.search(r"待|unknown|latest|pending|tbd|模拟|simulator|emulator", case[k], re.I)
                 for k in ("device_model", "os_build")):
            errors.append(f"Physical device model/build must be concrete: {key}")
        try:
            path = contained_path(root, result["artifact_path"], "output/research/device-reviews")
            if hashlib.sha256(path.read_bytes()).hexdigest() != result["sha256"]:
                errors.append(f"Device artifact hash mismatch: {key}")
        except (ValueError, OSError) as exc:
            errors.append(f"Device artifact unavailable: {key}: {exc}")
    return errors


def assessment_errors(feature, doc, claim, platforms, root):
    assessment = claim.get("assessment")
    if not assessment:
        return ["Confirmed claim requires confidence and device-review assessment"] if claim.get("verification") == "confirmed" else []
    errors = []
    if assessment["input_hash"] != assessment_input_hash(feature, doc, claim, platforms):
        errors.append("Confidence assessment input changed; re-review required")
    level = assessment["confidence"]
    if level == "unassessed" and claim.get("verification") == "confirmed":
        errors.append("Confirmed claim must have an explicit confidence tier")
    if level == "high" and claim.get("verification") != "confirmed":
        errors.append("High confidence requires confirmed official evidence")
    if level in ("high", "medium"):
        if claim.get("status", claim.get("result")) == "unknown":
            errors.append("Unknown conclusion cannot have high/medium confidence")
        if any(r["outcome"] != "pass" for r in assessment["device_review"].get("results", [])):
            errors.append("Conflicting/inconclusive device results require low confidence or unassessed")
    if level == "high" and claim.get("missing_requirements"):
        errors.append("High confidence cannot hide unresolved evidence gaps")
    if level == "low" and not (claim.get("evidence_refs") or claim.get("missing_requirements")):
        errors.append("Low confidence needs traceable evidence or explicit missing_requirements")
    errors.extend(device_review_errors(assessment["device_review"], platforms, doc["presence"], root,
                                      assessment_input_hash(feature, doc, claim, platforms)))
    return errors
