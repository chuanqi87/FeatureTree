* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/localauthentication#app-main)

Framework

# Local Authentication

Authenticate users biometrically or with a passphrase they already know.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.0+macOS 10.10+visionOS 1.0+watchOS 9.0+

## [Overview](https://developer.apple.com/documentation/localauthentication\#overview)

Many users rely on biometric authentication like Face ID, Touch ID, or Optic ID to enable secure, effortless access to their devices. As a fallback option, and for devices without biometry, a passcode or password serves a similar purpose. Use the LocalAuthentication framework to leverage these mechanisms in your app and extend authentication procedures your app already implements.

![Diagram showing the relationship between your app operating in user space, the LocalAuthentication framework in the operating system, and the Secure Enclave.](https://developer.apple.com/tutorials/images/com.apple.localauthentication/media-3002744@2x.png)

To maximize security, your app never gains access to any of the underlying authentication data. You can’t access any fingerprint images, for example. The Secure Enclave, a hardware-based security processor isolated from the rest of the system, manages this data out of reach even of the operating system. Instead, you specify a particular policy and provide messaging that tells the user why you want them to authenticate. The framework then coordinates with the Secure Enclave to carry out the operation. Afterward, you receive only a Boolean result indicating authentication success or failure.

## [Topics](https://developer.apple.com/documentation/localauthentication\#topics)

### [Essentials](https://developer.apple.com/documentation/localauthentication\#Essentials)

[Logging a User into Your App with Face ID or Touch ID](https://developer.apple.com/documentation/localauthentication/logging-a-user-into-your-app-with-face-id-or-touch-id)

Supplement your own authentication scheme with biometric authentication, making it easy for users to access sensitive parts of your app.

[Accessing Keychain Items with Face ID or Touch ID](https://developer.apple.com/documentation/localauthentication/accessing-keychain-items-with-face-id-or-touch-id)

Protect a keychain item with biometric authentication.

### [Authentication and access](https://developer.apple.com/documentation/localauthentication\#Authentication-and-access)

[`class LARight`](https://developer.apple.com/documentation/localauthentication/laright)

A grouped set of requirements that gate access to a resource or operation.

[`enum State`](https://developer.apple.com/documentation/localauthentication/laright/state-swift.enum)

The possible states for a right during authorization.

[`class LAContext`](https://developer.apple.com/documentation/localauthentication/lacontext)

A mechanism for evaluating authentication policies and access controls.

### [Persistence](https://developer.apple.com/documentation/localauthentication\#Persistence)

[`class LARightStore`](https://developer.apple.com/documentation/localauthentication/larightstore)

A container for data protected by a right.

[`class LAPersistedRight`](https://developer.apple.com/documentation/localauthentication/lapersistedright)

A right that gates access to a key and a secret.

[`class LASecret`](https://developer.apple.com/documentation/localauthentication/lasecret)

Data that’s protected by a persisted right.

### [Key pairs](https://developer.apple.com/documentation/localauthentication\#Key-pairs)

[`class LAPublicKey`](https://developer.apple.com/documentation/localauthentication/lapublickey)

The public portion of an asymmetric key pair.

[`class LAPrivateKey`](https://developer.apple.com/documentation/localauthentication/laprivatekey)

The private portion of an asymmetric key pair.

### [Requirements](https://developer.apple.com/documentation/localauthentication\#Requirements)

[`class LAAuthenticationRequirement`](https://developer.apple.com/documentation/localauthentication/laauthenticationrequirement)

A set of requirements that protect a right.

[`class LABiometryFallbackRequirement`](https://developer.apple.com/documentation/localauthentication/labiometryfallbackrequirement)

A set of requirements to fall back on if biometrics aren’t present.

### [Authentication views](https://developer.apple.com/documentation/localauthentication\#Authentication-views)

[`struct LocalAuthenticationView`](https://developer.apple.com/documentation/localauthentication/localauthenticationview)

A SwiftUI view that displays an authentication interface.

### [Errors](https://developer.apple.com/documentation/localauthentication\#Errors)

[`struct LAError`](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct)

Errors issued by the LocalAuthentication framework.

[`enum Code`](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code)

Errors issued by the LocalAuthentication framework.

[`let LAErrorDomain: String`](https://developer.apple.com/documentation/localauthentication/laerrordomain)

The error domain that the framework uses when issuing errors.

### [Reference](https://developer.apple.com/documentation/localauthentication\#Reference)

[API Reference\\
LocalAuthentication Constants](https://developer.apple.com/documentation/localauthentication/localauthentication-constants)

### [Classes](https://developer.apple.com/documentation/localauthentication\#Classes)

[`class LADomainState`](https://developer.apple.com/documentation/localauthentication/ladomainstate)

[`class LADomainStateBiometry`](https://developer.apple.com/documentation/localauthentication/ladomainstatebiometry)

[`class LADomainStateCompanion`](https://developer.apple.com/documentation/localauthentication/ladomainstatecompanion)

[`class LAEnvironment`](https://developer.apple.com/documentation/localauthentication/laenvironment)

### [Variables](https://developer.apple.com/documentation/localauthentication\#Variables)

[`var kLAAccessControlOperationCreateItem: Int32`](https://developer.apple.com/documentation/localauthentication/klaaccesscontroloperationcreateitem)

[`var kLAAccessControlOperationCreateKey: Int32`](https://developer.apple.com/documentation/localauthentication/klaaccesscontroloperationcreatekey)

[`var kLAAccessControlOperationUseItem: Int32`](https://developer.apple.com/documentation/localauthentication/klaaccesscontroloperationuseitem)

[`var kLAAccessControlOperationUseKeyDecrypt: Int32`](https://developer.apple.com/documentation/localauthentication/klaaccesscontroloperationusekeydecrypt)

[`var kLAAccessControlOperationUseKeyKeyExchange: Int32`](https://developer.apple.com/documentation/localauthentication/klaaccesscontroloperationusekeykeyexchange)

[`var kLAAccessControlOperationUseKeySign: Int32`](https://developer.apple.com/documentation/localauthentication/klaaccesscontroloperationusekeysign)

[`var kLACompanionTypeMac: Int32`](https://developer.apple.com/documentation/localauthentication/klacompaniontypemac)

[`var kLACompanionTypeNone: Int32`](https://developer.apple.com/documentation/localauthentication/klacompaniontypenone)

[`var kLACompanionTypeVision: Int32`](https://developer.apple.com/documentation/localauthentication/klacompaniontypevision)

[`var kLACompanionTypeWatch: Int32`](https://developer.apple.com/documentation/localauthentication/klacompaniontypewatch)

[`var kLAErrorCompanionNotAvailable: Int32`](https://developer.apple.com/documentation/localauthentication/klaerrorcompanionnotavailable)

[`var kLAPolicyDeviceOwnerAuthenticationWithBiometricsOrCompanion: Int32`](https://developer.apple.com/documentation/localauthentication/klapolicydeviceownerauthenticationwithbiometricsorcompanion)

[`var kLAPolicyDeviceOwnerAuthenticationWithCompanion: Int32`](https://developer.apple.com/documentation/localauthentication/klapolicydeviceownerauthenticationwithcompanion)

### [Enumerations](https://developer.apple.com/documentation/localauthentication\#Enumerations)

[`enum LACompanionType`](https://developer.apple.com/documentation/localauthentication/lacompaniontype)

Current page is Local Authentication