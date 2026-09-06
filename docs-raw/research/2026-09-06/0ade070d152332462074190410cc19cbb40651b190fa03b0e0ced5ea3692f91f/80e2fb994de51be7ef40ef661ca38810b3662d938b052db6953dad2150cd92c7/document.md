# Core NFC

Detect NFC tags, read messages that contain NDEF data, and save data to writable tags.

## Overview

Your app can read tags to give users more information about their physical environment and the real-world objects in it. Using Core NFC, you can read Near Field Communication (NFC) tags of types 1 through 5 that contain data in the NFC Data Exchange Format (NDEF). For example, your app might give users information about products they find in a store or exhibits they visit in a museum.

Your app can also write data to tags, and interact with protocol-specific tags such as ISO 7816, ISO 15693, FeliCa™, and MIFARE® tags.

Core NFC isn’t available for use in app extensions, and it requires a device that supports Near Field Communication. To determine if support is available, check the [`readingAvailable`](/documentation/CoreNFC/NFCReaderSession-swift.class/readingAvailable) class property before starting a reader session.

## Topics

### Essentials

[Building an NFC Tag-Reader App](/documentation/CoreNFC/building-an-nfc-tag-reader-app)

Read NFC tags with NDEF messages in your app.

[Adding Support for Background Tag Reading](/documentation/CoreNFC/adding-support-for-background-tag-reading)

Allow users to scan NFC tags without an app using background tag reading.

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NFCReaderUsageDescription>

### Reader sessions

Create a reader session to scan and detect NFC tags.

[`NFCNDEFReaderSession`](/documentation/CoreNFC/NFCNDEFReaderSession)

A reader session for detecting NFC Data Exchange Format (NDEF) tags.

[`NFCTagReaderSession`](/documentation/CoreNFC/NFCTagReaderSession)

A reader session for detecting ISO7816, ISO15693, FeliCa, and MIFARE tags.

[`NFCPaymentTagReaderSession`](/documentation/CoreNFC/NFCPaymentTagReaderSession)

A reader session that supports the use of payment tags.

[`NFCVASReaderSession`](/documentation/CoreNFC/NFCVASReaderSession)

A reader session for processing Value Added Service (VAS) tags.

[`NFCReaderSession`](/documentation/CoreNFC/NFCReaderSession-swift.class)

The abstract base class that represents a reader session for detecting NFC tags.

[`NFCReaderSessionProtocol`](/documentation/CoreNFC/NFCReaderSessionProtocol)

A general interface for interacting with a reader session.

[`NFCReaderSessionDelegate`](/documentation/CoreNFC/NFCReaderSessionDelegate)

A collection of callbacks that provide information about the status of an NFC reader session.

  <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.nfc.readersession.formats>

### Tag types

Read tag data, and save data to writable tags, by using the appropriate tag type interface.

[Creating NFC Tags from Your iPhone](/documentation/CoreNFC/creating-nfc-tags-from-your-iphone)

Save data to tags, and interact with them using native tag protocols.

[`NFCISO7816Tag`](/documentation/CoreNFC/NFCISO7816Tag)

An interface for interacting with an ISO 7816 tag.

[`NFCISO15693Tag`](/documentation/CoreNFC/NFCISO15693Tag)

An interface for interacting with an ISO 15693 tag.

[`NFCFeliCaTag`](/documentation/CoreNFC/NFCFeliCaTag)

An interface for interacting with a FeliCa™ tag.

[`NFCMiFareTag`](/documentation/CoreNFC/NFCMiFareTag)

An interface for interacting with a MIFARE® tag.

[`NFCNDEFTag`](/documentation/CoreNFC/NFCNDEFTag)

An interface for interacting with an NDEF tag.

[`NFCTag`](/documentation/CoreNFC/NFCTag-swift.enum)

An object that represents an NFC tag object.

[`NFCTag`](/documentation/CoreNFC/NFCTag-c.protocol)

An interface for interacting with an NFC or RFID tag.

[`NFCTagCommandConfiguration`](/documentation/CoreNFC/NFCTagCommandConfiguration)

A set of parameters you use to define the configuration of an NFC tag command.

### NDEF messages and payloads

[`NFCNDEFMessage`](/documentation/CoreNFC/NFCNDEFMessage)

An NFC NDEF message consisting of an array of payload records.

[`NFCNDEFPayload`](/documentation/CoreNFC/NFCNDEFPayload)

A payload record in an NFC NDEF message.

### Card sessions

[`CardSession`](/documentation/CoreNFC/CardSession)

An ISO 7816 card emulation session.

[`NFCPresentmentIntentAssertion`](/documentation/CoreNFC/NFCPresentmentIntentAssertion)

An object that signals your app’s intention to make exclusive use of the device’s contactless features.

### NFC window scenes

[`NFCWindowSceneDelegate`](/documentation/CoreNFC/NFCWindowSceneDelegate)

A protocol to notify your app’s user interface about NFC-related events.

[`NFCWindowSceneEvent`](/documentation/CoreNFC/NFCWindowSceneEvent)

An NFC-related event that your app uses to update its user interface.

### Errors

[`Code`](/documentation/CoreNFC/NFCReaderError-swift.struct/Code)

Reader session and tag error codes.

[`NFCReaderError`](/documentation/CoreNFC/NFCReaderError-swift.struct)

An error type that indicates problems with reader sessions or tags.

[`NFCErrorDomain`](/documentation/CoreNFC/NFCErrorDomain)

The domain for errors associated with Core NFC APIs.

[`NFCTagResponseUnexpectedLengthErrorKey`](/documentation/CoreNFC/NFCTagResponseUnexpectedLengthErrorKey)

A user-information dictionary key that indicates an invalid received response packet length.

### Reference

[CoreNFC Enumerations](/documentation/CoreNFC/corenfc-enumerations)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
