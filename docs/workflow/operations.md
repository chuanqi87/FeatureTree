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

发布分准备/提交。准备不会改变正式读取；提交持锁验证 CURRENT 的预期版本、对象哈希、冻结证明、作者/审查/评级交付和人工事件头，原子切换指针。重复提交幂等。冲突先读取新发布并重新准备完整候选，未变化知识对象可复用，无须重研。回滚命令创建新清单，审核历史持续生效。

HTTP 只保留 `/api/v2/`。current/tree/features/knowledge/sources/apis/runs/reviews/releases 为主要读取面；runs、knowledge/plans、runs/{id}/actions、calibrations/approve、freezes、releases/prepare|publish|rollback、reviews/{id}/decisions 为写入面。写请求必须带 JSON、Idempotency-Key、X-FeatureTree-Token 和 expected_release_id。令牌从本机 config 接口读取；Host、Origin、Sec-Fetch-Site 校验不允许跨站写入。版本冲突为 409；创建和启动模型任务为 202。

原文正文按窗口读取，source_catalog 的 body+query 可返回匹配段落和偏移。每个结果都固定快照；未采集正文返回 needs_sources。导出是指定发布的投影，修改导出不会自动改变正式事实。
