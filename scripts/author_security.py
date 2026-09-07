#!/usr/bin/env python3
"""Author the security domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "security_capability_family"


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "security", parent=None, level="L1",
        zh="安全与隐私", en="Security and Privacy",
        definition="权限模型、密码学、证书、生物识别、安全存储、证明、设备安全与隐私数据保护。",
        includes=["权限、密码学、证书、生物识别、安全存储、证明、设备安全、隐私、数据保护"],
        excludes=["静态文件加密容器见 storage.encryption", "账号登录编排见 identity", "VPN 见 network.vpn"],
        legacy={"disposition": "kept", "sources": ["security"]},
    ))

    l2 = [
        ("security.permissions", "权限模型", "Permission Model",
         "敏感能力的声明、请求、校验与特殊授权。",
         ["运行时权限、特殊权限、校验"], ["生物识别解锁见 security.biometrics"], ["security.permissions"]),
        ("security.crypto", "密钥与密码学", "Keys and Cryptography",
         "密钥库、加解密、签名、摘要与安全随机数。",
         ["密钥库、Cipher、签名、KDF、随机数"], ["凭据条目存储见 security.secure_storage"], ["security.crypto"]),
        ("security.certificates", "证书管理", "Certificate Management",
         "X.509 证书解析校验与系统证书存储。",
         ["解析校验、证书存储"], ["TLS 会话配置见 network.http.tls"], []),
        ("security.biometrics", "生物识别", "Biometrics",
         "指纹/面容等本地生物认证与设备凭据策略。",
         ["生物提示、设备凭据、能力探测"], ["远程身份登录见 identity"], ["security.biometrics"]),
        ("security.secure_storage", "安全存储", "Secure Storage",
         "钥匙串/凭据等敏感数据的系统安全存储。",
         ["凭据条目、访问控制"], ["文件加密见 storage.encryption"], ["security.secure_storage"]),
        ("security.attestation", "完整性与信任证明", "Integrity and Attestation",
         "应用/设备/密钥完整性证明与信任令牌。",
         ["应用完整性、密钥证明、设备令牌"], ["本地生物解锁见 biometrics"], []),
        ("security.device_safety", "设备安全检测", "Device Safety Detection",
         "系统完整性、恶意 URL、风控与反诈等设备侧安全检测。",
         ["完整性、恶意链接、风控"], ["应用证明令牌见 attestation"], []),
        ("security.privacy", "隐私保护", "Privacy Controls",
         "跟踪授权、隐私模式与界面防窥等隐私控制。",
         ["跟踪授权、隐私模式、防窥"], ["运行时权限见 permissions"], []),
        ("security.data_protection", "数据防泄漏保护", "Data Loss Protection",
         "企业级文件分级管控与恢复密钥等数据保护。",
         ["文件分级、恢复密钥"], ["通用文件加密见 storage.encryption"], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="security", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- permissions ---
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("security.permissions.runtime", "运行时权限请求", "Runtime Permission Request",
         "向用户请求危险/受保护资源访问权限并处理结果。",
         ["requestPermissions、requestPermission"], ["特殊设置页授权见 special"],
         merge_bindings(
             A("ActivityCompat.requestPermissions",
               "https://developer.android.com/reference/androidx/core/app/ActivityCompat#requestPermissions(android.app.Activity,%20java.lang.String[],%20int)"),
             I("requesting access", "https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources", "guide"),
             H("@ohos.abilityAccessCtrl", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl"),
         ), {"disposition": "kept", "sources": ["security.permissions.runtime"]}),
        ("security.permissions.special", "特殊权限与设置页", "Special Permissions Settings",
         "需跳转系统设置完成的特殊授权（如所有文件、悬浮窗）。",
         ["MANAGE_EXTERNAL_STORAGE、特殊设置 Intent"], ["普通运行时弹窗见 runtime"],
         merge_bindings(
             A("Settings.ACTION_MANAGE_APP_ALL_FILES_ACCESS_PERMISSION",
               "https://developer.android.com/reference/android/provider/Settings#ACTION_MANAGE_APP_ALL_FILES_ACCESS_PERMISSION"),
             I("UIApplication OpenSettings",
               "https://developer.apple.com/documentation/uikit/uiapplication/1623042-opensettingsurlstring", "property"),
             H("requestPermissionsFromUser", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization"),
         ), {"disposition": "kept", "sources": ["security.permissions.special"]}),
        ("security.permissions.check", "权限校验", "Permission Check",
         "查询自身或目标权限的授予状态。",
         ["checkSelfPermission、checkAccessToken"], ["发起请求见 runtime"],
         merge_bindings(
             A("ContextCompat.checkSelfPermission",
               "https://developer.android.com/reference/androidx/core/content/ContextCompat#checkSelfPermission(android.content.Context,%20java.lang.String)"),
             I("authorizationStatus", "https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624613-authorizationstatus", "method"),
             H("checkAccessToken", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl"),
         ), {"disposition": "new", "sources": []}),
        ("security.permissions.declare", "权限声明", "Permission Declaration",
         "在应用清单中声明所需权限与用途说明。",
         ["uses-permission、Info.plist usage、module.json5"], ["运行时请求见 runtime"],
         merge_bindings(
             A("uses-permission", "https://developer.android.com/guide/topics/manifest/uses-permission-element", "guide"),
             I("Protected resources keys",
               "https://developer.apple.com/documentation/bundleresources/information_property_list/protected_resources", "guide"),
             H("requestPermissions", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions"),
         ), {"disposition": "new", "sources": []}),
        ("security.permissions.rationale", "权限说明与二次请求", "Permission Rationale",
         "在再次请求前展示用途说明或引导设置。",
         ["shouldShowRequestPermissionRationale"], ["首次请求见 runtime"],
         merge_bindings(
             A("shouldShowRequestPermissionRationale",
               "https://developer.android.com/reference/androidx/core/app/ActivityCompat#shouldShowRequestPermissionRationale(android.app.Activity,%20java.lang.String)"),
             pending("ios", "自定义 UI + Open Settings"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
        ("security.permissions.revoke_listen", "权限变更监听", "Permission Change Listen",
         "监听权限授予状态变化。",
         ["OnPermissionsChangeListener、token 变更"], ["单次校验见 check"],
         merge_bindings(
             A("PackageManager.OnPermissionsChangedListener",
               "https://developer.android.com/reference/android/content/pm/PackageManager.OnPermissionsChangedListener"),
             pending("ios"),
             H("on('selfPermissionChange')", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent="security.permissions", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="permission_phase",
            granularity="atomic", bindings=bindings, legacy=legacy,
            privacy_class="runtime_permission",
        ))

    # --- crypto ---
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("security.crypto.keystore", "系统密钥库", "System Keystore",
         "在安全环境生成、导入、存储与使用密钥。",
         ["AndroidKeyStore、Secure Enclave、HUKS"], ["凭据密码条目见 secure_storage"],
         merge_bindings(
             A("Android Keystore", "https://developer.android.com/privacy-and-security/keystore", "guide"),
             I("Secure Enclave", "https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys/storing_keys_in_the_secure_enclave", "guide"),
             H("HUKS", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-overview", "guide"),
         ), {"disposition": "kept", "sources": ["security.crypto.keystore"]}),
        ("security.crypto.cipher", "对称加解密", "Symmetric Cipher",
         "执行对称加解密（如 AES）与工作模式。",
         ["Cipher、AES.GCM、cryptoFramework Cipher"], ["非对称签名见 signature"],
         merge_bindings(
             A("Cipher", "https://developer.android.com/reference/javax/crypto/Cipher"),
             I("AES.GCM", "https://developer.apple.com/documentation/cryptokit/aes/gcm", "struct"),
             H("cryptoFramework Cipher", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework"),
         ), {"disposition": "new", "sources": []}),
        ("security.crypto.signature", "签名与验签", "Sign and Verify",
         "非对称数字签名的生成与验证。",
         ["Signature、SecKeyCreateSignature、Sign/Verify"], ["对称加密见 cipher"],
         merge_bindings(
             A("Signature", "https://developer.android.com/reference/java/security/Signature"),
             I("SecKeyCreateSignature", "https://developer.apple.com/documentation/security/1644057-seckeycreatesignature", "function"),
             H("Sign", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework"),
         ), {"disposition": "new", "sources": []}),
        ("security.crypto.digest", "摘要与MAC", "Digest and MAC",
         "计算哈希摘要与消息认证码。",
         ["MessageDigest、SHA256、HMAC、Mac"], ["签名见 signature"],
         merge_bindings(
             A("MessageDigest", "https://developer.android.com/reference/java/security/MessageDigest"),
             I("SHA256", "https://developer.apple.com/documentation/cryptokit/sha256", "struct"),
             H("Md", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework"),
         ), {"disposition": "new", "sources": []}),
        ("security.crypto.kdf", "密钥派生与协商", "Key Derivation and Agreement",
         "从口令/共享秘密派生密钥或完成密钥协商。",
         ["PBKDF2、HKDF、KeyAgreement"], ["密钥存储见 keystore"],
         merge_bindings(
             A("SecretKeyFactory", "https://developer.android.com/reference/javax/crypto/SecretKeyFactory"),
             I("HKDF", "https://developer.apple.com/documentation/cryptokit/hkdf", "struct"),
             H("HUKS derive", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-overview"),
         ), {"disposition": "new", "sources": []}),
        ("security.crypto.rand", "安全随机数", "Secure Random",
         "生成密码学安全随机数。",
         ["SecureRandom、SecRandomCopyBytes"], ["密钥生成见 keystore"],
         merge_bindings(
             A("SecureRandom", "https://developer.android.com/reference/java/security/SecureRandom"),
             I("SecRandomCopyBytes", "https://developer.apple.com/documentation/security/1399291-secrandomcopybytes", "function"),
             H("Random", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework"),
         ), {"disposition": "new", "sources": []}),
        ("security.crypto.asymmetric", "非对称加解密", "Asymmetric Encryption",
         "使用公钥/私钥对执行加解密。",
         ["RSA/ECIES 加解密"], ["签名见 signature", "HPKE 见 hpke"],
         merge_bindings(
             A("Cipher RSA", "https://developer.android.com/reference/javax/crypto/Cipher"),
             I("ChaChaPoly / CryptoKit", "https://developer.apple.com/documentation/cryptokit", "framework"),
             H("Cipher asymmetric", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework"),
         ), {"disposition": "new", "sources": []}),
        ("security.crypto.hpke", "混合公钥加密", "Hybrid Public Key Encryption",
         "按 HPKE 进行混合公钥加密收发。",
         ["HPKE"], ["经典非对称见 asymmetric"],
         merge_bindings(
             A("android.crypto.hpke", "https://developer.android.com/reference/android/crypto/hpke/package-summary", "package"),
             I("HPKE", "https://developer.apple.com/documentation/cryptokit/hpke", "struct"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
        ("security.crypto.key_export_policy", "密钥不可导出策略", "Non-Exportable Key Policy",
         "配置密钥不可导出及用户认证绑定策略。",
         ["setUserAuthenticationRequired、kSecAttrTokenID"], ["密钥生成见 keystore"],
         merge_bindings(
             A("KeyGenParameterSpec.Builder.setUserAuthenticationRequired",
               "https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setUserAuthenticationRequired(boolean)"),
             I("kSecAttrAccessible", "https://developer.apple.com/documentation/security/ksecattraccessible", "constant"),
             H("HUKS access control", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-overview"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent="security.crypto", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="crypto_primitive",
            granularity="atomic", bindings=bindings, legacy=legacy,
        ))

    # --- certificates ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("security.certificates.parse", "证书解析与校验", "Certificate Parse and Verify",
         "解析证书链并校验签名与有效期。",
         ["CertificateFactory、SecTrustEvaluate"], ["系统存储见 certificates.storage"],
         merge_bindings(
             A("CertificateFactory", "https://developer.android.com/reference/java/security/cert/CertificateFactory"),
             I("SecTrustEvaluateWithError", "https://developer.apple.com/documentation/security/2980705-sectrustevaluatewitherror", "function"),
             H("Device Certificate Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-certificate-kit-overview", "guide"),
         )),
        ("security.certificates.storage", "证书与私钥存储", "Certificate and Key Storage",
         "在系统证书管理服务中存储/获取证书与私钥。",
         ["KeyChain、Keychain 证书、证书管理服务"], ["解析校验见 parse"],
         merge_bindings(
             A("KeyChain", "https://developer.android.com/reference/android/security/KeyChain"),
             I("SecItemAdd certificate", "https://developer.apple.com/documentation/security/1396431-secitemadd", "function"),
             H("证书管理服务", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-certificate-kit-overview"),
         )),
        ("security.certificates.pinning", "证书固定", "Certificate Pinning",
         "将期望公钥/证书固定到网络信任决策。",
         ["CertificatePinner、NSPinnedDomains"], ["TLS 会话见 network.http.tls"],
         merge_bindings(
             A("Network Security Config pinning",
               "https://developer.android.com/privacy-and-security/security-config#CertificatePinning", "guide"),
             I("NSAppTransportSecurity", "https://developer.apple.com/documentation/bundleresources/information_property_list/nsapptransportsecurity", "key"),
             pending("harmonyos"),
         )),
        ("security.certificates.user_install", "用户证书安装提示", "User Certificate Install",
         "引导用户安装或信任用户 CA/客户端证书。",
         ["KeyChain.createInstallIntent、配置描述文件"], ["应用内校验见 parse"],
         merge_bindings(
             A("KeyChain.createInstallIntent",
               "https://developer.android.com/reference/android/security/KeyChain#createInstallIntent()"),
             pending("ios", "通常经配置描述文件/MDM"),
             pending("harmonyos"),
         )),
    ]:
        f.append(feature(
            fid, parent="security.certificates", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="certificate_role",
            granularity="atomic", bindings=bindings,
        ))

    # --- biometrics ---
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("security.biometrics.local_auth", "本地生物认证", "Local Biometric Auth",
         "拉起系统生物识别提示完成本地认证。",
         ["BiometricPrompt、LAContext、userAuth"], ["设备 PIN 策略见 device_credential"],
         merge_bindings(
             A("BiometricPrompt", "https://developer.android.com/reference/androidx/biometric/BiometricPrompt", "class"),
             I("LAContext", "https://developer.apple.com/documentation/localauthentication/lacontext", "class"),
             H("@ohos.userIAM.userAuth", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-useriam-userauth"),
         ), {"disposition": "kept", "sources": ["security.biometrics.local_auth"]}),
        ("security.biometrics.device_credential", "设备凭据认证", "Device Credential Auth",
         "以锁屏 PIN/密码作为后备或替代认证。",
         ["DEVICE_CREDENTIAL、deviceOwnerAuthentication"], ["纯生物见 local_auth"],
         merge_bindings(
             A("BIOMETRIC_STRONG | DEVICE_CREDENTIAL",
               "https://developer.android.com/reference/androidx/biometric/BiometricManager.Authenticators"),
             I("deviceOwnerAuthentication",
               "https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthentication", "case"),
             H("AuthType PIN", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-useriam-userauth"),
         ), {"disposition": "new", "sources": []}),
        ("security.biometrics.capability", "生物能力探测", "Biometric Capability Probe",
         "查询设备可用的生物识别强度与可用性。",
         ["canAuthenticate、biometryType"], ["发起认证见 local_auth"],
         merge_bindings(
             A("BiometricManager.canAuthenticate",
               "https://developer.android.com/reference/androidx/biometric/BiometricManager#canAuthenticate(int)"),
             I("LAContext.biometryType",
               "https://developer.apple.com/documentation/localauthentication/lacontext/1622648-biometrytype", "property"),
             H("getAvailableStatus", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-useriam-userauth"),
         ), {"disposition": "new", "sources": []}),
        ("security.biometrics.crypto_bind", "生物绑定密钥使用", "Biometric-Bound Key Use",
         "在生物认证成功后解锁并使用绑定密钥。",
         ["CryptoObject、SecAccessControl biometry"], ["密钥生成见 crypto.keystore"],
         merge_bindings(
             A("BiometricPrompt.CryptoObject",
               "https://developer.android.com/reference/androidx/biometric/BiometricPrompt.CryptoObject"),
             I("SecAccessControlCreateWithFlags",
               "https://developer.apple.com/documentation/security/1394338-secaccesscontrolcreatewithflags", "function"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
        ("security.biometrics.enrollment_change", "生物登记变更感知", "Enrollment Change Detection",
         "感知生物特征登记集变更以作废旧密钥策略。",
         ["setInvalidatedByBiometricEnrollment"], ["认证提示见 local_auth"],
         merge_bindings(
             A("setInvalidatedByBiometricEnrollment",
               "https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setInvalidatedByBiometricEnrollment(boolean)"),
             I("evaluatedPolicyDomainState",
               "https://developer.apple.com/documentation/localauthentication/lacontext/1624652-evaluatedpolicydomainstate", "property"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent="security.biometrics", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="biometric_role",
            granularity="atomic", bindings=bindings, legacy=legacy,
            privacy_class="runtime_permission",
        ))

    # --- secure_storage ---
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("security.secure_storage.credentials", "凭据安全存储", "Credential Secure Storage",
         "在系统安全存储中保存密码、令牌等凭据。",
         ["Keychain、EncryptedSharedPreferences、Asset Store"], ["密钥对象见 crypto.keystore"],
         merge_bindings(
             A("EncryptedSharedPreferences",
               "https://developer.android.com/reference/androidx/security/crypto/EncryptedSharedPreferences", "class"),
             I("SecItemAdd", "https://developer.apple.com/documentation/security/1396431-secitemadd", "function"),
             H("@ohos.security.asset", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-security-asset"),
         ), {"disposition": "kept", "sources": ["security.secure_storage.credentials"]}),
        ("security.secure_storage.access_control", "凭据访问控制", "Credential Access Control",
         "为凭据条目设置解锁状态/生物访问控制。",
         ["kSecAttrAccessible、访问控制表"], ["写入条目见 credentials"],
         merge_bindings(
             pending("android", "MasterKey / Keystore 绑定待核"),
             I("kSecAttrAccessibleWhenUnlocked",
               "https://developer.apple.com/documentation/security/ksecattraccessiblewhenunlocked", "constant"),
             H("Asset access control", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-store-kit-overview"),
         ), {"disposition": "new", "sources": []}),
        ("security.secure_storage.shared", "跨应用凭据共享", "Shared Credential Access",
         "在应用组或授权应用间共享凭据条目。",
         ["Keychain access group、SharedPreferences 非适用"], ["单应用条目见 credentials"],
         merge_bindings(
             A("KeyChain", "https://developer.android.com/reference/android/security/KeyChain"),
             I("kSecAttrAccessGroup", "https://developer.apple.com/documentation/security/ksecattraccessgroup", "constant"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
        ("security.secure_storage.autofill", "系统自动填充对接", "Autofill Integration",
         "向系统自动填充框架暴露或消费凭据字段。",
         ["AutofillService、ASCredentialProvider"], ["通用凭据存储见 credentials"],
         merge_bindings(
             A("AutofillService", "https://developer.android.com/reference/android/service/autofill/AutofillService"),
             I("ASCredentialProviderExtensionViewController",
               "https://developer.apple.com/documentation/authenticationservices/ascredentialproviderextensionviewcontroller", "class"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent="security.secure_storage", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="secure_storage_role",
            granularity="atomic", bindings=bindings, legacy=legacy,
        ))

    # --- attestation ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("security.attestation.app_integrity", "应用完整性证明", "App Integrity Attestation",
         "获取应用未被篡改/来源可信的证明令牌。",
         ["Play Integrity、App Attest"], ["密钥证明见 key_attestation"],
         merge_bindings(
             A("Play Integrity", "https://developer.android.com/google/play/integrity/overview", "guide"),
             I("DCAppAttestService", "https://developer.apple.com/documentation/devicecheck/dcappattestservice", "class"),
             pending("harmonyos"),
         )),
        ("security.attestation.key_attestation", "密钥证明", "Key Attestation",
         "证明密钥生成于安全硬件及其属性。",
         ["Key Attestation、attestKey"], ["应用完整性见 app_integrity"],
         merge_bindings(
             A("Key Attestation", "https://developer.android.com/privacy-and-security/security-key-attestation", "guide"),
             pending("ios", "Secure Enclave 证明能力待核"),
             H("attestKeyItem", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-overview"),
         )),
        ("security.attestation.device_token", "设备信任令牌", "Device Trust Token",
         "获取设备维度信任令牌用于防刷与真机判定。",
         ["DeviceCheck token、DeviceVerify"], ["应用完整性见 app_integrity"],
         merge_bindings(
             pending("android", "Play Integrity 设备判决部分可覆盖"),
             I("DCDevice.generateToken",
               "https://developer.apple.com/documentation/devicecheck/dcdevice/generatetoken(completionhandler:)", "method"),
             H("DeviceVerify", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-verify-overview", "guide"),
         )),
        ("security.attestation.server_verify", "证明服务端核验入口", "Attestation Server Verify",
         "将端侧证明令牌提交服务端核验的配套能力说明（端侧取证）。",
         ["端侧取证 + 服务核验流程"], ["令牌获取见 app_integrity/device_token"],
         merge_bindings(
             A("Integrity token decode", "https://developer.android.com/google/play/integrity/verdict", "guide"),
             I("App Attest validation", "https://developer.apple.com/documentation/devicecheck/validating_apps_that_connect_to_your_server", "guide"),
             H("DeviceVerify REST", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-verify-overview"),
         )),
    ]:
        f.append(feature(
            fid, parent="security.attestation", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="attestation_kind",
            granularity="atomic", bindings=bindings,
        ))

    # --- device_safety ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("security.device_safety.sys_integrity", "系统完整性检测", "System Integrity Detection",
         "检测设备系统是否被破解并给出风险评级。",
         ["SafetyDetect 系统完整性、root 检测"], ["应用完整性令牌见 attestation.app_integrity"],
         merge_bindings(
             A("Play Integrity device verdict", "https://developer.android.com/google/play/integrity/verdicts", "guide"),
             I("DeviceCheck", "https://developer.apple.com/documentation/devicecheck", "framework"),
             H("SafetyDetect", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/safetydetect-sysintegrity"),
         )),
        ("security.device_safety.malicious_url", "恶意URL检测", "Malicious URL Detection",
         "检测 URL 是否为恶意或钓鱼链接。",
         ["恶意 URL API"], ["网络 TLS 见 network.http.tls"],
         merge_bindings(
             pending("android"), pending("ios"),
             H("SafetyDetect URL", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/safetydetect-overview"),
         )),
        ("security.device_safety.risk_engine", "综合风控评估", "Risk Assessment Engine",
         "提交多维风险因子获得综合风险评估。",
         ["RiskControlEngine"], ["单点完整性见 sys_integrity"],
         merge_bindings(
             pending("android"), pending("ios"),
             H("RiskControlEngine", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/risk-control-engine"),
         )),
        ("security.device_safety.fraud", "反诈与业务风险", "Anti-Fraud and Business Risk",
         "识别涉诈通信/消息或自动化作弊风险。",
         ["AntifraudPicker、BusinessRisk"], ["恶意 URL 见 malicious_url"],
         merge_bindings(
             pending("android"), pending("ios"),
             H("AntifraudPicker", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/antifraud-picker"),
         )),
        ("security.device_safety.trusted_app", "可信应用数据证明", "Trusted App Data Proof",
         "对应用数据/会话/媒体进行安全证明。",
         ["TrustedAppService"], ["密钥证明见 attestation.key_attestation"],
         merge_bindings(
             pending("android"), pending("ios"),
             H("TrustedAppService", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/trusted-app-service"),
         )),
        ("security.device_safety.audit", "安全审计订阅", "Security Audit Subscription",
         "订阅统一安全审计数据流。",
         ["SecurityAudit"], ["风控评分见 risk_engine"],
         merge_bindings(
             pending("android"), pending("ios"),
             H("SecurityAudit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/security-audit"),
         )),
        ("security.device_safety.antivirus", "病毒防护状态", "Antivirus Protection Status",
         "查询设备病毒查杀与防护状态。",
         ["SecurityAntivirus"], ["系统完整性见 sys_integrity"],
         merge_bindings(
             pending("android"), pending("ios"),
             H("SecurityAntivirus", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-security-antivirus"),
         )),
    ]:
        f.append(feature(
            fid, parent="security.device_safety", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="device_safety_kind",
            granularity="atomic", bindings=bindings,
        ))

    # --- privacy ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("security.privacy.tracking_consent", "跟踪授权", "Tracking Consent",
         "请求跨应用跟踪授权并读取广告标识相关状态。",
         ["ATTrackingManager、广告标识授权"], ["普通运行时权限见 permissions.runtime"],
         merge_bindings(
             A("Advertising ID", "https://developer.android.com/design-for-safety/privacy-sandbox/rights-preserving-api-android", "guide"),
             I("ATTrackingManager", "https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager", "class"),
             pending("harmonyos"),
         )),
        ("security.privacy.pasteboard_protect", "剪贴板访问保护", "Pasteboard Access Protection",
         "感知或限制对剪贴板敏感内容的访问。",
         ["UIPasteboard 检测、剪贴板提示"], ["通用权限见 permissions"],
         merge_bindings(
             A("ClipboardManager", "https://developer.android.com/reference/android/content/ClipboardManager"),
             I("UIPasteboard", "https://developer.apple.com/documentation/uikit/uipasteboard", "class"),
             pending("harmonyos"),
         )),
        ("security.privacy.screenshot_detect", "截屏/录屏感知", "Screenshot and Capture Detect",
         "感知截屏或屏幕录制以保护敏感界面。",
         ["userDidTakeScreenshot、capture callbacks"], ["防窥蒙层见 anti_peep"],
         merge_bindings(
             A("FLAG_SECURE", "https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE"),
             I("userDidTakeScreenshotNotification",
               "https://developer.apple.com/documentation/uikit/uiapplication/1622920-userdidtakescreenshotnotification", "property"),
             pending("harmonyos"),
         )),
        ("security.privacy.anti_peep", "防窥保护", "Anti-Peep Protection",
         "感知窥视状态并拉起系统蒙层遮盖敏感信息。",
         ["DlpAntiPeep"], ["截屏感知见 screenshot_detect"],
         merge_bindings(
             pending("android"), pending("ios"),
             H("DlpAntiPeep", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dlp-anti-peep"),
         )),
        ("security.privacy.super_privacy", "增强隐私模式感知", "Enhanced Privacy Mode",
         "查询增强/超级隐私模式状态并调整行为。",
         ["SuperPrivacyMode"], ["跟踪授权见 tracking_consent"],
         merge_bindings(
             pending("android"), pending("ios"),
             H("SuperPrivacyMode", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/super-privacy-mode"),
         )),
        ("security.privacy.data_usage_flag", "数据使用目的标记", "Data Use Purpose Flagging",
         "为敏感 API 调用声明数据使用目的（平台支持时）。",
         ["data usage flags"], ["权限请求见 permissions.runtime"],
         merge_bindings(
             A("Privacy Sandbox Attribution", "https://developer.android.com/design-for-safety/privacy-sandbox", "guide"),
             I("Purpose strings", "https://developer.apple.com/documentation/bundleresources/information_property_list/protected_resources", "guide"),
             pending("harmonyos"),
         )),
    ]:
        f.append(feature(
            fid, parent="security.privacy", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="privacy_control",
            granularity="atomic", bindings=bindings, privacy_class="runtime_permission",
        ))

    # --- data_protection ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("security.data_protection.dlp", "文件分级管控", "File Classification Control",
         "识别敏感资产文件并限制外发（企业场景）。",
         ["fileGuard、DLP"], ["通用文件加密见 storage.encryption"],
         merge_bindings(
             pending("android"),
             I("FileProvider / MDM", "https://developer.apple.com/documentation/devicemanagement", "guide"),
             H("fileGuard", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard"),
         )),
        ("security.data_protection.recovery_key", "企业恢复密钥", "Enterprise Recovery Key",
         "企业场景下磁盘加密数据解密与锁屏密码重置相关能力。",
         ["recoveryKey"], ["用户备份见 storage.backup"],
         merge_bindings(
             pending("android"),
             pending("ios", "MDM 托管恢复，待核"),
             H("recoveryKey", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recovery-key"),
         )),
        ("security.data_protection.screen_secure", "界面防泄密标志", "Secure Window Flag",
         "禁止敏感窗口被截屏或出现在最近任务预览。",
         ["FLAG_SECURE、isSecure"], ["截屏事件感知见 privacy.screenshot_detect"],
         merge_bindings(
             A("FLAG_SECURE", "https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE"),
             I("isSecure", "https://developer.apple.com/documentation/uikit/uitextfield/1619613-issecuretextentry", "property"),
             H("window privacy", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-privacy"),
         )),
        ("security.data_protection.managed_config", "托管数据隔离", "Managed Data Isolation",
         "工作资料/托管配置下的数据隔离入口。",
         ["Work Profile、Managed App Config"], ["DLP 文件级见 dlp"],
         merge_bindings(
             A("Work Profile", "https://developer.android.com/work/managed-profiles", "guide"),
             I("Managed App Configuration",
               "https://developer.apple.com/documentation/devicemanagement/apps/managedappconfiguration", "guide"),
             pending("harmonyos"),
         )),
        ("security.data_protection.clear_on_logout", "退出时敏感数据清理", "Sensitive Data Clear on Logout",
         "在退出登录或注销时清理内存与本地敏感缓存的系统辅助能力边界。",
         ["凭据删除、缓存清理入口"], ["凭据存储见 secure_storage.credentials"],
         merge_bindings(
             A("AccountManager clear", "https://developer.android.com/reference/android/accounts/AccountManager", "class"),
             I("SecItemDelete", "https://developer.apple.com/documentation/security/1396430-secitemdelete", "function"),
             H("asset delete", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-security-asset"),
         )),
        ("security.data_protection.clipboard_redact", "敏感内容剪贴板策略", "Sensitive Clipboard Policy",
         "限制敏感内容进入剪贴板或设置短暂有效期。",
         ["敏感标记、短暂剪贴板"], ["剪贴板访问感知见 privacy.pasteboard_protect"],
         merge_bindings(
             A("ClipDescription", "https://developer.android.com/reference/android/content/ClipDescription"),
             I("UIPasteboard.DetectionPattern",
               "https://developer.apple.com/documentation/uikit/uipasteboard/detectionpattern", "struct"),
             pending("harmonyos"),
         )),
    ]:
        f.append(feature(
            fid, parent="security.data_protection", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="data_protection_kind",
            granularity="atomic", bindings=bindings,
        ))

    # Extra crypto / permissions / privacy leaves for coverage density
    for fid, parent, axis, zh, en, definition, includes, excludes, bindings in [
        ("security.crypto.key_import", "security.crypto", "crypto_primitive",
         "密钥导入导出边界", "Key Import Export Boundary",
         "在策略允许时导入外部密钥材料或导出公钥。",
         ["importKey、SecItemImport"], ["不可导出策略见 key_export_policy"],
         merge_bindings(
             A("KeyStore.setEntry", "https://developer.android.com/reference/java/security/KeyStore#setEntry(java.lang.String,%20java.security.KeyStore.Entry,%20java.security.KeyStore.ProtectionParameter)"),
             I("SecItemImport", "https://developer.apple.com/documentation/security/1394828-secitemimport", "function"),
             H("HUKS importKeyItem", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-overview"),
         )),
        ("security.crypto.algorithm_probe", "security.crypto", "crypto_primitive",
         "算法套件能力探测", "Algorithm Suite Probe",
         "查询设备支持的算法/曲线/工作模式。",
         ["Provider、CryptoKit availability"], ["执行加解密见 cipher"],
         merge_bindings(
             A("Security.getProviders", "https://developer.android.com/reference/java/security/Security#getProviders()"),
             I("CryptoKit", "https://developer.apple.com/documentation/cryptokit", "framework"),
             H("cryptoFramework", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework"),
         )),
        ("security.permissions.background", "security.permissions", "permission_phase",
         "后台敏感权限", "Background Sensitive Permission",
         "请求或校验后台位置等后台敏感权限。",
         ["ACCESS_BACKGROUND_LOCATION、后台模式"], ["前台运行时权限见 runtime"],
         merge_bindings(
             A("ACCESS_BACKGROUND_LOCATION",
               "https://developer.android.com/reference/android/Manifest.permission#ACCESS_BACKGROUND_LOCATION"),
             I("background modes", "https://developer.apple.com/documentation/bundleresources/information_property_list/uibackgroundmodes", "key"),
             H("background permissions", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions"),
         )),
        ("security.permissions.one_time", "security.permissions", "permission_phase",
         "一次性授权", "One-Time Grant",
         "支持仅这一次的运行时授权选项。",
         ["one-time permission"], ["永久授权见 runtime"],
         merge_bindings(
             A("one-time permissions", "https://developer.android.com/training/permissions/requesting#one-time", "guide"),
             pending("ios", "部分 API 会话级授权"),
             pending("harmonyos"),
         )),
        ("security.privacy.local_network", "security.privacy", "privacy_control",
         "本地网络访问授权", "Local Network Access Consent",
         "请求访问本地网络的隐私授权。",
         ["local network privacy"], ["mDNS 发现见 network.discovery"],
         merge_bindings(
             pending("android", "CHANGE_WIFI_MULTICAST 等边界待核"),
             I("Local Network Privacy", "https://developer.apple.com/documentation/bundleresources/information_property_list/nslocalnetworkusagedescription", "key"),
             pending("harmonyos"),
         )),
        ("security.privacy.precise_toggle", "security.privacy", "privacy_control",
         "精确/模糊数据粒度选择", "Precise Versus Approximate Data",
         "在精确与模糊位置等粒度之间尊重用户选择。",
         ["precise/approximate location"], ["权限请求见 permissions.runtime"],
         merge_bindings(
             A("ACCESS_COARSE_LOCATION",
               "https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION"),
             I("accuracyAuthorization",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/3601124-accuracyauthorization", "property"),
             pending("harmonyos"),
         )),
        ("security.attestation.nonce", "security.attestation", "attestation_kind",
         "证明挑战随机数", "Attestation Challenge Nonce",
         "为证明流程提供服务端挑战随机数并绑定令牌。",
         ["nonce/challenge"], ["令牌获取见 app_integrity"],
         merge_bindings(
             A("IntegrityTokenRequest.setNonce",
               "https://developer.android.com/reference/com/google/android/play/core/integrity/IntegrityTokenRequest.Builder"),
             I("App Attest clientDataHash",
               "https://developer.apple.com/documentation/devicecheck/dcappattestservice", "class"),
             pending("harmonyos"),
         )),
        ("security.certificates.ct", "security.certificates", "certificate_role",
         "证书透明度感知", "Certificate Transparency Awareness",
         "在信任评估中考虑证书透明度信息（平台支持时）。",
         ["CT policy"], ["证书固定见 pinning"],
         merge_bindings(
             A("Network Security Config", "https://developer.android.com/privacy-and-security/security-config", "guide"),
             I("SecTrust", "https://developer.apple.com/documentation/security/sectrust", "type"),
             pending("harmonyos"),
         )),
    ]:
        f.append(feature(
            fid, parent=parent, level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=axis, granularity="atomic",
            bindings=bindings,
            privacy_class="runtime_permission" if "permissions" in parent or "privacy" in parent else "none",
        ))

    dedup = {}
    for node in f:
        dedup[node["id"]] = node
    return list(dedup.values())


def main():
    nodes = build()
    path = write_domain("security", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
