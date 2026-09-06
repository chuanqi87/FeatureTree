# Core ML

Integrate machine learning models into your app.

## Overview

Use [`Core ML`](/documentation/CoreML) to integrate machine learning models into your app. [`Core ML`](/documentation/CoreML) provides a unified representation for all models. Your app uses [`Core ML`](/documentation/CoreML) APIs and user data to make predictions, and to train or fine-tune models, all on a person’s device.

![Flow diagram going from left to right. Starting on the left is a Core ML model file icon. Next, in the center is the Core ML framework icon, and on the right is a generic app icon, labeled “your app”.](images/com.apple.coreml/media-3901331@2x.png)

A model is the result of applying a machine learning algorithm to a set of training data. You use a model to make predictions based on new input data. Models can accomplish a wide variety of tasks that would be difficult or impractical to write in code. For example, you can train a model to categorize photos, or detect specific objects within a photo directly from its pixels.

You build and train a model with the [Create ML app](https://developer.apple.com/machine-learning/create-ml/) bundled with Xcode. Models trained using <doc://com.apple.documentation/documentation/CreateML> are in the [`Core ML`](/documentation/CoreML) model format and are ready to use in your app. Alternatively, you can use a wide variety of other machine learning libraries and then use [Core ML Tools](https://coremltools.readme.io) to convert the model into the [`Core ML`](/documentation/CoreML) format. Once a model is on a person’s device, you can use [`Core ML`](/documentation/CoreML) to retrain or fine-tune it on-device, with that person’s data.

[`Core ML`](/documentation/CoreML) optimizes on-device performance by leveraging the CPU, GPU, and Neural Engine while minimizing its memory footprint and power consumption. Running a model strictly on a person’s device removes any need for a network connection, which helps keep a person’s data private and your app responsive.

The framework is the foundation for domain-specific frameworks and functionality. It supports <doc://com.apple.documentation/documentation/Vision> for analyzing images, <doc://com.apple.documentation/documentation/NaturalLanguage> for processing text, <doc://com.apple.documentation/documentation/Speech> for converting audio to text, and <doc://com.apple.documentation/documentation/SoundAnalysis> for identifying sounds in audio. [`Core ML`](/documentation/CoreML) itself builds on top of low-level primitives like <doc://com.apple.documentation/documentation/Accelerate> and <doc://com.apple.documentation/documentation/Accelerate/bnns-library>, as well as <doc://com.apple.documentation/documentation/MetalPerformanceShaders>.

![A block diagram of the machine learning stack. The top layer is a single block labeled “Your app,” which spans the entire width of the block diagram. The second layer has four blocks labeled “Vision,” “Natural Language,” “Speech,” and “Sound Analysis.” The third layer is labeled “Core ML,” which also spans the entire width. The fourth and final layer has two blocks, “Accelerate and BNNS” and “Metal Performance Shaders.”](images/com.apple.coreml/media-3330367@2x.png)

If your app integrates AI models using the latest architectures and inference
techniques, see <doc://com.apple.documentation/documentation/CoreAI>.

## Topics

### Core ML models

[Getting a Core ML Model](/documentation/CoreML/getting-a-core-ml-model)

Obtain a Core ML model to use in your app.

[Updating a Model File to a Model Package](/documentation/CoreML/updating-a-model-file-to-a-model-package)

Convert a Core ML model file into a model package in Xcode.

[Integrating a Core ML Model into Your App](/documentation/CoreML/integrating-a-core-ml-model-into-your-app)

Add a simple model to an app,
pass input data to the model, and process the model’s predictions.

[`MLModel`](/documentation/CoreML/MLModel)

An encapsulation of all the details of your machine learning model.

[Model Customization](/documentation/CoreML/model-customization)

Expand and modify your model with new layers.

[Model Personalization](/documentation/CoreML/model-personalization)

Update your model to adapt to new data.

### Model inputs and outputs

[Making Predictions with a Sequence of Inputs](/documentation/CoreML/making-predictions-with-a-sequence-of-inputs)

Integrate a recurrent neural network model to process sequences of inputs.

[`MLFeatureValue`](/documentation/CoreML/MLFeatureValue)

A generic wrapper around an underlying value and the value’s type.

[`MLSendableFeatureValue`](/documentation/CoreML/MLSendableFeatureValue)

A sendable feature value.

[`MLFeatureProvider`](/documentation/CoreML/MLFeatureProvider)

An interface that represents a collection of values for either a model’s input or its output.

[`MLDictionaryFeatureProvider`](/documentation/CoreML/MLDictionaryFeatureProvider)

A convenience wrapper for the given dictionary of data.

[`MLBatchProvider`](/documentation/CoreML/MLBatchProvider)

An interface that represents a collection of feature providers.

[`MLArrayBatchProvider`](/documentation/CoreML/MLArrayBatchProvider)

A convenience wrapper for batches of feature providers.

[`MLModelAsset`](/documentation/CoreML/MLModelAsset)

An abstraction of a compiled Core ML model asset.

### App integration

[Downloading and Compiling a Model on the User’s Device](/documentation/CoreML/downloading-and-compiling-a-model-on-the-user-s-device)

Install Core ML models on the user’s device dynamically at runtime.

[Model Integration Samples](/documentation/CoreML/model-integration-samples)

Integrate tabular, image, and text classifcation models into your app.

### Model encryption

[Generating a Model Encryption Key](/documentation/CoreML/generating-a-model-encryption-key)

Create a model encryption key to encrypt a compiled model or model archive.

[Encrypting a Model in Your App](/documentation/CoreML/encrypting-a-model-in-your-app)

Encrypt your app’s built-in model at compile time by adding a compiler flag.

### Compute devices

[`MLComputeDevice`](/documentation/CoreML/MLComputeDevice)

Compute devices for framework operations.

[`MLCPUComputeDevice`](/documentation/CoreML/MLCPUComputeDevice)

An object that represents a CPU compute device.

[`MLGPUComputeDevice`](/documentation/CoreML/MLGPUComputeDevice)

An object that represents a GPU compute device.

[`MLNeuralEngineComputeDevice`](/documentation/CoreML/MLNeuralEngineComputeDevice)

An object that represents a Neural Engine compute device.

[`MLComputeDeviceProtocol`](/documentation/CoreML/MLComputeDeviceProtocol)

An interface that represents a compute device type.

[`MLAllComputeDevices`](/documentation/CoreML/MLAllComputeDevices)

Returns an array that contains all of the compute devices that are accessible.

### Compute plan

[`MLComputePlan`](/documentation/CoreML/MLComputePlan-1w21n)

A class representing the compute plan of a model.

[`MLComputePlan`](/documentation/CoreML/MLComputePlan-85vdw)

A class describing the plan for executing a model.

[`MLModelStructure`](/documentation/CoreML/MLModelStructure-swift.enum)

An enum representing the structure of a model.

[`MLComputePlanCost`](/documentation/CoreML/MLComputePlanCost)

A class that represents the estimated cost of executing a layer or operation.

[`MLComputePlanDeviceUsage`](/documentation/CoreML/MLComputePlanDeviceUsage)

The anticipated compute devices to use for executing a layer or operation.

[`MLComputePolicy`](/documentation/CoreML/MLComputePolicy)

The compute policy determining what compute device, or compute devices, to execute ML workloads on.

[`withMLTensorComputePolicy(_:_:)`](/documentation/CoreML/withMLTensorComputePolicy(_:_:)-8stx9)

Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor
operations are executed on.

[`withMLTensorComputePolicy(_:_:)`](/documentation/CoreML/withMLTensorComputePolicy(_:_:)-6z33x)

Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor
operations are executed on.

### Model state

[`MLState`](/documentation/CoreML/MLState)

Handle to the state buffers.

[`MLStateConstraint`](/documentation/CoreML/MLStateConstraint)

Constraint of a state feature value.

### Model tensor

[`MLTensor`](/documentation/CoreML/MLTensor)

A multi-dimensional array of numerical or Boolean scalars tailored to ML use cases, containing methods to perform
transformations and mathematical operations efficiently using a ML compute device.

[`MLTensorScalar`](/documentation/CoreML/MLTensorScalar)

A type that represents the tensor scalar types supported by the framework. Don’t use this type directly.

[`MLTensorRangeExpression`](/documentation/CoreML/MLTensorRangeExpression)

A type that can be used to slice a dimension of a tensor. Don’t use this type directly.

[`func   pointwiseMin ( _ : _ :)`](/documentation/CoreML/pointwiseMin(_:_:))

Computes the element-wise minimum of two tensors.

[`func   pointwiseMax ( _ : _ :)`](/documentation/CoreML/pointwiseMax(_:_:))

Computes the element-wise minimum between two tensors.

[`func   withMLTensorComputePolicy ( _ : _ :)`](/documentation/CoreML/withMLTensorComputePolicy(_:_:))

Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor
operations are executed on.

### Model structure

[`MLModelStructure`](/documentation/CoreML/MLModelStructure-c.class)

A class representing the structure of a model.

[`MLModelStructure`](/documentation/CoreML/MLModelStructure-swift.enum)

An enum representing the structure of a model.

[`MLModelStructureNeuralNetwork`](/documentation/CoreML/MLModelStructureNeuralNetwork)

A class representing the structure of a NeuralNetwork model.

[`MLModelStructureNeuralNetworkLayer`](/documentation/CoreML/MLModelStructureNeuralNetworkLayer)

A class representing a layer in a NeuralNetwork.

[`MLModelStructurePipeline`](/documentation/CoreML/MLModelStructurePipeline)

A class representing the structure of a Pipeline model.

[`MLModelStructureProgram`](/documentation/CoreML/MLModelStructureProgram)

A class representing the structure of an ML Program model.

[`MLModelStructureProgramArgument`](/documentation/CoreML/MLModelStructureProgramArgument)

A class representing an argument in the Program.

[`MLModelStructureProgramBinding`](/documentation/CoreML/MLModelStructureProgramBinding)

A class representing a binding in the Program

[`MLModelStructureProgramBlock`](/documentation/CoreML/MLModelStructureProgramBlock)

A class representing a block in the Program.

[`MLModelStructureProgramFunction`](/documentation/CoreML/MLModelStructureProgramFunction)

A class representing a function in the Program.

[`MLModelStructureProgramNamedValueType`](/documentation/CoreML/MLModelStructureProgramNamedValueType)

A class representing a named value type in a Program.

[`MLModelStructureProgramOperation`](/documentation/CoreML/MLModelStructureProgramOperation)

A class representing an Operation in a Program.

[`MLModelStructureProgramValue`](/documentation/CoreML/MLModelStructureProgramValue)

A class representing a constant value in the Program.

[`MLModelStructureProgramValueType`](/documentation/CoreML/MLModelStructureProgramValueType)

A class representing the type of a value or a variable in the Program.

### Model errors

[`MLModelError`](/documentation/CoreML/MLModelError-swift.struct)

Information about a Core ML model error.

[`Code`](/documentation/CoreML/MLModelError-swift.struct/Code)

Information about a Core ML model error.

[`MLModelErrorDomain`](/documentation/CoreML/MLModelErrorDomain)

The domain for Core ML errors.

### Model deployments

[`MLModelCollection`](/documentation/CoreML/MLModelCollection)

A set of Core ML models from a model deployment.

### Optimization

[`MLOptimizationHints`](/documentation/CoreML/MLOptimizationHints-c.class)

MLOptimizationHints

### Reference

[CoreML Enumerations](/documentation/CoreML/coreml-enumerations)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
