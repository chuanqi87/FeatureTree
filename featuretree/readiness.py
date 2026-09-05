"""Preflight and reproducible work plans; preparation never confirms platform facts."""

import argparse
from collections import Counter
from datetime import date
import hashlib
import json

from .audit import audit
from .comparison import comparison_slots, subject_hash
from .context_checks import context_errors, read_context
from .corpus.context import build_contexts, context_input_hash
from .corpus.store import Corpus, now
from .paths import CONTEXTS_DIR, REPORTS_DIR
from .pilot_review import pilot_errors
from .research_profile import fingerprint, policy_errors, research_policy
from .research_contract import methodology_hash
from .storage import ROOT, Repository, write_json, write_text


def assess(repo, corpus, contexts, run_date):
    features = repo.features()
    knowledge, paths = repo.knowledge()
    config = repo.config()
    policy = research_policy(repo)
    method_hash = methodology_hash(repo.root)
    integrity = audit(repo)
    errors = list(integrity["errors"]) + policy_errors(policy)
    rows, verified_files = [], {}
    baseline_path = repo.root / "output/research/baseline.json"
    baseline_hash = hashlib.sha256(baseline_path.read_bytes()).hexdigest() if baseline_path.exists() else None
    pilots = set(policy.get("pilot_features", []))
    errors.extend(f"Unknown pilot feature: {fid}" for fid in pilots - features.keys())
    for fid, feature in sorted(features.items()):
        bundle = {}
        try:
            bundle = read_context(contexts, fid)
            failures = context_errors(bundle, feature, config, policy, corpus, verified_files)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            failures = [str(exc)]
        errors.extend(f"{fid}: {error}" for error in failures)
        platforms = bundle.get("platforms", {}) if isinstance(bundle, dict) else {}
        if not isinstance(platforms, dict):
            platforms = {}
        platforms = {p: value for p, value in platforms.items()
                     if isinstance(value, dict) and isinstance(value.get("documents"), list)}
        gaps = {p: value.get("binding_source_gaps", []) for p, value in platforms.items()}
        missing = [p for p in config["platforms"] if not platforms.get(p, {}).get("documents")]
        checks = ["read_official_bodies", "verify_release_sdk_device_applicability", "review_deprecation_and_service_retirement",
                  "record_traceable_facts", "review_all_comparison_dimensions", "grade_each_claim_confidence",
                  "assess_physical_device_review_and_write_reproducible_cases"]
        if missing or any(gaps.values()):
            checks.insert(0, "retrieve_missing_binding_or_platform_sources")
        if not feature["comparison_scope"]["excludes"]:
            checks.insert(0, "review_scope_boundaries")
        if feature["knowledge_role"] == "rollup":
            checks.append("review_aggregate_scope_without_inheriting_child_conclusions")
        if knowledge.get(fid, {}).get("status") != "stub":
            checks.append("recheck_historical_prose_against_current_sources")
        knowledge_hash = hashlib.sha256((repo.root / paths[fid]).read_bytes()).hexdigest()
        source_manifest = sorted((p, *(str(source.get(key, "")) for key in ("url", "raw_sha256", "body_sha256", "fetched_at")))
                                 for p, data in platforms.items() for source in data.get("documents", []) if isinstance(source, dict))
        inputs = {"context_input_hash": context_input_hash(feature, config, policy),
                  "source_manifest_hash": fingerprint(source_manifest), "baseline_sha256": baseline_hash,
                  "knowledge_sha256": knowledge_hash, "methodology_sha256": method_hash, "run_date": run_date}
        rows.append({"feature_id": fid, "role": feature["knowledge_role"],
                     "subject_hash": subject_hash(feature), "input_hash": fingerprint(inputs), **inputs,
                     "knowledge_path": paths[fid], "context_path": str(contexts / (fid + ".json")),
                     "pilot": fid in pilots,
                     "children_to_review": sorted(f["id"] for f in features.values() if f["parent"] == fid),
                     "related_features_to_review": feature.get("related_features", []),
                     "candidate_document_counts": {p: len(v.get("documents", [])) for p, v in platforms.items()},
                     "binding_source_gaps": gaps, "missing_platform_candidates": missing,
                     "preparation_errors": failures, "research_steps": checks,
                     "comparison_slots": [{"dimension": d, "platforms": pair} for d, pair in comparison_slots(feature, config["platforms"])]})
    rows.sort(key=lambda r: (r["role"] == "rollup", not r["pilot"], -int(features[r["feature_id"]]["level"][1:]), r["feature_id"]))
    # The baseline belongs to a particular launch date, never to the historical prose.
    baseline_task = {"task": "resolve_run_baseline", "run_date": run_date, "policy": policy,
                     "required_output": "output/research/baseline.json",
                     "official_entrypoints": policy.get("official_release_entrypoints", {}),
                     "requirements": ["official stable release and SDK for every platform",
                                      "official release sources, excerpts, fetch times and hashes",
                                      "phone applicability; other devices in separate findings",
                                      "pin AndroidX, Google/HMS service versions for each affected node"]}
    from .run_baseline import baseline_errors
    baseline_failures = baseline_errors(repo, config, policy, run_date)
    pilot_failures, pilot_pending = pilot_errors(repo, rows, knowledge, features, config, run_date)
    production_blockers = list(errors) + baseline_failures + pilot_failures
    source_gap_count = sum(len(gap) for row in rows for gap in row["binding_source_gaps"].values())
    run_id = fingerprint({"run_date": run_date, "policy": policy, "inputs": [row["input_hash"] for row in rows]})
    return {"generated_at": now(), "run_id": run_id, "run_date": run_date, "policy": policy,
            "research_inputs_ready": not errors, "bulk_analysis_ready": not production_blockers,
            "research_complete": integrity.get("research_complete", False),
            "input_errors": errors, "production_blockers": production_blockers,
            "counts": {"features": len(features), "roles": dict(Counter(f["knowledge_role"] for f in features.values())),
                       "verified_candidate_snapshots": len(verified_files), "binding_source_gaps": source_gap_count,
                       "nodes_missing_platform_candidates": sum(bool(row["missing_platform_candidates"]) for row in rows),
                       "scope_boundaries_to_review": sum(not f["comparison_scope"]["excludes"] for f in features.values())},
            "inventory": integrity.get("inventory", {}), "confirmation_progress": integrity.get("progress", {}),
            "knowledge_quality": integrity.get("quality", {}),
            "quality_by_role": integrity.get("quality_by_role", {}),
            "device_review_complete": integrity.get("device_review_complete", False),
            "pilot_pending": pilot_pending, "baseline_task": baseline_task, "nodes": rows,
            "insight_rules": ["Use validated confirmed facts and comparisons only",
                              "Carry confidence, device-review state and source claim IDs into every insight; never promote weakest inputs",
                              "High documentary confidence is not physical-device verification; sample passes do not cover all devices",
                              "Honor the exported review scope and budget; report omitted claims separately",
                              "Always report unknown counts and the applicable baseline",
                              "Do not combine leaf and rollup nodes into an exclusive capability count",
                              "Parent/child and related nodes are review context, not inherited evidence",
                              "Directory gaps and missing documents never imply unsupported"]}


def markdown(report):
    c = report["counts"]
    lines = ["# 全量分析启动检查", "", f"检查时间：{report['generated_at']}；运行日期：{report['run_date']}。", "",
             f"研究输入可用：{report['research_inputs_ready']}。全量分析放行：{report['bulk_analysis_ready']}。",
             "", "范围：启动日最新正式版，手机优先；其他形态单独记录。", "",
             f"节点 {c['features']}：{c['roles']}；候选原文及原始响应校验 {c['verified_candidate_snapshots']} 份。",
             f"绑定资料缺口 {c['binding_source_gaps']} 条；缺少平台候选的节点 {c['nodes_missing_platform_candidates']} 个。",
             f"尚需审查排除边界的节点 {c['scope_boundaries_to_review']} 个。", "", "## 尚未满足的全量启动条件", ""]
    lines += [f"- {error}" for error in report["production_blockers"]] or ["- 无。"]
    lines += ["", "逐节点缺口、研究步骤、平台对及输入指纹见 readiness.json。", "",
              "启动顺序：固定官方版本基线 → 完成五个高风险试点 → 叶子研究 → 父节点范围复核 → 按有效证据汇总洞察。",
              "候选、目录映射、历史正文和哈希通过均不代表事实已经核实。", ""]
    lines += ["## 目录与范围的剩余缺口", "", "| 平台 | 范围待定 | 已纳入但未映射 |", "| --- | ---: | ---: |"]
    lines += [f"| {p} | {counts['pending_scope']} | {counts['unmapped_included']} |" for p, counts in report["inventory"].items()]
    lines += ["", "这些目录统计不等于 SDK 全覆盖，需在发现阶段继续处理；叶子与父级汇总应分别计数。", ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rebuild-contexts", action="store_true")
    parser.add_argument("--require-ready", action="store_true", help="Exit 2 until baseline and pilot review pass")
    parser.add_argument("--run-date", default=date.today().isoformat())
    args = parser.parse_args(argv)
    date.fromisoformat(args.run_date)
    repo = Repository()
    corpus_path = ROOT / "docs-raw/official"
    if not (corpus_path / "corpus.sqlite").exists():
        parser.error("Official corpus is missing; follow docs/official-corpus.md")
    corpus = Corpus(corpus_path)
    try:
        if args.rebuild_contexts:
            print("Rebuilding candidate contexts; this does not confirm claims.", flush=True)
            build_contexts(corpus, repo, ROOT / CONTEXTS_DIR, limit=5)
        report = assess(repo, corpus, ROOT / CONTEXTS_DIR, args.run_date)
    finally:
        corpus.close()
    output = ROOT / REPORTS_DIR
    write_json(output / "readiness.json", report)
    write_text(output / "readiness.md", markdown(report))
    manifest = ROOT / "output/research/runs" / report["run_id"] / "manifest.json"
    if not manifest.exists():
        write_json(manifest, report)
    print(json.dumps({key: report[key] for key in ("research_inputs_ready", "bulk_analysis_ready", "counts", "production_blockers")}, ensure_ascii=False))
    return 1 if report["input_errors"] else 2 if args.require_ready and not report["bulk_analysis_ready"] else 0
