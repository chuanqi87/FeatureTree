# OpenCode 节点研究交接契约

执行器使用任务包中明确指定的 provider/model；本轮试点为 `volcengine/glm-5.3`，不得静默换模型。任务包只分配一个节点，一个节点同一时间只允许一个作者。任务包不是已确认知识，也不是扩大范围的授权。

## 定向原文回归（probe）

`scripts/research_probe.py prepare <spec.yaml> --model <provider/model>` 可准备最多三个明确问题的诊断包。协调者先执行 context、选择相关原文完整段落，程序核验候选有效性并固定来源、行号、问题、模型和输入指纹；不会提供上轮答案。题目不覆盖整节点，不能计作全节点研究完成。

此模式只手工提交包内 `response.json`，遵循包内 response_schema；引用仅填来源 ID、章节和行段，程序回填精确原文、URL、获取时间和 SHA。无需作者填完整知识 YAML、复制长哈希或阅读校验代码。最多五分钟软预算、一次调用，不自动重跑。文档缺失写具体缺口，当前模式始终 low，不自行确认版本或实测。必需阅读的仓库规则仍适用，不因缩小上下文省略证据要求。

`scripts/research_probe.py check <probe.json>` 拦截错题/漏题、越界来源/行号、空引用、过度评级、伪实测字段和变更后的输入。`response_contract_valid` 只证明答案结构和来源一致，不能证明文字解释正确；规范化结果保存在按内容哈希区分的 checks 文件，不覆盖历史。该模式不生成 candidate.yaml、不合并 knowledge、不改变全量启动门槛。解释通过后，仍需进入既有 candidate 与独立复核流程。

## 输入与写入边界

先看任务阶段：命令行默认 `stage: evidence`，先提交不超过 1200 中文字的 worker-report.md：每平台一条带 URL、正文章节、路径、SHA、获取时间的文档观察；两个具体差异候选或反例；缺口与真机计划。最多 6 篇正文、3 次按需抓取、约 5 分钟。此阶段不写 candidate.yaml、不填 24 个槽位、不研究校验实现代码。报告落盘通过仅表示交付存在，仍需证据与语义复核。

证据报告复核后才以 `--stage candidate` 准备结构化候选。允许 `--claim` 指定单节点内的精确知识项，未选中的陈述、上下文和引用不得受改动影响；需要调整共享上下文时先明确依赖范围。未指定知识项为全节点选择，可新增关键 facts。一次结构化任务优先限制为 3–5 个已研究项，复杂结论单独做。下面的完整 YAML 要求仅适用于 candidate 阶段。

两阶段都不会自动放行正式知识。软时长不是 provider 硬计费上限；超时由协调者取消。取消后的日志、输入与使用量保留，不把失败重跑伪装成首次成功。

来源元数据由 `.venv/bin/python scripts/export_research_sources.py <官方URL...>` 从资料库验哈希后导出；也可 `--notes <报告路径>` 提取证据表。返回的 source-indexes 清单关联随 Git 保存的精选原文与原始响应。不手抄长哈希、不缩写本地路径。此命令只验证快照，不生成章节摘录或适用性判断；这两项仍需作者阅读、协调者复核。

特别核对 can/must、编译 SDK/target SDK/系统版本、单接口/整个模块的区别。报告不得把预览 SDK 放入正式版主比较或主测试计划，不得从语言框架的传输抽象推断系统缺少其他框架。手机之外的用例单独列附录；模拟器结果不能计入人工真机完成。

先完整阅读 AGENTS.md、docs/official-documentation-entrypoints.md、docs/sources.md、docs/official-corpus.md、docs/knowledge-confidence.md、docs/comparison-model.md。再阅读任务包、目标 taxonomy 节点和原 knowledge。

必须执行 `.venv/bin/python scripts/official_docs.py context <feature_id>`，检查 binding_source_gaps，并读取相关官方正文。检索片段、目录、历史文章均不能替代证据。可以使用 official_docs.py 的 search / locate / fetch / read 按需补查；不启动整库 crawl。新增正文由资料库保存原始响应与哈希。

仅允许手工编辑任务包指定的 candidate.yaml 和 worker-report.md；不编辑正式 knowledge、taxonomy、Schema、公共基线、汇总输出或别人的任务文件，不提交 Git，不调用其他模型或代理。上下文、按需抓取缓存、来源导出命令生成的精选快照和元数据属于允许的工具副作用，不是额外知识写入权；已有知识项不得删除。

候选 YAML 从原 knowledge 的完整结构开始，保留历史字段。只研究任务包指定的节点和知识项；为每个平台支持项和全部指定比较槽位逐项记录结论、证据、评级与真机需求。关键新增事实使用 facts。不要用脚本批量套用同一句缺口/结论；每个维度必须有具体调查说明。

## 版本与置信度

以启动日最新正式版、手机为主。任务包的 baseline_errors 非空时，本次为诊断试点，不能产生 confirmed 或中/高可信记录，不能把推测的最新版本写成已固定基线。可报告已读到的官方契约及具体待核实条件；没有完成当前版本论证的支持/差异维持 unknown，评级 low，并明确 missing_requirements。

有有效基线时，context 必须与其系统、SDK、发行版、设备形态一致；生态库另在 conditions 固定。所有来源需准确摘录、章节/符号、官方 URL、适用性、获取时间和本地 SHA-256。OpenHarmony 不能代替 HarmonyOS。不支持、独有、等价须额外核查，找不到不等于不存在。

assessment 的哈希用仓库函数计算，不能编造。每条记录明确 high / medium / low / unassessed；真机需求独立为 required / recommended / not_required。真实运行行为需要可执行用例，静态文档缺口先补文档，不能全部推给用户买设备。没有人工实测材料绝不写 results/pass。

## 交付与停止条件

worker-report.md 记录：实际研究范围；逐平台读过的正文 URL、章节与快照路径；发现的边界问题；关键差异候选和反例；仍需官方检索的缺口；真机计划；命令校验结果。模型、时间和费用如不可观测就写不可观测，不估算账单。解释为何不应扩大某条结论。

候选完成后运行 `.venv/bin/python scripts/research_tasks.py check <task.json>`。失败时只修自己文件，不改规则以通过。任务即使因网络/模型失败也保留已生成产物，向协调者报告阻塞；不无限重试。协调者独立复核后才能并入正式知识。

每节点最多读取 15 份正文、补抓 6 个 URL；每次正文读取按相关章节控制上下文，必要时继续读取直到覆盖论证所需内容。达到此试点调查预算后记录缺口并交付，不能把预算耗尽伪装成研究完成。此预算只是任务指令，不是 provider 的硬计费上限；运行超时由协调者取消，失败不自动重启。
