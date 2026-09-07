# 特性树设计契约

本文件定义如何直接设计并写入正式 `taxonomy/`。inventory-first / tree-expansion 流程已归档，不再使用。

## 分层原则

| 阶段 | 谁做 | 做到什么程度就够 |
| --- | --- | --- |
| 树设计 | 协调者 | 定义、边界、切分轴、粒度、至少一端 API 锚点；可先用模型知识 |
| 结构验收 | 协调者 + `tree_lint.py` | 轴一致、去重、层数、品牌命名、旧 ID 去向 |
| 锚点核实 | `verify_anchors.py` + 可选模型 | URL/正文/符号命中；失败保留节点标 failed |
| 知识生产 | 并行模型（树冻结后） | 三端实现、条件、置信度、evidence_refs |

## L1 领域（29）

现有 25 根 + `documents`、`digital_wellbeing`、`print_scan`、`games`。新增 L1 前须先与用户对齐。

## 节点必填标准

每个节点写入 `taxonomy/<domain>.yaml`，符合 `config/schema/feature.schema.json`：

- `name.zh` / `name.en`、`definition`（能力定义 + 边界）
- `comparison_scope.includes`（≥1）、`excludes`（原子节点应指向其他节点 ID 或明确“无相邻混淆项”）
- `sibling_axis`：与同父兄弟共用的切分轴字符串；同一父下所有子节点必须相同
- `granularity`：`branch` 或 `atomic`；`atomic` 须 `leaf_at_this_level: true` 且 `knowledge_role: leaf`
- `bindings`：至少一端 `{kind, id, url}`；其他端未查到时 `note: 未查到公开入口，待核`，**禁止**写“不支持”
- `legacy`：见下节
- `anchor_status`：设计阶段默认 `unverified`；核实脚本回写

## 切分规则

- 按**独立可比较的应用能力**切分，不按 start/stop、callback、错误码、参数枚举、文件格式值凑节点。
- 不按平台品牌建平行节点（App Links / Universal Links / App Linking → 同一能力）。
- 同级必须共用同一 `sibling_axis`；单子分支应避免（除非过渡）。
- 能力节点不要直接挂在 L1；至少经过 L2。
- 未细分完保留 `granularity: branch`，不要为清零未展开而假 atomic。

## Legacy（旧 212 节点）

```yaml
legacy:
  disposition: kept          # kept | renamed_from | merged_from | split_from | new
  sources: []                # 相关旧 feature id 列表；kept 且 id 未变时可省略或填自身
```

- 能延续概念的**保留旧 ID**（`disposition: kept`）。
- 改名：`renamed_from` + `sources: [old.id]`，新 id 为当前 id。
- 合并：保留 canonical id，`merged_from` + 被合并旧 id。
- 拆分：多个新节点各自 `split_from` + 同一旧 id。
- 全新能力：`new`。
- `scripts/legacy_map.py` 要求每个旧 212 id 至少出现在一处 `sources` 或作为现网 `kept` id。

## 每域工作流

1. 读 `scripts/export_design_inputs.py --domain <id>` 输出（旧树 + 归档草稿线索）。
2. 先定 L2 与各 L2 的 `sibling_axis`，再细分到 atomic（目标每域约 50–150 节点，按密度调整）。
3. 写入 `taxonomy/<id>.yaml`，运行：
   ```bash
   .venv/bin/python scripts/tree_lint.py --domain <id>
   .venv/bin/python scripts/refresh.py
   ```
4. 知识空壳由 `create_missing_knowledge` 生成；阶段 1 **不**手写三端知识正文。

## 验收清单（全树）

- [ ] `tree_lint.py` 无 error
- [ ] 29 个 L1 均有合理 L2+ 子树
- [ ] 跨域已知重复已合并或 `related_features` 互指
- [ ] 旧 212 id 全部有 legacy 去向（`legacy_map.py`）
- [ ] 锚点核实完成或 failed 清单已交付用户
- [ ] ID 冻结后再启动知识生产

## 命令速查

```bash
.venv/bin/python scripts/export_design_inputs.py --domain connectivity
.venv/bin/python scripts/tree_lint.py
.venv/bin/python scripts/tree_lint.py --domain ui
.venv/bin/python scripts/verify_anchors.py --domain connectivity
.venv/bin/python scripts/legacy_map.py
.venv/bin/python scripts/refresh.py
.venv/bin/python scripts/serve_viewer.py
```
