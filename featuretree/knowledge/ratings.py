"""Deterministic confidence ceilings and weakest-required-conclusion aggregation."""

from featuretree.knowledge.claims import claim_hash, validate_claims

LEVEL = {"low": 0, "medium": 1, "high": 2}


def rate_article(spec, claims, reviews, assessments, evidence):
    by_id = validate_claims(spec, claims)
    review_by_id = {row["claim_id"]: row for row in reviews}
    ratings = {row["claim_id"]: row for row in assessments}
    if len(review_by_id) != len(reviews) or set(review_by_id) != set(by_id):
        raise ValueError("Independent review must cover every finalized claim exactly once")
    if len(ratings) != len(assessments) or set(ratings) != set(by_id):
        raise ValueError("Every substantive assertion needs one version-bound assessment")
    evidence_by_id = {item["id"]: item for item in evidence}
    for key, claim in by_id.items():
        review, assessment = review_by_id[key], ratings[key]
        fingerprint = claim_hash(claim)
        if review["claim_hash"] != fingerprint or assessment["claim_hash"] != fingerprint:
            raise ValueError("Review or assessment targets stale claim content")
        if review["verdict"] in ("invalid", "revise"):
            raise ValueError("Known erroneous or rejected content cannot be published with a low rating")
        if not set(claim["evidence_refs"]) <= set(evidence_by_id):
            raise ValueError("Claim references missing evidence")
        level = LEVEL[assessment["level"]]
        unknown_applicability = not claim["context"] or any(
            item["applicability"] != "verified" for item in claim["context"])
        missing_observation = assessment["requires_runtime_observation"] and not assessment["runtime_evidence_refs"]
        low_required = claim["result"] == "unknown" or unknown_applicability or missing_observation
        low_required |= any(evidence_by_id[item]["applicability"] != "verified" for item in claim["evidence_refs"])
        if low_required and level > LEVEL["low"]:
            raise ValueError("Unknown applicability, conclusion or required observation caps confidence at low")
        if level == LEVEL["high"] and (review["verdict"] != "confirmed" or claim["gaps"] or assessment["gaps"]):
            raise ValueError("High confidence requires independent confirmation without unresolved gaps")
        if assessment["runtime_evidence_refs"]:
            # Runtime results are never inferred from source documents or model assertions.
            raise ValueError("Runtime observation must be imported as a separately verified test artifact before rating")
        for premise in claim["premise_ids"]:
            if level > LEVEL[ratings[premise]["level"]]:
                raise ValueError("Comparison confidence exceeds its weakest critical premise")
    required = {question["id"] for question in spec["questions"] if question["required"]}
    essential = [row for row in claims if row["question_id"] in required]
    if not essential:
        raise ValueError("Article has no required conclusions")
    minimum = min(LEVEL[ratings[row["claim_id"]]["level"]] for row in essential)
    overall = next(name for name, level in LEVEL.items() if level == minimum)
    return overall, [row["claim_id"] for row in essential if ratings[row["claim_id"]]["level"] == overall]
