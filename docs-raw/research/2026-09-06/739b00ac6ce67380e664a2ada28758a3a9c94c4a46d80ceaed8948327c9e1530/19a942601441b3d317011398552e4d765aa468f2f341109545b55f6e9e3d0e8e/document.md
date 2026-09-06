# Platform Single Sign-on (SSO)

Provide a Platform Single Sign-on (Platform SSO) extension to integrate your identity provider with macOS.

## Discussion

Platform SSO is a replacement for binding a Mac to directory services. It builds on enterprise SSO extensions to perform single sign-on for apps and websites.

Platform SSO supports the following authentication methods with an identity provider:

- Password: With this method, a user authenticates with the identity provider using a password. This method also supports WS-Trust, allowing the user to authenticate even when using a federated identity provider.
- Secure Enclave–backed key: With this method, a user who logs in to their Mac with a local account password can use a Secure Enclave–backed key to authenticate with the identity provider without a password. The identity provider sets up the Secure Enclave key during the user registration process.
- Web-based: With this method, a user authenticates on a web form that the identity provider presents. This web-based authentication method can also offer multistep authentication flows, and allows camera access for users to sign in by scanning a QR code.
- Smart card: With this method, a user authenticates with the identity provider using a smart card. Register the smart card with the identity provider and configure smart card attribute-mapping on the Mac.
- Access key: With this method, a user uses a pass stored in Apple Wallet to authenticate with the identity provider. As with a smart card, register the access key with the identity provider.

Platform SSO can create new local user accounts on demand at the login window using identity provider credentials. It can also integrate identity provider group membership into macOS. You can use network accounts for authorization, and groups can also authorize network accounts.

## Implement Platform SSO 2.0

Platform SSO 2.0 revises the system by adding a new key service for SSO extensions and identity providers. Implement an alternative registration flow and additional login configuration to use it. Because Platform SSO 2.0 adds a new registration flow, the SSO extension must indicate that it supports the key service before Platform SSO can use the service.

The key service registers encryption keys that can unlock the Mac at the login window and screensaver unlock. The key service handles two request types: key creation and Diffie-Hellman key exchange. Platform SSO sends the request to create the key after the user registration call to the SSO extension completes successfully. The system then binds the key to the user’s account and performs multiple key exchange requests during this time. You can use the key service only with shared device keys because it must function before a user unlocks their key bag.

## Migrate from user keys to shared keys

To migrate from user keys to shared keys, create new Secure Enclave–backed keys and register them with the server. The system calls device registration on the SSO extension with the [`registrationDeviceKeyMigration`](/documentation/AuthenticationServices/ASAuthorizationProviderExtensionRequestOptions/registrationDeviceKeyMigration) option set. During this call only, both the user keys and the new shared keys become available. You can access them using the `loginManager.key(for:)` method. The SSO extension registers the new shared keys with the server and can use the existing user keys to provide a chain of trust.

After device registration completes successfully, the system calls user registration with the [`registrationDeviceKeyMigration`](/documentation/AuthenticationServices/ASAuthorizationProviderExtensionRequestOptions/registrationDeviceKeyMigration) option set. At this time, you should also migrate any user-specific login configuration to the [`ASAuthorizationProviderExtensionUserLoginConfiguration`](/documentation/AuthenticationServices/ASAuthorizationProviderExtensionUserLoginConfiguration). When user registration completes successfully, the system destroys the user keys and previous login configuration. For subsequent users, you repeat the same user registration flow, and the system destroys the user keys after a successful response.

For more information, see [Registering devices and users](/documentation/AuthenticationServices/registering-devices-and-users).

## Use SSO tokens

Regardless of authentication method, the system stores SSO tokens in the keychain using the keychain data protection attribute <doc://com.apple.documentation/documentation/Security/kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly> and shares them only with the SSO extension.

The SSO extension then uses the SSO tokens to authenticate the user to their on-premises apps and on websites as needed. If the SSO tokens are missing, expired, or more than four hours old, Platform SSO refreshes or retrieves new tokens from the identity provider. The system can also retrieve Kerberos TGTs, import them to a credential cache, and (optionally) share them with the Kerberos SSO extension.

## Configure Platform SSO using device management

Use <doc://com.apple.documentation/documentation/DeviceManagement> to securely configure Platform SSO, including registering devices and users, configuring groups, and managing account permissions.

For more information, see <doc://com.apple.documentation/documentation/DeviceManagement/configuring-platform-single-sign-on>.

## Topics

### Essentials

[Creating extensions that support Platform SSO](/documentation/AuthenticationServices/creating-extensions-that-support-platform-sso)

Configure capabilities and authentication options for extensions.

[Registering devices and users](/documentation/AuthenticationServices/registering-devices-and-users)

Implement device and user registration.

[`ASAuthorizationProviderExtensionRegistrationHandler`](/documentation/AuthenticationServices/ASAuthorizationProviderExtensionRegistrationHandler)

An interface through which a single sign-on (SSO) authentication provider extension registers users and devices for platform SSO.

[`ASAuthorizationProviderExtensionAuthenticationMethod`](/documentation/AuthenticationServices/ASAuthorizationProviderExtensionAuthenticationMethod)

The platform single sign-on method for the user.

[`ASAuthorizationProviderExtensionRequestOptions`](/documentation/AuthenticationServices/ASAuthorizationProviderExtensionRequestOptions)

The options for the extension to obtain the status of the registration.

[`ASAuthorizationProviderExtensionRegistrationResult`](/documentation/AuthenticationServices/ASAuthorizationProviderExtensionRegistrationResult)

The registration result.

### Configuration

[Configuring authentication with the identity provider (IdP)](/documentation/AuthenticationServices/configuring-authentication-with-the-identity-provider-idp)

Specify how Platform SSO authenticates with the identity provider.

[`ASAuthorizationProviderExtensionLoginConfiguration`](/documentation/AuthenticationServices/ASAuthorizationProviderExtensionLoginConfiguration)

An interface for configuring platform single sign-on.

[`ASAuthorizationProviderExtensionLoginManager`](/documentation/AuthenticationServices/ASAuthorizationProviderExtensionLoginManager)

An interface to maintain platform single sign-on (SSO) during authentication and registration.

  <doc://com.apple.documentation/documentation/DeviceManagement/configuring-platform-single-sign-on>

### Authentication

[Authentication process](/documentation/AuthenticationServices/authentication-process)

Use a system-supported method to authenticate with an identity provider.

[Implementing web-based authentication with Platform Single Sign-on](/documentation/AuthenticationServices/implementing-web-based-authentication)

Support modern, phishing-resistant, and flexible authentication methods.

[Using access keys with Platform Single Sign-on](/documentation/AuthenticationServices/using-access-keys-with-platform-single-sign-on)

Authenticate users with access keys stored in Apple Wallet.

[`ASAuthorizationProviderExtensionKerberosMapping`](/documentation/AuthenticationServices/ASAuthorizationProviderExtensionKerberosMapping)

A set of Kerberos mappings that the system login process uses.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
