# 状态驱动界面更新 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到声明式状态驱动UI的官方描述：HarmonyOS最直接（ArkTS声明式：声明UI结构与状态，自动驱动界面渲染）；Android证据来自Wear迁移文（状态驱动+recomposition）与compose.ui实验性接口的快照失效说明，手机范围核心状态文档未读；iOS仅SwiftUI/UIKit框架页概述（模型到视图数据流、事件驱动命令式对照），细节正文未读。命令式路径（UIKit、ArkUI NDK/类Web；Android View缺证）与更新范围粒度均待补。版本均未核实，置信度全low。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | android-2（Wear tiles→widgets迁移）明确'心智模型从命令式布局构建器转向状态驱动、基于Compose的架构，UI更新通过recomposition处理'，并以声明式状态支持即时更新；android-1在实验性mediaQuery接口描述快照上下文中属性读取被跟踪、变化时作用域失效。手机/平板范围核心状态文档与命令式View对照未读。 | recommended |
| ios | documented_mechanism | indirect | SwiftUI框架页正文：'为每个平台声明应用界面与行为'，并提供'管理应用模型到视图控件数据流'的工具；UIKit页描述事件驱动UI、窗口/视图架构、主run loop与主线程限制，并声明可与SwiftUI无缝互嵌。两页均为概述级，状态绑定与更新触发细节未读正文。 | recommended |
| harmonyos | documented_mechanism | direct | ArkUI简介列出两种范式：ArkTS声明式'通过声明UI结构和状态，自动驱动界面渲染'、无需手动管理UI更新（官方推荐）；类Web范式（HML/CSS/JS）另存，范式可用性受应用模型与页面形态约束。NDK Picker文展示命令式节点操作createNode/setAttribute/addChild（API version 23起）。状态装饰器正文未读。 | recommended |

## android 条件与证据

适用范围：AndroidX androidx.compose.ui:ui 库版本：materialize Added in 1.5.0、LocalUiMediaScope 1.11.0、mediaQuery 1.12.0（实验性）；android-2涉及Wear OS 3-7与renderer 1.6+条件；API Level与启动日基线均未核实
条件：android-1的状态跟踪/失效描述位于实验性@ExperimentalMediaQueryApi mediaQuery接口（Added in 1.12.0），并非通用状态管理文档；android-2的'状态驱动+recomposition'表述针对Wear OS tiles→widgets迁移（Remote Compose），不直接针对手机/平板应用主UI；符号引入需对应AndroidX compose-ui库版本（1.5.0/1.11.0/1.12.0）；Wear部分条件依赖Wear OS版本（3-7）与renderer 1.6+
缺口：手机/平板范围的Compose核心状态机制正文（jetpack/compose/state、mutableStateOf、重组范围）未读，主证据来自Wear迁移文与实验性接口；绑定来源为androidx.compose.ui包，而核心状态API（remember/mutableStateOf）位于androidx.compose.runtime，绑定映射待核对；命令式View系统对照正文未读，'vs imperative'另一侧无直接证据；AndroidX版本与API Level未对照启动日基线核实
真机分类理由：机制有官方文档，但状态-显示一致性、recomposition范围等属运行时行为，文档未给出粒度；正式研究建议真机验证，本轮未实测。

- [Migrate from tiles to widgets](https://developer.android.com/training/wearables/widgets/migration)，UI Translation Tips，正文 78–85 行；获取 2026-09-05T10:39:19.749916+00:00；SHA a49ada6090d9d170e7a9b4f4f41310d2df848289747dcc187d8aebea40ece980。
- [Migrate from tiles to widgets](https://developer.android.com/training/wearables/widgets/migration)，Migrate Event Handling (Actions vs. Lambdas)，正文 106–112 行；获取 2026-09-05T10:39:19.749916+00:00；SHA a49ada6090d9d170e7a9b4f4f41310d2df848289747dcc187d8aebea40ece980。
- [androidx.compose.ui](https://developer.android.com/reference/kotlin/androidx/compose/ui/package-summary)，CompositionLocalAccessorScope.mediaQuery 正文，正文 122–124 行；获取 2026-09-05T14:47:51.634457+00:00；SHA 22c514216d7424b648bcef59721f193e6d10a57e08438004aea8142be2e603f5。
- [androidx.compose.ui](https://developer.android.com/reference/kotlin/androidx/compose/ui/package-summary)，Composables 表（derivedMediaQuery 包裹 derivedStateOf），正文 62–63 行；获取 2026-09-05T14:47:51.634457+00:00；SHA 22c514216d7424b648bcef59721f193e6d10a57e08438004aea8142be2e603f5。

## ios 条件与证据

适用范围：正文未标注具体iOS版本；SwiftUI/UIKit框架页无availability元数据，逐符号iOS适用性未核（Apple目录含macOS等多平台）
条件：ios-1/ios-2均为框架目录级页面，正文无版本/availability元数据；UIKit页声明适用iOS/iPadOS/tvOS，且UI类仅限主线程或主派发队列使用；SwiftUI与UIKit可互相嵌套（ios-2正文），具体集成约束未读
缺口：SwiftUI状态管理正文（@State/@Observable、Model data文章）未读，更新触发与更新范围仅有框架页概述；iOS逐符号适用性与最低可用版本未核实（框架页无availability，Apple目录含多平台）；UIKit命令式更新机制（如失效标记/主线程约束细节）未读正文
真机分类理由：SwiftUI数据流仅概述级证据，更新触发/范围属运行时行为；正式精研建议真机核对，本轮未实测。

- [SwiftUI](https://developer.apple.com/documentation/swiftui)，SwiftUI 页首声明（Declare the user interface and behavior），正文 1–3 行；获取 2026-09-05T10:32:56.278693+00:00；SHA ea4c521336979f6d195f66b051f6ff05a6ad1cb0b25a2ae1e8cca9fa5a462028。
- [SwiftUI](https://developer.apple.com/documentation/swiftui)，SwiftUI Overview（manage the flow of data from models down to views），正文 7–10 行；获取 2026-09-05T10:32:56.278693+00:00；SHA ea4c521336979f6d195f66b051f6ff05a6ad1cb0b25a2ae1e8cca9fa5a462028。
- [UIKit](https://developer.apple.com/documentation/uikit)，UIKit Overview（事件驱动、窗口视图架构、与SwiftUI互嵌），正文 7–13 行；获取 2026-09-05T10:33:00.563643+00:00；SHA c942fc385ed072637dad7b6e01b0eccc0d8ed7814a88301dee6e788a1bdf2fde。
- [UIKit](https://developer.apple.com/documentation/uikit)，Important（UIKit类仅主线程/主派发队列使用），正文 17–18 行；获取 2026-09-05T10:33:00.563643+00:00；SHA c942fc385ed072637dad7b6e01b0eccc0d8ed7814a88301dee6e788a1bdf2fde。

## harmonyos 条件与证据

适用范围：HarmonyOS官方指南（harmonyos-guides）；harmonyos-2标注Picker NDK组件自API version 23起、NODE_PICKER_DISPLAYED_ITEM_COUNT/ITEM_HEIGHT自API 26.0.0起；harmonyos-1未标注API版本；未对照启动日基线
条件：范式可用性受应用模型与页面形态约束：Stage模型页面仅声明式（推荐），FA模型卡片仅类Web（harmonyos-1表1）；NDK Picker命令式组件自API version 23起，部分属性自API 26.0.0起；声明式范式依赖ArkTS语言；类Web范式为HML/CSS/JS三段式；ArkUI Kit支持模拟器但与真机存在部分能力差异（差异表未涉及状态管理条目）
缺口：@State/@Prop/@Link等状态装饰器与依赖收集/最小更新单元的正文未读本批来源；harmonyos-1未标注适用API版本，范式与机制描述的版本适用范围未知；状态保存与组件生命周期协作（comparison_scope包含项）未在本批正文出现；OpenHarmony与HarmonyOS发行版差异未核（本批仅读华为官网HarmonyOS指南）
真机分类理由：自动驱动渲染为官方明示，但失效粒度与状态-显示一致性属运行时行为，且官方提示模拟器与真机存在能力差异；正式精研建议真机，本轮未实测。

- [ArkUI简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-overview)，分层API架构与选型建议-声明式开发范式（自动驱动界面渲染），正文 46–46 行；获取 2026-09-04T09:35:09+00:00；SHA 2952294b4c79149fd872282d72d574a90b973c55357aeac99138466cc733f111。
- [ArkUI简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-overview)，两种开发范式（声明式/类Web），正文 15–17 行；获取 2026-09-04T09:35:09+00:00；SHA 2952294b4c79149fd872282d72d574a90b973c55357aeac99138466cc733f111。
- [ArkUI简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-overview)，表1 支持的UI开发范式（应用模型×页面形态），正文 33–42 行；获取 2026-09-04T09:35:09+00:00；SHA 2952294b4c79149fd872282d72d574a90b973c55357aeac99138466cc733f111。
- [ArkUI简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-overview)，自定义能力与NDK开发（FrameNode/RenderNode/NDK接口），正文 49–52 行；获取 2026-09-04T09:35:09+00:00；SHA 2952294b4c79149fd872282d72d574a90b973c55357aeac99138466cc733f111。
- [使用滑动选择器 (Picker)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-picker)，概述（API version 23起提供Picker NDK组件；API 26.0.0起新属性），正文 5–5 行；获取 2026-09-04T09:35:09+00:00；SHA c9f9ae6df8fb68edbf1b681bfa01de6a2624900491e66b58339ea4db344990b7。
- [使用滑动选择器 (Picker)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-picker)，创建Picker（createNode/setAttribute命令式节点操作），正文 13–13 行；获取 2026-09-04T09:35:09+00:00；SHA c9f9ae6df8fb68edbf1b681bfa01de6a2624900491e66b58339ea4db344990b7。

## 待验证差异假设

- programming_model：三平台官方文档均以'声明式、状态驱动UI'为主推范式：Android Compose'UI更新通过recomposition处理'（Wear迁移文），HarmonyOS ArkTS声明式'通过声明UI结构和状态，自动驱动界面渲染'，SwiftUI概述'声明界面并管理模型到视图的数据流'；三者均宣称开发者无需手动管理UI更新/渲染。；待核：SwiftUI与Compose的'无需手动管理'程度及例外（手动失效手段）未读正文；HarmonyOS明确标注'推荐'等级，Android/iOS本批正文未标注范式推荐等级；三平台声明式范式的状态可变性约束差异未读。
- api_surface：声明式范式外的命令式UI路径定位不同：iOS保留UIKit为与SwiftUI并列的完整事件驱动框架（可互相嵌套，主线程限制）；HarmonyOS的命令式操作体现为ArkUI框架内NDK C/C++节点级接口（createNode/setAttribute/addChild）与类Web范式，属同框架的扩展/兼容路径而非并列完整框架。；待核：Android命令式View系统对照正文缺失，无法假设三平台对称；ArkUI NDK/类Web范式与UIKit是否构成同等定位的'命令式路径'待定性；命令式与声明式混用时的状态一致性保证未读正文。
- limits_precision：状态变化→界面更新的失效范围描述粒度不同：Android明确快照感知上下文中属性读取被跟踪、变化时对应作用域失效（invalidated）；HarmonyOS仅概述'自动驱动界面渲染'，未在本批正文给出失效粒度；SwiftUI框架页亦未描述更新范围——三平台更新范围机制可能存在实质差异（can/粒度层面），待专门正文核对。；待核：三平台失效粒度/更新范围专门正文均未读（Compose重组范围、SwiftUI视图身份、ArkUI最小更新单元）；android-1的失效描述限于实验性mediaQuery接口，能否外推至通用状态机制未知。

范围缺口：更新触发与更新范围的专门正文（Compose重组范围、SwiftUI视图身份/diffing、ArkUI最小更新单元）三平台均未读；状态保存与组件生命周期协作维度（comparison_scope包含项）本批来源均未覆盖；Android手机/平板范围命令式View系统与Compose互操作正文缺失；iOS UIKit具体更新机制未读；三平台命令式对照不完整；HarmonyOS状态装饰器与绑定细节正文未读，harmonyos-1未标注适用API版本；启动日基线未固定，三平台版本条件均未核实

后续优先级：P1；Android绑定包为androidx.compose.ui而核心状态API位于compose.runtime，且手机范围机制证据来自Wear迁移文与实验性接口；iOS仅目录级框架页概述——存在映射偏差与机制误判风险，属关键缺口，需优先补读三平台状态管理正文（Compose state指南、SwiftUI状态与数据流、ArkUI状态装饰器）并核对版本基线。

逐条引用及原文摘录见同目录 normalized.json。
