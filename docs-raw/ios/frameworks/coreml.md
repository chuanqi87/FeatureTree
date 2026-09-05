* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/coreml#app-main)

Framework

# Core ML

Integrate machine learning models into your app.

iOS 11.0+iPadOS 11.0+Mac Catalyst 13.0+macOS 10.13+tvOS 11.0+visionOS 1.0+watchOS 4.0+

## [Overview](https://developer.apple.com/documentation/coreml\#overview)

Use [Core ML](https://developer.apple.com/documentation/coreml) to integrate machine learning models into your app. [Core ML](https://developer.apple.com/documentation/coreml) provides a unified representation for all models. Your app uses [Core ML](https://developer.apple.com/documentation/coreml) APIs and user data to make predictions, and to train or fine-tune models, all on a person’s device.

![Flow diagram going from left to right. Starting on the left is a Core ML model file icon. Next, in the center is the Core ML framework icon, and on the right is a generic app icon, labeled “your app”.](https://developer.apple.com/tutorials/images/com.apple.coreml/media-3901331@2x.png)

A model is the result of applying a machine learning algorithm to a set of training data. You use a model to make predictions based on new input data. Models can accomplish a wide variety of tasks that would be difficult or impractical to write in code. For example, you can train a model to categorize photos, or detect specific objects within a photo directly from its pixels.

You build and train a model with the [Create ML app](https://developer.apple.com/machine-learning/create-ml/) bundled with Xcode. Models trained using [Create ML](https://developer.apple.com/documentation/createml) are in the [Core ML](https://developer.apple.com/documentation/coreml) model format and are ready to use in your app. Alternatively, you can use a wide variety of other machine learning libraries and then use [Core ML Tools](https://coremltools.readme.io/) to convert the model into the [Core ML](https://developer.apple.com/documentation/coreml) format. Once a model is on a person’s device, you can use [Core ML](https://developer.apple.com/documentation/coreml) to retrain or fine-tune it on-device, with that person’s data.

[Core ML](https://developer.apple.com/documentation/coreml) optimizes on-device performance by leveraging the CPU, GPU, and Neural Engine while minimizing its memory footprint and power consumption. Running a model strictly on a person’s device removes any need for a network connection, which helps keep a person’s data private and your app responsive.

The framework is the foundation for domain-specific frameworks and functionality. It supports [Vision](https://developer.apple.com/documentation/vision) for analyzing images, [Natural Language](https://developer.apple.com/documentation/naturallanguage) for processing text, [Speech](https://developer.apple.com/documentation/speech) for converting audio to text, and [Sound Analysis](https://developer.apple.com/documentation/soundanalysis) for identifying sounds in audio. [Core ML](https://developer.apple.com/documentation/coreml) itself builds on top of low-level primitives like [Accelerate](https://developer.apple.com/documentation/accelerate) and [BNNS](https://developer.apple.com/documentation/accelerate/bnns-library), as well as [Metal Performance Shaders](https://developer.apple.com/documentation/metalperformanceshaders).

![A block diagram of the machine learning stack. The top layer is a single block labeled “Your app,” which spans the entire width of the block diagram. The second layer has four blocks labeled “Vision,” “Natural Language,” “Speech,” and “Sound Analysis.” The third layer is labeled “Core ML,” which also spans the entire width. The fourth and final layer has two blocks, “Accelerate and BNNS” and “Metal Performance Shaders.”](https://developer.apple.com/tutorials/images/com.apple.coreml/media-3330367@2x.png)

If your app integrates AI models using the latest architectures and inference techniques, see [Core AI](https://developer.apple.com/documentation/coreai).

## [Topics](https://developer.apple.com/documentation/coreml\#topics)

### [Core ML models](https://developer.apple.com/documentation/coreml\#Core-ML-models)

[Getting a Core ML Model](https://developer.apple.com/documentation/coreml/getting-a-core-ml-model)

Obtain a Core ML model to use in your app.

[Updating a Model File to a Model Package](https://developer.apple.com/documentation/coreml/updating-a-model-file-to-a-model-package)

Convert a Core ML model file into a model package in Xcode.

[Integrating a Core ML Model into Your App](https://developer.apple.com/documentation/coreml/integrating-a-core-ml-model-into-your-app)

Add a simple model to an app, pass input data to the model, and process the model’s predictions.

[`class MLModel`](https://developer.apple.com/documentation/coreml/mlmodel)

An encapsulation of all the details of your machine learning model.

[API Reference\\
Model Customization](https://developer.apple.com/documentation/coreml/model-customization)

Expand and modify your model with new layers.

[API Reference\\
Model Personalization](https://developer.apple.com/documentation/coreml/model-personalization)

Update your model to adapt to new data.

### [Model inputs and outputs](https://developer.apple.com/documentation/coreml\#Model-inputs-and-outputs)

[Making Predictions with a Sequence of Inputs](https://developer.apple.com/documentation/coreml/making-predictions-with-a-sequence-of-inputs)

Integrate a recurrent neural network model to process sequences of inputs.

[`class MLFeatureValue`](https://developer.apple.com/documentation/coreml/mlfeaturevalue)

A generic wrapper around an underlying value and the value’s type.

[`struct MLSendableFeatureValue`](https://developer.apple.com/documentation/coreml/mlsendablefeaturevalue)

A sendable feature value.

[`protocol MLFeatureProvider`](https://developer.apple.com/documentation/coreml/mlfeatureprovider)

An interface that represents a collection of values for either a model’s input or its output.

[`class MLDictionaryFeatureProvider`](https://developer.apple.com/documentation/coreml/mldictionaryfeatureprovider)

A convenience wrapper for the given dictionary of data.

[`protocol MLBatchProvider`](https://developer.apple.com/documentation/coreml/mlbatchprovider)

An interface that represents a collection of feature providers.

[`class MLArrayBatchProvider`](https://developer.apple.com/documentation/coreml/mlarraybatchprovider)

A convenience wrapper for batches of feature providers.

[`class MLModelAsset`](https://developer.apple.com/documentation/coreml/mlmodelasset)

An abstraction of a compiled Core ML model asset.

### [App integration](https://developer.apple.com/documentation/coreml\#App-integration)

[Downloading and Compiling a Model on the User’s Device](https://developer.apple.com/documentation/coreml/downloading-and-compiling-a-model-on-the-user-s-device)

Install Core ML models on the user’s device dynamically at runtime.

[API Reference\\
Model Integration Samples](https://developer.apple.com/documentation/coreml/model-integration-samples)

Integrate tabular, image, and text classifcation models into your app.

### [Model encryption](https://developer.apple.com/documentation/coreml\#Model-encryption)

[Generating a Model Encryption Key](https://developer.apple.com/documentation/coreml/generating-a-model-encryption-key)

Create a model encryption key to encrypt a compiled model or model archive.

[Encrypting a Model in Your App](https://developer.apple.com/documentation/coreml/encrypting-a-model-in-your-app)

Encrypt your app’s built-in model at compile time by adding a compiler flag.

### [Compute devices](https://developer.apple.com/documentation/coreml\#Compute-devices)

[`enum MLComputeDevice`](https://developer.apple.com/documentation/coreml/mlcomputedevice)

Compute devices for framework operations.

[`class MLCPUComputeDevice`](https://developer.apple.com/documentation/coreml/mlcpucomputedevice)

An object that represents a CPU compute device.

[`class MLGPUComputeDevice`](https://developer.apple.com/documentation/coreml/mlgpucomputedevice)

An object that represents a GPU compute device.

[`class MLNeuralEngineComputeDevice`](https://developer.apple.com/documentation/coreml/mlneuralenginecomputedevice)

An object that represents a Neural Engine compute device.

[`protocol MLComputeDeviceProtocol`](https://developer.apple.com/documentation/coreml/mlcomputedeviceprotocol)

An interface that represents a compute device type.

### [Compute plan](https://developer.apple.com/documentation/coreml\#Compute-plan)

[`class MLComputePlan`](https://developer.apple.com/documentation/coreml/mlcomputeplan-1w21n)

A class representing the compute plan of a model.

[`enum MLModelStructure`](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum)

An enum representing the structure of a model.

[`struct MLComputePolicy`](https://developer.apple.com/documentation/coreml/mlcomputepolicy)

The compute policy determining what compute device, or compute devices, to execute ML workloads on.

[`func withMLTensorComputePolicy<R>(MLComputePolicy, () async throws -> R) async rethrows -> R`](https://developer.apple.com/documentation/coreml/withmltensorcomputepolicy(_:_:)-8stx9)

Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.

[`func withMLTensorComputePolicy<Result>(MLComputePolicy, () throws -> Result) rethrows -> Result`](https://developer.apple.com/documentation/coreml/withmltensorcomputepolicy(_:_:)-6z33x)

Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.

### [Model state](https://developer.apple.com/documentation/coreml\#Model-state)

[`class MLState`](https://developer.apple.com/documentation/coreml/mlstate)

Handle to the state buffers.

[`class MLStateConstraint`](https://developer.apple.com/documentation/coreml/mlstateconstraint)

Constraint of a state feature value.

### [Model tensor](https://developer.apple.com/documentation/coreml\#Model-tensor)

[`struct MLTensor`](https://developer.apple.com/documentation/coreml/mltensor)

A multi-dimensional array of numerical or Boolean scalars tailored to ML use cases, containing methods to perform transformations and mathematical operations efficiently using a ML compute device.

[`protocol MLTensorScalar`](https://developer.apple.com/documentation/coreml/mltensorscalar)

A type that represents the tensor scalar types supported by the framework. Don’t use this type directly.

[`protocol MLTensorRangeExpression`](https://developer.apple.com/documentation/coreml/mltensorrangeexpression)

A type that can be used to slice a dimension of a tensor. Don’t use this type directly.

[`func pointwiseMin(_:_:)`](https://developer.apple.com/documentation/coreml/pointwisemin(_:_:))

Computes the element-wise minimum of two tensors.

[`func pointwiseMax(_:_:)`](https://developer.apple.com/documentation/coreml/pointwisemax(_:_:))

Computes the element-wise minimum between two tensors.

[`func withMLTensorComputePolicy(_:_:)`](https://developer.apple.com/documentation/coreml/withmltensorcomputepolicy(_:_:))

Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.

### [Model structure](https://developer.apple.com/documentation/coreml\#Model-structure)

[`enum MLModelStructure`](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum)

An enum representing the structure of a model.

### [Model errors](https://developer.apple.com/documentation/coreml\#Model-errors)

[`struct MLModelError`](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct)

Information about a Core ML model error.

[`enum Code`](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct/code)

Information about a Core ML model error.

[`let MLModelErrorDomain: String`](https://developer.apple.com/documentation/coreml/mlmodelerrordomain)

The domain for Core ML errors.

### [Model deployments](https://developer.apple.com/documentation/coreml\#Model-deployments)

[`class MLModelCollection`](https://developer.apple.com/documentation/coreml/mlmodelcollection)

A set of Core ML models from a model deployment.

Deprecated

### [Reference](https://developer.apple.com/documentation/coreml\#Reference)

[API Reference\\
CoreML Enumerations](https://developer.apple.com/documentation/coreml/coreml-enumerations)

Current page is Core ML