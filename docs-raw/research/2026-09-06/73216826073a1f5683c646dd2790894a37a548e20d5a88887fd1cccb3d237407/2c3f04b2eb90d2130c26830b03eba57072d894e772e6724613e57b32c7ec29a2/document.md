# SMS and Call Reporting

Create app extensions to manage and report unwanted SMS messages and spam calls.

## Overview

SMS and Call Reporting provides app extensions to manage unwanted communication.

- **Message Filter app extension**: Identifies and filters unwanted SMS and MMS messages.
- **Unwanted Communication app extension**: Lets people report unwanted SMS messages and calls as spam.
- **Live Caller ID Lookup app extension**: Enables up-to-date calling and blocking information.

Register your Live Caller ID configuration on the [Identity & Trust](https://icloud.developer.apple.com/dashboard/identity) page in the [CloudKit Console](https://icloud.developer.apple.com/).

## Topics

### Message filtering

  <doc://com.apple.identitylookup/documentation/IdentityLookup/sms-and-mms-message-filtering>

### Spam reporting

  <doc://com.apple.identitylookup/documentation/IdentityLookup/sms-and-call-spam-reporting>

### Live Caller ID Lookup

  <doc://com.apple.identitylookup/documentation/IdentityLookup/understanding-how-live-caller-id-lookup-preserves-privacy>

  <doc://com.apple.identitylookup/documentation/IdentityLookup/formatting-data-for-blocking-and-identity-information>

  <doc://com.apple.identitylookup/documentation/IdentityLookup/setting-up-the-http-endpoints-for-live-caller-id-lookup>

  <doc://com.apple.identitylookup/documentation/IdentityLookup/getting-up-to-date-calling-and-blocking-information-for-your-app>

[`LiveCallerIDLookupProtocol`](/documentation/IdentityLookup/LiveCallerIDLookupProtocol)

Information the system uses to query the app extension for context.

[`LiveCallerIDLookupExtensionConfiguration`](/documentation/IdentityLookup/LiveCallerIDLookupExtensionConfiguration)

An object that allows the system to query the app extension.

[`LiveCallerIDLookupExtensionContext`](/documentation/IdentityLookup/LiveCallerIDLookupExtensionContext)

The information the system uses for configuration.

[`CallLookupExtensionStatus`](/documentation/IdentityLookup/CallLookupExtensionStatus)

Returns a value with the current state of the app extension.

[`LiveCallerIDLookupManager`](/documentation/IdentityLookup/LiveCallerIDLookupManager)

The entry point that provides access to a collection of functions that help manage the state of the Live Caller ID Lookup app extension.

### Macros

  <doc://com.apple.identitylookup/documentation/IdentityLookup/macros>



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
