* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/security#app-main)

Framework

# Security

Secure the data your app manages, and control access to your app.

iOS 2.0+iPadOS 2.0+Mac Catalyst 13.0+macOS 10.0+tvOS 9.0+visionOS 1.0+watchOS 2.0+

## [Overview](https://developer.apple.com/documentation/security\#overview)

Use the Security framework to protect information, establish trust, and control access to software. Broadly, security services support these goals:

- Establish a user’s identity (authentication) and then selectively grant access to resources (authorization).

- Secure data, both on disk and in motion across a network connection.

- Ensure the validity of code to be executed for a particular purpose.


As shown in the image below, you can also use lower level cryptographic resources to create new secure services. Cryptography is difficult and the cost of bugs typically so high that it’s rarely a good idea to implement your own cryptography solution. Rely on the Security framework when you need cryptography in your app.

![Diagram showing your app sitting above the Security framework, which provides tools to enable secure interaction with users, data, and code.](https://developer.apple.com/tutorials/images/com.apple.security/media-2891898@2x.png)

## [Topics](https://developer.apple.com/documentation/security\#topics)

### [Essentials](https://developer.apple.com/documentation/security\#Essentials)

[Security updates](https://developer.apple.com/documentation/updates/security)

Learn about important changes to Security.

### [Authorization and authentication](https://developer.apple.com/documentation/security\#Authorization-and-authentication)

[API Reference\\
Password AutoFill](https://developer.apple.com/documentation/security/password-autofill)

Streamline your app’s login and onboarding procedures.

[API Reference\\
Shared Web Credentials](https://developer.apple.com/documentation/security/shared-web-credentials)

Share credentials between iOS apps and their website counterparts.

[API Reference\\
Authorization Services](https://developer.apple.com/documentation/security/authorization-services)

Access restricted areas of the operating system, and control access to particular features of your macOS app.

[API Reference\\
Authorization Plug-ins](https://developer.apple.com/documentation/security/authorization-plug-ins)

Extend the authorization services API by creating plug-ins that can participate in authorization decisions.

[API Reference\\
Sessions](https://developer.apple.com/documentation/security/sessions)

Manage login, authorization, and security sessions in macOS.

[API Reference\\
One-time codes](https://developer.apple.com/documentation/security/one-time-codes)

Streamline entry of authentication and recovery codes.

### [Secure data](https://developer.apple.com/documentation/security\#Secure-data)

[API Reference\\
Keychain services](https://developer.apple.com/documentation/security/keychain-services)

Securely store small chunks of data on behalf of the user.

[API Reference\\
Preventing Insecure Network Connections](https://developer.apple.com/documentation/security/preventing-insecure-network-connections)

Enforce secure network links in your app by relying on App Transport Security.

### [Secure code](https://developer.apple.com/documentation/security\#Secure-code)

[API Reference\\
Code Signing Services](https://developer.apple.com/documentation/security/code-signing-services)

Examine and validate signed code running on the system.

[API Reference\\
Notarizing macOS software before distribution](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution)

Give users even more confidence in your macOS software by submitting it to Apple for notarization.

[Preparing your app to work with pointer authentication](https://developer.apple.com/documentation/security/preparing-your-app-to-work-with-pointer-authentication)

Test your app against the arm64e architecture to ensure that it works seamlessly with enhanced security features.

[API Reference\\
App Sandbox](https://developer.apple.com/documentation/security/app-sandbox)

Restrict access to system resources and user data in macOS apps to contain damage if an app becomes compromised.

[API Reference\\
Hardened Runtime](https://developer.apple.com/documentation/security/hardened-runtime)

Manage security protections and resource access for your macOS apps.

[Disabling and Enabling System Integrity Protection](https://developer.apple.com/documentation/security/disabling-and-enabling-system-integrity-protection)

Disable system protections only temporarily during development to test drivers, kernel extensions, and other low-level code.

[Using the latest code signature format](https://developer.apple.com/documentation/xcode/using-the-latest-code-signature-format)

Update legacy app code signatures so your app runs on current OS releases.

[Updating Mac Software](https://developer.apple.com/documentation/security/updating-mac-software)

Implement Mac software updates without causing code-signing crashes.

[TN3125: Inside Code Signing: Provisioning Profiles](https://developer.apple.com/documentation/technotes/tn3125-inside-code-signing-provisioning-profiles)

Learn how provisioning profiles enable third-party code to run on Apple platforms.

### [Launch environment constraints](https://developer.apple.com/documentation/security\#Launch-environment-constraints)

[Applying launch environment and library constraints](https://developer.apple.com/documentation/security/applying-launch-environment-and-library-constraints)

Limit the libraries your process loads, and the situations where it runs.

[Defining launch environment and library constraints](https://developer.apple.com/documentation/security/defining-launch-environment-and-library-constraints)

Restrict your app’s components to their expected contexts.

[Constraining a tool’s launch environment](https://developer.apple.com/documentation/security/constraining-a-tool's-launch-environment)

Improve the security of your macOS app by limiting the ways its components can run.

### [Cryptography](https://developer.apple.com/documentation/security\#Cryptography)

[API Reference\\
Complying with Encryption Export Regulations](https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations)

Declare the use of encryption in your app to streamline the app submission process.

[API Reference\\
Certificate, Key, and Trust Services](https://developer.apple.com/documentation/security/certificate-key-and-trust-services)

Establish trust using certificates and cryptographic keys.

[API Reference\\
Cryptographic Message Syntax Services](https://developer.apple.com/documentation/security/cryptographic-message-syntax-services)

Cryptographically sign and encrypt S/MIME messages.

[API Reference\\
Randomization Services](https://developer.apple.com/documentation/security/randomization-services)

Generate cryptographically secure random numbers.

[API Reference\\
Security Transforms](https://developer.apple.com/documentation/security/security-transforms)

Perform cryptographic functions like encoding, encryption, signing, and signature verification.

[API Reference\\
ASN.1](https://developer.apple.com/documentation/security/asn-1)

Encode and decode Distinguished Encoding Rules (DER) and Basic Encoding Rules (BER) data streams.

### [Result codes](https://developer.apple.com/documentation/security\#Result-codes)

[API Reference\\
Security Framework Result Codes](https://developer.apple.com/documentation/security/security-framework-result-codes)

Evaluate result codes common to many Security framework functions.

### [Legacy interfaces](https://developer.apple.com/documentation/security\#Legacy-interfaces)

[API Reference\\
Common Security Services Manager](https://developer.apple.com/documentation/security/common-security-services-manager)

A set of open source modules underpinning the legacy implementation of the Security framework.

[API Reference\\
Secure Transport](https://developer.apple.com/documentation/security/secure-transport)

Secure network communication using standardized transport layer security mechanisms.

[API Reference\\
Secure Download](https://developer.apple.com/documentation/security/secure-download)

Implement Apple’s Secure Download System in macOS.

[API Reference\\
Security legacy reference](https://developer.apple.com/documentation/security/security-legacy-reference)

Learn about legacy APIs.

### [Reference](https://developer.apple.com/documentation/security\#Reference)

[API Reference\\
Security Structures](https://developer.apple.com/documentation/security/security-structures)

[API Reference\\
Security Constants](https://developer.apple.com/documentation/security/security-constants)

[API Reference\\
Security Functions](https://developer.apple.com/documentation/security/security-functions)

[API Reference\\
Security Data Types](https://developer.apple.com/documentation/security/security-data-types)

### [Variables](https://developer.apple.com/documentation/security\#Variables)

[`var CSSM_APPLE_PRIVATE_CSPDL_CODE_28: Int`](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_28)

[`var TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256: SSLCipherSuite`](https://developer.apple.com/documentation/security/tls_ecdhe_psk_with_chacha20_poly1305_sha256)

[`var errSecCSDetachedCertificates: OSStatus`](https://developer.apple.com/documentation/security/errseccsdetachedcertificates)

[`var errSecCSMultipleSelfSigning: OSStatus`](https://developer.apple.com/documentation/security/errseccsmultipleselfsigning)

[`var errSecCSRemoteSignerFirstSlotFull: OSStatus`](https://developer.apple.com/documentation/security/errseccsremotesignerfirstslotfull)

[`var errSecCSRemoteSignerSecondSlotFull: OSStatus`](https://developer.apple.com/documentation/security/errseccsremotesignersecondslotfull)

[`var errSecCSUnsupportedAlgorithm: OSStatus`](https://developer.apple.com/documentation/security/errseccsunsupportedalgorithm)

[`var errSecMissingQualifiedCertStatement: OSStatus`](https://developer.apple.com/documentation/security/errsecmissingqualifiedcertstatement)

[`let kSecCFErrorDetachedCertificates: CFString`](https://developer.apple.com/documentation/security/kseccferrordetachedcertificates)

[`var kSecCSMaxSignatures: Int`](https://developer.apple.com/documentation/security/kseccsmaxsignatures)

[`let kSecCodeInfoChosenSignature: CFString`](https://developer.apple.com/documentation/security/kseccodeinfochosensignature)

[`let kSecCodeInfoSignerInfoSKID: CFString`](https://developer.apple.com/documentation/security/kseccodeinfosignerinfoskid)

[`let kSecCodeInfoTotalSignatures: CFString`](https://developer.apple.com/documentation/security/kseccodeinfototalsignatures)

[`let kSecPolicyAppleEAPClient: CFString`](https://developer.apple.com/documentation/security/ksecpolicyappleeapclient)

[`let kSecPolicyAppleEAPServer: CFString`](https://developer.apple.com/documentation/security/ksecpolicyappleeapserver)

[`let kSecPolicyAppleIPSecClient: CFString`](https://developer.apple.com/documentation/security/ksecpolicyappleipsecclient)

[`let kSecPolicyAppleIPSecServer: CFString`](https://developer.apple.com/documentation/security/ksecpolicyappleipsecserver)

[`let kSecPolicyAppleSSLClient: CFString`](https://developer.apple.com/documentation/security/ksecpolicyapplesslclient)

[`let kSecPolicyAppleSSLServer: CFString`](https://developer.apple.com/documentation/security/ksecpolicyapplesslserver)

[`let kSecTrustQCStatements: CFString`](https://developer.apple.com/documentation/security/ksectrustqcstatements)

[`let kSecTrustQWACValidation: CFString`](https://developer.apple.com/documentation/security/ksectrustqwacvalidation)

### [Functions](https://developer.apple.com/documentation/security\#Functions)

[`func SecIdentityCreate(CFAllocator?, SecCertificate, SecKey) -> SecIdentity?`](https://developer.apple.com/documentation/security/secidentitycreate(_:_:_:))

[`func sec_protocol_metadata_copy_negotiated_protocol(sec_protocol_metadata_t) -> UnsafePointer<CChar>?`](https://developer.apple.com/documentation/security/sec_protocol_metadata_copy_negotiated_protocol(_:))

[`func sec_protocol_metadata_copy_server_name(sec_protocol_metadata_t) -> UnsafePointer<CChar>?`](https://developer.apple.com/documentation/security/sec_protocol_metadata_copy_server_name(_:))

### [Type Aliases](https://developer.apple.com/documentation/security\#Type-Aliases)

[`typealias CE_DataType`](https://developer.apple.com/documentation/security/ce_datatype-swift.typealias)

[`typealias CE_ExtendedKeyUsage`](https://developer.apple.com/documentation/security/ce_extendedkeyusage-swift.typealias)

[`typealias CE_GeneralNameType`](https://developer.apple.com/documentation/security/ce_generalnametype-swift.typealias)

Current page is Security