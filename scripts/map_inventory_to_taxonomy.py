#!/usr/bin/env python3
"""FeatureTree command entry point. See README.md for the authoring workflow."""

from _bootstrap import ROOT
import json
from featuretree.inventory import inventory_coverage
from featuretree.mapping import map_row
from featuretree.storage import Repository, read_yaml, write_json

if __name__ == "__main__":
    repo = Repository()
    features = repo.features()
    rules = read_yaml(repo.root / "config/mapping-rules.yaml")["rules"]
    summary = {}
    for platform in repo.config()["platforms"]:
        path = repo.root / f"inventory/{platform}/catalog.json"
        rows = [map_row(row, features, rules) for row in json.loads(path.read_text())]
        write_json(path, rows)
        write_json(repo.root / f"inventory/unmapped/{platform}.json",
                   [r for r in rows if r["scope"] != "excluded" and not any(
                       m["relationship"] == "capability" and m["verification"] == "confirmed" for m in r["mappings"])])
        summary[platform] = inventory_coverage(rows)
    write_json(repo.root / "inventory/mapping_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
