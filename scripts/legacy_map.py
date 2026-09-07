#!/usr/bin/env python3
"""Map disposition of the historical 212 feature ids onto the current taxonomy."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import _bootstrap  # noqa: F401
from featuretree.storage import ROOT, Repository, write_json, write_text


HISTORY_SNAPSHOT = (
    ROOT / "archive/2026-09-06-inventory-first/output/reports"
)


def historical_ids(repo: Repository) -> set[str]:
    """Use baseline snapshot file if present; otherwise treat current tree as the historical set.

    During rebuild, callers should pass --history-ids from a frozen list.
    """
    frozen = ROOT / "output/reports/historical-212-ids.txt"
    if frozen.is_file():
        return {line.strip() for line in frozen.read_text(encoding="utf-8").splitlines() if line.strip()}
    return set(repo.features())


def collect_coverage(features: dict) -> dict[str, list[dict]]:
    coverage: dict[str, list[dict]] = {}
    for feature in features.values():
        fid = feature["id"]
        legacy = feature.get("legacy") or {}
        disposition = legacy.get("disposition")
        sources = list(legacy.get("sources") or [])
        if disposition == "kept" and not sources:
            sources = [fid]
        if disposition == "new" and not sources:
            continue
        for source in sources or ([fid] if disposition == "kept" else []):
            coverage.setdefault(source, []).append({
                "current_id": fid,
                "disposition": disposition or ("kept" if source == fid else "unspecified"),
            })
        # Also count unchanged ids present in the new tree without explicit legacy.
        if fid not in (legacy.get("sources") or []) and disposition in (None, "kept"):
            coverage.setdefault(fid, []).append({
                "current_id": fid,
                "disposition": disposition or "present",
            })
    return coverage


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history-ids", type=Path, help="Text file with one historical id per line")
    parser.add_argument("--json-out", default="output/reports/legacy-disposition.json")
    parser.add_argument("--md-out", default="output/reports/legacy-disposition.md")
    args = parser.parse_args(argv)

    repo = Repository()
    features = repo.features()
    if args.history_ids:
        old_ids = {line.strip() for line in args.history_ids.read_text(encoding="utf-8").splitlines() if line.strip()}
    else:
        old_ids = historical_ids(repo)

    coverage = collect_coverage(features)
    mapped = sorted(oid for oid in old_ids if oid in coverage)
    missing = sorted(old_ids - set(coverage))
    payload = {
        "historical_count": len(old_ids),
        "mapped_count": len(mapped),
        "missing_count": len(missing),
        "missing": missing,
        "mapped": {oid: coverage[oid] for oid in mapped},
    }
    write_json(ROOT / args.json_out, payload)

    lines = [
        "# Legacy disposition",
        "",
        f"- historical ids: {len(old_ids)}",
        f"- mapped: {len(mapped)}",
        f"- missing: {len(missing)}",
        "",
        "## Missing",
        "",
    ]
    for oid in missing:
        lines.append(f"- `{oid}`")
    lines.extend(["", "## Mapped (sample)", ""])
    for oid in mapped[:100]:
        refs = ", ".join(f"{item['current_id']}({item['disposition']})" for item in coverage[oid])
        lines.append(f"- `{oid}` → {refs}")
    write_text(ROOT / args.md_out, "\n".join(lines) + "\n")
    print(f"mapped={len(mapped)} missing={len(missing)} -> {args.md_out}")
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
