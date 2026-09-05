* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/authenticationservices#app-main)

Framework

# Authentication Services

Make it easy for users to log into apps and services.

iOS 12.0+iPadOS 12.0+Mac Catalyst 13.0+macOS 10.15+tvOS 13.0+visionOS 1.0+watchOS 6.0+

## [Overview](https://developer.apple.com/documentation/authenticationservices\#overview)

Use the Authentication Services framework to improve the experience of users when they enter credentials to establish their identity.

- Give users the ability to sign into your services with their Apple ID.

- Enable users to look up their stored passwords from within the sign-in flow of an app.

- Provide a passwordless registration and authentication workflow for apps and websites using iCloud Keychain or a physical security key.

- Perform automatic security upgrades from weak to strong passwords, or upgrade to using Sign in with Apple.

- Share data between an app and a web browser using technologies like OAuth to leverage existing web-based logins in the app.

- Create a single sign-on (SSO) experience in an enterprise app.


Simple and straightforward sign-up and sign-in flows reduce the burden on the user to remember passwords, which may improve security.

## [Topics](https://developer.apple.com/documentation/authenticationservices\#topics)

### [Authorization requests](https://developer.apple.com/documentation/authenticationservices\#Authorization-requests)

[`class ASAuthorizationController`](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller)

A controller that manages authorization requests that a provider creates.

[`struct AuthorizationController`](https://developer.apple.com/documentation/authenticationservices/authorizationcontroller)

A SwiftUI environment value that views use to perform authorization requests.

[`enum ASAuthorizationResult`](https://developer.apple.com/documentation/authenticationservices/asauthorizationresult)

Describes the outcome of a successful authorization request.

### [Sign In with Apple](https://developer.apple.com/documentation/authenticationservices\#Sign-In-with-Apple)

[Implementing User Authentication with Sign in with Apple](https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple)

Provide a way for users of your app to set up an account and start using your services.

[Simplifying User Authentication in a tvOS App](https://developer.apple.com/documentation/authenticationservices/simplifying-user-authentication-in-a-tvos-app)

Build a fluid sign-in experience for your tvOS apps using AuthenticationServices.

[`struct SignInWithAppleButton`](https://developer.apple.com/documentation/authenticationservices/signinwithapplebutton)

A SwiftUI view that creates the Sign in with Apple button for display.

[`Sign in with Apple Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.applesignin)

An entitlement that lets your app use Sign in with Apple.

[`class ASAuthorizationAppleIDProvider`](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidprovider)

A mechanism for generating requests to authenticate users based on their Apple ID.

[`class ASAuthorizationAppleIDCredential`](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential)

A credential that results from a successful Apple ID authentication.

### [Passwords](https://developer.apple.com/documentation/authenticationservices\#Passwords)

[API Reference\\
Password AutoFill](https://developer.apple.com/documentation/security/password-autofill)

Streamline your app’s login and onboarding procedures.

[`class ASAuthorizationPasswordProvider`](https://developer.apple.com/documentation/authenticationservices/asauthorizationpasswordprovider)

A mechanism for generating requests to perform keychain credential sharing.

[`class ASPasswordCredential`](https://developer.apple.com/documentation/authenticationservices/aspasswordcredential)

A password credential.

[API Reference\\
Password use in web browsers](https://developer.apple.com/documentation/authenticationservices/password-use-in-web-browsers)

Register and authenticate website users by using passwords.

### [Passkeys](https://developer.apple.com/documentation/authenticationservices\#Passkeys)

[API Reference\\
Public-Private Key Authentication](https://developer.apple.com/documentation/authenticationservices/public-private-key-authentication)

Register and authenticate users with passkeys and security keys, without using passwords.

[API Reference\\
Passkey use in web browsers](https://developer.apple.com/documentation/authenticationservices/passkey-use-in-web-browsers)

Register and authenticate website users by using passkeys.

[Performing fast account creation with passkeys](https://developer.apple.com/documentation/authenticationservices/performing-fast-account-creation-with-passkeys)

Allow people to quickly create an account with passkeys and associated domains.

[Connecting to a service with passkeys](https://developer.apple.com/documentation/authenticationservices/connecting-to-a-service-with-passkeys)

Allow users to sign in to a service without typing a password.

### [Web authentication sessions](https://developer.apple.com/documentation/authenticationservices\#Web-authentication-sessions)

[Authenticating a User Through a Web Service](https://developer.apple.com/documentation/authenticationservices/authenticating-a-user-through-a-web-service)

Use a web authentication session to authenticate a user in your app.

[Securing Logins with iCloud Keychain Verification Codes](https://developer.apple.com/documentation/authenticationservices/securing-logins-with-icloud-keychain-verification-codes)

Use time-based codes generated on-device for a secure authentication experience.

[`class ASWebAuthenticationSession`](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession)

A session that an app uses to authenticate a user through a web service.

[`struct WebAuthenticationSession`](https://developer.apple.com/documentation/authenticationservices/webauthenticationsession)

A SwiftUI environment value that views use to authenticate someone using a web service.

[Supporting Single Sign-On in a Web Browser App](https://developer.apple.com/documentation/authenticationservices/supporting-single-sign-on-in-a-web-browser-app)

Extend your web browser app to handle web authentication requests from other apps.

[`class ASWebAuthenticationSessionWebBrowserSessionManager`](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionwebbrowsersessionmanager)

A session manager that mediates sharing data between an app and a web browser.

[`ASWebAuthenticationSessionWebBrowserSupportCapabilities`](https://developer.apple.com/documentation/bundleresources/information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities)

A collection of keys that a browser app uses to declare its ability to handle authentication requests from other apps.

### [AutoFill credentials](https://developer.apple.com/documentation/authenticationservices\#AutoFill-credentials)

[Providing one-time passcodes to AutoFill](https://developer.apple.com/documentation/authenticationservices/providing-one-time-passcodes-to-autofill)

Help people efficiently perform multifactor authentication.

[`AutoFill Credential Provider Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.authentication-services.autofill-credential-provider)

A Boolean value that indicates whether the app may, with user permission, provide user names and passwords for AutoFill in Safari and other apps.

[`class ASCredentialProviderViewController`](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller)

A view controller that a credential manager app uses to extend AutoFill.

### [Credential migration](https://developer.apple.com/documentation/authenticationservices\#Credential-migration)

[`class ASCredentialExportManager`](https://developer.apple.com/documentation/authenticationservices/ascredentialexportmanager)

A class to manage exporting credentials.

[`class ASCredentialImportManager`](https://developer.apple.com/documentation/authenticationservices/ascredentialimportmanager)

A class to manage importing credentials.

### [Single sign-on (SSO)](https://developer.apple.com/documentation/authenticationservices\#Single-sign-on-SSO)

[API Reference\\
Enterprise single sign-on (SSO)](https://developer.apple.com/documentation/authenticationservices/enterprise-single-sign-on-sso)

[API Reference\\
Platform Single Sign-on (SSO)](https://developer.apple.com/documentation/authenticationservices/platform-single-sign-on-sso)

Provide a Platform Single Sign-on (Platform SSO) extension to integrate your identity provider with macOS.

### [Apple TV authentication](https://developer.apple.com/documentation/authenticationservices\#Apple-TV-authentication)

[`var customAuthorizationMethods: [ASAuthorizationCustomMethod]`](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/customauthorizationmethods)

An array of custom authorization methods for the user to choose.

[`func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)`](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontrollerdelegate/authorizationcontroller(_:didcompletewithcustommethod:))

Informs the delegate when authorization completes, and specifies the custom method the user selected.

[`struct ASAuthorizationCustomMethod`](https://developer.apple.com/documentation/authenticationservices/asauthorizationcustommethod)

The custom authorization method.

### [Automatic security upgrades](https://developer.apple.com/documentation/authenticationservices\#Automatic-security-upgrades)

[Upgrading Account Security With an Account Authentication Modification Extension](https://developer.apple.com/documentation/authenticationservices/upgrading-account-security-with-an-account-authentication-modification-extension)

Automatically and transparently convert accounts to Sign in with Apple or to use strong passwords for improved security.

[`class ASAccountAuthenticationModificationController`](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationcontroller)

An object that performs a request to modify an account’s authentication properties.

[`class ASAccountAuthenticationModificationViewController`](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationviewcontroller)

A view controller that can upgrade user passwords to strong passwords, or convert accounts to use Sign in with Apple.

[`class ASAccountAuthenticationModificationExtensionContext`](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationextensioncontext)

An object that you interact with to change an account’s password or to upgrade to Sign in with Apple.

### [Updating credential managers](https://developer.apple.com/documentation/authenticationservices\#Updating-credential-managers)

[`class ASCredentialUpdater`](https://developer.apple.com/documentation/authenticationservices/ascredentialupdater)

A class to pass credential update events to credential managers enabled on the system.

Deprecated

### [Reference](https://developer.apple.com/documentation/authenticationservices\#Reference)

[API Reference\\
AuthenticationServices Enumerations](https://developer.apple.com/documentation/authenticationservices/authenticationservices-enumerations)

[API Reference\\
AuthenticationServices Data Types](https://developer.apple.com/documentation/authenticationservices/authenticationservices-data-types)

### [Classes](https://developer.apple.com/documentation/authenticationservices\#Classes)

[`class ASAuthorizationAccountCreationPlatformPublicKeyCredential`](https://developer.apple.com/documentation/authenticationservices/asauthorizationaccountcreationplatformpublickeycredential)

[`class ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest`](https://developer.apple.com/documentation/authenticationservices/asauthorizationaccountcreationplatformpublickeycredentialrequest)

[`class ASAuthorizationAccountCreationProvider`](https://developer.apple.com/documentation/authenticationservices/asauthorizationaccountcreationprovider)

[`class ASAuthorizationProviderExtensionUserLoginConfiguration`](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionuserloginconfiguration)

[`class ASCredentialDataManager`](https://developer.apple.com/documentation/authenticationservices/ascredentialdatamanager)

This class allows submitting credentials and events to any credential manager enabled on the system.

[`class ASDeliveredVerificationCodesManager`](https://developer.apple.com/documentation/authenticationservices/asdeliveredverificationcodesmanager)

This class allows interacting with one-time codes delivered to the system.

Beta

[`class ASGeneratePasswordsRequest`](https://developer.apple.com/documentation/authenticationservices/asgeneratepasswordsrequest)

[`class ASGeneratedPassword`](https://developer.apple.com/documentation/authenticationservices/asgeneratedpassword)

[`class ASOneTimeCodeCredentialIdentity`](https://developer.apple.com/documentation/authenticationservices/asonetimecodecredentialidentity)

[`class ASSavePasswordRequest`](https://developer.apple.com/documentation/authenticationservices/assavepasswordrequest)

### [Structures](https://developer.apple.com/documentation/authenticationservices\#Structures)

[`struct ASAuthorizationProviderExtensionEncryptionAlgorithm`](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionencryptionalgorithm)

[`struct ASAuthorizationProviderExtensionSigningAlgorithm`](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionsigningalgorithm)

[`struct ASAutoFillURLScope`](https://developer.apple.com/documentation/authenticationservices/asautofillurlscope)

This structure represents the subset of URL components supported for the AutoFill of credentials.

[`struct ASEmailIdentifier`](https://developer.apple.com/documentation/authenticationservices/asemailidentifier)

[`struct ASImportableCredentialScope`](https://developer.apple.com/documentation/authenticationservices/asimportablecredentialscope)

The scope for where a credential should be usable.

[`struct ASImportableEditableField`](https://developer.apple.com/documentation/authenticationservices/asimportableeditablefield)

A field that someone can edit within a credential.

[`struct ASImportableFIDO2Extensions`](https://developer.apple.com/documentation/authenticationservices/asimportablefido2extensions)

A representation of FIDO2 extensions as defined in CXF.

[`struct ASImportableFIDO2HMACCredential`](https://developer.apple.com/documentation/authenticationservices/asimportablefido2hmaccredential)

A representation of FIDO2 HMAC Credentials as defined in CXF.

[`struct ASImportableFIDO2LargeBlob`](https://developer.apple.com/documentation/authenticationservices/asimportablefido2largeblob)

A representation of FIDO2 LargeBlob extensions as defined in CXF.

[`struct ASPhoneNumberIdentifier`](https://developer.apple.com/documentation/authenticationservices/asphonenumberidentifier)

[`struct ASPublicKeyCredentialClientData`](https://developer.apple.com/documentation/authenticationservices/aspublickeycredentialclientdata-swift.struct)

[`struct ASVerificationCode`](https://developer.apple.com/documentation/authenticationservices/asverificationcode)

This is an instance of a verification code.

Beta

[`struct CredentialDataManager`](https://developer.apple.com/documentation/authenticationservices/credentialdatamanager)

[`struct DeliveredVerificationCodesManager`](https://developer.apple.com/documentation/authenticationservices/deliveredverificationcodesmanager) Beta

### [Variables](https://developer.apple.com/documentation/authenticationservices\#Variables)

[`let ASCredentialExchangeActivity: String`](https://developer.apple.com/documentation/authenticationservices/ascredentialexchangeactivity)

The activity type used in user activity objects sent to importing apps.

[`let ASCredentialImportToken: String`](https://developer.apple.com/documentation/authenticationservices/ascredentialimporttoken)

The key for the token in the user info dictionary of the user activity sent to importing apps.

### [Enumerations](https://developer.apple.com/documentation/authenticationservices\#Enumerations)

[`enum ASContactIdentifier`](https://developer.apple.com/documentation/authenticationservices/ascontactidentifier)

[`enum ASContactIdentifierRequest`](https://developer.apple.com/documentation/authenticationservices/ascontactidentifierrequest)

[`enum ASImportableExtension`](https://developer.apple.com/documentation/authenticationservices/asimportableextension)

A representation of CXF extensions.

Current page is Authentication Services