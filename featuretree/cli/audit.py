"""Validate data integrity separately from research completion."""

import argparse
import json
import yaml
from featuretree.core.paths import REPORTS_DIR
from featuretree.core.storage import Repository, write_json, write_text
from featuretree.reporting.audit import audit, report_markdown


def parser(description=__doc__):
    result = argparse.ArgumentParser(description=description)
    result.add_argument("--domain", help="Only restrict research completion to this subtree; integrity remains global")
    result.add_argument("--require-complete", action="store_true", help="Exit 2 when selected node comparisons remain unfinished")
    return result


def run(args):
    repo = Repository()
    try:
        report = audit(repo, args.domain)
    except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError) as exc:
        report = {"integrity": "failed", "errors": [str(exc)], "research_complete": False}
    suffix = "" if not args.domain else "-" + args.domain.replace(".", "-")
    output = repo.root / REPORTS_DIR
    write_json(output / f"audit{suffix}.json", report)
    if not args.domain:
        write_json(output / "review_queue.json", report.get("review_queue", []))
        write_text(output / "progress.md", report_markdown(report))
    for error in report["errors"][:30]:
        print(error)
    print(f"Integrity: {report['integrity']}; research complete: {report['research_complete']}")
    if "progress" in report:
        print(json.dumps(report["progress"], ensure_ascii=False))
    if report["errors"]:
        return 1
    return 2 if args.require_complete and not report["research_complete"] else 0


def main(argv=None):
    return run(parser().parse_args(argv))
