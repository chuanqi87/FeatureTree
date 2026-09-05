# 本地文档镜像

这里保存目录页、链接列表及部分正文。镜像是资料来源，尚不等于固定版本的公开 SDK 全集。

- Android：packages 索引、guide 链接及部分正文。
- Apple：文档目录、framework-roots 与部分框架落地页。
- OpenHarmony：52 个 Kit Readme 与关键模块正文；需要进一步核对 HarmonyOS 发行版。
- 华为站介绍页：部分有效正文、部分站点壳页，不能只凭 URL 确认能力。

采集条目会记录具体来源路径和 SHA-256。知识确认另外要求明确版本、章节/符号与平台运行上下文，详见 [证据契约](../docs/sources.md)。

更新镜像后运行 harvest_inventory_from_docs.py、map_inventory_to_taxonomy.py、refresh.py。来源变化若影响现有证据哈希，需重新核实对应结论。
