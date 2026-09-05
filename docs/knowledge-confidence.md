# 知识置信度与人工真机复核

评级对象是每一条 presence、facts、comparisons，不是整篇文章或平台优劣。它是依据证据、版本适用性和未解决问题作出的定性判断，不是统计校准后的正确概率；不填写未经校准的 90%、95%。

## 两条独立的判断轴

| 置信度 | 采用标准 | 使用方式 |
| --- | --- | --- |
| 高可信 high | 结论已 confirmed；官方正文、适用版本/设备、来源和节点指纹已核实；无未解决的证据缺口或实测冲突。分析还需说明推导过程和替代解释。 | 可注明条件后引用；仍须查看真机需求，不能宣称已经实测。 |
| 中可信 medium | 已读取可追溯官方正文且版本/上下文匹配，但条件解释、跨平台映射或推论仍需复核。 | 带限制的参考；未 confirmed 不进入确定性洞察。 |
| 低可信 low | 关键条件或证据有缺口、冲突，或实测不符/无法判断；明确写出缺口。 | 调查线索与风险提示。证据不足时支持/差异继续 unknown。 |
| 未评估 unassessed | 尚未评级、未形成结论或缺少比较项。 | 先研究或评估，不等于不支持或无需真机。 |

| 真机需求 | 采用标准 | 必须记录 |
| --- | --- | --- |
| 必须复核 required | 问题依赖真实运行观测，例如实际时序、精度、后台存活、设备差异，或需复现冲突。这是研究方法分类，不预断任何平台行为。 | 原因、各涉及平台的样本、条件、操作步骤、预期结果。 |
| 建议抽样 recommended | 文档判断较充分，但落地条件可能有实现差异，值得按业务重要性抽查。 | 同样提供可执行用例，选有代表性的环境。 |
| 无需真机 not_required | 当前这条陈述是官方可明确核实的静态契约，回答它不依赖运行观测。 | 解释为何文档足以回答；不表示该能力无需产品测试。 |

缺少 assessment 时两轴均显示未评估。高可信也可能必须真机复核：文档契约明确，但项目仍需验证目标设备行为。一次样本通过不会自动提高置信度；低可信可能应先补文档，而非立刻买设备。

## 选择本轮范围

特性树筛选栏支持领域、关键词、确认状态、置信度、真机需求、叶子/分支和“导出预算（知识项）”。“含高可信结论 + 必须真机复核”要求同一条结论同时满足，不能由同节点中两条不同记录拼成。

“导出复核清单”包含匹配知识项、原始文件、结论、两轴状态、评级理由、证据、上下文、缺口和用例。用于导航的祖先不进入清单；折叠节点不减少范围。预算以知识项数计，不是节点数或设备数；清单记录匹配总数、选择数和未选择数。

点击后先预览选择数量和完整 JSON，再下载或复制。若应用内浏览器未保存下载文件，复制入口仍可取出完整清单。输入完整节点 ID 会精确选择该节点，不连带选入引用它的父节点。

- 查阅结果：高可信 + 无需真机复核，或单独看“计划样本已通过”。引用仍需注明版本和设备条件。
- 人工测试：先看实测不符，再看必须待复核，最后按余量处理建议抽样。
- 新一轮研究：未评估 + 指定领域/叶子 + 本轮预算。必须复核清单为空不证明没有测试工作，可能只是尚未评估。

命令行支持任意子树 ID：

```bash
# 仅定义范围，不启动研究/测试；最多 20 条
.venv/bin/python scripts/export_review_scope.py --domain connectivity --role leaf --device-review required --limit 20

# 高可信且无需实测的结论
.venv/bin/python scripts/export_review_scope.py --confidence high --device-review not_required

# 未研究项目的小批次
.venv/bin/python scripts/export_review_scope.py --domain connectivity.bluetooth --role leaf --confidence unassessed --limit 10
```

结果在 `output/exports/review-scopes/<scope_hash>.json`，包含 feature_ids 和逐项 claim_id。相同筛选与输入得到同一哈希；输入改变另存新文件。后续执行者只生产选中的知识项；可阅读其他节点作背景，但不能把它们计为完成。preflight 仍检查全局输入与启动基线，不因小范围绕过证据要求。

排序：0 实测不符，1 必须待实测，2 建议待抽样，3 补证据/未评估，4 其他；同档按节点 ID、知识项 ID。它不是业务影响评分，也不是随机/统计代表性抽样。小预算可能集中同一节点，可按领域拆批；一项跨平台结论可能需要多台设备，实际成本查看 cases。

## 作者填写契约

Schema 在 `config/schema/confidence.schema.json`。旧草稿不强制补分；confirmed 必须填写有效且明确的评级，不能未评估。一般正文没有逐条结构化时不继承本节点评级。

assessment 必填：

- confidence、rationale：级别及证据充分性、推论、限制、不确定性的具体说明。
- assessed_by、assessed_at：实际评级者和日期；可以是研究代理，应如实标明。
- input_hash：`featuretree.confidence.assessment_input_hash(feature, doc, claim, platforms)`，覆盖本条记录、节点范围、涉及平台上下文、引用来源；其他字段填完后计算。
- device_review.requirement、reason：需求及理由。
- 必须/建议时 device_review.cases：唯一 id、platform、与 presence 一致的 context、device_model、os_build、conditions、steps、expected；至少覆盖本结论涉及的每个平台。机型/构建未确定可保留待选择计划，不能填写完成记录。

人工真机完成后才写 device_review.results：case_id、plan_hash（`featuretree.confidence.fingerprint(case)`）、claim_hash（当前 input_hash）、outcome（pass/fail/inconclusive）、observed、method（human_physical_device）、tested_by、tested_at（带时区）、artifact_path、sha256。材料位于 `output/research/device-reviews/`，包含可复查的日志、截图或测试报告。移除不必要的账号、设备唯一标识等个人信息，不捏造实测人和材料。

每个用例一条当前结果，历史复测保留在材料中。状态由结果推导，不能直接填写 passed：任一 fail 为实测不符；缺结果或 inconclusive 为待实测；全部计划用例 pass 才是“计划样本通过”。冲突/不确定结果需要降为低可信或未评估并说明范围，再调查解决。

修改结论、证据或版本会使旧评级失效；修改用例使旧结果失效。重新计算评级哈希也不能将旧实测自动归属新陈述。Schema、哈希和材料存在性仅验证一致性，不能证明人工真的测试过、样本具有代表性或评级解释正确，仍需负责人抽查。

## 洞察与统计

洞察保留来源 feature_id、claim_id、证据 URL/章节、基线和设备条件，并列置信度与真机状态。新的推论需独立复核，不得高于最弱关键前提；不能把低/中可信前提拼成高可信洞察。关键前提有待实测、不符、未评估时，洞察也要保留限制，不写已经验证。

节点展示逐项数量；缺失比较槽位在分母内，不取平均分掩盖缺口。汇总 level 保守取最弱档（有未评估则未评估）；筛选按“包含该档知识项”。父级不继承子节点评级，审计 quality_by_role 分开统计叶子和分支。

research_complete 是证据研究确认状态；device_review_complete 是所列计划的复核完成状态，两者独立。高可信、confirmed、输入就绪、自动测试通过均不自动证明真机工作完成，更不代表所有机型都已覆盖。
