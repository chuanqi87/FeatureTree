# FeatureTree

构建 Android、iOS、HarmonyOS 公开应用开发能力的公共特性树。树的完整性、边界和粒度优先，三端知识在树稳定后生产。

当前起点：**29 个 L1 领域、0 个能力叶子、0 条已确认知识，树未冻结。** `knowledge/` 只有维持数据契约的领域空壳。

初次阅读代码，从 [代码地图与旧文件去向](docs/architecture/code-map.md) 开始。后端看 [模块导航](featuretree/README.md)，前端看 [功能目录](web/src/README.md)，规则看 [文档导航](docs/README.md)。

```bash
# 一个入口查看所有可用能力
.venv/bin/python -m featuretree --help
# 启动管理台
.venv/bin/python -m featuretree console
```

## 正式目录

| 路径 | 用途 |
| --- | --- |
| `taxonomy/` | 当前树定义与 L1 顺序 |
| `knowledge/` | 当前节点知识；空壳不算研究成果 |
| `config/` | 数据 Schema、比较维度与来源适用性策略 |
| `docs/` | 树设计、资料使用和知识证据规则 |
| `docs-raw/` | 保留的官方原始资料与全文索引 |
| `featuretree/` | 分层后端：core / taxonomy / knowledge / corpus / reporting / workflow / console / cli |
| `scripts/` | 既有命令的兼容薄入口；业务实现在后端包内 |
| `web/` | 节点分析管理台、任务状态、候选验收与本地知识检索 |
| `tests/` | 使用独立样例的回归测试 |
| `output/` | 按需生成的视图和报告，可删除重建 |
| `archive/` | 历史数据和旧实现，不参与当前流程 |

旧批次调度、研究派单、试点验收、迁移、inventory 目录与映射管线已从正式目录移除。新的节点工作流独立实现，不读取旧运行状态。

## 标准 Agent 工作流

整体设计见 [职责、边界与验收标准](docs/workflow/design.md)，运行命令见 [批量执行操作手册](docs/workflow/operations.md)。

通过 `scripts/workflow.py` 创建节点工作单，交给 OpenCode 加载 `.opencode/agents/` 中的 7 个标准 agent 执行：范围设计 → 三端并行研究 → 候选汇总 → 局部审查 → 锚点检测 → 全局审查 → 协调者发布。支持任意深度 branch 下钻、有界并发/重试、定向返工、恢复与冲突检查。

```bash
.venv/bin/python scripts/workflow.py doctor
.venv/bin/python scripts/workflow.py --help
```

运行结果在 `.workflow/`，正式树由发布器统一写入。当前仍是 29 个 L1 起点；工作流代码与测试通过不表示实际能力树已研究完成。

## 从 L1 开始

遵循 [树设计规则](docs/taxonomy/design.md)，先设计领域的 L2/L3，再展开独立能力。使用 [官方资料工具](docs/corpus/guide.md) 查找具体 API 锚点。编辑后执行：

```bash
.venv/bin/python scripts/tree_lint.py
.venv/bin/python scripts/refresh.py
```

`refresh.py` 只补缺失知识空壳、生成导出并校验数据，不会调用模型或覆盖已有知识。`output/` 无须作为重启前置数据保留。只有 L1 时，各领域仍按分支统计。

## 本地看板

```bash
# 首次安装
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
npm --prefix web ci

# 构建并启动
npm --prefix web run build
.venv/bin/python scripts/serve_viewer.py
```

打开 [本地看板](http://127.0.0.1:8765)。服务直接读取当前 `taxonomy/` 和 `knowledge/`，不依赖 `output/`；更改数据后刷新页面。端口可用 `--port` 修改。知识检索是本地关键词检索，不自动生成平台结论。

在节点行点击“分析”，或在详情中选择“下钻分析 / 根节点分析”，可直接启动 OpenCode 工作流；侧栏“分析任务”提供阶段结果、重试、返工与合并入口。详见 [管理台操作说明](docs/workflow/management-console.md)。

## 校验

```bash
.venv/bin/python -m unittest discover -s tests -q
npm --prefix web test
```

结构检查通过不等于能力覆盖完整，官方链接存在不等于结论已确认。知识生产时遵循 [研究原则](docs/knowledge/research-runbook.md)、[比较模型](docs/knowledge/comparison-model.md) 和 [置信度规则](docs/knowledge/confidence.md)。

归档入口：[L1 重置前数据](archive/2026-09-08-l1-reset-145119/ARCHIVE-README.md) · [正式目录清理前快照](archive/2026-09-09-clean-restart-140141/ARCHIVE-README.md)。
