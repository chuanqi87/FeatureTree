"""Verify taxonomy binding URLs/symbols against the local official corpus."""

from __future__ import annotations
import argparse
import sys
from pathlib import Path
from featuretree.core.storage import ROOT, Repository, read_yaml, write_json, write_text, write_yaml
from featuretree.corpus.anchors import CorpusIndex, verify_feature


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain")
    parser.add_argument("--write", action="store_true", help="Write anchor_status back into taxonomy YAML")
    parser.add_argument("--json-out", default="output/reports/anchor-verification.json")
    parser.add_argument("--md-out", default="output/reports/anchor-verification.md")
    args = parser.parse_args(argv)

    db = ROOT / "docs-raw/official/corpus.sqlite"
    if not db.is_file():
        print(f"Corpus missing: {db}", file=sys.stderr)
        return 2
    corpus = CorpusIndex(db)
    repo = Repository()
    features = repo.features()

    results = []
    updates_by_file: dict[Path, list] = {}
    for feature in features.values():
        fid = feature["id"]
        if args.domain and not (fid == args.domain or fid.startswith(args.domain + ".")):
            continue
        status, details = verify_feature(feature, corpus)
        results.append({"id": fid, "anchor_status": status, "bindings": details})
        if args.write:
            domain = fid.split(".", 1)[0]
            path = ROOT / "taxonomy" / f"{domain}.yaml"
            updates_by_file.setdefault(path, []).append((fid, status))

    if args.write:
        for path, updates in updates_by_file.items():
            if not path.is_file():
                continue
            doc = read_yaml(path)
            by_id = {item["id"]: item for item in doc.get("features", [])}
            for fid, status in updates:
                if fid in by_id:
                    by_id[fid]["anchor_status"] = status
            write_yaml(path, doc)

    counts = {}
    for item in results:
        counts[item["anchor_status"]] = counts.get(item["anchor_status"], 0) + 1
    write_json(ROOT / args.json_out, {"counts": counts, "results": results})

    lines = ["# Anchor verification", "", f"counts: {counts}", ""]
    failed = [item for item in results if item["anchor_status"] == "failed"]
    lines.append(f"## Failed ({len(failed)})")
    for item in failed[:200]:
        lines.append(f"- `{item['id']}`")
        for detail in item["bindings"]:
            if detail["status"] == "failed":
                lines.append(f"  - {detail['platform']}: {detail.get('reason')}")
    write_text(ROOT / args.md_out, "\n".join(lines) + "\n")
    print(f"verified={len(results)} counts={counts} -> {args.json_out}")
    return 0
