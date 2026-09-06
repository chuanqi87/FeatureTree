# java.security.spec

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# java.security.spec

Provides classes and interfaces for key specifications and algorithm
parameter specifications.

A key specification is a transparent representation of the key material
that constitutes a key. A key may be specified in an algorithm-specific
way, or in an algorithm-independent encoding format (such as ASN.1).
This package contains key specifications for DSA public and private keys,
RSA public and private keys, PKCS #8 private keys in DER-encoded format,
and X.509 public and private keys in DER-encoded format.

An algorithm parameter specification is a transparent representation
of the sets of parameters used with an algorithm. This package contains
an algorithm parameter specification for parameters used with the
DSA algorithm.

## Package Specification

* PKCS #1: RSA Cryptography Specifications, Version 2.2 (RFC 8017)
* PKCS #8: Private-Key Information Syntax Standard,
  Version 1.2, November 1993
* Federal Information Processing Standards Publication (FIPS PUB) 186:
  Digital Signature Standard (DSS)

## Related Documentation

For documentation that includes information about algorithm parameter
and key specifications, please see:

* [**Java™
  Cryptography Architecture API Specification and Reference**](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html)
* [**How to Implement a Provider for the
  Java™ Cryptography Architecture**](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/HowToImplAProvider.html)

## Interfaces

|  |  |
| --- | --- |
| [AlgorithmParameterSpec](https://developer.android.com/reference/java/security/spec/AlgorithmParameterSpec) | A (transparent) specification of cryptographic parameters. |
| [ECField](https://developer.android.com/reference/java/security/spec/ECField) | This interface represents an elliptic curve (EC) finite field. |
| [KeySpec](https://developer.android.com/reference/java/security/spec/KeySpec) | A (transparent) specification of the key material that constitutes a cryptographic key. |

## Classes

|  |  |
| --- | --- |
| [DSAGenParameterSpec](https://developer.android.com/reference/java/security/spec/DSAGenParameterSpec) | This immutable class specifies the set of parameters used for generating DSA parameters as specified in [FIPS 186-3 Digital Signature Standard (DSS)](http://csrc.nist.gov/publications/fips/fips186-3/fips_186-3.pdf). |
| [DSAParameterSpec](https://developer.android.com/reference/java/security/spec/DSAParameterSpec) | This class specifies the set of parameters used with the DSA algorithm. |
| [DSAPrivateKeySpec](https://developer.android.com/reference/java/security/spec/DSAPrivateKeySpec) | This class specifies a DSA private key with its associated parameters. |
| [DSAPublicKeySpec](https://developer.android.com/reference/java/security/spec/DSAPublicKeySpec) | This class specifies a DSA public key with its associated parameters. |
| [ECFieldF2m](https://developer.android.com/reference/java/security/spec/ECFieldF2m) | This immutable class defines an elliptic curve (EC) characteristic 2 finite field. |
| [ECFieldFp](https://developer.android.com/reference/java/security/spec/ECFieldFp) | This immutable class defines an elliptic curve (EC) prime finite field. |
| [ECGenParameterSpec](https://developer.android.com/reference/java/security/spec/ECGenParameterSpec) | This immutable class specifies the set of parameters used for generating elliptic curve (EC) domain parameters. |
| [ECParameterSpec](https://developer.android.com/reference/java/security/spec/ECParameterSpec) | This immutable class specifies the set of domain parameters used with elliptic curve cryptography (ECC). |
| [ECPoint](https://developer.android.com/reference/java/security/spec/ECPoint) | This immutable class represents a point on an elliptic curve (EC) in affine coordinates. |
| [ECPrivateKeySpec](https://developer.android.com/reference/java/security/spec/ECPrivateKeySpec) | This immutable class specifies an elliptic curve private key with its associated parameters. |
| [ECPublicKeySpec](https://developer.android.com/reference/java/security/spec/ECPublicKeySpec) | This immutable class specifies an elliptic curve public key with its associated parameters. |
| [EdDSAParameterSpec](https://developer.android.com/reference/java/security/spec/EdDSAParameterSpec) | A class used to specify EdDSA signature and verification parameters. |
| [EdECPoint](https://developer.android.com/reference/java/security/spec/EdECPoint) | An elliptic curve point used to specify keys as defined by [RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA)](https://tools.ietf.org/html/rfc8032). |
| [EdECPrivateKeySpec](https://developer.android.com/reference/java/security/spec/EdECPrivateKeySpec) | A class representing elliptic curve private keys as defined in [RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA)](https://tools.ietf.org/html/rfc8032), including the curve and other algorithm parameters. |
| [EdECPublicKeySpec](https://developer.android.com/reference/java/security/spec/EdECPublicKeySpec) | A class representing elliptic curve public keys as defined in [RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA)](https://tools.ietf.org/html/rfc8032), including the curve and other algorithm parameters. |
| [EllipticCurve](https://developer.android.com/reference/java/security/spec/EllipticCurve) | This immutable class holds the necessary values needed to represent an elliptic curve. |
| [EncodedKeySpec](https://developer.android.com/reference/java/security/spec/EncodedKeySpec) | This class represents a public or private key in encoded format. |
| [MGF1ParameterSpec](https://developer.android.com/reference/java/security/spec/MGF1ParameterSpec) | This class specifies the set of parameters used with mask generation function MGF1 in OAEP Padding and RSASSA-PSS signature scheme, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard. |
| [NamedParameterSpec](https://developer.android.com/reference/java/security/spec/NamedParameterSpec) | This class is used to specify any algorithm parameters that are determined by a standard name. |
| [PKCS8EncodedKeySpec](https://developer.android.com/reference/java/security/spec/PKCS8EncodedKeySpec) | This class represents the ASN.1 encoding of a private key, encoded according to the ASN.1 type `PrivateKeyInfo`. |
| [PSSParameterSpec](https://developer.android.com/reference/java/security/spec/PSSParameterSpec) | This class specifies a parameter spec for RSASSA-PSS signature scheme, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard. |
| [RSAKeyGenParameterSpec](https://developer.android.com/reference/java/security/spec/RSAKeyGenParameterSpec) | This class specifies the set of parameters used to generate an RSA key pair. |
| [RSAMultiPrimePrivateCrtKeySpec](https://developer.android.com/reference/java/security/spec/RSAMultiPrimePrivateCrtKeySpec) | This class specifies an RSA multi-prime private key, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard using the Chinese Remainder Theorem (CRT) information values for efficiency. |
| [RSAOtherPrimeInfo](https://developer.android.com/reference/java/security/spec/RSAOtherPrimeInfo) | This class represents the triplet (prime, exponent, and coefficient) inside RSA's OtherPrimeInfo structure, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard. |
| [RSAPrivateCrtKeySpec](https://developer.android.com/reference/java/security/spec/RSAPrivateCrtKeySpec) | This class specifies an RSA private key, as defined in the [PKCS#1 v2.2](https://tools.ietf.org/rfc/rfc8017.txt) standard, using the Chinese Remainder Theorem (CRT) information values for efficiency. |
| [RSAPrivateKeySpec](https://developer.android.com/reference/java/security/spec/RSAPrivateKeySpec) | This class specifies an RSA private key. |
| [RSAPublicKeySpec](https://developer.android.com/reference/java/security/spec/RSAPublicKeySpec) | This class specifies an RSA public key. |
| [X509EncodedKeySpec](https://developer.android.com/reference/java/security/spec/X509EncodedKeySpec) | This class represents the ASN.1 encoding of a public key, encoded according to the ASN.1 type `SubjectPublicKeyInfo`. |
| [XECPrivateKeySpec](https://developer.android.com/reference/java/security/spec/XECPrivateKeySpec) | A class representing elliptic curve private keys as defined in RFC 7748, including the curve and other algorithm parameters. |
| [XECPublicKeySpec](https://developer.android.com/reference/java/security/spec/XECPublicKeySpec) | A class representing elliptic curve public keys as defined in RFC 7748, including the curve and other algorithm parameters. |

## Exceptions

|  |  |
| --- | --- |
| [InvalidKeySpecException](https://developer.android.com/reference/java/security/spec/InvalidKeySpecException) | This is the exception for invalid key specifications. |
| [InvalidParameterSpecException](https://developer.android.com/reference/java/security/spec/InvalidParameterSpecException) | This is the exception for invalid parameter specifications. |

* ## Interfaces

  + [AlgorithmParameterSpec](https://developer.android.com/reference/java/security/spec/AlgorithmParameterSpec)
  + [ECField](https://developer.android.com/reference/java/security/spec/ECField)
  + [KeySpec](https://developer.android.com/reference/java/security/spec/KeySpec)
* ## Classes

  + [DSAGenParameterSpec](https://developer.android.com/reference/java/security/spec/DSAGenParameterSpec)
  + [DSAParameterSpec](https://developer.android.com/reference/java/security/spec/DSAParameterSpec)
  + [DSAPrivateKeySpec](https://developer.android.com/reference/java/security/spec/DSAPrivateKeySpec)
  + [DSAPublicKeySpec](https://developer.android.com/reference/java/security/spec/DSAPublicKeySpec)
  + [ECFieldF2m](https://developer.android.com/reference/java/security/spec/ECFieldF2m)
  + [ECFieldFp](https://developer.android.com/reference/java/security/spec/ECFieldFp)
  + [ECGenParameterSpec](https://developer.android.com/reference/java/security/spec/ECGenParameterSpec)
  + [ECParameterSpec](https://developer.android.com/reference/java/security/spec/ECParameterSpec)
  + [ECPoint](https://developer.android.com/reference/java/security/spec/ECPoint)
  + [ECPrivateKeySpec](https://developer.android.com/reference/java/security/spec/ECPrivateKeySpec)
  + [ECPublicKeySpec](https://developer.android.com/reference/java/security/spec/ECPublicKeySpec)
  + [EdDSAParameterSpec](https://developer.android.com/reference/java/security/spec/EdDSAParameterSpec)
  + [EdECPoint](https://developer.android.com/reference/java/security/spec/EdECPoint)
  + [EdECPrivateKeySpec](https://developer.android.com/reference/java/security/spec/EdECPrivateKeySpec)
  + [EdECPublicKeySpec](https://developer.android.com/reference/java/security/spec/EdECPublicKeySpec)
  + [EllipticCurve](https://developer.android.com/reference/java/security/spec/EllipticCurve)
  + [EncodedKeySpec](https://developer.android.com/reference/java/security/spec/EncodedKeySpec)
  + [MGF1ParameterSpec](https://developer.android.com/reference/java/security/spec/MGF1ParameterSpec)
  + [NamedParameterSpec](https://developer.android.com/reference/java/security/spec/NamedParameterSpec)
  + [PKCS8EncodedKeySpec](https://developer.android.com/reference/java/security/spec/PKCS8EncodedKeySpec)
  + [PSSParameterSpec](https://developer.android.com/reference/java/security/spec/PSSParameterSpec)
  + [RSAKeyGenParameterSpec](https://developer.android.com/reference/java/security/spec/RSAKeyGenParameterSpec)
  + [RSAMultiPrimePrivateCrtKeySpec](https://developer.android.com/reference/java/security/spec/RSAMultiPrimePrivateCrtKeySpec)
  + [RSAOtherPrimeInfo](https://developer.android.com/reference/java/security/spec/RSAOtherPrimeInfo)
  + [RSAPrivateCrtKeySpec](https://developer.android.com/reference/java/security/spec/RSAPrivateCrtKeySpec)
  + [RSAPrivateKeySpec](https://developer.android.com/reference/java/security/spec/RSAPrivateKeySpec)
  + [RSAPublicKeySpec](https://developer.android.com/reference/java/security/spec/RSAPublicKeySpec)
  + [X509EncodedKeySpec](https://developer.android.com/reference/java/security/spec/X509EncodedKeySpec)
  + [XECPrivateKeySpec](https://developer.android.com/reference/java/security/spec/XECPrivateKeySpec)
  + [XECPublicKeySpec](https://developer.android.com/reference/java/security/spec/XECPublicKeySpec)
* ## Exceptions

  + [InvalidKeySpecException](https://developer.android.com/reference/java/security/spec/InvalidKeySpecException)
  + [InvalidParameterSpecException](https://developer.android.com/reference/java/security/spec/InvalidParameterSpecException)
