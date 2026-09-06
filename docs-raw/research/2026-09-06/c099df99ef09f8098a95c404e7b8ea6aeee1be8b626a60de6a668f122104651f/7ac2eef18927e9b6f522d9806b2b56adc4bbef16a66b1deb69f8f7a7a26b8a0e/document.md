# Security Framework Result Codes

Evaluate result codes common to many Security framework functions.

## Discussion

Use the [`SecCopyErrorMessageString(_:_:)`](/documentation/Security/SecCopyErrorMessageString(_:_:)) function to obtain a human readable string corresponding to these status codes.

In addition to the codes listed here, certain Security framework services provide additional status codes that are specific to that service. In particular, see [Authorization Services Result Codes](/documentation/Security/authorization-services-result-codes), [Sessions API Result Codes](/documentation/Security/sessions-api-result-codes), [Secure Transport Result Codes](/documentation/Security/secure-transport-result-codes), [Secure Download Result Codes](/documentation/Security/secure-download-result-codes), and [Code Signing Services Result Codes](/documentation/Security/code-signing-services-result-codes).

## Topics

### Result Strings

[`SecCopyErrorMessageString`](/documentation/Security/SecCopyErrorMessageString(_:_:))

Returns a string explaining the meaning of a security result code.

### System Result Codes

[`errSecSuccess`](/documentation/Security/errSecSuccess)

No error.

[`errSecUnimplemented`](/documentation/Security/errSecUnimplemented)

A function or operation is not implemented.

[`errSecDskFull`](/documentation/Security/errSecDskFull)

The disk is full.

[`errSecDiskFull`](/documentation/Security/errSecDiskFull)

The disk is full.

[`errSecIO`](/documentation/Security/errSecIO)

I/O error.

[`errSecOpWr`](/documentation/Security/errSecOpWr)

The file is already open with write permission.

[`errSecParam`](/documentation/Security/errSecParam)

One or more parameters passed to the function are not valid.

[`errSecWrPerm`](/documentation/Security/errSecWrPerm)

Write permissions error.

[`errSecAllocate`](/documentation/Security/errSecAllocate)

Failed to allocate memory.

[`errSecUserCanceled`](/documentation/Security/errSecUserCanceled)

User canceled the operation.

[`errSecBadReq`](/documentation/Security/errSecBadReq)

Bad parameter or invalid state for operation.

### Internal Error Result Codes

[`errSecInternalComponent`](/documentation/Security/errSecInternalComponent)

An internal component experienced an error.

[`errSecCoreFoundationUnknown`](/documentation/Security/errSecCoreFoundationUnknown)

An unknown Core Foundation error occurred.

[`errSecInternalError`](/documentation/Security/errSecInternalError)

An internal error occurred.

### Keychain Result Codes

[`errSecNotAvailable`](/documentation/Security/errSecNotAvailable)

No trust results are available.

[`errSecReadOnly`](/documentation/Security/errSecReadOnly)

Read-only error.

[`errSecAuthFailed`](/documentation/Security/errSecAuthFailed)

Authorization and/or authentication failed.

[`errSecNoSuchKeychain`](/documentation/Security/errSecNoSuchKeychain)

The keychain does not exist.

[`errSecInvalidKeychain`](/documentation/Security/errSecInvalidKeychain)

The keychain is not valid.

[`errSecDuplicateKeychain`](/documentation/Security/errSecDuplicateKeychain)

A keychain with the same name already exists.

[`errSecDuplicateCallback`](/documentation/Security/errSecDuplicateCallback)

More than one callback of the same name exists.

[`errSecInvalidCallback`](/documentation/Security/errSecInvalidCallback)

The callback is not valid.

[`errSecDuplicateItem`](/documentation/Security/errSecDuplicateItem)

The item already exists.

[`errSecItemNotFound`](/documentation/Security/errSecItemNotFound)

The item cannot be found.

[`errSecBufferTooSmall`](/documentation/Security/errSecBufferTooSmall)

The buffer is too small.

[`errSecDataTooLarge`](/documentation/Security/errSecDataTooLarge)

The data is too large for the particular data type.

[`errSecNoSuchAttr`](/documentation/Security/errSecNoSuchAttr)

The attribute does not exist.

[`errSecInvalidItemRef`](/documentation/Security/errSecInvalidItemRef)

The item reference is invalid.

[`errSecInvalidSearchRef`](/documentation/Security/errSecInvalidSearchRef)

The search reference is invalid.

[`errSecNoSuchClass`](/documentation/Security/errSecNoSuchClass)

The keychain item class does not exist.

[`errSecNoDefaultKeychain`](/documentation/Security/errSecNoDefaultKeychain)

A default keychain does not exist.

[`errSecInteractionNotAllowed`](/documentation/Security/errSecInteractionNotAllowed)

Interaction with the Security Server is not allowed.

[`errSecReadOnlyAttr`](/documentation/Security/errSecReadOnlyAttr)

The attribute is read-only.

[`errSecWrongSecVersion`](/documentation/Security/errSecWrongSecVersion)

The version is incorrect.

[`errSecKeySizeNotAllowed`](/documentation/Security/errSecKeySizeNotAllowed)

The key size is not allowed.

[`errSecNoStorageModule`](/documentation/Security/errSecNoStorageModule)

There is no storage module available.

[`errSecNoCertificateModule`](/documentation/Security/errSecNoCertificateModule)

There is no certificate module available.

[`errSecNoPolicyModule`](/documentation/Security/errSecNoPolicyModule)

There is no policy module available.

[`errSecInteractionRequired`](/documentation/Security/errSecInteractionRequired)

User interaction is required.

[`errSecDataNotAvailable`](/documentation/Security/errSecDataNotAvailable)

The data is not available.

[`errSecDataNotModifiable`](/documentation/Security/errSecDataNotModifiable)

The data is not modifiable.

[`errSecCreateChainFailed`](/documentation/Security/errSecCreateChainFailed)

The attempt to create a certificate chain failed.

[`errSecInvalidPrefsDomain`](/documentation/Security/errSecInvalidPrefsDomain)

The preference domain specified is invalid.

[`errSecInDarkWake`](/documentation/Security/errSecInDarkWake)

The user interface cannot be displayed because the system is in a dark wake state.

### Certificate Result Codes

[`errSecUnknownCriticalExtensionFlag`](/documentation/Security/errSecUnknownCriticalExtensionFlag)

There is an unknown critical extension flag.

[`errSecCertificateCannotOperate`](/documentation/Security/errSecCertificateCannotOperate)

The certificate cannot operate.

[`errSecCertificateExpired`](/documentation/Security/errSecCertificateExpired)

An expired certificate was detected.

[`errSecCertificateNotValidYet`](/documentation/Security/errSecCertificateNotValidYet)

The certificate is not yet valid.

[`errSecCertificateRevoked`](/documentation/Security/errSecCertificateRevoked)

The certificate was revoked.

[`errSecCertificateSuspended`](/documentation/Security/errSecCertificateSuspended)

The certificate was suspended.

[`errSecInvalidCertAuthority`](/documentation/Security/errSecInvalidCertAuthority)

The certificate authority is not valid.

[`errSecInvalidCertificateGroup`](/documentation/Security/errSecInvalidCertificateGroup)

An invalid certificate group was detected.

[`errSecInvalidCertificateRef`](/documentation/Security/errSecInvalidCertificateRef)

An invalid certificate reference was detected.

[`errSecCertificateNameNotAllowed`](/documentation/Security/errSecCertificateNameNotAllowed)

The requested name isn’t allowed for this certificate.

[`errSecCertificatePolicyNotAllowed`](/documentation/Security/errSecCertificatePolicyNotAllowed)

The requested policy isn’t allowed for this certificate.

[`errSecCertificateValidityPeriodTooLong`](/documentation/Security/errSecCertificateValidityPeriodTooLong)

The validity period in the certificate exceeds the maximum allowed period.

### ACL Result Codes

[`errSecACLAddFailed`](/documentation/Security/errSecACLAddFailed)

An ACL add operation failed.

[`errSecACLChangeFailed`](/documentation/Security/errSecACLChangeFailed)

An ACL change operation failed.

[`errSecACLDeleteFailed`](/documentation/Security/errSecACLDeleteFailed)

An ACL delete operation failed.

[`errSecACLNotSimple`](/documentation/Security/errSecACLNotSimple)

The access control list is not in standard simple form.

[`errSecACLReplaceFailed`](/documentation/Security/errSecACLReplaceFailed)

An ACL replace operation failed.

[`errSecAppleAddAppACLSubject`](/documentation/Security/errSecAppleAddAppACLSubject)

Adding an application ACL subject failed.

[`errSecInvalidBaseACLs`](/documentation/Security/errSecInvalidBaseACLs)

The base access control lists are not valid.

[`errSecInvalidACL`](/documentation/Security/errSecInvalidACL)

An invalid access control list was detected.

### CRL Result Codes

[`errSecCRLExpired`](/documentation/Security/errSecCRLExpired)

The certificate revocation list has expired.

[`errSecCRLNotValidYet`](/documentation/Security/errSecCRLNotValidYet)

The certificate revocation list is not yet valid.

[`errSecCRLNotFound`](/documentation/Security/errSecCRLNotFound)

The certificate revocation list was not found.

[`errSecCRLServerDown`](/documentation/Security/errSecCRLServerDown)

The certificate revocation list server is down.

[`errSecCRLBadURI`](/documentation/Security/errSecCRLBadURI)

The certificate revocation list has a bad uniform resource identifier.

[`errSecCRLNotTrusted`](/documentation/Security/errSecCRLNotTrusted)

The certificate revocation list is not trusted.

[`errSecUnknownCertExtension`](/documentation/Security/errSecUnknownCertExtension)

An unknown certificate extension was detected.

[`errSecUnknownCRLExtension`](/documentation/Security/errSecUnknownCRLExtension)

An unknown certificate revocation list extension was detected.

[`errSecCRLPolicyFailed`](/documentation/Security/errSecCRLPolicyFailed)

The certificate revocation list policy failed.

[`errSecCRLAlreadySigned`](/documentation/Security/errSecCRLAlreadySigned)

The certificate revocation list is already signed.

[`errSecIDPFailure`](/documentation/Security/errSecIDPFailure)

The issuing distribution point is not valid.

[`errSecInvalidCRLEncoding`](/documentation/Security/errSecInvalidCRLEncoding)

The certificate revocation list encoding is not valid.

[`errSecInvalidCRLType`](/documentation/Security/errSecInvalidCRLType)

The certificate revocation list type is not valid.

[`errSecInvalidCRL`](/documentation/Security/errSecInvalidCRL)

The certificate revocation list is not valid.

[`errSecInvalidCRLGroup`](/documentation/Security/errSecInvalidCRLGroup)

An invalid certificate revocation list group was detected.

[`errSecInvalidCRLIndex`](/documentation/Security/errSecInvalidCRLIndex)

The certificate revocation list index is not valid.

[`errSecInvaldCRLAuthority`](/documentation/Security/errSecInvaldCRLAuthority)

The certificate revocation list authority is not valid.

### SMIME Result Codes

[`errSecSMIMEEmailAddressesNotFound`](/documentation/Security/errSecSMIMEEmailAddressesNotFound)

An email address mismatch was detected.

[`errSecSMIMEBadExtendedKeyUsage`](/documentation/Security/errSecSMIMEBadExtendedKeyUsage)

The appropriate extended key usage for SMIME is not found.

[`errSecSMIMEBadKeyUsage`](/documentation/Security/errSecSMIMEBadKeyUsage)

The key usage is not compatible with SMIME.

[`errSecSMIMEKeyUsageNotCritical`](/documentation/Security/errSecSMIMEKeyUsageNotCritical)

The key usage extension is not marked as critical.

[`errSecSMIMENoEmailAddress`](/documentation/Security/errSecSMIMENoEmailAddress)

No email address is found in the certificate.

[`errSecSMIMESubjAltNameNotCritical`](/documentation/Security/errSecSMIMESubjAltNameNotCritical)

The subject alternative name extension is not marked as critical.

[`errSecSSLBadExtendedKeyUsage`](/documentation/Security/errSecSSLBadExtendedKeyUsage)

The appropriate extended key usage for SSL is not found.

### OCSP Result Codes

[`errSecOCSPBadResponse`](/documentation/Security/errSecOCSPBadResponse)

The online certificate status protocol (OCSP) response is incorrect or cannot be parsed.

[`errSecOCSPBadRequest`](/documentation/Security/errSecOCSPBadRequest)

The online certificate status protocol (OCSP) request is incorrect or cannot be parsed.

[`errSecOCSPUnavailable`](/documentation/Security/errSecOCSPUnavailable)

The online certificate status protocol (OCSP) service is unavailable.

[`errSecOCSPStatusUnrecognized`](/documentation/Security/errSecOCSPStatusUnrecognized)

The online certificate status protocol (OCSP) server does not recognize this certificate.

[`errSecEndOfData`](/documentation/Security/errSecEndOfData)

An end-of-data was detected.

[`errSecIncompleteCertRevocationCheck`](/documentation/Security/errSecIncompleteCertRevocationCheck)

An incomplete certificate revocation check occurred.

[`errSecNetworkFailure`](/documentation/Security/errSecNetworkFailure)

A network failure occurred.

[`errSecOCSPNotTrustedToAnchor`](/documentation/Security/errSecOCSPNotTrustedToAnchor)

The online certificate status protocol (OCSP) response is not trusted to a root or anchor certificate.

[`errSecRecordModified`](/documentation/Security/errSecRecordModified)

The record is modified.

[`errSecOCSPSignatureError`](/documentation/Security/errSecOCSPSignatureError)

The online certificate status protocol (OCSP) response has an invalid signature.

[`errSecOCSPNoSigner`](/documentation/Security/errSecOCSPNoSigner)

The online certificate status protocol (OCSP) response has no signer.

[`errSecOCSPResponderMalformedReq`](/documentation/Security/errSecOCSPResponderMalformedReq)

The online certificate status protocol (OCSP) responder detected a malformed request.

[`errSecOCSPResponderInternalError`](/documentation/Security/errSecOCSPResponderInternalError)

The online certificate status protocol (OCSP) responder detected an internal error.

[`errSecOCSPResponderTryLater`](/documentation/Security/errSecOCSPResponderTryLater)

The online certificate status protocol (OCSP) responder is busy, try again later.

[`errSecOCSPResponderSignatureRequired`](/documentation/Security/errSecOCSPResponderSignatureRequired)

The online certificate status protocol (OCSP) responder requires a signature.

[`errSecOCSPResponderUnauthorized`](/documentation/Security/errSecOCSPResponderUnauthorized)

The online certificate status protocol (OCSP) responder rejects the request as unauthorized.

[`errSecOCSPResponseNonceMismatch`](/documentation/Security/errSecOCSPResponseNonceMismatch)

The online certificate status protocol (OCSP) response nonce does not match the request.

### Code Signing Result Codes

[`errSecCodeSigningBadCertChainLength`](/documentation/Security/errSecCodeSigningBadCertChainLength)

Code signing encountered an incorrect certificate chain length.

[`errSecCodeSigningNoBasicConstraints`](/documentation/Security/errSecCodeSigningNoBasicConstraints)

Code signing found no basic constraints.

[`errSecCodeSigningBadPathLengthConstraint`](/documentation/Security/errSecCodeSigningBadPathLengthConstraint)

Code signing encountered an incorrect path length constraint.

[`errSecCodeSigningNoExtendedKeyUsage`](/documentation/Security/errSecCodeSigningNoExtendedKeyUsage)

Code signing found no extended key usage.

[`errSecCodeSigningDevelopment`](/documentation/Security/errSecCodeSigningDevelopment)

Code signing indicated use of a development-only certificate.

[`errSecResourceSignBadCertChainLength`](/documentation/Security/errSecResourceSignBadCertChainLength)

Resource signing detects an incorrect certificate chain length.

[`errSecResourceSignBadExtKeyUsage`](/documentation/Security/errSecResourceSignBadExtKeyUsage)

Resource signing detects an error in the extended key usage.

[`errSecTrustSettingDeny`](/documentation/Security/errSecTrustSettingDeny)

The trust setting for this policy is set to Deny.

[`errSecInvalidSubjectName`](/documentation/Security/errSecInvalidSubjectName)

An invalid certificate subject name was detected.

[`errSecUnknownQualifiedCertStatement`](/documentation/Security/errSecUnknownQualifiedCertStatement)

An unknown qualified certificate statement was detected.

### Mobile Me Result Codes

[`errSecMobileMeRequestQueued`](/documentation/Security/errSecMobileMeRequestQueued)

The MobileMe request will be sent during the next connection.

[`errSecMobileMeRequestRedirected`](/documentation/Security/errSecMobileMeRequestRedirected)

The MobileMe request was redirected.

[`errSecMobileMeServerError`](/documentation/Security/errSecMobileMeServerError)

A MobileMe server error occurred.

[`errSecMobileMeServerNotAvailable`](/documentation/Security/errSecMobileMeServerNotAvailable)

The MobileMe server is not available.

[`errSecMobileMeServerAlreadyExists`](/documentation/Security/errSecMobileMeServerAlreadyExists)

The MobileMe server reported that the item already exists.

[`errSecMobileMeServerServiceErr`](/documentation/Security/errSecMobileMeServerServiceErr)

A MobileMe service error occurred.

[`errSecMobileMeRequestAlreadyPending`](/documentation/Security/errSecMobileMeRequestAlreadyPending)

A MobileMe request is already pending.

[`errSecMobileMeNoRequestPending`](/documentation/Security/errSecMobileMeNoRequestPending)

MobileMe has no request pending.

[`errSecMobileMeCSRVerifyFailure`](/documentation/Security/errSecMobileMeCSRVerifyFailure)

A MobileMe certificate signing request verification failure occurred.

[`errSecMobileMeFailedConsistencyCheck`](/documentation/Security/errSecMobileMeFailedConsistencyCheck)

MobileMe found a failed consistency check.

### Cryptographic Key Result Codes

[`errSecKeyUsageIncorrect`](/documentation/Security/errSecKeyUsageIncorrect)

The key usage is incorrect.

[`errSecKeyBlobTypeIncorrect`](/documentation/Security/errSecKeyBlobTypeIncorrect)

The key blob type is incorrect.

[`errSecKeyHeaderInconsistent`](/documentation/Security/errSecKeyHeaderInconsistent)

The key header is inconsistent.

[`errSecKeyIsSensitive`](/documentation/Security/errSecKeyIsSensitive)

The key must be wrapped to be exported.

[`errSecUnsupportedKeyFormat`](/documentation/Security/errSecUnsupportedKeyFormat)

The key header format is not supported.

[`errSecUnsupportedKeySize`](/documentation/Security/errSecUnsupportedKeySize)

The key size is not supported.

[`errSecInvalidKeyUsageMask`](/documentation/Security/errSecInvalidKeyUsageMask)

The key usage mask is not valid.

[`errSecUnsupportedKeyUsageMask`](/documentation/Security/errSecUnsupportedKeyUsageMask)

The key usage mask is not supported.

[`errSecInvalidKeyAttributeMask`](/documentation/Security/errSecInvalidKeyAttributeMask)

The key attribute mask is not valid.

[`errSecUnsupportedKeyAttributeMask`](/documentation/Security/errSecUnsupportedKeyAttributeMask)

The key attribute mask is not supported.

[`errSecInvalidKeyLabel`](/documentation/Security/errSecInvalidKeyLabel)

The key label is not valid.

[`errSecUnsupportedKeyLabel`](/documentation/Security/errSecUnsupportedKeyLabel)

The key label is not supported.

[`errSecInvalidKeyFormat`](/documentation/Security/errSecInvalidKeyFormat)

The key format is not valid.

[`errSecInvalidKeyBlob`](/documentation/Security/errSecInvalidKeyBlob)

The specified database has an invalid key blob.

[`errSecInvalidKeyHierarchy`](/documentation/Security/errSecInvalidKeyHierarchy)

An invalid key hierarchy was detected.

[`errSecInvalidKeyRef`](/documentation/Security/errSecInvalidKeyRef)

An invalid key was encountered.

[`errSecInvalidKeyUsageForPolicy`](/documentation/Security/errSecInvalidKeyUsageForPolicy)

The key usage is not valid for the specified policy.

### Invalid Attribute Result Codes

[`errSecInvalidAttributeKey`](/documentation/Security/errSecInvalidAttributeKey)

A key attribute is not valid.

[`errSecInvalidAttributeInitVector`](/documentation/Security/errSecInvalidAttributeInitVector)

An init vector attribute is not valid.

[`errSecInvalidAttributeSalt`](/documentation/Security/errSecInvalidAttributeSalt)

A salt attribute is not valid.

[`errSecInvalidAttributePadding`](/documentation/Security/errSecInvalidAttributePadding)

A padding attribute is not valid.

[`errSecInvalidAttributeRandom`](/documentation/Security/errSecInvalidAttributeRandom)

A random number attribute is not valid.

[`errSecInvalidAttributeSeed`](/documentation/Security/errSecInvalidAttributeSeed)

A seed attribute is not valid.

[`errSecInvalidAttributePassphrase`](/documentation/Security/errSecInvalidAttributePassphrase)

A passphrase attribute is not valid.

[`errSecInvalidAttributeKeyLength`](/documentation/Security/errSecInvalidAttributeKeyLength)

A key length attribute is not valid.

[`errSecInvalidAttributeBlockSize`](/documentation/Security/errSecInvalidAttributeBlockSize)

A block size attribute is not valid.

[`errSecInvalidAttributeOutputSize`](/documentation/Security/errSecInvalidAttributeOutputSize)

An output size attribute is not valid.

[`errSecInvalidAttributeRounds`](/documentation/Security/errSecInvalidAttributeRounds)

The number of rounds attribute is not valid.

[`errSecInvalidAlgorithmParms`](/documentation/Security/errSecInvalidAlgorithmParms)

An algorithm parameters attribute is not valid.

[`errSecInvalidAttributeLabel`](/documentation/Security/errSecInvalidAttributeLabel)

A label attribute is not valid.

[`errSecInvalidAttributeKeyType`](/documentation/Security/errSecInvalidAttributeKeyType)

A key type attribute is not valid.

[`errSecInvalidAttributeMode`](/documentation/Security/errSecInvalidAttributeMode)

A mode attribute is not valid.

[`errSecInvalidAttributeEffectiveBits`](/documentation/Security/errSecInvalidAttributeEffectiveBits)

An effective bits attribute is not valid.

[`errSecInvalidAttributeStartDate`](/documentation/Security/errSecInvalidAttributeStartDate)

A start date attribute is not valid.

[`errSecInvalidAttributeEndDate`](/documentation/Security/errSecInvalidAttributeEndDate)

An end date attribute is not valid.

[`errSecInvalidAttributeVersion`](/documentation/Security/errSecInvalidAttributeVersion)

A version attribute is not valid.

[`errSecInvalidAttributePrime`](/documentation/Security/errSecInvalidAttributePrime)

A prime attribute is not valid.

[`errSecInvalidAttributeBase`](/documentation/Security/errSecInvalidAttributeBase)

A base attribute is not valid.

[`errSecInvalidAttributeSubprime`](/documentation/Security/errSecInvalidAttributeSubprime)

A subprime attribute is not valid.

[`errSecInvalidAttributeIterationCount`](/documentation/Security/errSecInvalidAttributeIterationCount)

An iteration count attribute is not valid.

[`errSecInvalidAttributeDLDBHandle`](/documentation/Security/errSecInvalidAttributeDLDBHandle)

A database handle attribute is not valid.

[`errSecInvalidAttributeAccessCredentials`](/documentation/Security/errSecInvalidAttributeAccessCredentials)

An access credentials attribute is not valid.

[`errSecInvalidAttributePublicKeyFormat`](/documentation/Security/errSecInvalidAttributePublicKeyFormat)

A public key format attribute is not valid.

[`errSecInvalidAttributePrivateKeyFormat`](/documentation/Security/errSecInvalidAttributePrivateKeyFormat)

A private key format attribute is not valid.

[`errSecInvalidAttributeSymmetricKeyFormat`](/documentation/Security/errSecInvalidAttributeSymmetricKeyFormat)

A symmetric key format attribute is not valid.

[`errSecInvalidAttributeWrappedKeyFormat`](/documentation/Security/errSecInvalidAttributeWrappedKeyFormat)

A wrapped key format attribute is not valid.

### Missing Attribute Result Codes

[`errSecMissingAttributeKey`](/documentation/Security/errSecMissingAttributeKey)

A key attribute is missing.

[`errSecMissingAttributeInitVector`](/documentation/Security/errSecMissingAttributeInitVector)

An init vector attribute is missing.

[`errSecMissingAttributeSalt`](/documentation/Security/errSecMissingAttributeSalt)

A salt attribute is missing.

[`errSecMissingAttributePadding`](/documentation/Security/errSecMissingAttributePadding)

A padding attribute is missing.

[`errSecMissingAttributeRandom`](/documentation/Security/errSecMissingAttributeRandom)

A random number attribute is missing.

[`errSecMissingAttributeSeed`](/documentation/Security/errSecMissingAttributeSeed)

A seed attribute is missing.

[`errSecMissingAttributePassphrase`](/documentation/Security/errSecMissingAttributePassphrase)

A passphrase attribute is missing.

[`errSecMissingAttributeKeyLength`](/documentation/Security/errSecMissingAttributeKeyLength)

A key length attribute is missing.

[`errSecMissingAttributeBlockSize`](/documentation/Security/errSecMissingAttributeBlockSize)

A block size attribute is missing.

[`errSecMissingAttributeOutputSize`](/documentation/Security/errSecMissingAttributeOutputSize)

An output size attribute is missing.

[`errSecMissingAttributeRounds`](/documentation/Security/errSecMissingAttributeRounds)

The number of rounds attribute is missing.

[`errSecMissingAlgorithmParms`](/documentation/Security/errSecMissingAlgorithmParms)

An algorithm parameters attribute is missing.

[`errSecMissingAttributeLabel`](/documentation/Security/errSecMissingAttributeLabel)

A label attribute is missing.

[`errSecMissingAttributeKeyType`](/documentation/Security/errSecMissingAttributeKeyType)

A key type attribute is missing.

[`errSecMissingAttributeMode`](/documentation/Security/errSecMissingAttributeMode)

A mode attribute is missing.

[`errSecMissingAttributeEffectiveBits`](/documentation/Security/errSecMissingAttributeEffectiveBits)

An effective bits attribute is missing.

[`errSecMissingAttributeStartDate`](/documentation/Security/errSecMissingAttributeStartDate)

A start date attribute is missing.

[`errSecMissingAttributeEndDate`](/documentation/Security/errSecMissingAttributeEndDate)

An end date attribute is missing.

[`errSecMissingAttributeVersion`](/documentation/Security/errSecMissingAttributeVersion)

A version attribute is missing.

[`errSecMissingAttributePrime`](/documentation/Security/errSecMissingAttributePrime)

A prime attribute is missing.

[`errSecMissingAttributeBase`](/documentation/Security/errSecMissingAttributeBase)

A base attribute is missing.

[`errSecMissingAttributeSubprime`](/documentation/Security/errSecMissingAttributeSubprime)

A subprime attribute is missing.

[`errSecMissingAttributeIterationCount`](/documentation/Security/errSecMissingAttributeIterationCount)

An iteration count attribute is missing.

[`errSecMissingAttributeDLDBHandle`](/documentation/Security/errSecMissingAttributeDLDBHandle)

A database handle attribute is missing.

[`errSecMissingAttributeAccessCredentials`](/documentation/Security/errSecMissingAttributeAccessCredentials)

An access credentials attribute is missing.

[`errSecMissingAttributePublicKeyFormat`](/documentation/Security/errSecMissingAttributePublicKeyFormat)

A public key format attribute is missing.

[`errSecMissingAttributePrivateKeyFormat`](/documentation/Security/errSecMissingAttributePrivateKeyFormat)

A private key format attribute is missing.

[`errSecMissingAttributeSymmetricKeyFormat`](/documentation/Security/errSecMissingAttributeSymmetricKeyFormat)

A symmetric key format attribute is missing.

[`errSecMissingAttributeWrappedKeyFormat`](/documentation/Security/errSecMissingAttributeWrappedKeyFormat)

A wrapped key format attribute is missing.

### Timestamp Result Codes

[`errSecTimestampMissing`](/documentation/Security/errSecTimestampMissing)

A timestamp is expected but is not found.

[`errSecTimestampInvalid`](/documentation/Security/errSecTimestampInvalid)

The timestamp is not valid.

[`errSecTimestampNotTrusted`](/documentation/Security/errSecTimestampNotTrusted)

The timestamp is not trusted.

[`errSecTimestampServiceNotAvailable`](/documentation/Security/errSecTimestampServiceNotAvailable)

[`errSecTimestampBadAlg`](/documentation/Security/errSecTimestampBadAlg)

Found an unrecognized or unsupported algorithm identifier (AI) in timestamp.

[`errSecTimestampBadRequest`](/documentation/Security/errSecTimestampBadRequest)

The timestamp transaction is not permitted or supported.

[`errSecTimestampBadDataFormat`](/documentation/Security/errSecTimestampBadDataFormat)

The timestamp data submitted has the wrong format.

[`errSecTimestampTimeNotAvailable`](/documentation/Security/errSecTimestampTimeNotAvailable)

The time source for the timestamp authority is not available.

[`errSecTimestampUnacceptedPolicy`](/documentation/Security/errSecTimestampUnacceptedPolicy)

The requested policy is not supported by the timestamp authority.

[`errSecTimestampUnacceptedExtension`](/documentation/Security/errSecTimestampUnacceptedExtension)

The requested extension is not supported by the timestamp authority.

[`errSecTimestampAddInfoNotAvailable`](/documentation/Security/errSecTimestampAddInfoNotAvailable)

The additional information requested is not available.

[`errSecTimestampSystemFailure`](/documentation/Security/errSecTimestampSystemFailure)

The timestamp request cannot be handled due to a system failure.

[`errSecSigningTimeMissing`](/documentation/Security/errSecSigningTimeMissing)

A signing time is missing.

[`errSecTimestampRejection`](/documentation/Security/errSecTimestampRejection)

A timestamp transaction is rejected.

[`errSecTimestampWaiting`](/documentation/Security/errSecTimestampWaiting)

A timestamp transaction is waiting.

[`errSecTimestampRevocationWarning`](/documentation/Security/errSecTimestampRevocationWarning)

A timestamp authority revocation warning is issued.

[`errSecTimestampRevocationNotification`](/documentation/Security/errSecTimestampRevocationNotification)

A timestamp authority revocation notification is issued.

### Invalid parameter result codes

[`errSecInvalidAction`](/documentation/Security/errSecInvalidAction)

The action is invalid.

[`errSecInvalidAddinFunctionTable`](/documentation/Security/errSecInvalidAddinFunctionTable)

An invalid add-in function table was detected.

[`errSecInvalidAlgorithm`](/documentation/Security/errSecInvalidAlgorithm)

An invalid algorithm was detected.

[`errSecInvalidAuthority`](/documentation/Security/errSecInvalidAuthority)

The authority is not valid.

[`errSecInvalidAuthorityKeyID`](/documentation/Security/errSecInvalidAuthorityKeyID)

The authority key ID is not valid.

[`errSecInvalidBundleInfo`](/documentation/Security/errSecInvalidBundleInfo)

The bundle information is not valid.

[`errSecInvalidContext`](/documentation/Security/errSecInvalidContext)

An invalid context was detected.

[`errSecInvalidDBList`](/documentation/Security/errSecInvalidDBList)

An invalid DB list was detected.

[`errSecInvalidDBLocation`](/documentation/Security/errSecInvalidDBLocation)

The database location is not valid.

[`errSecInvalidData`](/documentation/Security/errSecInvalidData)

Invalid data was detected.

[`errSecInvalidDatabaseBlob`](/documentation/Security/errSecInvalidDatabaseBlob)

The specified database has an invalid blob.

[`errSecInvalidDigestAlgorithm`](/documentation/Security/errSecInvalidDigestAlgorithm)

An invalid digest algorithm was detected.

[`errSecInvalidEncoding`](/documentation/Security/errSecInvalidEncoding)

The encoding is not valid.

[`errSecInvalidExtendedKeyUsage`](/documentation/Security/errSecInvalidExtendedKeyUsage)

The extended key usage is not valid.

[`errSecInvalidFormType`](/documentation/Security/errSecInvalidFormType)

The form type is not valid.

[`errSecInvalidGUID`](/documentation/Security/errSecInvalidGUID)

An invalid GUID was detected.

[`errSecInvalidHandle`](/documentation/Security/errSecInvalidHandle)

An invalid handle was encountered.

[`errSecInvalidHandleUsage`](/documentation/Security/errSecInvalidHandleUsage)

The common security services manager handle does not match with the service type.

[`errSecInvalidID`](/documentation/Security/errSecInvalidID)

The ID is not valid.

[`errSecInvalidIDLinkage`](/documentation/Security/errSecInvalidIDLinkage)

The ID linkage is not valid.

[`errSecInvalidIdentifier`](/documentation/Security/errSecInvalidIdentifier)

The identifier is not valid.

[`errSecInvalidIndex`](/documentation/Security/errSecInvalidIndex)

The index is not valid.

[`errSecInvalidIndexInfo`](/documentation/Security/errSecInvalidIndexInfo)

The index information is not valid.

[`errSecInvalidInputVector`](/documentation/Security/errSecInvalidInputVector)

The input vector is not valid.

[`errSecInvalidLoginName`](/documentation/Security/errSecInvalidLoginName)

An invalid login name was detected.

[`errSecInvalidModifyMode`](/documentation/Security/errSecInvalidModifyMode)

The modify mode is not valid.

[`errSecInvalidName`](/documentation/Security/errSecInvalidName)

An invalid name was detected.

[`errSecInvalidNetworkAddress`](/documentation/Security/errSecInvalidNetworkAddress)

An invalid network address was detected.

[`errSecInvalidNewOwner`](/documentation/Security/errSecInvalidNewOwner)

The new owner is not valid.

[`errSecInvalidNumberOfFields`](/documentation/Security/errSecInvalidNumberOfFields)

An invalid number of fields were detected.

[`errSecInvalidOutputVector`](/documentation/Security/errSecInvalidOutputVector)

The output vector is not valid.

[`errSecInvalidOwnerEdit`](/documentation/Security/errSecInvalidOwnerEdit)

An invalid attempt to change the owner of an item.

[`errSecInvalidPVC`](/documentation/Security/errSecInvalidPVC)

An invalid pointer validation checking policy was detected.

[`errSecInvalidParsingModule`](/documentation/Security/errSecInvalidParsingModule)

The parsing module is not valid.

[`errSecInvalidPassthroughID`](/documentation/Security/errSecInvalidPassthroughID)

An invalid passthrough ID was detected.

[`errSecInvalidPasswordRef`](/documentation/Security/errSecInvalidPasswordRef)

The password reference is invalid.

[`errSecInvalidPointer`](/documentation/Security/errSecInvalidPointer)

An invalid pointer was detected.

[`errSecInvalidPolicyIdentifiers`](/documentation/Security/errSecInvalidPolicyIdentifiers)

The policy identifiers are not valid.

[`errSecInvalidQuery`](/documentation/Security/errSecInvalidQuery)

The specified query is not valid.

[`errSecInvalidReason`](/documentation/Security/errSecInvalidReason)

The trust policy reason is not valid.

[`errSecInvalidRecord`](/documentation/Security/errSecInvalidRecord)

An invalid record was detected.

[`errSecInvalidRequestInputs`](/documentation/Security/errSecInvalidRequestInputs)

The request inputs are not valid.

[`errSecInvalidRequestor`](/documentation/Security/errSecInvalidRequestor)

The requestor is not valid.

[`errSecInvalidResponseVector`](/documentation/Security/errSecInvalidResponseVector)

The response vector is not valid.

[`errSecInvalidRoot`](/documentation/Security/errSecInvalidRoot)

The root or anchor certificate is not valid.

[`errSecInvalidSampleValue`](/documentation/Security/errSecInvalidSampleValue)

An invalid sample value was detected.

[`errSecInvalidScope`](/documentation/Security/errSecInvalidScope)

An invalid scope was detected.

[`errSecInvalidServiceMask`](/documentation/Security/errSecInvalidServiceMask)

An invalid service mask was detected.

[`errSecInvalidSignature`](/documentation/Security/errSecInvalidSignature)

An invalid signature was detected.

[`errSecInvalidStopOnPolicy`](/documentation/Security/errSecInvalidStopOnPolicy)

The stop-on policy is not valid.

[`errSecInvalidSubServiceID`](/documentation/Security/errSecInvalidSubServiceID)

An invalid sub-service ID was detected.

[`errSecInvalidSubjectKeyID`](/documentation/Security/errSecInvalidSubjectKeyID)

The subject key ID is not valid.

[`errSecInvalidTimeString`](/documentation/Security/errSecInvalidTimeString)

The time specified is not valid.

[`errSecInvalidTrustSetting`](/documentation/Security/errSecInvalidTrustSetting)

The trust setting is invalid.

[`errSecInvalidTrustSettings`](/documentation/Security/errSecInvalidTrustSettings)

The trust settings record is corrupted.

[`errSecInvalidTuple`](/documentation/Security/errSecInvalidTuple)

The tuple is not valid.

[`errSecInvalidTupleCredendtials`](/documentation/Security/errSecInvalidTupleCredendtials)

The tuple credentials are not valid.

[`errSecInvalidTupleGroup`](/documentation/Security/errSecInvalidTupleGroup)

The tuple group is not valid.

[`errSecInvalidValidityPeriod`](/documentation/Security/errSecInvalidValidityPeriod)

The validity period is not valid.

[`errSecInvalidValue`](/documentation/Security/errSecInvalidValue)

An invalid value was detected.

### Unsupported input result codes

[`errSecUnsupportedAddressType`](/documentation/Security/errSecUnsupportedAddressType)

The address type is not supported.

[`errSecUnsupportedFieldFormat`](/documentation/Security/errSecUnsupportedFieldFormat)

The field format is not supported.

[`errSecUnsupportedFormat`](/documentation/Security/errSecUnsupportedFormat)

The specified import or export format is not supported.

[`errSecUnsupportedIndexInfo`](/documentation/Security/errSecUnsupportedIndexInfo)

The index information is not supported.

[`errSecUnsupportedLocality`](/documentation/Security/errSecUnsupportedLocality)

The locality is not supported.

[`errSecUnsupportedNumAttributes`](/documentation/Security/errSecUnsupportedNumAttributes)

The number of attributes is not supported.

[`errSecUnsupportedNumIndexes`](/documentation/Security/errSecUnsupportedNumIndexes)

The number of indexes is not supported.

[`errSecUnsupportedNumRecordTypes`](/documentation/Security/errSecUnsupportedNumRecordTypes)

The number of record types is not supported.

[`errSecUnsupportedNumSelectionPreds`](/documentation/Security/errSecUnsupportedNumSelectionPreds)

The number of selection predicates is not supported.

[`errSecUnsupportedOperator`](/documentation/Security/errSecUnsupportedOperator)

The operator is not supported.

[`errSecUnsupportedQueryLimits`](/documentation/Security/errSecUnsupportedQueryLimits)

The query limits are not supported.

[`errSecUnsupportedService`](/documentation/Security/errSecUnsupportedService)

The service is not supported.

[`errSecUnsupportedVectorOfBuffers`](/documentation/Security/errSecUnsupportedVectorOfBuffers)

The vector of buffers is not supported.

### Apple specific result codes

[`errSecAppleInvalidKeyEndDate`](/documentation/Security/errSecAppleInvalidKeyEndDate)

The specified key has an invalid end date.

[`errSecAppleInvalidKeyStartDate`](/documentation/Security/errSecAppleInvalidKeyStartDate)

The specified key has an invalid start date.

[`errSecApplePublicKeyIncomplete`](/documentation/Security/errSecApplePublicKeyIncomplete)

The public key is incomplete.

[`errSecAppleSSLv2Rollback`](/documentation/Security/errSecAppleSSLv2Rollback)

A SSLv2 rollback error has occurred.

[`errSecAppleSignatureMismatch`](/documentation/Security/errSecAppleSignatureMismatch)

A signature mismatch has occurred.

### Module manager result codes

[`errSecEMMLoadFailed`](/documentation/Security/errSecEMMLoadFailed)

The elective module manager load failed.

[`errSecEMMUnloadFailed`](/documentation/Security/errSecEMMUnloadFailed)

The elective module manager unload has failed.

[`errSecModuleManagerInitializeFailed`](/documentation/Security/errSecModuleManagerInitializeFailed)

A module failed to initialize.

[`errSecModuleManagerNotFound`](/documentation/Security/errSecModuleManagerNotFound)

A module was not found.

[`errSecModuleManifestVerifyFailed`](/documentation/Security/errSecModuleManifestVerifyFailed)

A module manifest verification failure occurred.

[`errSecModuleNotLoaded`](/documentation/Security/errSecModuleNotLoaded)

A module was not loaded.

### Other Result Codes

[`errSecAddinLoadFailed`](/documentation/Security/errSecAddinLoadFailed)

The add-in load operation failed.

[`errSecAddinUnloadFailed`](/documentation/Security/errSecAddinUnloadFailed)

The add-in unload operation failed.

[`errSecAlgorithmMismatch`](/documentation/Security/errSecAlgorithmMismatch)

An algorithm mismatch occurred.

[`errSecAlreadyLoggedIn`](/documentation/Security/errSecAlreadyLoggedIn)

The user is already logged in.

[`errSecAttachHandleBusy`](/documentation/Security/errSecAttachHandleBusy)

The CSP handle was busy.

[`errSecAttributeNotInContext`](/documentation/Security/errSecAttributeNotInContext)

An attribute was not in the context.

[`errSecBlockSizeMismatch`](/documentation/Security/errSecBlockSizeMismatch)

A block size mismatch occurred.

[`errSecCallbackFailed`](/documentation/Security/errSecCallbackFailed)

A callback failed.

[`errSecConversionError`](/documentation/Security/errSecConversionError)

A conversion error has occurred.

[`errSecDatabaseLocked`](/documentation/Security/errSecDatabaseLocked)

The database is locked.

[`errSecDatastoreIsOpen`](/documentation/Security/errSecDatastoreIsOpen)

The data store is open.

[`errSecDecode`](/documentation/Security/errSecDecode)

Unable to decode the provided data.

[`errSecDeviceError`](/documentation/Security/errSecDeviceError)

A device error was encountered.

[`errSecDeviceFailed`](/documentation/Security/errSecDeviceFailed)

A device failure has occurred.

[`errSecDeviceReset`](/documentation/Security/errSecDeviceReset)

A device reset has occurred.

[`errSecDeviceVerifyFailed`](/documentation/Security/errSecDeviceVerifyFailed)

A device verification failure has occurred.

[`errSecEventNotificationCallbackNotFound`](/documentation/Security/errSecEventNotificationCallbackNotFound)

An event notification callback was not found.

[`errSecExtendedKeyUsageNotCritical`](/documentation/Security/errSecExtendedKeyUsageNotCritical)

The extended key usage extension was not marked critical.

[`errSecFieldSpecifiedMultiple`](/documentation/Security/errSecFieldSpecifiedMultiple)

Too many fields were specified.

[`errSecFileTooBig`](/documentation/Security/errSecFileTooBig)

The file is too big.

[`errSecFunctionFailed`](/documentation/Security/errSecFunctionFailed)

A function has failed.

[`errSecFunctionIntegrityFail`](/documentation/Security/errSecFunctionIntegrityFail)

A function address is not within the verified module.

[`errSecHostNameMismatch`](/documentation/Security/errSecHostNameMismatch)

A host name mismatch has occurred.

[`errSecIncompatibleDatabaseBlob`](/documentation/Security/errSecIncompatibleDatabaseBlob)

The specified database has an incompatible blob.

[`errSecIncompatibleFieldFormat`](/documentation/Security/errSecIncompatibleFieldFormat)

The field format is incompatible.

[`errSecIncompatibleKeyBlob`](/documentation/Security/errSecIncompatibleKeyBlob)

The specified database has an incompatible key blob.

[`errSecIncompatibleVersion`](/documentation/Security/errSecIncompatibleVersion)

The version is incompatible.

[`errSecInputLengthError`](/documentation/Security/errSecInputLengthError)

An input length error occurred.

[`errSecInsufficientClientID`](/documentation/Security/errSecInsufficientClientID)

The client ID is incorrect.

[`errSecInsufficientCredentials`](/documentation/Security/errSecInsufficientCredentials)

Insufficient credentials were detected.

[`errSecInvalidAccessCredentials`](/documentation/Security/errSecInvalidAccessCredentials)

Invalid access credentials were detected.

[`errSecInvalidAccessRequest`](/documentation/Security/errSecInvalidAccessRequest)

The access request is invalid.

[`errSecLibraryReferenceNotFound`](/documentation/Security/errSecLibraryReferenceNotFound)

A library reference was not found.

[`errSecMDSError`](/documentation/Security/errSecMDSError)

A module directory service error occurred.

[`errSecMemoryError`](/documentation/Security/errSecMemoryError)

A memory error occurred.

[`errSecMissingEntitlement`](/documentation/Security/errSecMissingEntitlement)

A required entitlement is missing.

[`errSecMissingRequiredExtension`](/documentation/Security/errSecMissingRequiredExtension)

A required certificate extension is missing.

[`errSecMissingValue`](/documentation/Security/errSecMissingValue)

A missing value was detected.

[`errSecMultiplePrivKeys`](/documentation/Security/errSecMultiplePrivKeys)

An attempt was made to import multiple private keys.

[`errSecMultipleValuesUnsupported`](/documentation/Security/errSecMultipleValuesUnsupported)

Multiple values are not supported.

[`errSecNoAccessForItem`](/documentation/Security/errSecNoAccessForItem)

The specified item has no access control.

[`errSecNoBasicConstraints`](/documentation/Security/errSecNoBasicConstraints)

No basic constraints were found.

[`errSecNoBasicConstraintsCA`](/documentation/Security/errSecNoBasicConstraintsCA)

No basic CA constraints were found.

[`errSecNoDefaultAuthority`](/documentation/Security/errSecNoDefaultAuthority)

No default authority was detected.

[`errSecNoFieldValues`](/documentation/Security/errSecNoFieldValues)

No field values were detected.

[`errSecNoTrustSettings`](/documentation/Security/errSecNoTrustSettings)

No trust settings were found.

[`errSecNotInitialized`](/documentation/Security/errSecNotInitialized)

A function was called without initializing the common security services manager.

[`errSecNotLoggedIn`](/documentation/Security/errSecNotLoggedIn)

You are not logged in.

[`errSecNotSigner`](/documentation/Security/errSecNotSigner)

The certificate is not signed by its proposed parent.

[`errSecNotTrusted`](/documentation/Security/errSecNotTrusted)

The trust policy is not trusted.

[`errSecOutputLengthError`](/documentation/Security/errSecOutputLengthError)

An output length error was detected.

[`errSecPVCAlreadyConfigured`](/documentation/Security/errSecPVCAlreadyConfigured)

The PVC is already configured.

[`errSecPVCReferentNotFound`](/documentation/Security/errSecPVCReferentNotFound)

A reference to the calling module was not found in the list of authorized callers.

[`errSecPassphraseRequired`](/documentation/Security/errSecPassphraseRequired)

A password is required for import or export.

[`errSecPathLengthConstraintExceeded`](/documentation/Security/errSecPathLengthConstraintExceeded)

The path length constraint was exceeded.

[`errSecPkcs12VerifyFailure`](/documentation/Security/errSecPkcs12VerifyFailure)

MAC verification failed during PKCS12 Import.

[`errSecPolicyNotFound`](/documentation/Security/errSecPolicyNotFound)

The specified policy cannot be found.

[`errSecPrivilegeNotGranted`](/documentation/Security/errSecPrivilegeNotGranted)

The privilege is not granted.

[`errSecPrivilegeNotSupported`](/documentation/Security/errSecPrivilegeNotSupported)

The privilege is not supported.

[`errSecPublicKeyInconsistent`](/documentation/Security/errSecPublicKeyInconsistent)

The public key is inconsistent.

[`errSecQuerySizeUnknown`](/documentation/Security/errSecQuerySizeUnknown)

The query size is unknown.

[`errSecQuotaExceeded`](/documentation/Security/errSecQuotaExceeded)

The quota was exceeded.

[`errSecRejectedForm`](/documentation/Security/errSecRejectedForm)

The trust policy has a rejected form.

[`errSecRequestDescriptor`](/documentation/Security/errSecRequestDescriptor)

The request descriptor is not valid.

[`errSecRequestLost`](/documentation/Security/errSecRequestLost)

The request is lost.

[`errSecRequestRejected`](/documentation/Security/errSecRequestRejected)

The request is rejected.

[`errSecSelfCheckFailed`](/documentation/Security/errSecSelfCheckFailed)

Self-check failed.

[`errSecServiceNotAvailable`](/documentation/Security/errSecServiceNotAvailable)

Self-check failed.

[`errSecStagedOperationInProgress`](/documentation/Security/errSecStagedOperationInProgress)

A staged operation is in progress.

[`errSecStagedOperationNotStarted`](/documentation/Security/errSecStagedOperationNotStarted)

A staged operation was not started.

[`errSecTagNotFound`](/documentation/Security/errSecTagNotFound)

The specified tag is not found.

[`errSecTrustNotAvailable`](/documentation/Security/errSecTrustNotAvailable)

No trust results are available.

[`errSecUnknownFormat`](/documentation/Security/errSecUnknownFormat)

The item you are trying to import has an unknown format.

[`errSecUnknownTag`](/documentation/Security/errSecUnknownTag)

An unknown tag was detected.

[`errSecVerificationFailure`](/documentation/Security/errSecVerificationFailure)

A verification failure occurred.

[`errSecVerifyActionFailed`](/documentation/Security/errSecVerifyActionFailed)

A verify action failed.

[`errSecVerifyFailed`](/documentation/Security/errSecVerifyFailed)

A cryptographic verification failure occurred.

## See Also

[Sessions API Result Codes](/documentation/Security/sessions-api-result-codes)

Recognize result codes specific to the sessions API.

[Secure Transport Result Codes](/documentation/Security/secure-transport-result-codes)

Recognize result codes specific to the secure transport API.

[Code Signing Services Result Codes](/documentation/Security/code-signing-services-result-codes)

Recognize result codes specific to the code signing services API.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
