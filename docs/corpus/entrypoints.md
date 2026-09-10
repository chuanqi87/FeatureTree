# 来源入口

- 原文：docs-raw/official/corpus.sqlite 与其 snapshots。原文库继续保存，导入只记录身份/路径/哈希，不复制约 2.8 GB 正文。
- 来源快照：data/sources/<snapshot_id>，声明、符号族、目录与正文索引分别为 JSONL；manifest.json 记录清单与哈希。
- 查询：sources query --snapshot ID --query TEXT --platform PLATFORM；HTTP /api/v2/apis、topics、documents 固定 snapshot_id 并分页。
- Agent：仅 source_catalog 工具。平台阶段只拿本端清单；对齐和设计共享三端资料；分页与正文窗口均留记录。
- 完整枚举：ApiCatalog.enumerate_records 读取并验证封存 JSONL，不用 SQLite 缓存作为覆盖分母。

详细导入、SDK 提取和缺口说明见 guide.md。来源事实不因候选分析成功自动成为正式基线。
