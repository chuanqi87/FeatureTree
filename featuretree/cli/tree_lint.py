#!/usr/bin/env python3
"""Structural lint for authored taxonomy trees."""

from __future__ import annotations

import argparse

from featuretree.core.storage import ROOT, Repository, write_json, write_text
from featuretree.taxonomy.structure import lint_features


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain")
    parser.add_argument("--json-out", type=str, default="output/reports/tree-lint.json")
    parser.add_argument("--md-out", type=str, default="output/reports/tree-lint.md")
    args = parser.parse_args(argv)

    repo = Repository()
    features = repo.features()
    issues = lint_features(features, set(), args.domain)
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
