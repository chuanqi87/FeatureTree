# 标准派发与独立验收

所有新 evidence、candidate、probe 任务统一生成 `handoff.md`，同一契约嵌入任务包 `handoff` 并参与任务 ID。交接单由程序生成，不能由执行者自行改范围、预算或降低标准。历史任务包保留为历史记录，不倒填新规则或冒充新验收。

用户明确授权的一天内 first_pass 粗分析采用 [单独的交接与抽查契约](first-pass-research.md)，不要求全部项逐条独立精审。它不会标记本节七项验收通过，也不能直接合并正式知识。

## 派发前固定什么

每单固定目标、阶段、单节点及精确知识项/问题、排除范围、模型、输入与版本状态、输出文件、调查预算、通过条件和停止/返工方式。协调者补齐具体问题及相关原文，不将“全面分析一下”作为可验收任务。优先拆成 1–3 个明确问题或 3–5 个已研究知识项；共享上下文变化时先检查会影响哪些未选项。

| 阶段 | 输出 | 自动检查实际能证明什么 |
| --- | --- | --- |
| evidence | worker-report.md | 输入未变化、报告非空；不能证明报告完整或结论正确 |
| candidate | candidate.yaml、worker-report.md | 候选结构、引用及版本契约、所选范围保护符合规则；不能证明解释正确 |
| probe | response.json | 问题覆盖、引用行段/原文哈希一致、评级和计划字段合规；不能证明引用支持每句话 |

具体模型沿用用户指定的 `volcengine/glm-5.3`，不得静默替换。单节点仅一个作者；每次调用一次尝试，超预算保留产物并交付缺口。时长与 token 使用量不是硬计费上限，不可观测的账单明确写未知。

## 七项逐条验收

验收记录必须覆盖“每个所选 target_id × 以下七项”，每项填写通过/失败、理由及具体定位。未完成的复核保留 pending，不计通过。不用整体平均分抵消任何实质性问题。

| 编号 | 检查内容 | 典型不合格情况 |
| --- | --- | --- |
| scope | 范围、问题覆盖、未知归属 | 漏题、扩写其他节点，或把三道问题计作整节点完成 |
| evidence | 每条实质性陈述及限定条件都有相关官方正文定位 | 引用真实存在，但只覆盖主句，遗漏例外或限制 |
| applicability | 系统/SDK/target/库、发行版、版本渠道和手机范围 | 用 introduced 版本当最新正式版，混用 OpenHarmony/HarmonyOS |
| interpretation | 官方明示与推论分开，保留原文主体及 can/must | 把“可以”改成“必须”；由任务停止推出音频一定停止 |
| confidence | 评级理由、未知与具体缺口，独立标注真机需求 | 有官方链接就标 high；文档缺口一律转为真机测试 |
| device_plan | 合法前提、机型/构建、可执行步骤、预期与观察项 | 缺调用前提；把待验证行为写成文档保证或已测通过 |
| integrity | 写入边界、来源真实性、失败与未完成如实记录 | 修改规则过关、伪造读取/实测、隐瞒重试或合并正式知识 |

“调查完成但未知”可以通过本次交付验收，前提是实际调查有记录，缺什么、影响哪条判断、下一步如何补查说清楚。它仍然是 unknown，不成为 confirmed 事实或确定性洞察。没有有效启动日基线时仍只允许诊断，不能通过验收绕过基线规则。

静态文档判断可以无需真机；涉及运行表现时，计划分别说明文档保证了什么、哪些现象只是待观察，覆盖必要权限、配置、API/SDK 条件和触发环境。尚未选定机型/构建应明确待选，不能把未执行计划记为 pass。

## 收回后的执行方式

先让作者运行包对应的 `research_tasks.py check` 或 `research_probe.py check` 自查并停止。协调者核对交付和执行日志，记录真实的作者 session/job 与独立复核者身份，再初始化验收单：

```bash
.venv/bin/python scripts/research_acceptance.py init output/research/tasks/<task_id>/task.json --author-id <实际作者session或job> --reviewer-id <实际独立复核者>
# probe 使用 output/research/probes/<probe_id>/probe.json，其余相同
.venv/bin/python scripts/research_acceptance.py check output/research/tasks/<task_id>/task.json output/research/acceptance/<review_id>/review.json
```

`init` 先重跑机器检查；交付缺失、不合规或任务过期均拒绝初始化。成功后保存任务包与原始交付的精确快照，并生成全 pending 的验收单。重复初始化不覆盖已有复核。作者不得填写独立验收记录；不能把作者自检当成独立评审，也不能通过换一个身份字符串冒充独立评审。

复核者读取正文并逐条填写 `checks`：`target_id`、`criterion_id`、`status`、`explanation`、`evidence_refs`。定位应具体到产物 JSON 字段/报告小节，以及正文路径与行号/章节；范围与诚实性检查可引用任务包和执行日志。涉及版本或真机材料时引用对应证据。`reviewed_at` 填实际带时区复核时间。

总体 `decision` 为 pending / pass / revise / blocked。`check` 校验完整矩阵、输入和产物哈希、身份字段、复核时间、问题明细；只有全部项 pass 且没有 open 问题时 `content_accepted` 才为 true、退出码才为 0，其余为 2。每次检查保存当时的完整复核文本和结果，避免后续编辑抹去失败记录。

这是复核记录校验器，不是自动语义裁判。程序不能仅凭身份字符串证明独立性，也不能仅凭文字理由证明实际读过原文或引用支持结论；这些责任仍由实际独立复核者承担。哈希保证版本一致，不保证知识真实。`content_accepted` 只表示该范围的提交通过所记录的复核。

## 不合格如何退回

每条失败标准至少对应一个 open issue，必填：`id`、`target_id`、`criterion_id`、`status`、`problem`、`location`、`required_change`、`expected_evidence`。不能只写“再完善一下”。例如：定位到某条结论的 conditions 字段，指出限定条件缺引用；要求补入直接支持该限定的章节或删去未证实断言，并以修订后的逐句引用映射验收。

默认不自动重试。协调者批准后最多返工一轮，只修明确失败项，保留原始交付与原复核；仍失败则缩小范围或明确阻塞，不能自动扩大检索/换模型。答案发生变化必须重新 `init`：新产物哈希对应新 review_id，原来的通过记录不能沿用。节点、基线、来源或规则变化则先重新准备任务包，再研究和复核。

任务完成、机器通过、内容验收通过、正式知识采纳、人工真机通过是不同状态。此工具不合并 knowledge，不升级 confirmed，不执行真机，也不替代 `pilot-review.json` 与 `preflight --require-ready` 的启动门槛。生产采纳仍按 [研究运行手册](research-runbook.md) 独立核实。
