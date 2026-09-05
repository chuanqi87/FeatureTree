* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/corenfc#app-main)

Framework

# Core NFC

Detect NFC tags, read messages that contain NDEF data, and save data to writable tags.

iOS 11.0+iPadOS 11.0+Mac Catalyst 13.1+

## [Overview](https://developer.apple.com/documentation/corenfc\#overview)

Your app can read tags to give users more information about their physical environment and the real-world objects in it. Using Core NFC, you can read Near Field Communication (NFC) tags of types 1 through 5 that contain data in the NFC Data Exchange Format (NDEF). For example, your app might give users information about products they find in a store or exhibits they visit in a museum.

Your app can also write data to tags, and interact with protocol-specific tags such as ISO 7816, ISO 15693, FeliCa™, and MIFARE® tags.

Core NFC isn’t available for use in app extensions, and it requires a device that supports Near Field Communication. To determine if support is available, check the [`readingAvailable`](https://developer.apple.com/documentation/corenfc/nfcreadersession-swift.class/readingavailable) class property before starting a reader session.

## [Topics](https://developer.apple.com/documentation/corenfc\#topics)

### [Essentials](https://developer.apple.com/documentation/corenfc\#Essentials)

[Building an NFC Tag-Reader App](https://developer.apple.com/documentation/corenfc/building-an-nfc-tag-reader-app)

Read NFC tags with NDEF messages in your app.

[Adding Support for Background Tag Reading](https://developer.apple.com/documentation/corenfc/adding-support-for-background-tag-reading)

Allow users to scan NFC tags without an app using background tag reading.

[`NFCReaderUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nfcreaderusagedescription)

A message that tells people why the app is requesting access to the device’s NFC hardware.

### [Reader sessions](https://developer.apple.com/documentation/corenfc\#Reader-sessions)

Create a reader session to scan and detect NFC tags.

[`class NFCNDEFReaderSession`](https://developer.apple.com/documentation/corenfc/nfcndefreadersession)

A reader session for detecting NFC Data Exchange Format (NDEF) tags.

[`class NFCTagReaderSession`](https://developer.apple.com/documentation/corenfc/nfctagreadersession)

A reader session for detecting ISO7816, ISO15693, FeliCa, and MIFARE tags.

[`class NFCPaymentTagReaderSession`](https://developer.apple.com/documentation/corenfc/nfcpaymenttagreadersession)

A reader session that supports the use of payment tags.

[`class NFCVASReaderSession`](https://developer.apple.com/documentation/corenfc/nfcvasreadersession)

A reader session for processing Value Added Service (VAS) tags.

[`class NFCReaderSession`](https://developer.apple.com/documentation/corenfc/nfcreadersession-swift.class)

The abstract base class that represents a reader session for detecting NFC tags.

[`protocol NFCReaderSessionProtocol`](https://developer.apple.com/documentation/corenfc/nfcreadersessionprotocol)

A general interface for interacting with a reader session.

[`Near Field Communication Tag Reader Session Formats Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.nfc.readersession.formats)

The Near Field Communication data formats an app can read.

### [Tag types](https://developer.apple.com/documentation/corenfc\#Tag-types)

Read tag data, and save data to writable tags, by using the appropriate tag type interface.

[Creating NFC Tags from Your iPhone](https://developer.apple.com/documentation/corenfc/creating-nfc-tags-from-your-iphone)

Save data to tags, and interact with them using native tag protocols.

[`protocol NFCISO7816Tag`](https://developer.apple.com/documentation/corenfc/nfciso7816tag)

An interface for interacting with an ISO 7816 tag.

[`protocol NFCISO15693Tag`](https://developer.apple.com/documentation/corenfc/nfciso15693tag)

An interface for interacting with an ISO 15693 tag.

[`protocol NFCFeliCaTag`](https://developer.apple.com/documentation/corenfc/nfcfelicatag)

An interface for interacting with a FeliCa™ tag.

[`protocol NFCMiFareTag`](https://developer.apple.com/documentation/corenfc/nfcmifaretag)

An interface for interacting with a MIFARE® tag.

[`protocol NFCNDEFTag`](https://developer.apple.com/documentation/corenfc/nfcndeftag)

An interface for interacting with an NDEF tag.

[`enum NFCTag`](https://developer.apple.com/documentation/corenfc/nfctag-swift.enum)

An object that represents an NFC tag object.

[`class NFCTagCommandConfiguration`](https://developer.apple.com/documentation/corenfc/nfctagcommandconfiguration)

A set of parameters you use to define the configuration of an NFC tag command.

### [NDEF messages and payloads](https://developer.apple.com/documentation/corenfc\#NDEF-messages-and-payloads)

[`class NFCNDEFMessage`](https://developer.apple.com/documentation/corenfc/nfcndefmessage)

An NFC NDEF message consisting of an array of payload records.

[`class NFCNDEFPayload`](https://developer.apple.com/documentation/corenfc/nfcndefpayload)

A payload record in an NFC NDEF message.

### [Card sessions](https://developer.apple.com/documentation/corenfc\#Card-sessions)

[`class CardSession`](https://developer.apple.com/documentation/corenfc/cardsession)

An ISO 7816 card emulation session.

[`class NFCPresentmentIntentAssertion`](https://developer.apple.com/documentation/corenfc/nfcpresentmentintentassertion)

An object that signals your app’s intention to make exclusive use of the device’s contactless features.

### [NFC window scenes](https://developer.apple.com/documentation/corenfc\#NFC-window-scenes)

[`protocol NFCWindowSceneDelegate`](https://developer.apple.com/documentation/corenfc/nfcwindowscenedelegate)

A protocol to notify your app’s user interface about NFC-related events.

[`enum NFCWindowSceneEvent`](https://developer.apple.com/documentation/corenfc/nfcwindowsceneevent)

An NFC-related event that your app uses to update its user interface.

### [Errors](https://developer.apple.com/documentation/corenfc\#Errors)

[`enum Code`](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/code)

Reader session and tag error codes.

[`struct NFCReaderError`](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct)

An error type that indicates problems with reader sessions or tags.

[`let NFCErrorDomain: String`](https://developer.apple.com/documentation/corenfc/nfcerrordomain)

The domain for errors associated with Core NFC APIs.

[`let NFCTagResponseUnexpectedLengthErrorKey: String`](https://developer.apple.com/documentation/corenfc/nfctagresponseunexpectedlengtherrorkey)

A user-information dictionary key that indicates an invalid received response packet length.

### [Reference](https://developer.apple.com/documentation/corenfc\#Reference)

[API Reference\\
CoreNFC Enumerations](https://developer.apple.com/documentation/corenfc/corenfc-enumerations)

### [Classes](https://developer.apple.com/documentation/corenfc\#Classes)

[`class NFCISO15693CustomCommandConfiguration`](https://developer.apple.com/documentation/corenfc/nfciso15693customcommandconfiguration)

[`class NFCISO15693ReadMultipleBlocksConfiguration`](https://developer.apple.com/documentation/corenfc/nfciso15693readmultipleblocksconfiguration)

### [Structures](https://developer.apple.com/documentation/corenfc\#Structures)

[`struct NFCFeliCaPollingResponse`](https://developer.apple.com/documentation/corenfc/nfcfelicapollingresponse)

[`struct NFCFeliCaRequestSpecificationVersionResponse`](https://developer.apple.com/documentation/corenfc/nfcfelicarequestspecificationversionresponse)

[`struct NFCFeliCaRequsetServiceV2Response`](https://developer.apple.com/documentation/corenfc/nfcfelicarequsetservicev2response)

[`struct NFCFeliCaStatusFlag`](https://developer.apple.com/documentation/corenfc/nfcfelicastatusflag)

[`struct NFCISO15693MultipleBlockSecurityStatus`](https://developer.apple.com/documentation/corenfc/nfciso15693multipleblocksecuritystatus)

[`struct NFCISO15693SystemInfo`](https://developer.apple.com/documentation/corenfc/nfciso15693systeminfo)

Current page is Core NFC