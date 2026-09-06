# Configuration options for hybrid experiences in Android apps

**Experimental:** Using the Firebase AI Logic SDK to build hybrid experiences is
an Experimental feature (and the Prompt API from ML Kit is in beta),
which means that this feature isn't subject to any SLA or deprecation policy and
could change in backwards-incompatible ways.

This page describes the following configuration options for hybrid experiences:

* [Set an inference mode.](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#inference-modes)
* [Determine whether on-device or in-cloud inference was used.](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#determine-inference-mode)
* [Specify a model to use.](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#specify-model)
* [Use model configuration to control responses (like temperature).](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#model-config)

**Make sure that you've completed the
[getting started guide for building hybrid experiences](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#get-started).**

## Set an inference mode

The examples in the getting started guide use the `PREFER_ON_DEVICE` mode, but
this is only one of the four available
[inference modes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/InferenceMode).

**Note**: Keep the following in mind:

* To use an on-device model, make sure to review the list of
  [not-yet-available
  features for on-device inference](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started#features-not-yet-available)
  on the get started page.
* To use a cloud-hosted model, the device must be online and
  you must explicitly
  [specify
  a cloud-hosted model to use](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#specify-model).
* As part of the response, the SDK tells you
  [whether
  on-device or in-cloud inference was used](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#determine-inference-mode).

Here are the available inference modes:

* **`PREFER_ON_DEVICE`**: Attempt to use the on-device model if it's available
  and supports the type of request. Otherwise, log an error on the device and
  then automatically *fall back to the cloud-hosted model*.

  ### Kotlin

  ```
  val config = OnDeviceConfig(mode = InferenceMode.PREFER_ON_DEVICE)
  ```

  ### Java

  ```
  InferenceMode mode = InferenceMode.PREFER_ON_DEVICE;
  OnDeviceConfig config = new OnDeviceConfig(mode);
  ```
* **`ONLY_ON_DEVICE`**: Attempt to use the on-device model if it's available
  and supports the type of request. Otherwise, *throw an exception*.

  ### Kotlin

  ```
  val config = OnDeviceConfig(mode = InferenceMode.ONLY_ON_DEVICE)
  ```

  ### Java

  ```
  InferenceMode mode = InferenceMode.ONLY_ON_DEVICE;
  OnDeviceConfig config = new OnDeviceConfig(mode);
  ```
* **`PREFER_IN_CLOUD`**: Attempt to use the cloud-hosted model if the device is
  online and if the model is available. If the device is offline,
  *fall back to the on-device model*. In all other failure cases,
  *throw an exception*.

  ### Kotlin

  ```
  val config = OnDeviceConfig(mode = InferenceMode.PREFER_IN_CLOUD)
  ```

  ### Java

  ```
  InferenceMode mode = InferenceMode.PREFER_IN_CLOUD;
  OnDeviceConfig config = new OnDeviceConfig(mode);
  ```
* **`ONLY_IN_CLOUD`**: Attempt to use the cloud-hosted model if the device is
  online and if the model is available. Otherwise, *throw an exception*.

  ### Kotlin

  ```
  val config = OnDeviceConfig(mode = InferenceMode.ONLY_IN_CLOUD)
  ```

  ### Java

  ```
  InferenceMode mode = InferenceMode.ONLY_IN_CLOUD;
  OnDeviceConfig config = new OnDeviceConfig(mode);
  ```

## Determine whether on-device or in-cloud inference was used

If your inference mode is `PREFER_ON_DEVICE` or `PREFER_IN_CLOUD`, then it might
be helpful to know which mode was used for given requests. This information is
provided by the `inferenceSource` property of each response.

When you access this property, the returned value will be either `ON_DEVICE` or
`IN_CLOUD`.

### Kotlin

```
// ...

print("You used: ${result.response.inferenceSource}")

print(result.response.text)
```

### Java

```
// ...

System.out.println("You used: " + result.getResponse().getInferenceSource());

System.out.println(result.getResponse().getText());
```

## Specify a model to use

|  |
| --- |
| *Click your Gemini API provider to view provider-specific content and code on this page.* |

You can specify a model to use when you create the `generativeModel` instance
([Kotlin](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel) |
[Java](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel)).

* **Specify a cloud-hosted model**:

  + If your inference mode is `PREFER_ON_DEVICE`, `PREFER_IN_CLOUD`, or
    `ONLY_IN_CLOUD`, then you ***must*** explicitly specify a cloud-hosted model
    to use. The SDK does *not* have a default cloud-hosted model.
  + Find model names for all
    [supported cloud-hosted Gemini models](https://firebase.google.com/docs/ai-logic/models).
* **Specify an on-device model**:

  + If your inference mode is `PREFER_ON_DEVICE`, `PREFER_IN_CLOUD`, or
    `ONLY_ON_DEVICE`, then you can ***optionally*** specify in the
    `onDeviceConfig` a "category" of on-device model to use. Categories are a
    combination of release stage and performance characteristics.
  + Supported category values are listed below.  
    AICore auto-selects the on-device model that meets the conditions of the
    specified category and is supported by the device. For example, if you
    specify `PREVIEW` and the device is a Pixel 9, then
    *Gemini Nano 4 Full [Preview]* (`nano-v4-full`) would likely be
    auto-selected.

    - **`STABLE`**: The latest *stable* on-device model.

      * Fully tested and on consumer devices.
      * For example, *Gemini Nano 3* (`nano-v3`) or
        *Gemini Nano 2* (`nano-v2`).
      * Default setting for the on-device model if no `OnDeviceModelOption`
        is specified.
    - **`PREVIEW`**: The latest *preview* on-device model with *full*
      performance capabilities.

      * Designed for higher reasoning power and complex tasks.
      * For example, *Gemini Nano 4 Full [Preview]* (`nano-v4-full`, which
        is based on Gemma 4 E4B).
    - **`PREVIEW_FAST`**: The latest *preview* on-device model that's *fast*.

      * Optimized for maximum speed and lower latency.
      * For example, *Gemini Nano 4 Fast [Preview]* (`nano-v4-fast`, which
        is based on Gemma 4 E2B).**Important:** To use a *preview* on-device model, review the prerequisites
    and enrollment instructions for the developer preview in the
    [AICore Developer Preview guide](https://developers.google.com/ml-kit/genai/aicore-dev-preview).

### Kotlin

```
val model = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel(
        // Specify a cloud-hosted model.
        // Required for `PREFER_ON_DEVICE`, `PREFER_IN_CLOUD`, and `ONLY_IN_CLOUD` inference modes.
        modelName = "CLOUD_HOSTED_MODEL_NAME",
        onDeviceConfig = OnDeviceConfig(
            mode = InferenceMode.INFERENCE_MODE,
            // (Optional) Specify an on-device model category.
            // AICore will auto-select an on-device model based on this category.
            // If not specified, AICore will auto-select the default stable on-device model.
            modelOption = OnDeviceModelOption.ON-DEVICE_MODEL_CATEGORY)
    )
```

### Java

```
GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
    .generativeModel(
        // Specify a cloud-hosted model.
        // Required for `PREFER_ON_DEVICE`, `PREFER_IN_CLOUD`, and `ONLY_IN_CLOUD` inference modes.
        "CLOUD_HOSTED_MODEL_NAME",
        /* config = */ null,
        /* safetySettings = */ null,
        /* tools = */ null,
        /* toolConfig = */ null,
        /* systemInstruction = */ null,
        /* requestOptions = */ new RequestOptions(),
        new OnDeviceConfig(
                /* mode = */ InferenceMode.INFERENCE_MODE,
                /* maxOutputTokens = */ null,
                /* temperature = */ null,
                /* topK = */ null,
                /* seed = */ null,
                /* candidateCount = */ 1,
                // (Optional) Specify an on-device model category.
                // AICore will auto-select an on-device model based on this category.
                // If not specified, AICore will auto-select the default stable on-device model.
                /* modelOption = */ OnDeviceModelOption.ON-DEVICE_MODEL_CATEGORY)
    );

GenerativeModelFutures model = GenerativeModelFutures.from(ai);
```

## Use model configuration to control responses

|  |
| --- |
| *Click your Gemini API provider to view provider-specific content and code on this page.* |

In each request to a model, you can send along a model configuration to control
how the model generates a response. Cloud-hosted models and on-device models
offer different configuration options
([cloud](https://firebase.google.com/docs/ai-logic/model-parameters#parameters-descriptions-gemini)
vs
[on-device](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig)
parameters).

For cloud-hosted models, set their configuration directly in the model's
configuration. However, for the on-device models, set their configuration within
an
[`onDeviceConfig`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig).

The configuration is maintained for the lifetime of the instance. If you want to
use a different config, create a new `GenerativeModel` instance with that
config.

Here's an example that sets the configurations for the cloud-hosted and
on-device models that could be used if `PREFER_ON_DEVICE` inference mode is
set:

### Kotlin

```
val model = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel("MODEL_NAME",
        // Config for cloud-hosted model
        generationConfig = generationConfig {
          temperature = 0.8f,
          topK = 10
        },
        // Config for on-device model
        onDeviceConfig = onDeviceConfig {
          mode = InferenceMode.PREFER_ON_DEVICE,
          temperature = 0.8f,
          topK = 5
        })
```

### Java

```
// Config for cloud-hosted model
GenerationConfig generationConfig = new GenerationConfig.Builder()
    .setTemperature(0.8f)
    .setTopK(10)
    .build();

// Config for on-device model
OnDeviceConfig onDeviceConfig = new OnDeviceConfig.Builder()
    .setMode(InferenceMode.PREFER_ON_DEVICE)
    .setTemperature(0.8f)
    .setTopK(5)
    .build();

GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI())
    .generativeModel(
        "MODEL_NAME",
        generationConfig,
        onDeviceConfig
    );

GenerativeModelFutures model = GenerativeModelFutures.from(ai);
```
