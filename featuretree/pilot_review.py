"""Pilot acceptance allows explicit unknowns, while requiring reviewed coverage."""

import json

from .comparison import comparison_slots, finding_key


def pilot_errors(repo, rows, knowledge, features, config, run_date):
    path = repo.root / "output/research/pilot-review.json"
    try:
        reviews = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    except (ValueError, OSError) as exc:
        return [f"Invalid pilot review: {exc}"], [row["feature_id"] for row in rows if row["pilot"]]
    errors, pending = [], []
    for row in rows:
        if not row["pilot"]:
            continue
        fid = row["feature_id"]
        review = reviews.get(fid, {}) if isinstance(reviews, dict) else {}
        if not isinstance(review, dict):
            review = {}
        problems = []
        if review.get("input_hash") != row["input_hash"] or review.get("verified_at") != run_date:
            problems.append("missing or stale pilot review")
        if any(not str(review.get(key, "")).strip() for key in ("verified_by", "scope_review", "evidence_review")):
            problems.append("reviewer and scope/evidence review notes required")
        doc = knowledge.get(fid, {})
        findings = {finding_key(f): f for f in doc.get("comparisons", [])}
        claims = [doc.get("presence", {}).get(p, {}) for p in config["platforms"]]
        claims += [findings.get(slot, {}) for slot in comparison_slots(features[fid], config["platforms"])]
        for claim in claims:
            if not claim.get("assessment"):
                problems.append("every investigated claim needs confidence and physical-device review assessment")
                break
            result = claim.get("status", claim.get("result"))
            if result == "unknown" and claim.get("missing_requirements") and claim.get("rationale"):
                continue
            if claim.get("verification") != "confirmed":
                problems.append("every platform/dimension must have a validated result or an explicit unknown with rationale and missing_requirements")
                break
        if problems:
            pending.append(fid)
            errors.append(f"Pilot {fid}: {'; '.join(problems)}")
    return errors, pending
