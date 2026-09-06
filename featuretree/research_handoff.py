"""One dispatch contract shared by evidence, candidate and diagnostic tasks."""

from copy import deepcopy


CRITERIA = (
    ("scope", "范围与覆盖", "逐项回答所选问题；未选范围不扩写、不计完成，缺口明确归属。"),
    ("evidence", "逐条证据覆盖", "每条实质性陈述和限定条件有直接相关的正文定位；引用存在不等于覆盖完整。"),
    ("applicability", "版本与适用条件", "区分系统/SDK/target/库、发行版、正式/预览、手机/其他形态；未固定处保留未知。"),
    ("interpretation", "解释与推论", "区分官方明示和分析，保留 can/must、主体、例外；不得由未命中推断不支持、独有或等价。"),
    ("confidence", "置信度与缺口", "评级有依据，未知有具体缺口；高可信不等于已实测，缺文档不能一概推给真机。"),
    ("device_plan", "真机判断与用例", "不需实测时限定静态判断；需要时前提合法、样本明确、步骤可执行，文档预期与待观察项分开。"),
    ("integrity", "交付与诚实性", "不改规则、正式知识或别人的文件；无伪造来源/实测，未完成与失败如实报告。"),
)


def handoff_contract(stage, feature, model, targets, budget):
    goals = {"evidence": "交付指定知识项的证据调查与缺口，不确认整节点支持。",
             "candidate": "把已调查的指定知识项整理为可复核候选，不自行采纳正式知识。",
             "probe": "逐题解释指定官方原文，诊断解读质量，不视为完整节点研究。"}
    outputs = {"evidence": ["worker-report.md"], "candidate": ["candidate.yaml", "worker-report.md"],
               "probe": ["response.json"]}
    return {"schema_version": 1, "stage": stage, "objective": goals[stage], "executor_model": model,
            "scope": {"feature_id": feature["id"], "definition": feature["definition"],
                      "target_ids": list(targets), "comparison_scope": deepcopy(feature["comparison_scope"]),
                      "non_goals": ["未选知识项与其他节点", "正式知识合并及全量放行", "人工真机执行"]},
            "inputs": {"required_readings": ["AGENTS.md", "docs/official-documentation-entrypoints.md",
                       "docs/sources.md", "docs/official-corpus.md", "docs/knowledge-confidence.md",
                       "docs/research-acceptance.md"],
                       "knowledge": feature["knowledge_path"],
                       "context": f"output/contexts/{feature['id']}.json",
                       "version_baseline": "output/research/baseline.json",
                       "missing_baseline_action": "仅诊断、明确未知，不猜测最新版本；不放宽确认要求。"},
            "outputs": outputs[stage], "budget": deepcopy(budget),
            "criteria": [{"id": key, "name": name, "requirement": requirement}
                         for key, name, requirement in CRITERIA],
            "acceptance": {"machine_checks_required": True, "independent_review_required": True,
                           "coverage": "每个 target_id × 每个验收项都需记录复核结果与定位",
                           "pass_rule": "全部通过且无未解决质量问题；不使用平均分抵消实质性错误。",
                           "production_accepted": False},
            "revision_policy": {"automatic_retry": False, "max_revision_rounds": 1,
                                "coordinator_approval_required": True,
                                "scope": "仅修失败知识项；附问题、位置、修改要求和验收证据。",
                                "stop": "超时、缺权限或本轮无法补齐资料时保留产物并报告；不自动扩大调查或换模型。"}}


def render_handoff(contract):
    scope = contract["scope"]
    lines = ["# 标准任务交接单", "", f"目标：{contract['objective']}",
             f"阶段：{contract['stage']}；模型：{contract['executor_model']}。", "",
             f"节点：{scope['feature_id']}；定义：{scope['definition']}",
             "本次只处理：" + "、".join(scope["target_ids"]),
             "不做：" + "；".join(scope["non_goals"]), "",
             "输入：任务包固定输入指纹、来源和版本状态；先阅读 " + "、".join(contract["inputs"]["required_readings"]),
             "交付：仅手工编辑本目录的 " + "、".join(contract["outputs"]),
             f"预算：{contract['budget']}。时长为软限制，不是 provider 硬计费上限。", "",
             "## 验收标准", "", "| 编号 | 验收项 | 通过条件 |", "| --- | --- | --- |"]
    lines.extend(f"| {row['id']} | {row['name']} | {row['requirement']} |" for row in contract["criteria"])
    lines += ["", "机器检查通过后才进入独立内容复核；作者不能以自评代替验收。",
              "所有所选项都须逐条核对。允许有明确证据缺口的未知，不允许漏查、猜测或无证据肯定。",
              "内容验收通过也不自动 confirmed、合并 knowledge 或放行全量。", "",
              "## 不合格处理", "", "按失败知识项返回：问题位置、原因、修改要求、再次通过所需证据。",
              "默认不自动重跑；协调者批准后最多返工一轮，保留原始交付与旧验收。输入变化必须重新派发。",
              "未知机型/版本先标待选，无法证明的运行表现列待观察；不得预写 pass 或保证结果。", ""]
    return "\n".join(lines)
