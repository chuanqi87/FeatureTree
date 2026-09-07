#!/usr/bin/env python3
"""Structural lint for authored taxonomy trees."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict

import _bootstrap  # noqa: F401
from featuretree.storage import ROOT, Repository, read_yaml, write_json, write_text


BRAND_RE = re.compile(
    r"(Android|iOS|iPhone|HarmonyOS|鸿蒙|华为|Huawei|Firebase|Google\s|Apple\s|Kit\b)",
    re.I,
)


def _children_map(features: dict) -> dict[str, list[str]]:
    children: dict[str, list[str]] = defaultdict(list)
    for feature in features.values():
        parent = feature.get("parent")
        if parent:
            children[parent].append(feature["id"])
    for parent, kids in children.items():
        kids.sort()
    return children


def lint_features(features: dict, old_ids: set[str], domain: str | None = None) -> list[dict]:
    issues: list[dict] = []
    children = _children_map(features)
    selected = {
        fid: feature
        for fid, feature in features.items()
        if domain is None or fid == domain or fid.startswith(domain + ".")
    }

    for fid, feature in selected.items():
        kids = children.get(fid, [])
        granularity = feature.get("granularity")
        role = feature.get("knowledge_role")
        level = feature.get("level") or ""
        parent = feature.get("parent")

        if granularity == "atomic":
            if kids:
                issues.append({"severity": "error", "id": fid, "code": "atomic_has_children",
                               "message": "atomic node must not have children"})
            if not feature.get("leaf_at_this_level"):
                issues.append({"severity": "error", "id": fid, "code": "atomic_missing_leaf_flag",
                               "message": "atomic node requires leaf_at_this_level: true"})
            if role != "leaf":
                issues.append({"severity": "warning", "id": fid, "code": "atomic_role",
                               "message": "atomic node should use knowledge_role: leaf"})
        elif granularity == "branch" and not kids and level != "L1":
            issues.append({"severity": "warning", "id": fid, "code": "branch_without_children",
                           "message": "branch has no children yet"})

        if role == "leaf" and kids:
            issues.append({"severity": "error", "id": fid, "code": "leaf_has_children",
                           "message": "leaf role cannot have children"})

        if parent is None and level != "L1":
            issues.append({"severity": "error", "id": fid, "code": "non_l1_root",
                           "message": "only L1 may have null parent"})

        # Capability / leaf directly under L1
        if parent and parent in features and features[parent].get("level") == "L1":
            if role == "leaf" or granularity == "atomic":
                issues.append({"severity": "error", "id": fid, "code": "capability_under_l1",
                               "message": "atomic/leaf must not hang directly under L1"})

        name_zh = ((feature.get("name") or {}).get("zh") or "")
        if BRAND_RE.search(name_zh) or BRAND_RE.search(((feature.get("name") or {}).get("en") or "")):
            issues.append({"severity": "warning", "id": fid, "code": "brand_name",
                           "message": f"platform/brand name in title: {name_zh}"})

        bindings = feature.get("bindings") or {}
        if (role == "leaf" or granularity == "atomic") and not any(bindings.get(p) for p in ("android", "ios", "harmonyos")):
            issues.append({"severity": "warning", "id": fid, "code": "missing_bindings",
                           "message": "atomic/leaf has no platform bindings"})

        if "sibling_axis" not in feature and parent and len(children.get(parent, [])) > 1:
            issues.append({"severity": "warning", "id": fid, "code": "missing_sibling_axis",
                           "message": "sibling_axis recommended when multiple siblings exist"})

    # Sibling axis consistency and fan-out
    parents = {feature.get("parent") for feature in selected.values() if feature.get("parent")}
    for parent in parents:
        kids = [features[kid] for kid in children.get(parent, []) if kid in selected]
        if len(kids) == 1 and features.get(parent, {}).get("level") != "L1":
            issues.append({"severity": "warning", "id": parent, "code": "single_child_branch",
                           "message": f"only one child: {kids[0]['id']}"})
        if len(kids) >= 12:
            issues.append({"severity": "warning", "id": parent, "code": "wide_branch",
                           "message": f"{len(kids)} siblings under one parent"})
        axes = {kid.get("sibling_axis") for kid in kids}
        axes.discard(None)
        axes.discard("")
        if len(axes) > 1:
            issues.append({"severity": "error", "id": parent, "code": "sibling_axis_conflict",
                           "message": f"conflicting sibling_axis values: {sorted(axes)}"})
        if len(kids) > 1 and not axes:
            issues.append({"severity": "warning", "id": parent, "code": "sibling_axis_absent",
                           "message": "siblings lack sibling_axis"})

    # Duplicate normalized names across selected set
    by_name: dict[str, list[str]] = defaultdict(list)
    for fid, feature in selected.items():
        name = ((feature.get("name") or {}).get("zh") or "").strip()
        if name:
            by_name[name].append(fid)
    for name, ids in by_name.items():
        if len(ids) > 1:
            issues.append({"severity": "warning", "id": ids[0], "code": "duplicate_name",
                           "message": f"duplicate zh name '{name}': {ids}"})

    # Legacy coverage for selected old ids that fall in domain prefix
    covered: set[str] = set()
    for feature in features.values():
        fid = feature["id"]
        if fid in old_ids:
            covered.add(fid)
        legacy = feature.get("legacy") or {}
        for source in legacy.get("sources") or []:
            if source in old_ids:
                covered.add(source)
    relevant_old = {
        oid for oid in old_ids
        if domain is None or oid == domain or oid.startswith(domain + ".")
    }
    for oid in sorted(relevant_old - covered):
        issues.append({"severity": "warning", "id": oid, "code": "legacy_unmapped",
                       "message": "historical id has no legacy disposition in current tree"})

    return issues


def load_old_ids(repo: Repository) -> set[str]:
    # Prefer archived snapshot of previous taxonomy if present; else current ids as baseline.
    archive_tax = ROOT / "archive/2026-09-06-inventory-first"
    # Current repo taxonomy before rebuild still is the 212-node set until rewritten.
    return set(repo.features())


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain")
    parser.add_argument("--json-out", type=str, default="output/reports/tree-lint.json")
    parser.add_argument("--md-out", type=str, default="output/reports/tree-lint.md")
    args = parser.parse_args(argv)

    repo = Repository()
    features = repo.features()
    old_ids = load_old_ids(repo)
    issues = lint_features(features, old_ids, args.domain)
    errors = [item for item in issues if item["severity"] == "error"]
    warnings = [item for item in issues if item["severity"] == "warning"]

    report = {
        "domain": args.domain,
        "feature_count": len(features),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "issues": issues,
    }
    write_json(ROOT / args.json_out, report)

    lines = [
        "# Tree lint",
        "",
        f"- features: {len(features)}",
        f"- errors: {len(errors)}",
        f"- warnings: {len(warnings)}",
        "",
    ]
    for item in issues:
        lines.append(f"- **{item['severity']}** `{item['code']}` `{item['id']}`: {item['message']}")
    write_text(ROOT / args.md_out, "\n".join(lines) + "\n")

    print(f"errors={len(errors)} warnings={len(warnings)} -> {args.json_out}")
    for item in errors[:20]:
        print(f"ERROR {item['code']} {item['id']}: {item['message']}")
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
