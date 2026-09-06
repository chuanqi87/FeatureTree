# Configuration options for hybrid experiences in Apple apps

**Experimental:** Using the Firebase AI Logic SDK to build hybrid experiences
is an Experimental feature, which means that this feature isn't subject to
any SLA or deprecation policy and could change in backwards-incompatible ways.

This page describes the following configuration options for hybrid and
on-device experiences:

* [Set an "inference mode".](https://firebase.google.com/docs/ai-logic/hybrid/ios/configuration-options#inference-modes)
* [Check if the on-device model is available.](https://firebase.google.com/docs/ai-logic/hybrid/ios/configuration-options#check-model-availability)
* [Determine whether on-device or in-cloud inference was used.](https://firebase.google.com/docs/ai-logic/hybrid/ios/configuration-options#determine-inference-source)
* [Use model configuration to control responses (like temperature).](https://firebase.google.com/docs/ai-logic/hybrid/ios/configuration-options#model-config)

**Note:** Function calling and generating structured output are supported for
on-device inference. Documentation for implementing those experiences is
coming soon!

**Make sure that you've completed the
[getting started guide for building hybrid experiences](https://firebase.google.com/docs/ai-logic/hybrid/ios/get-started#get-started).**

## Set an "inference mode"

The examples in the getting started guide show how to implement attempting
on-device inference first, and then falling back to the cloud-hosted model.
This is only one of the available "inference modes" that you can implement.

**Note**: Keep the following in mind:

* To use an on-device model, make sure to review the list of
  [not-yet-supported
  features](https://firebase.google.com/docs/ai-logic/hybrid/ios/get-started#features-not-yet-supported) at the bottom of the get started page.
* To use a cloud-hosted model, the device must be online and you must set
  either the `primary` or `secondary` model to a cloud model.
* As part of the response, the SDK tells you
  [whether on-device or in-cloud
  inference was used](https://firebase.google.com/docs/ai-logic/hybrid/ios/configuration-options#determine-inference-source).


#### Hybrid inference

* **Prefer on-device inference**: set `primary` to a "system" model and
  `secondary` to a cloud model.

  Attempt to use the on-device model if it's available and supports the type
  of request. Otherwise, log an error on the device and then automatically
  *fall back to the cloud-hosted model*.

  ```
  // Imports + initialization of Gemini API backend service
  // ...

  // Initialize a cloud model that supports your use case
  let cloudModel = ai.geminiModel(name: "GEMINI_MODEL_NAME")
  // Initialize an on-device model that supports your use case
  let systemModel = FirebaseAI.SystemLanguageModel.default

  // Create a GenerativeModelSession with a hybrid model.
  // Provide your preferred model as `primary` and your fallback model as `secondary`
  // Attempt to use the on-device model; otherwise, fall back to the cloud-hosted model.
  let session = ai.generativeModelSession(
    model: .hybridModel(primary: systemModel, secondary: cloudModel)
  )
  ```
* **Prefer in-cloud inference**: set `primary` to a cloud model and
  `secondary` to a "system" model.

  Attempt to use the cloud-hosted model if the device is online and if the
  model is available. If the device is offline, *fall back to the on-device
  model*. In all other failure cases, *throw an exception*.

  ```
  // Imports + initialization of Gemini API backend service
  // ...

  // Initialize a cloud model that supports your use case
  let cloudModel = ai.geminiModel(name: "GEMINI_MODEL_NAME")
  // Initialize an on-device model that supports your use case
  let systemModel = FirebaseAI.SystemLanguageModel.default

  // Create a GenerativeModelSession with a hybrid model.
  // Provide your preferred model as `primary` and your fallback model as `secondary`
  // Attempt to use the cloud-hosted model; otherwise, fall back to the on-device model.
  let session = ai.generativeModelSession(
    model: .hybridModel(primary: cloudModel, secondary: systemModel)
  )
  ```

#### Only on-device or only in-cloud inference

The SDK supports setting *only* a single `model` which means the SDK will *only*
attempt either on-device or in-cloud inference. Also, you don't create a
`HybridModel` for this use case. However, for a *hybrid* experience, you do need
to create a `HybridModel` and set both `primary` and `secondary` models
(as described above).

* **Only on-device inference**: set `model` to a "system" model. You don't
  create a `HybridModel` for this use case.

  Attempt to use the on-device model if it's available and supports the type
  of request. Otherwise, *throw an exception*.

  ```
  // Imports + initialization of Gemini API backend service
  // ...

  // Initialize an on-device model that supports your use case
  let systemModel = FirebaseAI.SystemLanguageModel.default

  // Create a GenerativeModelSession with the on-device model.
  let session = ai.generativeModelSession(
    model: systemModel
  )
  ```
* **Only in-cloud inference**: set `model` to a cloud model. You don't create
  a `HybridModel` for this use case.

  Attempt to use the cloud-hosted model if the device is online and if the
  model is available. Otherwise, *throw an exception*.

  ```
  // Imports + initialization of Gemini API backend service
  // ...

  // Initialize a cloud model that supports your use case
  let cloudModel = ai.geminiModel(name: "GEMINI_MODEL_NAME")

  // Create a GenerativeModelSession with a cloud model.
  let session = ai.generativeModelSession(
    model: cloudModel
  )
  ```

## Check if the on-device model is available

Manual checks for on-device availability are only necessary if you want to
surface that information to the user or request that end-users take action to
download the on-device model. If the on-device model is unavailable – and
you've set `primary` to an on-device model and `secondary` to a cloud model –
then the SDK will automatically fallback to using the cloud-hosted model.

**Note:** An app can't trigger an on-device model download or enable Apple
Intelligence on the device. However, if desired, you can check for on-device
model availability (as described in this section) and request that the end-user
[enable Apple Intelligence](https://support.apple.com/121115)
(and thus trigger the on-device model download).

To manually check whether the on-device model is actually usable, inspect the
`isAvailable` property:

```
if FirebaseAI.SystemLanguageModel.default.isAvailable {
  // The on-device model is ready to use.
} else {
  // The on-device model is unavailable.
}
```

To check for specific on-device model availability reasons, inspect the
`availability` property:

```
switch FirebaseAI.SystemLanguageModel.default.availability {
case .available:
  // The on-device model is ready to use.
  break
case .unavailable(.deviceNotEligible):
  // This device does not support Apple Intelligence.
  break
case .unavailable(.appleIntelligenceNotEnabled):
  // The user has not enabled Apple Intelligence in Settings.
  break
case .unavailable(.modelNotReady):
  // The model is still being downloaded.
  break
case let .unavailable(reason):
  // The model is unavailable due to the specified `reason`.
  break
}
```



## Determine whether on-device or in-cloud inference was used

If you use a `HybridModel` (and set both `primary` and `secondary` models),
then it might be helpful to know which model was used for a given request.
This information is provided by the `modelVersion` property of `rawResponse` in
each response.

When you access this property, the returned value will be one of the following:

* Cloud-hosted model used: the model name, for example `gemini-3.1-flash-lite`
* On-device model used: `apple-foundation-models-system-language-model`

```
// let response = try await session.respond(to: ...

print("You used: \(response.rawResponse.modelVersion)")

print(response.content)
```



## Use model configuration to control responses

In each request to a model, you can send along a model configuration to control
how the model generates a response. Cloud-hosted models and on-device models
offer different configuration options
([cloud](https://firebase.google.com/docs/ai-logic/model-parameters#parameters-descriptions-gemini)
vs
[on-device](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI/GenerationOptions)
parameters).

* Cloud-hosted models: set their configuration in a
  [`GenerationConfig`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerationConfig).
* On-device models: set their configuration within
  [`FirebaseAI.GenerationOptions`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI/GenerationOptions).

These options are configured for each request to the model.

Here's an example that sets the configurations for the cloud-hosted and
on-device models for hybrid inference:

```
// ...

let response = try await session.respond(
  to: "Why is the sky blue?",
  options: .hybrid(
    // Config for cloud-hosted model
    gemini: GenerationConfig(
      temperature: 0.8,
      topP: 0.9,
      thinkingConfig: ThinkingConfig(thinkingLevel: .high)
    ),
    // Config for on-device model
    foundationModels: FirebaseAI.GenerationOptions(
      sampling: .random(probabilityThreshold: 0.9),
      temperature: 0.8
    )
  )
)

// ...
```

[Give feedback
about your experience with Firebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)
