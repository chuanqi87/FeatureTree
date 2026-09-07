#!/usr/bin/env python3
"""Author the web domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "web_capability_family"


def B(a=None, i=None, h=None):
    parts = []
    if a:
        parts.append(A(a[0], a[1], a[2] if len(a) > 2 else "class"))
    else:
        parts.append(pending("android"))
    if i:
        parts.append(I(i[0], i[1], i[2] if len(i) > 2 else "framework"))
    else:
        parts.append(pending("ios"))
    if h:
        parts.append(H(h[0], h[1], h[2] if len(h) > 2 else "module"))
    else:
        parts.append(pending("harmonyos"))
    return merge_bindings(*parts)


def leaf(f, fid, parent, axis, zh, en, definition, includes, excludes, bindings, legacy=None, level="L3", privacy="none"):
    f.append(feature(
        fid, parent=parent, level=level, zh=zh, en=en, definition=definition,
        includes=includes, excludes=excludes, sibling_axis=axis,
        granularity="atomic", bindings=bindings,
        legacy=legacy or {"disposition": "new", "sources": []},
        privacy_class=privacy,
    ))


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "web", parent=None, level="L1",
        zh="Web与混合", en="Web and Hybrid",
        definition="嵌入式 Web 视图、原生-JS 桥接与混合应用支撑；不含系统浏览器应用本身的产品功能。",
        includes=['WebView、桥接、混合加载'],
        excludes=['network HTTP 客户端', 'interop 通用 deeplink'],
        legacy={'disposition': 'kept', 'sources': ['web']},
    ))
    l2 = [
        ('web.webview', '嵌入式Web视图', 'Embedded Web View', '应用内嵌浏览器组件的加载、导航与站点数据管理。', ['加载、导航、缓存、Cookie'], ['JS 桥接见 bridge'], ['web.webview']),
        ('web.bridge', '原生与脚本桥接', 'Native Script Bridge', '原生与页面脚本双向通信、脚本执行与消息通道。', ['JS bridge、eval、消息'], ['页面导航见 webview'], ['web.bridge']),
        ('web.hybrid', '混合应用支撑', 'Hybrid App Support', '本地资源包、能力桥与系统浏览器会话等混合形态支撑。', ['本地内容、能力桥、自定义标签页'], ['纯 WebView 见 webview'], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="web", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- web.webview ---
    leaf(f, "web.webview.embed", "web.webview", "webview_operation", "Web视图嵌入", "Web View Embed",
         "在应用界面中嵌入 Web 视图组件并加载 URL。", ['WebView / WKWebView'], ['导航控制见 navigation'],
         B(('WebView', 'https://developer.android.com/reference/android/webkit/WebView'), ('WKWebView', 'https://developer.apple.com/documentation/webkit/wkwebview', 'class'), ('Web', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'kept', 'sources': ['web.webview.embed']}, level="L3", privacy="none")
    leaf(f, "web.webview.navigation", "web.webview", "webview_operation", "页面导航控制", "Navigation Control",
         "控制前进后退、重定向拦截与加载生命周期。", ['shouldOverrideUrlLoading / decidePolicy'], ['嵌入见 embed'],
         B(('WebViewClient', 'https://developer.android.com/reference/android/webkit/WebViewClient'), ('WKNavigationDelegate', 'https://developer.apple.com/documentation/webkit/wknavigationdelegate', 'protocol'), ('Web onLoadIntercept', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.webview.cache", "web.webview", "webview_operation", "缓存与站点数据", "Cache and Site Data",
         "管理 Web 缓存、存储与站点数据清理。", ['cache / website data'], ['Cookie 见 cookies'],
         B(('WebStorage', 'https://developer.android.com/reference/android/webkit/WebStorage'), ('WKWebsiteDataStore', 'https://developer.apple.com/documentation/webkit/wkwebsitedatastore', 'class'), ('Web cacheMode', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.webview.cookies", "web.webview", "webview_operation", "Cookie管理", "Cookie Management",
         "读写与同步 Web Cookie。", ['CookieManager'], ['站点数据见 cache'],
         B(('CookieManager', 'https://developer.android.com/reference/android/webkit/CookieManager'), ('HTTPCookieStorage', 'https://developer.apple.com/documentation/foundation/httpcookiestorage', 'class'), ('Web cookie', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.webview.intercept", "web.webview", "webview_operation", "请求拦截与自定义资源", "Request Intercept",
         "拦截请求并提供自定义资源响应。", ['shouldInterceptRequest / scheme handler'], ['导航策略见 navigation'],
         B(('WebViewClient.shouldInterceptRequest', 'https://developer.android.com/reference/android/webkit/WebViewClient'), ('WKURLSchemeHandler', 'https://developer.apple.com/documentation/webkit/wkurlschemehandler', 'protocol'), ('Web onInterceptRequest', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.webview.basic_auth", "web.webview", "webview_operation", "网页认证质询", "Web Auth Challenge",
         "处理 HTTP 基本认证或证书质询。", ['onReceivedHttpAuthRequest'], ['系统浏览器认证会话见 hybrid.auth_session'],
         B(('HttpAuthHandler', 'https://developer.android.com/reference/android/webkit/HttpAuthHandler'), ('URLAuthenticationChallenge', 'https://developer.apple.com/documentation/foundation/urlauthenticationchallenge', 'class'), ('Web onHttpAuthRequest', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.webview.prefetch", "web.webview", "webview_operation", "页面预取预加载", "Page Prefetch",
         "预取或预渲染即将打开的页面。", ['prefetch / prerender'], ['加载见 embed'],
         B(('Profile.prefetchUrl', 'https://developer.android.com/reference/androidx/webkit/Profile', 'class'), None, ('Web prepare', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.webview.console", "web.webview", "webview_operation", "控制台与脚本错误", "Console and Script Errors",
         "接收页面控制台日志与脚本错误。", ['console / onJsError'], ['JS 执行见 bridge'],
         B(('WebChromeClient.onConsoleMessage', 'https://developer.android.com/reference/android/webkit/WebChromeClient'), ('WKUIDelegate', 'https://developer.apple.com/documentation/webkit/wkuidelegate', 'protocol'), ('Web onConsole', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.webview.media_capture", "web.webview", "webview_operation", "页面媒体采集权限", "Page Media Capture Permission",
         "处理页面对相机麦克风的权限请求。", ['getUserMedia permission'], ['系统相机见 media'],
         B(('PermissionRequest', 'https://developer.android.com/reference/android/webkit/PermissionRequest'), ('WKUIDelegate media capture', 'https://developer.apple.com/documentation/webkit', 'framework'), ('Web permission', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "web.webview.safe_browsing", "web.webview", "webview_operation", "安全浏览检查", "Safe Browsing Check",
         "对加载 URL 做安全浏览威胁检查。", ['Safe Browsing'], ['导航见 navigation'],
         B(('SafeBrowsing', 'https://developer.android.com/reference/android/webkit/WebView', 'class'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- web.bridge ---
    leaf(f, "web.bridge.native_js", "web.bridge", "bridge_operation", "原生与JS双向桥", "Native JS Bidirectional Bridge",
         "在原生与页面 JS 间注册对象并双向调用。", ['addJavascriptInterface / messageHandlers'], ['单次 eval 见 eval_js'],
         B(('WebViewCompat.addWebMessageListener', 'https://developer.android.com/reference/androidx/webkit/WebViewCompat'), ('WKUserContentController', 'https://developer.apple.com/documentation/webkit/wkusercontentcontroller', 'class'), ('Web javaScriptProxy', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'kept', 'sources': ['web.bridge.native_js']}, level="L3", privacy="none")
    leaf(f, "web.bridge.eval_js", "web.bridge", "bridge_operation", "执行页面脚本", "Evaluate Page Script",
         "在页面上下文中执行脚本并取回结果。", ['evaluateJavascript'], ['双向桥见 native_js'],
         B(('WebView.evaluateJavascript', 'https://developer.android.com/reference/android/webkit/WebView'), ('WKWebView.evaluateJavaScript', 'https://developer.apple.com/documentation/webkit/wkwebview', 'class'), ('Web runJavaScript', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.bridge.message_channel", "web.bridge", "bridge_operation", "Web消息通道", "Web Message Channel",
         "使用消息端口在原生与页面间传消息。", ['WebMessagePort'], ['双向桥见 native_js'],
         B(('WebMessagePort', 'https://developer.android.com/reference/android/webkit/WebMessagePort'), ('WKScriptMessage', 'https://developer.apple.com/documentation/webkit/wkscriptmessage', 'class'), ('Web message', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.bridge.user_script", "web.bridge", "bridge_operation", "用户脚本注入", "User Script Injection",
         "在文档加载前后注入用户脚本。", ['WKUserScript / inject'], ['执行见 eval_js'],
         B(('WebViewCompat', 'https://developer.android.com/reference/androidx/webkit/WebViewCompat'), ('WKUserScript', 'https://developer.apple.com/documentation/webkit/wkuserscript', 'class'), ('Web javaScriptOnDocumentStart', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.bridge.capability_bridge", "web.bridge", "bridge_operation", "Web能力桥接", "Web Capability Bridge",
         "向页面暴露受限系统能力调用入口。", ['capability bridge'], ['通用 JS 桥见 native_js'],
         B(None, None, ('Web inject', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-component-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- web.hybrid ---
    leaf(f, "web.hybrid.local_content", "web.hybrid", "hybrid_operation", "本地资源包加载", "Local Content Bundle",
         "从应用包内或本地目录加载混合内容。", ['file:/// android_asset'], ['网络加载见 webview.embed'],
         B(('WebViewAssetLoader', 'https://developer.android.com/reference/androidx/webkit/WebViewAssetLoader'), ('WKWebView loadFileURL', 'https://developer.apple.com/documentation/webkit/wkwebview', 'class'), ('Web loadData', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.hybrid.custom_tabs", "web.hybrid", "hybrid_operation", "系统浏览器会话标签", "System Browser Session Tabs",
         "拉起系统浏览器自定义标签页会话。", ['Custom Tabs / SFSafariViewController'], ['内嵌 WebView 见 webview'],
         B(('Custom Tabs', 'https://developer.chrome.com/docs/android/custom-tabs', 'guide'), ('SFSafariViewController', 'https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.hybrid.auth_session", "web.hybrid", "hybrid_operation", "网页认证会话", "Web Authentication Session",
         "使用系统认证会话完成 OAuth/网页登录。", ['ASWebAuthenticationSession'], ['WebView 内认证质询见 webview.basic_auth'],
         B(('Custom Tabs Auth', 'https://developer.chrome.com/docs/android/custom-tabs', 'guide'), ('ASWebAuthenticationSession', 'https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "web.hybrid.offline_pack", "web.hybrid", "hybrid_operation", "离线混合包更新", "Offline Hybrid Pack Update",
         "更新混合应用离线资源包版本。", ['offline pack update'], ['本地加载见 local_content'],
         B(None, None, ('Web offline', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-component-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "web.hybrid.download", "web.hybrid", "hybrid_operation", "Web下载处理", "Web Download Handling",
         "处理页面触发的文件下载。", ['DownloadListener'], ['系统下载管理见 network/storage'],
         B(('DownloadListener', 'https://developer.android.com/reference/android/webkit/DownloadListener'), ('WKDownload', 'https://developer.apple.com/documentation/webkit/wkdownload', 'class'), ('Web onDownload', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")


    leaf(f, "web.webview.zoom", "web.webview", "webview_operation", "页面缩放", "Page Zoom",
         "控制 Web 页面缩放与字号缩放。", ["zoom / textZoom"], ["导航见 navigation"],
         B(("WebSettings.setTextZoom", "https://developer.android.com/reference/android/webkit/WebSettings"),
           ("WKWebView pageZoom", "https://developer.apple.com/documentation/webkit/wkwebview", "class"),
           ("Web zoomAccess", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web")))
    leaf(f, "web.webview.geolocation", "web.webview", "webview_operation", "页面地理位置权限", "Page Geolocation Permission",
         "处理页面对地理位置的权限请求。", ["geolocation permission"], ["系统定位见 location"],
         B(("WebChromeClient.onGeolocationPermissionsShowPrompt", "https://developer.android.com/reference/android/webkit/WebChromeClient"),
           ("WKUIDelegate", "https://developer.apple.com/documentation/webkit/wkuidelegate", "protocol"), None), privacy="runtime_permission")
    leaf(f, "web.webview.file_chooser", "web.webview", "webview_operation", "页面文件选择", "Page File Chooser",
         "处理网页 input 文件选择请求。", ["file chooser"], ["系统选择器见 storage"],
         B(("WebChromeClient.onShowFileChooser", "https://developer.android.com/reference/android/webkit/WebChromeClient"),
           ("WKUIDelegate", "https://developer.apple.com/documentation/webkit/wkuidelegate", "protocol"),
           ("Web onShowFileSelector", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web")))
    leaf(f, "web.bridge.origin_whitelist", "web.bridge", "bridge_operation", "桥接源白名单", "Bridge Origin Whitelist",
         "限制可调用原生桥的页面源。", ["origin allowlist"], ["双向桥见 native_js"],
         B(("WebViewCompat.addWebMessageListener", "https://developer.android.com/reference/androidx/webkit/WebViewCompat"),
           ("WKUserContentController", "https://developer.apple.com/documentation/webkit/wkusercontentcontroller", "class"), None))
    leaf(f, "web.hybrid.ssl_error", "web.hybrid", "hybrid_operation", "证书错误处理", "SSL Error Handling",
         "处理混合内容或证书错误策略。", ["ssl error"], ["导航见 webview.navigation"],
         B(("WebViewClient.onReceivedSslError", "https://developer.android.com/reference/android/webkit/WebViewClient"),
           ("WKNavigationDelegate", "https://developer.apple.com/documentation/webkit/wknavigationdelegate", "protocol"),
           ("Web onSslErrorEventReceive", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web")))

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("web", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
