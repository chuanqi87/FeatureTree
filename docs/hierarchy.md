# 层级语义与稳定 ID

树用父子关系表达能力分类和细分。L1、L2 等只表示实际深度；没有终止层数上限。同组兄弟节点使用一致的切分轴，横切内容用引用连接。

节点 definition 与 comparison_scope 定义“比较什么”。knowledge_role 的 leaf / rollup 表达其是否有子节点，二者都可以维护平台支持与差异记录。父节点不必等待所有子节点完成后才开始比较自己的范围。

所有节点都有 knowledge_path。生成的 output/exports/tree.json 将节点、平台支持、子节点和进度合并成可浏览视图。

已存在的 ID 保留，以免破坏引用；它不要求永久等于当前导航路径。graphics.2d 等历史数字段被 Schema 正式支持。部分历史 ID 含平台机制词，本次通过中立名称与定义修正含义并保留 aliases。新 ID 优先用稳定能力术语。

layer、device_forms、privacy_class 是导航提示，不能据此推断某平台的服务来源、实际设备支持或权限结论。正式运行上下文放在对应平台的 presence.context。

修改 parent 时更新 level 和显式 child_index；审计检查环、深度、角色及索引一致性。节点定义变化时同步 knowledge.definition，原知识需按新范围复核。
