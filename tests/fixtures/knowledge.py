"""tests.fixtures.knowledge."""

import copy
import hashlib
from featuretree.knowledge.comparison import new_knowledge, subject_hash
from featuretree.knowledge.confidence import assessment_input_hash, claim_slots


FIXTURE_BODY = b"# Sample capability\n\nSynthetic evidence used only in tests.\n"


def feature():
    return {"schema_version": 2, "id": "sample", "parent": None, "level": "L1",
            "name": {"zh": "样例能力", "en": "Sample"}, "definition": "完成样例任务。",
            "knowledge_role": "leaf", "knowledge_path": "knowledge/sample.yaml",
            "comparison_scope": {"includes": ["样例任务"], "excludes": []},
            "comparison_dimensions": ["availability"]}


def confirmed_doc():
    """Synthetic claims and source metadata; no downloaded platform evidence."""
    doc = new_knowledge(feature(), ["android", "ios"])
    urls = {"android": "https://developer.android.com/reference/fixture",
            "ios": "https://developer.apple.com/documentation/fixture"}
    for platform in doc["presence"]:
        context = {"release": "1.0", "sdk": "1.0", "distribution": platform, "device_forms": ["phone"]}
        doc["presence"][platform] = {
            "status": "supported", "verification": "confirmed", "rationale": "测试用已核实能力。",
            "context": context, "evidence_refs": [platform], "verified_by": "fixture", "verified_at": "2026-09-05",
            "subject_hash": subject_hash(feature()), "basis": "official_statement"}
        doc["evidence"].append({"id": platform, "platform": platform, "title": "Fixture",
                                "url": urls[platform], "locator": "Sample capability",
                                "revision": "sdk-1.0", "applies_to": copy.deepcopy(context),
                                "local_path": f"docs-raw/fixtures/{platform}.md",
                                "sha256": hashlib.sha256(FIXTURE_BODY).hexdigest(),
                                "fetched_at": "2026-09-05T00:00:00Z",
                                "excerpt": "Synthetic evidence used only in tests.",
                                "applicability_note": "Fixture-only SDK 1.0 scope.",
                                "source_kind": "api_reference"})
    doc["comparisons"] = [{"dimension": "availability", "platforms": ["android", "ios"],
                            "result": "same", "verification": "confirmed", "scope": "样例任务",
                            "rationale": "双方在指定条件下满足任务。", "evidence_refs": ["android", "ios"],
                            "verified_by": "fixture", "verified_at": "2026-09-05", "subject_hash": subject_hash(feature()),
                            "basis": "evidence_based_analysis", "coverage_note": "Both synthetic platform fixtures checked."}]
    for _, _, _, platforms, claim in claim_slots(feature(), doc, doc["presence"]):
        claim["assessment"] = {
            "confidence": "high", "rationale": "Synthetic reviewed fixture, not platform research.",
            "assessed_by": "fixture", "assessed_at": "2026-09-05",
            "input_hash": assessment_input_hash(feature(), doc, claim, platforms),
            "device_review": {"requirement": "not_required", "reason": "Synthetic document-only fixture."}}
    return doc
