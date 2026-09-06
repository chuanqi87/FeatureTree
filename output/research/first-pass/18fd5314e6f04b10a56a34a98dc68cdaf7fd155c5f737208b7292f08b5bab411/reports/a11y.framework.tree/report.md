# 无障碍树与语义 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到向辅助技术暴露语义的官方机制：Android Compose 并行语义树（merged/unmerged 双树、语义属性）；iOS UIKit accessibility element（label/hint/分组）与 Safari 网页内容无障碍树；HarmonyOS 服务卡片无障碍属性（API 8+）与 NDK Provider 节点树（API 13/23+）。三平台系统级树 API 正文均未读，版本基线未固定，全部 low 初判。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | Compose 文档明示组合树之外存在并行语义树，供无障碍服务与测试框架使用；语义属性（text、contentDescription、Role、stateDescription、heading、liveRegion 等）描述组件含义，mergeDescendants 控制合并，无障碍服务使用 unmerged 树；自定义低阶组件需手动提供语义。仅覆盖 Compose，未标注版本。 | recommended |
| ios | documented_mechanism | direct | UIKit 文档说明标准控件默认可被 VoiceOver 朗读，自定义元素需设置 isAccessibilityElement 与 accessibilityLabel/Hint，可用 UIAccessibilityElement 分组控制阅读顺序；Safari 18.1 发行说明提及网页内容在无障碍树中的暴露修复。未见 UIKit 侧『无障碍树』API 正文。 | recommended |
| harmonyos | documented_mechanism | direct | 服务卡片组件可设 accessibilitygroup/text/description/importance（API 8 起）并接收无障碍事件；NDK 文档明示自绘三方框架经 ArkUI_AccessibilityProvider 回调暴露无障碍节点树（根节点 parentId=-2100000 等约定），API 13 起 XComponent、API 23 起 CustomNode。主应用 ArkTS 属性指南未读。 | recommended |

## android 条件与证据

适用范围：两篇来源均未标注 API Level 或 Compose 库版本（version_verified=false，快照 2026-09-05）；属 Jetpack Compose UI 无障碍文档，非系统 View 层 API；启动日基线未固定。
条件：来源为 Jetpack Compose（AndroidX）UI 框架文档，适用范围为 Compose 构建的应用；语义树由 Compose 组合与 Foundation/Material 组件自动填充，自定义低阶组件需手动设置；语义信息需由无障碍服务（如 TalkBack）或测试框架消费；调试依赖 Android Studio Layout Inspector、TalkBack 开发者设置 TreeDebug 或 ComposeTestRule
缺口：未读到系统 View 层无障碍树 API（AccessibilityNodeInfo/AccessibilityDelegate/importantForAccessibility）正文；来源未标注 API Level/Compose 版本，最新正式版支持情况未核实；语义属性全集仅以链接引用（SemanticsProperties/SemanticsActions），参考正文未读；TalkBack 等服务实际合并与播报行为未验证
真机分类理由：语义树结构与属性为静态文档，但服务实际如何合并 unmerged 树并播报需真机开启 TalkBack 验证；本轮仅文档初判，未执行实测。

- [Semantics](https://developer.android.com/develop/ui/compose/accessibility/semantics)，Semantics - Semantic properties convey the meaning of the composable，正文 24–28 行；获取 2026-09-05T10:24:40.906712+00:00；SHA 19f72a2f81ce8568a9c429ad95d4c81f2400740260c1e217c51287c3d1906c4f。
- [Semantics](https://developer.android.com/develop/ui/compose/accessibility/semantics)，Semantics tree - parallel tree used by accessibility services and testing，正文 425–432 行；获取 2026-09-05T10:24:40.906712+00:00；SHA 19f72a2f81ce8568a9c429ad95d4c81f2400740260c1e217c51287c3d1906c4f。
- [Semantics](https://developer.android.com/develop/ui/compose/accessibility/semantics)，Semantics tree - custom low-level composables require manual semantics，正文 439–444 行；获取 2026-09-05T10:24:40.906712+00:00；SHA 19f72a2f81ce8568a9c429ad95d4c81f2400740260c1e217c51287c3d1906c4f。
- [Semantics](https://developer.android.com/develop/ui/compose/accessibility/semantics)，Inspect the tree - merged and unmerged trees, services use unmerged tree，正文 514–521 行；获取 2026-09-05T10:24:40.906712+00:00；SHA 19f72a2f81ce8568a9c429ad95d4c81f2400740260c1e217c51287c3d1906c4f。
- [Inspect and debug](https://developer.android.com/develop/ui/compose/accessibility/inspect-debug)，Debug - tools provide information about nodes and properties exposed to accessibility services，正文 25–28 行；获取 2026-09-05T10:24:40.353131+00:00；SHA a210c2525229776e871d242295340d0983a6db3f24aa3b9d53b91e0226a6aa6a。

## ios 条件与证据

适用范围：Safari 18.1 发行说明明示适用 iOS 18.1/iPadOS 18.1/visionOS 2.1/macOS 15.1 等（2024-10-28 发布）；UIKit 文章未标注最低 iOS 版本；启动日基线未固定。
条件：UIKit 文档适用范围为标准 UIKit 控件与自定义 UI 元素，需开启 VoiceOver 交互；VoiceOver 按设备语言方向朗读，元素分组影响阅读顺序；Safari 18.1 发行说明仅覆盖 WebKit 网页内容场景的无障碍树行为；审计方式为真机/模拟器开启 VoiceOver 手动遍历界面
缺口：『无障碍树』直接文字证据仅见于 Safari/WebKit 网页内容发行说明，UIKit/SwiftUI 侧树概念 API 参考正文未读；accessibilityLabel/Hint、UIAccessibilityElement 等符号的 availability（最低 iOS 版本）未核实；SwiftUI 无障碍机制未覆盖；iOS 18.1 仅为 Safari 发行说明适用范围，不能代表 UIKit 文档版本
真机分类理由：文档自身要求开启 VoiceOver 审计元素可达性与阅读顺序，实际朗读与分组效果属运行时行为；本轮未执行实测。

- [Supporting VoiceOver in your app](https://developer.apple.com/documentation/uikit/supporting-voiceover-in-your-app)，Identify common accessibility issues - custom UI elements not recognized by default, grouping，正文 35–39 行；获取 2026-09-05T11:19:58.549660+00:00；SHA 528d221f44d9e061eadf8c2d11a8e151183fdfe68ef6365ad63024a0e78618f3。
- [Supporting VoiceOver in your app](https://developer.apple.com/documentation/uikit/supporting-voiceover-in-your-app)，Update your app's accessibility - accessibilityLabel and accessibilityHint properties，正文 45–47 行；获取 2026-09-05T11:19:58.549660+00:00；SHA 528d221f44d9e061eadf8c2d11a8e151183fdfe68ef6365ad63024a0e78618f3。
- [Supporting VoiceOver in your app](https://developer.apple.com/documentation/uikit/supporting-voiceover-in-your-app)，Add accessibility labels programmatically - isAccessibilityElement，正文 61–67 行；获取 2026-09-05T11:19:58.549660+00:00；SHA 528d221f44d9e061eadf8c2d11a8e151183fdfe68ef6365ad63024a0e78618f3。
- [Supporting VoiceOver in your app](https://developer.apple.com/documentation/uikit/supporting-voiceover-in-your-app)，Simplify your accessibility information - grouping with UIAccessibilityElement，正文 78–84 行；获取 2026-09-05T11:19:58.549660+00:00；SHA 528d221f44d9e061eadf8c2d11a8e151183fdfe68ef6365ad63024a0e78618f3。
- [Safari 18.1 Release Notes](https://developer.apple.com/documentation/safari-release-notes/safari-18_1-release-notes)，Overview - Safari 18.1 availability for iOS 18.1 and other systems，正文 3–7 行；获取 2026-09-05T10:25:23.738171+00:00；SHA 1f9ba3ccee71f3e749ac48ec12e2d602e4cf634510ad5040637d0980dc0bda9a。
- [Safari 18.1 Release Notes](https://developer.apple.com/documentation/safari-release-notes/safari-18_1-release-notes)，Accessibility resolved issues - content exposed in the accessibility tree，正文 13–18 行；获取 2026-09-05T10:25:23.738171+00:00；SHA 1f9ba3ccee71f3e749ac48ec12e2d602e4cf634510ad5040637d0980dc0bda9a。

## harmonyos 条件与证据

适用范围：文档标注 API 8（服务卡片公共属性）、API 13（XComponent 自绘接入）、API 23（CustomNode 自绘接入）；对应 HarmonyOS/OpenHarmony 发行版映射未核实；启动日基线未固定。
条件：harmonyos-1 为服务卡片（js-service-widget-common）场景的公共组件无障碍属性文档；NDK 自绘接入需从绘制容器获取 ArkUI_AccessibilityProvider 并注册回调（单实例或多实例）；无障碍节点须满足根节点约定：唯一根、parentId=-2100000、enabled/visible 为 true；需无障碍辅助服务（如屏幕朗读）开启后完成交互
缺口：harmonyos-1 为服务卡片文档，主应用 ArkTS 组件无障碍属性指南正文未读；API 8/13/23 对应的 HarmonyOS 发行版与 SDK 版本未核实；ArkUI_AccessibilityElementInfo 语义属性全集（参考页仅链接）未读；无障碍事件类型全集与屏幕朗读实际播报行为未验证
真机分类理由：Provider 回调契约与属性为静态文档，根节点约定、事件发送与屏幕朗读实际交互需真机开启无障碍服务验证；本轮未执行实测。

- [无障碍](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-accessibility)，无障碍 - 组件无障碍属性与事件说明，从 API version 8 开始支持，正文 3–5 行；获取 2026-09-05T10:38:21.585697+00:00；SHA 3b90f266444afc4d14acd40c5c06aaf5b095bf24db20b91cc4f5ccb6d316f320。
- [无障碍](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-accessibility)，无障碍属性表 - accessibilitygroup/text/description/importance，正文 7–14 行；获取 2026-09-05T10:38:21.585697+00:00；SHA 3b90f266444afc4d14acd40c5c06aaf5b095bf24db20b91cc4f5ccb6d316f320。
- [通过自绘制接入无障碍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-accessibility-xcomponent)，NDK 自绘制接入概述 - Provider 获取与回调注册，API 13/23 起支持，正文 3–13 行；获取 2026-09-04T09:35:09+00:00；SHA bcfbbf19b8239752d0fdb18c904b6a6edce90c7de0a76d2025ab021e8840497c。
- [通过自绘制接入无障碍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-accessibility-xcomponent)，根节点约定 - elementId=-1 根节点标识、parentId=-2100000、enabled/visible 须为 true，正文 88–92 行；获取 2026-09-04T09:35:09+00:00；SHA bcfbbf19b8239752d0fdb18c904b6a6edce90c7de0a76d2025ab021e8840497c。

## 待验证差异假设

- programming_model：三平台向辅助技术暴露语义的编程模型可能不同：Android Compose 文档明示由组合自动生成并行语义树并以语义属性描述组件；iOS UIKit 文档明示以 accessibility element 属性（isAccessibilityElement/label/hint）手动标记与分组；HarmonyOS 文档明示组件无障碍属性（卡片）与 NDK Provider 回调节点树（自绘）两条接入路径。；待核：各平台语义属性集合与默认值的逐项映射未完成；Android 系统 View 层与 iOS SwiftUI 的对应机制不在本轮来源内；HarmonyOS 主应用 ArkTS 属性与卡片属性是否一致未核实。
- api_surface：对自定义/自绘内容的语义接入机制可能不同：三者文档均要求手动补充语义，但接入面不同——Compose 用语义 modifier 补充自定义低阶组件，UIKit 需以编程方式定义 accessibility element，HarmonyOS NDK 提供显式 Provider 回调契约（节点查询、焦点、操作执行等回调与根节点硬编码约定）。；待核：iOS 自绘内容（如 CALayer/Metal）是否存在等价 Provider 式契约未读；Android View 层等价机制（如 ExploreByTouchHelper）不在本轮来源内；HarmonyOS 声明式组件与自绘接入两条路径的语义能力是否等价未验证。
- limits_precision：树的合并语义可能不同：Android Compose 文档明示语义树存在 merged/unmerged 两种形态且无障碍服务使用 unmerged 树并自行合并；本轮 iOS 来源仅描述开发者手动分组（UIAccessibilityElement）控制阅读顺序，HarmonyOS 来源仅描述 accessibilitygroup 将组件及子组件合并为整体可选中，均未见等价双树结构描述。；待核：iOS 无障碍元素树内部是否存在框架级合并策略文档未查；HarmonyOS ArkUI 无障碍树内部结构与合并规则文档未读；unmerged 树语义在 iOS/HarmonyOS 是否存在等价物未知。

范围缺口：Android 侧仅读 Compose 文档，系统 View 层无障碍树 API（AccessibilityNodeInfo 等）未覆盖；iOS 侧『无障碍树』直接证据仅 Safari/WebKit 网页内容发行说明，UIKit/SwiftUI 树概念 API 正文未读；HarmonyOS 侧缺主应用 ArkTS 组件无障碍属性指南正文，发行版与 API 版本映射未核实；三平台启动日最新正式版基线未固定（version_baseline unresolved），版本适用性均待核实；本轮为 first_pass 初判，24 个比较槽与真机用例设计未涉及

后续优先级：P1；三平台来源与节点核心范围错位（Android 仅 Compose、iOS 仅 UIKit 入门文章加 WebKit 发行说明、HarmonyOS 仅服务卡片与 NDK 自绘），各平台系统级无障碍树 API 正文均缺失，编程模型映射与版本适用风险高，需优先补读核心 API 参考后复核。

逐条引用及原文摘录见同目录 normalized.json。
