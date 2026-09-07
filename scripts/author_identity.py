#!/usr/bin/env python3
"""Author the identity domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "identity_concern"


def leaf(f, fid, parent, axis, zh, en, definition, includes, excludes, bindings,
         legacy=None, level="L3", related=None, privacy="none"):
    f.append(feature(
        fid, parent=parent, level=level, zh=zh, en=en, definition=definition,
        includes=includes, excludes=excludes, sibling_axis=axis,
        granularity="atomic", bindings=bindings,
        legacy=legacy or {"disposition": "new", "sources": []},
        related=related, privacy_class=privacy,
    ))


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "identity", parent=None, level="L1",
        zh="身份与账号", en="Identity and Accounts",
        definition="系统账号框架、联邦登录、认证因子/核身与会话凭据管理。",
        includes=["system_account、federated、authn_factors、session"],
        excludes=["生物识别解锁见 security", "支付实名收银台见 commerce.payment", "开发者实名入驻排除"],
        legacy={"disposition": "kept", "sources": ["identity"]},
    ))

    l2 = [
        ("identity.system_account", "系统账号", "System Account",
         "设备/系统账号注册表、认证器插件、变更监听与应用账号。",
         ["manager、authenticator、change_listener、app_accounts、distributed"],
         ["联邦登录按钮流见 federated", "会话凭据见 session"],
         ["identity.system_account"]),
        ("identity.federated", "联邦登录", "Federated Sign-In",
         "平台账号授权登录、第三方联邦、范围授权、服务端校验与账号关联。",
         ["platform_sign_in、third_party、scopes、server_verify、account_linking"],
         ["系统账号注册表见 system_account", "通行密钥见 session.passkey"],
         ["identity.federated"]),
        ("identity.authn_factors", "认证因子与核身", "Auth Factors and Verification",
         "手机号/邮箱、人脸核身、实名与未成年人保护等核身因子。",
         ["phone_email、face_verify、realname、minors_protection"],
         ["本地生物解锁见 security", "联邦 OAuth 见 federated"],
         []),
        ("identity.session", "会话与凭据", "Session and Credentials",
         "凭据管理器、通行密钥、自动填充、凭据提供者与数字证件会话。",
         ["credential_manager、passkey、autofill、provider、digital_id"],
         ["联邦授权码流见 federated", "系统账号条目见 system_account"],
         []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="identity", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- system_account ---
    leaf(f, "identity.system_account.manager", "identity.system_account", "account_role",
         "账号管理", "Account Manager",
         "查询/添加/移除系统账号条目。",
         ["AccountManager、osAccount query"],
         ["认证器插件见 authenticator"],
         merge_bindings(
             A("AccountManager", "https://developer.android.com/reference/android/accounts/AccountManager"),
             I("ACAccountStore", "https://developer.apple.com/documentation/accounts/acaccountstore", "class"),
             H("@ohos.account.osAccount", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-os-account"),
         ),
         legacy={"disposition": "kept", "sources": ["identity.system_account.manager"]},
         privacy="runtime_permission")
    leaf(f, "identity.system_account.authenticator", "identity.system_account", "account_role",
         "账号认证器插件", "Account Authenticator Plugin",
         "向系统注册自定义账号类型认证器服务。",
         ["AbstractAccountAuthenticator"],
         ["账号列表管理见 manager"],
         merge_bindings(
             A("AbstractAccountAuthenticator", "https://developer.android.com/reference/android/accounts/AbstractAccountAuthenticator"),
             pending("ios"),
             H("@ohos.account.appAccount", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-account"),
         ))
    leaf(f, "identity.system_account.change_listener", "identity.system_account", "account_role",
         "账号变更监听", "Account Change Listener",
         "监听账号增删或系统账号切换。",
         ["OnAccountsUpdateListener、osAccountSwitch"],
         ["账号查询见 manager"],
         merge_bindings(
             A("OnAccountsUpdateListener", "https://developer.android.com/reference/android/accounts/OnAccountsUpdateListener"),
             pending("ios"),
             H("osAccount.on", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-os-account"),
         ))
    leaf(f, "identity.system_account.app_accounts", "identity.system_account", "account_role",
         "应用账号", "App Account Store",
         "应用级账号创建、凭据与授权数据。",
         ["appAccount create/setCredential"],
         ["系统账号注册表见 manager"],
         merge_bindings(
             A("AccountManager.setUserData", "https://developer.android.com/reference/android/accounts/AccountManager"),
             pending("ios"),
             H("@ohos.account.appAccount", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-account"),
         ),
         privacy="sensitive")
    leaf(f, "identity.system_account.distributed", "identity.system_account", "account_role",
         "分布式账号", "Distributed Account",
         "跨设备分布式账号标识查询/设置入口。",
         ["distributedAccount"],
         ["联邦登录见 federated", "分布式 Continuity 见 distributed"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("@ohos.account.distributedAccount", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-account"),
         ),
         related=["distributed"])

    # --- federated ---
    leaf(f, "identity.federated.platform_sign_in", "identity.federated", "federated_role",
         "平台账号登录", "Platform Account Sign-In",
         "使用系统平台账号一键授权登录应用。",
         ["Sign in with Apple、Sign in with Google / Credential Manager、Account Kit"],
         ["第三方 IdP 见 third_party", "通行密钥见 session.passkey"],
         merge_bindings(
             A("CredentialManager", "https://developer.android.com/reference/androidx/credentials/CredentialManager"),
             I("ASAuthorizationAppleIDProvider", "https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidprovider", "class"),
             H("Account Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-kit-intro", "guide"),
         ),
         legacy={"disposition": "kept", "sources": ["identity.federated.platform_sign_in"]},
         privacy="sensitive")
    leaf(f, "identity.federated.third_party", "identity.federated", "federated_role",
         "第三方联邦登录", "Third-Party Federated Sign-In",
         "接入非本平台 IdP 的联邦登录 SDK 能力边界（公开 API 入口）。",
         ["OAuth IdP SDK entry"],
         ["平台账号登录见 platform_sign_in"],
         merge_bindings(
             A("Identity toolkit", "https://developer.android.com/training/sign-in", "guide"),
             I("AuthenticationServices", "https://developer.apple.com/documentation/authenticationservices"),
             H("Authentication Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/authentication-service-introduction", "guide"),
         ))
    leaf(f, "identity.federated.scopes", "identity.federated", "federated_role",
         "授权范围", "Authorization Scopes",
         "请求/增量授权用户资料与能力范围。",
         ["OAuth scopes、AuthorizationController"],
         ["服务端 token 校验见 server_verify"],
         merge_bindings(
             A("Google Sign-In scopes", "https://developers.google.com/identity/sign-in/android", "guide"),
             I("ASAuthorization", "https://developer.apple.com/documentation/authenticationservices/asauthorization", "class"),
             H("Account Kit AuthorizationController", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-kit-intro", "guide"),
         ))
    leaf(f, "identity.federated.server_verify", "identity.federated", "federated_role",
         "服务端令牌校验", "Server Token Verification",
         "服务端校验/撤销联邦 id_token 或授权码。",
         ["Sign in with Apple REST、id_token verify"],
         ["客户端授权 UI 见 platform_sign_in"],
         merge_bindings(
             A("Google ID token", "https://developer.android.com/identity/sign-in/credential-manager-siwg", "guide"),
             I("Sign in with Apple REST API", "https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api", "guide"),
             H("Account Kit server", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-kit-intro", "guide"),
         ))
    leaf(f, "identity.federated.account_linking", "identity.federated", "federated_role",
         "账号关联", "Account Linking",
         "将应用账号与平台/渠道账号关联。",
         ["ServicesAccountLinking、streamlined linking"],
         ["平台登录见 platform_sign_in"],
         merge_bindings(
             A("Account linking", "https://developer.android.com/training/sign-in", "guide"),
             I("ServicesAccountLinking", "https://developer.apple.com/documentation/storekisservicesaccountlinking"),
             pending("harmonyos"),
         ))

    # --- authn_factors ---
    leaf(f, "identity.authn_factors.phone_email", "identity.authn_factors", "factor_kind",
         "手机号邮箱认证", "Phone and Email Auth",
         "以手机号/邮箱作为应用内认证因子。",
         ["phone/email OTP or hint"],
         ["人脸核身见 face_verify", "联邦账号见 federated"],
         merge_bindings(
             A("Phone Number Hint", "https://developers.google.com/identity/phone-number-hint/android", "guide"),
             pending("ios"),
             H("Authentication Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/authentication-service-introduction", "guide"),
         ),
         privacy="sensitive")
    leaf(f, "identity.authn_factors.face_verify", "identity.authn_factors", "factor_kind",
         "人脸核身", "Face Identity Verification",
         "系统级人脸核身通道完成身份核验（区别于本地生物解锁）。",
         ["face verify FunctionalButton"],
         ["本地生物解锁见 security.biometrics"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("Scenario Fusion Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenariokit-introduction", "guide"),
         ),
         privacy="sensitive",
         related=["security"])
    leaf(f, "identity.authn_factors.realname", "identity.authn_factors", "factor_kind",
         "实名核验", "Real-Name Verification",
         "应用侧触发的用户实名核验能力（非开发者入驻）。",
         ["realNameService"],
         ["支付实名见 commerce.payment", "开发者实名入驻排除"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("Game Service / realname", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-introduction", "guide"),
         ),
         privacy="sensitive",
         related=["commerce.payment"])
    leaf(f, "identity.authn_factors.minors_protection", "identity.authn_factors", "factor_kind",
         "未成年人保护", "Minors Protection",
         "查询未成年人保护/防沉迷状态并引导验证。",
         ["minors protection info / FamilyControls"],
         ["普通账号登录见 federated"],
         merge_bindings(
             A("Families", "https://developer.android.com/topic/families", "guide"),
             I("FamilyControls", "https://developer.apple.com/documentation/familycontrols"),
             H("getMinorsProtectionInfo", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-account-game-service"),
         ),
         privacy="sensitive")

    # --- session ---
    leaf(f, "identity.session.credential_manager", "identity.session", "session_role",
         "凭据管理器", "Credential Manager",
         "统一创建/获取密码与联邦凭据的系统凭据管理器。",
         ["CredentialManager get/create"],
         ["通行密钥专型见 passkey", "自动填充 UI 见 autofill"],
         merge_bindings(
             A("CredentialManager", "https://developer.android.com/reference/androidx/credentials/CredentialManager"),
             I("AuthenticationServices", "https://developer.apple.com/documentation/authenticationservices"),
             H("autofill / password vault", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-basic-components-textinput", "guide"),
         ),
         privacy="sensitive")
    leaf(f, "identity.session.passkey", "identity.session", "session_role",
         "通行密钥", "Passkeys",
         "WebAuthn/FIDO2 通行密钥注册与断言。",
         ["public key credential、FIDO2"],
         ["密码凭据管理见 credential_manager"],
         merge_bindings(
             A("CreatePublicKeyCredentialRequest", "https://developer.android.com/reference/androidx/credentials/CreatePublicKeyCredentialRequest"),
             I("ASAuthorizationPublicKeyCredentialRegistration", "https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialregistration", "protocol"),
             H("FIDO2 Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fido2-overview", "guide"),
         ),
         privacy="sensitive",
         related=["identity.session.credential_manager"])
    leaf(f, "identity.session.autofill", "identity.session", "session_role",
         "凭据自动填充", "Credential Autofill",
         "输入框声明自动填充提示并由系统填充账号密码。",
         ["AutofillManager、textContentType、enableAutoFill"],
         ["凭据提供者扩展见 provider"],
         merge_bindings(
             A("AutofillManager", "https://developer.android.com/reference/android/view/autofill/AutofillManager"),
             I("textContentType", "https://developer.apple.com/documentation/uikit/uitextcontenttype", "type"),
             H("TextInput enableAutoFill", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-basic-components-textinput", "guide"),
         ),
         privacy="sensitive")
    leaf(f, "identity.session.provider", "identity.session", "session_role",
         "凭据提供者扩展", "Credential Provider Extension",
         "作为系统凭据/自动填充提供者向其他应用供数。",
         ["AutofillService、ASCredentialProvider"],
         ["消费侧自动填充见 autofill"],
         merge_bindings(
             A("AutofillService", "https://developer.android.com/reference/android/service/autofill/AutofillService"),
             I("ASCredentialProviderViewController", "https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller", "class"),
             pending("harmonyos"),
         ),
         privacy="sensitive")
    leaf(f, "identity.session.digital_id", "identity.session", "session_role",
         "数字证件凭据", "Digital Identity Credentials",
         "移动驾驶证等数字证件/mdoc 出示与钱包凭据读取。",
         ["mdoc、Identity Credential、digital credentials"],
         ["钱包卡券写入见 commerce.payment.wallet"],
         merge_bindings(
             A("IdentityCredentialClient", "https://developer.android.com/reference/androidx/security/identity/IdentityCredentialClient"),
             I("IdentityDocumentServices", "https://developer.apple.com/documentation/identitydocumentservices"),
             pending("harmonyos"),
         ),
         privacy="sensitive",
         related=["commerce.payment"])

    dedup = {}
    for node in f:
        dedup[node["id"]] = node
    return list(dedup.values())


def main():
    nodes = build()
    path = write_domain("identity", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
