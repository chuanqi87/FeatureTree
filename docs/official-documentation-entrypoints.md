# 三平台官方文档入口与生产使用规则

核验日期：2026-09-05。范围：Android、iOS、HarmonyOS 应用开发的官方资料。

已找到可用于检索、读取和缓存官方正文的入口，并完成大批正文下载、离线索引、按需补抓和逐节点候选上下文工具；使用方式见 [官方资料库](official-corpus.md)，实际数量与错误见 [验收报告](../output/reports/official-documents/progress.md)。尚未完成全站离线镜像，也没有把候选资料自动认定为知识证据。没有找到并验证同时满足“当前版本、完整 API、全部指南”的三平台官方整包下载方案。

## Android

| 用途 | 官方入口 | 使用方式 |
| --- | --- | --- |
| 开发指南与功能主题 | [Develop for Android](https://developer.android.com/develop) | 沿具体主题读取开发指导、约束和示例 |
| API 参考 | [Android API reference](https://developer.android.com/reference) | 继续进入具体包、类、方法和属性，不能只读包目录 |
| 页面发现 | [官方 Sitemap](https://developer.android.com/sitemap.xml) | 本次返回 9 个子 Sitemap；这是页面清单入口，不是正文离线包 |
| 官方知识库 | [Google Developer Knowledge](https://developers.google.com/knowledge/mcp) | 官方远程 MCP：`https://developerknowledge.googleapis.com/mcp` |
| 知识库范围 | [Corpus reference](https://developers.google.com/knowledge/reference/corpus-reference) | 明确包含 `developer.android.com`，也包含 Google/Firebase 等其他来源；检索时限定来源 |

Google 的官方服务提供 `search_documents` 和 `get_documents`：先检索，再读取命中文档的完整内容。REST 的 [documents.get](https://developers.google.com/knowledge/reference/rest/v1/documents/get) 明确返回完整 Markdown；[searchDocumentChunks](https://developers.google.com/knowledge/reference/rest/v1/documents/searchDocumentChunks) 返回片段和所属文档标识。

接入需要启用 Developer Knowledge API，并使用 API key 或 OAuth。官方说明该服务返回英文公开文档并依赖网络。本次只核对官方说明，未配置认证或调用已认证的知识库查询。无需凭据的官网 HTML 读取已实测成功；应提取文章主体，保留代码、表格和章节关系。

离线策略：使用 Sitemap 建立待采集清单，再缓存所需官方正文；API Level、AndroidX 库版本和 Google 生态服务分别标注。本次读取的 [SDK 仓库清单](https://dl.google.com/android/repository/repository2-3.xml) 没有发现 path 含 `docs` 的 remotePackage，不能依赖旧教程中的 SDK Manager 文档下载选项来证明当前全量离线包存在。

## Apple / iOS

| 用途 | 官方入口 | 使用方式 |
| --- | --- | --- |
| 框架与技术目录 | [Technologies](https://developer.apple.com/documentation/technologies) | 发现框架，继续遍历 Topics、符号和文章 |
| 场景与技术选型 | [Technology Overviews](https://developer.apple.com/documentation/technologyoverviews) | 补充任务、场景与跨框架指导 |
| 可直接读取的正文 | [Core Bluetooth Markdown 示例](https://developer.apple.com/documentation/corebluetooth.md) | 页面公开提供 View Markdown 链接；已验证 HTTP 200 和 Markdown 正文 |
| 结构化目录数据 | [Technologies DocC JSON](https://developer.apple.com/tutorials/data/documentation/technologies.json) | 本次可读取；保存元数据和引用，继续获取所引用文章的正文 |
| 官方 Agent 工具 | [Xcode 外部 Agent 接入](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode) | Apple 提供 `xcrun mcpbridge`；[Xcode updates](https://developer.apple.com/documentation/updates/xcode) 介绍 Apple Documentation Search |

离线策略：从官网目录发现页面，保存每页官方 Markdown，以及用于符号标识和可用性核对的 DocC JSON。`.md` 读取在抽样页面成立，批量采集仍须逐页验证内容类型和正文，不能把任意拼接 URL 的成功状态当成完整覆盖。DocC 数据地址是实测的站点数据入口，不在此承诺第三方采集接口的稳定性。

Apple 的目录包含多个操作系统；需逐符号核对 iOS 适用性。框架页面的 availability 元数据可能为空，需要具体符号与版本资料补足，不能默认该目录全部适用于 iOS。

本机已安装 Xcode 26.6，并存在 `mcpbridge` 可执行文件；本次没有修改 Xcode 或 Agent 配置，也没有验证 MCP 查询。没有找到并验证可直接下载的“最新全部 Apple 文档整包”，不能将 Xcode 安装完成或本地索引存在当成全文离线就绪。

## HarmonyOS

| 用途 | 官方入口 | 使用方式 |
| --- | --- | --- |
| 文档总入口 | [华为文档中心](https://developer.huawei.com/consumer/cn/doc/) | 发现 SDK、开发指导及其他文档集合 |
| 开发指导 | [应用开发导读](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-guide) | 导读说明指南与 API 参考的范围 |
| API 参考 | [开发说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/development-intro-api) | 获取具体 Kit、模块、接口与限制 |
| 知识导航 | [官方知识地图](https://developer.huawei.com/consumer/cn/app/knowledge-map/) | 导读链接的应用开发旅程入口；用于导航，不代替正文 |
| 可直接读取的正文 | [BLE API Markdown 示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble.md) | 已实测返回参数、权限、版本、错误码和示例等正文 |

本次还读取了官网使用的目录端点：

`POST https://svc-drcn.developer.huawei.com/community/servlet/consumer/cn/documentPortal/getCatalogTree`

请求体分别为：

```json
{"language":"cn","catalogName":"harmonyos-guides","showHide":1}
```

```json
{"language":"cn","catalogName":"harmonyos-references","showHide":1}
```

两份响应均为业务成功（`code: 0`）。开发指南目录返回 5,743 个节点、5,722 个唯一非空文档目标；API 目录返回 4,771 个节点、4,762 个唯一非空文档目标。这些是本次返回的目录统计，包含容器、不同适用范围和需要过滤的条目，不能当成已成功下载的正文数或公开应用 API 数。这两棵目录也不等于华为站所有文档集合。

目录端点是实测可用的官网服务，尚未找到对第三方稳定调用的公开契约。用于发现页面时需保存响应快照，并准备官网导航回退。采集正文可以使用页面的 `.md` 表示，但需处理失效页面、媒体占位符、代码和表格保真，以及重复条目。

离线执行：已校验并导入旧项目的指南/API 原始缓存，再按当前目录和正文链接补抓；内容已独立保存到本仓库 `docs-raw/official/`。目录中仍有失效或无法取得 Markdown 的条目，具体状态逐 URL 保留。不能把缓存目录是否提交 Git 当成正文是否存在的判断依据。

## 可整库离线的补充来源：OpenHarmony

[OpenHarmony 官方文档仓库](https://github.com/openharmony/docs) 提供应用开发、设备开发文档及发行版分支，可通过 Git 克隆或归档下载离线保存。保存选定分支的具体 commit，而不只记录漂移的 `master`。

这是 OpenHarmony 的文档全集来源。HarmonyOS 的商业 Kit、HMS、设备和发行版条件仍应核对华为官方文档；不能用该仓库代替 HarmonyOS 全集。

## 生成时的证据流程

1. 确定特性节点的定义、比较范围、目标系统/SDK/库版本及设备条件。
2. 在各平台官方目录或知识库中检索具体 API、指南、权限、后台约束和版本变化。
3. 读取命中文档的正文，并跟进与当前结论有关的链接。标题、搜索片段和 API 名称只用于发现资料。
4. 保存官方 URL、获取时间、原始正文、SHA-256、章节或符号定位，以及适用版本。抓取时间与哈希只能固定文档快照，不能自动证明系统版本。
5. 按节点组织相关正文段落和必要上下文；保留完整原文供回查，不把所有平台的整站正文一次性塞入上下文。
6. 生成的平台事实和跨平台差异关联证据。区分官方明示、基于证据的分析及尚未确认的推断；未检索到资料不能推出“不支持”。
7. 证据不足、相互冲突或版本不匹配的项保留 `unknown`/待研究，不用模型记忆补成确定结论，也不自动标记 `confirmed`。

上述要求已落实为 `AGENTS.md` 的研究规则，并配套 `scripts/official_docs.py` 的下载、检索、读取和上下文命令。工具提供的是候选资料与缺口，不是语义证据自动验收；现有知识生成维护脚本没有接入模型研究流水线。

## 实测文件

原始响应与 [核验清单](../docs-raw/source-probes/2026-09-05/manifest.json) 位于 `docs-raw/source-probes/2026-09-05/`。清单记录请求、HTTP 状态、内容类型、字节数和哈希。

HTTP 200 只证明传输成功。正文抽样另外核对了 Android 文章主体、Apple Markdown 内容、鸿蒙 API 的参数/权限/版本章节，以及目录响应的业务状态；尚未逐页验收所有目录目标。
