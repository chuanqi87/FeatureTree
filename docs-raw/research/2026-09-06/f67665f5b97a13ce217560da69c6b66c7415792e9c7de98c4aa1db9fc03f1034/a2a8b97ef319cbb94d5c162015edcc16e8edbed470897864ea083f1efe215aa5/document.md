# android.hardware.biometrics

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# android.hardware.biometrics

---

[Kotlin](https://developer.android.com/reference/kotlin/android/hardware/biometrics/package-summary "View this page in Kotlin")
|Java

## Interfaces

|  |  |
| --- | --- |
| [BiometricManager.Authenticators](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager.Authenticators) | Types of authenticators, defined at a level of granularity supported by `BiometricManager` and `BiometricPrompt`. |
| [EmbeddedBiometricPrompt.EmbeddedContentFactory](https://developer.android.com/reference/android/hardware/biometrics/EmbeddedBiometricPrompt.EmbeddedContentFactory) | A factory that produces the custom embedded content view for the biometric prompt. |
| [PromptContentItem](https://developer.android.com/reference/android/hardware/biometrics/PromptContentItem) | An item shown on `PromptContentView`. |
| [PromptContentView](https://developer.android.com/reference/android/hardware/biometrics/PromptContentView) | Contains the information of the template of content view for Biometric Prompt. |

## Classes

|  |  |
| --- | --- |
| [BiometricManager](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager) | A class that contains biometric utilities. |
| [BiometricManager.Strings](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager.Strings) | Provides localized strings for an application that uses `BiometricPrompt` to authenticate the user. |
| [BiometricPrompt](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt) | A class that manages a system-provided biometric dialog. |
| [BiometricPrompt.AuthenticationCallback](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt.AuthenticationCallback) | Callback structure provided to `BiometricPrompt.authenticate(CancellationSignal,Executor,AuthenticationCallback)` or `BiometricPrompt.authenticate(CryptoObject,CancellationSignal,Executor,AuthenticationCallback)`. |
| [BiometricPrompt.AuthenticationResult](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt.AuthenticationResult) | Container for callback data from `authenticate(CancellationSignal,Executor,AuthenticationCallback)` and `authenticate(CryptoObject,CancellationSignal,Executor,AuthenticationCallback)`. |
| [BiometricPrompt.Builder](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt.Builder) | A builder that collects arguments to be shown on the system-provided biometric dialog. |
| [BiometricPrompt.CryptoObject](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt.CryptoObject) | A wrapper class for the cryptographic operations supported by BiometricPrompt. |
| [BiometricPromptStyleSpec](https://developer.android.com/reference/android/hardware/biometrics/BiometricPromptStyleSpec) | A class that describes the visual styles of the embedded BiometricPrompt UI to allow client applications to maintain visual consistency. |
| [EmbeddedBiometricPrompt](https://developer.android.com/reference/android/hardware/biometrics/EmbeddedBiometricPrompt) | The embedded version of `BiometricPrompt` that allows client apps to pass in content to display above the biometric prompt as a connected sheet. |
| [EmbeddedBiometricPrompt.AuthenticationCallback](https://developer.android.com/reference/android/hardware/biometrics/EmbeddedBiometricPrompt.AuthenticationCallback) | Callback structure provided to `EmbeddedBiometricPrompt.startAuthenticationSession(CancellationSignal,int,Executor,AuthenticationCallback)`. |
| [EmbeddedBiometricPrompt.Builder](https://developer.android.com/reference/android/hardware/biometrics/EmbeddedBiometricPrompt.Builder) | A builder for the embedded version of BiometricPrompt that collects arguments to be shown on the system-provided biometric dialog. |
| [FallbackOption](https://developer.android.com/reference/android/hardware/biometrics/FallbackOption) | Contains the information for a fallback option to be displayed within Biometric Prompt. |
| [PromptContentItemBulletedText](https://developer.android.com/reference/android/hardware/biometrics/PromptContentItemBulletedText) | A list item with bulleted text shown on `PromptVerticalListContentView`. |
| [PromptContentItemPlainText](https://developer.android.com/reference/android/hardware/biometrics/PromptContentItemPlainText) | A list item with plain text shown on `PromptVerticalListContentView`. |
| [PromptContentViewWithMoreOptionsButton](https://developer.android.com/reference/android/hardware/biometrics/PromptContentViewWithMoreOptionsButton) | Contains the information of the template of content view with a more options button for Biometric Prompt. |
| [PromptContentViewWithMoreOptionsButton.Builder](https://developer.android.com/reference/android/hardware/biometrics/PromptContentViewWithMoreOptionsButton.Builder) | A builder that collects arguments to be shown on the content view with more options button. |
| [PromptVerticalListContentView](https://developer.android.com/reference/android/hardware/biometrics/PromptVerticalListContentView) | Contains the information of the template of vertical list content view for Biometric Prompt. |
| [PromptVerticalListContentView.Builder](https://developer.android.com/reference/android/hardware/biometrics/PromptVerticalListContentView.Builder) | A builder that collects arguments to be shown on the vertical list view. |

* ## Interfaces

  + [BiometricManager.Authenticators](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager.Authenticators)
  + [EmbeddedBiometricPrompt.EmbeddedContentFactory](https://developer.android.com/reference/android/hardware/biometrics/EmbeddedBiometricPrompt.EmbeddedContentFactory)
  + [PromptContentItem](https://developer.android.com/reference/android/hardware/biometrics/PromptContentItem)
  + [PromptContentView](https://developer.android.com/reference/android/hardware/biometrics/PromptContentView)
* ## Classes

  + [BiometricManager](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager)
  + [BiometricManager.Strings](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager.Strings)
  + [BiometricPrompt](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt)
  + [BiometricPrompt.AuthenticationCallback](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt.AuthenticationCallback)
  + [BiometricPrompt.AuthenticationResult](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt.AuthenticationResult)
  + [BiometricPrompt.Builder](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt.Builder)
  + [BiometricPrompt.CryptoObject](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt.CryptoObject)
  + [BiometricPromptStyleSpec](https://developer.android.com/reference/android/hardware/biometrics/BiometricPromptStyleSpec)
  + [EmbeddedBiometricPrompt](https://developer.android.com/reference/android/hardware/biometrics/EmbeddedBiometricPrompt)
  + [EmbeddedBiometricPrompt.AuthenticationCallback](https://developer.android.com/reference/android/hardware/biometrics/EmbeddedBiometricPrompt.AuthenticationCallback)
  + [EmbeddedBiometricPrompt.Builder](https://developer.android.com/reference/android/hardware/biometrics/EmbeddedBiometricPrompt.Builder)
  + [FallbackOption](https://developer.android.com/reference/android/hardware/biometrics/FallbackOption)
  + [PromptContentItemBulletedText](https://developer.android.com/reference/android/hardware/biometrics/PromptContentItemBulletedText)
  + [PromptContentItemPlainText](https://developer.android.com/reference/android/hardware/biometrics/PromptContentItemPlainText)
  + [PromptContentViewWithMoreOptionsButton](https://developer.android.com/reference/android/hardware/biometrics/PromptContentViewWithMoreOptionsButton)
  + [PromptContentViewWithMoreOptionsButton.Builder](https://developer.android.com/reference/android/hardware/biometrics/PromptContentViewWithMoreOptionsButton.Builder)
  + [PromptVerticalListContentView](https://developer.android.com/reference/android/hardware/biometrics/PromptVerticalListContentView)
  + [PromptVerticalListContentView.Builder](https://developer.android.com/reference/android/hardware/biometrics/PromptVerticalListContentView.Builder)
