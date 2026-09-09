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

优先以小批次验证分支切分轴，再扩大并发。默认同一时刻最多 3 个 OpenCode 进程；三端研究与跨节点研究共用此上限。默认输入字符预算 500,000，`--max-input-chars` 可调。工作包保留目标子树的完整记录、邻域边界及全局简表，整批审查复用局部审查结果；完整不可变树通过 snapshot_path 读取。超出预算停止并提示拆分，不静默裁掉树。

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

retry 保留所有失败尝试，不把语义退回改成通过。revise 自动将退回意见及旧提案交给 synthesis，重跑受影响节点的综合、审查、锚点检测与全局审查；成功的三端研究和其他节点复用。达到返工上限后，收窄节点范围再新建批次。

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

## 文件与追溯

```text
.workflow/runs/<run-id>/
  snapshot.json                  全树、原始 YAML 字节内容、比较基线
  state.json                     DAG、尝试预算、状态、产物哈希
  attempts/<node>/<stage>/<n>/
    input.json                   本次完整输入、Schema、输入哈希
    events.jsonl                 OpenCode 原始事件
    stderr.log                   CLI 诊断
    response.json                模型最终原始 JSON 文本
    result.json                  通过契约后的结果
    metadata.json                会话、用时、后端提供的 usage
    process.json                 进程身份，用于中断后的安全清理
  report.json                    可重建报告
  publication.json               发布前后内容及文件哈希
```

失败尝试可能只有输入和原始日志，原因在 state.json。`.workflow/` 被 Git 忽略但用于恢复和审计，应随研究成果单独备份；它不是可随意删除的临时 output。Schema 和 agent 定义必须随代码版本管理。

## 本轮实现验收

- 契约验收：错 task_id/input_hash、缺必填字段、错误平台 URL、丢候选、越界节点、重复 ID、知识路径逃逸和无锚点被拒绝。
- 运行验收：实际命名 agent 可加载；测试覆盖有界重试、局部/全局退回、成功阶段复用、共享并发上限与运行锁。
- 发布验收：run 无正式写入；发布前全部审查通过；过期树与产物篡改被拒绝；中断后可继续；重复发布幂等；新增知识为 unknown。
- 研究验收：需要另行运行真实节点试点，人工抽查边界、覆盖、粒度与证据适用性。合成测试和协议 smoke 均不代替这项验收。
