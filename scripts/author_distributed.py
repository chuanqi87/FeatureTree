#!/usr/bin/env python3
"""Author the distributed domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "distributed_capability_family"


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
        "distributed", parent=None, level="L1",
        zh="分布式与多端", en="Distributed and Continuity",
        definition="跨设备任务接续、近场发现连接、软总线、配件与穿戴链路、共享体验与跨端数据同步。",
        includes=['接续、附近连接、软总线、配件、穿戴链路、共享体验、跨端同步'],
        excludes=['connectivity 近距无线协议', 'network HTTP/Socket', 'storage 本机持久化'],
        legacy={'disposition': 'kept', 'sources': ['distributed']},
    ))
    l2 = [
        ('distributed.continuity', '任务接续', 'Task Continuity', '跨已登录设备接续同一用户任务与应用状态。', ['handoff、迁移、多端协同'], ['附近临时会话见 nearby'], ['distributed.continuity']),
        ('distributed.nearby', '附近设备发现与连接', 'Nearby Discovery and Connection', '近场设备发现、会话建立与点对点数据通道。', ['发现、连接、会话、快传'], ['账号接续见 continuity'], ['distributed.nearby']),
        ('distributed.softbus', '分布式软总线', 'Distributed Soft Bus', '跨设备设备管理、RPC/代理通道与链路增强。', ['设备管理、RPC、代理通道'], ['应用层接续见 continuity'], ['distributed.softbus']),
        ('distributed.companion', '配件关联与虚拟外设', 'Companion and Virtual Peripherals', '手机与配件信任配对及虚拟外设能力共享。', ['配对、虚拟外设'], ['穿戴消息见 wear_link'], []),
        ('distributed.wear_link', '穿戴设备链路', 'Wearable Device Link', '手机与穿戴设备的消息、文件、状态与远程应用通道。', ['消息、文件、状态、远程应用'], ['通用 BLE 见 connectivity'], []),
        ('distributed.share_experience', '跨端共享体验', 'Cross-Device Shared Experience', '跨设备剪贴板、拖拽、同屏协作与共享活动。', ['剪贴板、拖拽、共享活动'], ['文件快传见 nearby'], []),
        ('distributed.data_sync', '跨端数据同步', 'Cross-Device Data Sync', '分布式对象/库/文件及穿戴数据层同步。', ['对象、库、文件、穿戴数据层'], ['账号云同步见 storage.cloud'], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="distributed", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- distributed.continuity ---
    leaf(f, "distributed.continuity.handoff", "distributed.continuity", "continuity_operation", "跨设备活动接续", "Activity Handoff",
         "将当前活动状态传到另一台同账号设备并继续。", ['NSUserActivity、App Continuity'], ['整包迁移见 migration'],
         B(('App Continuity', 'https://developer.android.com/guide/topics/large-screens/app-continuity', 'guide'), ('NSUserActivity', 'https://developer.apple.com/documentation/foundation/nsuseractivity', 'class'), ('UIAbility migration', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hop-cross-device-migration')), {'disposition': 'kept', 'sources': ['distributed.continuity.handoff']}, level="L3", privacy="runtime_permission")
    leaf(f, "distributed.continuity.migration", "distributed.continuity", "continuity_operation", "应用跨端迁移", "App Cross-Device Migration",
         "将应用任务整体迁移到另一设备并恢复运行上下文。", ['migrateTo、continue'], ['轻量接续见 handoff'],
         B(None, ('Handoff', 'https://developer.apple.com/handoff/', 'guide'), ('startAbility migrate', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hop-cross-device-migration')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.continuity.multi_device", "distributed.continuity", "continuity_operation", "多端协同会话", "Multi-Device Collaboration",
         "同一业务在多台设备上协同运行并同步协作状态。", ['multi-device collaboration'], ['单设备接续见 handoff'],
         B(None, ('Group Activities', 'https://developer.apple.com/documentation/groupactivities', 'framework'), ('distributed collaboration', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hop-multi-device-collaboration')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.continuity.spec", "distributed.continuity", "continuity_operation", "接续兼容规格", "Continuity Compatibility Spec",
         "声明与校验跨端接续所需能力与兼容规格。", ['continueType、兼容声明'], ['实际迁移见 migration'],
         B(None, None, ('continueType', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hop-cross-device-migration')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.continuity.device_picker", "distributed.continuity", "continuity_operation", "接续设备选择", "Continuity Device Picker",
         "按能力过滤并展示可选接续目标设备。", ['device picker、capability filter'], ['附近发现见 nearby.discovery'],
         B(None, None, ('distributedDeviceManager', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "distributed.continuity.state", "distributed.continuity", "continuity_operation", "接续状态回调", "Continuity State Callbacks",
         "监听接续成功、失败与进行中状态。", ['onContinue、completion'], ['发起接续见 handoff'],
         B(None, ('NSUserActivityDelegate', 'https://developer.apple.com/documentation/foundation/nsuseractivitydelegate', 'protocol'), ('UIAbility onContinue', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hop-cross-device-migration')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- distributed.nearby ---
    leaf(f, "distributed.nearby.discovery", "distributed.nearby", "nearby_operation", "附近设备发现", "Nearby Device Discovery",
         "发现周边可连接设备并接收发现结果。", ['startDiscovery、advertising'], ['连接见 connection'],
         B(('Nearby Connections', 'https://developers.google.com/nearby/connections/overview', 'guide'), ('Multipeer Connectivity', 'https://developer.apple.com/documentation/multipeerconnectivity', 'framework'), ('distributedDeviceManager', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager')), {'disposition': 'kept', 'sources': ['distributed.nearby.discovery']}, level="L3", privacy="runtime_permission")
    leaf(f, "distributed.nearby.connection", "distributed.nearby", "nearby_operation", "附近点对点连接", "Nearby Peer Connection",
         "建立近场点对点连接并收发载荷。", ['requestConnection、payload'], ['发现见 discovery'],
         B(('ConnectionsClient', 'https://developers.google.com/nearby/connections/android/get-started', 'guide'), ('MCSession', 'https://developer.apple.com/documentation/multipeerconnectivity/mcsession', 'class'), ('SoftBus session', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/softbus-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "distributed.nearby.session", "distributed.nearby", "nearby_operation", "附近会话管理", "Nearby Session Management",
         "管理近场会话生命周期与成员。", ['session create/join/leave'], ['连接通道见 connection'],
         B(('Nearby Connections', 'https://developers.google.com/nearby/connections/overview', 'guide'), ('MCSession', 'https://developer.apple.com/documentation/multipeerconnectivity/mcsession', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.nearby.wakeup", "distributed.nearby", "nearby_operation", "近场设备唤醒", "Nearby Device Wakeup",
         "通过近场机制唤醒目标设备侧应用或服务。", ['wakeup'], ['发现见 discovery'],
         B(None, None, ('remote wakeup', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hop-cross-device-migration')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.nearby.knock", "distributed.nearby", "nearby_operation", "碰一碰触发", "Tap Knock Trigger",
         "通过轻碰触发近场配对或分享。", ['knock share'], ['通用分享见 interop'],
         B(('Nearby Share', 'https://developers.google.com/nearby/sharing', 'guide'), None, ('Share Kit', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-kit-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.nearby.gesture_share", "distributed.nearby", "nearby_operation", "隔空手势分享", "Air Gesture Share",
         "基于空间手势将内容投向附近设备。", ['air gesture share'], ['碰一碰见 knock'],
         B(None, ('AirDrop', 'https://developer.apple.com/airdrop/', 'guide'), ('Share Kit', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-kit-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.nearby.file_transfer", "distributed.nearby", "nearby_operation", "近场文件快传", "Nearby File Transfer",
         "在附近设备间高速传输文件。", ['file payload'], ['穿戴文件见 wear_link.file_transfer'],
         B(('Nearby Payload', 'https://developers.google.com/nearby/connections/android/exchange-data', 'guide'), ('Multipeer Connectivity', 'https://developer.apple.com/documentation/multipeerconnectivity', 'framework'), ('Share Kit', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-kit-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "distributed.nearby.uwb_session", "distributed.nearby", "nearby_operation", "近场UWB会话", "Nearby UWB Session",
         "基于超宽带建立空间感知近场会话。", ['UWB session'], ['UWB 测距硬件见 connectivity'],
         B(('UwbManager', 'https://developer.android.com/develop/connectivity/uwb', 'guide'), ('Nearby Interaction', 'https://developer.apple.com/documentation/nearbyinteraction', 'framework'), ('nearbyInteraction', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nearbyinteraction')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")

    # --- distributed.softbus ---
    leaf(f, "distributed.softbus.fabric", "distributed.softbus", "softbus_operation", "软总线组网", "Soft Bus Fabric",
         "加入并维护分布式软总线组网拓扑。", ['fabric join'], ['RPC 见 rpc'],
         B(None, None, ('SoftBus', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/softbus-overview')), {'disposition': 'kept', 'sources': ['distributed.softbus.fabric']}, level="L3", privacy="none")
    leaf(f, "distributed.softbus.device_manager", "distributed.softbus", "softbus_operation", "分布式设备管理", "Distributed Device Manager",
         "查询可信设备列表与在线状态。", ['getAvailableDeviceList'], ['组网见 fabric'],
         B(None, None, ('distributedDeviceManager', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.softbus.rpc", "distributed.softbus", "softbus_operation", "跨设备RPC", "Cross-Device RPC",
         "通过软总线发起跨设备远程过程调用。", ['RPC stub/proxy'], ['代理通道见 proxy_channel'],
         B(None, None, ('RPC', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ipc-rpc-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.softbus.proxy_channel", "distributed.softbus", "softbus_operation", "代理数据通道", "Proxy Data Channel",
         "建立跨设备代理字节流或消息通道。", ['proxy channel'], ['RPC 见 rpc'],
         B(None, None, ('SoftBus session', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/softbus-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.softbus.link_enhance", "distributed.softbus", "softbus_operation", "链路增强", "Link Enhancement",
         "对跨设备链路做带宽与时延增强调度。", ['link enhance'], ['组网见 fabric'],
         B(None, None, ('SoftBus', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/softbus-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.softbus.capability_call", "distributed.softbus", "softbus_operation", "跨端能力调用", "Cross-Device Capability Call",
         "按能力描述调用远端设备已发布能力。", ['capability call'], ['RPC 底层见 rpc'],
         B(None, None, ('distributed capability', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hop-multi-device-collaboration')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.softbus.mechanic", "distributed.softbus", "softbus_operation", "特殊外设总线扩展", "Specialty Bus Extension",
         "面向机械臂等特殊外设的软总线扩展接入。", ['mechanic bus'], ['USB 见 connectivity.usb'],
         B(None, None, ('SoftBus', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/softbus-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- distributed.companion ---
    leaf(f, "distributed.companion.pairing", "distributed.companion", "companion_operation", "配件信任配对", "Companion Trust Pairing",
         "建立手机与配件间的信任关联与授权。", ['CompanionDeviceManager'], ['穿戴消息见 wear_link'],
         B(('CompanionDeviceManager', 'https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing'), ('AccessorySetupKit', 'https://developer.apple.com/documentation/accessorysetupkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "distributed.companion.virtual_keyboard_mouse", "distributed.companion", "companion_operation", "虚拟键鼠共享", "Virtual Keyboard Mouse",
         "将键鼠输入虚拟化为跨设备输入源。", ['virtual keyboard/mouse'], ['配对见 pairing'],
         B(None, None, ('distributed input', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hop-multi-device-collaboration')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.companion.virtual_camera", "distributed.companion", "companion_operation", "虚拟相机共享", "Virtual Camera Share",
         "将一端相机能力作为虚拟设备供另一端使用。", ['distributed camera'], ['媒体采集见 media.capture'],
         B(None, None, ('distributed camera', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-distributed')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "distributed.companion.virtual_wear", "distributed.companion", "companion_operation", "虚拟穿戴外设", "Virtual Wear Peripheral",
         "将穿戴侧传感器或交互能力虚拟化给主机应用。", ['wear virtual peripheral'], ['wear 消息见 wear_link'],
         B(('Wearable Data Layer', 'https://developer.android.com/training/wearables/data', 'guide'), ('Watch Connectivity', 'https://developer.apple.com/documentation/watchconnectivity', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.companion.state", "distributed.companion", "companion_operation", "配件关联状态", "Companion Association State",
         "查询并监听配件关联与在线状态。", ['association state'], ['配对见 pairing'],
         B(('CompanionDeviceManager', 'https://developer.android.com/reference/android/companion/CompanionDeviceManager'), ('WCSession', 'https://developer.apple.com/documentation/watchconnectivity/wcsession', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.companion.richeditor", "distributed.companion", "companion_operation", "控件级跨端互通", "Control-Level Interop",
         "编辑控件在跨端场景下的互通接入。", ['distributed rich editor'], ['共享拖拽见 share_experience'],
         B(None, None, ('RichEditor', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richtext')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- distributed.wear_link ---
    leaf(f, "distributed.wear_link.message", "distributed.wear_link", "wear_link_operation", "穿戴消息通道", "Wear Message Channel",
         "手机与穿戴间收发消息与数据项。", ['MessageClient、sendMessage'], ['文件见 file_transfer'],
         B(('MessageClient', 'https://developer.android.com/training/wearables/data/messages', 'guide'), ('WCSession.sendMessage', 'https://developer.apple.com/documentation/watchconnectivity/wcsession', 'class'), ('wearEngine', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wearengine')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.wear_link.file_transfer", "distributed.wear_link", "wear_link_operation", "穿戴文件传输", "Wear File Transfer",
         "在手机与穿戴间传输文件。", ['DataClient assets、transferFile'], ['消息见 message'],
         B(('DataClient', 'https://developer.android.com/training/wearables/data/sync', 'guide'), ('WCSession.transferFile', 'https://developer.apple.com/documentation/watchconnectivity/wcsession', 'class'), ('wearEngine', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wearengine')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.wear_link.device_status", "distributed.wear_link", "wear_link_operation", "穿戴设备状态", "Wear Device Status",
         "查询穿戴在线、佩戴与电量等状态。", ['NodeClient、isReachable'], ['消息见 message'],
         B(('NodeClient', 'https://developer.android.com/training/wearables/data/nodes', 'guide'), ('WCSession.isReachable', 'https://developer.apple.com/documentation/watchconnectivity/wcsession/1615683-isreachable', 'property'), ('wearEngine', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wearengine')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.wear_link.device_select", "distributed.wear_link", "wear_link_operation", "穿戴设备选择", "Wear Device Selection",
         "选择目标穿戴节点作为通信对端。", ['connected nodes'], ['状态见 device_status'],
         B(('CapabilityClient', 'https://developer.android.com/training/wearables/data/capabilities', 'guide'), ('WCSession', 'https://developer.apple.com/documentation/watchconnectivity/wcsession', 'class'), ('wearEngine', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wearengine')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.wear_link.sensor_data", "distributed.wear_link", "wear_link_operation", "穿戴传感器数据订阅", "Wear Sensor Data Subscribe",
         "订阅穿戴侧运动或健康传感器数据流。", ['sensor subscribe'], ['健康库见 health_home'],
         B(('Wearable Sensors', 'https://developer.android.com/training/wearables/apps/sensors', 'guide'), ('HealthKit', 'https://developer.apple.com/documentation/healthkit', 'framework'), ('wearEngine', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wearengine')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "distributed.wear_link.remote_app", "distributed.wear_link", "wear_link_operation", "穿戴远程应用控制", "Wear Remote App Control",
         "在穿戴上启动或控制配对应用。", ['remote launch'], ['消息见 message'],
         B(('RemoteActivityHelper', 'https://developer.android.com/training/wearables/apps/opening-on-phone', 'guide'), ('WatchKit', 'https://developer.apple.com/documentation/watchkit', 'framework'), ('wearEngine', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wearengine')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.wear_link.template_notification", "distributed.wear_link", "wear_link_operation", "穿戴模板通知", "Wear Template Notification",
         "向穿戴下发模板化通知或卡片。", ['wear notification bridge'], ['本机通知见 notifications'],
         B(('NotificationCompat.WearableExtender', 'https://developer.android.com/develop/ui/views/notifications/wear', 'guide'), ('UserNotifications', 'https://developer.apple.com/documentation/usernotifications', 'framework'), ('wearEngine', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wearengine')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.wear_link.p2p_message", "distributed.wear_link", "wear_link_operation", "穿戴直连消息", "Wear P2P Message",
         "在手机与穿戴间建立直连消息通道。", ['ChannelClient'], ['通用消息见 message'],
         B(('ChannelClient', 'https://developer.android.com/training/wearables/data/messages', 'guide'), ('WCSession', 'https://developer.apple.com/documentation/watchconnectivity/wcsession', 'class'), ('wearEngine', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wearengine')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.wear_link.lite_profile", "distributed.wear_link", "wear_link_operation", "轻量穿戴配置", "Lite Wear Profile",
         "面向轻量穿戴设备的精简链路配置与能力协商。", ['lite wear profile'], ['完整消息见 message'],
         B(None, None, ('wearEngine', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wearengine')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- distributed.share_experience ---
    leaf(f, "distributed.share_experience.clipboard", "distributed.share_experience", "share_experience_operation", "跨设备剪贴板", "Cross-Device Clipboard",
         "在受信任设备间同步剪贴板内容。", ['universal clipboard'], ['本机剪贴板见 input'],
         B(None, ('UIPasteboard', 'https://developer.apple.com/documentation/uikit/uipasteboard', 'class'), ('pasteboard', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pasteboard')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.share_experience.cross_drag", "distributed.share_experience", "share_experience_operation", "跨设备拖拽", "Cross-Device Drag and Drop",
         "在多设备间拖拽传递内容。", ['cross-device drag'], ['本机拖拽见 input'],
         B(None, ('UIDragInteraction', 'https://developer.apple.com/documentation/uikit/uidraginteraction', 'class'), ('drag drop', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-drag-drop')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.share_experience.group_activity", "distributed.share_experience", "share_experience_operation", "共享群组活动", "Shared Group Activity",
         "创建跨用户或跨设备共享活动会话。", ['GroupSession'], ['接续见 continuity'],
         B(None, ('GroupActivity', 'https://developer.apple.com/documentation/groupactivities/groupactivity', 'protocol'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.share_experience.tabletop", "distributed.share_experience", "share_experience_operation", "桌面同屏协作", "Tabletop Collaboration",
         "多设备在同一桌面场景下同屏协作。", ['tabletop share'], ['共享活动见 group_activity'],
         B(None, ('SharePlay', 'https://developer.apple.com/shareplay/', 'guide'), ('multi-device collaboration', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hop-multi-device-collaboration')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.share_experience.state", "distributed.share_experience", "share_experience_operation", "共享体验状态", "Share Experience State",
         "监听共享体验会话状态与成员变更。", ['session state'], ['建立会话见 group_activity'],
         B(None, ('GroupSession', 'https://developer.apple.com/documentation/groupactivities/groupsession', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.share_experience.screen_share", "distributed.share_experience", "share_experience_operation", "跨端屏幕共享", "Cross-Device Screen Share",
         "将屏幕内容共享到另一受信任设备。", ['screen share'], ['录屏见 graphics.capture'],
         B(('MediaProjection', 'https://developer.android.com/reference/android/media/projection/MediaProjection'), ('RPBroadcastSampleHandler', 'https://developer.apple.com/documentation/replaykit', 'framework'), ('screen share', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hop-multi-device-collaboration')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")

    # --- distributed.data_sync ---
    leaf(f, "distributed.data_sync.data_object", "distributed.data_sync", "data_sync_operation", "分布式数据对象", "Distributed Data Object",
         "跨设备同步内存对象图并监听变更。", ['distributedDataObject'], ['关系库同步见 distributed_db'],
         B(None, None, ('distributedDataObject', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-distributeddataobject')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.data_sync.distributed_db", "distributed.data_sync", "data_sync_operation", "分布式数据库同步", "Distributed Database Sync",
         "跨设备同步关系或键值数据库。", ['distributed KV/RDB'], ['对象同步见 data_object'],
         B(None, ('NSUbiquitousKeyValueStore', 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore', 'class'), ('distributedKVStore', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributedkvstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.data_sync.distributed_file", "distributed.data_sync", "data_sync_operation", "分布式文件同步", "Distributed File Sync",
         "跨设备访问或同步分布式文件系统路径。", ['distributed file'], ['本机文件见 storage'],
         B(None, ('NSFileCoordinator', 'https://developer.apple.com/documentation/foundation/nsfilecoordinator', 'class'), ('distributedFileManager', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-distributedfilemanager')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.data_sync.wear_data_layer", "distributed.data_sync", "data_sync_operation", "穿戴数据层同步", "Wear Data Layer Sync",
         "通过穿戴数据层同步数据项与资源。", ['DataClient putDataItem'], ['消息通道见 wear_link.message'],
         B(('DataClient', 'https://developer.android.com/training/wearables/data/sync', 'guide'), ('WCSession.transferUserInfo', 'https://developer.apple.com/documentation/watchconnectivity/wcsession', 'class'), ('wearEngine', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wearengine')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.data_sync.cloud_bridge", "distributed.data_sync", "data_sync_operation", "端云桥接同步", "Device-Cloud Bridge Sync",
         "将跨端同步与账号云存储桥接。", ['device-cloud bridge'], ['纯云记录见 storage.cloud'],
         B(None, ('CloudKit', 'https://developer.apple.com/documentation/cloudkit', 'framework'), ('cloud sync', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-cloud-sync')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "distributed.data_sync.conflict", "distributed.data_sync", "data_sync_operation", "跨端同步冲突处理", "Sync Conflict Handling",
         "处理分布式同步冲突与版本合并策略入口。", ['conflict resolver'], ['同步通道见 distributed_db'],
         B(None, ('NSFileVersion', 'https://developer.apple.com/documentation/foundation/nsfileversion', 'class'), ('distributedKVStore', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributedkvstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("distributed", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
