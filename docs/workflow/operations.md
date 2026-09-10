# v2 操作与恢复

环境准备：

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
npm ci --prefix tools/sdk
npm ci --prefix tools/opencode --ignore-scripts
swift build -c release --package-path tools/sdk/swift
npm ci --prefix web
npm run build --prefix web
.venv/bin/python -m featuretree console serve --port 8765
```

模型执行需要用户已有的 OpenCode provider/model 配置；不把凭证写入工作单。所有命令支持全局 `--root`，必须放在命令组之前。复杂输入使用 `--request request.json`，相同操作重试保留 `--key`。`--expected none` 表示尚无正式版本，之后用完整 release_id 做乐观并发检查。

| 命令组 | 动作 |
|---|---|
| sources | import、extract、capture、seal、validate、query、report |
| workflow | plan、replan、run、resume、retry、revise、revalidate、supplement、cancel、report |
| taxonomy | check、diff、freeze、policies、approve-calibration |
| knowledge | plan、show、check、impact、import-observation |
| review | queue、show、decide、research |
| release | prepare、publish、rebase、show、compare、rollback、export |
| console | serve |

常用操作：

```sh
.venv/bin/python -m featuretree sources report
.venv/bin/python -m featuretree workflow plan --request run.json --key research-001 --expected none
.venv/bin/python -m featuretree workflow run --id RUN_ID
.venv/bin/python -m featuretree workflow report --id RUN_ID
.venv/bin/python -m featuretree taxonomy policies
.venv/bin/python -m featuretree taxonomy approve-calibration --request approval.json --key approval-001
.venv/bin/python -m featuretree taxonomy freeze --request freeze.json --key freeze-001
.venv/bin/python -m featuretree knowledge plan --request leaf-plan.json --key knowledge-001
.venv/bin/python -m featuretree release prepare --request release.json --key release-001
.venv/bin/python -m featuretree release publish --id release-001 --key commit-001
```

run.json 固定 pipeline（taxonomy/knowledge）、model、scopes。每个 scope 包含 definition、snapshot_id、selection、topic_selection、inputs、mode、work_type。selection 可以是 ids、platforms、modules、query 的明确组合；运行前枚举完整匹配集合，不以检索页数替代范围。enumeration_complete 默认 false，仅在范围已经闭合并可解释时显式设为 true。大于上下文预算时阻断并保留完整清单。

简化的 leaf-plan.json 为 `{"freeze_ref":"对象哈希","feature_ids":["稳定叶子ID"],"model":"provider/model"}`。校准样稿改用 tree_ref、bindings_ref、baseline_ref；系统按绑定生成叶子输入，不需要手写三端任务。

重试使用 `workflow retry --id RUN_ID --request action.json`，其中 action.json 含 task_id；语义修订使用 revise，并附 feedback 数组。revalidate 只重新校验保留的完整响应，验证原始文件哈希，保留原失败与路由调整历史，不执行新的模型研究。中断调用需显式重试，取消记录保留，不能误把外部复用 PID 当旧工作进程杀死。

来源补充使用 supplement，参数为 work_id，可附 source_requests。它从已提交交付件收集官方 URL，以新快照创建关联修订运行，默认最多两轮；不修改旧快照。没有 URL 或采集失败保留缺口。SDK 枚举缺失不会因补抓同一正文自动变为完整。

已有树的修订必须携带 scope_root_ids 和旧绑定。同一运行的结构范围不能祖孙重叠，跨域整合固定同一基础树。补来源时核对其他领域仍引用的声明、主题和正文；相关内容变化则要求把受影响领域纳入修订，未变化的领域保留绑定并记录 source-migration.json。

执行代码、Agent 或规则变化时使用 `workflow replan --id OLD_RUN --request replacement.json --key NEW_KEY`。replacement.json 包含 `fresh_stages`、`reason`，可显式给出新 `model`、`variant` 或 `budget`。兼容产物保留原作者与实际模型，用 reuse_ref 记录兼容检查；变化阶段及下游重新运行。新任务创建后用 run 启动。生产不能复用无执行指纹的开发阶段产物。

OpenCode CLI 和插件固定为 tools/opencode/package.json 的版本（当前 1.18.29）；版本漂移时停止。HTTP 402 表示账户余额不足，不能靠自动重试修复。恢复服务后重新计划，原始失败记录保留。不要把 retry 用于绕过已经变化的输入或执行器指纹。

模型默认采用文件交付：submit_payload 按字段路径分批写入当前 attempt/workspace/delivery，finish_payload 生成 completed.json。每批最多 24000 字符；数组按明确引用顺序合并，不能覆盖父子字段、重复引用或跨输入复用。完成文件通过结构校验后，执行器结束模型进程并读取文件，再做原有完整业务校验；普通聊天无需承载长 JSON。未完成的分批文件只作诊断材料，不是成功产物。

工作单 budget 中的 max_output_tokens（默认 32000）、max_agent_steps（默认 96）、max_delivery_chunks（默认 256）分别控制单次输出、模型步骤和交付分批数量。max_tool_calls 仍独立控制来源查询。输出预算通过 OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX 显式传给该次进程，服务商/模型自身上限仍可能更低；不会修改全局配置。有效 Agent 步数写入不可变计划。提高步数不会提高单次输出上限。

length 记录为 OutputLimitError，保留用量与预算且不原样自动重试。首响应超时与总执行超时仍分别保留并停止；调整预算或修复执行器后新建 replan。文件提交不依赖额外聊天回复；完成后不因等待聊天而浪费剩余超时预算。

三端建树研究（ft-android/ft-ios/ft-harmonyos）由执行器强制分批。source_batch_size 默认 32，指每次调用的 API 与主题合计上限，不是叶子粒度标准；API 按封存声明的 qualified_name 排序，让相近符号尽量同批。各批使用独立上下文、输入哈希、目录和原有平台研究契约，source_catalog 只允许枚举该批输入。batch_timeout_seconds 默认 900、batch_max_tool_calls 默认 8，分别限制每批执行时间和来源查询。阶段总耗时可能跨多个批次，不把全部批次压进一个模型调用。

通过校验的批次写入 run/batch-checkpoints；attempt/batch-progress.json 记录已校验、复用、当前批和失败原因，管理台阶段卡同步显示。全部批次提交后代码合并，重新验证完整输入守恒与证据；局部事实 ID 加平台和批次前缀以避免独立作者撞名，原始交付与映射关系由执行回执保留。中途失败不会产生阶段成功状态。retry 保留同一研究修订并校验复用已完成批次；revise、输入/模型/实现变更不会套用旧检查点。取消及孤儿恢复会检查嵌套批次进程身份。合并产物的作者证明必须包含全部批次的输入、响应和已校验回执，复用批次不重复计入新尝试的模型用量。

此分批策略目前用于三端平台事实研究；后续对齐、建树、绑定及独立审查仍以固定阶段契约执行，不将批次当成公共树分支或叶子。超出其他阶段上下文预算仍会明确阻断，不能将该错误或来源缺口标作整棵树完成。

发布分准备/提交。准备不会改变正式读取；提交持锁验证 CURRENT 的预期版本、对象哈希、冻结证明、作者/审查/评级交付和人工事件头，原子切换指针。重复提交幂等。冲突先读取新发布并重新准备完整候选，未变化知识对象可复用，无须重研。回滚命令创建新清单，审核历史持续生效。

HTTP 只保留 `/api/v2/`。current/tree/features/knowledge/sources/apis/runs/reviews/releases 为主要读取面；runs、knowledge/plans、runs/{id}/actions、calibrations/approve、freezes、releases/prepare|publish|rollback、reviews/{id}/decisions 为写入面。写请求必须带 JSON、Idempotency-Key、X-FeatureTree-Token 和 expected_release_id。令牌从本机 config 接口读取；Host、Origin、Sec-Fetch-Site 校验不允许跨站写入。版本冲突为 409；创建和启动模型任务为 202。

原文正文按窗口读取，source_catalog 的 body+query 可返回匹配段落和偏移。每个结果都固定快照；未采集正文返回 needs_sources。导出是指定发布的投影，修改导出不会自动改变正式事实。


执行资源限制支持 JSON `null`：阶段与首响应超时、Agent 步数、来源调用次数、交付块数、输入字符数，以及自动重试、语义返工和来源补充轮数均可取消，当前默认如此。分批大小仍用于划分完整输入，不限制总研究量；取消和业务校验保持有效。交付块字符数不再硬拒绝。`max_output_tokens: null` 仅取消 FeatureTree 注入的环境变量；OpenCode 原生默认和服务端硬上限仍存在，不能称为无限输出。改变执行政策后，可通过 checkpoint_reuse 重新校验旧批次，保留原始收据与内容，禁止跨模型或研究输入变化复用。
