# NFCReaderError

An error type that indicates problems with reader sessions or tags.

```
struct NFCReaderError
```

## Topics

### Session Errors

[`readerSessionInvalidationErrorFirstNDEFTagRead`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerSessionInvalidationErrorFirstNDEFTagRead)

The first NDEF tag read by this session is invalid.

[`readerSessionInvalidationErrorSessionTerminatedUnexpectedly`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerSessionInvalidationErrorSessionTerminatedUnexpectedly)

The reader session terminated unexpectedly.

[`readerSessionInvalidationErrorSessionTimeout`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerSessionInvalidationErrorSessionTimeout)

The reader session timed out.

[`readerSessionInvalidationErrorSystemIsBusy`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerSessionInvalidationErrorSystemIsBusy)

The reader session failed because the system is busy.

[`readerSessionInvalidationErrorUserCanceled`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerSessionInvalidationErrorUserCanceled)

The user canceled the reader session.

### NDEF Tag Errors

[`ndefReaderSessionErrorTagNotWritable`](/documentation/CoreNFC/NFCReaderError-swift.struct/ndefReaderSessionErrorTagNotWritable)

The NDEF tag isn’t writable.

[`ndefReaderSessionErrorTagSizeTooSmall`](/documentation/CoreNFC/NFCReaderError-swift.struct/ndefReaderSessionErrorTagSizeTooSmall)

The NDEF tag memory size is too small to store the data.

[`ndefReaderSessionErrorTagUpdateFailure`](/documentation/CoreNFC/NFCReaderError-swift.struct/ndefReaderSessionErrorTagUpdateFailure)

The reader session failed to update the NDEF tag.

[`ndefReaderSessionErrorZeroLengthMessage`](/documentation/CoreNFC/NFCReaderError-swift.struct/ndefReaderSessionErrorZeroLengthMessage)

The NDEF tag doesn’t contain an NDEF message.

### Transceive Errors

[`readerTransceiveErrorRetryExceeded`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerTransceiveErrorRetryExceeded)

Too many retries have occurred.

[`readerTransceiveErrorTagConnectionLost`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerTransceiveErrorTagConnectionLost)

The reader lost the connection to the tag.

[`readerTransceiveErrorTagNotConnected`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerTransceiveErrorTagNotConnected)

The tag isn’t in the connected state.

[`readerTransceiveErrorTagResponseError`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerTransceiveErrorTagResponseError)

The tag has responded with an error.

[`readerTransceiveErrorSessionInvalidated`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerTransceiveErrorSessionInvalidated)

The reader session is invalid.

[`readerTransceiveErrorPacketTooLong`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerTransceiveErrorPacketTooLong)

The packet length exceeds the limit supported by the tag.

### Tag Command Configuration Error

[`tagCommandConfigurationErrorInvalidParameters`](/documentation/CoreNFC/NFCReaderError-swift.struct/tagCommandConfigurationErrorInvalidParameters)

The tag has been configured with invalid parameters.

### Other Errors

[`readerErrorUnsupportedFeature`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerErrorUnsupportedFeature)

The reader session does not support this feature.

[`readerErrorInvalidParameter`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerErrorInvalidParameter)

An input parameter is invalid.

[`readerErrorInvalidParameterLength`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerErrorInvalidParameterLength)

The length of an input parameter is invalid.

[`readerErrorParameterOutOfBound`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerErrorParameterOutOfBound)

A parameter value is outside of the acceptable boundary.

[`readerErrorRadioDisabled`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerErrorRadioDisabled)

The NFC wireless radio on the device is disabled.

[`readerErrorSecurityViolation`](/documentation/CoreNFC/NFCReaderError-swift.struct/readerErrorSecurityViolation)

A security violation associated with the reader session has occurred.

### Error Domain

[`NFCErrorDomain`](/documentation/CoreNFC/NFCErrorDomain)

The domain for errors associated with Core NFC APIs.

## Relationships

### Conforms To

[`SendableMetatype`](/documentation/Swift/SendableMetatype)

[`Hashable`](/documentation/Swift/Hashable)

[`CustomNSError`](/documentation/Foundation/CustomNSError)

[`Sendable`](/documentation/Swift/Sendable)

[`Equatable`](/documentation/Swift/Equatable)

[`Error`](/documentation/Swift/Error)

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
