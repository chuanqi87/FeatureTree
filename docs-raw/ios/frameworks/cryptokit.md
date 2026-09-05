* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/cryptokit#app-main)

Framework

# Apple CryptoKit

Perform cryptographic operations securely and efficiently.

iOS 13.0+iPadOS 13.0+Mac Catalyst 15.0+macOS 10.15+tvOS 15.0+visionOS 1.0+watchOS 8.0+

## [Overview](https://developer.apple.com/documentation/cryptokit\#overview)

Use Apple CryptoKit to perform common cryptographic operations:

- Compute and compare cryptographically secure digests.

- Use public-key cryptography to create and evaluate digital signatures, and to perform key exchange. In addition to working with keys stored in memory, you can also use private keys stored in and managed by the Secure Enclave.

- Generate symmetric keys, and use them in operations like message authentication and encryption.


Prefer CryptoKit over lower-level interfaces. CryptoKit frees your app from managing raw pointers, and automatically handles tasks that make your app more secure, like overwriting sensitive data during memory deallocation.

## [Topics](https://developer.apple.com/documentation/cryptokit\#topics)

### [Essentials](https://developer.apple.com/documentation/cryptokit\#Essentials)

[API Reference\\
Complying with Encryption Export Regulations](https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations)

Declare the use of encryption in your app to streamline the app submission process.

[Performing Common Cryptographic Operations](https://developer.apple.com/documentation/cryptokit/performing-common-cryptographic-operations)

Use CryptoKit to carry out operations like hashing, key generation, and encryption.

[Storing CryptoKit Keys in the Keychain](https://developer.apple.com/documentation/cryptokit/storing-cryptokit-keys-in-the-keychain)

Convert between strongly typed cryptographic keys and native keychain types.

[Enhancing your app’s privacy and security with quantum-secure workflows](https://developer.apple.com/documentation/cryptokit/enhancing-your-app-s-privacy-and-security-with-quantum-secure-workflows)

Use quantum-secure cryptography to protect your app from quantum attacks.

### [Cryptographically secure hashes](https://developer.apple.com/documentation/cryptokit\#Cryptographically-secure-hashes)

[`protocol HashFunction`](https://developer.apple.com/documentation/cryptokit/hashfunction)

A type that performs cryptographically secure hashing.

[`struct SHA512`](https://developer.apple.com/documentation/cryptokit/sha512)

An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 512-bit digest.

[`struct SHA384`](https://developer.apple.com/documentation/cryptokit/sha384)

An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 384-bit digest.

[`struct SHA256`](https://developer.apple.com/documentation/cryptokit/sha256)

An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 256-bit digest.

### [Message authentication codes](https://developer.apple.com/documentation/cryptokit\#Message-authentication-codes)

[`struct HMAC`](https://developer.apple.com/documentation/cryptokit/hmac)

A hash-based message authentication algorithm.

[`struct SymmetricKey`](https://developer.apple.com/documentation/cryptokit/symmetrickey)

A symmetric cryptographic key.

[`struct SymmetricKeySize`](https://developer.apple.com/documentation/cryptokit/symmetrickeysize)

The sizes that a symmetric cryptographic key can take.

### [Ciphers](https://developer.apple.com/documentation/cryptokit\#Ciphers)

[`enum AES`](https://developer.apple.com/documentation/cryptokit/aes)

A container for Advanced Encryption Standard (AES) ciphers.

[`enum ChaChaPoly`](https://developer.apple.com/documentation/cryptokit/chachapoly)

An implementation of the ChaCha20-Poly1305 cipher.

### [Public key cryptography](https://developer.apple.com/documentation/cryptokit\#Public-key-cryptography)

[`enum Curve25519`](https://developer.apple.com/documentation/cryptokit/curve25519)

An elliptic curve that enables X25519 key agreement and Ed25519 signatures.

[`enum P521`](https://developer.apple.com/documentation/cryptokit/p521)

An elliptic curve that enables NIST P-521 signatures and key agreement.

[`enum P384`](https://developer.apple.com/documentation/cryptokit/p384)

An elliptic curve that enables NIST P-384 signatures and key agreement.

[`enum P256`](https://developer.apple.com/documentation/cryptokit/p256)

An elliptic curve that enables NIST P-256 signatures and key agreement.

[`struct SharedSecret`](https://developer.apple.com/documentation/cryptokit/sharedsecret)

A key agreement result from which you can derive a symmetric cryptographic key.

[`enum SecureEnclave`](https://developer.apple.com/documentation/cryptokit/secureenclave)

A representation of a device’s hardware-based key manager.

[`enum HPKE`](https://developer.apple.com/documentation/cryptokit/hpke)

A container for hybrid public key encryption (HPKE) operations.

### [Key derivation functions](https://developer.apple.com/documentation/cryptokit\#Key-derivation-functions)

[`struct HKDF`](https://developer.apple.com/documentation/cryptokit/hkdf)

A standards-based implementation of an HMAC-based Key Derivation Function (HKDF).

### [Key encapsulation mechanisms (KEM)](https://developer.apple.com/documentation/cryptokit\#Key-encapsulation-mechanisms-KEM)

[`enum KEM`](https://developer.apple.com/documentation/cryptokit/kem)

A key encapsulation mechanism.

[`enum MLKEM768`](https://developer.apple.com/documentation/cryptokit/mlkem768)

The Module-Lattice key encapsulation mechanism (KEM).

[`enum MLKEM1024`](https://developer.apple.com/documentation/cryptokit/mlkem1024)

The Module-Lattice key encapsulation mechanism (KEM).

[`enum XWingMLKEM768X25519`](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519)

The X-Wing (ML-KEM768 with X25519) Key Encapsulation Mechanism, defined in https://datatracker.ietf.org/doc/html/draft-connolly-cfrg-xwing-kem-06

### [KEM keys](https://developer.apple.com/documentation/cryptokit\#KEM-keys)

[`protocol KEMPrivateKey`](https://developer.apple.com/documentation/cryptokit/kemprivatekey)

The private key for a key encapsulation mechanism.

[`protocol KEMPublicKey`](https://developer.apple.com/documentation/cryptokit/kempublickey)

The public key for a key encapsulation mechanism.

### [Errors](https://developer.apple.com/documentation/cryptokit\#Errors)

[`enum CryptoKitError`](https://developer.apple.com/documentation/cryptokit/cryptokiterror)

General cryptography errors used by CryptoKit.

[`enum CryptoKitASN1Error`](https://developer.apple.com/documentation/cryptokit/cryptokitasn1error)

Errors from decoding ASN.1 content.

### [Legacy algorithms](https://developer.apple.com/documentation/cryptokit\#Legacy-algorithms)

[`enum Insecure`](https://developer.apple.com/documentation/cryptokit/insecure)

A container for older, cryptographically insecure algorithms.

### [Protocols](https://developer.apple.com/documentation/cryptokit\#Protocols)

[`protocol DiffieHellmanKeyAgreement`](https://developer.apple.com/documentation/cryptokit/diffiehellmankeyagreement)

A Diffie-Hellman Key Agreement Key

[`protocol HPKEDiffieHellmanPrivateKey`](https://developer.apple.com/documentation/cryptokit/hpkediffiehellmanprivatekey)

A type that represents the private key in a Diffie-Hellman key exchange.

[`protocol HPKEDiffieHellmanPrivateKeyGeneration`](https://developer.apple.com/documentation/cryptokit/hpkediffiehellmanprivatekeygeneration)

A type that represents the generation of private keys in a Diffie-Hellman key exchange.

[`protocol HPKEDiffieHellmanPublicKey`](https://developer.apple.com/documentation/cryptokit/hpkediffiehellmanpublickey)

A type that represents the public key in a Diffie-Hellman key exchange.

[`protocol HPKEKEMPrivateKey`](https://developer.apple.com/documentation/cryptokit/hpkekemprivatekey)

A type that represents the private key in HPKE.

[`protocol HPKEKEMPrivateKeyGeneration`](https://developer.apple.com/documentation/cryptokit/hpkekemprivatekeygeneration)

A type that represents the generation of private keys in HPKE

[`protocol HPKEKEMPublicKey`](https://developer.apple.com/documentation/cryptokit/hpkekempublickey)

A type that represents the public key in HPKE

[`protocol HPKEPublicKeySerialization`](https://developer.apple.com/documentation/cryptokit/hpkepublickeyserialization)

A type that [`HPKE`](https://developer.apple.com/documentation/cryptokit/hpke) uses to encode the public key.

[`protocol KEMOneTimePrivateKey`](https://developer.apple.com/documentation/cryptokit/kemonetimeprivatekey)

A one-time private key for a key encapsulation mechanism, which can only decapsulate once but it does so faster.

Beta

### [Structures](https://developer.apple.com/documentation/cryptokit\#Structures)

[`struct CorecryptoCurveType`](https://developer.apple.com/documentation/cryptokit/corecryptocurvetype)

[`struct SHA3_256`](https://developer.apple.com/documentation/cryptokit/sha3_256)

An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 256-bit digest.

[`struct SHA3_256Digest`](https://developer.apple.com/documentation/cryptokit/sha3_256digest)

The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 256-bit digest.

[`struct SHA3_384`](https://developer.apple.com/documentation/cryptokit/sha3_384)

An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 384-bit digest.

[`struct SHA3_384Digest`](https://developer.apple.com/documentation/cryptokit/sha3_384digest)

The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 384-bit digest.

[`struct SHA3_512`](https://developer.apple.com/documentation/cryptokit/sha3_512)

An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 512-bit digest.

[`struct SHA3_512Digest`](https://developer.apple.com/documentation/cryptokit/sha3_512digest)

The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 512-bit digest.

### [Type Aliases](https://developer.apple.com/documentation/cryptokit\#Type-Aliases)

[`typealias CryptoKitMetaError`](https://developer.apple.com/documentation/cryptokit/cryptokitmetaerror)

[`typealias SHA2_256`](https://developer.apple.com/documentation/cryptokit/sha2_256)

An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 256-bit digest.

[`typealias SHA2_384`](https://developer.apple.com/documentation/cryptokit/sha2_384)

An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 384-bit digest.

[`typealias SHA2_512`](https://developer.apple.com/documentation/cryptokit/sha2_512)

An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 512-bit digest.

### [Enumerations](https://developer.apple.com/documentation/cryptokit\#Enumerations)

[`enum MLDSA65`](https://developer.apple.com/documentation/cryptokit/mldsa65)

The MLDSA65 Digital Signature Algorithm

[`enum MLDSA87`](https://developer.apple.com/documentation/cryptokit/mldsa87)

The MLDSA87 Digital Signature Algorithm

Current page is Apple CryptoKit