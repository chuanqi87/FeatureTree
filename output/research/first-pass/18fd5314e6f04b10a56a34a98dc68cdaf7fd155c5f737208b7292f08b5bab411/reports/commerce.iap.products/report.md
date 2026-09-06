# 内购商品 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到内购商品查询/购买机制：Android 经 Play Billing（Unity 插件、Play Points 指南）见购买流程、延迟购买与店外购买交付；iOS StoreKit views 列四类商品、StoreView 展示并监听交易；HarmonyOS IAP Kit 有 queryEnvironmentStatus 地区前置检查与 queryProducts 单类型≤200条约束。Android 客户端查询主流程、iOS 购买 API 版本、HarmonyOS 购买流程正文未读到，全部 low 初判。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | indirect | Play Billing 提供购买工作流：Unity 插件经 GooglePlayStoreModule 接入，支持延迟购买（pending）、订阅改价确认与 proration 升降级；一次性商品须及时交付并检测店外购买，服务端可用 Onetimeproducts:list。客户端商品查询接口未读到。 | recommended |
| ios | documented_mechanism | direct | StoreKit views 支持消耗型/非消耗型/自动续期/非续期订阅四类商品，StoreView(ids:) 直接展示；经 Transaction.unfinished/currentEntitlements/updates 异步序列监听交易；可离线本地配置原型，购买经系统支付面板完成。 | recommended |
| harmonyos | documented_mechanism | direct | IAP Kit 需先 queryEnvironmentStatus 判定华为账号服务地（当前仅中国境内，不含港澳台，可结算），再 queryProducts 按 productType（消耗/非消耗/自动续期订阅）查询 AppGallery Connect 配置的商品，单次仅一种类型且不超 200 条；差异页另见 createPurchase/finishPurchase/queryPurchases 及 CashierComponent 新增。 | recommended |

## android 条件与证据

适用范围：未固定：快照未标注 Billing Library 版本；android-1 为 Unity 插件指南、android-2 为 Play Points 一次性商品指南（均 fetched 2026-09-05，version_verified=false）
条件：需 Google Play 商店分发并接入 Google Play Billing；android-1 证据为 Unity 插件路径，非 Kotlin 主流程；Play Points 一次性商品需先创建商品与促销配置；订阅升降级须改用 proration mode API，旧 UpdateSubscription 会抛 GooglePlayStoreUnsupportedException；延迟购买须注册监听且不得在回调中立即发货
缺口：客户端商品查询接口（queryProductDetails/querySkuDetails 等）正文未在冻结来源中读到；Billing Library 当前版本、最低 Play 商店版本与 API Level 条件未固定；订阅商品的完整类型集合与查询约束未读到（仅一次性商品指南）；Play Points 促销是一次性商品特例路径，不能代表全部可消耗商品行为
真机分类理由：购买流程依赖 Play 商店账号、支付面板与店外购买/延迟购买场景，静态文档无法验证实际交付与确认时序；后续精研建议用沙盒账号真机验证。

- [Use the Google Play Billing Library with Unity](https://developer.android.com/google/play/billing/unity)，Implement Google Play Billing Library features in your game（购买工作流与延迟购买），正文 125–146 行；获取 2026-09-05T10:42:34.186144+00:00；SHA 6c6a0e7d72402761f69784872c120303d20837011532922028980fa8f208fd07。
- [Use the Google Play Billing Library with Unity](https://developer.android.com/google/play/billing/unity)，UpdateSubscription has small API changes（proration mode 替代），正文 284–299 行；获取 2026-09-05T10:42:34.186144+00:00；SHA 6c6a0e7d72402761f69784872c120303d20837011532922028980fa8f208fd07。
- [Detect and deliver one-time items](https://developer.android.com/guide/playpoints/deliver-items-one-time)，Delivery timing: use Google Play Billing Library to deliver one-time items，正文 30–33 行；获取 2026-09-05T10:29:57.507688+00:00；SHA cde515724938c5478539c6e60b0dfb742b937e8a44d089a01b18d62f1edeb70f。
- [Detect and deliver one-time items](https://developer.android.com/guide/playpoints/deliver-items-one-time)，Detect items received outside of the game，正文 66–70 行；获取 2026-09-05T10:29:57.507688+00:00；SHA cde515724938c5478539c6e60b0dfb742b937e8a44d089a01b18d62f1edeb70f。
- [Detect and deliver one-time items](https://developer.android.com/guide/playpoints/deliver-items-one-time)，Server-side best practices: Purchases.products:get / Onetimeproducts:list，正文 88–100 行；获取 2026-09-05T10:29:57.507688+00:00；SHA cde515724938c5478539c6e60b0dfb742b937e8a44d089a01b18d62f1edeb70f。

## ios 条件与证据

适用范围：未固定：快照未标注 StoreKit 2 / 最低 iOS 版本（availability 需逐符号核对）；文档使用 StoreView、Transaction.updates 等 StoreKit 2 风格 API（fetched 2026-09-05，version_verified=false）
条件：商品需在 App Store Connect 配置，或先用 Xcode StoreKit 本地配置离线原型；StoreKit views 默认样式可直接展示全部四类商品，无需自定义编程；交易处理经 Transaction.unfinished/currentEntitlements/updates 异步序列；正式购买经系统支付面板接受或取消；示例交易不产生真实扣费
缺口：Product.purchase 等购买 API 符号级正文与 iOS 最低可用版本未核对（Apple 目录含多平台，需逐符号确认 iOS 适用性）；产品 ID 查询（Product.products(for:)）与数量限制未在快照中读到；非续期订阅仅列名，行为细节未展开；正式环境（App Store Connect 商品）与本地测试差异未核
真机分类理由：支付面板行为、交易监听时序与本地配置到 App Store Connect 正式商品的差异需 Xcode 沙盒/真机验证；静态文档未覆盖实际扣费与交付时序。

- [Getting started with In-App Purchase using StoreKit views](https://developer.apple.com/documentation/storekit/getting-started-with-in-app-purchases-using-storekit-views)，Choose your product types（consumables/non-consumables/auto-renewable/non-renewing），正文 9–16 行；获取 2026-09-05T10:26:00.796705+00:00；SHA 93b32a8cf125897c422874b0308080cb45b1f0045ad0b0fc4a4651dc969ee855。
- [Getting started with In-App Purchase using StoreKit views](https://developer.apple.com/documentation/storekit/getting-started-with-in-app-purchases-using-storekit-views)，Monitor transactions in your app（Transaction.unfinished/currentEntitlements/updates），正文 54–61 行；获取 2026-09-05T10:26:00.796705+00:00；SHA 93b32a8cf125897c422874b0308080cb45b1f0045ad0b0fc4a4651dc969ee855。
- [Getting started with In-App Purchase using StoreKit views](https://developer.apple.com/documentation/storekit/getting-started-with-in-app-purchases-using-storekit-views)，Create SwiftUI views that display your products（StoreView(ids:)），正文 183–212 行；获取 2026-09-05T10:26:00.796705+00:00；SHA 93b32a8cf125897c422874b0308080cb45b1f0045ad0b0fc4a4651dc969ee855。
- [Understanding StoreKit workflows](https://developer.apple.com/documentation/storekit/understanding-storekit-workflows)，Configure and run the project（商品类型清单与支付面板购买），正文 13–34 行；获取 2026-09-05T10:26:04.064447+00:00；SHA 68d517dffb7a07effe20a1b299a16070fc269435c8dd72d9010622f4417b2988。

## harmonyos 条件与证据

适用范围：未固定：harmonyos-1 指南未标注 SDK/API 版本；harmonyos-2 为 IAP Kit API 差异页（URL 含 iapkit-6101，具体 HarmonyOS 发行版归属未核；fetched 2026-09-04/05，version_verified=false）
条件：需当前登录华为账号服务地支持数字商品服务，当前仅中国境内（香港、澳门特别行政区及中国台湾除外）可结算；商品须先在 AppGallery Connect 配置；queryProducts 单次仅能查询一种 productType，且不超过 200 条；订阅型商品 productType 须指定为 iap.ProductType.AUTORENEWABLE
缺口：购买主流程（createPurchase 拉起收银台）正文未读取，仅差异表条目；错误码语义未核：差异页新增 801、PURCHASE_NOT_FOUND=1001860064 等含义需读 API 参考；差异页对应的 HarmonyOS/OpenHarmony 发行版与 SDK 版本未在快照标注；queryEnvironmentStatus 失败后的降级/提示行为未读到
真机分类理由：结算可用性绑定中国境内华为账号服务地，且购买/收银台链路依赖真实账号环境，静态文档无法验证；需中国区账号真机核实 queryEnvironmentStatus/queryProducts/购买链路。

- [展示数字商品](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-distribute-query)，前提条件与 queryEnvironmentStatus（支持地区仅中国境内），正文 5–15 行；获取 2026-09-04T09:35:09+00:00；SHA df3e409cbc933f079299c91d5e1f543124aa354ebc06a39b817433f13691fb94。
- [展示数字商品](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-distribute-query)，查询商品信息：queryProducts/productType/单次200条限制，正文 47–53 行；获取 2026-09-04T09:35:09+00:00；SHA df3e409cbc933f079299c91d5e1f543124aa354ebc06a39b817433f13691fb94。
- [展示数字商品](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-distribute-query)，queryProducts 代码示例（CONSUMABLE/NONCONSUMABLE/AUTORENEWABLE），正文 69–77 行；获取 2026-09-04T09:35:09+00:00；SHA df3e409cbc933f079299c91d5e1f543124aa354ebc06a39b817433f13691fb94。
- [IAP Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-iapkit-6101)，iap.queryProducts/createPurchase/finishPurchase/queryPurchases 新增错误码 801，正文 3–16 行；获取 2026-09-05T10:56:01.793739+00:00；SHA 5c851d940e7fbdc2d41f5df3aa7eee84db8e841166bd34c27a8ffcda8eb6f3a4。
- [IAP Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-iapkit-6101)，新增 CashierComponent 与 showManagedInvoices，正文 17–31 行；获取 2026-09-05T10:56:01.793739+00:00；SHA 5c851d940e7fbdc2d41f5df3aa7eee84db8e841166bd34c27a8ffcda8eb6f3a4。

## 待验证差异假设

- programming_model：商品类型集合可能不同：iOS StoreKit 明确四类（含非续期订阅），HarmonyOS IAP Kit 文档仅列消耗型/非消耗型/自动续期订阅三类，Android 一次性商品指南区分消耗型（consumable）与耐久型（durable）商品。；待核：Android 订阅与一次性商品的完整官方类型集合需读 Billing 类型文档核对；非续期订阅在 Android/HarmonyOS 是否存在等价类型未确认；类型枚举仅为文档快照，未核实最新正式版。
- limits_precision：商品查询约束可能不同：HarmonyOS queryProducts 单次仅能查询一种 productType 且不超 200 条；iOS 示例经 StoreView(ids:) 一次传入产品 ID 数组，未见条数或类型限制说明；Android 客户端查询约束未读到。；待核：iOS StoreKit 产品查询的数量/类型限制未在快照中说明，需读 Product.products(for:) 参考；Android queryProductDetails 的批量与类型约束需补读正文；限制可能随版本变化，基线未固定。
- availability：购买前置条件可能不同：HarmonyOS 要求先 queryEnvironmentStatus 判定华为账号服务地且当前仅中国境内可结算；已读 Android（Unity 插件购买流程）与 iOS（StoreKit views 交易监听）文档均未描述类似环境前置检查步骤。；待核：Android Play 结算国家/地区限制与 iOS 商店区域限制未在冻结来源中读到，不能断言无此类限制；queryEnvironmentStatus 失败后的官方降级建议未读到；差异仅为所读文档描述层面，未经真机核实。

范围缺口：Android 核心 Billing Library（Kotlin/Java）商品查询与购买主流程正文未纳入冻结来源，现证据经 Unity 插件与 Play Points 指南路径；iOS Product.purchase 等购买 API 符号级 availability 与最低 iOS 版本未核对（Apple 目录需逐符号确认 iOS 适用性）；HarmonyOS 购买主流程（createPurchase/收银台 CashierComponent）正文未读取，仅 API 差异表条目；三平台订阅升级/降级/价格变更行为仅有 Android 侧（proration mode、改价确认）证据，未做跨平台比较

后续优先级：P1；三平台查询/购买主流程文档均有实质缺口（Android 无核心集成正文、iOS 版本未核、HarmonyOS 购买流程未读），且商品类型集合与区域可用性属高风险映射，应优先安排正式研究与真机沙盒验证。

逐条引用及原文摘录见同目录 normalized.json。
