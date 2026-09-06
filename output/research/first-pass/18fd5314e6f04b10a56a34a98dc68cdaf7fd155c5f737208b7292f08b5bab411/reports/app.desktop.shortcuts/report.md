# 桌面快捷方式 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

Android与HarmonyOS均读到明示的长按图标快捷方式机制：Android分静态/动态/固定三类，launcher最多同时显示4个静态+动态、设备上限各异、pinned无上限；HarmonyOS经shortcuts_config.json+module.json5 metadata静态配置，桌面最多展示4个，shortcutManager管理可见性，仅跳转UIAbility。iOS已读AppIntents App Shortcuts面向Shortcuts app/Siri/Spotlight，未见长按图标入口明示，仅算可能映射。三平台版本基线均未固定，结论全部low。提出3条差异假设：快捷方式类型与运行时能力、展示surface、数量上限机制。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 读到完整机制：静态(shortcuts.xml随APK打包)、动态(ShortcutManagerCompat运行时推送/更新/移除)、固定(API 26+ requestPinShortcut需用户确认)三类；仅主Activity可定义；大多数launcher最多同时显示4个静态+动态、设备上限不一、pinned无数量上限；长按图标查看、拖拽固定。 | recommended |
| ios | possible_mapping | indirect | 已读AppIntents App Shortcuts：代码定义AppShortcutsProvider静态快捷方式(app intent+标题/图像/口令短语)，安装即生效、无需自行注册，正文列出的surface为Shortcuts app、Siri、Spotlight等系统体验，另有SiriTipView/ShortcutsLink引导入口；已读正文未见主屏幕长按图标菜单展示快捷方式的明示。 | recommended |
| harmonyos | documented_mechanism | direct | 读到明示静态快捷方式机制：resources/base/profile/shortcuts_config.json(shortcutId≤63字节/label≤255字节/icon/wants含bundleName等目标与parameters)+module.json5 abilities的metadata(name固定ohos.ability.shortcuts)；长按图标打开入口，长按列表项可拖拽至桌面；桌面最多展示4个；shortcutManager可隐藏/展示；快捷方式仅跳转至具体UIAbility。 | recommended |

## android 条件与证据

适用范围：固定快捷方式需Android 8.0 (API 26)+，Support Library兼容API 25及以下；静态/动态最低API级别未在读文标明；启动日SDK/AndroidX基线未固定。
条件：仅主Activity(Intent.ACTION_MAIN+CATEGORY_LAUNCHER)可定义快捷方式；固定快捷方式需Android 8.0 (API 26)+，且用户经确认对话框授权；大多数launcher最多同时显示4个静态+动态；设备上限可用getMaxShortcutCountPerActivity()查询；launcher可访问快捷方式元数据，需隐藏敏感信息
缺口：静态/动态快捷方式最低API级别未在读文标明；启动日最新正式版SDK/AndroidX基线未固定；Google Shortcuts Integration Library等生态服务的版本与运行条件未核实
真机分类理由：展示上限、长按菜单与固定流程依赖具体launcher/设备实现且版本基线未固定，建议后续精研真机核验；非本轮必需。

- [App shortcuts overview](https://developer.android.com/develop/ui/compose/system/shortcuts)，Note: Only main activities can have shortcuts，正文 30–33 行；获取 2026-09-05T10:25:34.793195+00:00；SHA 7cc91ed559d09c75d0a4271fd164c2ceaeedcffdc6c3917bfb489373a6a95be6。
- [App shortcuts overview](https://developer.android.com/develop/ui/compose/system/shortcuts)，Shortcut types: static/dynamic/pinned，正文 35–42 行；获取 2026-09-05T10:25:34.793195+00:00；SHA 7cc91ed559d09c75d0a4271fd164c2ceaeedcffdc6c3917bfb489373a6a95be6。
- [App shortcuts overview](https://developer.android.com/develop/ui/compose/system/shortcuts)，Shortcut limitations: 4 shown, per-device max, pinned unlimited，正文 53–67 行；获取 2026-09-05T10:25:34.793195+00:00；SHA 7cc91ed559d09c75d0a4271fd164c2ceaeedcffdc6c3917bfb489373a6a95be6。
- [Create shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/creating-shortcuts)，Dynamic shortcuts: ShortcutManagerCompat push/remove，正文 189–203 行；获取 2026-09-05T10:45:05.453630+00:00；SHA 13666428f990fa67c0de01cd6470ddb1d01328936e81c48f8c4ea1678ee076b3。
- [Create shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/creating-shortcuts)，Pinned shortcuts require Android 8.0 (API 26)+ and user confirmation，正文 288–298 行；获取 2026-09-05T10:45:05.453630+00:00；SHA 13666428f990fa67c0de01cd6470ddb1d01328936e81c48f8c4ea1678ee076b3。

## ios 条件与证据

适用范围：已读正文未标注最低iOS版本与平台可用性；Apple目录含多平台，iOS适用性需逐符号核对；版本基线未固定。
条件：以代码定义AppShortcutsProvider，编译器生成系统所需信息；安装后即可用，无需自行注册；正文列出的surface为Shortcuts app、Siri、Spotlight等系统体验
缺口：长按主屏幕图标菜单是否展示App Shortcuts未读到正文证据，与节点定义的映射待确认；iOS最低版本与符号级availability未核对；运行时动态增改快捷方式的能力未在读文范围
真机分类理由：App Shortcuts在Siri/Spotlight/Shortcuts app及可能的长按菜单中的实际呈现需真机核对，且已读正文无版本信息；非本轮必需。

- [App Shortcuts](https://developer.apple.com/documentation/appintents/app-shortcuts)，Overview: App Shortcuts in Shortcuts app and system experiences, AppShortcutsProvider，正文 5–24 行；获取 2026-09-05T10:17:04.504685+00:00；SHA 9375f5abe168d01e9dca5ece666adfa323210d7e9d54141d3b2a597b37adff94。
- [App Shortcuts](https://developer.apple.com/documentation/appintents/app-shortcuts)，SiriTipView/ShortcutsLink make shortcuts available from your app，正文 30–33 行；获取 2026-09-05T10:17:04.504685+00:00；SHA 9375f5abe168d01e9dca5ece666adfa323210d7e9d54141d3b2a597b37adff94。
- [Adding Shortcuts for Wind Down](https://developer.apple.com/documentation/sirikit/adding-shortcuts-for-wind-down)，Wind Down sample: shortcuts visible in Health app，正文 5–13 行；获取 2026-09-05T10:25:47.519549+00:00；SHA 998d215b4b78a180de73dc4263343e63aff1533a0d0206674986066a9bab8af7。

## harmonyos 条件与证据

适用范围：华为官网HarmonyOS开发指南与最佳实践(2026-09-05快照)；正文未标明适用API/SDK起始版本，OpenHarmony与HarmonyOS发行版适用性未区分；基线未固定。
条件：静态配置：shortcuts_config.json+module.json5 metadata(ohos.ability.shortcuts)；长按应用图标打开快捷方式入口；长按列表项可拖拽至桌面；桌面展示快捷方式数量有上限，最多4个；快捷方式只允许跳转至具体UIAbility，无法直接跳转非入口页面
缺口：适用API/SDK起始版本未在读文标明；shortcutManager模块完整能力未读正文，仅链接引用；是否存在动态/固定类快捷方式未确认；OpenHarmony与HarmonyOS发行版适用性未区分
真机分类理由：长按入口、拖拽桌面与最多4个上限的实际表现依赖设备桌面实现且版本基线未固定，建议精研时真机核验；非本轮必需。

- [桌面快捷方式](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-desktop-shortcuts)，快捷方式启动方式：点击入口列表项、长按拖拽至桌面，正文 11–18 行；获取 2026-09-05T10:40:26.358004+00:00；SHA 49ed223a7ecee52779779c80650ab5e90104e6b7ba63c04d41c2d02ae694504f。
- [桌面快捷方式](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-desktop-shortcuts)，shortcuts标签配置：shortcutId/label/icon/wants，正文 24–38 行；获取 2026-09-05T10:40:26.358004+00:00；SHA 49ed223a7ecee52779779c80650ab5e90104e6b7ba63c04d41c2d02ae694504f。
- [桌面快捷方式](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-desktop-shortcuts)，快捷方式只允许跳转至具体UIAbility，正文 40–40 行；获取 2026-09-05T10:40:26.358004+00:00；SHA 49ed223a7ecee52779779c80650ab5e90104e6b7ba63c04d41c2d02ae694504f。
- [创建应用静态快捷方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/typical-scenario-configuration)，桌面展示快捷方式数量上限：最多展示4个，正文 9–9 行；获取 2026-09-05T10:24:47.845301+00:00；SHA c67d9d99a929883d502a6b87389b5583b01bd75030d36dd93b0844ee6132eab0。
- [创建应用静态快捷方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/typical-scenario-configuration)，module.json5配置metadata(ohos.ability.shortcuts)及长按图标展示效果，正文 83–97 行；获取 2026-09-05T10:24:47.845301+00:00；SHA c67d9d99a929883d502a6b87389b5583b01bd75030d36dd93b0844ee6132eab0。
- [创建应用静态快捷方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/typical-scenario-configuration)，setShortcutVisibleForSelf隐藏或展示快捷方式，正文 100–102 行；获取 2026-09-05T10:24:47.845301+00:00；SHA c67d9d99a929883d502a6b87389b5583b01bd75030d36dd93b0844ee6132eab0。

## 待验证差异假设

- programming_model：快捷方式类型与运行时能力可能不同：Android读到静态/动态/固定三类，动态类可运行时推送、更新、移除；HarmonyOS已读文档仅覆盖静态配置与shortcutManager可见性管理；iOS App Shortcuts为代码静态声明(编译期生成、安装即用)。是否支持运行时动态变更是待确认差异。；待核：HarmonyOS shortcutManager模块是否支持运行时新增/更新快捷方式；iOS App Shortcuts是否可运行时变更(已读正文称static data定义)；各能力的最低版本条件。
- availability：快捷方式展示surface可能不同：Android为受支持的launcher及assistant；iOS App Shortcuts正文列出Shortcuts app、Siri、Spotlight等系统体验，未明示主屏幕长按图标菜单；HarmonyOS明示长按图标打开入口并支持拖拽至桌面成独立图标。；待核：iOS主屏幕长按图标菜单是否列出App Shortcuts(未读到正文证据)；Android assistant surface的适用条件与Google服务依赖。
- limits_precision：数量上限机制可能不同：Android大多数launcher最多同时显示4个静态+动态快捷方式，但设备上限各异、需getMaxShortcutCountPerActivity()查询，pinned无数量上限；HarmonyOS文档明示桌面最多展示4个。；待核：HarmonyOS的4个上限是否可经接口查询或因桌面实现而异；HarmonyOS拖拽至桌面的快捷方式数量上限未读到。

范围缺口：iOS App Shortcuts与本节点'长按图标/系统菜单深链入口'的对应关系未建立，需主屏幕长按菜单行为与符号级iOS availability证据；三平台启动日最新正式版与手机基线均未固定，版本适用性结论全部待核；ShortcutManager(Android)/shortcutManager(HarmonyOS)/AppShortcutsProvider(iOS)的API参考正文未纳入本轮冻结sources，接口细节未读；动态/固定类快捷方式在HarmonyOS的存在性与iOS运行时变更能力未确认

后续优先级：P1；iOS侧映射未建立(possible_mapping、间接证据、surface语义与节点定义不符风险高)，且三平台版本基线未固定、快捷方式类型与数量上限机制可能存在高风险差异，属关键缺口，需优先精研。

逐条引用及原文摘录见同目录 normalized.json。
