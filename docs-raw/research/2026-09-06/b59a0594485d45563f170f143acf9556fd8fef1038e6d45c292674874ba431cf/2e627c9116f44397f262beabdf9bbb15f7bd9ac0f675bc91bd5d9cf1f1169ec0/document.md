# android.inputmethodservice

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# android.inputmethodservice

---

[Kotlin](https://developer.android.com/reference/kotlin/android/inputmethodservice/package-summary "View this page in Kotlin")
|Java

Base classes for writing input methods (such as software keyboards). These APIs are not for use by
normal applications, they are a framework specifically for writing input
method components. Implementations will typically derive from
`InputMethodService`.

## Interfaces

|  |  |
| --- | --- |
| [KeyboardView.OnKeyboardActionListener](https://developer.android.com/reference/android/inputmethodservice/KeyboardView.OnKeyboardActionListener) | Listener for virtual keyboard events. |

## Classes

|  |  |
| --- | --- |
| [AbstractInputMethodService](https://developer.android.com/reference/android/inputmethodservice/AbstractInputMethodService) | AbstractInputMethodService provides a abstract base class for input methods. |
| [AbstractInputMethodService.AbstractInputMethodImpl](https://developer.android.com/reference/android/inputmethodservice/AbstractInputMethodService.AbstractInputMethodImpl) | Base class for derived classes to implement their `InputMethod` interface. |
| [AbstractInputMethodService.AbstractInputMethodSessionImpl](https://developer.android.com/reference/android/inputmethodservice/AbstractInputMethodService.AbstractInputMethodSessionImpl) | Base class for derived classes to implement their `InputMethodSession` interface. |
| [ExtractEditText](https://developer.android.com/reference/android/inputmethodservice/ExtractEditText) | \* Specialization of `EditText` for showing and interacting with the extracted text in a full-screen input method. |
| [InputMethodService](https://developer.android.com/reference/android/inputmethodservice/InputMethodService) | InputMethodService provides a standard implementation of an InputMethod, which final implementations can derive from and customize. |
| [InputMethodService.InputMethodImpl](https://developer.android.com/reference/android/inputmethodservice/InputMethodService.InputMethodImpl) | Concrete implementation of `AbstractInputMethodService.AbstractInputMethodImpl` that provides all of the standard behavior for an input method. |
| [InputMethodService.InputMethodSessionImpl](https://developer.android.com/reference/android/inputmethodservice/InputMethodService.InputMethodSessionImpl) | Concrete implementation of `AbstractInputMethodService.AbstractInputMethodSessionImpl` that provides all of the standard behavior for an input method session. |
| [InputMethodService.Insets](https://developer.android.com/reference/android/inputmethodservice/InputMethodService.Insets) | Information about where interesting parts of the input method UI appear. |
| [Keyboard](https://developer.android.com/reference/android/inputmethodservice/Keyboard) | *This class was deprecated in API level 29. This class is deprecated because this is just a convenient UI widget class that application developers can re-implement on top of existing public APIs. If you have already depended on this class, consider copying the implementation from AOSP into your project or re-implementing a similar widget by yourselves* |
| [Keyboard.Key](https://developer.android.com/reference/android/inputmethodservice/Keyboard.Key) | Class for describing the position and characteristics of a single key in the keyboard. |
| [Keyboard.Row](https://developer.android.com/reference/android/inputmethodservice/Keyboard.Row) | Container for keys in the keyboard. |
| [KeyboardView](https://developer.android.com/reference/android/inputmethodservice/KeyboardView) | *This class was deprecated in API level 29. This class is deprecated because this is just a convenient UI widget class that application developers can re-implement on top of existing public APIs. If you have already depended on this class, consider copying the implementation from AOSP into your project or re-implementing a similar widget by yourselves* |

* ## Interfaces

  + [KeyboardView.OnKeyboardActionListener](https://developer.android.com/reference/android/inputmethodservice/KeyboardView.OnKeyboardActionListener)
* ## Classes

  + [AbstractInputMethodService](https://developer.android.com/reference/android/inputmethodservice/AbstractInputMethodService)
  + [AbstractInputMethodService.AbstractInputMethodImpl](https://developer.android.com/reference/android/inputmethodservice/AbstractInputMethodService.AbstractInputMethodImpl)
  + [AbstractInputMethodService.AbstractInputMethodSessionImpl](https://developer.android.com/reference/android/inputmethodservice/AbstractInputMethodService.AbstractInputMethodSessionImpl)
  + [ExtractEditText](https://developer.android.com/reference/android/inputmethodservice/ExtractEditText)
  + [InputMethodService](https://developer.android.com/reference/android/inputmethodservice/InputMethodService)
  + [InputMethodService.InputMethodImpl](https://developer.android.com/reference/android/inputmethodservice/InputMethodService.InputMethodImpl)
  + [InputMethodService.InputMethodSessionImpl](https://developer.android.com/reference/android/inputmethodservice/InputMethodService.InputMethodSessionImpl)
  + [InputMethodService.Insets](https://developer.android.com/reference/android/inputmethodservice/InputMethodService.Insets)
  + [Keyboard](https://developer.android.com/reference/android/inputmethodservice/Keyboard)
  + [Keyboard.Key](https://developer.android.com/reference/android/inputmethodservice/Keyboard.Key)
  + [Keyboard.Row](https://developer.android.com/reference/android/inputmethodservice/Keyboard.Row)
  + [KeyboardView](https://developer.android.com/reference/android/inputmethodservice/KeyboardView)
