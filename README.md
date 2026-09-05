# FeatureTree

构建一棵以平台无关语义定义的特性树，**以每个节点为比较单元，持续补充并确认各平台的支持情况和行为差异**。

平台无关约束节点的定义与分类方式。Android、iOS、HarmonyOS 的信息附着在每个节点上；单平台独有能力也进入公共树。

## 当前结果

- 已有 212 个比较节点，父节点和叶子都能记录平台支持与差异。
- 树的定义、范围与分类维护在 `taxonomy/`；每个节点对应一份 `knowledge/` 记录。
- 支持状态与确认进度分开；没有差异记录表示待确认。
- 原知识正文、编辑状态和历史判断已保留。迁移不会把旧断言自动升级为已确认。
- 结构校验与研究完成度分别报告，最新结果见 [进度报告](output/reports/progress.md)。

## 开始使用

大规模研究前按 [全量研究启动契约](docs/research-runbook.md) 执行 `.venv/bin/python scripts/preflight.py --rebuild-contexts`。当前选择为启动日最新正式版、手机优先；预检查会列出版本基线、试点、绑定正文和范围缺口，报告位于 `output/reports/readiness.md`。研究输入可用与结论完成确认分别判断。

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# 日常编辑后执行：只创建缺失知识，重建视图和审计
.venv/bin/python scripts/refresh.py

# 回归测试
.venv/bin/python -m unittest discover -s tests -v

# 验收指定域的差异是否全部确认；未完成返回 2
.venv/bin/python scripts/audit_coverage.py --domain connectivity --require-complete
```

原始镜像发生变化时，更新采集和候选映射：

```bash
.venv/bin/python scripts/harvest_inventory_from_docs.py
.venv/bin/python scripts/map_inventory_to_taxonomy.py
.venv/bin/python scripts/refresh.py
```

采集保留人工范围决定与人工映射；规则只产出候选。修改目录规则后运行映射命令，不会修改节点支持结论。

知识生产前的官方资料下载、离线检索和逐节点上下文命令见 [官方资料库](docs/official-corpus.md)；最新下载数量与文件完整性见 [资料验收报告](output/reports/official-documents/progress.md)。检索候选不等于平台结论已确认。

## 本地特性树浏览器

前端采用 React 19 + Ant Design 6 的标准管理台组件。首次启动需要安装并构建前端（Node.js 22.12+）：

```bash
npm --prefix web ci
npm --prefix web run build
.venv/bin/python scripts/serve_viewer.py
```

打开 <http://127.0.0.1:8765>。如端口被占用，可添加 `--port 8766`。

- 侧栏仅保留“特性树”和“知识评测”两个入口。特性树默认完整展开所有节点，通过筛选栏选择领域；Ant Design 树形表格用缩进和 L1–Ln 标记展示父子关系，各列展示定义、平台支持和确认进度。
- 支持搜索中文、英文、ID、别名和知识正文；搜索结果保留祖先路径。按 `/` 聚焦搜索，按 Escape 清空搜索。
- 支持按确认状态筛选，筛选后保留匹配节点的祖先路径；可一键重置。
- 新增置信度、真机复核需求、叶子/分支筛选，以及知识项数量预算；点击“导出复核清单”取得真正匹配的逐项 JSON，不含仅用于导航的祖先。详情新增“置信度与复核”，检索片段也显示评级。高可信不等于已实测，未评估不等于无需实测。规则与命令见 [知识置信度](docs/knowledge-confidence.md)。
- “关系图”展示节点连线，支持拖动平移、缩放和适应画布。详情中的“定位到树中”会清除筛选并展开所在路径。
- 点击节点或“查看详情”打开抽屉，查看定义、范围、平台支持、确认进度、知识正文、API 绑定、证据与全部原始字段。页面通过 `#node=节点ID` 记录选中节点。
- 支持与复核状态分开显示，历史判断单独归档展示；知识正文已整理不代表比较结论已确认。
- 页面直接读取 `taxonomy/`、`knowledge/` 和平台配置；修改数据后点击“刷新数据”即可，无须提前生成 `output/exports/tree.json`。读取失败时保留上一次成功的数据并显示错误。
- “知识评测”当前提供简单的本地关键词检索：输入问题或 API 名称后按 Enter 或点击“检索”，查看相关节点、正文及跨平台差异片段、确认状态与来源字段。点击示例问题会立即检索；点击结果可查看完整节点。检索不调用外部模型，不生成新的平台结论，不使用历史支持判断作为当前答案。

服务只监听本机地址，提供只读数据接口，不修改源文件。前端源码位于 `web/src/`；服务提供 `web/dist/` 中的构建产物。只修改树数据时不需要重建前端。

开发界面时，先启动上述 Python 服务，再在另一个终端运行 `npm --prefix web run dev`。Vite 开发服务器会将 `/api` 代理到本机的 8765 端口；若修改后端端口，请同步 `web/vite.config.js`。

前端树模型与 Ant Design 详情渲染回归测试：

```bash
npm --prefix web test
```

## 编辑入口与生成结果

| 路径 | 职责 |
| --- | --- |
| [方案](跨平台特性树方案.md) | 目标、分层、粒度和验收标准 |
| [比较模型](docs/comparison-model.md) | 支持、差异、确认状态及证据填写规则 |
| `config/comparison.yaml` | 平台与比较维度注册表 |
| `config/schema/*.schema.json` | 特性、知识、目录与比较记录的数据格式约束 |
| `taxonomy/*.yaml` | 唯一可编辑的特性树，定义范围、父子关系与精选绑定 |
| `knowledge/**/*.yaml` | 每节点的平台支持、维度比较、证据与知识正文 |
| `inventory/*/catalog.json` | 原始目录、纳入范围及多对多映射，人工决定标记 method |
| `config/mapping-rules.yaml` | 自动候选映射规则，无全局兜底归类 |
| `output/exports/tree.json` | 合并平台信息及进度的全节点树视图 |
| `output/exports/presence_matrix.csv` | 全节点 × 平台支持与确认状态 |
| `output/exports/comparison_matrix.csv` | 全节点 × 比较维度 × 平台对，空缺显式为 unknown |
| `output/exports/review_queue.json` | 知识项的置信度、真机需求、证据、复核计划和统计 |
| `output/exports/review-scopes/*.json` | 按子树、级别、实测需求、预算导出的范围清单 |
| `output/exports/index.json` | 精选绑定和目录映射的完整反向索引 |
| `output/reports/` | 结构审计与待确认清单 |
| `output/contexts/` | 按需生成的逐节点候选资料包 |
| `featuretree/` | 数据读写、比较、映射、证据校验、生成与迁移模块 |

从 [BLE 扫描过滤](knowledge/connectivity/bluetooth/le/scan/filter.yaml)、[目标组件调用](knowledge/interop/action_dispatch/component_intent.yaml)、[状态驱动界面更新](knowledge/ui/declarative/vs_imperative.yaml) 查看核实中的示例。它们保留了原知识，尚未完成固定版本下的确认。

## 数据维护约定

已有知识文件不会被生成器覆盖，包括 draft、注释和人工格式。`generate_taxonomy.py` 从 YAML 导出树视图，不覆盖树定义。日常使用 `scripts/refresh.py` 重建全部视图与审计；仅需重建绑定索引时运行 `scripts/rebuild_bindings.py`。

`scripts/migrate_v2.py` 只迁移 v1 数据，v2 数据重复执行不变。稳定 ID 保留，包括历史命名；名称与定义可在明确范围后修订。

`output/contexts/`、`output/reports/official-documents/documents.jsonl` 和 Python 缓存都是可删除重建的生成文件，重建资料输出的命令见 [官方资料库](docs/official-corpus.md)。`docs-raw/official/` 保存原始证据和数据库，应完整保留。`web/dist/` 是本地浏览器运行所需的构建产物。

配置与 Schema 统一放在 `config/`；导出结果、报告和候选资料统一放在 `output/`。其中历史验收记录保留，Git 仅忽略大型明细导出和候选资料包。
