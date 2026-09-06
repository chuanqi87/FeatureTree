# 轻量即用安装 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到官方轻量即用机制正文：Android 为 Google Play Instant（instant-enabled App Bundle，合计≤15MB、Android 8.0+、受限沙箱），且官方两处明示自 2025-12 起停发并终止所有 Instant API；iOS 为 App Clips（随父应用构建、invocation 入口、不驻留主屏）；HarmonyOS 为元服务（免安装、可独立上架、仅元服务API集，需 HarmonyOS NEXT DP1/API 11+）。三平台初判均 low，启动日基线未固定；主要缺口为 Android 终止后残余状态与 iOS/HarmonyOS 数值级限制。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | Google Play Instant 以 instant-enabled App Bundle 提供免完整安装体验：运行于受限 SELinux 沙箱（有限权限子集、禁后台服务与后台通知），生产轨道合计下载≤15MB，需 Android 8.0+。官方两处明示自 2025-12 起不能再经 Google Play 发布，所有 Google Play services Instant API 停止工作。 | recommended |
| ios | documented_mechanism | direct | App Clips 是 Apple 官方轻量形态：无需安装完整 App 即可即用部分功能，符合一组约束可更大体积提供 demo 版；不驻留主屏幕，系统在一段时间不活跃后自动移除；经 invocation URL、App Clip Code（NFC/扫码）、网站 Smart App Banner 等入口启动，App Store Connect 中以关联注册父应用的 AppClip 资源管理。 | recommended |
| harmonyos | documented_mechanism | direct | 元服务是 HarmonyOS 免安装的轻量应用形态：秒开直达、即用即走，可独立上架、分发、运行并独立实现业务闭环；对比传统应用包大小有限制、自动更新、跟随华为账号，且只能使用元服务API集；自 HarmonyOS NEXT Developer Preview1（API 11）起仅支持 Stage 模型与 ArkTS，要求系统 NEXT DP1 及以上，支持 1+8+N 设备。 | recommended |

## android 条件与证据

适用范围：快照 2026-09-05（version_verified=false）；属 Google Play/GMS 生态服务而非 AOSP 系统 SDK；官方声明 2025-12 起 Instant Apps 停发、Instant API 失效；机制描述基于 Android 8.0 (API 26)+ 条件
条件：以 instant-enabled App Bundle 形式随同一包名的可安装应用发布，即时体验版本号须低于可安装版本；运行于特殊 SELinux 沙箱：仅允许有限权限子集（INTERNET、CAMERA、ACCESS_FINE_LOCATION 等），不能用后台服务、不能后台发通知；所有 instant 模块代码与资源合计下载体积生产轨道≤15MB；仅 Android 8.0 (API level 26) 及以上设备可体验即时应用；发布与分发依赖 Google Play / Play Console（GMS 生态服务）
缺口：快照 version_verified=false；2025-12 终止后的残余状态（已缓存体验、非 Google Play 渠道、厂商机制）无文档，需真机或后续精研核实；Instant Apps 属 Google Play 生态服务；AOSP 系统 SDK 或其他 Android 应用市场是否存在等价轻量安装形态未调查；tablet 形态的即时体验条件未在所读文档单独说明；权限清单中 INSTANT_APP_FOREGROUND_SERVICE 等仅标注 Android 8.0+，更低版本与具体 API Level 适配细节未读
真机分类理由：终止事实已由官方文档明示，初判不需真机；但 2025-12 之后设备与 Play 的实际残余状态（如已缓存体验是否仍可运行）文档未覆盖，正式确认时建议真机抽检。

- [InstantApps](https://developers.google.com/android/reference/com/google/android/gms/instantapps/InstantApps)，InstantApps 类弃用声明：Starting December 2025, Instant Apps cannot be published through Google Play, and all Google Play services Instant APIs will no longer work，正文 7–11 行；获取 2026-09-05T14:47:49.515867+00:00；SHA 41bb576dbe37ad0c549c5f7ebc4f625ae9e3f81d244dde74242217b7c886130a。
- [Create an instant-enabled app bundle](https://developer.android.com/topic/instant-apps/getting-started/structure)，Warning: Google Play Instant will no longer be available；Users will no longer be served Instant Apps by Play using any mechanism，正文 3–7 行；获取 2026-09-05T10:47:58.080488+00:00；SHA df025673d019dbec8da468b2de739981d677677f5e0fdc2dff87a8b6e203034d。
- [Create an instant-enabled app bundle](https://developer.android.com/topic/instant-apps/getting-started/structure)，required execution conditions：SELinux sandbox 与受限交互，正文 49–52 行；获取 2026-09-05T10:47:58.080488+00:00；SHA df025673d019dbec8da468b2de739981d677677f5e0fdc2dff87a8b6e203034d。
- [Create an instant-enabled app bundle](https://developer.android.com/topic/instant-apps/getting-started/structure)，Supported permissions and operations：instant-enabled app bundles 仅可用列表内权限，正文 56–71 行；获取 2026-09-05T10:47:58.080488+00:00；SHA df025673d019dbec8da468b2de739981d677677f5e0fdc2dff87a8b6e203034d。
- [Create an instant-enabled app bundle](https://developer.android.com/topic/instant-apps/getting-started/structure)，combined download size of the code and resources within all instant-enabled modules must be at most 15 MB，正文 220–222 行；获取 2026-09-05T10:47:58.080488+00:00；SHA df025673d019dbec8da468b2de739981d677677f5e0fdc2dff87a8b6e203034d。
- [Create an instant-enabled app bundle](https://developer.android.com/topic/instant-apps/getting-started/structure)，Instant experiences are available only on devices running Android 8.0 (API level 26) or higher，正文 370–371 行；获取 2026-09-05T10:47:58.080488+00:00；SHA df025673d019dbec8da468b2de739981d677677f5e0fdc2dff87a8b6e203034d。

## ios 条件与证据

适用范围：Apple 官方文档快照 2026-09-05（version_verified=false）；所读正文未标注 App Clips 最低 iOS 版本，仅出现 iOS 16.3（网站关联适用设备上下文）；当前最新 iOS 正式版基线未固定
条件：App Clip 随宿主完整 App 的 Xcode 工程构建（新增 App Clip target 并共享代码），在 App Store Connect 配置 App Clip 体验；通过 invocation URL / App Clip 体验被发现和启动，支持 App Clip Code（NFC 集成或扫码）、网站 Smart App Banner 与 Messages 入口；符合一组约束的 App Clip 可使用更大体积提供 demo 版本，用完引导安装完整 App；不出现在主屏幕，用户不像管理完整 App 那样管理，系统在一段不活跃期后移除；可经 CloudKit、Sign in with Apple、共享容器等向完整 App 传递数据
缺口：App Clips 体积上限数值与最低 iOS 版本未在所读冻结正文出现（仅 iOS 16.3 一处上下文）；通知时长限制（短/长时段）具体规则未读正文；tablet（iPad）适用性未逐符号核对 Apple 目录 availability；当前最新 iOS 正式版基线未固定，无法确认现行版本状态
真机分类理由：机制与入口为文档明示，初判不需真机；invocation 入口（NFC/扫码/横幅）与体积约束的实际运行行为需真机核实，留待精研。

- [App Clips](https://developer.apple.com/documentation/appclip)，An App Clip is a lightweight version of your app... instantly available – ... without the need to install the full app，正文 7–7 行；获取 2026-09-05T10:29:51.993299+00:00；SHA a121c7feb705700c17f1bf07cb9bfc006e155c8dea154669d7486bdb1639216d。
- [App Clips](https://developer.apple.com/documentation/appclip)，App Clips that conform to a set of constraints can be larger in size... demo version of your app，正文 11–11 行；获取 2026-09-05T10:29:51.993299+00:00；SHA a121c7feb705700c17f1bf07cb9bfc006e155c8dea154669d7486bdb1639216d。
- [App Clips](https://developer.apple.com/documentation/appclip)，App Clips don't appear on the Home screen... the system removes an App Clip from a device after a period of inactivity，正文 15–15 行；获取 2026-09-05T10:29:51.993299+00:00；SHA a121c7feb705700c17f1bf07cb9bfc006e155c8dea154669d7486bdb1639216d。
- [App Clips](https://developer.apple.com/documentation/appclip)，创建流程：add an App Clip target、Create App Clip experiences in App Store Connect、create App Clip Codes，正文 29–35 行；获取 2026-09-05T10:29:51.993299+00:00；SHA a121c7feb705700c17f1bf07cb9bfc006e155c8dea154669d7486bdb1639216d。
- [App Clips](https://developer.apple.com/documentation/appclip)，Associating your App Clip with your website... devices running iOS 16.3 or earlier，正文 75–75 行；获取 2026-09-05T10:29:51.993299+00:00；SHA a121c7feb705700c17f1bf07cb9bfc006e155c8dea154669d7486bdb1639216d。
- [App Clips](https://developer.apple.com/documentation/appstoreconnectapi/app-clips)，AppClip object: A lightweight version of an app that users can launch instantly without installation, associated with a registered parent app，正文 35–35 行；获取 2026-09-05T10:37:40.813082+00:00；SHA 96f57d7c4e6baa7e25c6c06e265b63fd6d511b7b3044a7b13db8780b7b2d5143。

## harmonyos 条件与证据

适用范围：华为官方文档快照 2026-09-05（version_verified=false）；声明自 HarmonyOS NEXT Developer Preview1（对应 API 11）起的元服务开发与运行规则；当前 HarmonyOS 最新正式版基线未固定；未核对 OpenHarmony 发行版
条件：基于 HarmonyOS SDK 且只能使用元服务API集，仅支持 Stage 模型与 ArkTS 接口；仅可运行在系统软件版本为 HarmonyOS NEXT Developer Preview1 及以上的设备；可独立上架、分发、运行，独立实现业务闭环；包大小有限制（具体数值未在所读文档给出）、自动更新、跟随华为账号；开发需在 AGC 创建元服务、用 DevEco Studio 创建工程，真机调试需对 HAP 签名
缺口：元服务包大小具体上限数值与上架审核要求未在所读文档给出；HarmonyOS 当前最新正式版（如 5.x/6.x）下元服务状态未核实，启动日基线未固定；OpenHarmony 发行版是否具备对应免安装形态未核对（本包仅华为 HarmonyOS 文档）；tablet 属 1+8+N 表述范围但未逐设备形态核对适用性
真机分类理由：免安装、秒开为运行态行为且文档已明示；正式确认元服务在真机上的免安装运行、留存与 1+8+N 设备覆盖需设备验证，留待精研。

- [什么是元服务](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-service-definition)，从HarmonyOS NEXT Developer Preview1（对应API 11）版本开始：元服务只能用元服务API集、仅支持Stage模型与ArkTS，运行需系统 NEXT DP1 及以上，正文 4–7 行；获取 2026-09-05T10:41:39.788512+00:00；SHA 1353cbf5585a31fbbb60b0ac5e92986ef3aec204859d35b54679b3f0dacfd8d6。
- [什么是元服务](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-service-definition)，HarmonyOS 除传统需要安装的应用外，还支持更加方便快捷的免安装的应用，即元服务，正文 9–9 行；获取 2026-09-05T10:41:39.788512+00:00；SHA 1353cbf5585a31fbbb60b0ac5e92986ef3aec204859d35b54679b3f0dacfd8d6。
- [什么是元服务](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-service-definition)，元服务是HarmonyOS提供的一种轻量应用程序形态...可独立上架、分发、运行，正文 11–13 行；获取 2026-09-05T10:41:39.788512+00:00；SHA 1353cbf5585a31fbbb60b0ac5e92986ef3aec204859d35b54679b3f0dacfd8d6。
- [什么是元服务](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-service-definition)，基于HarmonyOS SDK开发，支持运行在1+8+N设备上，正文 15–15 行；获取 2026-09-05T10:41:39.788512+00:00；SHA 1353cbf5585a31fbbb60b0ac5e92986ef3aec204859d35b54679b3f0dacfd8d6。
- [什么是元服务](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-service-definition)，表1 元服务与传统应用对比：免安装、包大小有限制、即用即走、自动更新、跟随华为账号、只能使用元服务API集，正文 21–25 行；获取 2026-09-05T10:41:39.788512+00:00；SHA 1353cbf5585a31fbbb60b0ac5e92986ef3aec204859d35b54679b3f0dacfd8d6。
- [元服务开发准备](https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-dev-preparation)，元服务开发准备：AGC 创建元服务、DevEco Studio 创建工程、真机调试需对 HAP 签名，正文 9–23 行；获取 2026-09-05T10:41:39.496584+00:00；SHA cf079b3768d507a1d798644c2f11173ecbde36ce74eb21ed8d5259a8398fda93。

## 待验证差异假设

- availability：可用性走向差异（can 层面）：Android 的 Google Play Instant 被官方宣布自 2025-12 起不能再经 Google Play 发布且所有 Google Play services Instant API 停止工作，而 iOS App Clips 与 HarmonyOS 元服务在各自官方文档中仍作为现行机制描述。；待核：iOS App Clips 与 HarmonyOS 元服务在 2026 当前最新正式版中的实际状态需以发行说明核实；Android 终止后官方是否提供替代轻量机制（文档建议改用 deeplink 引导完整应用）未在机制层核实。
- programming_model：与完整应用的宿主关系差异：iOS App Clips 须随宿主完整 App 工程（App Clip target）构建并与注册父应用关联；HarmonyOS 元服务可独立上架、分发、运行；Android 即时体验须作为同包名 App Bundle 的一部分且版本号低于可安装版本。；待核：HarmonyOS 元服务“一体两面，嵌入运行”特征是否也允许依附宿主应用的形态未读正文；iOS 是否存在脱离父应用单独分发 App Clip 的途径未见文档。
- lifecycle_background：留存与更新机制差异：iOS 系统在一段不活跃期后自动移除 App Clip 且不驻留主屏幕；Android 即时体验缓存在设备内存不足或重启后被清除、需重新下载；HarmonyOS 元服务自动更新并跟随华为账号。；待核：各平台具体保留时长与清退阈值数值未读；HarmonyOS 元服务本地留存与清理策略未在所读文档说明。

范围缺口：iOS App Clips 体积上限数值、最低系统版本与通知时长限制未在冻结来源正文中读取；HarmonyOS 元服务包大小上限具体数值与上架审核要求未读取；Android Instant Apps 终止（2025-12）后的残余状态与非 Google Play 渠道未调查；OpenHarmony 发行版的对应能力未核对；Apple 目录 iOS 逐符号适用性核对未完成；启动日三平台最新正式版与手机基线未固定，本轮结论仅基于 2026-09-05 快照

后续优先级：P1；Android 官方明示 Google Play Instant 自 2025-12 终止，直接改变该节点 Android 侧可用性结论，属高风险映射；且 iOS/HarmonyOS 的数值级限制（体积上限、最低版本）缺失，需优先精研核实。

逐条引用及原文摘录见同目录 normalized.json。
