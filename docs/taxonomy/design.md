# 特性树设计规则

从 29 个稳定 L1 领域入口重新设计。正式源为 `taxonomy/<domain>.yaml`，领域顺序为 `taxonomy/_index.yaml`。当前没有子能力，树未冻结。

## 范围与粒度

- 取 Android、iOS、HarmonyOS 公开应用开发能力的并集，单平台能力同样进入公共树。
- 只纳入公开 API/SDK 可调用能力；排除注册入驻、认证、结算和纯控制台操作。
- 先设计 L2/L3 的划分轴和边界，再按独立可比较能力细化到 L4/L5 或更深。
- 不按平台品牌、API 方法、回调、参数或枚举值凑节点；能力叶子目标约两千个，数量不代替质量。
- 同父节点的子节点共用 `sibling_axis`，避免单子分支和过宽分支。
- `branch` 是待细分或汇总范围；`atomic` 是独立能力。未展开 L1 保持 `branch`，不得算作能力叶子。

## 节点内容

按 `config/schema/feature.schema.json` 填写中英文名称、定义、父节点、层级、比较范围 includes/excludes、`sibling_axis`、`granularity` 与知识路径。

能力叶子使用 `knowledge_role: leaf` 和 `leaf_at_this_level: true`；分支使用 `knowledge_role: rollup`。跨域关联通过 `related_features` 明确表达，不能保留指向不存在节点的引用。

新设计节点至少提供一端的具体 API 符号和官方 URL，其他端未核实就保留未知。设计阶段 `anchor_status: unverified`；脚本核实失败时保留节点复审，不据此声称平台不支持。L1 起点暂不要求能力锚点。

`legacy` 用于明确的概念沿用、合并和拆分，新增节点用 `new`。历史 ID 的遗漏对照在新树形成后再做，不能为了旧数量恢复归档子树。

## 每域步骤

1. 阅读该 L1 的范围，设计 L2 和各分支的切分轴。
2. 用模型知识与官方语料提出能力、边界和 API 线索。
3. 标准 agent 先提交候选，经过结构门、独立局部审查和跨域审查，由协调者通过发布器写入正式 YAML。详见 [节点工作流](../workflow/design.md)。
4. 执行结构检查与刷新；只生成必要的知识空壳。
5. 树设计稳定后核实锚点，明确未解决问题，再决定是否冻结 ID。

```bash
.venv/bin/python scripts/export_design_inputs.py --domain connectivity
.venv/bin/python scripts/tree_lint.py --domain connectivity
.venv/bin/python scripts/refresh.py
.venv/bin/python scripts/verify_anchors.py --domain connectivity --write
```

设计输入只来自当前树。旧产物在 `archive/`，不参与默认生成。明确标为 `granularity: branch` 的未展开分支可以作为中间设计产物发布，再派单继续下钻；必须在报告中列明，不计为 atomic 叶子。

## 冻结前验收

确认各领域有合理子树、切分轴一致、粒度合理、跨域边界已处理、节点锚点已核实或缺口有清单。分别报告领域、总节点、分支与能力叶子数量。树结构通过和空分支清零均不代表覆盖完整。

冻结后才按 [知识研究原则](../knowledge/research-runbook.md) 生产三端知识；冻结必须基于实际验收，不能由脚本写死通过结论。
