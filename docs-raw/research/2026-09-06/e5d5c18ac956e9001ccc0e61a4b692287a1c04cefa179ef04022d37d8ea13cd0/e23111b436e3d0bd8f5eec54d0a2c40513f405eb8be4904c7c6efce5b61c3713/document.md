# Apple CryptoKit

Perform cryptographic operations securely and efficiently.

## Overview

Use Apple CryptoKit to perform common cryptographic operations:

- Compute and compare cryptographically secure digests.
- Use public-key cryptography to create and evaluate digital signatures, and to
  perform key exchange. In addition to working with keys stored in memory, you
  can also use private keys stored in and managed by the Secure Enclave.
- Generate symmetric keys, and use them in operations like message
  authentication and encryption.

Prefer CryptoKit over lower-level interfaces. CryptoKit frees your app from
managing raw pointers, and automatically handles tasks that make your app more
secure, like overwriting sensitive data during memory deallocation.

## Topics

### Essentials

  <doc://com.apple.documentation/documentation/Security/complying-with-encryption-export-regulations>

[Performing Common Cryptographic Operations](/documentation/CryptoKit/performing-common-cryptographic-operations)

Use CryptoKit to carry out operations like hashing, key generation, and encryption.

[Storing CryptoKit Keys in the Keychain](/documentation/CryptoKit/storing-cryptokit-keys-in-the-keychain)

Convert between strongly typed cryptographic keys and native keychain types.

[Enhancing your app’s privacy and security with quantum-secure workflows](/documentation/CryptoKit/enhancing-your-app-s-privacy-and-security-with-quantum-secure-workflows)

Use quantum-secure cryptography to protect your app from quantum attacks.

### Cryptographically secure hashes

[`HashFunction`](/documentation/CryptoKit/HashFunction)

A type that performs cryptographically secure hashing.

[`SHA512`](/documentation/CryptoKit/SHA512)

An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a
512-bit digest.

[`SHA384`](/documentation/CryptoKit/SHA384)

An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a
384-bit digest.

[`SHA256`](/documentation/CryptoKit/SHA256)

An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a
256-bit digest.

### Message authentication codes

[`HMAC`](/documentation/CryptoKit/HMAC)

A hash-based message authentication algorithm.

[`SymmetricKey`](/documentation/CryptoKit/SymmetricKey)

A symmetric cryptographic key.

[`SymmetricKeySize`](/documentation/CryptoKit/SymmetricKeySize)

The sizes that a symmetric cryptographic key can take.

### Ciphers

[`AES`](/documentation/CryptoKit/AES)

A container for Advanced Encryption Standard (AES) ciphers.

[`ChaChaPoly`](/documentation/CryptoKit/ChaChaPoly)

An implementation of the ChaCha20-Poly1305 cipher.

### Public key cryptography

[`Curve25519`](/documentation/CryptoKit/Curve25519)

An elliptic curve that enables X25519 key agreement and Ed25519 signatures.

[`P521`](/documentation/CryptoKit/P521)

An elliptic curve that enables NIST P-521 signatures and key agreement.

[`P384`](/documentation/CryptoKit/P384)

An elliptic curve that enables NIST P-384 signatures and key agreement.

[`P256`](/documentation/CryptoKit/P256)

An elliptic curve that enables NIST P-256 signatures and key agreement.

[`SharedSecret`](/documentation/CryptoKit/SharedSecret)

A key agreement result from which you can derive a symmetric cryptographic
key.

[`SecureEnclave`](/documentation/CryptoKit/SecureEnclave)

A representation of a device’s hardware-based key manager.

[`HPKE`](/documentation/CryptoKit/HPKE)

A container for hybrid public key encryption (HPKE) operations.

### Key derivation functions

[`HKDF`](/documentation/CryptoKit/HKDF)

A standards-based implementation of an HMAC-based Key Derivation Function
(HKDF).

### Key encapsulation mechanisms (KEM)

[`KEM`](/documentation/CryptoKit/KEM)

A key encapsulation mechanism.

[`MLKEM768`](/documentation/CryptoKit/MLKEM768)

The Module-Lattice key encapsulation mechanism (KEM).

[`MLKEM1024`](/documentation/CryptoKit/MLKEM1024)

The Module-Lattice key encapsulation mechanism (KEM).

[`XWingMLKEM768X25519`](/documentation/CryptoKit/XWingMLKEM768X25519)

The X-Wing (ML-KEM768 with X25519) Key Encapsulation Mechanism, defined in
https://datatracker.ietf.org/doc/html/draft-connolly-cfrg-xwing-kem-06

### KEM keys

[`KEMPrivateKey`](/documentation/CryptoKit/KEMPrivateKey)

The private key for a key encapsulation mechanism.

[`KEMPublicKey`](/documentation/CryptoKit/KEMPublicKey)

The public key for a key encapsulation mechanism.

### Errors

[`CryptoKitError`](/documentation/CryptoKit/CryptoKitError)

General cryptography errors used by CryptoKit.

[`CryptoKitASN1Error`](/documentation/CryptoKit/CryptoKitASN1Error)

Errors from decoding ASN.1 content.

### Legacy algorithms

[`Insecure`](/documentation/CryptoKit/Insecure)

A container for older, cryptographically insecure algorithms.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
