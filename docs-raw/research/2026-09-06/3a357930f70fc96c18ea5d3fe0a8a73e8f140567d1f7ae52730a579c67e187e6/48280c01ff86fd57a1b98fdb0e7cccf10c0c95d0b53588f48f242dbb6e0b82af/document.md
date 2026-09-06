# Local Authentication

Authenticate users biometrically or with a passphrase they already know.

## Overview

Many users rely on biometric authentication like Face ID, Touch ID, or Optic ID to enable secure, effortless access to their devices. As a fallback option, and for devices without biometry, a passcode or password serves a similar purpose. Use the LocalAuthentication framework to leverage these mechanisms in your app and extend authentication procedures your app already implements.

![Diagram showing the relationship between your app operating in user space, the LocalAuthentication framework in the operating system, and the Secure Enclave.](images/com.apple.localauthentication/media-3002744@2x.png)

To maximize security, your app never gains access to any of the underlying authentication data. You can’t access any fingerprint images, for example. The Secure Enclave, a hardware-based security processor isolated from the rest of the system, manages this data out of reach even of the operating system. Instead, you specify a particular policy and provide messaging that tells the user why you want them to authenticate. The framework then coordinates with the Secure Enclave to carry out the operation. Afterward, you receive only a Boolean result indicating authentication success or failure.

## Topics

### Essentials

[Logging a User into Your App with Face ID or Touch ID](/documentation/LocalAuthentication/logging-a-user-into-your-app-with-face-id-or-touch-id)

Supplement your own authentication scheme with biometric authentication, making it easy for users to access sensitive parts of your app.

[Accessing Keychain Items with Face ID or Touch ID](/documentation/LocalAuthentication/accessing-keychain-items-with-face-id-or-touch-id)

Protect a keychain item with biometric authentication.

### Authentication and access

[`LARight`](/documentation/LocalAuthentication/LARight)

A grouped set of requirements that gate access to a resource or operation.

[`State`](/documentation/LocalAuthentication/LARight/State-swift.enum)

The possible states for a right during authorization.

[`LAContext`](/documentation/LocalAuthentication/LAContext)

A mechanism for evaluating authentication policies and access controls.

### Persistence

[`LARightStore`](/documentation/LocalAuthentication/LARightStore)

A container for data protected by a right.

[`LAPersistedRight`](/documentation/LocalAuthentication/LAPersistedRight)

A right that gates access to a key and a secret.

[`LASecret`](/documentation/LocalAuthentication/LASecret)

Data that’s protected by a persisted right.

### Key pairs

[`LAPublicKey`](/documentation/LocalAuthentication/LAPublicKey)

The public portion of an asymmetric key pair.

[`LAPrivateKey`](/documentation/LocalAuthentication/LAPrivateKey)

The private portion of an asymmetric key pair.

### Requirements

[`LAAuthenticationRequirement`](/documentation/LocalAuthentication/LAAuthenticationRequirement)

A set of requirements that protect a right.

[`LABiometryFallbackRequirement`](/documentation/LocalAuthentication/LABiometryFallbackRequirement)

A set of requirements to fall back on if biometrics aren’t present.

### Authentication views

[`LocalAuthenticationView`](/documentation/LocalAuthentication/LocalAuthenticationView)

A SwiftUI view that displays an authentication interface.

### Errors

[`LAError`](/documentation/LocalAuthentication/LAError-swift.struct)

Errors issued by the LocalAuthentication framework.

[`Code`](/documentation/LocalAuthentication/LAError-swift.struct/Code)

Errors issued by the LocalAuthentication framework.

[`LAErrorDomain`](/documentation/LocalAuthentication/LAErrorDomain)

The error domain that the framework uses when issuing errors.

### Reference

[LocalAuthentication Constants](/documentation/LocalAuthentication/localauthentication-constants)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
