#!/usr/bin/env python3
"""Author the notifications domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "notification_capability_family"


def atomic(fid, parent, axis, zh, en, definition, includes, excludes, bindings, legacy=None, privacy="none", related=None):
    return feature(
        fid, parent=parent, level="L" + str(parent.count(".") + 2),
        zh=zh, en=en, definition=definition,
        includes=includes, excludes=excludes, sibling_axis=axis,
        granularity="atomic", bindings=bindings,
        legacy=legacy or {"disposition": "new", "sources": []},
        privacy_class=privacy, related=related,
    )


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "notifications", parent=None, level="L1",
        zh="通知与推送", en="Notifications and Push",
        definition="本地通知构建展示、远程推送通道、渠道分类、交互动作、角标、实时活动/ongoing 与勿扰策略；不含跨端 Continuity 编排。",
        includes=["本地通知、推送、渠道、动作、角标、实时活动、勿扰"],
        excludes=["跨端流转见 distributed", "媒体播控会话见 media.session"],
        legacy={"disposition": "kept", "sources": ["notifications"]},
    ))

    l2 = [
        ("notifications.local", "本地通知", "Local Notifications",
         "由本机应用创建、调度与展示的通知内容与样式。",
         ["构建发布、样式、分组、进度、可见性、点击意图"],
         ["远程推送见 notifications.push", "渠道配置见 notifications.channels"],
         ["notifications.local"]),
        ("notifications.push", "远程推送", "Remote Push",
         "远程推送标识、静默/优先消息与通道侧能力。",
         ["token、静默、优先、回执、撤回、场景消息"],
         ["本地构建见 notifications.local"],
         ["notifications.push"]),
        ("notifications.channels", "通知渠道与分类", "Notification Channels",
         "通知渠道、分类与重要性/打断级别配置。",
         ["渠道创建、分类、重要性"],
         ["通知正文见 notifications.local"],
         ["notifications.push.channel"]),
        ("notifications.actions", "通知交互动作", "Notification Actions",
         "通知上的可操作按钮、直接回复与消除。",
         ["动作按钮、直接回复、消除"],
         ["展示样式见 notifications.local"],
         ["notifications.local.actions"]),
        ("notifications.badges", "角标", "Badges",
         "应用图标角标数量与清除。",
         ["角标设置、清除"],
         ["通知栏展示见 notifications.local"],
         []),
        ("notifications.live_activities", "实时活动与持续通知", "Live Activities and Ongoing",
         "实时活动/实况窗与 ongoing 持续状态通知。",
         ["Live Activity、ongoing、实况窗更新"],
         ["普通本地通知见 notifications.local"],
         []),
        ("notifications.dnd", "勿扰与打断策略", "Do Not Disturb",
         "勿扰模式感知、时效性与打断分级。",
         ["DND 状态、时效性、打断级别"],
         ["渠道重要性见 notifications.channels"],
         []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        disp = "kept" if sources and sources[0] == fid else (
            "renamed_from" if sources else "new"
        )
        f.append(feature(
            fid, parent="notifications", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy={"disposition": disp, "sources": sources},
        ))

    # --- local ---
    for row in [
        ("notifications.local.display", "通知展示与发布", "Notification Display",
         "构建通知内容并发布到系统通知栏/横幅/锁屏。",
         ["NotificationCompat、UNNotificationRequest、publish"],
         ["notifications.local.styles", "notifications.channels"],
         merge_bindings(
             A("NotificationManager.notify",
               "https://developer.android.com/reference/android/app/NotificationManager#notify(int,%20android.app.Notification)"),
             I("UNUserNotificationCenter",
               "https://developer.apple.com/documentation/usernotifications/unusernotificationcenter", "class"),
             H("@ohos.notificationManager",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
         ), {"disposition": "kept", "sources": ["notifications.local.display"]}),
        ("notifications.local.schedule", "本地定时与触发", "Local Schedule",
         "按时间或日历触发本地通知调度。",
         ["schedule、UNCalendarNotificationTrigger"],
         ["notifications.local.display"],
         merge_bindings(
             A("AlarmManager", "https://developer.android.com/reference/android/app/AlarmManager"),
             I("UNCalendarNotificationTrigger",
               "https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger", "class"),
             H("publish", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
         ), None),
        ("notifications.local.styles", "通知内容样式", "Notification Styles",
         "大文本、收件箱、媒体等扩展样式模板。",
         ["BigText、MessagingStyle、UNNotificationContent"],
         ["notifications.local.display"],
         merge_bindings(
             A("NotificationCompat.BigTextStyle",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.BigTextStyle"),
             I("UNNotificationContent",
               "https://developer.apple.com/documentation/usernotifications/unnotificationcontent", "class"),
             H("NotificationContent",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationcontent"),
         ), None),
        ("notifications.local.group", "通知分组与会话", "Notification Grouping",
         "将多条通知归组或会话摘要展示。",
         ["setGroup、threadIdentifier"],
         ["notifications.local.display"],
         merge_bindings(
             A("NotificationCompat.Builder.setGroup",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setGroup(java.lang.String)"),
             I("threadIdentifier",
               "https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/1649872-threadidentifier", "property"),
             H("NotificationRequest",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationrequest"),
         ), None),
        ("notifications.local.progress", "进度通知", "Progress Notification",
         "展示不确定或百分比进度的通知。",
         ["setProgress"],
         ["notifications.local.display"],
         merge_bindings(
             A("NotificationCompat.Builder.setProgress",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setProgress(int,%20int,%20boolean)"),
             pending("ios", "自定义内容扩展展示进度"),
             H("NotificationContent",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationcontent"),
         ), None),
        ("notifications.local.visibility", "锁屏可见性", "Lock Screen Visibility",
         "控制通知在锁屏上的公开/私密可见级别。",
         ["VISIBILITY_PRIVATE、UNNotificationPresentationOptions"],
         ["notifications.local.display"],
         merge_bindings(
             A("Notification.VISIBILITY_PRIVATE",
               "https://developer.android.com/reference/android/app/Notification#VISIBILITY_PRIVATE"),
             I("UNNotificationPresentationOptions",
               "https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptions", "struct"),
             pending("harmonyos"),
         ), None),
        ("notifications.local.click_intent", "通知点击意图", "Notification Click Intent",
         "用户点击通知正文时的深链/拉起目标。",
         ["contentIntent、UNNotificationResponse"],
         ["notifications.actions"],
         merge_bindings(
             A("NotificationCompat.Builder.setContentIntent",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setContentIntent(android.app.PendingIntent)"),
             I("UNNotificationResponse",
               "https://developer.apple.com/documentation/usernotifications/unnotificationresponse", "class"),
             H("NotificationRequest",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationrequest"),
         ), None),
        ("notifications.local.sound", "通知声音", "Notification Sound",
         "自定义或系统默认通知提示音。",
         ["setSound、UNNotificationSound"],
         ["notifications.channels"],
         merge_bindings(
             A("NotificationCompat.Builder.setSound",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setSound(android.net.Uri)"),
             I("UNNotificationSound",
               "https://developer.apple.com/documentation/usernotifications/unnotificationsound", "class"),
             H("NotificationContent",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationcontent"),
         ), None),
        ("notifications.local.cancel", "通知取消", "Cancel Notification",
         "按 id/tag 取消已发布通知或清空。",
         ["cancel、removeDeliveredNotifications"],
         ["notifications.actions.dismiss"],
         merge_bindings(
             A("NotificationManager.cancel",
               "https://developer.android.com/reference/android/app/NotificationManager#cancel(int)"),
             I("removeDeliveredNotifications",
               "https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1647859-removedeliverednotifications", "method"),
             H("cancel",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
         ), None),
        ("notifications.local.permission", "通知授权请求", "Notification Permission",
         "请求用户授予发送通知的权限并查询状态。",
         ["POST_NOTIFICATIONS、requestAuthorization"],
         ["notifications.dnd"],
         merge_bindings(
             A("POST_NOTIFICATIONS",
               "https://developer.android.com/develop/ui/views/notifications/notification-permission"),
             I("requestAuthorization",
               "https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649524-requestauthorization", "method"),
             H("requestEnableNotification",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
         ), None),
    ]:
        fid, zh, en, definition, includes, excludes, bindings, legacy = row
        f.append(atomic(
            fid, "notifications.local", "local_capability",
            zh, en, definition, includes, excludes, bindings, legacy,
            privacy="runtime_permission" if "permission" in fid else "none",
        ))

    # --- push ---
    for row in [
        ("notifications.push.token", "推送标识获取", "Push Token",
         "获取/刷新远程推送设备或应用标识。",
         ["FCM token、APNs device token、getToken"],
         ["notifications.push.silent"],
         merge_bindings(
             A("FirebaseMessaging.getToken",
               "https://firebase.google.com/docs/cloud-messaging/android/client#sample-register"),
             I("didRegisterForRemoteNotifications",
               "https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622958-application", "method"),
             H("getToken",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-gettoken"),
         )),
        ("notifications.push.silent", "静默后台消息", "Silent Push",
         "不展示通知的静默/数据消息以唤醒后台处理。",
         ["data message、content-available"],
         ["notifications.push.priority"],
         merge_bindings(
             A("FirebaseMessagingService.onMessageReceived",
               "https://firebase.google.com/docs/cloud-messaging/android/receive"),
             I("content-available",
               "https://developer.apple.com/documentation/usernotifications/pushing-background-updates-to-your-app", "guide"),
             H("pushType",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-offline"),
         )),
        ("notifications.push.priority", "优先与高优先级推送", "Priority Push",
         "高优先级远程消息以尽快触达或唤醒。",
         ["priority high、interruptionLevel"],
         ["notifications.push.silent"],
         merge_bindings(
             A("Android message priority",
               "https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message", "guide"),
             I("interruptionLevel",
               "https://developer.apple.com/documentation/usernotifications/unnotificationcontent/3727255-interruptionlevel", "property"),
             H("Push 消息分类",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-message-freq-control", "guide"),
         )),
        ("notifications.push.receipt", "消息回执", "Push Receipt",
         "查询或回调推送送达/点击回执。",
         ["delivery receipt"],
         ["notifications.push.recall"],
         merge_bindings(
             pending("android"),
             I("Notification Service Extension",
               "https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension", "class"),
             H("消息回执",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-receipt", "guide"),
         )),
        ("notifications.push.recall", "消息撤回", "Push Recall",
         "撤回已下发但未展示或可撤销的远程通知。",
         ["revoke、collapse key"],
         ["notifications.local.cancel"],
         merge_bindings(
             A("collapse_key",
               "https://firebase.google.com/docs/cloud-messaging/concept-options#collapsible_and_non-collapsible_messages", "guide"),
             I("apns-collapse-id",
               "https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns", "guide"),
             H("消息撤回",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-update-revoke", "guide"),
         )),
        ("notifications.push.voip", "通话类推送", "VoIP Push",
         "面向来电/通话场景的专用推送唤醒。",
         ["PushKit VoIP、CallKit 配合"],
         ["notifications.push.token"],
         merge_bindings(
             pending("android", "电信来电通道见 telecom；FCM 高优待核"),
             I("PushKit", "https://developer.apple.com/documentation/pushkit", "framework"),
             pending("harmonyos"),
         )),
        ("notifications.push.service_subscribe", "服务订阅消息", "Service Subscribe Message",
         "用户订阅后的服务号/场景化推送触达。",
         ["订阅消息、服务通知"],
         ["notifications.push.token"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("服务通知",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-service-notification", "guide"),
         )),
        ("notifications.push.payload_handle", "推送载荷处理", "Push Payload Handling",
         "应用前台/后台接收并解析远程推送载荷。",
         ["onMessageReceived、userNotificationCenter willPresent"],
         ["notifications.push.silent"],
         merge_bindings(
             A("FirebaseMessagingService",
               "https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService"),
             I("UNUserNotificationCenterDelegate",
               "https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate", "protocol"),
             H("Push 接收",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-app-receive", "guide"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atomic(
            fid, "notifications.push", "push_capability",
            zh, en, definition, includes, excludes, bindings,
            privacy="runtime_permission",
        ))

    # --- channels ---
    for row in [
        ("notifications.channels.create", "渠道创建与更新", "Create Channel",
         "创建或更新通知渠道及其名称/描述。",
         ["createNotificationChannel、UNNotificationCategory"],
         ["notifications.channels.importance"],
         merge_bindings(
             A("NotificationManager.createNotificationChannel",
               "https://developer.android.com/reference/android/app/NotificationManager#createNotificationChannel(android.app.NotificationChannel)"),
             I("UNNotificationCategory",
               "https://developer.apple.com/documentation/usernotifications/unnotificationcategory", "class"),
             H("NotificationSlot",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationslot"),
         )),
        ("notifications.channels.importance", "重要性与打断级别", "Channel Importance",
         "配置渠道默认重要性或通知打断级别。",
         ["IMPORTANCE_HIGH、interruptionLevel"],
         ["notifications.channels.create"],
         merge_bindings(
             A("NotificationManager.IMPORTANCE_HIGH",
               "https://developer.android.com/reference/android/app/NotificationManager#IMPORTANCE_HIGH"),
             I("UNNotificationInterruptionLevel",
               "https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel", "enum"),
             H("SlotLevel",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
         )),
        ("notifications.channels.group", "渠道分组", "Channel Groups",
         "将多个渠道归入用户可见分组。",
         ["NotificationChannelGroup"],
         ["notifications.channels.create"],
         merge_bindings(
             A("NotificationChannelGroup",
               "https://developer.android.com/reference/android/app/NotificationChannelGroup"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("notifications.channels.query", "渠道查询与设置跳转", "Channel Query",
         "查询渠道状态并跳转系统通知设置页。",
         ["getNotificationChannel、openNotificationSettings"],
         ["notifications.channels.create"],
         merge_bindings(
             A("NotificationManager.getNotificationChannel",
               "https://developer.android.com/reference/android/app/NotificationManager#getNotificationChannel(java.lang.String)"),
             I("openSettingsURLString",
               "https://developer.apple.com/documentation/uikit/uiapplication/1623042-opensettingsurlstring", "property"),
             H("isNotificationEnabled",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
         )),
        ("notifications.channels.delete", "渠道删除", "Delete Channel",
         "删除应用创建的通知渠道。",
         ["deleteNotificationChannel"],
         ["notifications.channels.create"],
         merge_bindings(
             A("NotificationManager.deleteNotificationChannel",
               "https://developer.android.com/reference/android/app/NotificationManager#deleteNotificationChannel(java.lang.String)"),
             pending("ios"),
             H("removeSlot",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atomic(
            fid, "notifications.channels", "channel_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # --- actions ---
    for row in [
        ("notifications.actions.buttons", "动作按钮", "Action Buttons",
         "在通知上添加可点击动作按钮。",
         ["addAction、UNNotificationAction"],
         ["notifications.actions.reply"],
         merge_bindings(
             A("NotificationCompat.Action",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.Action"),
             I("UNNotificationAction",
               "https://developer.apple.com/documentation/usernotifications/unnotificationaction", "class"),
             H("NotificationAction",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationactionbutton"),
         )),
        ("notifications.actions.reply", "直接回复", "Inline Reply",
         "在通知界面直接输入文本回复。",
         ["RemoteInput、UNTextInputNotificationAction"],
         ["notifications.actions.buttons"],
         merge_bindings(
             A("RemoteInput",
               "https://developer.android.com/reference/android/app/RemoteInput"),
             I("UNTextInputNotificationAction",
               "https://developer.apple.com/documentation/usernotifications/untextinputnotificationaction", "class"),
             pending("harmonyos"),
         )),
        ("notifications.actions.dismiss", "滑动消除处理", "Dismiss Handling",
         "监听或响应用户清除/滑动消除通知。",
         ["DELETE_INTENT、dismissed"],
         ["notifications.local.cancel"],
         merge_bindings(
             A("NotificationCompat.Builder.setDeleteIntent",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setDeleteIntent(android.app.PendingIntent)"),
             I("UNNotificationDismissActionIdentifier",
               "https://developer.apple.com/documentation/usernotifications/unnotificationdismissactionidentifier", "property"),
             pending("harmonyos"),
         )),
        ("notifications.actions.category", "动作分类注册", "Action Category",
         "注册可复用的通知动作分类。",
         ["UNNotificationCategory、setNotificationCategories"],
         ["notifications.actions.buttons"],
         merge_bindings(
             pending("android", "渠道+Action 组合，无独立 Category API"),
             I("setNotificationCategories",
               "https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649517-setnotificationcategories", "method"),
             pending("harmonyos"),
         )),
        ("notifications.actions.background_handler", "后台动作处理", "Background Action Handler",
         "在后台处理通知动作回调而不必前台拉起。",
         ["BroadcastReceiver、UNNotificationResponse"],
         ["notifications.actions.buttons"],
         merge_bindings(
             A("BroadcastReceiver",
               "https://developer.android.com/reference/android/content/BroadcastReceiver"),
             I("didReceive",
               "https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate/1649501-usernotificationcenter", "method"),
             pending("harmonyos"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atomic(
            fid, "notifications.actions", "action_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # --- badges ---
    for row in [
        ("notifications.badges.set", "设置角标数", "Set Badge Count",
         "设置应用图标角标显示数量。",
         ["setNumber、badgeCount、setBadgeNumber"],
         ["notifications.badges.clear"],
         merge_bindings(
             A("NotificationCompat.Builder.setNumber",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setNumber(int)"),
             I("badgeCount",
               "https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1648816-setbadgecount", "method"),
             H("setBadgeNumber",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
         )),
        ("notifications.badges.clear", "清除角标", "Clear Badge",
         "将角标清零或移除。",
         ["badgeCount 0"],
         ["notifications.badges.set"],
         merge_bindings(
             A("ShortcutBadger / Notification number",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setNumber(int)", "guide"),
             I("setBadgeCount",
               "https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1648816-setbadgecount", "method"),
             H("setBadgeNumber",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
         )),
        ("notifications.badges.query", "角标能力查询", "Badge Capability Query",
         "查询系统是否支持桌面角标。",
         ["areNotificationsEnabled 关联、桌面角标能力"],
         ["notifications.badges.set"],
         merge_bindings(
             pending("android", "OEM 角标能力差异，待核统一 API"),
             I("authorizationStatus",
               "https://developer.apple.com/documentation/usernotifications/unnotificationsettings/1648392-authorizationstatus", "property"),
             H("isBadgeNumberEnabled",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
         )),
        ("notifications.badges.auto_update", "角标与未读同步", "Badge Unread Sync",
         "按未读数自动同步角标。",
         ["未读计数驱动角标"],
         ["notifications.badges.set"],
         merge_bindings(
             A("NotificationManager",
               "https://developer.android.com/reference/android/app/NotificationManager"),
             I("setBadgeCount",
               "https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1648816-setbadgecount", "method"),
             H("setBadgeNumber",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atomic(
            fid, "notifications.badges", "badge_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # --- live activities / ongoing ---
    for row in [
        ("notifications.live_activities.start", "启动实时活动", "Start Live Activity",
         "启动实时活动/实况窗会话。",
         ["ActivityKit request、liveView"],
         ["notifications.live_activities.update"],
         merge_bindings(
             A("NotificationCompat.Builder.setOngoing",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setOngoing(boolean)"),
             I("ActivityKit", "https://developer.apple.com/documentation/activitykit", "framework"),
             H("Live View",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/live-view-kit", "guide"),
         )),
        ("notifications.live_activities.update", "更新实时活动", "Update Live Activity",
         "更新已启动实时活动的展示内容。",
         ["Activity.update、push update"],
         ["notifications.live_activities.end"],
         merge_bindings(
             A("NotificationManager.notify",
               "https://developer.android.com/reference/android/app/NotificationManager#notify(int,%20android.app.Notification)"),
             I("Activity.update",
               "https://developer.apple.com/documentation/activitykit/activity/update(_:)", "method"),
             H("Live View update",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/live-view-kit", "guide"),
         )),
        ("notifications.live_activities.end", "结束实时活动", "End Live Activity",
         "结束实时活动并决定最终状态展示。",
         ["Activity.end"],
         ["notifications.live_activities.start"],
         merge_bindings(
             A("NotificationManager.cancel",
               "https://developer.android.com/reference/android/app/NotificationManager#cancel(int)"),
             I("Activity.end",
               "https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:)", "method"),
             H("Live View end",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/live-view-kit", "guide"),
         )),
        ("notifications.live_activities.push_update", "推送更新实时活动", "Push Update Live Activity",
         "通过远程推送更新实时活动内容。",
         ["push-to-start / update token"],
         ["notifications.live_activities.update"],
         merge_bindings(
             pending("android"),
             I("Updating Live Activities with ActivityKit push",
               "https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications", "guide"),
             H("实况窗推送",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/live-view-kit", "guide"),
         )),
        ("notifications.live_activities.ongoing", "持续前台服务通知", "Ongoing Service Notification",
         "与前台服务绑定的不可轻易滑掉的持续通知。",
         ["startForeground、ongoing"],
         ["notifications.live_activities.start"],
         merge_bindings(
             A("Service.startForeground",
               "https://developer.android.com/reference/android/app/Service#startForeground(int,%20android.app.Notification)"),
             pending("ios", "BGTask/Live Activity 替代路径待核"),
             H("continuousTask",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/continuous-task", "guide"),
         )),
        ("notifications.live_activities.progress_ui", "实时进度展示", "Live Progress UI",
         "在实时活动/ongoing 中展示阶段进度。",
         ["progress content state"],
         ["notifications.local.progress"],
         merge_bindings(
             A("NotificationCompat.Builder.setProgress",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setProgress(int,%20int,%20boolean)"),
             I("ActivityContentState",
               "https://developer.apple.com/documentation/activitykit", "framework"),
             H("Live View",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/live-view-kit", "guide"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atomic(
            fid, "notifications.live_activities", "live_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # --- dnd ---
    for row in [
        ("notifications.dnd.status", "勿扰状态查询", "DND Status",
         "查询系统勿扰/专注模式是否启用。",
         ["NotificationManager.getCurrentInterruptionFilter、FocusStatus"],
         ["notifications.dnd.policy"],
         merge_bindings(
             A("NotificationManager.getCurrentInterruptionFilter",
               "https://developer.android.com/reference/android/app/NotificationManager#getCurrentInterruptionFilter()"),
             I("FocusStatus", "https://developer.apple.com/documentation/intents/focusstatus", "class"),
             pending("harmonyos"),
         )),
        ("notifications.dnd.policy", "勿扰策略感知", "DND Policy",
         "感知允许告警类别等勿扰策略摘要。",
         ["NotificationManager.Policy"],
         ["notifications.dnd.status"],
         merge_bindings(
             A("NotificationManager.Policy",
               "https://developer.android.com/reference/android/app/NotificationManager.Policy"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("notifications.dnd.time_sensitive", "时效性通知", "Time Sensitive",
         "声明时效性以在专注模式下仍可能送达。",
         ["TIME_SENSITIVE、interruptionLevel.timeSensitive"],
         ["notifications.channels.importance"],
         merge_bindings(
             A("NotificationCompat.CATEGORY_REMINDER",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat#CATEGORY_REMINDER"),
             I("timeSensitive",
               "https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive", "case"),
             pending("harmonyos"),
         )),
        ("notifications.dnd.bypass", "关键告警放行", "Critical Alert Bypass",
         "关键/紧急告警在勿扰下的放行能力。",
         ["ACCESS_NOTIFICATION_POLICY、criticalAlert"],
         ["notifications.dnd.time_sensitive"],
         merge_bindings(
             A("NotificationManager.INTERRUPTION_FILTER_PRIORITY",
               "https://developer.android.com/reference/android/app/NotificationManager#INTERRUPTION_FILTER_PRIORITY"),
             I("criticalAlert",
               "https://developer.apple.com/documentation/usernotifications/unauthorizationoptions/1648840-criticalalert", "property"),
             pending("harmonyos"),
         )),
        ("notifications.dnd.settings_intent", "跳转勿扰设置", "Open DND Settings",
         "引导用户打开系统勿扰/通知设置。",
         ["ACTION_NOTIFICATION_POLICY_ACCESS_SETTINGS"],
         ["notifications.dnd.status"],
         merge_bindings(
             A("Settings.ACTION_NOTIFICATION_POLICY_ACCESS_SETTINGS",
               "https://developer.android.com/reference/android/provider/Settings#ACTION_NOTIFICATION_POLICY_ACCESS_SETTINGS"),
             I("openSettingsURLString",
               "https://developer.apple.com/documentation/uikit/uiapplication/1623042-opensettingsurlstring", "property"),
             pending("harmonyos"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atomic(
            fid, "notifications.dnd", "dnd_capability",
            zh, en, definition, includes, excludes, bindings,
            privacy="runtime_permission",
        ))

    # extension / listener extras under actions? add as L2 siblings? User didn't list.
    # Add bubbles/toast under local as extra atomics already enough.
    # Add notification listener / content extension under a small L3? Keep within count.
    # Extra: bubbles, heads-up, content extension as atomics under local would widen too much.
    # Put under live_activities or actions — add extension group as L3 under local via more atomics:

    # Move extension/listener under dedicated L3 branches to avoid ultra-wide local siblings.
    f.append(feature(
        "notifications.local.extension", parent="notifications.local", level="L3",
        zh="通知扩展形态", en="Notification Extensions",
        definition="气泡、内容扩展与通知监听等扩展形态。",
        includes=["气泡、内容扩展、监听服务"],
        excludes=["基础展示见 notifications.local.display"],
        sibling_axis="local_capability",
        bindings=merge_bindings(
            A("NotificationCompat",
              "https://developer.android.com/reference/androidx/core/app/NotificationCompat"),
            I("UserNotificationsUI",
              "https://developer.apple.com/documentation/usernotificationsui", "framework"),
            H("@ohos.notificationManager",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
        ),
    ))
    for row in [
        ("notifications.local.extension.bubbles", "气泡通知", "Notification Bubbles",
         "将对话类通知以气泡形式浮层展示。",
         ["BubbleMetadata"],
         ["notifications.local.display"],
         merge_bindings(
             A("NotificationCompat.BubbleMetadata",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.BubbleMetadata"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("notifications.local.extension.content", "通知内容扩展", "Content Extension",
         "自定义通知详情展开界面。",
         ["UNNotificationContentExtension、DecoratedCustomViewStyle"],
         ["notifications.local.styles"],
         merge_bindings(
             A("NotificationCompat.DecoratedCustomViewStyle",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.DecoratedCustomViewStyle"),
             I("UNNotificationContentExtension",
               "https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension", "protocol"),
             pending("harmonyos"),
         )),
        ("notifications.local.extension.listener", "通知监听服务", "Notification Listener",
         "读取/管理其他应用通知的监听服务（需用户授权）。",
         ["NotificationListenerService"],
         ["notifications.local.display"],
         merge_bindings(
             A("NotificationListenerService",
               "https://developer.android.com/reference/android/service/notification/NotificationListenerService"),
             pending("ios", "无等价第三方通知读取 API"),
             pending("harmonyos"),
         )),
        ("notifications.local.extension.service", "通知服务扩展", "Service Extension",
         "在通知送达前修改内容的服务扩展。",
         ["UNNotificationServiceExtension"],
         ["notifications.local.extension.content"],
         merge_bindings(
             pending("android"),
             I("UNNotificationServiceExtension",
               "https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension", "class"),
             pending("harmonyos"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(feature(
            fid, parent="notifications.local.extension", level="L4",
            zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="local_extension_kind",
            granularity="atomic", bindings=bindings,
            privacy_class="runtime_permission" if "listener" in fid else "none",
        ))

    # Extra coverage under thinner L2s
    for row in [
        ("notifications.push.aaid", "应用匿名推送标识", "App Anonymous Push ID",
         "获取推送通道侧应用匿名标识。",
         ["AAID / installation id"],
         ["notifications.push.token"],
         merge_bindings(
             pending("android", "FCM/实例 ID 已迁移，待核现行入口"),
             pending("ios"),
             H("getAAID",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-getaaid"),
         ), "notifications.push", "push_capability"),
        ("notifications.push.topic", "主题订阅推送", "Topic Subscribe Push",
         "按主题订阅/退订远程推送。",
         ["subscribeToTopic"],
         ["notifications.push.token"],
         merge_bindings(
             A("FirebaseMessaging.subscribeToTopic",
               "https://firebase.google.com/docs/cloud-messaging/android/topic-messaging"),
             pending("ios"),
             H("subscribeToTopic",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-topic", "guide"),
         ), "notifications.push", "push_capability"),
        ("notifications.channels.conversation", "会话渠道", "Conversation Channel",
         "为会话/人脉类通知配置专用渠道属性。",
         ["setConversationId"],
         ["notifications.channels.create"],
         merge_bindings(
             A("NotificationChannel.setConversationId",
               "https://developer.android.com/reference/android/app/NotificationChannel#setConversationId(java.lang.String,%20java.lang.String)"),
             I("UNNotificationCategory",
               "https://developer.apple.com/documentation/usernotifications/unnotificationcategory", "class"),
             pending("harmonyos"),
         ), "notifications.channels", "channel_capability"),
        ("notifications.actions.semantic", "语义动作类型", "Semantic Action",
         "声明动作的语义类型（回复/归档等）。",
         ["setSemanticAction、UNNotificationActionOptions"],
         ["notifications.actions.buttons"],
         merge_bindings(
             A("NotificationCompat.Action.Builder.setSemanticAction",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.Action.Builder#setSemanticAction(int)"),
             I("UNNotificationActionOptions",
               "https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions", "struct"),
             pending("harmonyos"),
         ), "notifications.actions", "action_capability"),
        ("notifications.badges.launcher", "启动器角标同步", "Launcher Badge Sync",
         "与桌面启动器角标机制同步未读数。",
         ["ShortcutBadger 类能力 / setBadgeNumber"],
         ["notifications.badges.set"],
         merge_bindings(
             A("NotificationCompat.Builder.setNumber",
               "https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setNumber(int)"),
             I("setBadgeCount",
               "https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1648816-setbadgecount", "method"),
             H("setBadgeNumber",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager"),
         ), "notifications.badges", "badge_capability"),
        ("notifications.live_activities.relevance", "实时活动相关分", "Live Activity Relevance",
         "设置实时活动相关性分数以影响展示优先级。",
         ["relevanceScore"],
         ["notifications.live_activities.update"],
         merge_bindings(
             pending("android"),
             I("relevanceScore",
               "https://developer.apple.com/documentation/activitykit/activitycontent", "class"),
             pending("harmonyos"),
         ), "notifications.live_activities", "live_capability"),
        ("notifications.dnd.access_request", "勿扰策略访问授权", "DND Policy Access",
         "请求访问系统通知策略（勿扰）的授权。",
         ["ACTION_NOTIFICATION_POLICY_ACCESS_SETTINGS"],
         ["notifications.dnd.policy"],
         merge_bindings(
             A("NotificationManager.isNotificationPolicyAccessGranted",
               "https://developer.android.com/reference/android/app/NotificationManager#isNotificationPolicyAccessGranted()"),
             pending("ios"),
             pending("harmonyos"),
         ), "notifications.dnd", "dnd_capability"),
        ("notifications.dnd.conversation_priority", "会话优先放行", "Priority Conversations",
         "在勿扰下允许优先会话通知。",
         ["PRIORITY_CATEGORY_CONVERSATIONS"],
         ["notifications.dnd.policy"],
         merge_bindings(
             A("NotificationManager.Policy.PRIORITY_CATEGORY_CONVERSATIONS",
               "https://developer.android.com/reference/android/app/NotificationManager.Policy#PRIORITY_CATEGORY_CONVERSATIONS"),
             I("FocusStatus",
               "https://developer.apple.com/documentation/intents/focusstatus", "class"),
             pending("harmonyos"),
         ), "notifications.dnd", "dnd_capability"),
    ]:
        fid, zh, en, definition, includes, excludes, bindings, parent, axis = row
        f.append(atomic(
            fid, parent, axis, zh, en, definition, includes, excludes, bindings,
            privacy="runtime_permission" if "dnd" in fid or "push" in fid else "none",
        ))

    dedup = {n["id"]: n for n in f}
    return list(dedup.values())


def main():
    nodes = build()
    path = write_domain("notifications", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
