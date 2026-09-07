#!/usr/bin/env python3
"""Author the enterprise domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "enterprise_capability_family"


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
        "enterprise", parent=None, level="L1",
        zh="企业与管理", en="Enterprise and Management",
        definition="设备管理、工作资料、设备策略与企业身份接入；不含消费级家长控制。",
        includes=['MDM、工作资料、设备策略、企业身份'],
        excludes=['家长控制见 digital_wellbeing', '消费账号见 identity'],
        legacy={'disposition': 'kept', 'sources': ['enterprise']},
    ))
    l2 = [
        ('enterprise.mdm', '移动设备管理', 'Mobile Device Management', '企业设备注册、策略通道与远程管理入口。', ['注册、策略通道、远程操作'], ['工作资料隔离见 work_profile'], ['enterprise.mdm']),
        ('enterprise.work_profile', '工作资料', 'Work Profile', '工作资料创建、隔离与跨资料互操作。', ['配置、隔离、跨资料'], ['整机 MDM 见 mdm'], ['enterprise.work_profile']),
        ('enterprise.device_policy', '设备策略控制', 'Device Policy Controls', '密码、限制、证书、擦除等设备策略能力。', ['密码、限制、证书、擦除'], ['工作资料生命周期见 work_profile'], []),
        ('enterprise.identity_enterprise', '企业身份接入', 'Enterprise Identity', '企业单点登录、Kerberos 与学校/企业管理器身份。', ['SSO、Kerberos、学校管理器'], ['消费联合登录见 identity'], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="enterprise", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- enterprise.mdm ---
    leaf(f, "enterprise.mdm.policy", "enterprise.mdm", "mdm_operation", "MDM策略下发", "MDM Policy Delivery",
         "通过设备管理通道下发与查询策略。", ['DevicePolicyManager / MDM'], ['具体限制项见 device_policy'],
         B(('DevicePolicyManager', 'https://developer.android.com/reference/android/app/admin/DevicePolicyManager'), ('DeviceManagement', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), ('MDM Kit', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro')), {'disposition': 'kept', 'sources': ['enterprise.mdm.policy']}, level="L3", privacy="none")
    leaf(f, "enterprise.mdm.enrollment", "enterprise.mdm", "mdm_operation", "设备企业注册", "Enterprise Enrollment",
         "将设备注册到企业管理。", ['enrollment'], ['策略见 policy'],
         B(('Device Policy Controller', 'https://developer.android.com/work/dpc/build-dpc', 'guide'), ('Device Enrollment', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), ('MDM enrollment', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.mdm.remote_wipe", "enterprise.mdm", "mdm_operation", "远程锁定与擦除", "Remote Lock and Wipe",
         "远程锁定或擦除托管设备。", ['lock/wipe'], ['策略见 policy'],
         B(('DevicePolicyManager.wipeData', 'https://developer.android.com/reference/android/app/admin/DevicePolicyManager'), ('DeviceManagement erase', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), ('MDM wipe', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.mdm.app_distribution", "enterprise.mdm", "mdm_operation", "企业应用分发", "Enterprise App Distribution",
         "向托管设备分发企业应用。", ['managed Google Play / VPP'], ['安装管控见 device_policy'],
         B(('Managed Google Play', 'https://developer.android.com/work/play/emm-api', 'guide'), ('Apps and Books', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.mdm.compliance", "enterprise.mdm", "mdm_operation", "合规状态上报", "Compliance Status Reporting",
         "上报设备合规状态给管理端。", ['compliance'], ['策略见 policy'],
         B(('DevicePolicyManager', 'https://developer.android.com/reference/android/app/admin/DevicePolicyManager'), ('DeviceManagement', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), ('MDM', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.mdm.financed_device", "enterprise.mdm", "mdm_operation", "融资设备管控", "Financed Device Controls",
         "融资设备专用管控能力入口。", ['financed device'], ['通用注册见 enrollment'],
         B(('FinancedDevice', 'https://developer.android.com/work/dpc/build-dpc', 'guide'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- enterprise.work_profile ---
    leaf(f, "enterprise.work_profile.isolation", "enterprise.work_profile", "work_profile_operation", "工作资料隔离", "Work Profile Isolation",
         "工作与个人资料数据与进程隔离。", ['work profile isolation'], ['跨资料互操作见 cross_profile'],
         B(('Work profiles', 'https://developer.android.com/work/versions', 'guide'), None, None), {'disposition': 'kept', 'sources': ['enterprise.work_profile.isolation']}, level="L3", privacy="none")
    leaf(f, "enterprise.work_profile.provisioning", "enterprise.work_profile", "work_profile_operation", "工作资料配置", "Work Profile Provisioning",
         "创建并配置工作资料。", ['provisioning'], ['隔离见 isolation'],
         B(('ACTION_PROVISION_MANAGED_PROFILE', 'https://developer.android.com/work/dpc/build-dpc', 'guide'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.work_profile.cross_profile", "enterprise.work_profile", "work_profile_operation", "跨资料互操作", "Cross-Profile Interop",
         "受控的跨工作/个人资料意图与数据共享。", ['cross-profile intents'], ['隔离见 isolation'],
         B(('CrossProfileApps', 'https://developer.android.com/reference/android/content/pm/CrossProfileApps'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.work_profile.cope", "enterprise.work_profile", "work_profile_operation", "公司自备设备模式", "COPE Mode",
         "公司自备设备（COPE）管理模式入口。", ['COPE'], ['纯工作资料见 provisioning'],
         B(('COPE', 'https://developer.android.com/work/versions', 'guide'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.work_profile.policy", "enterprise.work_profile", "work_profile_operation", "工作资料策略", "Work Profile Policy",
         "针对工作资料的专用策略项。", ['profile policy'], ['整机策略见 device_policy'],
         B(('DevicePolicyManager', 'https://developer.android.com/reference/android/app/admin/DevicePolicyManager'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.work_profile.managed_config", "enterprise.work_profile", "work_profile_operation", "应用托管配置", "Managed App Configuration",
         "向托管应用下发托管配置字典。", ['managed configurations'], ['分发见 mdm.app_distribution'],
         B(('ManagedConfigurations', 'https://developer.android.com/work/managed-configurations', 'guide'), ('ManagedAppConfig', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- enterprise.device_policy ---
    leaf(f, "enterprise.device_policy.password", "enterprise.device_policy", "device_policy_operation", "密码与锁屏策略", "Password and Lock Policy",
         "设置密码复杂度与锁屏策略。", ['password quality'], ['擦除见 wipe'],
         B(('setPasswordQuality', 'https://developer.android.com/reference/android/app/admin/DevicePolicyManager'), ('Passcode policy', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), ('MDM password', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.device_policy.restrictions", "enterprise.device_policy", "device_policy_operation", "功能限制策略", "Feature Restriction Policy",
         "限制相机、截屏等设备功能。", ['user restrictions'], ['密码见 password'],
         B(('addUserRestriction', 'https://developer.android.com/reference/android/app/admin/DevicePolicyManager'), ('Restrictions payload', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), ('MDM restrictions', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.device_policy.certificates", "enterprise.device_policy", "device_policy_operation", "企业证书管理", "Enterprise Certificate Management",
         "安装与管理企业证书。", ['install cert'], ['身份 SSO 见 identity_enterprise'],
         B(('installCaCert', 'https://developer.android.com/reference/android/app/admin/DevicePolicyManager'), ('Certificate payload', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), ('MDM cert', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.device_policy.wipe", "enterprise.device_policy", "device_policy_operation", "本地策略擦除", "Local Policy Wipe",
         "按策略触发本地数据擦除。", ['wipeData'], ['远程擦除见 mdm.remote_wipe'],
         B(('wipeData', 'https://developer.android.com/reference/android/app/admin/DevicePolicyManager'), ('EraseDevice', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), ('MDM wipe', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.device_policy.app_restrict", "enterprise.device_policy", "device_policy_operation", "应用安装限制", "App Install Restrictions",
         "限制应用安装、卸载或可用列表。", ['app restrictions'], ['托管配置见 work_profile.managed_config'],
         B(('setPackagesSuspended', 'https://developer.android.com/reference/android/app/admin/DevicePolicyManager'), ('App lock payload', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), ('MDM app', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.device_policy.network_location", "enterprise.device_policy", "device_policy_operation", "网络与定位管控", "Network and Location Policy",
         "管控 VPN/Wi-Fi/定位等网络相关策略。", ['network/location policy'], ['功能限制见 restrictions'],
         B(('setAlwaysOnVpnPackage', 'https://developer.android.com/reference/android/app/admin/DevicePolicyManager'), ('Network payload', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.device_policy.device_admin", "enterprise.device_policy", "device_policy_operation", "设备管理员组件", "Device Admin Component",
         "实现设备管理接收器/管理员组件。", ['DeviceAdminReceiver'], ['策略 API 见 password'],
         B(('DeviceAdminReceiver', 'https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver'), None, ('MDM', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.device_policy.threat_remediation", "enterprise.device_policy", "device_policy_operation", "威胁修复动作", "Threat Remediation Actions",
         "企业威胁防护触发的修复动作入口。", ['threat remediation'], ['通用安全见 security'],
         B(None, ('DeviceManagement', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- enterprise.identity_enterprise ---
    leaf(f, "enterprise.identity_enterprise.sso", "enterprise.identity_enterprise", "identity_enterprise_operation", "企业单点登录", "Enterprise SSO",
         "企业身份提供方单点登录接入。", ['SSO extension'], ['消费登录见 identity'],
         B(('Enterprise SSO', 'https://developer.android.com/work', 'guide'), ('AuthenticationServices SSO', 'https://developer.apple.com/documentation/authenticationservices', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "enterprise.identity_enterprise.kerberos", "enterprise.identity_enterprise", "identity_enterprise_operation", "Kerberos企业认证", "Kerberos Enterprise Auth",
         "GSS/Kerberos 企业认证。", ['GSSAPI / Kerberos'], ['SSO 见 sso'],
         B(None, ('GSS/Kerberos', 'https://developer.apple.com/documentation/gss', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.identity_enterprise.school_manager", "enterprise.identity_enterprise", "identity_enterprise_operation", "学校企业管理器", "School Manager Identity",
         "学校/教育管理器身份与名册接入。", ['ASM / SchoolManager'], ['课堂进度见 education_classkit'],
         B(None, ('Apple School Manager', 'https://developer.apple.com/support/apple-school-manager/', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.identity_enterprise.managed_account", "enterprise.identity_enterprise", "identity_enterprise_operation", "托管企业账号", "Managed Enterprise Account",
         "托管企业账号的添加与状态。", ['managed account'], ['SSO 见 sso'],
         B(('AccountManager', 'https://developer.android.com/reference/android/accounts/AccountManager'), ('Managed Apple ID', 'https://developer.apple.com/documentation/devicemanagement', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.identity_enterprise.acl", "enterprise.identity_enterprise", "identity_enterprise_operation", "企业受限权限ACL", "Enterprise Restricted Permission ACL",
         "对企业受限权限做 ACL 开放。", ['restricted permission ACL'], ['运行时权限见 security'],
         B(None, None, ('ACL permissions', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "enterprise.identity_enterprise.education_classkit", "enterprise.identity_enterprise", "identity_enterprise_operation", "课堂作业进度", "Class Assignment Progress",
         "教育场景作业与进度上报。", ['ClassKit'], ['学校管理器见 school_manager'],
         B(None, ('ClassKit', 'https://developer.apple.com/documentation/classkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")


    leaf(f, "enterprise.mdm.kiosk", "enterprise.mdm", "mdm_operation", "单应用锁定模式", "Single-App Lock Mode",
         "将设备锁定为展台/单应用模式。", ["lock task / kiosk"], ["策略见 policy"],
         B(("setLockTaskPackages", "https://developer.android.com/reference/android/app/admin/DevicePolicyManager"),
           ("Autonomous Single App Mode", "https://developer.apple.com/documentation/devicemanagement", "framework"), None))
    leaf(f, "enterprise.mdm.attestation", "enterprise.mdm", "mdm_operation", "设备证明", "Device Attestation",
         "获取设备完整性/证明令牌供管理端校验。", ["attestation"], ["合规见 compliance"],
         B(("generateKeyPair attestation", "https://developer.android.com/work/dpc/build-dpc", "guide"),
           ("DeviceCheck / ManagedDevice", "https://developer.apple.com/documentation/devicecheck", "framework"), None))
    leaf(f, "enterprise.work_profile.intent_filter", "enterprise.work_profile", "work_profile_operation", "跨资料意图过滤", "Cross-Profile Intent Filters",
         "声明可跨工作/个人资料传递的意图。", ["cross-profile intent filters"], ["互操作见 cross_profile"],
         B(("addCrossProfileIntentFilter", "https://developer.android.com/reference/android/app/admin/DevicePolicyManager"), None, None))
    leaf(f, "enterprise.work_profile.widget", "enterprise.work_profile", "work_profile_operation", "工作资料小部件策略", "Work Profile Widget Policy",
         "控制工作资料小部件可用性。", ["profile widgets"], ["隔离见 isolation"],
         B(("DevicePolicyManager", "https://developer.android.com/reference/android/app/admin/DevicePolicyManager"), None, None))
    leaf(f, "enterprise.device_policy.camera_mic", "enterprise.device_policy", "device_policy_operation", "相机麦克风禁用", "Camera Mic Disable",
         "策略禁用相机或麦克风。", ["disable camera/mic"], ["功能限制见 restrictions"],
         B(("setCameraDisabled", "https://developer.android.com/reference/android/app/admin/DevicePolicyManager"),
           ("Restrictions payload", "https://developer.apple.com/documentation/devicemanagement", "framework"),
           ("MDM", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-intro")))
    leaf(f, "enterprise.device_policy.usb_file_transfer", "enterprise.device_policy", "device_policy_operation", "USB传输限制", "USB Transfer Restriction",
         "限制 USB 文件传输或调试。", ["USB restriction"], ["功能限制见 restrictions"],
         B(("UserManager.DISALLOW_USB_FILE_TRANSFER", "https://developer.android.com/reference/android/os/UserManager"),
           ("Restrictions payload", "https://developer.apple.com/documentation/devicemanagement", "framework"), None))
    leaf(f, "enterprise.device_policy.wifi_config", "enterprise.device_policy", "device_policy_operation", "企业Wi-Fi配置下发", "Enterprise Wi-Fi Config",
         "下发企业 Wi-Fi 配置档案。", ["Wi-Fi config"], ["网络管控见 network_location"],
         B(("WifiNetworkSuggestion / DPC", "https://developer.android.com/work/dpc/build-dpc", "guide"),
           ("WiFi payload", "https://developer.apple.com/documentation/devicemanagement", "framework"), None))
    leaf(f, "enterprise.identity_enterprise.vpn_per_app", "enterprise.identity_enterprise", "identity_enterprise_operation", "按应用企业VPN", "Per-App Enterprise VPN",
         "为企业应用绑定 VPN 隧道。", ["per-app VPN"], ["SSO 见 sso"],
         B(("setAlwaysOnVpnPackage", "https://developer.android.com/reference/android/app/admin/DevicePolicyManager"),
           ("Per-App VPN", "https://developer.apple.com/documentation/networkextension", "framework"), None))
    leaf(f, "enterprise.identity_enterprise.cert_auth", "enterprise.identity_enterprise", "identity_enterprise_operation", "证书身份认证", "Certificate Based Auth",
         "使用企业证书进行客户端身份认证。", ["client cert auth"], ["证书管理见 device_policy.certificates"],
         B(("KeyChain", "https://developer.android.com/reference/android/security/KeyChain"),
           ("URLCredential", "https://developer.apple.com/documentation/foundation/urlcredential", "class"), None))

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("enterprise", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
