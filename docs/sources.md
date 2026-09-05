# 采集范围、证据与版本

三平台官方知识库、目录与正文读取入口，以及 2026-09-05 的实测结果，见 [官方文档入口与生产使用规则](official-documentation-entrypoints.md)。

新增的官方正文下载、离线检索、缺失资料补抓和逐节点上下文准备，见 [官方资料库使用说明](official-corpus.md)。其覆盖与错误单独记录在 [资料验收报告](../output/reports/official-documents/progress.md)；下述 inventory 仍是原有目录与映射层，不等同于新增全文库。

## 当前资料状态

现有 docs-raw 是本地文档镜像，不是已经锁定版本的三平台 SDK 全集。每条 inventory 保存来源路径、SHA-256、发行版说明及 version_pinned。

| 来源 | 可以证明 | 尚不能据此确认 |
| --- | --- | --- |
| Android packages 索引与 guide 链接 | 镜像包含这些目录和文档入口 | 它们完整对应某个 API Level；GMS/Jetpack 已全覆盖 |
| Apple 文档目录与部分落地页 | 文档存在；部分落地页声明 iOS 适用 | Apple 所有目录都适用于 iOS；全部内容属于 iOS 18 |
| OpenHarmony Kit Readme 与模块正文 | 指定镜像中的目录、符号和说明 | HarmonyOS 指定发行版/SDK 的实现和可见性 |

旧知识 baseline 原样保留为历史/计划说明，正式确认使用 presence.context 与 evidence.applies_to。旧 BOM 示意值、API 12+、master 等不再作为已固定基线。

## 确认所需信息

每个平台填写发行版 distribution、系统 release、sdk、device_forms 和必要 conditions。证据填写 URL、具体章节或符号 locator、固定 revision、适用上下文 applies_to。确认者与日期记录在判断上。

本地证据使用 local_path + sha256；文件变化触发审计失败，提醒重新核对。哈希不自动说明 SDK 版本。固定版本依据与上下文不一致时不能确认；升级 SDK 必须重新核实受影响结论。

## 范围与可见性

- scope: included 表示纳入本轮目录研究；pending 表示尚待确认范围；excluded 必须说明原因。
- visibility 独立描述访问属性，系统接口和隐藏接口不得以 public 身份纳入。
- 纯语言基础库和测试专用目录按本期规则排除。
- Apple 无落地页适用性证据的目录保留 pending，不伪标 duplicate。
- Android 系统 SDK、生态服务、OpenHarmony/HarmonyOS 发行版分开记录上下文，不能靠根节点 layer 得出结论。

采集来自部分目录镜像，included 仍需核实具体 API 级可见性和版本。采集覆盖与能力确认分别计数。

## 更新流程

```bash
.venv/bin/python scripts/harvest_inventory_from_docs.py
.venv/bin/python scripts/map_inventory_to_taxonomy.py
.venv/bin/python scripts/refresh.py
```

人工范围决定填写 scope_method: manual；人工映射填写 method: manual。重采集与规则刷新保留这些决定。镜像中消失的记录保留为范围待定项，不静默删除。
