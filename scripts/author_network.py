#!/usr/bin/env python3
"""Author the network domain taxonomy.

Note: local hotspot canonical is connectivity.wifi.hotspot_local
(legacy merged_from network.hotspot*). Do not recreate hotspot leaves here.
"""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "network_stack_layer"


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "network", parent=None, level="L1",
        zh="网络", en="Networking",
        definition="IP 层及以上的应用联网：HTTP、套接字、WebSocket、VPN、RPC、切换与发现；不含近距无线连接。",
        includes=["HTTP、Socket、WebSocket、VPN、RPC、切换、发现、连接状态"],
        excludes=[
            "近距无线见 connectivity",
            "本地热点见 connectivity.wifi.hotspot_local（network.hotspot* 已合并）",
            "蜂窝通话见 telecom",
        ],
        legacy={"disposition": "kept", "sources": ["network"]},
        notes="network.hotspot / network.hotspot.local legacy 去向：connectivity.wifi.hotspot_local (merged_from)。",
    ))

    l2 = [
        ("network.http", "HTTP客户端", "HTTP Client",
         "HTTP(S) 请求构建、传输、缓存与安全参数。",
         ["请求、缓存、Cookie、代理、TLS"], ["WebSocket 见 network.websocket"], ["network.http"]),
        ("network.socket", "套接字", "Sockets",
         "TCP/UDP/本地/组播等传输层套接字。",
         ["TCP、UDP、本地套接字、组播"], ["HTTP 见 network.http"], ["network.socket"]),
        ("network.websocket", "WebSocket", "WebSocket",
         "全双工 WebSocket 长连接。",
         ["连接、收发、关闭"], ["原始 TCP 见 network.socket"], []),
        ("network.vpn", "VPN", "VPN",
         "应用提供的系统级 VPN 隧道。",
         ["Packet tunnel、VpnService"], ["普通 HTTP 代理见 network.http.proxy"], ["network.vpn"]),
        ("network.rpc", "远程过程调用", "Remote Procedure Call",
         "面向服务的高性能 RPC 通道（非 REST/HTTP 业务封装）。",
         ["RPC 会话、调用"], ["HTTP 见 network.http"], []),
        ("network.handover", "网络切换增强", "Network Handover",
         "跨接入技术切换与传输加速决策。",
         ["handover 事件、加速"], ["路径监视见 network.connection"], []),
        ("network.discovery", "本地服务发现", "Local Service Discovery",
         "局域网服务发现与解析（含 mDNS/DNS-SD）。",
         ["mDNS、服务浏览/发布"], ["主机名 DNS 查询见 network.connection.dns_lookup"], []),
        ("network.connection", "网络连接与路径", "Network Connection and Path",
         "默认网络、按能力请求网络、计费感知与 DNS 查询。",
         ["默认网络、NetworkRequest、metered、DNS"], ["Wi-Fi 扫描连接见 connectivity.wifi"], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="network", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- http (L3 groups to keep sibling fan-out bounded) ---
    http_groups = [
        ("network.http.request", "请求构建与收发", "Request Build and Exchange",
         "HTTP 请求构建、正文、头字段与进度回调。",
         ["基础请求、头、正文、进度"], ["缓存/代理见 http.session"]),
        ("network.http.session", "会话与传输策略", "Session and Transport Policy",
         "缓存、Cookie、代理、TLS、认证与连接复用。",
         ["缓存、Cookie、代理、TLS、会话"], ["单次报文见 http.request"]),
        ("network.http.diagnostics", "协议与诊断", "Protocol and Diagnostics",
         "HTTP/3、拦截器与请求级诊断指标。",
         ["HTTP/3、拦截器、指标"], ["基础收发见 http.request"]),
    ]
    for fid, zh, en, definition, includes, excludes in http_groups:
        f.append(feature(
            fid, parent="network.http", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="http_capability",
            bindings=merge_bindings(
                A("HttpURLConnection", "https://developer.android.com/reference/java/net/HttpURLConnection"),
                I("URLSession", "https://developer.apple.com/documentation/foundation/urlsession", "class"),
                H("@ohos.net.http", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http"),
            ),
        ))

    for fid, parent, axis, zh, en, definition, includes, excludes, bindings, legacy in [
        ("network.http.client", "network.http.request", "http_request_part",
         "基础HTTP请求", "Basic HTTP Request",
         "发起 GET/POST 等 HTTP(S) 请求并接收响应。",
         ["request、dataTask、createHttp"], ["WebSocket 见 network.websocket"],
         merge_bindings(
             A("HttpURLConnection", "https://developer.android.com/reference/java/net/HttpURLConnection"),
             I("URLSession", "https://developer.apple.com/documentation/foundation/urlsession", "class"),
             H("@ohos.net.http", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http"),
         ), {"disposition": "kept", "sources": ["network.http.client"]}),
        ("network.http.headers", "network.http.request", "http_request_part",
         "HTTP头处理", "HTTP Header Handling",
         "读写请求与响应头字段。",
         ["setRequestProperty、allHTTPHeaderFields"], ["Cookie 专用 API 见 http.cookies"],
         merge_bindings(
             A("URLConnection.setRequestProperty",
               "https://developer.android.com/reference/java/net/URLConnection#setRequestProperty(java.lang.String,%20java.lang.String)"),
             I("URLRequest.allHTTPHeaderFields",
               "https://developer.apple.com/documentation/foundation/urlrequest/2011607-allhttpheaderfields", "property"),
             H("Rcp_Header", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.body", "network.http.request", "http_request_part",
         "请求体与表单上传", "Request Body and Multipart",
         "构建请求体、表单字段与 multipart 文件上传。",
         ["RequestBody、multipart、httpBody"], ["进度回调见 http.progress"],
         merge_bindings(
             A("MultipartBody", "https://square.github.io/okhttp/features/calls/", "guide"),
             I("URLRequest.httpBody", "https://developer.apple.com/documentation/foundation/urlrequest/1411317-httpbody", "property"),
             H("Rcp_MultipartForm", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.progress", "network.http.request", "http_request_part",
         "传输进度与流式回调", "Transfer Progress and Streaming",
         "订阅上传/下载进度与流式数据到达事件。",
         ["progress、didReceive data"], ["完整缓冲响应见 http.client"],
         merge_bindings(
             A("OkHttp progress", "https://square.github.io/okhttp/", "guide"),
             I("URLSessionDataDelegate", "https://developer.apple.com/documentation/foundation/urlsessiondatadelegate", "protocol"),
             H("onProgress", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.cache", "network.http.session", "http_session_part",
         "HTTP缓存", "HTTP Cache",
         "配置、使用与清理 HTTP 响应缓存。",
         ["HttpResponseCache、URLCache、usingCache"], ["单次请求见 http.client"],
         merge_bindings(
             A("HttpResponseCache", "https://developer.android.com/reference/android/net/http/HttpResponseCache"),
             I("URLCache", "https://developer.apple.com/documentation/foundation/urlcache", "class"),
             H("usingCache", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.cookies", "network.http.session", "http_session_part",
         "Cookie管理", "Cookie Management",
         "存储、读取与同步 HTTP Cookie。",
         ["CookieManager、HTTPCookieStorage"], ["请求头手工设置见 http.headers"],
         merge_bindings(
             A("CookieManager", "https://developer.android.com/reference/android/webkit/CookieManager"),
             I("HTTPCookieStorage", "https://developer.apple.com/documentation/foundation/httpcookiestorage", "class"),
             H("RCP cookies", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.proxy", "network.http.session", "http_session_part",
         "代理配置", "Proxy Configuration",
         "为会话或请求配置 HTTP/HTTPS 代理与例外。",
         ["ProxySelector、connectionProxyDictionary"], ["VPN 隧道见 network.vpn"],
         merge_bindings(
             A("ProxySelector", "https://developer.android.com/reference/java/net/ProxySelector"),
             I("connectionProxyDictionary",
               "https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411499-connectionproxydictionary", "property"),
             H("Rcp_Proxy", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.tls", "network.http.session", "http_session_part",
         "TLS与证书配置", "TLS and Certificate Config",
         "配置信任锚、客户端证书与服务器校验策略。",
         ["Network Security Config、ATS、SecurityConfig"], ["系统证书存储见 security.certificates"],
         merge_bindings(
             A("Network Security Config", "https://developer.android.com/privacy-and-security/security-config", "guide"),
             I("URLSessionDelegate challenge",
               "https://developer.apple.com/documentation/foundation/urlsessiondelegate/1409308-urlsession", "method"),
             H("Rcp_SecurityConfig", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.auth", "network.http.session", "http_session_part",
         "HTTP服务器认证", "HTTP Server Authentication",
         "向服务器提供用户名密码等认证凭据。",
         ["Authenticator、ServerAuthentication"], ["TLS 客户端证书见 http.tls"],
         merge_bindings(
             A("Authenticator", "https://developer.android.com/reference/java/net/Authenticator"),
             I("URLCredential", "https://developer.apple.com/documentation/foundation/urlcredential", "class"),
             H("Rcp_ServerAuthentication", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.priority_session", "network.http.session", "http_session_part",
         "高性能会话化客户端", "High-Performance Session Client",
         "会话化连接复用与高性能 HTTP 客户端能力。",
         ["RCP session、连接池"], ["单次请求见 http.client"],
         merge_bindings(
             A("OkHttpClient", "https://square.github.io/okhttp/", "guide"),
             I("URLSessionConfiguration", "https://developer.apple.com/documentation/foundation/urlsessionconfiguration", "class"),
             H("Rcp_Session", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.http3", "network.http.diagnostics", "http_diag_part",
         "HTTP/3与QUIC", "HTTP/3 and QUIC",
         "通过 QUIC 进行 HTTP/3 传输。",
         ["HTTP/3、QUIC session"], ["HTTP/1.1/2 见 http.client"],
         merge_bindings(
             A("Cronet", "https://developer.android.com/guide/topics/connectivity/cronet/start", "guide"),
             I("URLSession HTTP/3", "https://developer.apple.com/documentation/foundation/urlsession", "class"),
             H("rcp_quic", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.interceptor", "network.http.diagnostics", "http_diag_part",
         "请求拦截器", "Request Interceptor",
         "在请求发送前后插入拦截与改写逻辑。",
         ["Interceptor、RequestInterceptor"], ["基础请求见 http.client"],
         merge_bindings(
             A("Interceptor", "https://square.github.io/okhttp/features/interceptors/", "guide"),
             pending("ios", "URLProtocol 可模拟，待核"),
             H("Rcp_RequestInterceptor", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.metrics", "network.http.diagnostics", "http_diag_part",
         "请求级诊断指标", "Request Diagnostics Metrics",
         "收集单次请求的时序与调试指标。",
         ["URLSessionTaskTransactionMetrics、DebugInfo"], ["传输进度见 http.progress"],
         merge_bindings(
             A("Network Event Listener", "https://developer.android.com/guide/topics/connectivity/cronet/start", "guide"),
             I("URLSessionTaskTransactionMetrics",
               "https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics", "class"),
             H("Rcp_DebugInfo", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.redirect", "network.http.diagnostics", "http_diag_part",
         "重定向策略", "Redirect Policy",
         "控制跟随重定向次数与策略。",
         ["redirect policy"], ["基础请求见 http.client"],
         merge_bindings(
             A("HttpURLConnection.setInstanceFollowRedirects",
               "https://developer.android.com/reference/java/net/HttpURLConnection#setInstanceFollowRedirects(boolean)"),
             I("URLSessionTaskDelegate redirect",
               "https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate", "protocol"),
             H("maxRedirects", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http"),
         ), {"disposition": "new", "sources": []}),
        ("network.http.timeout", "network.http.session", "http_session_part",
         "超时与重试策略", "Timeout and Retry Policy",
         "配置连接/读写超时与重试策略。",
         ["connectTimeout、timeoutInterval、retry"], ["进度见 http.progress"],
         merge_bindings(
             A("OkHttp timeouts", "https://square.github.io/okhttp/recipes/#timeouts-kt-java", "guide"),
             I("timeoutIntervalForRequest",
               "https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1408153-timeoutintervalforrequest", "property"),
             H("connectTimeout", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent=parent, level="L4", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=axis, granularity="atomic",
            bindings=bindings, legacy=legacy,
        ))

    # --- socket ---
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("network.socket.tcp", "TCP套接字", "TCP Socket",
         "建立 TCP 连接并进行字节流收发。",
         ["Socket、NWConnection tcp、TCPSocket"], ["UDP 见 socket.udp"],
         merge_bindings(
             A("Socket", "https://developer.android.com/reference/java/net/Socket"),
             I("NWConnection", "https://developer.apple.com/documentation/network/nwconnection", "class"),
             H("TCPSocket", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket"),
         ), {"disposition": "split_from", "sources": ["network.socket.tcp_udp"]}),
        ("network.socket.udp", "UDP套接字", "UDP Socket",
         "发送与接收 UDP 数据报。",
         ["DatagramSocket、NWConnection udp、UDPSocket"], ["TCP 见 socket.tcp"],
         merge_bindings(
             A("DatagramSocket", "https://developer.android.com/reference/java/net/DatagramSocket"),
             I("NWConnection", "https://developer.apple.com/documentation/network/nwconnection", "class"),
             H("UDPSocket", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket"),
         ), {"disposition": "split_from", "sources": ["network.socket.tcp_udp"]}),
        ("network.socket.local", "本地域套接字", "Local Domain Socket",
         "本机进程间 UNIX 域套接字通信。",
         ["LocalSocket、本地 socket"], ["TCP 回环见 socket.tcp"],
         merge_bindings(
             A("LocalSocket", "https://developer.android.com/reference/android/net/LocalSocket"),
             I("NWEndpoint.unix", "https://developer.apple.com/documentation/network/nwendpoint", "struct"),
             H("local socket", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket"),
         ), {"disposition": "new", "sources": []}),
        ("network.socket.multicast", "组播", "Multicast",
         "加入组播组进行一对多数据报收发。",
         ["MulticastSocket、multicast entitlement"], ["单播 UDP 见 socket.udp"],
         merge_bindings(
             A("MulticastSocket", "https://developer.android.com/reference/java/net/MulticastSocket"),
             I("NWParameters allowLocalEndpointReuse",
               "https://developer.apple.com/documentation/network/nwparameters", "class"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
        ("network.socket.server", "套接字服务端监听", "Socket Server Listen",
         "在本地端口监听并接受入站连接。",
         ["ServerSocket、NWListener"], ["客户端连接见 socket.tcp"],
         merge_bindings(
             A("ServerSocket", "https://developer.android.com/reference/java/net/ServerSocket"),
             I("NWListener", "https://developer.apple.com/documentation/network/nwlistener", "class"),
             H("TCPSocket listen", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket"),
         ), {"disposition": "new", "sources": []}),
        ("network.socket.tls", "套接字层TLS", "Socket-Level TLS",
         "在套接字上启用 TLS 包装传输。",
         ["SSLSocket、NWProtocolTLS"], ["HTTPS 见 network.http.tls"],
         merge_bindings(
             A("SSLSocket", "https://developer.android.com/reference/javax/net/ssl/SSLSocket"),
             I("NWProtocolTLS", "https://developer.apple.com/documentation/network/nwprotocoltls", "class"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
        ("network.socket.keepalive", "套接字保活与选项", "Socket Keepalive Options",
         "配置 keepalive、超时与套接字选项。",
         ["SO_KEEPALIVE、NWProtocolTCP"], ["连接建立见 socket.tcp"],
         merge_bindings(
             A("Socket.setKeepAlive", "https://developer.android.com/reference/java/net/Socket#setKeepAlive(boolean)"),
             I("NWProtocolTCP.Options", "https://developer.apple.com/documentation/network/nwprotocoltcp/options", "class"),
             H("TCPSocket setExtraOptions", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket"),
         ), {"disposition": "new", "sources": []}),
        ("network.socket.dual_stack", "双栈与地址族", "Dual-Stack Address Families",
         "选择 IPv4/IPv6 地址族并处理双栈连接。",
         ["AF_INET/AF_INET6、happy eyeballs"], ["DNS 查询见 connection.dns_lookup"],
         merge_bindings(
             A("Inet6Address", "https://developer.android.com/reference/java/net/Inet6Address"),
             I("NWEndpoint.hostPort", "https://developer.apple.com/documentation/network/nwendpoint", "struct"),
             H("getAddressesByName", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent="network.socket", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="socket_kind",
            granularity="atomic", bindings=bindings, legacy=legacy,
        ))

    # --- websocket ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("network.websocket.client", "WebSocket客户端", "WebSocket Client",
         "建立 WebSocket 连接并收发文本/二进制消息。",
         ["URLSessionWebSocketTask、createWebSocket"], ["服务端见 websocket.server"],
         merge_bindings(
             A("OkHttp WebSocket", "https://square.github.io/okhttp/features/websockets/", "guide"),
             I("URLSessionWebSocketTask", "https://developer.apple.com/documentation/foundation/urlsessionwebsockettask", "class"),
             H("@ohos.net.webSocket", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-webSocket"),
         )),
        ("network.websocket.server", "WebSocket服务端", "WebSocket Server",
         "在本机或服务侧接受 WebSocket 连接（平台支持时）。",
         ["服务端接受升级"], ["客户端见 websocket.client"],
         merge_bindings(
             pending("android", "无统一 OS API，待核"),
             pending("ios", "无统一 OS API，待核"),
             pending("harmonyos", "公开服务端 API 待核"),
         )),
        ("network.websocket.lifecycle", "连接生命周期与心跳", "Connection Lifecycle and Heartbeat",
         "管理 WebSocket 连接状态、关闭码与保活。",
         ["ping/pong、close code、state"], ["消息收发见 websocket.client"],
         merge_bindings(
             A("WebSocketListener", "https://square.github.io/okhttp/features/websockets/", "guide"),
             I("URLSessionWebSocketTask.sendPing",
               "https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/2889656-sendping", "method"),
             H("webSocket.on", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-webSocket"),
         )),
    ]:
        f.append(feature(
            fid, parent="network.websocket", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="websocket_role",
            granularity="atomic", bindings=bindings,
        ))

    # --- vpn ---
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("network.vpn.app_vpn", "应用VPN扩展", "App VPN Extension",
         "以系统 VPN 扩展形式建立隧道并处理报文。",
         ["VpnService、NEPacketTunnelProvider"], ["代理见 network.http.proxy"],
         merge_bindings(
             A("VpnService", "https://developer.android.com/reference/android/net/VpnService"),
             I("NEPacketTunnelProvider",
               "https://developer.apple.com/documentation/networkextension/nepackettunnelprovider", "class"),
             pending("harmonyos", "VPN 扩展能力待核"),
         ), {"disposition": "kept", "sources": ["network.vpn.app_vpn"]}),
        ("network.vpn.config", "VPN配置与偏好", "VPN Configuration",
         "创建、保存与启用 VPN 配置档案。",
         ["NEVPNManager、VpnService.Builder"], ["报文处理见 app_vpn"],
         merge_bindings(
             A("VpnService.Builder", "https://developer.android.com/reference/android/net/VpnService.Builder"),
             I("NEVPNManager", "https://developer.apple.com/documentation/networkextension/nevpnmanager", "class"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
        ("network.vpn.per_app", "按应用分流VPN", "Per-App VPN Routing",
         "按应用或规则将流量导入 VPN。",
         ["per-app VPN、allowed applications"], ["全局隧道见 app_vpn"],
         merge_bindings(
             A("VpnService.Builder.addAllowedApplication",
               "https://developer.android.com/reference/android/net/VpnService.Builder#addAllowedApplication(java.lang.String)"),
             I("NEAppRule", "https://developer.apple.com/documentation/networkextension/neapprule", "class"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
        ("network.vpn.on_demand", "按需连接VPN", "On-Demand VPN",
         "按网络条件自动连接或断开 VPN。",
         ["OnDemandRules"], ["手动配置见 vpn.config"],
         merge_bindings(
             pending("android"),
             I("NEOnDemandRule", "https://developer.apple.com/documentation/networkextension/neondemandrule", "class"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent="network.vpn", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="vpn_capability",
            granularity="atomic", bindings=bindings, legacy=legacy,
        ))

    # --- rpc ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("network.rpc.session", "RPC会话", "RPC Session",
         "建立并管理高性能 RPC 会话。",
         ["urpc session"], ["HTTP 见 network.http"],
         merge_bindings(
             pending("android"), pending("ios"),
             H("urpc", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rpc-development-guide"),
         )),
        ("network.rpc.call", "RPC调用", "RPC Call",
         "发起远程过程调用并接收结果。",
         ["invoke/call"], ["会话建立见 rpc.session"],
         merge_bindings(
             pending("android"), pending("ios"),
             H("urpc call", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rpc-development-guide"),
         )),
        ("network.rpc.stream", "RPC流式传输", "RPC Streaming",
         "在 RPC 通道上进行流式数据传输。",
         ["streaming RPC"], ["一元调用见 rpc.call"],
         merge_bindings(
             pending("android"), pending("ios"),
             H("urpc stream", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rpc-development-guide"),
         )),
    ]:
        f.append(feature(
            fid, parent="network.rpc", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="rpc_role",
            granularity="atomic", bindings=bindings,
        ))

    # --- handover ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("network.handover.event", "切换事件订阅", "Handover Event Subscription",
         "订阅 Wi-Fi/蜂窝等接入间切换事件。",
         ["handover events"], ["路径变化见 network.connection.path"],
         merge_bindings(
             pending("android", "ConnectivityManager 回调可覆盖部分语义"),
             pending("ios"),
             H("Network Boost handover", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-networkBoost"),
         )),
        ("network.handover.boost", "传输加速申请", "Transfer Boost Request",
         "在切换场景申请传输加速或保活。",
         ["boost request"], ["事件订阅见 handover.event"],
         merge_bindings(
             pending("android"), pending("ios"),
             H("netHandover", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-networkBoost"),
         )),
        ("network.handover.policy", "多网协同策略", "Multi-Network Policy",
         "配置多网络协同/切换策略入口。",
         ["multi-net policy"], ["单网绑定见 connection.request"],
         merge_bindings(
             A("NetworkRequest", "https://developer.android.com/reference/android/net/NetworkRequest"),
             pending("ios"),
             H("Network Boost", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-boost-kit"),
         )),
    ]:
        f.append(feature(
            fid, parent="network.handover", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="handover_role",
            granularity="atomic", bindings=bindings,
        ))

    # --- discovery (mdns) ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("network.discovery.browse", "服务浏览", "Service Browse",
         "浏览局域网内发布的服务实例（DNS-SD/mDNS）。",
         ["NsdManager.discover、NetServiceBrowser"], ["发布见 discovery.publish"],
         merge_bindings(
             A("NsdManager", "https://developer.android.com/reference/android/net/nsd/NsdManager"),
             I("NetServiceBrowser", "https://developer.apple.com/documentation/foundation/netservicebrowser", "class"),
             H("mdns", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-mdns"),
         )),
        ("network.discovery.publish", "服务发布", "Service Publish",
         "在局域网发布可发现的服务实例。",
         ["registerService、NetService"], ["浏览见 discovery.browse"],
         merge_bindings(
             A("NsdManager.registerService",
               "https://developer.android.com/reference/android/net/nsd/NsdManager#registerService(android.net.nsd.NsdServiceInfo,%20int,%20android.net.nsd.NsdManager.RegistrationListener)"),
             I("NetService", "https://developer.apple.com/documentation/foundation/netservice", "class"),
             H("mdns.addLocalService", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-mdns"),
         )),
        ("network.discovery.resolve", "服务解析", "Service Resolve",
         "将服务实例解析为主机与端口。",
         ["resolveService"], ["浏览见 discovery.browse"],
         merge_bindings(
             A("NsdManager.resolveService",
               "https://developer.android.com/reference/android/net/nsd/NsdManager#resolveService(android.net.nsd.NsdServiceInfo,%20android.net.nsd.NsdManager.ResolveListener)"),
             I("NetService.resolve", "https://developer.apple.com/documentation/foundation/netservice/1412679-resolve", "method"),
             H("mdns resolve", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-mdns"),
         )),
        ("network.discovery.bonjour_txt", "服务TXT记录", "Service TXT Records",
         "读写 DNS-SD TXT 元数据记录。",
         ["TXT record"], ["解析主机见 discovery.resolve"],
         merge_bindings(
             A("NsdServiceInfo.setAttribute",
               "https://developer.android.com/reference/android/net/nsd/NsdServiceInfo#setAttribute(java.lang.String,%20java.lang.String)"),
             I("NetService.txtRecordData",
               "https://developer.apple.com/documentation/foundation/netservice/1409000-txtrecorddata", "property"),
             pending("harmonyos"),
         )),
    ]:
        f.append(feature(
            fid, parent="network.discovery", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="discovery_role",
            granularity="atomic", bindings=bindings, privacy_class="runtime_permission",
        ))

    # --- connection ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("network.connection.path", "默认网络与路径监视", "Default Network and Path Monitor",
         "获取当前默认网络并监听连通性/路径变化。",
         ["getActiveNetwork、NWPathMonitor、getDefaultNet"], ["按能力请求见 connection.request"],
         merge_bindings(
             A("ConnectivityManager", "https://developer.android.com/reference/android/net/ConnectivityManager"),
             I("NWPathMonitor", "https://developer.apple.com/documentation/network/nwpathmonitor", "class"),
             H("@ohos.net.connection", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection"),
         )),
        ("network.connection.request", "按能力请求网络", "Capability-Based Network Request",
         "按传输类型或能力请求并绑定特定网络。",
         ["NetworkRequest、requestNetwork"], ["默认监视见 connection.path"],
         merge_bindings(
             A("ConnectivityManager.requestNetwork",
               "https://developer.android.com/reference/android/net/ConnectivityManager#requestNetwork(android.net.NetworkRequest,%20android.net.ConnectivityManager.NetworkCallback)"),
             I("NWParameters requiredInterfaceType",
               "https://developer.apple.com/documentation/network/nwparameters", "class"),
             H("createNetConnection", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection"),
         )),
        ("network.connection.metered", "计费网络感知", "Metered Network Awareness",
         "感知当前网络是否计量/昂贵以控制流量。",
         ["NOT_METERED、isExpensive"], ["路径监视见 connection.path"],
         merge_bindings(
             A("NET_CAPABILITY_NOT_METERED",
               "https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_NOT_METERED"),
             I("NWPath.isExpensive", "https://developer.apple.com/documentation/network/nwpath/isexpensive", "property"),
             H("netCapabilities", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection"),
         )),
        ("network.connection.bind_process", "进程网络绑定", "Process Network Binding",
         "将进程或套接字绑定到指定网络。",
         ["bindProcessToNetwork、required interface"], ["请求网络见 connection.request"],
         merge_bindings(
             A("ConnectivityManager.bindProcessToNetwork",
               "https://developer.android.com/reference/android/net/ConnectivityManager#bindProcessToNetwork(android.net.Network)"),
             I("NWConnection", "https://developer.apple.com/documentation/network/nwconnection", "class"),
             H("setAppNet", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection"),
         )),
        ("network.connection.dns_lookup", "主机名DNS查询", "Hostname DNS Lookup",
         "将主机名解析为地址（含自定义解析入口）。",
         ["InetAddress、getAddresses"], ["DoH 见 connection.doh", "mDNS 服务发现见 network.discovery"],
         merge_bindings(
             A("InetAddress", "https://developer.android.com/reference/java/net/InetAddress"),
             I("getaddrinfo", "https://developer.apple.com/documentation/network", "framework"),
             H("getAddressesByName", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection"),
         )),
        ("network.connection.doh", "DNS over HTTPS", "DNS over HTTPS",
         "以加密 HTTPS 通道执行 DNS 解析。",
         ["dnsOverHttps"], ["明文查询见 dns_lookup"],
         merge_bindings(
             A("DnsResolver", "https://developer.android.com/reference/android/net/DnsResolver"),
             pending("ios", "系统 DoH 配置为主，应用 API 待核"),
             H("dnsOverHttps", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         )),
        ("network.connection.validated", "网络校验状态", "Network Validation State",
         "查询网络是否通过系统连通性校验。",
         ["NET_CAPABILITY_VALIDATED"], ["路径监视见 connection.path"],
         merge_bindings(
             A("NET_CAPABILITY_VALIDATED",
               "https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_VALIDATED"),
             I("NWPath.status", "https://developer.apple.com/documentation/network/nwpath/status", "property"),
             H("netCapabilities", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection"),
         )),
        ("network.connection.captive_portal", "强制门户检测", "Captive Portal Detection",
         "检测当前网络是否处于强制门户/登录页状态。",
         ["captive portal capability"], ["路径监视见 connection.path"],
         merge_bindings(
             A("NET_CAPABILITY_CAPTIVE_PORTAL",
               "https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_CAPTIVE_PORTAL"),
             pending("ios", "系统处理为主，应用 API 待核"),
             pending("harmonyos"),
         )),
        ("network.connection.bandwidth", "带宽与链路估计", "Bandwidth Estimation",
         "查询或估计上下行带宽/链路能力。",
         ["LINK_DOWNSTREAM_BANDWIDTH_KBPS、NWPath"], ["计费感知见 connection.metered"],
         merge_bindings(
             A("getLinkDownstreamBandwidthKbps",
               "https://developer.android.com/reference/android/net/NetworkCapabilities#getLinkDownstreamBandwidthKbps()"),
             I("NWPath", "https://developer.apple.com/documentation/network/nwpath", "class"),
             H("netCapabilities", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection"),
         )),
        ("network.connection.dns_custom", "自定义DNS规则", "Custom DNS Rules",
         "为请求指定自定义 DNS 服务器或静态解析规则。",
         ["dnsRules、DnsResolver"], ["DoH 见 connection.doh"],
         merge_bindings(
             A("DnsResolver", "https://developer.android.com/reference/android/net/DnsResolver"),
             pending("ios"),
             H("Rcp_DnsConfiguration", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rcp-development-guide"),
         )),
        ("network.connection.background_transfer", "系统后台传输", "System Background Transfer",
         "由系统托管的后台下载/上传任务。",
         ["DownloadManager、URLSession background"], ["前台请求见 network.http.client"],
         merge_bindings(
             A("DownloadManager", "https://developer.android.com/reference/android/app/DownloadManager"),
             I("background URLSession",
               "https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1411552-background", "method"),
             pending("harmonyos"),
         )),
    ]:
        f.append(feature(
            fid, parent="network.connection", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="connection_aspect",
            granularity="atomic", bindings=bindings,
        ))

    dedup = {}
    for node in f:
        dedup[node["id"]] = node
    return list(dedup.values())


def main():
    nodes = build()
    path = write_domain("network", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
