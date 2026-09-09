"""Validate data integrity separately from research completion."""

import argparse
import json
import re
from collections import Counter

import yaml

from .bindings import build_index
from .comparison import progress
from .confidence import claim_rows, quality_summary
from .evidence import validate_knowledge_evidence
from .paths import EXPORTS_DIR, REPORTS_DIR
from .storage import Repository, contained_path, write_json, write_text
from .validation import schema_validators, validate_schemas, validate_tree


def audit(repo, domain=None, check_index=True):
    config = repo.config()
    if config.get("schema_version") != 2 or len(config.get("platforms", {})) < 2 or not config.get("dimensions"):
        raise ValueError("Comparison config needs schema_version=2, at least two platforms and nonempty dimensions")
    for identifier in [*config["platforms"], *config["dimensions"]]:
        if not re.fullmatch(r"[a-z][a-z0-9_]*", identifier):
            raise ValueError(f"Invalid comparison config id: {identifier}")
    features = repo.features()
    knowledge, paths = repo.knowledge()
    errors = validate_schemas(schema_validators(repo.root), features, knowledge)
    if errors:
        return {"integrity": "failed", "errors": errors, "research_complete": False}
    errors += validate_tree(features, knowledge, paths, config)
    for feature in features.values():
        contained_path(repo.root, feature["knowledge_path"], "knowledge")
        if set(feature.get("bindings", {})) - set(config["platforms"]):
            errors.append(f"Unknown binding platform: {feature['id']}")
    if not errors:
        errors += validate_knowledge_evidence(features, knowledge, config["platforms"], repo.root)
    if check_index:
        path = repo.root / EXPORTS_DIR / "index.json"
        if not path.exists() or json.loads(path.read_text()) != build_index(features):
            errors.append(f"Stale or incomplete {EXPORTS_DIR}/index.json; run scripts/refresh.py")
    selected = {fid: f for fid, f in features.items()
                if domain is None or fid == domain or fid.startswith(domain + ".")}
    if not selected:
        errors.append(f"No features selected: {domain}")
    queue = [{"feature_id": fid, **progress(f, knowledge.get(fid, {}), config["platforms"])}
             for fid, f in selected.items()]
    totals = {key: sum(q[key] for q in queue) for key in
              ("confirmed_support", "total_support", "confirmed_comparisons", "total_comparisons")}
    quality = [row for fid, feature in selected.items()
               for row in claim_rows(feature, knowledge[fid], config["platforms"])]
    return {"integrity": "failed" if errors else "passed", "errors": errors,
            "research_complete": not errors and bool(queue) and all(q["state"] == "complete" for q in queue),
            "selection": domain or "all", "feature_count": len(selected),
            "article_status": dict(Counter(knowledge[fid]["status"] for fid in selected if fid in knowledge)),
            "progress": totals,
            "tree_counts": {"domains": sum(f["parent"] is None for f in selected.values()),
                            "branches": sum(f["knowledge_role"] == "rollup" for f in selected.values()),
                            "atomic_leaves": sum(f["knowledge_role"] == "leaf" for f in selected.values())},
            "quality": quality_summary(quality),
            "quality_by_role": {role: quality_summary([r for r in quality if r["role"] == role]) for role in ("leaf", "rollup")},
            "device_review_complete": not errors and bool(quality) and all(r["device_state"] in ("not_required", "passed") for r in quality),
            "review_queue": [q for q in queue if q["state"] != "complete"]}


def report_markdown(report):
    if "progress" not in report:
        return "# 当前进度\n\n结构校验失败，请查看 audit.json。\n"
    p = report["progress"]
    lines = ["# 当前进度（自动生成）", "",
             f"结构校验：{report['integrity']}。差异确认完成：{'是' if report['research_complete'] else '否'}。",
             "", f"比较节点：{report['feature_count']}；文章编辑状态：{report['article_status']}。",
             f"领域：{report['tree_counts']['domains']}；分支：{report['tree_counts']['branches']}；能力叶子：{report['tree_counts']['atomic_leaves']}。",
             "", f"平台支持已确认：{p['confirmed_support']} / {p['total_support']}。",
             f"维度 × 平台对已确认：{p['confirmed_comparisons']} / {p['total_comparisons']}。", "",
             "旧文章 reviewed 状态不自动确认结构化结论。空白比较项表示待确认。", "",
             f"知识置信度（逐项）：{report['quality']['counts']}；真机复核状态：{report['quality']['device_states']}。",
             f"所列计划真机复核完成：{report['device_review_complete']}；不表示覆盖全部机型。",
             "叶子与分支的分级统计分别保存在 audit.json 的 quality_by_role。",
             "按置信度、实测需求和预算筛选：scripts/export_review_scope.py；逐项清单：../exports/review_queue.json。"]
    lines += ["", "领域入口与能力叶子分开统计；结构通过不代表树覆盖完整。",
              "", "待确认节点见 review_queue.json；逐项空缺见 ../exports/comparison_matrix.csv。", ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain", help="Only restrict research completion to this subtree; integrity remains global")
    parser.add_argument("--require-complete", action="store_true", help="Exit 2 when selected node comparisons remain unfinished")
    args = parser.parse_args(argv)
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


if __name__ == "__main__":
    raise SystemExit(main())
