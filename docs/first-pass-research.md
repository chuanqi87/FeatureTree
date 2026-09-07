# 一天内的全量首次粗分析

> 历史已停止流程：inventory-first / first-pass 批次已归档。当前树设计见 [tree-design.md](tree-design.md)。下文保留解释旧批次，不是当前任务授权；prepare/run 需显式 `--existing-nodes-only`，不能恢复已停止批次。

2026-09-06 曾将用户的“一天内全量粗分析”错误收窄为现有特性树调查，下面记录该历史实现，不再将此范围归因于用户的最终目标。此通道与正式研究分开，不能把赶进度当作编造事实或 confirmed 的理由。

## 范围与产物

一节点一包，共覆盖现有 212 节点（106 叶子、106 父级）。每包输出三平台文档初判、实际读到的适用条件、最多三条差异假设、逐条官方正文引用、具体缺口、真机需求分类、后续精研优先级。不填写全部 24 个比较槽，不设计详细真机用例，不生成确定性平台优劣排名。

本轮的“全量”是节点首次调查覆盖，不是 5,088 个知识项精审，更不代表三个完整 SDK 的全部能力。先执行叶子；叶子尝试全部结束后执行父级，父级只研究自己的范围，不把一处机制推广到全部后代。

最新正式版、手机优先仍是最终目标；当前未完成启动日基线核实，所有首轮结论置信度保持 low，明确记录文档实际版本与待核缺口，不声称已经确认最新手机版本支持。`evidence_strength` 的 direct/indirect/missing 只表示作者判断的文档证据关系，供选题，不替代 high/medium 置信度。

`signal` 的 documented_mechanism 表示读到了相关机制，possible_mapping 表示可能对应，unknown 表示未能建立判断。它们不是正式 supported/unsupported 状态。没有证据不得写不支持、独有、完全等价。每个平台的非 unknown 信号要有本平台来源；差异假设要有所有比较平台的来源。不够相关时写具体未知，允许没有差异假设。

## 执行与预算

模型固定 `volcengine/glm-5.3`，通过已安装 Agent Bridge launcher 派发，不改 provider 配置和全局默认模型。先 4 路冒烟，至少 3 份通过机器交付检查后升 8 路；小范围不足四项时按实际项数。冒烟是运行/结构检查，不是五类正式生产试点，也不代表语义通过。

每节点最多两篇/平台、共六篇已冻结官方正文；从 context 的直接绑定及候选选择。候选与建议行段只是导航，必须阅读相关正文和必要上下文。本轮不广泛联网补查；资料不足进入缺口队列。每个工作者仍运行 context，使用自己的 `--output <任务目录>/context`，不会争写全局候选汇总。不得改公共资料库、正式 knowledge、taxonomy、校验规则、其他任务或自行调用其他代理。

软预算六分钟；运行池在约十五分钟任务时限或批次截止时请求取消，存在轮询与CLI响应延迟，不是 provider 硬计费上限。每节点最多一次模型调用，作者可以在同次调用内修一次自己的格式错误。失败保留日志和产物，不自动重复研究或换模型。发起结果不确定时停止新增派发，先核对实际 job，避免重复付费。

运行池有单实例锁，保存 job_id、session、执行状态、实际耗时、失败与机器检查；重启时跟踪已知在途任务，不重新发起。来源和规则随包固定，运行中不要改研究规则/基线/正式知识；变化后停止新增派发，不借旧输入确认新结论。机器休眠、网络/额度不足会影响一天目标，实际截止仍需监控，不能承诺后台永远可用。

## 检查与验收

机器全检：节点/平台覆盖、JSON 字段、来源行号与原文哈希、引用平台、缺口与评级、输出大小和输入未变。自动检查不证明内容解释正确。协调者对跨领域样本、差异假设和明显风险项做内容抽查；抽查记录单独保存，未抽查结果不能伪标“已独立复核”。本轮不要求对全部知识项逐条做七项独立精审。

真机只记录 required / recommended / not_required / unassessed 与理由，不写执行结果。正式采纳时仍需补充精细用例、固定基线、完整证据与原有七项独立验收；本通道不改变 `bulk_analysis_ready` 或 `production_accepted`。

执行统计区分 pending、running、delivered、delivered_partial、failed、launch_uncertain。delivered 只表示机器交付合格；partial 表示取得合规文件但执行被取消或后端未正常完成。所有节点保留在总表中，失败和未运行不算已分析完成。允许在截止时交付完整范围清单及实际取得的初判，但必须明确完成率和缺失节点。

## 命令与查看

先执行 `scripts/preflight.py --rebuild-contexts` 确认研究输入可用；正式基线/精审门槛可继续为 false，这只允许本隔离通道，不允许正式全量采纳。

```bash
.venv/bin/python scripts/research_first_pass.py prepare --model volcengine/glm-5.3 --deadline <带时区的实际截止时间>
.venv/bin/python scripts/research_first_pass.py run output/research/first-pass/<run_id>/manifest.json --launcher <已安装Agent-Bridge技能launcher绝对路径> --background
.venv/bin/python scripts/research_first_pass.py status output/research/first-pass/<run_id>/manifest.json
.venv/bin/python scripts/research_first_pass.py report output/research/first-pass/<run_id>/manifest.json
```

全部产物隔离在 `output/research/first-pass/<run_id>/`：`report.md` 为全树总表，`index.json` 为可筛选数据，`reports/<feature_id>/report.md` 为节点报告；对应 normalized.json 含官方 URL、获取时间、SHA 和精确摘录。`state.json`、任务 checks 与执行日志保留实际状态。无需等待全批结束即可查看已完成节点；正式知识浏览器的数据不自动混入这些初判。
