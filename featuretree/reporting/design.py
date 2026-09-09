"""Export current authored domain definitions as compact design inputs."""

from __future__ import annotations
from featuretree.core.storage import Repository


def export_domain(repo: Repository, domain: str) -> dict:
    features = repo.features()
    authored = []
    for feature in features.values():
        fid = feature["id"]
        if fid == domain or fid.startswith(domain + "."):
            authored.append({
                "id": fid,
                "parent": feature.get("parent"),
                "level": feature.get("level"),
                "name": feature.get("name"),
                "definition": feature.get("definition"),
                "knowledge_role": feature.get("knowledge_role"),
                "bindings": feature.get("bindings") or {},
            })
    authored.sort(key=lambda item: item["id"])

    return {
        "domain": domain,
        "authored_count": len(authored),
        "authored": authored,
        "notice": "Current taxonomy only; no historical campaign data included.",
    }
