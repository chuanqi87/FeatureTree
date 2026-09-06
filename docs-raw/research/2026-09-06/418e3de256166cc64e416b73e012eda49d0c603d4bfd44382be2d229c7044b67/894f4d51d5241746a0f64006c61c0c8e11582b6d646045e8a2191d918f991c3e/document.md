# Core AI

Run AI models in your app on Apple silicon.

## Overview

Core AI helps you build, run, and deploy AI models in your app. Designed with Apple silicon in mind, Core AI allows your app to use the latest model architectures and inference techniques across the CPU, GPU, and Neural Engine. The Swift API makes common tasks simple, while giving you more control over model specialization, caching, and inference performance when needed.

![An illustration showing AI models connecting to Apple devices.](images/com.apple.coreai/core-ai-framework-hero@2x.png)

Alongside the framework, Core AI includes additional tools for model preparation, integration, and debugging. Prepare your models for Apple silicon with [Core AI Optimization](https://apple.github.io/coreai-optimization), then convert them into the `.aimodel` format with [Core AI PyTorch Extensions](https://apple.github.io/coreai-torch). The [Core AI Debugger](https://developer.apple.com/core-ai-debugger/) app supports visualization and numeric debugging, letting you inspect model structure and trace tensor values directly back to your Python source code. For a catalog of ready-to-export models and a Swift package with helpers for common inference patterns, see [Core AI Models](https://github.com/apple/coreai-models).

Core AI also integrates with Xcode and the developer toolchain. The Core AI debug gauge and Core AI instrument help you monitor and profile inference performance in your app. You can also compile models ahead of time with the `coreai-build` command-line tool.

If your app uses model types other than neural networks, such as decision trees or tabular feature engineering, see <doc://com.apple.documentation/documentation/CoreML>.

## Topics

### Essentials

[Integrating on-device AI models in your app with Core AI](/documentation/CoreAI/integrating-on-device-ai-models-in-your-app-with-core-ai)

Power your app’s intelligent features with an on-device AI model.

[`AIModel`](/documentation/CoreAI/AIModel)

A specialized model for running inference on a device.

[`AIModelAsset`](/documentation/CoreAI/AIModelAsset)

An unspecialized source model asset.

### Inference

[`InferenceFunction`](/documentation/CoreAI/InferenceFunction)

A function that performs inference on input values and produces output values.

[`InferenceFunctionDescriptor`](/documentation/CoreAI/InferenceFunctionDescriptor)

A description of an inference function’s signature.

[`InferenceValue`](/documentation/CoreAI/InferenceValue)

A value that an inference function accepts as input or produces as output.

[`ImageDescriptor`](/documentation/CoreAI/ImageDescriptor)

A description of an image’s dimensions and pixel format.

[`ComputeStream`](/documentation/CoreAI/ComputeStream)

A stream of work to be run asynchronously.

### Multidimensional arrays

[`NDArray`](/documentation/CoreAI/NDArray)

A multidimensional array of scalar values used for model inference.

[`NDArrayDescriptor`](/documentation/CoreAI/NDArrayDescriptor)

A description of an array’s shape, scalar type, and memory layout expectations.

### Configuration

[Managing model specialization and caching](/documentation/CoreAI/managing-model-specialization-and-caching)

Configure model specialization, manage cached assets, and reduce your app’s storage footprint.

[Compiling Core AI models ahead of time](/documentation/CoreAI/compiling-core-ai-models-ahead-of-time)

Reduce on-device specialization time by compiling Core AI models at build time.

[`AIModelCache`](/documentation/CoreAI/AIModelCache)

A cache that stores the specialized model artifacts for inference.

[`ComputeUnitKind`](/documentation/CoreAI/ComputeUnitKind)

A type of hardware compute unit available for model inference.

[`SpecializationOptions`](/documentation/CoreAI/SpecializationOptions)

### Debugging and performance

[Inspecting, debugging, and profiling Core AI models](/documentation/CoreAI/inspecting-debugging-and-profiling-core-ai-models)

Investigate model behavior, monitor activity, and profile performance using the Core AI tools across Xcode and the Core AI Debugger app.

### Errors

[`AssetError`](/documentation/CoreAI/AssetError)

An error that occurs during model asset operations.

### Internal types

**Engineering:** These internal types are visible in public SDK.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
