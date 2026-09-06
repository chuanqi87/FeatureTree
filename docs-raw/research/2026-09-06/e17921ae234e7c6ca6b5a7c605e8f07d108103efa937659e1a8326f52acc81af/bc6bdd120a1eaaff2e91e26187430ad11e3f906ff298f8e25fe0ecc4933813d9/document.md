# CFStream Socket Security Level Constants

Constants for setting the security level of a socket stream.

## Discussion

This enumeration defines the preferred constants for setting the security protocol for a socket stream pair when calling [`CFReadStreamSetProperty(_:_:_:)`](/documentation/CoreFoundation/CFReadStreamSetProperty(_:_:_:)) or [`CFWriteStreamSetProperty(_:_:_:)`](/documentation/CoreFoundation/CFWriteStreamSetProperty(_:_:_:)).

## Topics

### Constants

[`kCFStreamSocketSecurityLevelNone`](/documentation/CoreFoundation/kCFStreamSocketSecurityLevelNone)

Specifies that no security level be set.

[`kCFStreamSocketSecurityLevelSSLv2`](/documentation/CoreFoundation/kCFStreamSocketSecurityLevelSSLv2)

Specifies that SSL version 2 be set as the security protocol for a socket stream.

[`kCFStreamSocketSecurityLevelSSLv3`](/documentation/CoreFoundation/kCFStreamSocketSecurityLevelSSLv3)

Specifies that SSL version 3 be set as the security protocol for a socket stream pair.

[`kCFStreamSocketSecurityLevelTLSv1`](/documentation/CoreFoundation/kCFStreamSocketSecurityLevelTLSv1)

Specifies that TLS version 1 be set as the security protocol for a socket stream.

[`kCFStreamSocketSecurityLevelNegotiatedSSL`](/documentation/CoreFoundation/kCFStreamSocketSecurityLevelNegotiatedSSL)

Specifies that the highest level security protocol that can be negotiated be set as the security protocol for a socket stream.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
