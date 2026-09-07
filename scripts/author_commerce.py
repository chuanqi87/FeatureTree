#!/usr/bin/env python3
"""Author the commerce domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "commerce_capability_family"


def leaf(f, fid, parent, axis, zh, en, definition, includes, excludes, bindings,
         legacy=None, level="L3", related=None, privacy="none", aliases=None):
    f.append(feature(
        fid, parent=parent, level=level, zh=zh, en=en, definition=definition,
        includes=includes, excludes=excludes, sibling_axis=axis,
        granularity="atomic", bindings=bindings,
        legacy=legacy or {"disposition": "new", "sources": []},
        related=related, privacy_class=privacy, aliases=aliases,
    ))


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "commerce", parent=None, level="L1",
        zh="商业与增长", en="Commerce and Growth",
        definition="应用内购订阅、广告变现、分析事件、支付收银/钱包与增长运营 API。",
        includes=["iap、ads、analytics、payment、growth"],
        excludes=["开发者商户入驻与分成结算控制台", "纯网页支付无公开移动 SDK"],
        legacy={"disposition": "kept", "sources": ["commerce"]},
        layer="ecosystem",
    ))

    l2 = [
        ("commerce.iap", "应用内购买", "In-App Purchase",
         "数字商品查询购买、订阅、权益确认、退款与沙盒。",
         ["products、purchase、subscription、entitlement、refund、sandbox、server"],
         ["实物/线下收银见 payment", "广告变现见 ads"],
         ["commerce.iap"]),
        ("commerce.ads", "广告", "Advertising",
         "广告展示 SDK、广告标识、归因与个性化控制。",
         ["display、identifier、attribution、personalization、privacy_signals"],
         ["分析事件见 analytics", "增长归因设备见 growth"],
         ["commerce.ads"]),
        ("commerce.analytics", "分析", "Analytics",
         "应用内分析事件、用户属性与转化上报。",
         ["events、user_properties、conversion"],
         ["广告归因见 ads.attribution", "崩溃观测见 observability"],
         ["commerce.analytics"]),
        ("commerce.payment", "支付与钱包", "Payment and Wallet",
         "系统支付授权、第三方收银台、卡券钱包与订单追踪。",
         ["request_payment、third_party、wallet、order_tracking"],
         ["数字内购见 iap", "NFC 卡模拟见 connectivity.nfc"],
         []),
        ("commerce.growth", "增长运营", "Growth Operations",
         "应用内评价、远程配置、安装来源、动态图标与运营触达。",
         ["inapp_review、remote_config、install_referrer、dynamic_icon、engage、product_view"],
         ["分析事件见 analytics", "广告展示见 ads.display"],
         []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        f.append(feature(
            fid, parent="commerce", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy={"disposition": "kept" if sources else "new", "sources": sources},
            layer="ecosystem",
        ))

    # --- iap ---
    leaf(f, "commerce.iap.products", "commerce.iap", "iap_stage",
         "内购商品", "IAP Products",
         "查询可消耗/非消耗/订阅等数字商品目录。",
         ["queryProduct、Product.products"],
         ["发起购买见 iap.purchase"],
         merge_bindings(
             A("BillingClient.queryProductDetailsAsync", "https://developer.android.com/google/play/billing", "guide"),
             I("Product", "https://developer.apple.com/documentation/storekit/product", "class"),
             H("iap.queryProducts", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-iap"),
         ),
         legacy={"disposition": "kept", "sources": ["commerce.iap.products"]},
         aliases=["Play Billing", "StoreKit", "IAP Kit"])
    leaf(f, "commerce.iap.purchase", "commerce.iap", "iap_stage",
         "发起购买", "Launch Purchase",
         "拉起系统内购流程完成数字商品购买。",
         ["launchBillingFlow、Product.purchase、createPurchase"],
         ["商品查询见 products", "订阅专型见 subscription"],
         merge_bindings(
             A("BillingClient.launchBillingFlow", "https://developer.android.com/google/play/billing", "guide"),
             I("Product.purchase", "https://developer.apple.com/documentation/storekit/product", "class"),
             H("iap.createPurchase", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-iap"),
         ))
    leaf(f, "commerce.iap.subscription", "commerce.iap", "iap_stage",
         "自动续期订阅", "Auto-Renewable Subscriptions",
         "自动续期订阅购买、状态与管理入口。",
         ["SUBS products、SubscriptionInfo"],
         ["非订阅内购见 purchase", "服务端延期见 server_notify"],
         merge_bindings(
             A("Play Billing subscriptions", "https://developer.android.com/google/play/billing/subscriptions", "guide"),
             I("Product.SubscriptionInfo", "https://developer.apple.com/documentation/storekit/product/subscriptioninfo", "class"),
             H("iap subscription", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-iap"),
         ))
    leaf(f, "commerce.iap.entitlement", "commerce.iap", "iap_stage",
         "权益确认与查询", "Entitlement Confirm and Query",
         "确认发货/完成交易并查询当前权益。",
         ["acknowledgePurchase、Transaction.finish、confirmDelivery、queryPurchases"],
         ["退款见 refund"],
         merge_bindings(
             A("BillingClient.acknowledgePurchase", "https://developer.android.com/google/play/billing", "guide"),
             I("Transaction", "https://developer.apple.com/documentation/storekit/transaction", "structure"),
             H("iap.confirmDelivery", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-delivering-products", "guide"),
         ))
    leaf(f, "commerce.iap.refund", "commerce.iap", "iap_stage",
         "退款请求", "Refund Request",
         "应用内发起退款请求流程。",
         ["beginRefundRequest、createRefundRequest"],
         ["权益查询见 entitlement"],
         merge_bindings(
             pending("android", "Play 退款多为控制台/API，应用侧入口待核"),
             I("beginRefundRequest", "https://developer.apple.com/documentation/storekit/requesting-a-refund", "guide"),
             H("iap.createRefundRequest", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-refund", "guide"),
         ))
    leaf(f, "commerce.iap.sandbox", "commerce.iap", "iap_stage",
         "内购沙盒", "IAP Sandbox",
         "沙盒/许可测试账号下的内购联调。",
         ["StoreKit Test、license testers、IAP sandbox"],
         ["正式购买见 purchase"],
         merge_bindings(
             A("Play Billing testing", "https://developer.android.com/google/play/billing/testing", "guide"),
             I("StoreKit Test", "https://developer.apple.com/documentation/storekittest"),
             H("IAP sandbox", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-sandbox-testing", "guide"),
         ))
    leaf(f, "commerce.iap.server_notify", "commerce.iap", "iap_stage",
         "服务端交易通知", "Server Transaction Notifications",
         "商店服务端实时开发者通知与服务端 API。",
         ["RTDN、ASSN、IAP Server API"],
         ["客户端购买见 purchase"],
         merge_bindings(
             A("Real-time developer notifications", "https://developer.android.com/google/play/billing/rtdn", "guide"),
             I("App Store Server Notifications", "https://developer.apple.com/documentation/app-store-server-notifications"),
             H("IAP Server API", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-server-api", "guide"),
         ))

    # --- ads ---
    leaf(f, "commerce.ads.display", "commerce.ads", "ads_role",
         "广告展示", "Ad Display",
         "加载并展示横幅/插屏/激励等应用内广告。",
         ["Mobile Ads SDK、AdsKit AdComponent"],
         ["广告标识见 identifier", "归因见 attribution"],
         merge_bindings(
             A("Mobile Ads SDK", "https://developer.android.com/reference/com/google/android/gms/ads/package-summary", "package"),
             pending("ios", "Google Mobile Ads / AdMob iOS 同能力，待核官方入口"),
             H("@kit.AdsKit advertising", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising"),
         ),
         legacy={"disposition": "renamed_from", "sources": ["commerce.ads.sdk"]})
    leaf(f, "commerce.ads.identifier", "commerce.ads", "ads_role",
         "广告标识符", "Advertising Identifier",
         "读取可重置的广告标识（AAID/OAID/IDFA 等）。",
         ["AdvertisingIdClient、ASIdentifierManager、oaid"],
         ["应用集标识见 app_set_id"],
         merge_bindings(
             A("AdvertisingIdClient", "https://developer.android.com/training/articles/ad-id", "guide"),
             I("ASIdentifierManager", "https://developer.apple.com/documentation/adsupport/asidentifiermanager", "class"),
             H("identifier.oaid", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-oaid"),
         ),
         privacy="sensitive")
    leaf(f, "commerce.ads.app_set_id", "commerce.ads", "ads_role",
         "应用集标识", "App Set Identifier",
         "开发者应用集合级标识，用于分析与反欺诈。",
         ["App Set ID"],
         ["设备广告标识见 identifier"],
         merge_bindings(
             A("App Set ID", "https://developer.android.com/training/articles/app-set-id", "guide"),
             pending("ios"),
             pending("harmonyos"),
         ),
         privacy="sensitive")
    leaf(f, "commerce.ads.attribution", "commerce.ads", "ads_role",
         "广告归因", "Ad Attribution",
         "安装/转化归因测量（SKAN/Attribution Reporting/AdAttribution 等同一能力簇）。",
         ["SKAdNetwork、Attribution Reporting、AdAttributionKit、Ads attribution"],
         ["分析事件见 analytics.events"],
         merge_bindings(
             A("Attribution Reporting", "https://developer.android.com/design-for-safety/privacy-sandbox/attribution", "guide"),
             I("AdAttributionKit", "https://developer.apple.com/documentation/adattributionkit"),
             H("ads-attribution", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-attribution", "guide"),
         ),
         related=["commerce.analytics.events"])
    leaf(f, "commerce.ads.personalization", "commerce.ads", "ads_role",
         "广告个性化控制", "Ad Personalization Controls",
         "请求非个性化广告或用户个性化同意控制。",
         ["nonPersonalizedAd、UMP/ATT 边界"],
         ["展示见 display"],
         merge_bindings(
             A("UMP / request configuration", "https://developers.google.com/admob/android/privacy", "guide"),
             I("AppTrackingTransparency", "https://developer.apple.com/documentation/apptrackingtransparency"),
             H("AdOptions.nonPersonalizedAd", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising"),
         ),
         privacy="sensitive")
    leaf(f, "commerce.ads.privacy_signals", "commerce.ads", "ads_role",
         "广告隐私信号与运行时", "Ad Privacy Signals and Runtime",
         "隐私沙箱类广告信号与隔离 SDK 运行时入口。",
         ["Privacy Sandbox AdServices、SDK Runtime"],
         ["归因见 attribution", "展示见 display"],
         merge_bindings(
             A("Privacy Sandbox", "https://developer.android.com/design-for-safety/privacy-sandbox", "guide"),
             I("AdServices", "https://developer.apple.com/documentation/adservices"),
             pending("harmonyos"),
         ))

    # --- analytics ---
    leaf(f, "commerce.analytics.events", "commerce.analytics", "analytics_role",
         "分析事件", "Analytics Events",
         "记录自定义/推荐分析事件。",
         ["logEvent、FirebaseAnalytics、AGC analytics"],
         ["广告归因见 ads.attribution"],
         merge_bindings(
             A("FirebaseAnalytics", "https://firebase.google.com/docs/analytics/android/start", "guide"),
             I("Analytics", "https://developer.apple.com/documentation/analytics"),
             H("AppGallery analytics", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/analytics-kit-introduction", "guide"),
         ),
         legacy={"disposition": "kept", "sources": ["commerce.analytics.events"]},
         related=["commerce.ads.attribution"])
    leaf(f, "commerce.analytics.user_properties", "commerce.analytics", "analytics_role",
         "用户属性", "User Properties",
         "设置分析用用户属性/用户 ID（合规边界内）。",
         ["setUserProperty"],
         ["事件见 events"],
         merge_bindings(
             A("FirebaseAnalytics.setUserProperty", "https://firebase.google.com/docs/analytics/android/start", "guide"),
             pending("ios"),
             H("Analytics Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/analytics-kit-introduction", "guide"),
         ),
         privacy="sensitive")
    leaf(f, "commerce.analytics.conversion", "commerce.analytics", "analytics_role",
         "转化上报", "Conversion Reporting",
         "关键转化点上报供分析/增长漏斗使用。",
         ["conversion events"],
         ["广告归因测量见 ads.attribution"],
         merge_bindings(
             A("Firebase recommended events", "https://firebase.google.com/docs/analytics/android/start", "guide"),
             pending("ios"),
             H("Analytics Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/analytics-kit-introduction", "guide"),
         ),
         related=["commerce.ads.attribution", "commerce.growth.install_referrer"])

    # --- payment ---
    leaf(f, "commerce.payment.request_payment", "commerce.payment", "payment_role",
         "系统支付授权", "System Payment Authorization",
         "拉起系统级支付表单完成付款授权（Apple Pay / Google Pay / Payment Kit 等）。",
         ["PKPaymentAuthorization、PaymentsClient、requestPayment"],
         ["数字内购见 iap", "第三方聚合收银台见 third_party"],
         merge_bindings(
             A("Google Pay API", "https://developer.android.com/google/pay/android", "guide"),
             I("PKPaymentAuthorizationViewController", "https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller", "class"),
             H("paymentService.requestPayment", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-service"),
         ))
    leaf(f, "commerce.payment.third_party", "commerce.payment", "payment_role",
         "第三方收银台", "Third-Party Checkout",
         "调用第三方/合单/代扣等收银台能力。",
         ["ThirdPay、combined prepay、sign deduct"],
         ["系统支付授权见 request_payment"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("thirdPaymentService", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/third-paymentservice"),
         ))
    leaf(f, "commerce.payment.wallet", "commerce.payment", "payment_role",
         "卡券钱包", "Passes Wallet",
         "向系统钱包添加/管理会员卡、票证等卡券。",
         ["PKAddPasses、WalletPassClient、Save to Wallet"],
         ["数字证件核身见 identity.session.digital_id", "支付授权见 request_payment"],
         merge_bindings(
             A("Google Wallet API", "https://developer.android.com/google/wallet/overview", "guide"),
             I("PKAddPassesViewController", "https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller", "class"),
             H("WalletPassClient", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/walletpass"),
         ),
         related=["identity.session.digital_id"])
    leaf(f, "commerce.payment.order_tracking", "commerce.payment", "payment_role",
         "订单追踪", "Order Tracking",
         "将订单状态同步到系统钱包/订单界面。",
         ["Orders in Wallet"],
         ["卡券添加见 wallet"],
         merge_bindings(
             pending("android"),
             I("Orders", "https://developer.apple.com/documentation/passkit/orders"),
             pending("harmonyos"),
         ))
    leaf(f, "commerce.payment.quick_access_wallet", "commerce.payment", "payment_role",
         "快捷访问钱包卡", "Quick Access Wallet Cards",
         "向系统快捷访问钱包表面提供卡片。",
         ["WalletCardViewService"],
         ["Pass 添加见 wallet"],
         merge_bindings(
             A("Quick Access Wallet", "https://developer.android.com/reference/android/service/quickaccesswallet/package-summary", "package"),
             pending("ios"),
             pending("harmonyos"),
         ))

    # --- growth ---
    leaf(f, "commerce.growth.inapp_review", "commerce.growth", "growth_role",
         "应用内评价", "In-App Review",
         "请求系统应用内评分/评论对话框。",
         ["In-App Review、SKStoreReviewController、commentManager"],
         ["商店详情页跳转见 product_view"],
         merge_bindings(
             A("Play In-App Review", "https://developer.android.com/guide/playcore/in-app-review", "guide"),
             I("SKStoreReviewController", "https://developer.apple.com/documentation/storekit/skstorereviewcontroller", "class"),
             H("commentManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-appgallery-commentmanager"),
         ))
    leaf(f, "commerce.growth.remote_config", "commerce.growth", "growth_role",
         "远程配置", "Remote Config",
         "拉取云端远程配置参数驱动客户端行为。",
         ["Firebase Remote Config"],
         ["分析事件见 analytics"],
         merge_bindings(
             A("FirebaseRemoteConfig", "https://firebase.google.com/docs/remote-config/android/get-started", "guide"),
             pending("ios", "Firebase Remote Config iOS 同能力"),
             pending("harmonyos"),
         ))
    leaf(f, "commerce.growth.install_referrer", "commerce.growth", "growth_role",
         "安装来源", "Install Referrer",
         "读取应用安装来源/引荐信息。",
         ["Install Referrer API、attributionManager"],
         ["广告归因见 ads.attribution"],
         merge_bindings(
             A("Install Referrer", "https://developer.android.com/google/play/installreferrer/library", "guide"),
             pending("ios"),
             H("attributionManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-appgallery-attributionmanager"),
         ),
         related=["commerce.ads.attribution", "commerce.analytics.conversion"])
    leaf(f, "commerce.growth.dynamic_icon", "commerce.growth", "growth_role",
         "动态图标", "Dynamic App Icon",
         "切换应用备用图标/动态图标。",
         ["setAlternateIconName、selectDynamicIcon"],
         ["桌面快捷方式见 pin_shortcut"],
         merge_bindings(
             pending("android"),
             I("setAlternateIconName", "https://developer.apple.com/documentation/uikit/uiapplication/1627681-setalternateiconname", "method"),
             H("iconManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-appgallery-iconmanager"),
         ))
    leaf(f, "commerce.growth.pin_shortcut", "commerce.growth", "growth_role",
         "固定快捷方式", "Pin Shortcut",
         "请求将快捷方式固定到桌面/启动器。",
         ["requestPinShortcut"],
         ["动态图标见 dynamic_icon"],
         merge_bindings(
             A("ShortcutManager.requestPinShortcut", "https://developer.android.com/reference/android/content/pm/ShortcutManager"),
             pending("ios"),
             H("requestNewPinShortcut", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-appgallery-productviewmanager"),
         ))
    leaf(f, "commerce.growth.engage", "commerce.growth", "growth_role",
         "系统内容推荐承接", "System Engage Surfaces",
         "向系统推荐/内容聚合表面发布应用内容实体。",
         ["Engage SDK"],
         ["应用内消息见 inapp_messaging"],
         merge_bindings(
             A("Engage SDK", "https://developer.android.com/guide/playcore/engage", "guide"),
             pending("ios"),
             pending("harmonyos"),
         ))
    leaf(f, "commerce.growth.inapp_messaging", "commerce.growth", "growth_role",
         "应用内消息", "In-App Messaging",
         "展示运营配置的应用内消息活动。",
         ["Firebase In-App Messaging"],
         ["推送通知见 notifications"],
         merge_bindings(
             A("FirebaseInAppMessaging", "https://firebase.google.com/docs/in-app-messaging/android/get-started", "guide"),
             pending("ios"),
             pending("harmonyos"),
         ))
    leaf(f, "commerce.growth.product_view", "commerce.growth", "growth_role",
         "商店商品页", "Store Product View",
         "应用内加载应用商店商品/详情页。",
         ["loadProduct、SKStoreProductViewController"],
         ["应用内评价见 inapp_review"],
         merge_bindings(
             pending("android", "Play 应用内更新/详情 待核"),
             I("SKStoreProductViewController", "https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller", "class"),
             H("productViewManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-appgallery-productviewmanager"),
         ))

    dedup = {}
    for node in f:
        dedup[node["id"]] = node
    return list(dedup.values())


def main():
    nodes = build()
    path = write_domain("commerce", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
