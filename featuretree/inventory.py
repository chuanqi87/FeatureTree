"""Inventory scope decisions and non-destructive catalog refresh helpers."""

import hashlib
import re


def classify_scope(row):
    native = row["native_id"].lower()
    title = row["title"]
    if "-sys.md" in native or "系统接口" in title or row["visibility"] in ("system", "hidden"):
        return "excluded", "系统或隐藏接口不属于公开应用 SDK 范围", "system"
    if re.match(r"^(java|javax|kotlin|dalvik|org\.xmlpull)\.", native):
        return "excluded", "纯语言/基础库不纳入本期平台能力目录", row["visibility"]
    if (re.search(r"(^|\.)test(s)?(\.|$)", native) or "testing" in native
            or native.startswith("apis-test-kit") or native == "storekittest"):
        return "excluded", "测试专用目录不纳入本期范围", row["visibility"]
    if row["visibility"] == "duplicate":
        return "pending", "旧 duplicate 标记混合了范围判断，需复核", "public"
    if row["platform"] == "ios":
        return "pending", "Apple 文档目录需要逐项确认 iOS 适用性", row["visibility"]
    return "included", "公开应用目录候选；具体 API 可见性与版本仍需逐项核实", row["visibility"]


def source_for(row, root):
    platform = row["platform"]
    native = row["native_id"]
    if platform == "android":
        path = "docs-raw/maps/android-guide-sitemap.txt" if row["kind"] == "guide" else "docs-raw/android/packages-index.md"
        distribution = "Android documentation"
    elif platform == "ios":
        path = "docs-raw/ios/framework-roots.txt"
        distribution = "Apple documentation catalog (platform applicability unverified)"
    else:
        kit = native if row["kind"] == "kit" else row.get("parent")
        path = f"docs-raw/harmonyos/api-index/kits/{kit}-Readme-CN.md"
        distribution = "OpenHarmony (not yet verified against HarmonyOS SDK)"
    return {"local_path": path, "sha256": hashlib.sha256((root / path).read_bytes()).hexdigest(),
            "distribution": distribution, "version_pinned": False}


def prepare_row(row, root, previous=None):
    result = dict(row)
    result.pop("feature_id", None)
    result["schema_version"] = 2
    result["source"] = source_for(row, root)
    result["version"] = "unversioned local documentation snapshot; see source.sha256"
    result["layer"] = "unknown"
    scope, reason, visibility = classify_scope(row)
    if row["platform"] == "ios" and scope == "pending":
        page = root / "docs-raw/ios/frameworks" / (row["native_id"].lower() + ".md")
        if page.is_file() and re.search(r"\biOS \d", "\n".join(page.read_text().splitlines()[:40])):
            scope, reason = "included", "本地落地页声明 iOS 适用；具体版本与能力仍待核实"
    result.update(scope=scope, scope_reason=reason, visibility=visibility, scope_method="rule")
    result["mappings"] = list((previous or {}).get("mappings", []))
    if previous and previous.get("scope_method") == "manual":
        for field in ("scope", "scope_reason", "scope_method", "visibility"):
            result[field] = previous[field]
    return result


def inventory_coverage(rows):
    counts = {"total": len(rows), "included": 0, "excluded": 0, "pending_scope": 0,
              "candidate_catalog": 0, "candidate_capability": 0,
              "confirmed_capability": 0, "unmapped_included": 0}
    for row in rows:
        counts["pending_scope" if row["scope"] == "pending" else row["scope"]] += 1
        if row["scope"] != "included":
            continue
        mappings = row["mappings"]
        if not mappings:
            counts["unmapped_included"] += 1
        if any(m["relationship"] == "catalog" and m["verification"] == "candidate" for m in mappings):
            counts["candidate_catalog"] += 1
        if any(m["relationship"] == "capability" and m["verification"] == "candidate" for m in mappings):
            counts["candidate_capability"] += 1
        if any(m["relationship"] == "capability" and m["verification"] == "confirmed" for m in mappings):
            counts["confirmed_capability"] += 1
    return counts
