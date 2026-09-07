#!/usr/bin/env python3
"""Author the digital_wellbeing domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "wellbeing_capability_family"


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
        "digital_wellbeing", parent=None, level="L1",
        zh="数字健康与家庭守护", en="Digital Wellbeing",
        definition="屏幕使用时间、应用限额、家长控制与专注模式等数字健康能力。",
        includes=['屏幕时间、应用限额、家长控制、专注'],
        excludes=['健康体征数据见 health_home', '通知打扰见 notifications'],
        legacy={'disposition': 'new', 'sources': []},
    ))
    l2 = [
        ('digital_wellbeing.screen_time', '屏幕使用时间', 'Screen Time', '查询与汇报应用/设备使用时长。', ['使用时长、使用报告'], ['限额策略见 app_limits'], []),
        ('digital_wellbeing.app_limits', '应用限额', 'App Limits', '为应用或类别设置使用限额与阻断。', ['限额、阻断、选择器'], ['家长策略见 parental'], []),
        ('digital_wellbeing.parental', '家长控制', 'Parental Controls', '家庭账号下的监护、审批与内容限制。', ['监护、审批、限制'], ['个人专注见 focus'], []),
        ('digital_wellbeing.focus', '专注模式', 'Focus Modes', '专注/勿扰相关的系统模式与应用适配。', ['专注状态、过滤'], ['通知渠道见 notifications'], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="digital_wellbeing", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- digital_wellbeing.screen_time ---
    leaf(f, "digital_wellbeing.screen_time.usage_query", "digital_wellbeing.screen_time", "screen_time_operation", "使用时长查询", "Usage Duration Query",
         "查询应用或设备屏幕使用时长统计。", ['UsageStatsManager / DeviceActivity'], ['限额见 app_limits'],
         B(('UsageStatsManager', 'https://developer.android.com/reference/android/app/usage/UsageStatsManager'), ('DeviceActivity', 'https://developer.apple.com/documentation/deviceactivity', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "digital_wellbeing.screen_time.events", "digital_wellbeing.screen_time", "screen_time_operation", "使用事件流", "Usage Event Stream",
         "读取应用前台/通知等使用事件流。", ['UsageEvents'], ['聚合查询见 usage_query'],
         B(('UsageEvents', 'https://developer.android.com/reference/android/app/usage/UsageEvents'), ('DeviceActivityData', 'https://developer.apple.com/documentation/deviceactivity', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "digital_wellbeing.screen_time.report_ui", "digital_wellbeing.screen_time", "screen_time_operation", "使用报告界面", "Usage Report UI",
         "展示或跳转系统使用报告界面。", ['screen time report'], ['查询 API 见 usage_query'],
         B(('Digital Wellbeing', 'https://developer.android.com/guide/topics/usage', 'guide'), ('Screen Time API', 'https://developer.apple.com/documentation/screentime', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.screen_time.category_stats", "digital_wellbeing.screen_time", "screen_time_operation", "类别使用统计", "Category Usage Stats",
         "按应用类别聚合使用时长。", ['category stats'], ['应用级见 usage_query'],
         B(('UsageStats', 'https://developer.android.com/reference/android/app/usage/UsageStats'), ('DeviceActivityFilter', 'https://developer.apple.com/documentation/deviceactivity', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.screen_time.token_auth", "digital_wellbeing.screen_time", "screen_time_operation", "屏幕时间授权令牌", "Screen Time Auth Token",
         "获取家庭/屏幕时间能力授权令牌。", ['AuthorizationCenter'], ['查询见 usage_query'],
         B(None, ('AuthorizationCenter', 'https://developer.apple.com/documentation/familycontrols/authorizationcenter', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")

    # --- digital_wellbeing.app_limits ---
    leaf(f, "digital_wellbeing.app_limits.set_limit", "digital_wellbeing.app_limits", "app_limits_operation", "设置应用限额", "Set App Limit",
         "为应用或类别设置每日使用限额。", ['ManagedSettings / AppTimer'], ['阻断见 shield'],
         B(None, ('ManagedSettings', 'https://developer.apple.com/documentation/managedsettings', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.app_limits.shield", "digital_wellbeing.app_limits", "app_limits_operation", "超限阻断护盾", "Limit Shield",
         "在超限时展示阻断护盾界面。", ['shield'], ['设置限额见 set_limit'],
         B(None, ('ManagedSettingsStore', 'https://developer.apple.com/documentation/managedsettings', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.app_limits.picker", "digital_wellbeing.app_limits", "app_limits_operation", "应用类别选择器", "App Category Picker",
         "选择受限额约束的应用或类别。", ['FamilyActivityPicker'], ['限额见 set_limit'],
         B(None, ('FamilyActivityPicker', 'https://developer.apple.com/documentation/familycontrols', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.app_limits.monitor", "digital_wellbeing.app_limits", "app_limits_operation", "限额监测扩展", "Limit Monitor Extension",
         "在后台监测使用并触发限额事件。", ['DeviceActivityMonitor'], ['事件流见 screen_time.events'],
         B(None, ('DeviceActivityMonitor', 'https://developer.apple.com/documentation/deviceactivity/deviceactivitymonitor', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.app_limits.schedule", "digital_wellbeing.app_limits", "app_limits_operation", "限额时间表", "Limit Schedule",
         "按时间表启用或停用限额。", ['schedule'], ['设置限额见 set_limit'],
         B(None, ('DeviceActivitySchedule', 'https://developer.apple.com/documentation/deviceactivity', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.app_limits.android_policy", "digital_wellbeing.app_limits", "app_limits_operation", "使用访问策略", "Usage Access Policy",
         "基于使用情况访问权限实施限制策略入口。", ['PACKAGE_USAGE_STATS policies'], ['查询见 screen_time'],
         B(('UsageStatsManager', 'https://developer.android.com/reference/android/app/usage/UsageStatsManager'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")

    # --- digital_wellbeing.parental ---
    leaf(f, "digital_wellbeing.parental.family_auth", "digital_wellbeing.parental", "parental_operation", "家庭监护授权", "Family Guardianship Auth",
         "请求家庭控件/监护授权。", ['FamilyControls auth'], ['审批见 ask_to_buy'],
         B(None, ('FamilyControls', 'https://developer.apple.com/documentation/familycontrols', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "digital_wellbeing.parental.ask_to_buy", "digital_wellbeing.parental", "parental_operation", "购买与下载审批", "Ask to Buy Approval",
         "儿童购买或下载需监护人审批。", ['Ask to Buy / parental approval'], ['内容过滤见 content_restrict'],
         B(None, ('FamilySharing', 'https://developer.apple.com/documentation/storekit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.parental.content_restrict", "digital_wellbeing.parental", "parental_operation", "内容分级限制", "Content Rating Restrictions",
         "按分级限制应用、媒体或网页内容。", ['content restrictions'], ['应用限额见 app_limits'],
         B(('Restrictions', 'https://developer.android.com/work/dpc/build-dpc', 'guide'), ('Screen Time restrictions', 'https://developer.apple.com/documentation/screentime', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.parental.device_supervise", "digital_wellbeing.parental", "parental_operation", "设备监督配置", "Supervised Device Config",
         "对受监护设备下发基础监督配置。", ['supervised device'], ['企业 MDM 见 enterprise'],
         B(None, ('Supervised devices', 'https://developer.apple.com/documentation/devicedevice', 'other'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.parental.remote_manage", "digital_wellbeing.parental", "parental_operation", "远程家长管理", "Remote Parental Manage",
         "监护人远程查看或调整孩子设备限制。", ['remote parental'], ['本机限额见 app_limits'],
         B(None, ('FamilyControls', 'https://developer.apple.com/documentation/familycontrols', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.parental.account_link", "digital_wellbeing.parental", "parental_operation", "亲子账号关联", "Parent-Child Account Link",
         "关联亲子账号以启用监护能力。", ['family account link'], ['授权见 family_auth'],
         B(None, ('FamilySharing', 'https://developer.apple.com/family-sharing/', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- digital_wellbeing.focus ---
    leaf(f, "digital_wellbeing.focus.status", "digital_wellbeing.focus", "focus_operation", "专注模式状态", "Focus Mode Status",
         "读取当前专注/勿扰状态。", ['FocusStatusCenter / ZenMode'], ['意图过滤见 intent_filter'],
         B(('NotificationManager', 'https://developer.android.com/reference/android/app/NotificationManager'), ('FocusStatusCenter', 'https://developer.apple.com/documentation/intents/focusstatuscenter', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.focus.intent_filter", "digital_wellbeing.focus", "focus_operation", "专注意图过滤", "Focus Intent Filtering",
         "在专注模式下过滤可打断的意图或通知。", ['focus filter'], ['状态见 status'],
         B(('InterruptionFilter', 'https://developer.android.com/reference/android/app/NotificationManager'), ('FocusFilterIntent', 'https://developer.apple.com/documentation/appintents', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.focus.profile_config", "digital_wellbeing.focus", "focus_operation", "专注配置档", "Focus Profile Config",
         "配置专注模式允许的应用与联系人。", ['focus config'], ['状态见 status'],
         B(None, ('Focus', 'https://support.apple.com/guide/iphone/focus-ipha0fc1b5d2/ios', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.focus.activity_share", "digital_wellbeing.focus", "focus_operation", "专注状态共享", "Focus Status Sharing",
         "向联系人或系统共享当前专注状态。", ['share focus status'], ['状态见 status'],
         B(None, ('FocusStatusCenter', 'https://developer.apple.com/documentation/intents/focusstatuscenter', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "digital_wellbeing.focus.schedule", "digital_wellbeing.focus", "focus_operation", "专注时间表", "Focus Schedule",
         "按时间或位置自动启用专注模式。", ['focus schedule'], ['配置档见 profile_config'],
         B(('AutomaticZenRule', 'https://developer.android.com/reference/android/app/AutomaticZenRule'), ('Focus', 'https://developer.apple.com/focus/', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")


    leaf(f, "digital_wellbeing.screen_time.notification_stats", "digital_wellbeing.screen_time", "screen_time_operation", "通知使用统计", "Notification Usage Stats",
         "统计通知到达与互动相关使用数据。", ["notification stats"], ["使用时长见 usage_query"],
         B(("UsageEvents", "https://developer.android.com/reference/android/app/usage/UsageEvents"),
           ("DeviceActivity", "https://developer.apple.com/documentation/deviceactivity", "framework"), None), privacy="runtime_permission")
    leaf(f, "digital_wellbeing.screen_time.unlock_count", "digital_wellbeing.screen_time", "screen_time_operation", "解锁次数统计", "Unlock Count Stats",
         "统计设备解锁次数。", ["unlock count"], ["使用时长见 usage_query"],
         B(("UsageStatsManager", "https://developer.android.com/reference/android/app/usage/UsageStatsManager"),
           ("DeviceActivity", "https://developer.apple.com/documentation/deviceactivity", "framework"), None), privacy="runtime_permission")
    leaf(f, "digital_wellbeing.app_limits.downtime", "digital_wellbeing.app_limits", "app_limits_operation", "停用时间段", "Downtime Schedule",
         "设置设备停用时间段限制应用。", ["downtime"], ["时间表见 schedule"],
         B(None, ("ManagedSettings", "https://developer.apple.com/documentation/managedsettings", "framework"), None))
    leaf(f, "digital_wellbeing.app_limits.website_limit", "digital_wellbeing.app_limits", "app_limits_operation", "网站限额", "Website Limits",
         "对网站或域名设置使用限额。", ["website limits"], ["应用限额见 set_limit"],
         B(None, ("ManagedSettingsStore", "https://developer.apple.com/documentation/managedsettings", "framework"), None))
    leaf(f, "digital_wellbeing.parental.communication_limit", "digital_wellbeing.parental", "parental_operation", "通信限制", "Communication Limits",
         "限制可通话/消息的联系人范围。", ["communication limits"], ["内容限制见 content_restrict"],
         B(None, ("CommunicationLimits", "https://developer.apple.com/documentation/managedsettings", "framework"), None))
    leaf(f, "digital_wellbeing.parental.location_share", "digital_wellbeing.parental", "parental_operation", "家庭位置共享", "Family Location Share",
         "家庭成员间位置共享入口。", ["family location"], ["远程管理见 remote_manage"],
         B(None, ("Find My / Family", "https://developer.apple.com/documentation/", "guide"), None), privacy="runtime_permission")
    leaf(f, "digital_wellbeing.parental.screen_distance", "digital_wellbeing.parental", "parental_operation", "屏幕距离提醒", "Screen Distance Alert",
         "屏幕距离过近提醒能力入口。", ["screen distance"], ["使用报告见 screen_time"],
         B(None, ("Screen Distance", "https://developer.apple.com/documentation/screentime", "framework"), None))
    leaf(f, "digital_wellbeing.focus.drive_mode", "digital_wellbeing.focus", "focus_operation", "驾驶专注", "Driving Focus",
         "驾驶场景专注模式适配。", ["driving focus"], ["状态见 status"],
         B(("AutomaticZenRule", "https://developer.android.com/reference/android/app/AutomaticZenRule"),
           ("Focus Driving", "https://developer.apple.com/focus/", "guide"), None))
    leaf(f, "digital_wellbeing.focus.sleep_mode", "digital_wellbeing.focus", "focus_operation", "睡眠专注", "Sleep Focus",
         "睡眠场景专注模式适配。", ["sleep focus"], ["状态见 status"],
         B(("AutomaticZenRule", "https://developer.android.com/reference/android/app/AutomaticZenRule"),
           ("Sleep Focus", "https://developer.apple.com/focus/", "guide"), None))
    leaf(f, "digital_wellbeing.focus.allowed_people", "digital_wellbeing.focus", "focus_operation", "允许打断联系人", "Allowed Interrupt People",
         "配置专注模式下允许打断的联系人。", ["allowed people"], ["配置档见 profile_config"],
         B(("NotificationManager.Policy", "https://developer.android.com/reference/android/app/NotificationManager.Policy"),
           ("Focus allowed people", "https://developer.apple.com/focus/", "guide"), None))
    leaf(f, "digital_wellbeing.focus.app_exceptions", "digital_wellbeing.focus", "focus_operation", "专注应用例外", "Focus App Exceptions",
         "配置专注模式下仍允许通知的应用。", ["app exceptions"], ["意图过滤见 intent_filter"],
         B(("NotificationManager.Policy", "https://developer.android.com/reference/android/app/NotificationManager.Policy"),
           ("Focus allowed apps", "https://developer.apple.com/focus/", "guide"), None))
    leaf(f, "digital_wellbeing.screen_time.pickup_stats", "digital_wellbeing.screen_time", "screen_time_operation", "拿起次数统计", "Pickup Count Stats",
         "统计设备拿起/唤醒相关次数。", ["pickups"], ["解锁见 unlock_count"],
         B(None, ("DeviceActivity", "https://developer.apple.com/documentation/deviceactivity", "framework"), None), privacy="runtime_permission")


    leaf(f, "digital_wellbeing.app_limits.always_allowed", "digital_wellbeing.app_limits", "app_limits_operation", "始终允许应用", "Always Allowed Apps",
         "配置不受限额约束的始终允许应用。", ["always allowed"], ["限额见 set_limit"],
         B(None, ("ManagedSettingsStore", "https://developer.apple.com/documentation/managedsettings", "framework"), None))

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("digital_wellbeing", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
