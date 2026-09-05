"""Pure comparison progress calculations. Absence of findings means unknown."""

import hashlib
import json
from itertools import combinations


def subject_hash(feature):
    """Invalidate confirmations after the comparison subject's meaning changes."""
    subject = {key: feature[key] for key in ("id", "definition", "comparison_scope", "comparison_dimensions")}
    subject.update({key: feature.get(key) for key in ("device_forms", "layer", "privacy_class")})
    return hashlib.sha256(json.dumps(subject, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def comparison_slots(feature, platforms):
    for dimension in feature["comparison_dimensions"]:
        for pair in combinations(sorted(platforms), 2):
            yield dimension, pair


def finding_key(finding):
    return finding["dimension"], tuple(sorted(finding["platforms"]))


def progress(feature, knowledge, platforms):
    slots = set(comparison_slots(feature, platforms))
    findings = {finding_key(f): f for f in knowledge.get("comparisons", [])}
    confirmed = [findings[key] for key in slots if key in findings
                 and findings[key]["verification"] == "confirmed"]
    support_done = sum(knowledge.get("presence", {}).get(p, {}).get("verification") == "confirmed"
                       for p in platforms)
    complete = len(confirmed) == len(slots) and support_done == len(platforms)
    applicable = [f for f in confirmed if f["result"] != "not_applicable"]
    if any(f["result"] == "different" for f in applicable):
        conclusion = "has_confirmed_differences"
    elif complete and applicable:
        conclusion = "confirmed_same"
    elif complete:
        conclusion = "not_applicable"
    else:
        conclusion = "unknown"
    started = bool(findings) or any(c.get("verification") != "unreviewed"
                                   for c in knowledge.get("presence", {}).values())
    return {
        "state": "complete" if complete else "in_progress" if started else "not_started",
        "conclusion": conclusion,
        "confirmed_support": support_done,
        "total_support": len(platforms),
        "confirmed_comparisons": len(confirmed),
        "total_comparisons": len(slots),
    }


def new_knowledge(feature, platforms):
    return {
        "schema_version": 2,
        "feature_id": feature["id"],
        "role": feature["knowledge_role"],
        "status": "stub",
        "baseline": {p: "待确定并固定版本" for p in platforms},
        "definition": feature["definition"],
        "presence": {p: {"status": "unknown", "verification": "unreviewed"} for p in platforms},
        "comparisons": [],
        "evidence": [],
    }
