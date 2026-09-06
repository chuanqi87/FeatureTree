# android.nfc

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# android.nfc

---

[Kotlin](https://developer.android.com/reference/kotlin/android/nfc/package-summary "View this page in Kotlin")
|Java

## Interfaces

|  |  |
| --- | --- |
| [NfcAdapter.CreateBeamUrisCallback](https://developer.android.com/reference/android/nfc/NfcAdapter.CreateBeamUrisCallback) | *This interface was deprecated in API level 29. this feature is removed. File sharing can work using other technology like Bluetooth.* |
| [NfcAdapter.CreateNdefMessageCallback](https://developer.android.com/reference/android/nfc/NfcAdapter.CreateNdefMessageCallback) | *This interface was deprecated in API level 29. this feature is removed. File sharing can work using other technology like Bluetooth.* |
| [NfcAdapter.OnNdefPushCompleteCallback](https://developer.android.com/reference/android/nfc/NfcAdapter.OnNdefPushCompleteCallback) | *This interface was deprecated in API level 29. this feature is removed. File sharing can work using other technology like Bluetooth.* |
| [NfcAdapter.OnTagRemovedListener](https://developer.android.com/reference/android/nfc/NfcAdapter.OnTagRemovedListener) | A callback that is invoked when a tag is removed from the field. |
| [NfcAdapter.ReaderCallback](https://developer.android.com/reference/android/nfc/NfcAdapter.ReaderCallback) | A callback to be invoked when the system finds a tag while the foreground activity is operating in reader mode. |

## Classes

|  |  |
| --- | --- |
| [AvailableNfcAntenna](https://developer.android.com/reference/android/nfc/AvailableNfcAntenna) | Represents a single available Nfc antenna on an Android device. |
| [NdefMessage](https://developer.android.com/reference/android/nfc/NdefMessage) | Represents an immutable NDEF Message. |
| [NdefRecord](https://developer.android.com/reference/android/nfc/NdefRecord) | Represents an immutable NDEF Record. |
| [NfcAdapter](https://developer.android.com/reference/android/nfc/NfcAdapter) | Represents the local NFC adapter. |
| [NfcAntennaInfo](https://developer.android.com/reference/android/nfc/NfcAntennaInfo) | Contains information on all available Nfc antennas on an Android device as well as information on the device itself in relation positioning of the antennas. |
| [NfcEvent](https://developer.android.com/reference/android/nfc/NfcEvent) | Wraps information associated with any NFC event. |
| [NfcManager](https://developer.android.com/reference/android/nfc/NfcManager) | High level manager used to obtain an instance of an `NfcAdapter`. |
| [Tag](https://developer.android.com/reference/android/nfc/Tag) | Represents an NFC tag that has been discovered. |

## Exceptions

|  |  |
| --- | --- |
| [FormatException](https://developer.android.com/reference/android/nfc/FormatException) |  |
| [TagLostException](https://developer.android.com/reference/android/nfc/TagLostException) |  |

* ## Interfaces

  + [NfcAdapter.CreateBeamUrisCallback](https://developer.android.com/reference/android/nfc/NfcAdapter.CreateBeamUrisCallback)
  + [NfcAdapter.CreateNdefMessageCallback](https://developer.android.com/reference/android/nfc/NfcAdapter.CreateNdefMessageCallback)
  + [NfcAdapter.OnNdefPushCompleteCallback](https://developer.android.com/reference/android/nfc/NfcAdapter.OnNdefPushCompleteCallback)
  + [NfcAdapter.OnTagRemovedListener](https://developer.android.com/reference/android/nfc/NfcAdapter.OnTagRemovedListener)
  + [NfcAdapter.ReaderCallback](https://developer.android.com/reference/android/nfc/NfcAdapter.ReaderCallback)
* ## Classes

  + [AvailableNfcAntenna](https://developer.android.com/reference/android/nfc/AvailableNfcAntenna)
  + [NdefMessage](https://developer.android.com/reference/android/nfc/NdefMessage)
  + [NdefRecord](https://developer.android.com/reference/android/nfc/NdefRecord)
  + [NfcAdapter](https://developer.android.com/reference/android/nfc/NfcAdapter)
  + [NfcAntennaInfo](https://developer.android.com/reference/android/nfc/NfcAntennaInfo)
  + [NfcEvent](https://developer.android.com/reference/android/nfc/NfcEvent)
  + [NfcManager](https://developer.android.com/reference/android/nfc/NfcManager)
  + [Tag](https://developer.android.com/reference/android/nfc/Tag)
* ## Exceptions

  + [FormatException](https://developer.android.com/reference/android/nfc/FormatException)
  + [TagLostException](https://developer.android.com/reference/android/nfc/TagLostException)
