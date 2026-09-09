"""Export current authored domain definitions as compact design inputs."""

from __future__ import annotations
import argparse
import sys
from pathlib import Path
from featuretree.core.storage import ROOT, Repository, write_json
from featuretree.reporting.design import export_domain


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain", help="Single L1 domain id")
    parser.add_argument("--all", action="store_true", help="Export every L1 domain")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "output/reports/design-inputs",
    )
    args = parser.parse_args(argv)
    if not args.domain and not args.all:
        parser.error("Provide --domain or --all")

    repo = Repository()
    registry = repo.root / "taxonomy/_index.yaml"
    from featuretree.core.storage import read_yaml

    domains = [item["id"] for item in read_yaml(registry)["domains"]]
    selected = domains if args.all else [args.domain]
    for missing in selected:
        if missing not in domains:
            print(f"Unknown domain: {missing}", file=sys.stderr)
            return 2

    args.out_dir.mkdir(parents=True, exist_ok=True)
    summary = []
    for domain in selected:
        payload = export_domain(repo, domain)
        target = args.out_dir / f"{domain}.json"
        write_json(target, payload)
        summary.append({
            "domain": domain,
            "path": str(target),
            "authored_count": payload["authored_count"],
        })
        print(f"{domain}: authored={payload['authored_count']} -> {target}")
    write_json(args.out_dir / "index.json", {"domains": summary})
    return 0
