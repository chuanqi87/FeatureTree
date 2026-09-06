# 分析事件 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到自定义事件采集官方机制：Android/iOS 为 Firebase Analytics logEvent（500 种事件类型上限、名称区分大小写、控制台报表），HarmonyOS 为系统级 hiAppEvent.write+addWatcher（domain/name/参数规格受限、本地存储订阅）。上传侧 Firebase 有控制台与调试日志证据，HarmonyOS 冻结来源未覆盖云端上报，生态对位服务未核实；全部 low 置信，基线未固定。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | Firebase Analytics 生态服务：FirebaseAnalytics.logEvent() 记录自定义事件，另有推荐事件常量与 setDefaultEventParameters；每应用最多 500 种事件类型、总量不限、名称区分大小写（C++ SDK 文档同载 500 上限）；自定义参数注册后入报表并可随 BigQuery 导出；adb verbose 日志与控制台面板可验证。 | recommended |
| ios | documented_mechanism | direct | Firebase Analytics for iOS+：配置 FirebaseApp 实例后用 Analytics.logEvent()（Swift/ObjC）记录自定义事件，机制与 Android 对应：500 种事件类型上限、名称区分大小写、默认参数与控制台注册；SPM 集成，可选含/不含 IDFA 采集的分析库并关联 ATT；Xcode 调试参数与控制台可验证。 | recommended |
| harmonyos | documented_mechanism | direct | 系统级 @ohos.hiviewdfx.hiAppEvent（PerformanceAnalysisKit，API 9 首批）：write() 写入自定义应用事件（domain+name+eventType+params；域≤32 字符、名≤48、参数名≤32、string 值≤8*1024、参数≤32 个），addWatcher 订阅消费，configure 可关闭打点并设存储配额（默认 10MB）；冻结来源未覆盖云端上传。 | recommended |

## android 条件与证据

适用范围：Firebase Android SDK（Google 生态服务，非系统 SDK）；冻结正文未标注 SDK/BOM 版本与最低 API Level（version_verified=false），未核对启动日最新正式版
条件：需先完成 Firebase 项目接入并启用 Analytics（Before you begin 指向 Get Started）；能力属 Firebase 生态 SDK 而非 Android 系统 SDK，设备/服务运行条件正文未展开；自定义参数需在 Firebase 控制台注册后才出现在报表；即时验证依赖 adb verbose 日志，控制台面板为周期性更新
缺口：未读取 get-started 与 logEvent API 参考正文，SDK 版本/最低 API Level 未核实；500 类型上限之外的服务侧限制（参数个数/长度等）冻结正文未说明；上传时机、离线缓存、批量/频率与后台约束未覆盖；启动日最新正式版基线未固定，不声称已核实最新版本
真机分类理由：采集接口有静态文档，但上传时机、离线缓存、控制台可见性与 500 上限的实际执行需真机与服务端验证；首轮未做实测

- [Log events](https://firebase.google.com/docs/analytics/android/events)，Log events 开头：500 种事件类型上限、总量不限、名称区分大小写，正文 10–16 行；获取 2026-09-05T10:51:08.931872+00:00；SHA cac19cabfd81a4adb7e08bd633d76dacfa9dc8319a51a0a4ac05c50b5f879ba4。
- [Log events](https://firebase.google.com/docs/analytics/android/events)，Before you begin / Log events：FirebaseAnalytics 实例与 logEvent() 方法、推荐事件，正文 18–29 行；获取 2026-09-05T10:51:08.931872+00:00；SHA cac19cabfd81a4adb7e08bd633d76dacfa9dc8319a51a0a4ac05c50b5f879ba4。
- [Log events](https://firebase.google.com/docs/analytics/android/events)，自定义参数作为维度/指标、控制台注册、BigQuery 导出，正文 80–103 行；获取 2026-09-05T10:51:08.931872+00:00；SHA cac19cabfd81a4adb7e08bd633d76dacfa9dc8319a51a0a4ac05c50b5f879ba4。
- [Log events](https://firebase.google.com/docs/analytics/android/events)，自定义事件示例与 Set default event parameters，正文 105–137 行；获取 2026-09-05T10:51:08.931872+00:00；SHA cac19cabfd81a4adb7e08bd633d76dacfa9dc8319a51a0a4ac05c50b5f879ba4。
- [Log events](https://firebase.google.com/docs/analytics/android/events)，View events in the Android Studio debug log / in the dashboard，正文 167–201 行；获取 2026-09-05T10:51:08.931872+00:00；SHA cac19cabfd81a4adb7e08bd633d76dacfa9dc8319a51a0a4ac05c50b5f879ba4。
- [Log events](https://firebase.google.com/docs/analytics/cpp/events)，C++ SDK Log events：同样载明 500 种事件类型上限与大小写敏感，正文 10–16 行；获取 2026-09-05T10:55:01.337510+00:00；SHA fb79e18c48912a80a62861bf4e201ac2d5e89a924b468b60d06f9f46d2a9b6b9。

## ios 条件与证据

适用范围：Firebase Apple 平台 SDK（iOS+ 文档）；正文未标注 SDK 版本与最低部署版本（version_verified=false），iOS 适用性来自 iOS+ 文档口径，未逐符号核对
条件：需 Firebase 项目启用 Google Analytics 并经 Swift Package Manager 集成 SDK；可选含/不含 IDFA 采集的分析库；IDFA 相关受 Apple ATT 约束（正文链接 Apple 官方文档）；需配置 FirebaseApp 实例后方可调用 logEvent；自定义参数需在控制台注册后方可入报表
缺口：未读取 ATT/AdSupport 与 Apple 隐私政策原文，IDFA 采集的强制条件未核实；最低 iOS 部署版本未标注；iPad/其他 Apple 平台适用范围未逐符号核对；上传时机、离线缓存与后台约束未覆盖；SDK 版本未固定（正文仅建议新项目使用最新版）
真机分类理由：接口有静态文档，但 IDFA/ATT 实际采集行为、上传时机与控制台可见性需真机验证；首轮未做实测

- [Log events](https://firebase.google.com/docs/analytics/ios/events)，Log events 开头：500 种事件类型上限、总量不限、名称区分大小写，正文 11–17 行；获取 2026-09-05T10:55:02.857162+00:00；SHA e89ba858cef49c7c9d6c1c36e5e9718101625681457cfa7b822fb842b5b54f66。
- [Log events](https://firebase.google.com/docs/analytics/ios/events)，Log events：配置 FirebaseApp 后使用 logEvent()，正文 28–32 行；获取 2026-09-05T10:55:02.857162+00:00；SHA e89ba858cef49c7c9d6c1c36e5e9718101625681457cfa7b822fb842b5b54f66。
- [Log events](https://firebase.google.com/docs/analytics/ios/events)，自定义事件 Swift/ObjC 示例与 Set default event parameters，正文 100–160 行；获取 2026-09-05T10:55:02.857162+00:00；SHA e89ba858cef49c7c9d6c1c36e5e9718101625681457cfa7b822fb842b5b54f66。
- [Log events](https://firebase.google.com/docs/analytics/ios/events)，View events in the Xcode debug console / in the dashboard，正文 162–191 行；获取 2026-09-05T10:55:02.857162+00:00；SHA e89ba858cef49c7c9d6c1c36e5e9718101625681457cfa7b822fb842b5b54f66。
- [Get started with Google Analytics for iOS+](https://firebase.google.com/docs/analytics/ios/get-started)，Before you begin：Firebase 项目需启用 Google Analytics，正文 23–40 行；获取 2026-09-05T10:55:03.226281+00:00；SHA 1e2774feafd3e5ae38a997cd7a2313cd61eb94ca329469221188d7589bd15a58。
- [Get started with Google Analytics for iOS+](https://firebase.google.com/docs/analytics/ios/get-started)，Add the Analytics SDK：SPM 安装、-ObjC、含/不含 IDFA 采集库与 ATT 链接，正文 57–73 行；获取 2026-09-05T10:55:03.226281+00:00；SHA 1e2774feafd3e5ae38a997cd7a2313cd61eb94ca329469221188d7589bd15a58。

## harmonyos 条件与证据

适用范围：HarmonyOS API 9 起（write/addWatcher 首批；元服务 API 11 起；setEventParam API 12+）；属华为 HarmonyOS 参考文档，未核对具体发行版与启动日最新正式版，OpenHarmony 对应关系未查
条件：经 @kit.PerformanceAnalysisKit 导入；系统能力 SystemCapability.HiviewDFX.HiAppEvent；write 写入的事件建议避免使用系统事件名称；事件写入本地后经 addWatcher 订阅获取；打点可经 configure 的 disable 关闭；存储配额默认 10MB，超限按旧到新清理；元服务场景自 API 11 起支持
缺口：上传侧（云端/生态分析服务）不在冻结来源，本包仅覆盖系统级采集与订阅；harmonyos-2（交互响应概述）主题为 ArkUI 输入事件，与节点无关，未用作证据；OpenHarmony 与 HarmonyOS 发行版对应关系及最新 API 版本未核对；事件落盘行为、配额清理与真机表现未验证；addProcessor 等扩展机制未读
真机分类理由：write 落盘、订阅回调与配额清理行为需真机验证；上传路径缺失更需结合生态服务在设备上核实；首轮未做实测

- [@ohos.hiviewdfx.hiAppEvent (应用事件打点)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent)，模块说明：打点/订阅/存储/清理/配置，系统事件与应用事件，首批 API version 9，正文 1–9 行；获取 2026-09-05T10:27:30.964615+00:00；SHA f04306f8ff0ad3a317fceb69ce80505bd9cfa1b33e3f882ca34237968c76a493。
- [@ohos.hiviewdfx.hiAppEvent (应用事件打点)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent)，导入模块与 hiAppEvent.addWatcher 签名（元服务 API 11、系统能力），正文 11–25 行；获取 2026-09-05T10:27:30.964615+00:00；SHA f04306f8ff0ad3a317fceb69ce80505bd9cfa1b33e3f882ca34237968c76a493。
- [@ohos.hiviewdfx.hiAppEvent (应用事件打点)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent)，hiAppEvent.setEventParam^12+^：按事件领域/名称关联自定义参数，正文 205–209 行；获取 2026-09-05T10:27:30.964615+00:00；SHA f04306f8ff0ad3a317fceb69ce80505bd9cfa1b33e3f882ca34237968c76a493。
- [@ohos.hiviewdfx.hiAppEvent (应用事件打点)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent)，AppEventInfo：domain/name/eventType/params 字符与数量规格，正文 557–570 行；获取 2026-09-05T10:27:30.964615+00:00；SHA f04306f8ff0ad3a317fceb69ce80505bd9cfa1b33e3f882ca34237968c76a493。
- [@ohos.hiviewdfx.hiAppEvent (应用事件打点)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent)，hiAppEvent.write（callback）：自定义事件存储、可经 addWatcher 订阅、错误码与 I/O 说明，正文 599–634 行；获取 2026-09-05T10:27:30.964615+00:00；SHA f04306f8ff0ad3a317fceb69ce80505bd9cfa1b33e3f882ca34237968c76a493。
- [@ohos.hiviewdfx.hiAppEvent (应用事件打点)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent)，hiAppEvent.configure 与 ConfigOption：disable 开关、maxStorage 配额默认 10MB，正文 1041–1093 行；获取 2026-09-05T10:27:30.964615+00:00；SHA f04306f8ff0ad3a317fceb69ce80505bd9cfa1b33e3f882ca34237968c76a493。

## 待验证差异假设

- limits_precision：事件标识与限制假设：Firebase 以单个事件名（区分大小写）标识事件，每应用最多 500 种事件类型、总日志量不限；HarmonyOS hiAppEvent 以 domain+name 双字段标识应用事件，域≤32 字符、名≤48 字符、参数≤32 个、string 参数≤8*1024 字符、数组≤100 元素，超限报错或丢弃。；待核：Firebase 侧参数名/值长度与个数限制未在冻结正文说明，需查事件与参数参考；HarmonyOS 应用事件类型总数是否有限制未见文档；超限行为语义（错误码返回 vs 静默丢弃）与 Firebase 服务端过滤规则需对齐精研。
- programming_model：上传与消费模型假设：Firebase 事件由 SDK 发送至 Google Analytics 后端并在 Firebase 控制台事件面板周期性呈现（调试日志可验证 events are being sent）；HarmonyOS hiAppEvent.write 将事件存入本地，应用需经 addWatcher 订阅获取，冻结来源未记录自动云端上传路径。；待核：HarmonyOS 生态侧（如 AGC 分析服务）是否存在对等自动上报能力，冻结来源未核实，不能据此断言不支持云端上报；Firebase 上传时机、离线缓存、网络与耗电约束未读；HarmonyOS 事件本地保留时长与跨进程消费限制未查。
- availability：能力层级假设：Android/iOS 的自定义事件采集证据均来自 Google Firebase 生态服务（需 Firebase 项目启用 Analytics 并集成第三方 SDK，logEvent 为 FirebaseAnalytics/Analytics 实例方法）；HarmonyOS 冻结证据为系统级 hiAppEvent（SystemCapability.HiviewDFX.HiAppEvent，API 9 起首批，经 PerformanceAnalysisKit 导入）。同一节点在三平台的证据分属生态层与系统层。；待核：HarmonyOS 生态层与 Firebase Analytics 对位的服务与文档未检索，节点 ecosystem 层映射未建立；Firebase 在无 Google 服务设备（部分 Android 发行版）的可用条件未读；Android/iOS 系统层是否存在无需生态服务的对等接口未查。

范围缺口：HarmonyOS 生态侧分析服务（如 AGC Analytics）对位文档缺失，ecosystem 层在 HarmonyOS 的对应物未建立，本包仅能以系统级 hiAppEvent 初判采集半边；三平台事件上传时机、离线缓存、批量/频率与耗电约束均未在冻结正文覆盖；Firebase SDK 版本（BOM/SPM）与最低系统版本未标注（version_verified=false），启动日最新正式版基线未固定；tablet 形态适用性未单独核对，仅沿用节点 device_forms 假设；来源 harmonyos-2 与节点无关，HarmonyOS 实际仅 1 篇相关正文，addProcessor 等扩展机制未读

后续优先级：P1；HarmonyOS 侧只有系统级采集证据，节点定义的上传半边与 ecosystem 层映射缺失，与 Android/iOS 的 Firebase 证据不同层，属高风险映射；三平台版本基线与上传行为亦未核实，为关键缺口。

逐条引用及原文摘录见同目录 normalized.json。
