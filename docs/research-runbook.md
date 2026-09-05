# 全量研究与洞察的启动契约

本轮采用用户确定的范围：**启动日各平台最新正式版，先比较手机；其他设备形态单独注明**。策略保存在 `config/research.yaml`。旧知识的 baseline 是历史说明，不能充当本轮版本依据。

## 启动检查

```bash
# 重新准备全部候选、校验使用到的原文与原始响应、生成研究清单
.venv/bin/python scripts/preflight.py --rebuild-contexts

# 基线和试点完成后，检查是否可以放大全量执行；条件未满足返回 2
.venv/bin/python scripts/preflight.py --require-ready
```

`output/reports/readiness.json` 保存逐节点输入指纹、源码路径、候选来源缺口、范围检查任务和全部维度 × 平台对。Markdown 报告在同目录。每组输入另存到 `output/research/runs/<run_id>/manifest.json`；旧清单保留。改变节点、绑定、研究策略、原文快照、知识内容或运行基线会改变输入指纹，不能沿用旧试点复核记录。

- `research_inputs_ready`：结构、策略和候选文件可用，可以开始检索、版本核实与试点。
- `bulk_analysis_ready`：另已通过启动日基线与试点复核，可以扩大全量研究。其他节点仍需要逐条核实。
- `research_complete`：所选研究结论已完成确认，独立于前两项。

未找到平台候选或绑定正文会进入具体节点的补查任务；这些缺口不是“不支持”的证据，也不会因存在通用搜索候选而被抹去。预检查不调用模型，不自动生产事实或完成语义评审。

## 先固定运行基线

沿 [官方入口](official-documentation-entrypoints.md) 检索和读取发布说明、SDK 说明，核对启动日已经正式发布的系统与 SDK，排除预览版。各来源正文、获取时间与 SHA-256 必须保存；不能从文档获取时间、API 的 introduced 版本或本机开发工具版本推断最新系统版本。

配置中的 `official_release_entrypoints` 是本次发现的检索起点，不表示已经确认这些页面对应启动日的最新正式版。需要继续跟进后续发布、补丁与 SDK 配套关系。华为新版发布资料还包括 `doccenter-release-notes` 路径，旧的两棵指南/API 目录不能代替版本资料。

将基线写入 `output/research/baseline.json`，结构如下。使用真实核实结果填写，不预填猜测版本。

| 字段 | 要求 |
| --- | --- |
| `run_date` | 实际启动日期，`YYYY-MM-DD`；`preflight --run-date` 可复查指定轮次 |
| `policy_hash` | `featuretree.research_profile.fingerprint(research_policy(repo))` |
| `platforms` | 与 `config/comparison.yaml` 平台集合一致 |
| 每个平台的 `context` | release、sdk、distribution、device_forms；这里 sdk 表示该轮系统 SDK，手机为 `["phone"]` |
| `release_channel` | `stable` |
| `latest_stable_rationale` | 说明官方发布依据如何证明是启动日最新正式版，及已核对的预览/正式版本区别 |
| `verified_by`、`verified_at` | 实际复核者和启动日期 |
| `evidence` | 与 knowledge 证据相同的完整记录，必须包含官方正文摘录和适用性依据 |

基线校验同时检查已有 confirmed 记录的系统、SDK、发行版及设备范围，防止混入旧轮次结果。AndroidX、Google/Firebase、HMS 等组件版本与运行依赖另在节点 `context.conditions` 中固定，并与引用的 `evidence.applies_to` 保持一致。

## 先做代表性试点，再扩大全量

默认试点覆盖 BLE 过滤、前台/后台任务、运行时权限、声明式 UI，以及分布式通信。这些节点分别暴露细粒度条件、系统版本变化、隐私限制、编程模型和发行版/设备范围问题。

每个试点先执行 `official_docs.py context <feature_id>`，按节点研究全部平台和比较维度。允许调查后保留 unknown，但必须逐条填写 `rationale` 和具体的 `missing_requirements`；不允许为了通过门槛写成 supported、same 或 not_applicable。已得出结论的项需要完成证据核实。

完成后先运行 `preflight.py` 取得当前节点 `input_hash`，再将实际复核记录写入 `output/research/pilot-review.json`：以 feature_id 为键，每项含 `input_hash`、`verified_by`、`verified_at`（运行日期）、`scope_review`、`evidence_review`（具体复核说明）。最后执行 `preflight.py --require-ready`。

按清单先处理叶子，再处理父级汇总节点；父节点需要阅读子节点研究结果，但必须独立核实自身范围。每个工作单元只编辑它对应的 knowledge 文件；范围有变化时同步 taxonomy 并重建上下文。工作完成后运行 `refresh.py`，使用当前输入重新检查，不以旧成功报告代替验收。

## 事实与洞察的边界

每条平台支持、事实和比较按 [知识置信度与人工真机复核](knowledge-confidence.md) 写 assessment；试点中调查后仍 unknown 的项也要明确评级依据和真机需求。高/中/低可信与必须/建议/无需真机独立记录。使用导出的复核清单限制本轮知识项及预算，不隐式扩大执行范围。

新增关键平台事实记录到 `facts`，包含 id、platform、dimension、statement、basis、verification 和 evidence_refs。`basis` 区分 `official_statement` 与 `evidence_based_analysis`。确认字段及证据契约见 [比较模型](comparison-model.md)。原有说明正文需重新核实，文章 reviewed 不代表其每句话已确认。

洞察只能引用通过当前校验的 confirmed 事实或比较，并保留其证据、版本和设备条件。试点接受的 unknown 仍计为 unknown。对“不支持”“相同”“不适用”填写 `coverage_note`，说明具体检查范围和替代路径；搜索未命中和目录缺项不能支撑这些结论。

叶子与父节点汇总分开计数，显式给出 unknown 分母和未覆盖范围。当前树与 inventory 均不能证明覆盖三个完整 SDK；目录未映射项和范围待定项进入发现任务，不能省略后声称平台完全覆盖或某能力独有。201 个尚未填写 excludes 的节点在本次清单中要求复核边界；不能通过机械填充排除项代替语义审查。

## 更新后的确认校验

洞察同时列出置信度、来源知识项和真机状态；新推论需独立复核，不得高于最弱关键前提。研究 confirmed 不等于真机通过。真机完成只覆盖计划中的机型、构建和条件，不能推及所有设备。

审计、视图导出和浏览器均校验确认记录的来源、正文摘录、哈希、适用上下文及节点指纹。无效记录不能继续作为已确认结果导出或展示。自动检查只能证明契约和快照一致，不能证明作者的解释正确；仍需实际阅读与复核。

候选包检查配置和绑定变更、来源更新、原文哈希和摘录行号。iOS 候选排除元数据明确仅适用于其他 Apple 平台的页面；适用性为空仍保留未知。Android 候选排除路径明确属于 iOS/Web 等目标的生态服务页面；通用跨平台页面仍需阅读判断。相同正文不会重复占用通用搜索名额。

Google/Firebase 路径明确属于 iOS 的资料进入 iOS 候选，不能因提供方属于 Google 而划为 Android 能力。官网标为 AI 生成的 Page Summary 从检索正文中排除；原始响应和旧的规范化文件保留供追溯，历史摘要不能成为本轮语义证据。
