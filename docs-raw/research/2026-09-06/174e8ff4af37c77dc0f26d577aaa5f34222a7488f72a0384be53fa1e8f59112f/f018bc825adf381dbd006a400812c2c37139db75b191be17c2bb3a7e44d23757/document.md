# BrowserEngineCore

Integrate an alternative browser engine into your web browser app.

## Overview

Use the `BrowserEngineCore` framework to support low-level functions for your alternative browser engine that renders its UI using <doc://com.apple.documentation/documentation/BrowserEngineKit>.
For more information on developing web browser apps, see <doc://com.apple.documentation/documentation/BrowserEngineKit/designing-your-browser-architecture>.

## Topics

### Kernel events

[`be_kevent`](/documentation/BrowserEngineCore/be_kevent(_:_:_:_:_:_:))

Registers for kernel events on the specified queue, and returns events that are pending on the queue, using 32-bit data types.

[`be_kevent64`](/documentation/BrowserEngineCore/be_kevent64(_:_:_:_:_:_:))

Registers for kernel events on the specified queue, and returns events that are pending on the queue, using 64-bit data types.

[`BE_KEVENT_NO_FLAGS`](/documentation/BrowserEngineCore/BE_KEVENT_NO_FLAGS)

Indicates that no flags are set in a request to receive kernel events.

[`BE_KEVENT_RETURN_IMMEDIATELY`](/documentation/BrowserEngineCore/BE_KEVENT_RETURN_IMMEDIATELY)

Indicates that a request to receive kernel events needs to return without waiting for events.

### JIT compilation

[`be_memory_inline_jit_restrict_with_witness_supported`](/documentation/BrowserEngineCore/be_memory_inline_jit_restrict_with_witness_supported)

Reports whether write protection for just-in-time (JIT) compilation is available.

[`be_memory_inline_jit_restrict_rwx_to_rw_with_witness`](/documentation/BrowserEngineCore/be_memory_inline_jit_restrict_rwx_to_rw_with_witness)

Makes a region of memory writable for use in just-in-time (JIT) compilation.

[`be_memory_inline_jit_restrict_rwx_to_rx_with_witness`](/documentation/BrowserEngineCore/be_memory_inline_jit_restrict_rwx_to_rx_with_witness)

Makes a region of memory executable for use in just-in-time (JIT) compilation.

[`BE_JIT_WRITE_PROTECT_TAG`](/documentation/BrowserEngineCore/BE_JIT_WRITE_PROTECT_TAG)

A discriminator value the system uses to generate pointer authentication codes for just-in-time compilation.

### Audio preferences

[`BEAudioSession`](/documentation/BrowserEngineCore/BEAudioSession-7bb2q)

An object that wraps an AV audio session to scope the browser app’s audio session control.

[`BEAudioSession`](/documentation/BrowserEngineCore/BEAudioSession-6b7ig)

An object that wraps an AV audio session to scope the browser app’s audio session control.

### Memory-protection implementation

[`be_memory_inline_jit_restrict_rwx_to_rw_with_witness_impl`](/documentation/BrowserEngineCore/be_memory_inline_jit_restrict_rwx_to_rw_with_witness_impl)

Makes a region of memory writable for use in just-in-time (JIT) compilation.

[`be_memory_inline_jit_restrict_rwx_to_rx_with_witness_impl`](/documentation/BrowserEngineCore/be_memory_inline_jit_restrict_rwx_to_rx_with_witness_impl)

Makes a region of memory executable for use in just-in-time (JIT) compilation.

### API availability

[`BROWSERENGINE_ACCESSIBILITY_AVAILABILITY`](/documentation/BrowserEngineCore/BROWSERENGINE_ACCESSIBILITY_AVAILABILITY)

A macro the framework uses to indicate which SDK versions provide the accessibility APIs.

[`BROWSERENGINE_ACCESSIBILITY_MARKER_AVAILABILITY`](/documentation/BrowserEngineCore/BROWSERENGINE_ACCESSIBILITY_MARKER_AVAILABILITY)

A macro the framework uses to indicate which SDK versions provide the accessibility marker APIs.

[`BROWSERENGINE_ACCESSIBILITY_REMOTE_AVAILABILITY`](/documentation/BrowserEngineCore/BROWSERENGINE_ACCESSIBILITY_REMOTE_AVAILABILITY)

A macro that indicates the SDK versions that provide the APIs for accessibility remote elements.

[`BROWSERENGINE_TEXTINPUT_AVAILABILITY`](/documentation/BrowserEngineCore/BROWSERENGINE_TEXTINPUT_AVAILABILITY)

A macro the framework uses to indicate which SDK versions provide the text input APIs.

[`BROWSERENGINE_EXPORT`](/documentation/BrowserEngineCore/BROWSERENGINE_EXPORT)

A macro the framework uses to make API available for use in your code.

[`BROWSERENGINE_EXTERN`](/documentation/BrowserEngineCore/BROWSERENGINE_EXTERN)

A macro the framework uses to indicate that a symbol is defined in a different file.

[`BROWSERENGINE_FINAL`](/documentation/BrowserEngineCore/BROWSERENGINE_FINAL)

A macro the framework uses to indicate that an Objective-C class isn’t available for subclassing.

[`BROWSERENGINE_IMPORT`](/documentation/BrowserEngineCore/BROWSERENGINE_IMPORT)

A macro the framework uses to import APIs from other frameworks.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
