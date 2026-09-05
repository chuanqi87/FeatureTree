# 每个节点如何填写和确认差异

每条支持、事实和差异还需独立记录 [知识置信度与真机复核](knowledge-confidence.md)。confirmed 必须有有效的 assessment；高可信不是已实测，正文状态不代替评级。按分级选择复核范围可使用 `scripts/export_review_scope.py` 或特性树筛选栏。

每个节点对应一份 knowledge 文件。正式支持记录放在 presence，正式比较放在 comparisons；原有正文用于解释，legacy_presence 只保留历史断言。浏览视图将它们通过 feature_id 附着到节点。

## 状态

| 字段 | 取值 | 含义 |
| --- | --- | --- |
| presence.status | unknown | 还不能判断支持情况 |
| presence.status | supported | 在声明范围与上下文内满足任务 |
| presence.status | conditional | 仅在明确条件下满足，确认时必须填写 conditions |
| presence.status | unsupported | 在指定范围和上下文中不提供，有明确证据 |
| comparisons.result | unknown / same / different / not_applicable | 某维度、某平台对的判断 |
| verification | unreviewed / in_review / confirmed | 尚未核实 / 核实中 / 已确认 |
| status（文章级） | stub / draft / reviewed | 编辑状态，不代替上述确认 |

暂时找不到 API 时使用 unknown。核实中的 supported、different 仍是候选判断；导出时始终同时显示 verification。

## 开始核实

先检查 taxonomy 节点的 definition 和 comparison_scope。明确任务边界后，在知识记录中补平台条件与差异说明。每条比较对应一个维度与一个无序平台对，反向重复会失败；没有写出的维度和平台对自动显示为待确认。

以下是仓库中 BLE 扫描过滤记录的结构示例（节选）：

```yaml
presence:
  android:
    status: unknown
    verification: in_review
  ios:
    status: unknown
    verification: in_review
  harmonyos:
    status: unknown
    verification: unreviewed
comparisons:
- dimension: api_surface
  platforms: [android, ios]
  result: different
  verification: in_review
  scope: 扫描过滤条件与执行位置
  rationale: 历史资料提示存在差异，需固定 SDK、设备与扫描模式后核实。
  evidence_refs: [android-1, ios-2]
```

这里的 different 是待核实判断。它不会被统计成“已确认存在差异”。

## 确认为 confirmed 前

| 所在位置 | 必填内容 |
| --- | --- |
| presence.context（涉及的每个平台） | release、sdk、distribution、device_forms，必要时 conditions |
| 判断记录 | rationale、evidence_refs、verified_by、verified_at、subject_hash |
| 比较记录 | 另需明确 scope；双方都须有证据 |
| 每份引用证据 | id、platform、title、url、locator、固定 revision、applies_to |
| 本地证据 | local_path、sha256，且文件哈希保持一致 |

evidence.applies_to 必须与对应 presence.context 一致，防止把其他 SDK、发行版或设备条件下的资料套用到当前结论。revision 记录所使用文档的固定版本或不可变修订，不能填写 master/latest/API 12+ 等漂移范围。

subject_hash 是当前节点定义、包含/排除范围、维度、设备范围、层级类型和隐私分类的指纹，可在生成的 output/exports/tree.json 对应节点中取得。只在审核完当前范围后把它填入确认记录。语义范围变化会使旧确认失效；仅移动导航位置不会改变指纹。

确认记录还须填写 `basis: official_statement`（官方明示）或 `basis: evidence_based_analysis`（基于证据的分析）。unsupported、same、not_applicable 另需 `coverage_note`，写清已经检查的范围和替代路径。比较记录可用 `missing_requirements` 保留具体缺口。

确认引用的每份证据必须有 `local_path`、`sha256`、`fetched_at`（带时区的 ISO 时间）、`excerpt`（相关正文原文）、`source_kind`（api_reference / developer_guide / release_notes / official_support）和 `applicability_note`（版本与设备的官方适用依据）。摘录必须能在哈希一致的本地正文中找到，不能使用生成的解释冒充原文。revision 可用固定文档修订或内容快照标识，但仍必须另外核实 applies_to；快照时间和哈希不证明 SDK 适用性。

新增关键平台事实可记录在 `facts`：每项包含唯一 id、platform、dimension、statement、basis、verification、evidence_refs。confirmed 事实还需 rationale、verified_by、verified_at、subject_hash，并通过与支持/比较相同的来源校验。旧的自由正文不自动成为已确认事实。

已确认的 unknown 不合法。conditional 需要明确条件。same 也需要双方证据。not_applicable 必须说明本维度为何对该平台对不适用，不能用来跳过尚未调查的内容。

一次比较采用节点当前声明的版本上下文。更换版本后重新核实相关支持与差异；原有版本说明可保留在正文中，不自动继承旧结论。

## 父节点与完成度

父节点可以比较自己的整体范围和跨子能力模型，不自动继承子节点结论；也不能将父节点结论扩散到所有后代。每节点可按 comparison_dimensions 选取适用维度，选择本身应有能力语义依据。

- 已确认任意一项 different：conclusion 显示 has_confirmed_differences，仍保留未完成数量。
- 所有平台支持和全部适用比较均确认，且没有 different：才能显示 confirmed_same。
- 所有比较均明确不适用：显示 not_applicable。
- 其他情况：unknown，配合 not_started / in_progress 状态。

编辑后运行 scripts/refresh.py。结构通过仅说明契约有效；--require-complete 额外要求所选节点的平台支持和全部比较项确认完毕。
