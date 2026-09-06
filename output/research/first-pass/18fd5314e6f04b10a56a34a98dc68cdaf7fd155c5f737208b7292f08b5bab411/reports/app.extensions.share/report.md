# 分享扩展 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台文档初判：iOS 读到 share extension 官方机制（Xcode 模板、NSExtension/INSendMessageIntent 捐赠、SLComposeServiceViewController 预填）；HarmonyOS 读到 ShareExtensionAbility（三方可实现、系统服务管理）及 Share Kit 碰一碰跨设备分享；Android 两篇冻结来源（Firebase 扩展、KTX）与本节点无关，未能建立判断，不据此称不支持。差异假设 3 条均限 iOS/HarmonyOS；全部 low，未确认支持状态。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | unknown | missing | 两篇冻结来源为 Firebase 服务端扩展发布指南与 AndroidX KTX Kotlin 扩展库文档，均不涉及应用作为分享目标或接收分享内容的机制；本轮未能建立 Android 判断，不据此声称不支持。 | unassessed |
| ios | documented_mechanism | direct | 读到 iOS Share Extension 机制：Xcode iOS 面板模板添加扩展 target；Info.plist 的 NSExtension.IntentsSupported 声明 INSendMessageIntent；SLComposeServiceViewController 子类经 extensionContext.intent 预填界面；应用与扩展捐赠意图后会话进入分享面板建议列表。 | recommended |
| harmonyos | documented_mechanism | direct | 读到 ShareExtensionAbility：系统定义的分享扩展组件、提供分享模板服务扩展、允许三方应用实现、无独立 Extension 沙箱；ExtensionAbility 不能被应用直接启动而由系统服务拉起管理。另读到 Share Kit 碰一碰跨设备文件分享（on('knockShare')/on('dataReceive')、UTD 类型匹配）。 | recommended |

## android 条件与证据

适用范围：不适用：未读到相关机制正文，无版本或条件可记录。
条件：无：本轮无 Android 相关机制正文可提取运行条件。
缺口：未检索到应用分享目标机制正文：ACTION_SEND intent 过滤、分享快捷方式/DirectShare 等均不在冻结来源，需从 developer.android.com 补查。；Firebase Extensions 属服务端 Cloud Functions 产品，不能据其推断 Android 应用侧分享行为。；Android KTX 为 Kotlin 语法扩展库文档，与本节点无关联，不构成证据。
真机分类理由：未建立任何 Android 机制文档判断，无从评估真机需求；待补充官方分享文档后再分类。

- [Extension publisher overview](https://firebase.google.com/docs/extensions/publishers)，Extension publisher overview > 引言：Firebase Extension 由 Cloud Functions 代码组成，响应 HTTP/Firebase 触发事件并发布到 Extensions Hub，正文 1–12 行；获取 2026-09-05T11:12:51.999778+00:00；SHA 4022a98b968df02d8f6bfe37e22d2035fdf81326707a3e2ec9d5f235f72618eb。
- [Android KTX Part of Android Jetpack .](https://developer.android.com/kotlin/ktx)，Android KTX > 引言：KTX 是 Jetpack 及其他 Android 库附带的 Kotlin 扩展函数集，正文 1–8 行；获取 2026-09-05T10:33:23.228362+00:00；SHA 9782e9753510ee6fdfaa3212a2692ba57c468b27724aca766036e9fcf35082fb。

## ios 条件与证据

适用范围：Apple 文档快照（2026-09-05）；正文明示 iOS 16+ 用于图片识人优先建议、TRUEPREDICATE 仅限调试期；模板标注 iOS 面板，最低 iOS 版本未在正文给出。
条件：用 Xcode iOS 面板的 share extension 模板向应用添加扩展 target。；Info.plist 声明 NSExtension.IntentsSupported 包含 INSendMessageIntent 才会话进入建议。；需在应用及其 share extension 中捐赠 INSendMessageIntent 才生成分享面板建议。；提交审核前须将 NSExtensionActivationRule 由 TRUEPREDICATE 替换为有效激活规则。；iOS 16+ 且启用相关建议设置时，图片分享按识别到的人物优先建议。
缺口：App Extension Programming Guide 正文（生命周期、内存上限）未冻结，仅有 archive 链接被引用。；NSExtensionActivationRule 有效语法与可接收数据类型细则未读到。；最低 iOS 版本与 DocC availability 未核对；建议机制依赖 SiriKit intents 的适用范围未展开。；ios-2 为 Final Cut Pro（macOS 专业视频）工作流扩展文档，其 Share extension 表述的 iOS 适用性未核实。
真机分类理由：分享面板建议出现、意图预填与激活规则生效属运行时行为，静态文档不足以完全核实；本轮未实测，精研时建议真机验证。

- [Supporting suggestions in your app’s share extension](https://developer.apple.com/documentation/foundation/supporting-suggestions-in-your-app-s-share-extension)，Discussion：分享面板建议来源与 INSendMessageIntent 捐赠条件、扩展经 intent 预填，正文 11–17 行；获取 2026-09-05T10:51:39.657228+00:00；SHA 34fcdb3ac04e93c66a1a119555c5eb0b35e6b30b0255427f075ae371c53687ae。
- [Supporting suggestions in your app’s share extension](https://developer.apple.com/documentation/foundation/supporting-suggestions-in-your-app-s-share-extension)，Add a share extension to your app / Support the send message intent：Xcode iOS 模板与 Info.plist IntentsSupported、TRUEPREDICATE 调试提示，正文 23–33 行；获取 2026-09-05T10:51:39.657228+00:00；SHA 34fcdb3ac04e93c66a1a119555c5eb0b35e6b30b0255427f075ae371c53687ae。
- [Supporting suggestions in your app’s share extension](https://developer.apple.com/documentation/foundation/supporting-suggestions-in-your-app-s-share-extension)，Donate a send message intent：仅在用户收发消息时捐赠 INSendMessageIntent，正文 35–39 行；获取 2026-09-05T10:51:39.657228+00:00；SHA 34fcdb3ac04e93c66a1a119555c5eb0b35e6b30b0255427f075ae371c53687ae。
- [Supporting suggestions in your app’s share extension](https://developer.apple.com/documentation/foundation/supporting-suggestions-in-your-app-s-share-extension)，iOS 16+ 图片分享优先建议图片中识别的人物（建议来自 Apple 设置启用时），正文 68–68 行；获取 2026-09-05T10:51:39.657228+00:00；SHA 34fcdb3ac04e93c66a1a119555c5eb0b35e6b30b0255427f075ae371c53687ae。
- [Supporting suggestions in your app’s share extension](https://developer.apple.com/documentation/foundation/supporting-suggestions-in-your-app-s-share-extension)，Populate your share extension's interface：SLComposeServiceViewController 模板经 extensionContext.intent 读取 INSendMessageIntent 预填，正文 77–77 行；获取 2026-09-05T10:51:39.657228+00:00；SHA 34fcdb3ac04e93c66a1a119555c5eb0b35e6b30b0255427f075ae371c53687ae。
- [Designing Workflow Extensions](https://developer.apple.com/documentation/professional-video-applications/designing-workflow-extensions)，Designing Workflow Extensions：与 workflow 扩展对比，Share extension 通常以模态会话运行（macOS 专业视频文档，iOS 适用性未核实），正文 7–7 行；获取 2026-09-05T11:17:05.921799+00:00；SHA f951e4a48d69ca7b1d2a6506375d87c48803b332c5069dcb6b042a267765d8e5。

## harmonyos 条件与证据

适用范围：ExtensionAbility 总览未标注 ShareExtensionAbility 引入的 API 版本；碰一碰正文标明 HarmonyOS 6.0.0 Beta1+ 手机/电脑、电脑 API 26.0.0+ 精准碰一碰、dataReceive 仅 2in1 设备。
条件：ShareExtensionAbility 允许三方应用实现，生命周期由系统服务管理，应用不能直接启动。；碰一碰分享依赖 SystemCapability.Collaboration.HarmonyShare 系统能力（canIUse 校验）。；on('dataReceive') 当前仅 2in1 设备类型可调用，其他设备类型返回 801 错误码。；手机碰电脑需登录同一华为账号；精准碰一碰需电脑 API 26.0.0 及以上。；文件分享场景须传 uri 与 utd；内容与文件混合分享不被支持。
缺口：js-apis-app-ability-shareextensionability API 正文未冻结，接口、module.json5 配置与版本引入未读。；Share Kit 系统分享与 ShareExtensionAbility 的关系未澄清。；HarmonyOS 与 OpenHarmony 发行版适用性未分别核对。；碰一碰为跨设备分享，与本节点'应用间分享目标'定义的映射待确认。
真机分类理由：ShareExtensionAbility 被系统拉起的实际行为、版本可用性与 2in1 设备限制需真机核对；本轮仅静态文档初判。

- [ExtensionAbility组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)，ExtensionAbility组件 > 概述：面向特定场景的应用组件，类型由系统定义，开发者不能直接继承，正文 3–5 行；获取 2026-09-04T09:35:09+00:00；SHA d8486a77883f70af10fde21445db5421ce7959ddbe2b5d1988c01f1b1b2176d0。
- [ExtensionAbility组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)，ExtensionAbility类型说明表：ShareExtensionAbility 分享扩展组件，提供分享模板服务扩展，允许三方实现，无独立沙箱，正文 25–25 行；获取 2026-09-04T09:35:09+00:00；SHA d8486a77883f70af10fde21445db5421ce7959ddbe2b5d1988c01f1b1b2176d0。
- [ExtensionAbility组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)，访问指定类型的ExtensionAbility组件：均不能被应用直接启动，由系统管理服务拉起并管理生命周期，正文 62–62 行；获取 2026-09-04T09:35:09+00:00；SHA d8486a77883f70af10fde21445db5421ce7959ddbe2b5d1988c01f1b1b2176d0。
- [碰一碰文件分享](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-knock-file-share)，概述：HarmonyOS 通过 Share Kit 提供分享功能，API 26.0.0+ 电脑支持精准碰一碰，正文 5–5 行；获取 2026-09-05T10:41:42.267608+00:00；SHA cfe47c54ac64e0df3f24a9b1a874a31410b23dcddb52d6a5c062f02e69628832。
- [碰一碰文件分享](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-knock-file-share)，发起分享 > 分享数据构建：SharedRecord 必传 uri 与 utd，UTD 用于系统匹配精确目标应用，正文 33–37 行；获取 2026-09-05T10:41:42.267608+00:00；SHA cfe47c54ac64e0df3f24a9b1a874a31410b23dcddb52d6a5c062f02e69628832。
- [碰一碰文件分享](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-knock-file-share)，接收文件：on('dataReceive') 仅 2in1 设备可调用，其他设备返回 801；需传窗口 ID 与 capabilities，正文 144–146 行；获取 2026-09-05T10:41:42.267608+00:00；SHA cfe47c54ac64e0df3f24a9b1a874a31410b23dcddb52d6a5c062f02e69628832。

## 待验证差异假设

- programming_model：接收分享内容的编程模型差异假设：iOS share extension 是 Xcode 模板创建的独立 app extension target，在宿主中通常以模态会话运行；HarmonyOS 为系统预定义的 ShareExtensionAbility 组件，由相应系统服务统一拉起与销毁，应用不能直接启动。；待核：HarmonyOS ShareExtensionAbility 的生命周期回调与 UI 形态需读 API 正文确认。；iOS 扩展会话模型细则在未冻结的 App Extension Programming Guide 中。；Android 侧缺来源，未纳入本假设比较。。
- api_surface：分享目标匹配/建议机制差异假设：iOS 通过应用与扩展捐赠 INSendMessageIntent 使会话进入分享面板建议并用 intent 预填扩展界面；HarmonyOS 分享服务通过 UTD 标准化数据类型匹配目标应用（图片入图库、文档入文件管理）。两者实现'系统选择或建议分享目标'的接口体系不同。；待核：HarmonyOS 三方应用如何成为系统分享面板目标未读到正文。；iOS 建议机制依赖 SiriKit intents 的适用范围（仅消息类）及其他内容类型对应机制未展开。。
- device_forms：设备形态范围差异假设：本轮读到的 HarmonyOS Share Kit 碰一碰正文聚焦手机与 PC/2in1 跨设备分享（同一华为账号、API 26.0.0+ 等条件），iOS 正文描述的是单设备分享面板建议；两平台在'跨设备分享入口'的覆盖形态可能不同。；待核：iOS 对应的跨设备分享入口（如 AirDrop）未在本轮资料中读到正文。；HarmonyOS 单设备应用间分享面板与 ShareExtensionAbility 的关系未读到。。

范围缺口：Android：冻结来源未覆盖应用分享目标或接收分享机制（ACTION_SEND、DirectShare 等），全平台比较暂缺 Android 侧证据。；iOS：App Extension Programming Guide 与 NSExtensionActivationRule 细则正文未冻结；ios-2 为 macOS 专业视频文档，iOS 适用性未核实。；HarmonyOS：ShareExtensionAbility API 正文与版本引入未读；Share Kit 与 ShareExtensionAbility 关系未澄清。；三平台均未固定启动日基线版本，本轮全部结论为 low 初判，不代表最新正式版支持状态。

后续优先级：P1；Android 侧零相关证据属关键缺口；iOS/HarmonyOS 的 ShareExtensionAbility 与 share extension 映射涉及跨平台等价的高风险判断，需优先补源并核实版本与实际拉起行为。

逐条引用及原文摘录见同目录 normalized.json。
