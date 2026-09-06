# 标准任务交接单

目标：交付指定知识项的证据调查与缺口，不确认整节点支持。
阶段：evidence；模型：volcengine/glm-5.3。

节点：app.background.foreground_task；定义：向用户明示的长时后台工作（如下载、导航）。
本次只处理：support:android、support:harmonyos、support:ios
不做：未选知识项与其他节点；正式知识合并及全量放行；人工真机执行

输入：任务包固定输入指纹、来源和版本状态；先阅读 AGENTS.md、docs/official-documentation-entrypoints.md、docs/sources.md、docs/official-corpus.md、docs/knowledge-confidence.md、docs/research-acceptance.md
交付：仅手工编辑本目录的 worker-report.md
预算：{'max_bodies': 6, 'max_fetches': 3, 'soft_minutes': 5, 'max_attempts': 1, 'hard_provider_cost_cap': False}。时长为软限制，不是 provider 硬计费上限。

## 验收标准

| 编号 | 验收项 | 通过条件 |
| --- | --- | --- |
| scope | 范围与覆盖 | 逐项回答所选问题；未选范围不扩写、不计完成，缺口明确归属。 |
| evidence | 逐条证据覆盖 | 每条实质性陈述和限定条件有直接相关的正文定位；引用存在不等于覆盖完整。 |
| applicability | 版本与适用条件 | 区分系统/SDK/target/库、发行版、正式/预览、手机/其他形态；未固定处保留未知。 |
| interpretation | 解释与推论 | 区分官方明示和分析，保留 can/must、主体、例外；不得由未命中推断不支持、独有或等价。 |
| confidence | 置信度与缺口 | 评级有依据，未知有具体缺口；高可信不等于已实测，缺文档不能一概推给真机。 |
| device_plan | 真机判断与用例 | 不需实测时限定静态判断；需要时前提合法、样本明确、步骤可执行，文档预期与待观察项分开。 |
| integrity | 交付与诚实性 | 不改规则、正式知识或别人的文件；无伪造来源/实测，未完成与失败如实报告。 |

机器检查通过后才进入独立内容复核；作者不能以自评代替验收。
所有所选项都须逐条核对。允许有明确证据缺口的未知，不允许漏查、猜测或无证据肯定。
内容验收通过也不自动 confirmed、合并 knowledge 或放行全量。

## 不合格处理

按失败知识项返回：问题位置、原因、修改要求、再次通过所需证据。
默认不自动重跑；协调者批准后最多返工一轮，保留原始交付与旧验收。输入变化必须重新派发。
未知机型/版本先标待选，无法证明的运行表现列待观察；不得预写 pass 或保证结果。
