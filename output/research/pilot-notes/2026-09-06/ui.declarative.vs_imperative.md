# ui.declarative.vs_imperative 研究试点笔记（2026-09-06）

复核版：原始模型交付保存在 `output/research/pilot-originals/2026-09-06/`。协调者已收紧节点拆分建议、范式归类和真机边界，并自动校正证据元数据；本文仍为低置信诊断草稿，不是正式确认结果。

执行条件：模型 volcengine/glm-5.3，无子代理；候选来自 `context ui.declarative.vs_imperative --limit 5`；补抓 URL 0 个（所读正文均已在库）；API 费用与 token 消耗本会话不可观测。无实测，全部 low/待核实。

## 范围与节点结构审查

节点定义"将应用状态变化同步为界面变化，并维护状态与显示的一致性"。本轮仅做静态文档观察，不开发 HarmonyOS 应用，不填比较槽位。材料涉及编程范式、状态同步、状态保存/生命周期和互操作；它们不因分属不同文档就必须拆成四个特性。本轮以状态到界面的一致性为主单元；其他内容优先放入既有比较维度，只有形成独立用户任务和可观察结果时才提出新节点并经范围复核。本轮覆盖范式、状态同步及部分互操作；生命周期正文未读，不调整正式特性树。

## 三条官方文档观察（每平台一条）

Android：官方将"声明式/命令式"表述为同一 Android 内并存的编程范式，而非互斥平台能力。《Thinking in Compose》称 Compose 为 declarative UI Toolkit；"The declarative programming paradigm"一节把命令式描述为历史做法（findViewById+setText 手工改视图树，易漏改、产生非法状态），声明式则"概念上重建整个屏幕、只应用必要变化"，由框架选择重绘范围（recomposition）。该页未给 Compose/View 互操作范围。另读 androidx.compose.ui 包索引：纯 API 清单，无直接证据价值，印证 API 名称不能单独证明行为。

iOS：Technology Overviews《SwiftUI apps》明示 SwiftUI 的 declarative programming model，"SwiftUI assumes responsibility for your interface and making sure it stays consistent with your data"——状态与显示一致性由框架承担；并写明"改变数据、让 SwiftUI 处理更新"。互操作：可在 UIKit/AppKit 应用中显示 SwiftUI 视图，反之亦然，可渐进采纳。SwiftUI 框架页同样写明可与 UIKit/AppKit/WatchKit 对象集成。两页均未附 iOS 版本适用性元数据，iOS 逐符号适用性未核对，保留缺口。

HarmonyOS：《ArkUI简介》声明 ArkUI 提供两种开发范式——基于 ArkTS 的声明式开发范式与兼容 JS 的类 Web 开发范式，且支持矩阵按"应用模型×页面形态"约束（表1：Stage 页面仅声明式；FA 页面两者皆可；Stage 卡片两者皆可；FA 卡片仅类Web）。声明式范式"通过声明UI结构和状态，自动驱动界面渲染……无需手动管理UI更新"；另有 NDK（C/C++）构建 UI 与 FrameNode 等自定义节点。第二篇《applySync/flushUpdates/flushUIUpdates》显示状态管理 V2 修改状态变量后不立即标脏（抛 Promise 微任务），与 animateTo 即时刷新冲突可致动效首帧异常，需 API version 22 起的同步刷新接口——声明式框架内部存在命令式补口与时序契约细节。

### 证据表（SHA-256 为本地规范化正文哈希，已逐文件重算核对一致；raw_sha256 存于 corpus.sqlite）

| 平台 | 文档与章节 | 官方 URL | 本地正文路径（相对仓库根） | SHA-256 | 获取时间(UTC) |
| --- | --- | --- | --- | --- | --- |
| Android | Thinking in Compose, §The declarative programming paradigm | https://developer.android.com/develop/ui/compose/mental-model | docs-raw/research/2026-09-06/08ab851ce941685db75cebf52710bc9725f7e0a19da0cd3d10e5fedf97e6a1b9/eef2acfc0a110286d34ebc0428b02684734e8de051951f4f074d2ee6b0dd3349/document.md | eef2acfc0a110286d34ebc0428b02684734e8de051951f4f074d2ee6b0dd3349 | 2026-09-05T10:25:05.867938+00:00 |
| Android | androidx.compose.ui 包索引（弱证据，仅目录） | https://developer.android.com/reference/kotlin/androidx/compose/ui/package-summary | docs-raw/research/2026-09-06/54ad3d3d272158f2b0a3aebd5232b56a87a85a4919c643dfd9f443e1317d3351/22c514216d7424b648bcef59721f193e6d10a57e08438004aea8142be2e603f5/document.md | 22c514216d7424b648bcef59721f193e6d10a57e08438004aea8142be2e603f5 | 2026-09-05T14:47:51.634457+00:00 |
| iOS | SwiftUI apps (Technology Overviews), §Discussion/§Declare your interface/§UIKit 混用条目 | https://developer.apple.com/documentation/technologyoverviews/swiftui | docs-raw/research/2026-09-06/d851e84beb3a64905cdf8378ff6559ff85a449b80c423fc2bafefeb28af222eb/9b9c81e0fbad7966a51879bfaa3153c325c75cfd7d8127dd5fb804bb06e69493/document.md | 9b9c81e0fbad7966a51879bfaa3153c325c75cfd7d8127dd5fb804bb06e69493 | 2026-09-05T10:26:40.546104+00:00 |
| iOS | SwiftUI 框架页, §Overview | https://developer.apple.com/documentation/swiftui | docs-raw/research/2026-09-06/692affe97a4bae3f761eeb2ed58fe8ba704b73e0f68ee37ad1ade11808277338/ea4c521336979f6d195f66b051f6ff05a6ad1cb0b25a2ae1e8cca9fa5a462028/document.md | ea4c521336979f6d195f66b051f6ff05a6ad1cb0b25a2ae1e8cca9fa5a462028 | 2026-09-05T10:32:56.278693+00:00 |
| HarmonyOS | ArkUI简介, §两种开发范式/§不同应用类型支持的开发范式(表1)/§分层API架构与选型建议 | https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-overview | docs-raw/research/2026-09-06/62692cc35718abb5e257150e27062ab1d65cf3b009fbcd41acc4e647b21752e2/2952294b4c79149fd872282d72d574a90b973c55357aeac99138466cc733f111/document.md | 2952294b4c79149fd872282d72d574a90b973c55357aeac99138466cc733f111 | 2026-09-04T09:35:09+00:00 |
| HarmonyOS | applySync/flushUpdates/flushUIUpdates接口：同步刷新, §概述/§使用规则 | https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates | docs-raw/research/2026-09-06/d2223d1db5c4a8efd95ddac5f379bb82bd8fc678a9ce6dd31d1b42ad78832d42/e9410d3b808c49ee7aa4c0794cea1528f2ac5ff161f1e3272d757a0d06cadb4a/document.md | e9410d3b808c49ee7aa4c0794cea1528f2ac5ff161f1e3272d757a0d06cadb4a | 2026-09-04T09:35:09+00:00 |

## 两个具体待证差异/反例

1. 互操作约束差异（待证）：Apple 官方明示 SwiftUI↔UIKit 双向、可渐进采纳；HarmonyOS 范式选择受 Stage/FA×页面/卡片矩阵约束；Android 的 Compose↔View 互操作正文本轮未读（库中 Interoperability APIs、Using Views in Compose 等 ready 未读）。三平台"混用粒度"（应用级/页面级/卡片级）差异需读齐互操作正文后立论，不可由 AndroidView、UIViewRepresentable、EmbeddedComponent 等名称推定等价。
2. 声明式框架的时序反例（待证）：HarmonyOS V2 状态更新异步标脏，animateTo 首帧问题需 applySync（API 22+）；Android Compose 重组存在可跳过、乱序执行等时序规则（同页锚点未逐段核读）；SwiftUI 更新时序契约无正文证据。若比较单元定为"状态修改→界面刷新时序"，该差异需实测。

## 需补文档与真机的独立判断

- 优先补读（均在本地库，ready）：Android《Interoperability APIs》《Using Views in Compose》《Using Compose in Views》《Lifecycle in Compose》；iOS《UIKit integration》及 UIViewRepresentable 符号页，并核对 iOS availability；HarmonyOS《状态管理V1/V2更新差异》《类Web开发范式 (ui-js-overview)》《Stage/FA 应用模型》。
- 版本基线：最新正式版基线未完成（research_policy 的发布入口未读）；Compose BOM/AndroidX、iOS release notes、API 22 对应的 HarmonyOS 发行版均待固定后复核。
- 真机判断：范式共存、互操作 API 存在性属静态契约，补文档即可核实，无需真机；状态→刷新时序、动效首帧、状态保存/恢复依赖运行观测，纳入比较时应真机实测。ArkUI 文档已提示模拟器与真机有差异。

## 测试步骤（如需；均未执行，不写 pass）

- Android：单 Activity 混用 ComposeView 与 XML/RecyclerView；修改 State 观察重组范围；验证 rememberSaveable 在配置变更/进程重建后恢复。记录机型、Android 版本、Compose BOM。
- iOS：UIKit 内嵌 UIHostingController，SwiftUI 内用 UIViewRepresentable 包自定义 UIView；修改 @State 观察更新时机；验证 @SceneStorage 恢复。记录 iPhone 机型、iOS 版本。
- HarmonyOS：先核实选定正式手机系统与 API 22+ 的配对，再检查 Stage 页面及卡片约束、复现 V2 状态变量与 animateTo 首帧问题并以 applySync 对比。模拟器只可用于预检查，不能代替标记为“真机复核”的实际手机记录；保存手机型号、系统构建号、SDK/API 和操作证据，其他设备形态单列。

## 状态

已读正文支持把声明式作为编程模型/开发范式讨论，但不能据此断言三平台具有相同的命令式路径或互操作范围；尤其 ArkUI 的“类 Web”不能直接等同于“命令式”。因基线、逐符号适用性与互操作正文未读齐，全部 low/待核实，不写 confirmed，不声称平台独有、不支持或完全等价。
