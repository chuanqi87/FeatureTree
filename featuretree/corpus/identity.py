"""Lossless declaration identity; SDK revision and hierarchy are not identity inputs."""

import re
from featuretree.core.content import digest


def declaration_id(platform, distribution, language, qualified_name, signature):
    normalized = re.sub(r"\s+", " ", signature).strip()
    return "api_" + digest([platform, distribution, language, qualified_name, normalized])


def normalize_legacy(record, source_hash, language):
    platform = record["platform"]
    availability = record.get("availability") or {}
    path = record["source_path"]
    ecosystem = availability.get("contract") not in (None, "os-sdk")
    distribution = {"android": "Android SDK", "ios": "Apple SDK", "harmonyos": "HarmonyOS SDK"}[platform]
    if ecosystem:
        distribution = str(availability["contract"])
    visibility = "unknown"
    if availability.get("systemapi") or "/@internal/" in path or "/PrivateHeaders/" in path:
        visibility = "nonpublic"
    elif availability.get("public") is True:
        visibility = "public"
    # Legacy absence of a systemapi tag is insufficient to certify public application use.
    return {"schema_version": 3, "id": declaration_id(platform, distribution, language,
            record["qualified_name"], record.get("signature") or ""), "platform": platform,
            "distribution": distribution, "language": language,
            "qualified_name": record["qualified_name"], "signature": record.get("signature") or "",
            "kind": record["kind"], "visibility": visibility,
            "availability": {**availability, "since": record.get("since"),
                             "deprecated_since": record.get("deprecated_since"),
                             "module_id": record.get("module_id"), "historical": True},
            "sdk_version": record.get("sdk_stamp", "unknown"), "source_path": path,
            "source_line": record.get("source_line") or 0, "source_hash": source_hash,
            "original_id": record["id"], "documentation": record.get("doc_summary") or "",
            "evidence_refs": []}
