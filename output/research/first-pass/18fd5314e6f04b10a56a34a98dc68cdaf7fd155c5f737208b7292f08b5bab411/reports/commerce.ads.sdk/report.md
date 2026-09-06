# 广告SDK — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台广告SDK初判：Android/iOS 均读到 Google AdMob（Mobile Ads SDK）官方正文，文档化 Banner/Interstitial（iOS 另有 Native）/Rewarded 广告单元及清单配置与初始化机制；C++ 跨平台路径已弃用（2025-06 EoM），instant app 广告路径 2025-12 终止。HarmonyOS 本包仅有智能体广告展示合规规范与 hvigor 构建错误码，未见应用内广告 SDK 正文，判 unknown。均为生态服务证据，版本基线未固定，置信度 low。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 读到 Google 生态广告 SDK 机制：AdMob/Mobile Ads SDK 提供 Banner、Interstitial、Rewarded 广告单元；Android 经 AndroidManifest.xml meta-data 配置 AdMob App ID，经 gradle/CMake 链接 firebase_gma。另读到 instant app 广告接入指南（含横幅/插页广告校验、禁止 HTTP 广告），但该路径 2025-12 起终止；C++ SDK 已弃用，官方建议改用平台原生 SDK。 | recommended |
| ios | documented_mechanism | direct | 读到 Google Mobile Ads SDK（AdMob）iOS 接入机制：Podfile 引入 Google-Mobile-Ads-SDK；Info.plist 配置 GADApplicationIdentifier（v7.42.0 起缺失会崩溃）；启动时调用 startWithCompletionHandler: 初始化一次（30 秒超时），初始化前需处理 EEA 同意与儿童定向标记。文档列出 Banner、Interstitial、Native、Rewarded 四种广告单元。Apple 第一方文档（ios-2）为应用许可交付 DRM SDK，与广告无关。 | recommended |
| harmonyos | unknown | indirect | 未读到 HarmonyOS 应用内横幅/激励广告单元 SDK 机制。本包两篇 HarmonyOS 正文：智能体广告为展示内容合规规范（标明'广告'、一键关闭、禁止体外弹出等），无 SDK 接口、广告单元或版本信息；另一篇为 hvigor 构建配置错误码，与广告无关。不能据此判断 HarmonyOS 支持或不支持应用内广告 SDK。 | unassessed |

## android 条件与证据

适用范围：快照 2026-09-05：Google Mobile Ads C++ SDK 2024-06-17 弃用、2025-06-17 进入 EoM；Google Play Instant 自 2025-12 起不可发布；原生 Android SDK 当前版本未在所读正文固定，版本基线 unresolved。
条件：广告 SDK 属 Google 生态服务（AdMob 账号、应用注册、App ID），非系统 SDK；Android 需在 AndroidManifest.xml 以 meta-data com.google.android.gms.ads.APPLICATION_ID 配置 AdMob App ID；instant app 广告路径要求广告网络 SDK 兼容 Google Play Instant 且不得投放 HTTP 广告，该路径 2025-12 起终止；C++ 路径已弃用，官方建议改用 Android/iOS 原生 SDK；未固定启动日最新正式版 SDK 基线
缺口：原生（Java/Kotlin）AdMob Android quick start 正文未在本包，当前 SDK 版本、最低 API Level 与依赖要求未核实；Google Mobile Ads Lite SDK 仅见名称引用，正文未读；广告加载/渲染、 mediation 、隐私合规（如 UMP 同意）机制未覆盖；phone/tablet 设备形态适配条件未在所读段落声明
真机分类理由：广告单元的加载、渲染与 SDK 初始化行为依赖运行时、AdMob 账号配置与网络，纯文档无法核实实际表现；本轮仅文档初判未做实测，正式精研建议真机验证。

- [Get started with AdMob in your C++ project](https://firebase.google.com/docs/admob/cpp/quick-start)，Step 5 AdMob 广告格式：Banner（顶部/底部矩形、自动刷新）、Interstitial（全屏）、Rewarded（激励视频/试玩/问卷），正文 359–399 行；获取 2026-09-05T11:00:08.246764+00:00；SHA 7b16be5447fbb320a826529f29a970400a6fddf96bd9bb441e7782c9f324972f。
- [Get started with AdMob in your C++ project](https://firebase.google.com/docs/admob/cpp/quick-start)，Step 2 Android 段：AndroidManifest.xml 配置 com.google.android.gms.ads.APPLICATION_ID meta-data，正文 89–107 行；获取 2026-09-05T11:00:08.246764+00:00；SHA 7b16be5447fbb320a826529f29a970400a6fddf96bd9bb441e7782c9f324972f。
- [Get started with AdMob in your C++ project](https://firebase.google.com/docs/admob/cpp/quick-start)，Google Mobile Ads C++ SDK 弃用声明（2024-06-17 弃用、2025-06-17 EoM），建议改用 iOS/Android 原生 SDK，正文 5–16 行；获取 2026-09-05T11:00:08.246764+00:00；SHA 7b16be5447fbb320a826529f29a970400a6fddf96bd9bb441e7782c9f324972f。
- [Get started with AdMob in your C++ project](https://firebase.google.com/docs/admob/cpp/quick-start)，Android gradle.properties/settings.gradle/build.gradle 与 CMakeLists 链接 firebase_gma 库，正文 138–194 行；获取 2026-09-05T11:00:08.246764+00:00；SHA 7b16be5447fbb320a826529f29a970400a6fddf96bd9bb441e7782c9f324972f。
- [Add ads to your instant app](https://developer.android.com/topic/google-play-instant/guides/advertising)，instant app 广告：需广告网络 SDK 兼容 Google Play Instant，逐类校验横幅/插页广告，禁止 HTTP 广告，正文 19–34 行；获取 2026-09-05T10:36:54.699334+00:00；SHA f037701ad1d34573d0e3f453a1fbd019bf2a2c41c891b3a8e84cd01c291ebc9b。
- [Add ads to your instant app](https://developer.android.com/topic/google-play-instant/guides/advertising)，警告：Google Play Instant 自 2025-12 起不可发布、Instant API 失效，正文 3–7 行；获取 2026-09-05T10:36:54.699334+00:00；SHA f037701ad1d34573d0e3f453a1fbd019bf2a2c41c891b3a8e84cd01c291ebc9b。

## ios 条件与证据

适用范围：快照 2026-09-05：Google Mobile Ads SDK v7.42.0 起强制 Info.plist App ID；当前最新 SDK 版本、Xcode/iOS 部署目标未在所读正文核实，版本基线 unresolved。
条件：证据来自 Google 第三方生态 SDK（AdMob），非 Apple 第一方框架；Info.plist 需配置 GADApplicationIdentifier，SDK v7.42.0 起缺失会导致启动崩溃；加载广告前需调用 GADMobileAds.sharedInstance 的 startWithCompletionHandler: 初始化，且仅调用一次；EEA 用户同意与 tagForChildDirectedTreatment 等请求标记需在初始化前处理（SDK 可能预加载广告）；未核实当前最新 SDK 版本与 iOS 部署目标
缺口：Apple 第一方是否提供广告 SDK 未检索到文档（本包 Apple 正文为 DRM 许可交付），不能据此断言有无；Google-Mobile-Ads-SDK 当前版本、iOS 最低部署目标与隐私清单（Privacy Manifest）要求未核实；ATT/广告标识符等 iOS 广告合规条件未在所读段落系统覆盖；phone/tablet（iPad）适配条件未声明
真机分类理由：广告加载/渲染、初始化时序与合规弹窗行为依赖真机运行时与 AdMob 账号，文档不能替代实测；本轮仅文档初判，正式精研建议真机验证。

- [Get started with AdMob in your iOS project](https://firebase.google.com/docs/admob/ios/quick-start)，Step 6 iOS 广告格式：Banner、Interstitial、Native、Rewarded 及各自实现链接，正文 255–311 行；获取 2026-09-05T11:00:08.731816+00:00；SHA 9f7a6037d3de58ca6d27fc8d13175f828a9f2cafb70f2c378b0887ba8e86e967。
- [Get started with AdMob in your iOS project](https://firebase.google.com/docs/admob/ios/quick-start)，Step 2 Info.plist 配置 GADApplicationIdentifier，SDK v7.42.0 起强制，缺失即崩溃，正文 69–77 行；获取 2026-09-05T11:00:08.731816+00:00；SHA 9f7a6037d3de58ca6d27fc8d13175f828a9f2cafb70f2c378b0887ba8e86e967。
- [Get started with AdMob in your iOS project](https://firebase.google.com/docs/admob/ios/quick-start)，Step 3 Podfile 引入 Google-Mobile-Ads-SDK 并在启动时调用 startWithCompletionHandler: 初始化（30 秒超时），正文 91–105 行；获取 2026-09-05T11:00:08.731816+00:00；SHA 9f7a6037d3de58ca6d27fc8d13175f828a9f2cafb70f2c378b0887ba8e86e967。
- [Get started with AdMob in your iOS project](https://firebase.google.com/docs/admob/ios/quick-start)，警告：初始化即可能预加载广告，EEA 同意与儿童定向标记需在初始化前完成，正文 107–120 行；获取 2026-09-05T11:00:08.731816+00:00；SHA 9f7a6037d3de58ca6d27fc8d13175f828a9f2cafb70f2c378b0887ba8e86e967。
- [App License Delivery SDK](https://developer.apple.com/documentation/applicensedeliverysdk)，Apple 第一方 App License Delivery SDK 为替代分发应用的 DRM 许可交付，与广告 SDK 无关，正文 1–9 行；获取 2026-09-05T10:29:55.775912+00:00；SHA 3bde5d40986d946e52ffa7903bc2b810666b07b8a299f4d079772ee73441fb09。

## harmonyos 条件与证据

适用范围：快照 2026-09-05：两篇文档均无 SDK/系统版本信息；HarmonyOS 与 OpenHarmony 发行版适用性未区分核实，版本基线 unresolved。
条件：本包 HarmonyOS 文档均非应用内广告 SDK 正文（智能体广告合规规范、hvigor 配置错误码）；智能体广告文档仅约束智能体内的展示行为（可识别、一键关闭、不得恶意弹出），不提供广告单元接口；HarmonyOS/OpenHarmony 发行版与设备条件未核对
缺口：未读取华为广告服务（如 Petal Ads/广告服务 Kit）官方 SDK 文档，横幅/激励广告单元支持情况 unknown；智能体广告规范与 app 内广告单元是否属同一能力域未界定，且该文无版本与适用对象说明；未检索到不等于不支持：HarmonyOS 生态广告 SDK 的存在性、接口形态、接入条件均待补证据；缺少 HarmonyOS 侧与 AdMob 等第三方 SDK 可比对的接入机制文档
真机分类理由：尚未识别可验证的 HarmonyOS 广告 SDK 机制，无从设计真机验证项；待补齐官方广告服务 SDK 文档后再评估真机需求。

- [智能体广告](https://developer.huawei.com/consumer/cn/doc/service/agent-advertisement-0000002520493294)，智能体广告定位：作为智能体一部分展示，内容需合法合规、显著标明'广告'并可识别，正文 1–13 行；获取 2026-09-05T10:53:14.137279+00:00；SHA 43fe33ee70f6d04aff67ec9ec7e5e4dff8e15ab8efebaa79fab46cb2c282a4b8。
- [智能体广告](https://developer.huawei.com/consumer/cn/doc/service/agent-advertisement-0000002520493294)，展示行为要求：不得体外弹出、不得干扰系统功能键、需一键关闭且关闭标志明显有效，正文 15–35 行；获取 2026-09-05T10:53:14.137279+00:00；SHA 43fe33ee70f6d04aff67ec9ec7e5e4dff8e15ab8efebaa79fab46cb2c282a4b8。
- [配置错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00303-1)，本篇为 hvigor 构建配置错误码（compatibleSdkVersion<=targetSdkVersion<=compileSdkVersion 规则），不含广告 SDK 内容，正文 131–147 行；获取 2026-09-05T10:22:49.668162+00:00；SHA 77208e92127d1bbc61acbbbfdb7a53a4c8f794ad5bb39cdc5aeccdd6d4ed3214。

## 待验证差异假设

- api_surface：广告单元格式集合映射差异假设：Android 与 iOS 经 AdMob 文档化 Banner/Interstitial/Rewarded（iOS 另列 Native）等广告单元及实现入口；HarmonyOS 本包仅见智能体广告展示合规要求，未见应用内广告单元 SDK 格式清单，是否存在等价格式待确认。；待核：HarmonyOS 是否有官方广告服务 SDK（如 Petal Ads）及横幅/激励单元，需检索华为广告服务文档；AdMob 各格式在 Android/iOS 的当前 API 形态与最新 SDK 版本适配未核实；智能体广告（智能体内展示）与应用内广告单元是否属同一比较范围需先界定。
- programming_model：SDK 配置与初始化机制差异假设（can 层面）：Android 经 AndroidManifest.xml meta-data 配置 AdMob App ID 并经 gradle/CMake 链接 firebase_gma；iOS 经 Info.plist 的 GADApplicationIdentifier（v7.42.0 起缺失即崩溃）并在启动时调用 startWithCompletionHandler: 初始化，两平台接入与初始化契约不同。；待核：两平台最新 SDK 版本的配置与初始化要求是否变化未核实；iOS 初始化 30 秒超时与预加载行为和 Android 路径的实际差异待查；HarmonyOS 若存在广告 SDK，其配置与初始化机制未知，暂无法纳入本假设比较。

范围缺口：HarmonyOS：本包无应用内广告 SDK（华为广告服务/Petal Ads 等）官方正文，横幅/激励单元支持判 unknown，需检索 service 广告服务文档后再定；iOS：证据全部来自 Google 第三方 SDK；Apple 第一方广告 SDK 文档未检索到（ios-2 为 DRM 许可交付），不能据此断言 Apple 平台有无第一方方案；Android：原生（Java/Kotlin）AdMob 接入正文未在包内，仅读到已弃用 C++ 路径与 2025-12 终止的 instant app 指南，当前 SDK 版本与要求未核实；版本基线 unresolved：三平台 SDK/系统版本适用性均未固定，文档快照不证明启动日最新正式版支持；广告合规维度（EEA 同意/UMP、儿童定向、隐私清单、广告标识符）仅 iOS 文档片段提及，未做三平台系统比较

后续优先级：P1；HarmonyOS 侧零直接证据（关键缺口），且广告 SDK 属生态服务、三平台映射风险高：需检索华为广告服务 SDK 文档、补 Android/iOS 原生接入正文并固定版本基线后才能形成可比初判。

逐条引用及原文摘录见同目录 normalized.json。
