"""Validate claims against explicit scope, platform context and traceable sources."""

import hashlib
import re

from featuretree.knowledge.comparison import finding_key, subject_hash
from featuretree.knowledge.confidence_validation import assessment_errors
from featuretree.knowledge.source_policy import official_source_error
from featuretree.core.storage import contained_path


def snapshot_errors(evidence, root):
    if not evidence.get("local_path"):
        return []
    try:
        path = contained_path(root, evidence["local_path"], "docs-raw")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
    except (ValueError, OSError) as exc:
        return [str(exc)]
    errors = [] if digest == evidence.get("sha256") else [f"Source snapshot hash mismatch: {path}"]
    if evidence.get("excerpt"):
        body = path.read_text(encoding="utf-8")
        if " ".join(evidence["excerpt"].split()) not in " ".join(body.split()):
            errors.append(f"Evidence excerpt not found in source snapshot: {evidence['id']}")
    return errors


def confirmed_claim_errors(claim, platforms, presence, evidence):
    """Presence contexts also define the scope of pairwise findings."""
    errors = []
    if claim.get("basis") not in ("official_statement", "evidence_based_analysis"):
        errors.append("Confirmed claim needs basis: official_statement or evidence_based_analysis")
    if (claim.get("status") == "unsupported" or claim.get("result") in ("same", "not_applicable")) and not claim.get("coverage_note", "").strip():
        errors.append("Negative/equivalence claim needs coverage_note describing the checked scope and alternatives")
    refs = [evidence[r] for r in claim.get("evidence_refs", []) if r in evidence]
    for platform in platforms:
        context = presence.get(platform, {}).get("context", {})
        if not context:
            errors.append(f"Confirmed claim has no platform context: {platform}")
            continue
        for key in ("release", "sdk", "distribution"):
            value = context.get(key, "").strip()
            if not value or re.search(r"master|latest|\bmain\b|待|unknown|\+|\btbd\b|\bpending\b|\bcurrent\b", value, re.I):
                errors.append(f"Unpinned {platform} context: {key}")
        sources = [e for e in refs if e["platform"] == platform]
        if not sources:
            errors.append(f"Confirmed claim needs evidence for {platform}")
        for source in sources:
            for key in ("local_path", "sha256", "fetched_at", "excerpt", "applicability_note", "source_kind"):
                if not source.get(key):
                    errors.append(f"Confirmed evidence needs {key}: {source['id']}")
            error = official_source_error(source["url"], platform, context.get("distribution", ""))
            if error:
                errors.append(f"{source['id']}: {error}")
            if not source.get("locator") or not source.get("revision"):
                errors.append(f"Evidence needs locator and fixed revision: {source['id']}")
            if re.search(r"master|latest|\bmain\b|待|unknown|\+", source.get("revision", ""), re.I):
                errors.append(f"Unpinned source revision: {source['id']}")
            if source.get("applies_to") != context:
                errors.append(f"Evidence/context mismatch: {source['id']} ({platform})")
    return errors


def validate_knowledge_evidence(features, knowledge, platforms, root):
    errors = []
    for fid, doc in knowledge.items():
        sources = doc["evidence"]
        evidence = {e["id"]: e for e in sources}
        if len(evidence) != len(sources):
            errors.append(f"Duplicate evidence id: {fid}")
        for source in sources:
            if source["platform"] not in platforms and source["platform"] != "cross":
                errors.append(f"Unknown evidence platform: {fid}: {source['platform']}")
            errors.extend(f"{fid}: {err}" for err in snapshot_errors(source, root))
        keys = set()
        claims = [(f"support:{p}", cell, [p]) for p, cell in doc["presence"].items()]
        fact_ids = set()
        for fact in doc.get("facts", []):
            if fact["id"] in fact_ids:
                errors.append(f"Duplicate fact id: {fid}: {fact['id']}")
            fact_ids.add(fact["id"])
            if fact["platform"] not in platforms or fact["dimension"] not in features[fid]["comparison_dimensions"]:
                errors.append(f"Fact outside node platform/dimension scope: {fid}: {fact['id']}")
            claims.append((f"fact:{fact['id']}", fact, [fact["platform"]]))
        for finding in doc["comparisons"]:
            key = finding_key(finding)
            if key in keys:
                errors.append(f"Duplicate comparison dimension/pair: {fid}: {key}")
            keys.add(key)
            if finding["dimension"] not in features[fid]["comparison_dimensions"]:
                errors.append(f"Comparison outside node dimensions: {fid}: {key}")
            if set(finding["platforms"]) - set(platforms):
                errors.append(f"Unknown comparison platform: {fid}: {key}")
            claims.append((str(key), finding, finding["platforms"]))
        for label, claim, claim_platforms in claims:
            errors.extend(f"{fid}: {label}: {e}" for e in
                          assessment_errors(features[fid], doc, claim, claim_platforms, root))
            for ref in claim.get("evidence_refs", []):
                if ref not in evidence:
                    errors.append(f"Broken evidence reference: {fid}: {label}: {ref}")
            if claim["verification"] == "confirmed" or claim.get("assessment", {}).get("confidence") == "medium":
                if claim.get("subject_hash") != subject_hash(features[fid]):
                    errors.append(f"Comparison subject changed; re-review required: {fid}: {label}")
                errors.extend(f"{fid}: {label}: {e}" for e in
                              confirmed_claim_errors(claim, claim_platforms, doc["presence"], evidence))
    return errors
