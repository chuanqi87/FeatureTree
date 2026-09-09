# FeatureTree

构建 Android、iOS、HarmonyOS 公开应用开发能力的公共特性树。树的完整性、边界和粒度优先，三端知识在树稳定后生产。

当前起点：**29 个 L1 领域、0 个能力叶子、0 条已确认知识，树未冻结。** `knowledge/` 只有维持数据契约的领域空壳。

## 正式目录

| 路径 | 用途 |
| --- | --- |
| `taxonomy/` | 当前树定义与 L1 顺序 |
| `knowledge/` | 当前节点知识；空壳不算研究成果 |
| `config/` | 数据 Schema、比较维度与来源适用性策略 |
| `docs/` | 树设计、资料使用和知识证据规则 |
| `docs-raw/` | 保留的官方原始资料与全文索引 |
| `featuretree/`、`scripts/` | 数据校验、官方检索、导出和本地服务 |
| `web/` | 只读树浏览器与本地知识检索 |
| `tests/` | 使用独立样例的回归测试 |
| `output/` | 按需生成的视图和报告，可删除重建 |
| `archive/` | 历史数据和旧实现，不参与当前流程 |

旧批次调度、研究派单、试点验收、迁移、inventory 目录与映射管线已从正式目录移除。当前没有后台生成任务。

## 从 L1 开始

遵循 [树设计规则](docs/tree-design.md)，先设计领域的 L2/L3，再展开独立能力。使用 [官方资料工具](docs/official-corpus.md) 查找具体 API 锚点。编辑后执行：

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

## 校验

```bash
.venv/bin/python -m unittest discover -s tests -q
npm --prefix web test
```

结构检查通过不等于能力覆盖完整，官方链接存在不等于结论已确认。知识生产时遵循 [研究原则](docs/research-runbook.md)、[比较模型](docs/comparison-model.md) 和 [置信度规则](docs/knowledge-confidence.md)。

归档入口：[L1 重置前数据](archive/2026-09-08-l1-reset-145119/ARCHIVE-README.md) · [正式目录清理前快照](archive/2026-09-09-clean-restart-140141/ARCHIVE-README.md)。
