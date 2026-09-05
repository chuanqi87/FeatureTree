# 官方资料库与知识生产前的读取流程

本仓库已实现官网目录采集、正文下载、可续传队列、离线全文检索和按特性节点组装候选上下文。数据保存在本机 `docs-raw/official/`，使用 Python 命令读取，不依赖旧项目继续存在。该工具不调用模型，也不生成或确认平台支持结论。

最新数量、失败项和完整性结果见 [下载验收报告](../output/reports/official-documents/progress.md)。逐 URL 的来源、状态、原文路径、获取时间和哈希保存在 `docs-raw/official/corpus.sqlite` 中，执行 `audit` 命令会导出到 `output/reports/official-documents/documents.jsonl`。该明细导出可删除，需要时重新生成。官方入口及接口使用条件见 [官方文档入口](official-documentation-entrypoints.md)。

## 准备范围

| 平台 | 目录与正文来源 | 仍需按节点核实 |
| --- | --- | --- |
| Android | 官方 Sitemap 及 9 个子清单；开发指南、框架与部分 API 的官方 HTML 正文；跟进正文中的官方链接 | 深层 API 仍有待下载项；AndroidX、系统 API Level 和 Google 服务版本分别核对 |
| Apple / iOS | Technologies DocC 目录及正文引用图；官方 Markdown，缺失时回退 DocC JSON | 引用图不是已验证的全站清单；部分细分符号尚未下载；资料包含 macOS 等其他平台，不能默认适用于 iOS |
| HarmonyOS | 华为官网 `harmonyos-guides`、`harmonyos-references` 两棵目录，旧缓存校验后导入，并下载目录及正文中的新增链接 | 两棵目录不等于华为全站；失效路径、没有 Markdown 的旧页面、媒体和其他文档集合仍可能需要官网人工读取 |

第一轮下载优先级为 0–40，包括已引用资料、开发指南、框架、Kit、模块入口及其主题文章。Android / Apple 的细分 API 和历史 Android API diff 仍可通过完整的已发现 URL 清单定位后按需下载。此处的“完整清单”仅指已采集清单的本地保存，不表示三个官网所有页面均已发现。

目前不是完整离线镜像。图片、视频、下载附件和动态交互没有整站离线保存；部分鸿蒙正文保留 `media:` 占位符。必要事实如果依赖这些内容，必须到官网查看并补充证据。OpenHarmony 的资料独立于本库的 HarmonyOS 发行版判断。

## 生产一个节点前

在仓库根目录运行以下命令。先检查节点定义、比较范围和目标版本；检索结果只是候选资料。

```bash
# 1. 搜索已经下载的正文（支持英文 API 名与中文词组）
.venv/bin/python scripts/official_docs.py search 'Bluetooth scan filter' --platform android
.venv/bin/python scripts/official_docs.py search '蓝牙扫描' --platform harmonyos

# 2. 查官方目录，包括尚未下载的 API
.venv/bin/python scripts/official_docs.py locate 'PeriodicWorkRequest' --platform android

# 3. 根据查到的官方地址下载缺失正文；已有正文则复用，可加 --refresh 更新
.venv/bin/python scripts/official_docs.py fetch 'https://developer.android.com/reference/androidx/work/PeriodicWorkRequest'

# 4. 读取原文及其行号；读取时自动核验正文 SHA-256
.venv/bin/python scripts/official_docs.py read 'https://developer.android.com/reference/androidx/work/PeriodicWorkRequest' --start-line 1 --lines 100

# 5. 为一个节点重新整理三平台候选资料与段落
.venv/bin/python scripts/official_docs.py context connectivity.bluetooth.le.scan.filter --limit 5

# 或为全部节点重建候选资料包
.venv/bin/python scripts/official_docs.py context --all --limit 5
```

运行上述 `context` 命令后，生成的 `output/contexts/<feature_id>.json` 包含节点定义、比较维度、三平台候选文档、官方 URL、原文路径、获取时间、双份 SHA-256、章节行号和截断标记。这些候选包可删除重建。`binding_source_gaps` 列出尚无可读正文的绑定资料，通用搜索命中不会消除这些缺口。完整文件仍可用 `read` 或本地路径继续阅读。

生成者必须执行下面的证据核实：

1. 阅读候选正文，判断是否确实涉及当前节点；跟进方法、参数、权限、后台限制和版本说明。不要把检索片段直接作为全文。
2. 核对发行版、系统/SDK/库版本、设备和运行条件；Apple 的 availability 需要明确包含 iOS 或由其他官方材料说明适用性。
3. 为每个关键平台事实和差异绑定官方 URL、章节或符号、适用上下文；使用本地原文时记录路径与哈希。官方明示与分析分开写。
4. 缺少正文、版本依据或必要媒体时继续从官方入口检索；无法核实则保留 `unknown` 并写具体缺口。不能据此声称平台不支持。
5. 完成核实后再按 [比较模型](comparison-model.md) 填写确认信息。`claim_ready` 默认且始终为 `false`，候选匹配数不构成自动确认条件。

这份工具已提供资料获取与上下文准备能力。现有 `generate_knowledge.py` 负责知识记录维护，不是已接入模型的批量研究流水线；未来生产程序需要显式调用上述流程并遵守 `AGENTS.md` 的证据要求。

## 下载、续传和更新

```bash
# 获取或复用官方目录快照，再将目录纳入可检索的 URL 队列
.venv/bin/python scripts/official_docs.py catalogs
.venv/bin/python scripts/official_docs.py seed

# 继续优先下载指南、框架和模块主题；已保存正文自动跳过
.venv/bin/python scripts/official_docs.py crawl --workers 12 --max-priority 40 --retry

# 扩展到所有已发现 API 和历史文档；--limit 可限制本次请求次数
.venv/bin/python scripts/official_docs.py crawl --workers 12 --max-priority 100 --retry --limit 2000

# 更新官网目录；正文按需 fetch --refresh，避免把旧快照静默覆盖
.venv/bin/python scripts/official_docs.py catalogs --refresh
.venv/bin/python scripts/official_docs.py seed

.venv/bin/python scripts/official_docs.py status
.venv/bin/python scripts/official_docs.py audit --verify-files
```

下载按官网主机限速，遇到 429 遵守退避；最多 4 次自动尝试，HTTP 404/410 和访问拒绝不会无休止重试。修复来源地址或解析问题后可用 `fetch URL` 单独重试。该命令只接受允许的官方文档域名和路径；跳转到其他来源会留下错误，需查明后处理。

Google Developer Knowledge API/MCP 和 Xcode Documentation Search 的官方入口已记录，但本机尚未为本任务配置其认证/连接。当前检索和下载使用本地索引及无需凭据的官方正文入口。

下载器使用已有的 HTTP/HTTPS 代理环境变量，并在未显式设置代理时读取 macOS 系统代理；仅设置 NO_PROXY 不再阻止系统代理回退。正文与目录下载采用相同策略，无需修改系统网络设置。跨平台候选筛选、上下文过期检测和全量启动检查见 [研究启动契约](research-runbook.md)。

## 文件与状态

- `docs-raw/official/catalogs/`：官网清单原始响应、请求与时间/哈希元数据，以及按哈希保存的历史目录快照。
- `docs-raw/official/snapshots/`：按平台、URL 哈希和原文哈希保存的 gzip 原始响应、规范化 Markdown 与元数据。
- `docs-raw/official/corpus.sqlite`：下载状态、历史快照引用、目录索引、英文/中文全文索引。
- `output/contexts/`：从资料库生成的逐节点候选上下文及汇总，可重建。
- `output/reports/official-documents/`：可追踪的状态清单和验收报告。

`ready` 表示解析出可检索正文；`thin` 表示正文太少、主要用于导航；`partial` 表示原始结构化数据已保存，但 Markdown 渲染有未处理的结构。这些状态都不能证明该节点的事实研究已完成。

`pending` 表示尚未请求；`failed` 表示网络、跳转或解析错误；`not_found` 表示尝试的正文表示返回 404/410，**不证明官网导航页面不存在或平台不支持**；`blocked` 表示访问受限；`excluded` 表示地址被识别为非文档资源并排除。错误、发现来源和原始地址均保留。

获取时间固定抓取时点，原文 SHA-256 固定内容，二者都不能固定 SDK 适用版本。更新会保留旧的原文文件；失败的刷新保留此前可读取的正文，并留下刷新错误。

大型资料库和候选上下文已加入 `.gitignore`。资料库保存在本机，候选上下文按需生成。迁移时，在下载命令结束后整体复制 `docs-raw/official/`，保留 SQLite 文件与全部 snapshots/catalogs；再运行 `audit --verify-files`。不能仅复制数据库或 Markdown 并称作已保留原始证据。
