# 原始目录与能力映射

每个平台唯一的源目录是 catalog.json。unmapped/ 为生成的待确认清单，不进入统计分母。

scope 表示 included / excluded / pending，scope_reason 说明原因。visibility 独立表示 public / system 等访问属性。source 记录本地来源、哈希和发行版，未固定 SDK 的镜像明确标记 version_pinned: false。

mappings 是多对多关联数组。relationship 分 catalog（目录归类）与 capability（任务能力关联）；verification 分 candidate 与 confirmed。规则只生成候选。人工确认需要 method: manual、rationale、evidence_url、verified_by、verified_at。

允许将大目录候选挂到父节点，但不计作能力确认完成。未知项保留待处理，不强制兜底 runtime。完整反向索引直接合并 catalog 映射和节点精选绑定，保留来源，数量不截断。

```bash
.venv/bin/python scripts/harvest_inventory_from_docs.py
.venv/bin/python scripts/map_inventory_to_taxonomy.py
.venv/bin/python scripts/refresh.py
```

见 mapping_summary.json 获取范围、候选关联及确认数量。它不是特性树语义完备率，也不是节点差异确认率。
