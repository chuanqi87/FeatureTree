# 系统智能建议 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

Android 冻结来源仅 ML Kit Smart Reply（Google 生态库，英语会话、最多3条回复、API 23+），映射到系统级节点待确认；iOS 读到 Apple Intelligence Smart Reply（UIKit 会话上下文）与 Journaling Suggestions（entitlement+系统通知）两个系统机制，但文档未标注 iOS 版本；HarmonyOS 两篇来源（车机导航流转、性能测试）与本节点无关，unknown。差异假设：调用模型、生成限制、分发条件。全部 low。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | possible_mapping | direct | ML Kit Smart Reply 文档化上下文回复建议机制：应用传入按时间排序的会话历史，端侧模型在识别为英语且无敏感话题时最多生成 3 条回复建议；bundled 静态链接或 unbundled 经 Google Play services 下载（beta）。属 Google 生态库而非系统服务，映射至本系统级节点待确认。 | recommended |
| ios | documented_mechanism | direct | 读到两个系统机制：Smart Reply 由系统 Apple Intelligence 生成，应用将 UIMessageConversationContext/UIMailConversationContext 绑定到输入框并在收发消息时更新，系统在特定情形自动给出建议，长文本需应用自行用模型展开；Journaling Suggestions 经系统周期通知推荐日记时刻，需 entitlement 与 URL 格式配置。 | recommended |
| harmonyos | unknown | missing | 两篇冻结来源分别为车机导航流转（CarKit：碰一碰/上车/车内导航流转、smartMobilityEvent 监听）与 DevEco Testing 性能测试（智能遍历算法、性能指标检测），均不涉及系统级上下文建议或快捷操作，未建立任何机制判断。 | unassessed |

## android 条件与证据

适用范围：ML Kit 指南快照（2026-09-05 抓取）：要求 minSdkVersion 23+；示例库版本 bundled com.google.mlkit:smart-reply 17.0.4、unbundled play-services-mlkit-smart-reply 16.0.0-beta1；未绑定启动日最新 Android 正式版基线（version_verified=false）。
条件：应用内集成 ML Kit 库：bundled 模型静态链接（约 +5.7MB）或 unbundled 经 Google Play services 动态下载（约 +200KB，beta，首次使用前需下载完成）；要求 Android API level 23 及以上；仅英语会话生成建议；模型基于最近最多 10 条消息，检测敏感话题或置信不足时可能无结果；最多返回 3 条建议；被建议回复的最后一条消息应来自对方用户
缺口：ML Kit 属 Google 生态服务（Play services/bundled），非 AOSP 系统 SDK；本节点 layer=os，生态库映射到系统级节点需确认；冻结来源未覆盖 Android 系统级建议机制（如系统通知智能回复、App Prediction/App Actions/动态快捷方式推荐）；未核实启动日最新 ML Kit / Play services 版本与最新 Android 正式版手机基线；仅覆盖文本回复建议，快捷操作（quick actions）维度无证据
真机分类理由：建议内容由端侧模型运行时决定（语言识别、敏感话题过滤、置信度、数量上限），静态文档无法验证实际输出；后续精研需真机会话验证，本轮仅分类不设计用例。

- [Generate smart replies with ML Kit on Android](https://developers.google.com/ml-kit/language/smart-reply/android)，Overview — pass log of recent messages; English & non-sensitive topic -> up to three replies，正文 5–8 行；获取 2026-09-05T10:51:03.207349+00:00；SHA 0ed9df2fc4224b9f27c64e1580b2751c3af7380c5205683c0c42f12f7effb21b。
- [Generate smart replies with ML Kit on Android](https://developers.google.com/ml-kit/language/smart-reply/android)，Bundled vs unbundled library comparison table; unbundled version offered in beta，正文 16–25 行；获取 2026-09-05T10:51:03.207349+00:00；SHA 0ed9df2fc4224b9f27c64e1580b2751c3af7380c5205683c0c42f12f7effb21b。
- [Generate smart replies with ML Kit on Android](https://developers.google.com/ml-kit/language/smart-reply/android)，Before you begin — API requires Android API level 23 or above，正文 36–37 行；获取 2026-09-05T10:51:03.207349+00:00；SHA 0ed9df2fc4224b9f27c64e1580b2751c3af7380c5205683c0c42f12f7effb21b。
- [Generate smart replies with ML Kit on Android](https://developers.google.com/ml-kit/language/smart-reply/android)，Get message replies — SmartReplyGenerator.suggestReplies(conversation)，正文 141–150 行；获取 2026-09-05T10:51:03.207349+00:00；SHA 0ed9df2fc4224b9f27c64e1580b2751c3af7380c5205683c0c42f12f7effb21b。
- [Generate smart replies with ML Kit on Android](https://developers.google.com/ml-kit/language/smart-reply/android)，SmartReplySuggestionResult contains up to three suggested replies to present to your user，正文 192–194 行；获取 2026-09-05T10:51:03.207349+00:00；SHA 0ed9df2fc4224b9f27c64e1580b2751c3af7380c5205683c0c42f12f7effb21b。
- [Smart reply](https://developers.google.com/ml-kit/language/smart-reply)，Limitations & How the model works — English only, sensitive topics suppressed, up to 10 recent messages, up to three replies，正文 21–39 行；获取 2026-09-05T10:54:35.391097+00:00；SHA 646d4eddf4b7b200f1775b6bfb489d843d866fbe9fc69aa21c0e0a829b1b5155。

## ios 条件与证据

适用范围：两篇 Apple 文档（2026-09-05 抓取）均未标注最低 iOS 版本、Apple Intelligence 机型条件或 iPad 适用性；符号级 availability 需另行核对，未固定启动日基线。
条件：Smart Reply：应用构造并维护会话上下文（线程ID、参与者、条目）绑定到输入框 conversationContext；键盘会话初始化使用一次，焦点变化后需重设并通知 inputDelegate；系统仅在特定情形生成：输入框为空、最后一条来自对方、近期纯文本消息；邮件：本人为直接收件人、未回复过、发件人与收件人地址不同；Journaling Suggestions：需 com.apple.developer.journal.allow entitlement、JSNotificationURLFormat 通用链接，且用户在设置中开启通知；长文本邮件建议需应用自持模型基于 UISmartReplySuggestion 展开
缺口：文档未标注 iOS 最低版本与 Apple Intelligence 机型要求，无法判断手机/平板（phone/tablet）覆盖；Smart Reply 是否需要额外能力开关/entitlement 未在文中说明；Journaling Suggestions 与 Smart Reply 符号级 availability（DocC 元数据）未核对；App Intents 等其他系统快捷建议方向不在冻结来源内
真机分类理由：Smart Reply 触发情形与键盘会话行为、Journaling Suggestions 的系统通知和设置开关均属系统运行时行为，静态文档不足以验证；后续精研需真机，本轮仅分类。

- [Adopting Smart Reply in your messaging or email app](https://developer.apple.com/documentation/uikit/adopting-smart-reply-in-your-messaging-or-email-app)，Discussion — Messages and Mail use Apple Intelligence for Smart Reply; adoption steps，正文 5–13 行；获取 2026-09-05T11:19:47.440203+00:00；SHA 07ace0f60be34551c89a43c751628e492f5c6a518b763f2222f79f7c0d3e563e。
- [Adopting Smart Reply in your messaging or email app](https://developer.apple.com/documentation/uikit/adopting-smart-reply-in-your-messaging-or-email-app)，Create a conversation context — UIMessageConversationContext / UIMailConversationContext，正文 14–26 行；获取 2026-09-05T11:19:47.440203+00:00；SHA 07ace0f60be34551c89a43c751628e492f5c6a518b763f2222f79f7c0d3e563e。
- [Adopting Smart Reply in your messaging or email app](https://developer.apple.com/documentation/uikit/adopting-smart-reply-in-your-messaging-or-email-app)，Attach conversation context to text view or field; keyboard uses it once per session，正文 72–80 行；获取 2026-09-05T11:19:47.440203+00:00；SHA 07ace0f60be34551c89a43c751628e492f5c6a518b763f2222f79f7c0d3e563e。
- [Adopting Smart Reply in your messaging or email app](https://developer.apple.com/documentation/uikit/adopting-smart-reply-in-your-messaging-or-email-app)，Understand when the system generates Smart Reply suggestions (messaging & mail circumstances)，正文 118–133 行；获取 2026-09-05T11:19:47.440203+00:00；SHA 07ace0f60be34551c89a43c751628e492f5c6a518b763f2222f79f7c0d3e563e。
- [Receiving journaling suggestions system notifications](https://developer.apple.com/documentation/journalingsuggestions/receiving-journaling-suggestions-from-system-notifications)，Overview — system periodic notifications launch the selected journal app with suggestion details，正文 5–9 行；获取 2026-09-05T10:23:14.006470+00:00；SHA 85cf5388ed9e8eb6d2d5c2e52df3f257abb4fabd43aaf7cf73fc61e90b810f60。
- [Receiving journaling suggestions system notifications](https://developer.apple.com/documentation/journalingsuggestions/receiving-journaling-suggestions-from-system-notifications)，Entitlement com.apple.developer.journal.allow note; JSNotificationURLFormat universal link requirement，正文 21–25 行；获取 2026-09-05T10:23:14.006470+00:00；SHA 85cf5388ed9e8eb6d2d5c2e52df3f257abb4fabd43aaf7cf73fc61e90b810f60。

## harmonyos 条件与证据

适用范围：不适用：冻结来源与节点无关，未读到任何可核对的 HarmonyOS 系统/SDK 版本条件。
条件：无可报告条件：冻结来源未包含与系统智能建议相关的机制或适用条件
缺口：冻结两篇来源（车机导航流转、性能测试）与本节点无关，未建立机制判断；未检索小艺建议/Intents Kit/情景感知等 HarmonyOS 官方系统建议文档（本轮不联网补查）；HarmonyOS 与 OpenHarmony 发行版差异未涉及；手机/平板设备条件未读取
真机分类理由：未读到任何相关机制文档，缺少评估基础；待定位 HarmonyOS 官方对应功能后再评估真机需求。

- [导航流转至车机](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-navi-hop)，场景介绍 — 碰一碰/上车/车内导航流转场景（车机流转主题，非智能建议），正文 1–13 行；获取 2026-09-04T09:35:09+00:00；SHA 7b9c7dfe7a0ad1426f2a18551154f3f2359fd302f7a98f6a9620ed4b0d41cd3c。
- [导航流转至车机](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-navi-hop)，接口说明 — registerSystemNavigationListener、smartMobilityEvent 等 CarKit 接口，正文 17–27 行；获取 2026-09-04T09:35:09+00:00；SHA 7b9c7dfe7a0ad1426f2a18551154f3f2359fd302f7a98f6a9620ed4b0d41cd3c。
- [性能测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/performance-testing)，性能基础质量测试 — 智能遍历算法与性能指标检测（与本节点无关），正文 1–7 行；获取 2026-09-05T10:24:36.266176+00:00；SHA b55f509323467a527b1f89aeb45701c50aa7ffd69176251ebb24d863431ef8bf。

## 待验证差异假设

- programming_model：Android 由应用显式调用 SmartReplyGenerator.suggestReplies(会话历史) 取回建议数组并自行展示；iOS Smart Reply 由系统 Apple Intelligence 生成——应用把会话上下文绑定到输入框，系统在特定情形自动产生建议（长文本经 insertInputSuggestion 委托回调应用）。；待核：iOS 建议的实际呈现通道（键盘候选/输入建议列表）未在冻结文档完整说明，需读 UITextInputTraits.conversationContext 等符号页；Android 系统侧是否另有自动注入建议的机制（如通知智能回复）不在冻结来源内；HarmonyOS 机制未知，暂无法三方比较。
- limits_precision：Android 文档给出硬性限制：仅英语、敏感话题不出建议、最多 3 条、基于最近最多 10 条消息；iOS 文档仅列触发情形（空输入框、最后一条来自对方、近期纯文本；邮件另有收件人条件），未标注语言限制或数量上限——两平台约束类型不同。；待核：iOS Smart Reply 是否有语言限制与建议数上限，需符号页或其他官方文档核对；Apple Intelligence 可用性对 iOS 触发情形的实际影响未在冻结文档说明。
- availability：部署条件不同：Android 依赖 ML Kit 库分发（bundled +5.7MB 或 unbundled 经 Google Play services 动态下载、beta、API 23+）；iOS 为系统集成机制，Journaling Suggestions 需专用 entitlement，Smart Reply 依赖 Apple Intelligence 但文档未列机型/系统门槛。；待核：iOS Apple Intelligence 机型/最低系统门槛需版本资料核对；无 Google Play services 设备上 unbundled ML Kit 可用性未验证；HarmonyOS 侧无来源，无法比较。

范围缺口：HarmonyOS 平台无相关冻结来源，本轮只能 unknown；需专项检索小艺建议、Intents Kit、智能提醒等官方文档；Android 证据为 Google 生态 ML Kit 库；OS 层（AOSP/系统服务）建议机制无文档，layer=os 映射待确认；iOS 版本适用性（Apple Intelligence 最低系统/机型、Journaling Suggestions 最低版本、iPad 支持）未在冻结文档标注；快捷操作（quick actions）方向三平台证据均不足；本轮仅覆盖文本回复建议与日记建议

后续优先级：P1；HarmonyOS 完全无相关来源（关键缺口），且 Android 存在生态库映射到系统级节点的高风险映射，iOS 版本条件缺失；需优先精研以建立三方可比基础。

逐条引用及原文摘录见同目录 normalized.json。
