#!/usr/bin/env python3
"""Author the telecom domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "telecom_capability_family"


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
        "telecom", parent=None, level="L1",
        zh="通信与内容", en="Telecom and Personal Content",
        definition="通话、短信、联系人、日历与邮件撰写等个人通信内容能力。",
        includes=['通话、短信、联系人、日历、邮件'],
        excludes=['蜂窝数据链路见 network', '推送见 notifications'],
        legacy={'disposition': 'kept', 'sources': ['telecom']},
    ))
    l2 = [
        ('telecom.phone', '通话', 'Phone Calls', '拨号、通话状态、系统通话与 VoIP 接入。', ['拨号、状态、筛选、VoIP'], ['短信见 sms'], ['telecom.phone']),
        ('telecom.sms', '短信彩信', 'SMS and MMS', '短信发送、过滤与相关消息能力。', ['发送、过滤、RCS/卫星入口'], ['通话见 phone'], ['telecom.sms']),
        ('telecom.contacts', '联系人', 'Contacts', '联系人读写、选择器与名片交换。', ['读写、选择器、vCard'], ['通话记录见 phone'], ['telecom.contacts']),
        ('telecom.calendar', '日历', 'Calendar', '日历账户、日程与提醒。', ['账户、日程、提醒'], ['系统闹钟见 device'], ['telecom.calendar']),
        ('telecom.mail', '邮件撰写', 'Mail Compose', '系统邮件撰写与发送入口。', ['mailto、撰写界面'], ['通用分享见 interop'], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="telecom", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- telecom.phone ---
    leaf(f, "telecom.phone.dial", "telecom.phone", "phone_operation", "拉起拨号", "Place Call Dial",
         "发起或拉起系统拨号。", ['ACTION_DIAL / tel:'], ['通话状态见 state'],
         B(('TelecomManager', 'https://developer.android.com/reference/android/telecom/TelecomManager'), ('CallKit / tel URL', 'https://developer.apple.com/documentation/callkit', 'framework'), ('call', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-call')), {'disposition': 'kept', 'sources': ['telecom.phone.dial']}, level="L3", privacy="runtime_permission")
    leaf(f, "telecom.phone.state", "telecom.phone", "phone_operation", "通话状态监听", "Call State Listen",
         "监听来电、摘机与空闲等状态。", ['TelephonyCallback / CXCallObserver'], ['拨号见 dial'],
         B(('TelephonyCallback', 'https://developer.android.com/reference/android/telephony/TelephonyCallback'), ('CXCallObserver', 'https://developer.apple.com/documentation/callkit/cxcallobserver', 'class'), ('call', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-call')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "telecom.phone.screening", "telecom.phone", "phone_operation", "来电筛选", "Call Screening",
         "实现来电筛选与拦截。", ['CallScreeningService'], ['状态见 state'],
         B(('CallScreeningService', 'https://developer.android.com/reference/android/telecom/CallScreeningService'), ('Call Directory', 'https://developer.apple.com/documentation/callkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "telecom.phone.voip", "telecom.phone", "phone_operation", "VoIP通话接入", "VoIP Call Integration",
         "将 VoIP 通话接入系统通话界面。", ['ConnectionService / CallKit'], ['蜂窝拨号见 dial'],
         B(('ConnectionService', 'https://developer.android.com/reference/android/telecom/ConnectionService'), ('CallKit', 'https://developer.apple.com/documentation/callkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "telecom.phone.incall_ui", "telecom.phone", "phone_operation", "通话中界面", "In-Call UI",
         "提供或定制通话中界面。", ['InCallService'], ['VoIP 见 voip'],
         B(('InCallService', 'https://developer.android.com/reference/android/telecom/InCallService'), ('CallKit UI', 'https://developer.apple.com/documentation/callkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.phone.emergency", "telecom.phone", "phone_operation", "紧急号码识别", "Emergency Number Detect",
         "识别紧急号码并走紧急呼叫路径。", ['isEmergencyNumber'], ['拨号见 dial'],
         B(('TelephonyManager.isEmergencyNumber', 'https://developer.android.com/reference/android/telephony/TelephonyManager'), None, ('call', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-call')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.phone.audio_route", "telecom.phone", "phone_operation", "通话音频路由", "Call Audio Route",
         "切换听筒/扬声器/蓝牙等通话音频路由。", ['call audio route'], ['媒体路由见 device'],
         B(('CallAudioState', 'https://developer.android.com/reference/android/telecom/CallAudioState'), ('AVAudioSession', 'https://developer.apple.com/documentation/avfaudio/avaudiosession', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.phone.rtt_video", "telecom.phone", "phone_operation", "RTT与视频通话", "RTT and Video Call",
         "实时文本与运营商视频通话能力入口。", ['RTT / video call'], ['VoIP 见 voip'],
         B(('Connection RTT', 'https://developer.android.com/reference/android/telecom/Connection'), ('CallKit', 'https://developer.apple.com/documentation/callkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- telecom.sms ---
    leaf(f, "telecom.sms.send", "telecom.sms", "sms_operation", "短信发送", "SMS Send",
         "发送短信或彩信。", ['SmsManager'], ['过滤见 filter'],
         B(('SmsManager', 'https://developer.android.com/reference/android/telephony/SmsManager'), ('MFMessageComposeViewController', 'https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller', 'class'), ('sms', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-telephony-sms')), {'disposition': 'kept', 'sources': ['telecom.sms.send']}, level="L3", privacy="runtime_permission")
    leaf(f, "telecom.sms.compose_ui", "telecom.sms", "sms_operation", "短信撰写界面", "SMS Compose UI",
         "拉起系统短信撰写界面。", ['sms: / MFMessageCompose'], ['直接发送见 send'],
         B(('ACTION_SENDTO', 'https://developer.android.com/guide/components/intents-common#Messaging', 'guide'), ('MFMessageComposeViewController', 'https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.sms.filter", "telecom.sms", "sms_operation", "短信过滤", "SMS Filtering",
         "实现短信过滤扩展。", ['SMS filter extension'], ['发送见 send'],
         B(None, ('IdentityLookup', 'https://developer.apple.com/documentation/identitylookup', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.sms.receive", "telecom.sms", "sms_operation", "短信接收", "SMS Receive",
         "接收短信广播或回调。", ['SMS_RECEIVED'], ['过滤见 filter'],
         B(('SMS_RECEIVED_ACTION', 'https://developer.android.com/reference/android/provider/Telephony.Sms.Intents', 'class'), None, ('sms', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-telephony-sms')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "telecom.sms.rcs", "telecom.sms", "sms_operation", "富通信入口", "RCS Messaging Entry",
         "RCS 富通信能力入口。", ['RCS'], ['短信见 send'],
         B(('RcsUceAdapter', 'https://developer.android.com/reference/android/telephony/ims/RcsUceAdapter'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.sms.satellite", "telecom.sms", "sms_operation", "卫星消息入口", "Satellite Messaging Entry",
         "卫星短信/消息能力入口。", ['satellite SMS'], ['普通短信见 send'],
         B(('SatelliteManager', 'https://developer.android.com/reference/android/telephony/satellite/SatelliteManager'), ('Emergency SOS via satellite', 'https://developer.apple.com/documentation/', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.sms.voicemail", "telecom.sms", "sms_operation", "语音信箱", "Visual Voicemail",
         "访问视觉语音信箱。", ['VoicemailContract'], ['通话见 phone'],
         B(('VoicemailContract', 'https://developer.android.com/reference/android/provider/VoicemailContract'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")

    # --- telecom.contacts ---
    leaf(f, "telecom.contacts.read", "telecom.contacts", "contacts_operation", "联系人读取", "Contacts Read",
         "查询联系人与原始数据。", ['ContactsContract / CNContactStore'], ['写入见 write'],
         B(('ContactsContract', 'https://developer.android.com/reference/android/provider/ContactsContract'), ('CNContactStore', 'https://developer.apple.com/documentation/contacts/cncontactstore', 'class'), ('contact', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-contact')), {'disposition': 'kept', 'sources': ['telecom.contacts.read']}, level="L3", privacy="runtime_permission")
    leaf(f, "telecom.contacts.write", "telecom.contacts", "contacts_operation", "联系人写入", "Contacts Write",
         "创建、更新与删除联系人。", ['insert/update/delete'], ['读取见 read'],
         B(('ContactsContract', 'https://developer.android.com/reference/android/provider/ContactsContract'), ('CNContactStore', 'https://developer.apple.com/documentation/contacts/cncontactstore', 'class'), ('contact', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-contact')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "telecom.contacts.picker", "telecom.contacts", "contacts_operation", "联系人选择器", "Contacts Picker",
         "拉起系统联系人选择界面。", ['ACTION_PICK / CNContactPicker'], ['读取见 read'],
         B(('ACTION_PICK', 'https://developer.android.com/guide/components/intents-common#Contacts', 'guide'), ('CNContactPickerViewController', 'https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller', 'class'), ('contact', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-contact')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.contacts.vcard", "telecom.contacts", "contacts_operation", "vCard导入导出", "vCard Import Export",
         "导入导出 vCard 名片。", ['vCard'], ['写入见 write'],
         B(('ImportVCardActivity hooks', 'https://developer.android.com/guide/topics/providers/contacts-provider', 'guide'), ('CNContactVCardSerialization', 'https://developer.apple.com/documentation/contacts', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.contacts.accounts", "telecom.contacts", "contacts_operation", "联系人账户源", "Contacts Account Sources",
         "管理联系人同步账户源。", ['RawContacts account'], ['读写见 read/write'],
         B(('ContactsContract.Settings', 'https://developer.android.com/reference/android/provider/ContactsContract.Settings'), ('CNContainer', 'https://developer.apple.com/documentation/contacts/cncontainer', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.contacts.quick_access", "telecom.contacts", "contacts_operation", "联系人快捷访问按钮", "Contacts Quick Access",
         "系统级联系人快捷访问入口。", ['access button'], ['选择器见 picker'],
         B(None, ('CNContactViewController', 'https://developer.apple.com/documentation/contactsui', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- telecom.calendar ---
    leaf(f, "telecom.calendar.events", "telecom.calendar", "calendar_operation", "日程读写", "Calendar Events CRUD",
         "创建、查询、更新与删除日程。", ['CalendarContract / EventKit'], ['提醒见 reminders'],
         B(('CalendarContract', 'https://developer.android.com/reference/android/provider/CalendarContract'), ('EventKit', 'https://developer.apple.com/documentation/eventkit', 'framework'), ('calendarManager', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-calendarManager')), {'disposition': 'kept', 'sources': ['telecom.calendar.events']}, level="L3", privacy="runtime_permission")
    leaf(f, "telecom.calendar.accounts", "telecom.calendar", "calendar_operation", "日历账户", "Calendar Accounts",
         "枚举与管理日历账户。", ['calendars / EKSource'], ['日程见 events'],
         B(('CalendarContract.Calendars', 'https://developer.android.com/reference/android/provider/CalendarContract.Calendars'), ('EKSource', 'https://developer.apple.com/documentation/eventkit/eksource', 'class'), ('calendarManager', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-calendarManager')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.calendar.reminders", "telecom.calendar", "calendar_operation", "日程提醒", "Event Reminders",
         "为日程设置提醒。", ['Reminders / EKAlarm'], ['日程见 events'],
         B(('CalendarContract.Reminders', 'https://developer.android.com/reference/android/provider/CalendarContract.Reminders'), ('EKAlarm', 'https://developer.apple.com/documentation/eventkit/ekalarm', 'class'), ('calendarManager', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-calendarManager')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.calendar.event_ui", "telecom.calendar", "calendar_operation", "日程系统界面", "Calendar Event UI",
         "拉起系统日程创建/编辑界面。", ['INTENT insert / EKEventEdit'], ['API 读写见 events'],
         B(('Intent INSERT', 'https://developer.android.com/guide/components/intents-common#Calendar', 'guide'), ('EKEventEditViewController', 'https://developer.apple.com/documentation/eventkitui', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.calendar.attendees", "telecom.calendar", "calendar_operation", "日程参与者", "Event Attendees",
         "管理日程参与者与响应状态。", ['Attendees'], ['日程见 events'],
         B(('CalendarContract.Attendees', 'https://developer.android.com/reference/android/provider/CalendarContract.Attendees'), ('EKParticipant', 'https://developer.apple.com/documentation/eventkit/ekparticipant', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.calendar.availability", "telecom.calendar", "calendar_operation", "忙闲查询", "Freebusy Availability",
         "查询日历忙闲状态。", ['freebusy'], ['日程见 events'],
         B(None, ('EKEventStore', 'https://developer.apple.com/documentation/eventkit/ekeventstore', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- telecom.mail ---
    leaf(f, "telecom.mail.compose", "telecom.mail", "mail_operation", "邮件撰写发送", "Mail Compose Send",
         "拉起系统邮件撰写并发送。", ['mailto: / MFMailCompose'], ['通用分享见 interop'],
         B(('ACTION_SENDTO mailto', 'https://developer.android.com/guide/components/intents-common#Email', 'guide'), ('MFMailComposeViewController', 'https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.mail.attachments", "telecom.mail", "mail_operation", "邮件附件", "Mail Attachments",
         "在系统邮件撰写中添加附件。", ['addAttachment'], ['撰写见 compose'],
         B(('Intent EXTRA_STREAM', 'https://developer.android.com/guide/components/intents-common#Email', 'guide'), ('MFMailComposeViewController addAttachmentData', 'https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.mail.accounts_query", "telecom.mail", "mail_operation", "邮件账户可用性", "Mail Account Availability",
         "查询设备是否可发送邮件。", ['canSendMail'], ['撰写见 compose'],
         B(None, ('MFMailComposeViewController.canSendMail', 'https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "telecom.mail.mailto_parse", "telecom.mail", "mail_operation", "mailto链接处理", "Mailto Link Handling",
         "解析并处理 mailto 链接。", ['mailto parse'], ['撰写见 compose'],
         B(('Intent.parseUri', 'https://developer.android.com/reference/android/content/Intent'), ('mailto', 'https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/MailLinks/MailLinks.html', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")


    leaf(f, "telecom.phone.conference", "telecom.phone", "phone_operation", "电话会议", "Conference Calls",
         "合并通话形成会议。", ["conference"], ["状态见 state"],
         B(("Connection.conference", "https://developer.android.com/reference/android/telecom/Connection"),
           ("CallKit", "https://developer.apple.com/documentation/callkit", "framework"), None), privacy="runtime_permission")
    leaf(f, "telecom.phone.caller_id", "telecom.phone", "phone_operation", "来电显示增强", "Caller ID Enrichment",
         "提供来电号码识别与企业来电信息。", ["caller ID"], ["筛选见 screening"],
         B(("CallScreeningService", "https://developer.android.com/reference/android/telecom/CallScreeningService"),
           ("Call Directory Extension", "https://developer.apple.com/documentation/callkit", "framework"), None), privacy="runtime_permission")
    leaf(f, "telecom.sms.delivery_report", "telecom.sms", "sms_operation", "短信送达报告", "SMS Delivery Report",
         "接收短信送达状态报告。", ["delivery report"], ["发送见 send"],
         B(("SmsManager", "https://developer.android.com/reference/android/telephony/SmsManager"), None,
           ("sms", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-telephony-sms")), privacy="runtime_permission")
    leaf(f, "telecom.contacts.aggregation", "telecom.contacts", "contacts_operation", "联系人聚合", "Contacts Aggregation",
         "聚合同一人的多账户联系人数据。", ["aggregation"], ["读取见 read"],
         B(("ContactsContract.AggregationSuggestions", "https://developer.android.com/reference/android/provider/ContactsContract"),
           ("CNContact", "https://developer.apple.com/documentation/contacts/cncontact", "class"), None))
    leaf(f, "telecom.calendar.recurrence", "telecom.calendar", "calendar_operation", "重复日程规则", "Recurrence Rules",
         "设置与解析重复日程规则。", ["RRULE"], ["日程见 events"],
         B(("CalendarContract.Events", "https://developer.android.com/reference/android/provider/CalendarContract.Events"),
           ("EKRecurrenceRule", "https://developer.apple.com/documentation/eventkit/ekrecurrencerule", "class"),
           ("calendarManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-calendarManager")))
    leaf(f, "telecom.mail.recipients", "telecom.mail", "mail_operation", "收件人字段", "Mail Recipients",
         "设置收件/抄送/密送收件人。", ["to/cc/bcc"], ["撰写见 compose"],
         B(("Intent EXTRA_EMAIL", "https://developer.android.com/guide/components/intents-common#Email", "guide"),
           ("MFMailComposeViewController", "https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller", "class"), None))
    leaf(f, "telecom.mail.subject_body", "telecom.mail", "mail_operation", "主题与正文预填", "Subject Body Prefill",
         "预填邮件主题与正文。", ["subject/body"], ["撰写见 compose"],
         B(("Intent EXTRA_SUBJECT", "https://developer.android.com/guide/components/intents-common#Email", "guide"),
           ("MFMailComposeViewController", "https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller", "class"), None))

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("telecom", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
