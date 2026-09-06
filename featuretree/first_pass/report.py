"""Readable preliminary outputs with complete attempted/failed/unstarted denominators."""

from collections import Counter
from datetime import datetime, timezone

from ..storage import contained_path, read_yaml, write_json, write_text


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def node_report(feature, response):
    lines = [f"# {feature['name']['zh']} — 首轮初判", "",
             "低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。", "",
             response["summary"], "", "## 三平台初判", "",
             "| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |",
             "| --- | --- | --- | --- | --- |"]
    for row in response["platforms"]:
        lines.append("| " + " | ".join(cell(v) for v in (row["platform"], row["signal"], row["evidence_strength"],
                                                       row["observation"], row["device_review"]["requirement"])) + " |")
    for row in response["platforms"]:
        lines += ["", f"## {row['platform']} 条件与证据", "", "适用范围：" + row["version_scope"],
                  "条件：" + "；".join(row["conditions"]), "缺口：" + "；".join(row["gaps"]),
                  "真机分类理由：" + row["device_review"]["reason"], ""]
        for citation in row["citations"]:
            source = citation["source"]
            lines.append(f"- [{cell(source['title'])}]({source['url']})，{cell(citation['locator'])}，"
                         f"正文 {citation['start_line']}–{citation['end_line']} 行；获取 {source['fetched_at']}；SHA {source['sha256']}。")
    lines += ["", "## 待验证差异假设", ""]
    for row in response["difference_hypotheses"]:
        lines += [f"- {row['dimension']}：{row['statement']}；待核：{'；'.join(row['open_questions'])}。"]
    if not response["difference_hypotheses"]:
        lines.append("没有形成满足双方引用要求的差异假设；不代表没有差异。")
    lines += ["", "范围缺口：" + "；".join(response["scope_gaps"]), "",
              f"后续优先级：{response['followup_priority']['level']}；{response['followup_priority']['reason']}",
              "", "逐条引用及原文摘录见同目录 normalized.json。", ""]
    return "\n".join(lines)


def write_report(repo, manifest_path, manifest, state):
    directory = manifest_path.parent
    features = repo.features()
    rows = []
    for item in manifest["tasks"]:
        fid = item["feature_id"]
        execution = state["nodes"][fid]
        row = {"feature_id": fid, "name": features[fid]["name"]["zh"], "role": item["role"],
               "status": execution["status"], "job_id": execution.get("job_id"),
               "error": execution.get("error"), "semantic_review_passed": False, "production_accepted": False}
        if execution.get("check", {}).get("delivery_valid"):
            path = contained_path(directory, execution["check"]["check_path"], ".").parent / "normalized.json"
            response = read_yaml(path)
            report_dir = directory / "reports" / fid
            write_json(report_dir / "normalized.json", response)
            write_text(report_dir / "report.md", node_report(features[fid], response))
            row.update(summary=response["summary"], platforms=response["platforms"],
                       difference_hypotheses=response["difference_hypotheses"], scope_gaps=response["scope_gaps"],
                       followup_priority=response["followup_priority"], report=f"reports/{fid}/report.md")
        rows.append(row)
    counts = dict(Counter(row["status"] for row in rows))
    result = {"run_id": manifest["run_id"], "generated_at": datetime.now(timezone.utc).isoformat(),
              "stage": "first_pass", "state": state["status"], "deadline": manifest["deadline"],
              "counts": counts, "total_nodes": len(rows), "roles": dict(Counter(r["role"] for r in rows)),
              "production_accepted": False, "semantic_review_passed": False,
              "notice": "Preliminary observations only; coverage is nodes, not all 5088 claims. Unknown/failed/unstarted remain explicit.",
              "rows": rows}
    write_json(directory / "index.json", result)
    lines = ["# 全量首轮粗分析", "", "**初判资料，不是已确认知识；没有人工真机实测。**", "",
             f"目标 {len(rows)} 节点；当前 {counts}。叶子和父级范围草图分开计数：{result['roles']}。",
             f"状态：{state['status']}；截止：{manifest['deadline']}。",
             "此处的全量是现有节点的首次调查覆盖，不是全部知识项精审，也不是三个完整SDK的覆盖证明。", "",
             "所有正式置信度为 low；direct/indirect/missing 只是文档证据强弱，不能当 high/medium 使用。",
             "父级仅初判自身范围，不自动继承或证明子节点的支持情况。失败和未运行项不会伪填研究结论。", "",
             "| 节点 | 角色 | 执行状态 | 精研优先级 | 初步摘要 |", "| --- | --- | --- | --- | --- |"]
    for row in rows:
        name = f"[{cell(row['name'])}]({row['report']})" if row.get("report") else cell(row["name"])
        lines.append(f"| {name} | {row['role']} | {row['status']} | {row.get('followup_priority', {}).get('level', '未评估')} | "
                     f"{cell(row.get('summary', row.get('error') or '尚未取得合格初判'))} |")
    lines += ["", "来源、版本限制、差异假设、真机需求和具体缺口见各节点报告及 index.json。",
              "后续内容抽查单独记录，自动检查通过不代表抽查通过；费用不可观测，不以reported_cost=0宣称免费。", ""]
    write_text(directory / "report.md", "\n".join(lines))
    return {k: v for k, v in result.items() if k != "rows"}
