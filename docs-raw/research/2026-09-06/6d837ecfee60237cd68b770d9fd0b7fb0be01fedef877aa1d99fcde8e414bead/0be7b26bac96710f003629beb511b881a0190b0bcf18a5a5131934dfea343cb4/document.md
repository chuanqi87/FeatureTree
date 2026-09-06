# Concurrency support

Types you use to access model attributes and perform storage-related tasks in
a safe and isolated way.

## Topics

### Model actors

[`ModelActor()`](/documentation/SwiftData/ModelActor())

Converts a Swift actor into a model actor by generating boilerplate code that
fulfills the requirements of the associated protocol.

[`ModelActor`](/documentation/SwiftData/ModelActor)

An interface for providing mutually-exclusive access to the attributes of a conforming model.

### Model executors

[`DefaultSerialModelExecutor`](/documentation/SwiftData/DefaultSerialModelExecutor)

An object that safely performs storage-related tasks using an isolated model context.

[`SerialModelExecutor`](/documentation/SwiftData/SerialModelExecutor)

An interface for performing serial storage-related tasks using an isolated model context.

[`ModelExecutor`](/documentation/SwiftData/ModelExecutor)

An interface for performing storage-related tasks using an isolated model context.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
