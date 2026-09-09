"""Pure constructors for taxonomy nodes and API bindings."""

from __future__ import annotations

DEFAULT_DIMENSIONS = [
    "availability",
    "programming_model",
    "lifecycle_background",
    "permissions_privacy",
    "limits_precision",
    "device_forms",
    "api_surface",
]


def feature(
    fid: str,
    *,
    parent: str | None,
    level: str,
    zh: str,
    en: str,
    definition: str,
    includes: list[str],
    excludes: list[str] | None = None,
    granularity: str = "branch",
    sibling_axis: str | None = None,
    bindings: dict | None = None,
    legacy: dict | None = None,
    related: list[str] | None = None,
    aliases: list[str] | None = None,
    layer: str = "os",
    device_forms: list[str] | None = None,
    privacy_class: str = "none",
    notes: str | None = None,
) -> dict:
    parts = fid.split(".")
    if parent is None:
        knowledge_path = f"knowledge/{fid}/_rollup.yaml"
    elif granularity == "atomic":
        knowledge_path = "knowledge/" + "/".join(parts) + ".yaml"
    else:
        knowledge_path = "knowledge/" + "/".join(parts) + "/_rollup.yaml"

    node = {
        "id": fid,
        "level": level,
        "parent": parent,
        "name": {"zh": zh, "en": en},
        "definition": definition,
        "knowledge_role": "leaf" if granularity == "atomic" else "rollup",
        "layer": layer,
        "device_forms": device_forms or ["phone", "tablet"],
        "privacy_class": privacy_class,
        "knowledge_path": knowledge_path,
        "bindings": bindings or {},
        "comparison_scope": {
            "includes": includes,
            "excludes": excludes if excludes is not None else ["无相邻混淆项时由子节点各自界定"],
        },
        "schema_version": 2,
        "comparison_dimensions": list(DEFAULT_DIMENSIONS),
        "granularity": granularity,
        "anchor_status": "unverified",
        "legacy": legacy or {"disposition": "new", "sources": []},
    }
    if sibling_axis:
        node["sibling_axis"] = sibling_axis
    if granularity == "atomic":
        node["leaf_at_this_level"] = True
        if level not in {"L1", "L2"}:
            node["split_justification"] = "independent_capability"
    if related:
        node["related_features"] = related
    if aliases:
        node["aliases"] = aliases
    if notes:
        node["notes"] = notes
    return node


def bind(platform: str, kind: str, symbol: str, url: str, **extra) -> dict:
    entry = {"kind": kind, "id": symbol, "url": url, "role": "primary"}
    entry.update(extra)
    return {platform: [entry]}

