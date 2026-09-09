# 来源、范围与证据

资料发现入口见 [官方文档入口](../corpus/entrypoints.md)，读取命令见 [官方资料库](../corpus/guide.md)。`docs-raw/` 是来源库，不是已经完成的节点知识或锁定版本的 SDK 全集。

- 使用官方正文支持结论，不能用目录、检索摘要或历史文章代替正文。
- Android 系统 SDK、AndroidX 和生态服务分别记录依赖；Apple 文档逐项核对 iOS 适用性；OpenHarmony 与 HarmonyOS 发行版分开。
- 核对公开应用接口可见性。系统、隐藏或仅供设备厂商调用的接口不能归入普通应用能力。
- 来源保存官方 URL、章节/符号、获取时间、原文与哈希。快照哈希保证内容一致，不自动证明版本或解释正确。
- 结论记录 distribution、release、sdk、device_forms 和必要 conditions，与证据 applies_to 对齐。
- 新一轮开始时核实最新正式版；不把文档获取日期或接口 introduced 版本当作当前系统版本。
- 未找到资料时保留具体缺口；不支持、独有、等价结论需要核对相关官方框架与替代途径。

来源更新后应重新核对受影响的判断。结构化记录遵循 [比较模型](comparison-model.md)，置信度和真机需求遵循 [知识置信度](confidence.md)。
