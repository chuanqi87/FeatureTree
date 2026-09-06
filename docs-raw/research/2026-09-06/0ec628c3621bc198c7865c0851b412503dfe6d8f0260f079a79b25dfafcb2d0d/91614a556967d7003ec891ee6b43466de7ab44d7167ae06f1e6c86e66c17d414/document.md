# NFCTag

An interface for interacting with an NFC or RFID tag.

```
@protocol NFCTag <NSObject, NSSecureCoding, NSCopying>
```

## Overview

When an NFC reader session detects a tag, it returns an object that conforms to this protocol.

## Topics

### Getting Information About a Tag

[`available`](/documentation/CoreNFC/NFCTag-c.protocol/available)

A Boolean value that indicates whether a detected tag is available.

[`session`](/documentation/CoreNFC/NFCTag-c.protocol/session)

The reader session that provides the tag.

### Getting the Tag Type

[`type`](/documentation/CoreNFC/NFCTag-c.protocol/type)

The tag type.

[`-  asNFCISO15693Tag`](/documentation/CoreNFC/NFCTag-c.protocol/asNFCISO15693Tag)

Returns the tag as an ISO 15693 tag object.

[`-  asNFCISO7816Tag`](/documentation/CoreNFC/NFCTag-c.protocol/asNFCISO7816Tag)

Returns the tag as an ISO 7816 tag object.

[`-  asNFCFeliCaTag`](/documentation/CoreNFC/NFCTag-c.protocol/asNFCFeliCaTag)

Returns the tag as a FeliCa tag object.

[`-  asNFCMiFareTag`](/documentation/CoreNFC/NFCTag-c.protocol/asNFCMiFareTag)

Returns the tag as a MIFARE tag object.

[`NFCTagType`](/documentation/CoreNFC/NFCTagType)

Constants that identify the type of an NFC tag.

## Relationships

### Inherited By

[`NFCFeliCaTag`](/documentation/CoreNFC/NFCFeliCaTag)

[`NFCISO7816Tag`](/documentation/CoreNFC/NFCISO7816Tag)

[`NFCISO15693Tag`](/documentation/CoreNFC/NFCISO15693Tag)

[`NFCMiFareTag`](/documentation/CoreNFC/NFCMiFareTag)

### Inherits From

[`NSSecureCoding`](/documentation/Foundation/NSSecureCoding)

[`NSCopying`](/documentation/Foundation/NSCopying)

[`NSObjectProtocol`](/documentation/ObjectiveC/NSObjectProtocol)

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
