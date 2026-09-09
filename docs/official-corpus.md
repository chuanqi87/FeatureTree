# 官方资料库

`docs-raw/official/` 保存已有官方正文、原始响应、目录与 SQLite 全文索引，可继续复用。下载状态不是能力覆盖率，也不是知识确认进度。

## 查找与阅读

```bash
.venv/bin/python scripts/official_docs.py search 'Bluetooth scan filter' --platform android
.venv/bin/python scripts/official_docs.py search '蓝牙扫描' --platform harmonyos
.venv/bin/python scripts/official_docs.py locate 'PeriodicWorkRequest' --platform android
.venv/bin/python scripts/official_docs.py fetch 'https://developer.android.com/reference/androidx/work/PeriodicWorkRequest'
.venv/bin/python scripts/official_docs.py read 'https://developer.android.com/reference/androidx/work/PeriodicWorkRequest' --start-line 1 --lines 100
.venv/bin/python scripts/official_docs.py context connectivity --limit 5
```

`context` 只针对当前存在的节点生成候选资料，不生成平台结论。节点细化后使用对应新 ID。候选包按需写入 `output/contexts/`，可删除重建。

阅读时核对正文、具体版本、发行版、设备与调用条件。查看 `binding_source_gaps`，按需补抓缺失正文。检索片段不能代替引用的完整章节。

## 状态与维护

```bash
.venv/bin/python scripts/official_docs.py status
.venv/bin/python scripts/official_docs.py audit --verify-files
.venv/bin/python scripts/official_docs.py catalogs
.venv/bin/python scripts/official_docs.py seed
.venv/bin/python scripts/official_docs.py crawl --workers 6 --max-priority 40 --limit 100
```

- `ready`：存在可检索正文；`thin` / `partial`：正文或转换不完整，需要继续查读。
- `pending`：待获取；`failed` / `blocked`：获取失败或访问受限；`not_found`：此次请求未找到正文，不代表平台无该能力。
- `catalogs/` 保存目录快照，`snapshots/` 保存原始响应、正文及元数据，`corpus.sqlite` 保存索引与下载状态。
- `audit` 报告按需生成到 `output/reports/official-documents/`，不保留旧报告作为当前研究结论。

用 `fetch URL --refresh` 更新具体来源。迁移资料库时整体复制数据库、catalogs 和 snapshots，再验文件哈希；不能只复制数据库。

证据采用规则见 [sources.md](sources.md)，知识研究见 [research-runbook.md](research-runbook.md)。
