# System Extensions

Install and manage user space code that extends the capabilities of macOS.

## Overview

Extend the capabilities of macOS by installing and managing system extensions—drivers and other low-level code—in user space rather than in the kernel. By running in user space, system extensions can’t compromise the security or stability of macOS. The system grants these extensions a high level of privilege, so they can perform the kinds of tasks previously reserved for kernel extensions (KEXTs).

You use frameworks like <doc://com.apple.documentation/documentation/DriverKit>, <doc://com.apple.documentation/documentation/EndpointSecurity>, and <doc://com.apple.documentation/documentation/NetworkExtension> to write your system extension, and you package the extension in your app bundle. At runtime, use the SystemExtensions framework to install or update the extension on the user’s system. Once installed, an extension remains available for all users on the system. Users can disable the extension by deleting the app, which deletes the extension.

### Configure the system extension and the host app

To successfully activate your extension, you must adhere to the following rules:

- The extension must match your bundle identifier, excluding file extension. For example, a DriverKit extension with bundle identifier `com.example.usbdriver` must use the filename `com.example.usbdriver.dext`. Similarly, a NetworkExtension extension with bundle identifier `com.example.networkextension` must use the filename `com.example.networkextension.systemextension`.
- You must use the same Team ID when signing the extension that you use for signing your app, unless the extension has the `com.apple.developer.system-extension.redistributable` entitlement.
- You must either distribute your app and extension through the Mac App Store, or notarize them. See <doc://com.apple.documentation/documentation/Security/notarizing-macos-software-before-distribution> to learn more about notarization.

## Topics

### Essentials

[Implementing drivers, system extensions, and kexts](/documentation/SystemExtensions/implementing-drivers-system-extensions-and-kexts)

Create drivers and system extensions to communicate with hardware and provide low-level services, and only use kernel extensions for a few tasks.

  <doc://com.apple.documentation/documentation/DriverKit/debugging-and-testing-system-extensions>

  <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.system-extension.install>

### Usage descriptions

[`NSSystemExtensionUsageDescriptionKey`](/documentation/SystemExtensions/NSSystemExtensionUsageDescriptionKey)

A message that tells the user why the app is trying to install a system extension bundle.

[`OSBundleUsageDescriptionKey`](/documentation/SystemExtensions/OSBundleUsageDescriptionKey)

A message that tells the user why the app is trying to install a driver extension bundle.

### Extension activation and deactivation

[Installing System Extensions and Drivers](/documentation/SystemExtensions/installing-system-extensions-and-drivers)

Activate system extensions and drivers to make them available to the system, and update or deactivate them as needed.

[`OSSystemExtensionManager`](/documentation/SystemExtensions/OSSystemExtensionManager)

A type that facilitates activation and deactivation of system extensions.

[`OSSystemExtensionRequest`](/documentation/SystemExtensions/OSSystemExtensionRequest)

A request to activate or deactivate a system extension.

  <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.system-extension.redistributable>

### Errors

[`OSSystemExtensionError`](/documentation/SystemExtensions/OSSystemExtensionError)

An error that describes a failed extension manager request.

[`Code`](/documentation/SystemExtensions/OSSystemExtensionError/Code)

Error codes for system extensions.

[`OSSystemExtensionErrorDomain`](/documentation/SystemExtensions/OSSystemExtensionErrorDomain)

The error domain identifying system extension errors.

### Reference

[SystemExtensions Constants](/documentation/SystemExtensions/systemextensions-constants)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
