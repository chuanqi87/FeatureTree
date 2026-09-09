# 批量节点研究操作手册

流程设计与职责表见 [agent-workflow.md](design.md)。当前可运行闭环为树设计、研究、审查与发布；知识正文生产不在此 CLI 的执行范围。

也可以从 [管理台](management-console.md) 选择节点，直接执行同一工作流并查看结果。

## 安装与预检

使用仓库已有 Python 环境与已配置好的 OpenCode。7 个 agent 在 `.opencode/agents/`，由项目路径加载；无需安装 Agent Bridge，也不修改用户全局 OpenCode 设置。

```bash
.venv/bin/python scripts/workflow.py doctor
# 可选：调用一次真实模型，检验命名 agent 和 JSON 契约；会使用模型额度
.venv/bin/python scripts/workflow.py doctor --smoke --timeout 300
```

doctor 校验 agent 名称与写入/shell/派单权限。smoke 产物在 `.workflow/smoke/`，只含合成协议测试内容；不算树研究证据。若默认模型不可用，检查 OpenCode 的供应商设置，或在 doctor/plan 使用已配置的 `--model provider/model`。不要以预检加载成功替代实际模型执行成功。

## 创建批次

先为本次研究准备 baseline JSON，结构见 `config/workflow/baseline.schema.json`。核实启动日期的最新正式版，填写三端 release、SDK、设备、官方来源。示例明确标为 unknown，只适合设计试跑，不能作最新正式版结论。

```bash
WORKFLOW_RUN=$(.venv/bin/python scripts/workflow.py plan \
  --node connectivity --node network \
  --baseline config/workflow/baseline.example.json \
  --depth 2 --max-nodes 40 --workers 3 \
  --timeout 600 --max-attempts 2 --max-revisions 2 \
  | .venv/bin/python -c 'import json,sys; print(json.load(sys.stdin)["run_id"])')

.venv/bin/python scripts/workflow.py report "$WORKFLOW_RUN"
```

plan 不调用模型、不生成平台结论、不修改树。`--node` 可重复；节点必须是当前已存在的 branch，不能同时选择祖先和后代。下钻已经产生的更深分支时，直接传其完整 ID。`--depth` 是相对当前节点的新增层数。`--max-nodes` 同时限制每端候选数和最终新增节点数，模型达到预算必须记录待拆单项。

优先以小批次验证分支切分轴，再扩大并发。默认同一时刻最多 3 个 OpenCode 进程；三端研究与跨节点研究共用此上限。默认输入字符预算 500,000，`--max-input-chars` 可调。工作包保留目标子树的完整记录、邻域边界及全局简表，整批审查复用局部审查结果；snapshot_path 供协调者追溯，禁用工具的 agent 直接消费包内数据。超出预算停止并提示拆分，不静默裁掉树。

生产运行建议显式设置 `--model provider/model`，必要时同时设置 `--variant`。不指定模型时使用 OpenCode 的默认选择；模型提供商或默认模型变化可能影响重现性，不能声称只靠输入哈希就能完全重现模型答案。

## 执行与汇总

```bash
.venv/bin/python scripts/workflow.py run "$WORKFLOW_RUN"
.venv/bin/python scripts/workflow.py report "$WORKFLOW_RUN"
```

run 返回 0 表示所有阶段已成功并具备设计发布条件；返回 2 表示仍有失败、退回或等待依赖。成功结果会复用，再次 run 不重复调用已成功的阶段。可以在另一终端执行 report 查看状态。

report 分开报告：任务状态、尝试次数、候选/分支/atomic 数、未展开分支、未知基线、锚点等级、研究缺口、deferred 候选、退回审查与后端 usage。`ready_to_publish` 仅表示这个批次可合入设计树，`tree_frozen` 始终为 false；不计算虚构的完整能力覆盖率。

## 错误恢复与语义返工

```bash
# 修复模型服务、格式或其他执行问题后，给 failed 任务追加一组有限尝试
.venv/bin/python scripts/workflow.py retry "$WORKFLOW_RUN"
.venv/bin/python scripts/workflow.py run "$WORKFLOW_RUN"

# 审查要求返工时，指定报告指向的原工作节点；可重复 --node
.venv/bin/python scripts/workflow.py revise "$WORKFLOW_RUN" --node connectivity
.venv/bin/python scripts/workflow.py run "$WORKFLOW_RUN"
```

retry 保留所有失败尝试，不把语义退回改成通过。revise 将退回意见与旧提案交给综合阶段；blocking 问题通过 target_stage 指向平台时，先重跑该平台并携带旧候选，再重跑综合、审查、锚点检测与全局审查。未被点名的平台和其他节点复用。达到返工上限后，收窄节点范围再新建批次。

中断后的 running 尝试会先核对记录的进程 ID、启动时间及命令，终止仍存活的旧进程组，再记为 interrupted，并按原尝试预算继续；已被系统复用的 PID 不会被终止。超时同样终止对应 OpenCode 进程组。CLI 前台取消时可能等待已发出的调用退出；每个调用仍受 timeout 限制。本地 manifest 锁避免双调度器抢写；v1 不提供跨机器分布式租约或远程结果导入。硬杀恰好发生在进程创建与登记之间时，记录可能不完整，需要核对未登记的进程。

规则/agent/契约更新会令旧运行拒绝恢复，需新 plan。正式树变化也要求重新计划与审查；不自动把旧批次 rebase 到新树。一个并行批次的节点先一起完成整批审查，再一次发布，可以避免同批任务互相造成快照过期。

## 发布与验收

```bash
.venv/bin/python scripts/workflow.py publish "$WORKFLOW_RUN"
.venv/bin/python scripts/tree_lint.py
.venv/bin/python scripts/refresh.py
```

publish 是本地协调者写入动作，不是在线部署。它重新校验产物与输入哈希，检查正式 taxonomy 的字节快照，再生成可恢复事务。新增节点补未知知识 stub；已有知识正文保留，只更新必要的 rollup child_index。锚点缺失保留 failed，不删除候选、不据此声称不支持。

若发布中断，再执行同一 publish 即可继续；若文件出现既非 before 又非 after 的内容，则停止并报告冲突。发布成功后重复调用返回同一回执。跨文件更新不保证原子可见，因此发布完成后再刷新看板。

## 准确性与执行预算

### 检索与角色边界

scope 提供三端各自的 `research_queries`，每条为单一 API 符号或短语。检索器保留原查询和归一化查询，优先具体模块/标题，跨查询分配最多 6 份材料，每条最多 2 份。正文去重、排除元数据明确不适用 iOS 的资料、核对哈希，并附带行号摘录；无匹配明确记录缺口。摘录降低定位成本，不能替代公开性、版本与设备条件核实。

scope/synthesize/integrate 禁用全部工具，只消费工作包内的树、候选、Schema 和 policy_context。平台研究与局部审查使用 read 或官方 URL 定向复核，文件权限限定为 `docs/*` 与 `docs-raw/official/snapshots/<platform>/*`；禁止读取其他运行目录。OpenCode 的 glob/grep 权限匹配对象不是目录，这两个工具在标准研究角色中禁用。审查另收到经过输入/产物哈希核对的 source_refs。平台 agent 限制额外定位轮数并短段阅读；轮数是提示词约束，时间预算由执行器强制限制。

未知候选必须保留 unknown；框架公开不等于该候选能力可公开调用，目录缺项不能证明不支持。公共并集节点至少一端有具体正向 API 即可保留，不为凑齐三端添加否定性 binding。符号与解释分开，缺口不独立生成能力叶子。

### 超时与格式恢复

`plan --first-response-timeout 120` 配置首次 CLI 模型活动等待上限，管理台高级参数亦可设置。启动事件不计入活动；文本、工具事件、错误或步骤完成才计入。此值不是底层模型首 token 时间，OpenCode 可能在整段文本完成后才输出事件。首次活动超时、单阶段总超时、进程被信号终止均停止自动重试；检查日志、模型服务与任务预算后再显式 retry 或新建计划，不能直接归因于供应商故障。

已有信封形态的答案若只因 JSON 语法/包装失败，下一次尝试携带原答案和原输入做格式修复，不重复检索。前置说明、围栏、字符串引号损坏可进入修复；原答案字节哈希和原输入哈希必须一致，修复结果仍须通过全部契约与结构门。此分类不从原文本截取 JSON 直接采信，也不能保证模型逐字保留内容。格式修复计入原尝试预算；没有信封的步骤耗尽说明、缺失答案和多个歧义 JSON 停止自动修复，重复 JSON 键亦不走此捷径。

### 定向语义返工

审查 blocking issue 通过 `target_stage` 指定责任：候选字段、证据或平台条件错误归 `android` / `ios` / `harmonyos`，结构和映射错误归 `synthesize`。只重跑所选节点被点名的平台，再执行下游验收；warning 不自动扩大研究范围。未带 target_stage 的旧审查兼容综合返工。模型必须实际修正上游字段，不能只在节点 note 中口头覆盖旧值。

### 度量与质量结论

管理台分别展示墙钟耗时、累计阶段耗时、首次 CLI 活动、Agent 执行次数和复用标签。兼容字段 `model_calls` 统计 Agent 后端执行尝试（OpenCode run），复用产物不计入；不是供应商 HTTP 请求数或工具对话轮数。usage 仅为后端已返回步骤的使用量，缺失不补零，上报金额 0 不代表账单免费。

实际研究仍需人工验收覆盖、边界、粒度和公开 API 适用性；小预算留下的分支、deferred 与 gaps 必须继续处理。运行与试跑记录位于 `.workflow/experiments/`、`output/reports/`。2026-09-09 的 print_scan 样本产生 9 个分支草案，但未通过研究验收；最后一轮流程修复有自动测试、真实权限探针及浏览器验证，尚未重新完成全流程实跑。不得将协议 smoke 或自动测试通过率当作树质量验收。

## 文件与追溯

```text
.workflow/runs/<run-id>/
  snapshot.json                  全树、原始 YAML 字节内容、比较基线
  state.json                     DAG、尝试预算、状态、产物哈希
  attempts/<node>/<stage>/<n>/
    input.json                   本次完整输入、Schema、输入哈希
    events.jsonl                 OpenCode 原始事件
    stderr.log                   CLI 诊断
    response.json                模型原始答案（可能尚非合法 JSON）
    result.json                  通过契约后的结果
    metadata.json                会话、用时、后端提供的 usage
    process.json                 进程身份，用于中断后的安全清理
  report.json                    可重建报告
  publication.json               发布前后内容及文件哈希
```

失败尝试可能只有输入和日志，原因保存在 state.json。`.workflow/` 被 Git 忽略但用于恢复和审计，应随研究成果单独备份；不能作为临时 output 随意删除。Schema 和 agent 定义随代码版本管理。规则修改令旧任务只读可查，须新 plan；本次显式诊断复用不代表生产支持跨规则恢复。

## 实现验收

- 契约：错误 task_id/input_hash、必填字段、平台 URL、丢候选、越界节点、重复 ID、知识路径逃逸和无锚点被拒绝。
- 运行：命名 agent 可加载；有界重试、局部/全局退回、定向上游返工、成功阶段复用、共享并发与运行锁通过测试。
- 发布：run 不写正式树；全部审查通过后才能合并；过期树和产物篡改被拒绝；发布可恢复、幂等；新增知识保持 unknown。
- 研究：真实节点必须独立检查边界、覆盖、粒度与证据适用性。当前试跑未通过此项，不能据此扩大批量研究。
