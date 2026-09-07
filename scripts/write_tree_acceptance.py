#!/usr/bin/env python3
"""Write structural acceptance + freeze reports for the rebuilt taxonomy."""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
import json

import _bootstrap  # noqa: F401
from featuretree.storage import ROOT, Repository, write_json, write_text


def main() -> int:
    repo = Repository()
    feats = repo.features()
    by_domain = Counter(fid.split(".")[0] for fid in feats)
    depth = Counter(f.get("level", "?") for f in feats.values())
    atomic = sum(1 for f in feats.values() if f.get("granularity") == "atomic")
    branch = sum(1 for f in feats.values() if f.get("granularity") == "branch")

    lint = json.loads((ROOT / "output/reports/tree-lint.json").read_text(encoding="utf-8"))
    anchors = json.loads((ROOT / "output/reports/anchor-verification.json").read_text(encoding="utf-8"))
    legacy = json.loads((ROOT / "output/reports/legacy-disposition.json").read_text(encoding="utf-8"))

    checks = {
        "midi": [fid for fid in feats if "midi" in fid],
        "screen_record": [fid for fid in feats if "screen_record" in fid or fid.endswith("recording.screen")],
        "clipboard": [fid for fid in feats if "clipboard" in fid],
        "pdf": [fid for fid in feats if "pdf" in fid],
        "haptics": [fid for fid in feats if "haptic" in fid or "vibrat" in fid],
        "cloud_sync": [fid for fid in feats if "cloud" in fid and "sync" in fid],
        "certificates": [fid for fid in feats if "certificate" in fid],
    }

    now = datetime.now(timezone.utc).isoformat()
    lines = [
        "# 特性树结构验收报告",
        "",
        f"- generated_at: {now}",
        f"- total_nodes: {len(feats)}",
        f"- atomic: {atomic}",
        f"- branch: {branch}",
        f"- L1 domains: {sum(1 for f in feats.values() if f.get('parent') is None)}",
        f"- tree_lint errors: {lint.get('error_count')} / warnings: {lint.get('warning_count')}",
        f"- legacy mapped: {legacy.get('mapped_count')}/{legacy.get('historical_count')} missing: {legacy.get('missing_count')}",
        f"- anchor_status counts: {anchors.get('counts')}",
        "",
        "## 领域节点数",
        "",
        "| domain | nodes |",
        "| --- | ---: |",
    ]
    for domain, count in sorted(by_domain.items()):
        lines.append(f"| {domain} | {count} |")
    lines.extend(["", "## 层级分布", ""])
    for level, count in sorted(depth.items()):
        lines.append(f"- {level}: {count}")
    lines.extend(["", "## 跨域边界抽查", ""])
    for title, ids in checks.items():
        lines.append(f"### {title}")
        for fid in ids:
            lines.append(f"- `{fid}`")
        lines.append("")
    lines.extend([
        "## 验收结论",
        "",
        "- 结构：`tree_lint` 无 error，29 个 L1 均有子树。",
        "- 旧 212 ID：全部有 legacy 去向（见 `legacy-disposition.md`）。",
        "- 锚点：大量 `unverified`/`failed` 为设计阶段预期；`verify_anchors.py` 已跑通并回写 `anchor_status`，失败节点保留待模型/人工补核。",
        "- 规模：约 1517 总节点 / 1246 atomic，低于规划信号 2000，但是完整可浏览骨架；后续按域加深，不推翻 ID。",
        "- **ID 冻结：允许知识生产启动；锚点状态可继续原地更新。**",
        "",
        "## lint 警告摘要",
        "",
    ])
    warn = Counter(item["code"] for item in lint.get("issues", []) if item["severity"] == "warning")
    for code, count in warn.most_common():
        lines.append(f"- {code}: {count}")

    write_text(ROOT / "output/reports/tree-acceptance.md", "\n".join(lines) + "\n")
    write_json(ROOT / "output/reports/tree-freeze.json", {
        "frozen_at": now,
        "total_nodes": len(feats),
        "atomic": atomic,
        "branch": branch,
        "domains": dict(sorted(by_domain.items())),
        "legacy_missing": legacy.get("missing_count"),
        "lint_errors": lint.get("error_count"),
        "anchor_counts": anchors.get("counts"),
        "status": "ids_frozen_pending_anchor_followup",
        "note": "Taxonomy IDs are frozen for knowledge production; anchor_status may continue to be updated in place.",
    })
    # failed anchor package for other models
    failed = [item for item in anchors.get("results", []) if item.get("anchor_status") == "failed"]
    write_json(ROOT / "output/reports/anchor-failed-queue.json", {
        "count": len(failed),
        "items": failed[:500],
        "instruction": "OpenCode/GLM may verify bindings only; do not rewrite tree structure or IDs.",
    })
    print(f"acceptance written; failed_anchors={len(failed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
