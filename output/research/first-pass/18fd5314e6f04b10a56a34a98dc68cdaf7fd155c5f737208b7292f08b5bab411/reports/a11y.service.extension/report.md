# 无障碍服务扩展 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台文档初判：Android（Android 11 行为变更）证实应用可实现无障碍服务并以 AccessibilityServiceInfo flags 与服务元数据文件声明，但观察/操作界面能力正文未读到；HarmonyOS 明示 AccessibilityExtensionAbility 允许三方应用实现、支持访问与操作前台界面，并给出 capabilities 与 Action 能力模型；iOS 冻结资料（BrowserEngineKit、Safari 16 说明）未涉及该机制，保持 unknown。全部 low 置信，基线未固定。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | indirect | 行为变更文档证实应用侧无障碍服务机制：应用可实现 accessibility service，经 AccessibilityServiceInfo 与服务元数据文件声明能力；Android 11 起不能运行时声明与系统无障碍按钮的关联，须在元数据文件配置 flagRequestAccessibilityButton。观察/操作界面能力正文未读到。 | recommended |
| ios | unknown | missing | 两篇冻结资料均不涉及本节点：BrowserEngineKit 的 Accessibility 主题仅是浏览器引擎扩展进程的无障碍符号（BEAccessibility 系列，区域受限 entitlement 场景）；Safari 16 说明仅提及 VoiceOver Isolated Tree Mode。未读到 iOS 应用作为无障碍服务观察操作界面的机制。 | unassessed |
| harmonyos | documented_mechanism | direct | ExtensionAbility 总览明示 AccessibilityExtensionAbility 为无障碍服务扩展能力，支持访问与操作前台界面，允许三方应用实现；@ohos.accessibility 提供辅助应用信息（capabilities 含 retrieve/gesture）、目标动作（click/setText/home 等）、事件类型与扩展列表查询。 | recommended |

## android 条件与证据

适用范围：所读为 Android 11（API 30）行为变更文档，适用 targetSdkVersion 30+；服务机制本体的 API Level 范围冻结资料未覆盖，启动日最新正式版未核实。
条件：行为变更仅适用 targetSdkVersion 30+（Android 11）的应用；无障碍按钮关联须在服务元数据文件（如 res/raw/accessibilityservice.xml）的 accessibilityFlags 中声明 flagRequestAccessibilityButton；运行时向 AccessibilityServiceInfo.flags 追加 FLAG_REQUEST_ACCESSIBILITY_BUTTON 不再获得按钮回调事件
缺口：缺少 AccessibilityService API 参考与无障碍服务开发指南正文：节点树观察、动作执行、手势注入等观察/操作能力未读到；未核实启动日最新 Android 正式版对无障碍服务的限制变化（基线未固定）；android-2（develop/ui）为导航页，仅含'支持无障碍'链接，无本节点正文证据
真机分类理由：应用作为无障碍服务跨应用观察/操作界面属高风险能力，冻结资料未覆盖实际观察与操作行为；正式结论需真机验证服务启用流程与操作效果。

- [Behavior changes: Apps targeting Android 11](https://developer.android.com/about/versions/11/behavior-changes-11)，Behavior changes: Apps targeting Android 11 > 引言（targetSdkVersion 30 适用范围），正文 3–7 行；获取 2026-09-05T10:21:36.232005+00:00；SHA a501b44fc076374d699dca76ade48a53387ff3556b8a4153518ee0bebbfaa61e。
- [Behavior changes: Apps targeting Android 11](https://developer.android.com/about/versions/11/behavior-changes-11)，Behavior changes: Apps targeting Android 11 > Accessibility > Declare accessibility button usage in metadata file，正文 184–197 行；获取 2026-09-05T10:21:36.232005+00:00；SHA a501b44fc076374d699dca76ade48a53387ff3556b8a4153518ee0bebbfaa61e。
- [ui](https://developer.android.com/develop/ui)，ui 页 > Support accessibility 导航链接（仅导航，无服务机制正文），正文 68–72 行；获取 2026-09-05T10:15:52.494948+00:00；SHA 73e39935372a754100e6ae7cf3c003644b739b71f5b54c41d78f384dec907417。

## ios 条件与证据

适用范围：Safari 16 发行说明标注 2022-09-12 发布（随 iOS 16 提供）；BrowserEngineKit 快照未含符号级 availability 核对；两篇均与本节点无直接版本关系。
条件：未读到本节点相关机制的适用条件；冻结资料中 BrowserEngineKit 能力面向替代浏览器引擎场景，且按区域（欧盟/日本）需申请 entitlement
缺口：冻结资料无 iOS 应用作为无障碍服务观察/操作其他应用界面的机制文档，不能判断支持与否；未检索 Apple 辅助技术相关框架文档（如 UIAccessibility 及辅助应用类主题）是否提供或明确禁止该能力；两篇资料分别面向浏览器引擎扩展与 WebKit 发行说明，与节点定义无直接关联
真机分类理由：冻结资料未提供任何机制文档，无法定义待验证行为；需先补充 Apple 官方资料调查后再评估真机需求。

- [BrowserEngineKit](https://developer.apple.com/documentation/browserenginekit)，BrowserEngineKit > Develop by region（替代浏览器引擎按区域申请 entitlement），正文 43–46 行；获取 2026-09-05T10:30:01.358391+00:00；SHA 5e6d43754a4f8f42649df6fe93d52a97e3dffdf062ab270b5bf3a26f3334507c。
- [BrowserEngineKit](https://developer.apple.com/documentation/browserenginekit)，BrowserEngineKit > Topics > Accessibility（BEAccessibility 系列符号，面向浏览器引擎扩展），正文 120–128 行；获取 2026-09-05T10:30:01.358391+00:00；SHA 5e6d43754a4f8f42649df6fe93d52a97e3dffdf062ab270b5bf3a26f3334507c。
- [Safari 16 Release Notes](https://developer.apple.com/documentation/safari-release-notes/safari-16-release-notes)，Safari 16 Release Notes > Accessibility > New Features（VoiceOver Isolated Tree Mode），正文 56–61 行；获取 2026-09-05T10:25:20.847973+00:00；SHA e7fd915e97522fadf1eeacfbcb727faaab5eef9cae8f8bae7211ca3533eca88f。

## harmonyos 条件与证据

适用范围：华为 harmonyos-references/guides 在线文档快照：@ohos.accessibility 首批接口 API 7 起，多数条目 9+/12+，injectAction/executeCustomAction 标注起始版本 26.0.0；ExtensionAbility 总览未标注该类型起始 API 版本，HarmonyOS 发行版基线未固定。
条件：ExtensionAbility 类型由系统定义并由相应系统服务统一管理，开发者不能直接继承 ExtensionAbility 基类，只能实现已定义类型；ExtensionAbility 组件不能被应用直接启动，由相应系统管理服务拉起并管理生命周期；能力通过 capabilities 声明：retrieve/touchGuide/keyEventObserver/zoom/gesture，其中 zoom 标注当前版本暂不支持；辅助应用状态分 enable/disable/install；动作与接口分版本标注（9+/12+/26.0.0），需按版本核对可用性
缺口：AccessibilityExtensionAbility 专属 API 参考正文（生命周期回调、事件接收、具体操作接口）未在冻结资料中；辅助应用的启用流程与用户同意/权限机制在已读段落未覆盖；总览表未标注该类型起始 API 版本；与 HarmonyOS 商业发行版的对应关系未核实；所读为华为官方文档，OpenHarmony 发行版差异未单独核对
真机分类理由：官方明示三方应用可实现并访问/操作前台界面，实际跨应用行为、启用流程与运行限制需真机确认后方可形成正式结论。

- [ExtensionAbility组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)，ExtensionAbility组件 > 引言（类型由系统定义、系统服务统一管理、不能直接继承），正文 3–5 行；获取 2026-09-04T09:35:09+00:00；SHA d8486a77883f70af10fde21445db5421ce7959ddbe2b5d1988c01f1b1b2176d0。
- [ExtensionAbility组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)，ExtensionAbility类型说明表 > AccessibilityExtensionAbility 行（无障碍服务扩展能力，支持访问与操作前台界面，允许三方应用实现），正文 14–20 行；获取 2026-09-04T09:35:09+00:00；SHA d8486a77883f70af10fde21445db5421ce7959ddbe2b5d1988c01f1b1b2176d0。
- [ExtensionAbility组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)，访问指定类型的ExtensionAbility组件（不能被应用直接启动，由系统管理服务拉起），正文 60–64 行；获取 2026-09-04T09:35:09+00:00；SHA d8486a77883f70af10fde21445db5421ce7959ddbe2b5d1988c01f1b1b2176d0。
- [@ohos.accessibility (辅助功能)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility)，@ohos.accessibility > 模块说明（首批接口从 API version 7 开始支持），正文 5–5 行；获取 2026-09-05T10:26:36.716236+00:00；SHA 4ec6b7954f14905638c64308e8d4fc3425c97797380dc4bfd6ffa91d27c0ec38。
- [@ohos.accessibility (辅助功能)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility)，@ohos.accessibility > AccessibilityAbilityInfo（capabilities/eventTypes/targetBundleNames 等属性），正文 52–75 行；获取 2026-09-05T10:26:36.716236+00:00；SHA 4ec6b7954f14905638c64308e8d4fc3425c97797380dc4bfd6ffa91d27c0ec38。
- [@ohos.accessibility (辅助功能)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility)，@ohos.accessibility > Action 值表（common/home/back 等 12+，injectAction/executeCustomAction 起始版本 26.0.0）与 Capability（retrieve/gesture 等），正文 113–141 行；获取 2026-09-05T10:26:36.716236+00:00；SHA 4ec6b7954f14905638c64308e8d4fc3425c97797380dc4bfd6ffa91d27c0ec38。

## 待验证差异假设

- programming_model：应用侧无障碍服务的能力声明载体可能不同：Android 以 AccessibilityServiceInfo flags 加服务元数据文件声明（Android 11 起按钮关联仅元数据声明有效）；HarmonyOS 以辅助应用信息中的 capabilities/abilityTypes/eventTypes 列表声明。；待核：Android AccessibilityServiceInfo flags 全集与 HarmonyOS capabilities 的语义对应关系未读；双方声明载体的具体结构（res/raw XML 与应用配置文件）差异需读双方指南确认；运行时能否变更能力声明双方均未确认。
- api_surface：HarmonyOS 文档枚举了辅助应用可执行的目标动作集合（click/longClick/setText/setCursorPosition/home/back 等，部分 12+，injectAction/executeCustomAction 标注 26.0.0 起）；Android 冻结资料仅覆盖无障碍按钮回调，未覆盖服务可执行动作集合，双方操作能力范围与版本起点差异待查。；待核：Android 服务端动作/手势 API（如 performAction、手势注入）正文未读到，无法对齐枚举比较；HarmonyOS 各动作实际生效条件与 targetBundleNames 过滤行为未验证。

范围缺口：iOS 平台本节点机制在冻结资料中完全缺失，为关键缺口，无法初判支持与否；Android 观察与操作界面的能力正文（AccessibilityService API 参考/服务指南）未读到；HarmonyOS AccessibilityExtensionAbility 专属参考文档与启用/权限流程未读；三平台启动日最新正式版与手机基线未固定（version_baseline unresolved），所有结论仅基于冻结快照

后续优先级：P1；iOS 无任何本节点证据、Android 核心观察/操作能力正文缺失，且节点涉及跨应用观察/操作界面的高风险映射；需优先补源并精研。

逐条引用及原文摘录见同目录 normalized.json。
