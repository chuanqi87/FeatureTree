# android.accounts

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# android.accounts

---

[Kotlin](https://developer.android.com/reference/kotlin/android/accounts/package-summary "View this page in Kotlin")
|Java

## Interfaces

|  |  |
| --- | --- |
| [AccountManagerCallback](https://developer.android.com/reference/android/accounts/AccountManagerCallback)<V> |  |
| [AccountManagerFuture](https://developer.android.com/reference/android/accounts/AccountManagerFuture)<V> | A AccountManagerFuture represents the result of an asynchronous `AccountManager` call. |
| [OnAccountsUpdateListener](https://developer.android.com/reference/android/accounts/OnAccountsUpdateListener) | An interface that contains the callback used by the AccountManager |

## Classes

|  |  |
| --- | --- |
| [AbstractAccountAuthenticator](https://developer.android.com/reference/android/accounts/AbstractAccountAuthenticator) | Abstract base class for creating AccountAuthenticators. |
| [Account](https://developer.android.com/reference/android/accounts/Account) | Value type that represents an Account in the `AccountManager`. |
| [AccountAuthenticatorActivity](https://developer.android.com/reference/android/accounts/AccountAuthenticatorActivity) | *This class was deprecated in API level 30. Applications should extend Activity themselves. This class is not compatible with AppCompat, and the functionality it provides is not complex.* |
| [AccountAuthenticatorResponse](https://developer.android.com/reference/android/accounts/AccountAuthenticatorResponse) | Object used to communicate responses back to the AccountManager |
| [AccountManager](https://developer.android.com/reference/android/accounts/AccountManager) | This class provides access to a centralized registry of the user's online accounts. |
| [AuthenticatorDescription](https://developer.android.com/reference/android/accounts/AuthenticatorDescription) | A `Parcelable` value type that contains information about an account authenticator. |

## Exceptions

|  |  |
| --- | --- |
| [AccountsException](https://developer.android.com/reference/android/accounts/AccountsException) |  |
| [AuthenticatorException](https://developer.android.com/reference/android/accounts/AuthenticatorException) |  |
| [NetworkErrorException](https://developer.android.com/reference/android/accounts/NetworkErrorException) |  |
| [OperationCanceledException](https://developer.android.com/reference/android/accounts/OperationCanceledException) |  |

* ## Interfaces

  + [AccountManagerCallback](https://developer.android.com/reference/android/accounts/AccountManagerCallback)
  + [AccountManagerFuture](https://developer.android.com/reference/android/accounts/AccountManagerFuture)
  + [OnAccountsUpdateListener](https://developer.android.com/reference/android/accounts/OnAccountsUpdateListener)
* ## Classes

  + [AbstractAccountAuthenticator](https://developer.android.com/reference/android/accounts/AbstractAccountAuthenticator)
  + [Account](https://developer.android.com/reference/android/accounts/Account)
  + [AccountAuthenticatorActivity](https://developer.android.com/reference/android/accounts/AccountAuthenticatorActivity)
  + [AccountAuthenticatorResponse](https://developer.android.com/reference/android/accounts/AccountAuthenticatorResponse)
  + [AccountManager](https://developer.android.com/reference/android/accounts/AccountManager)
  + [AuthenticatorDescription](https://developer.android.com/reference/android/accounts/AuthenticatorDescription)
* ## Exceptions

  + [AccountsException](https://developer.android.com/reference/android/accounts/AccountsException)
  + [AuthenticatorException](https://developer.android.com/reference/android/accounts/AuthenticatorException)
  + [NetworkErrorException](https://developer.android.com/reference/android/accounts/NetworkErrorException)
  + [OperationCanceledException](https://developer.android.com/reference/android/accounts/OperationCanceledException)
