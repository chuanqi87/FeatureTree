#!/usr/bin/env python3
"""Author the interop domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "interop_channel"


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
        "interop", parent=None, level="L1",
        zh="跨应用协作", en="Cross-App Interop",
        definition="系统分享、深度链接、跨应用动作分发、数据传递与轻量即时体验入口。",
        includes=["share、deeplink、action_dispatch、data_transfer、lightweight_ui"],
        excludes=["分布式跨端 Continuity 见 distributed", "账号联邦登录见 identity"],
        legacy={"disposition": "kept", "sources": ["interop"]},
    ))

    l2 = [
        ("interop.share", "系统分享", "System Share",
         "系统分享面板、接收扩展、近距碰一碰分享与统一数据类型。",
         ["sheet、receive、nearby、utd、link_preview"],
         ["意图启动见 action_dispatch", "文件 URI 授权见 data_transfer"],
         ["interop.share"]),
        ("interop.deeplink", "深度链接", "Deep Linking",
         "自定义 scheme 与域名验证的 https 应用链接（三端同一能力）。",
         ["custom_scheme、verified_links"],
         ["通用 URL 启动见 action_dispatch.url_launch"],
         ["interop.deeplink"]),
        ("interop.action_dispatch", "跨应用动作分发", "Cross-App Action Dispatch",
         "显式/隐式启动组件、系统意图注册、过滤器解析与助手调用。",
         ["component_intent、system_intents、url_launch、filters、assistant"],
         ["深度链接路由见 deeplink", "分享面板见 share.sheet"],
         ["interop.action_dispatch"]),
        ("interop.data_transfer", "跨应用数据传递", "Cross-App Data Transfer",
         "拖放、内容提供者、文件提供者、URI 授权与内容嵌入。",
         ["drag_drop、content_provider、file_provider、uri_grant、content_embed"],
         ["系统分享面板见 share", "存储侧共享见 storage.sharing"],
         []),
        ("interop.lightweight_ui", "轻量即时体验", "Lightweight Instant Experience",
         "免安装/轻量入口体验（App Clip 与原子化服务等归为同一能力）。",
         ["instant_experience、embedded_slice"],
         ["完整应用安装生命周期见 app", "小组件见 app.desktop"],
         []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="interop", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- share ---
    leaf(f, "interop.share.sheet", "interop.share", "share_role",
         "系统分享面板", "System Share Sheet",
         "拉起系统分享面板向外发送文本/文件/多媒体。",
         ["ACTION_SEND、UIActivityViewController、systemShare"],
         ["作为接收方见 share.receive", "拖放见 data_transfer.drag_drop"],
         merge_bindings(
             A("ACTION_SEND", "https://developer.android.com/training/sharing/send", "guide"),
             I("UIActivityViewController", "https://developer.apple.com/documentation/uikit/uiactivityviewcontroller", "class"),
             H("@ohos.share", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-share"),
         ),
         legacy={"disposition": "kept", "sources": ["interop.share.sheet"]})
    leaf(f, "interop.share.receive", "interop.share", "share_role",
         "分享接收扩展", "Share Receive Extension",
         "注册为系统分享目标/扩展以接收外来内容。",
         ["share extension、share target、Share Kit 接入方"],
         ["主动拉起分享面板见 share.sheet"],
         merge_bindings(
             A("intent-filter SEND", "https://developer.android.com/training/sharing/receive", "guide"),
             I("Share extension", "https://developer.apple.com/documentation/xcode/configuring-a-share-extension", "guide"),
             H("Share Kit access", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-access-mode", "guide"),
         ),
         related=["interop.action_dispatch.system_intents"])
    leaf(f, "interop.share.nearby", "interop.share", "share_role",
         "近距碰触分享", "Nearby Knock Share",
         "设备近距碰一碰触发的内容分享。",
         ["knock share"], ["通用蓝牙传输见 connectivity", "系统分享面板见 share.sheet"],
         merge_bindings(
             pending("android", "Nearby Share 应用侧 API 待核"),
             pending("ios", "NameDrop/AirDrop 应用 API 受限，待核"),
             H("Knock Share", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-between-phones-content", "guide"),
         ))
    leaf(f, "interop.share.utd", "interop.share", "share_role",
         "统一分享数据类型", "Uniform Share Data Types",
         "分享载荷的统一类型描述（UTD 等）。",
         ["UTD image/file types"], ["MIME/UTI 通用标识见 storage.type_id"],
         merge_bindings(
             pending("android"),
             I("UTType", "https://developer.apple.com/documentation/uniformtypeidentifiers", "class"),
             H("Share UTD", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-utd-image", "guide"),
         ),
         related=["storage.type_id"])
    leaf(f, "interop.share.link_preview", "interop.share", "share_role",
         "链接预览元数据", "Link Preview Metadata",
         "为 URL 提供丰富链接预览元数据。",
         ["LPLinkMetadata"], ["深度链接路由见 deeplink"],
         merge_bindings(
             pending("android"),
             I("LPLinkMetadata", "https://developer.apple.com/documentation/linkpresentation", "class"),
             pending("harmonyos"),
         ))
    leaf(f, "interop.share.shared_with_you", "interop.share", "share_role",
         "与你共享汇聚", "Shared With You Aggregation",
         "汇聚消息等渠道分享给当前用户的内容入口。",
         ["SharedWithYou"], ["主动分享面板见 share.sheet"],
         merge_bindings(
             pending("android"),
             I("SharedWithYou", "https://developer.apple.com/documentation/sharedwithyou"),
             pending("harmonyos"),
         ))

    # --- deeplink ---
    leaf(f, "interop.deeplink.custom_scheme", "interop.deeplink", "deeplink_kind",
         "自定义Scheme链接", "Custom Scheme Links",
         "通过自定义 URL scheme 打开应用内页面。",
         ["myapp:// paths、intent-filter scheme"],
         ["域名验证 https 链接见 verified_links"],
         merge_bindings(
             A("intent-filter scheme", "https://developer.android.com/guide/components/intents-filters", "guide"),
             I("URL Schemes", "https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app", "guide"),
             H("Want URI", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup-overview", "guide"),
         ),
         legacy={"disposition": "split_from", "sources": ["interop.deeplink.url"]})
    leaf(f, "interop.deeplink.verified_links", "interop.deeplink", "deeplink_kind",
         "验证域名应用链接", "Verified Domain App Links",
         "经域名所有权验证的 https 应用链接（App Links / Universal Links / App Linking 同一能力）。",
         ["autoVerify App Links、Associated Domains、App Linking"],
         ["自定义 scheme 见 custom_scheme", "未验证 URL 启动见 action_dispatch.url_launch"],
         merge_bindings(
             A("App Links", "https://developer.android.com/training/app-links", "guide"),
             I("Associated Domains", "https://developer.apple.com/documentation/xcode/supporting-associated-domains", "guide"),
             H("App Linking", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startupapp", "guide"),
         ),
         legacy={"disposition": "merged_from", "sources": [
             "interop.deeplink.url",
             "interop.deep_linking.app_links",
             "interop.deep_linking.universal_links",
             "interop.deep_linking.app_linking",
         ]},
         aliases=["App Links", "Universal Links", "App Linking"],
         related=["interop.action_dispatch.url_launch"])

    # --- action_dispatch ---
    leaf(f, "interop.action_dispatch.component_intent", "interop.action_dispatch", "dispatch_role",
         "目标组件调用", "Target Component Invocation",
         "显式启动另一应用/本应用组件并传递参数。",
         ["startActivity、startAbility、openURL to component"],
         ["系统隐式意图注册见 system_intents"],
         merge_bindings(
             A("Intent", "https://developer.android.com/reference/android/content/Intent"),
             I("UIApplication.open", "https://developer.apple.com/documentation/uikit/uiapplication", "class"),
             H("startAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-want"),
         ),
         legacy={"disposition": "kept", "sources": ["interop.action_dispatch.component_intent"]})
    leaf(f, "interop.action_dispatch.system_intents", "interop.action_dispatch", "dispatch_role",
         "系统意图注册", "System Intent Registration",
         "声明可处理的系统动作/类别供其他应用解析调用。",
         ["intent-filter actions、App Intents"],
         ["分享接收见 share.receive"],
         merge_bindings(
             A("intent-filter", "https://developer.android.com/guide/components/intents-filters", "guide"),
             I("App Intents", "https://developer.apple.com/documentation/appintents"),
             H("skills / want actions", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-stage-brief", "guide"),
         ),
         legacy={"disposition": "kept", "sources": ["interop.action_dispatch.system_intents"]})
    leaf(f, "interop.action_dispatch.url_launch", "interop.action_dispatch", "dispatch_role",
         "URL应用启动", "URL App Launch",
         "通过 URL 交由系统解析并启动目标应用（不一定经域名验证）。",
         ["openURL、ACTION_VIEW"],
         ["验证域名链接见 deeplink.verified_links"],
         merge_bindings(
             A("ACTION_VIEW", "https://developer.android.com/guide/components/intents-common", "guide"),
             I("openURL", "https://developer.apple.com/documentation/uikit/uiapplication/1648685-open", "method"),
             H("startAbility by URI", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-want"),
         ),
         legacy={"disposition": "kept", "sources": ["interop.action_dispatch.url_launch"]},
         related=["interop.deeplink.verified_links", "interop.deeplink.custom_scheme"])
    leaf(f, "interop.action_dispatch.filters", "interop.action_dispatch", "dispatch_role",
         "意图过滤与解析", "Intent Filter Resolution",
         "查询可处理某意图的应用集合并做可见性约束。",
         ["queryIntentActivities、<queries>"],
         ["实际启动见 component_intent"],
         merge_bindings(
             A("PackageManager.queryIntentActivities", "https://developer.android.com/reference/android/content/pm/PackageManager"),
             pending("ios", "LSServices 可见性受限，待核"),
             pending("harmonyos"),
         ),
         related=None)
    leaf(f, "interop.action_dispatch.assistant", "interop.action_dispatch", "dispatch_role",
         "助手与语音调用", "Assistant and Voice Invoke",
         "向系统助手/语音暴露可调用动作。",
         ["App Actions、App Intents shortcuts"],
         ["普通系统意图见 system_intents"],
         merge_bindings(
             A("App Actions", "https://developer.android.com/guide/app-actions/overview", "guide"),
             I("App Intents", "https://developer.apple.com/documentation/appintents"),
             pending("harmonyos"),
         ))
    leaf(f, "interop.action_dispatch.media_intents", "interop.action_dispatch", "dispatch_role",
         "媒体域系统意图", "Media Domain System Intents",
         "媒体相关系统意图（播放/搜索等）跨应用分发。",
         ["Media Intents"], ["播控会话见 media.session"],
         merge_bindings(
             pending("android", "Media STYLE intents 待核"),
             I("Media Intents", "https://developer.apple.com/documentation/mediaintents"),
             pending("harmonyos"),
         ),
         related=["media.session"])

    # --- data_transfer ---
    leaf(f, "interop.data_transfer.drag_drop", "interop.data_transfer", "transfer_role",
         "拖放", "Drag and Drop",
         "跨视图/跨应用拖放数据载荷。",
         ["startDragAndDrop、UIDragInteraction"], ["分享面板见 share.sheet"],
         merge_bindings(
             A("View.startDragAndDrop", "https://developer.android.com/guide/topics/ui/drag-drop", "guide"),
             I("UIDragInteraction", "https://developer.apple.com/documentation/uikit/uidraginteraction", "class"),
             H("drag-drop", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-drag-drop", "guide"),
         ))
    leaf(f, "interop.data_transfer.content_provider", "interop.data_transfer", "transfer_role",
         "内容提供者", "Content Provider",
         "以 URI 向其他应用暴露结构化数据集。",
         ["ContentProvider"], ["文件专用提供者见 file_provider"],
         merge_bindings(
             A("ContentProvider", "https://developer.android.com/reference/android/content/ContentProvider"),
             pending("ios"),
             pending("harmonyos", "DataShare / 类 ContentProvider 待核"),
         ),
         related=["storage.sharing"])
    leaf(f, "interop.data_transfer.file_provider", "interop.data_transfer", "transfer_role",
         "安全文件提供者", "Secure File Provider",
         "通过 content URI 安全共享应用私有文件。",
         ["FileProvider"], ["URI 临时授权见 uri_grant"],
         merge_bindings(
             A("FileProvider", "https://developer.android.com/reference/androidx/core/content/FileProvider"),
             pending("ios"),
             pending("harmonyos"),
         ))
    leaf(f, "interop.data_transfer.uri_grant", "interop.data_transfer", "transfer_role",
         "URI临时授权", "URI Permission Grant",
         "向目标应用授予 URI 读写临时权限。",
         ["FLAG_GRANT_READ_URI_PERMISSION"], ["提供者实现见 content_provider/file_provider"],
         merge_bindings(
             A("FLAG_GRANT_READ_URI_PERMISSION", "https://developer.android.com/training/secure-file-sharing", "guide"),
             pending("ios"),
             pending("harmonyos"),
         ))
    leaf(f, "interop.data_transfer.content_embed", "interop.data_transfer", "transfer_role",
         "跨应用内容嵌入", "Cross-App Content Embed",
         "将其他应用内容嵌入本应用窗口区域。",
         ["Content Embedding"], ["轻量即时体验见 lightweight_ui"],
         merge_bindings(
             pending("android", "Activity embedding / SDK 待核"),
             pending("ios"),
             H("Content Embedding", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed"),
         ),
         related=["interop.lightweight_ui.instant_experience"])

    # --- lightweight_ui ---
    leaf(f, "interop.lightweight_ui.instant_experience", "interop.lightweight_ui", "lightweight_kind",
         "免安装即时入口", "Install-Free Instant Entry",
         "免完整安装即可触达的轻量应用体验（App Clip、原子化服务等同一能力）。",
         ["App Clip、Atomic Service / instant experience entry"],
         ["嵌入切片卡片见 embedded_slice", "完整应用见 app"],
         merge_bindings(
             pending("android", "Google Play Instant 边界待核"),
             I("App Clip", "https://developer.apple.com/documentation/appclip"),
             H("Atomic Service", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/atomic-service-overview", "guide"),
         ),
         aliases=["App Clip", "Atomic Service"])
    leaf(f, "interop.lightweight_ui.embedded_slice", "interop.lightweight_ui", "lightweight_kind",
         "嵌入式内容切片", "Embedded Content Slice",
         "向其他应用/系统表面提供可嵌入的轻量 UI 切片。",
         ["SliceProvider"], ["完整即时体验入口见 instant_experience"],
         merge_bindings(
             A("SliceProvider", "https://developer.android.com/guide/slices", "guide"),
             pending("ios", "Widget/Live Activity 边界见 app.desktop"),
             pending("harmonyos"),
         ),
         related=["interop.lightweight_ui.instant_experience"])

    # optional education under collaboration-ish share/dispatch — ClassKit as dispatch-adjacent
    leaf(f, "interop.action_dispatch.education", "interop.action_dispatch", "dispatch_role",
         "教育任务分发", "Education Task Dispatch",
         "向教育/课堂系统分发作业与进度类跨应用协作入口。",
         ["ClassKit"], ["通用助手调用见 assistant"],
         merge_bindings(
             pending("android"),
             I("ClassKit", "https://developer.apple.com/documentation/classkit"),
             pending("harmonyos"),
         ))

    dedup = {}
    for node in f:
        dedup[node["id"]] = node
    return list(dedup.values())


def main():
    nodes = build()
    path = write_domain("interop", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
