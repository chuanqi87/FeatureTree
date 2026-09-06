# android.bluetooth

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# android.bluetooth

---

[Kotlin](https://developer.android.com/reference/kotlin/android/bluetooth/package-summary "View this page in Kotlin")
|Java

## Interfaces

|  |  |
| --- | --- |
| [BluetoothAdapter.LeScanCallback](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter.LeScanCallback) | Callback interface used to deliver LE scan results. |
| [BluetoothProfile](https://developer.android.com/reference/android/bluetooth/BluetoothProfile) | Public APIs for the Bluetooth Profiles. |
| [BluetoothProfile.ServiceListener](https://developer.android.com/reference/android/bluetooth/BluetoothProfile.ServiceListener) | An interface for notifying BluetoothProfile IPC clients when they have been connected or disconnected to the service. |

## Classes

|  |  |
| --- | --- |
| [BluetoothA2dp](https://developer.android.com/reference/android/bluetooth/BluetoothA2dp) | This class provides the public APIs to control the Bluetooth A2DP profile. |
| [BluetoothAdapter](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter) | Represents the local device Bluetooth adapter. |
| [BluetoothAssignedNumbers](https://developer.android.com/reference/android/bluetooth/BluetoothAssignedNumbers) | Bluetooth Assigned Numbers. |
| [BluetoothClass](https://developer.android.com/reference/android/bluetooth/BluetoothClass) | Represents a Bluetooth class, which describes general characteristics and capabilities of a device. |
| [BluetoothClass.Device](https://developer.android.com/reference/android/bluetooth/BluetoothClass.Device) | Defines standard device class constants based on the Bluetooth specification. |
| [BluetoothClass.Device.Major](https://developer.android.com/reference/android/bluetooth/BluetoothClass.Device.Major) | Defines standard major device class constants based on the Bluetooth specification. |
| [BluetoothClass.Service](https://developer.android.com/reference/android/bluetooth/BluetoothClass.Service) | Defines standard service class constants based on the Bluetooth specification. |
| [BluetoothCodecConfig](https://developer.android.com/reference/android/bluetooth/BluetoothCodecConfig) | Represents the codec configuration for a Bluetooth A2DP source device. |
| [BluetoothCodecConfig.Builder](https://developer.android.com/reference/android/bluetooth/BluetoothCodecConfig.Builder) | Builder for `BluetoothCodecConfig`. |
| [BluetoothCodecStatus](https://developer.android.com/reference/android/bluetooth/BluetoothCodecStatus) | Represents the codec status (configuration and capability) for a Bluetooth A2DP source device. |
| [BluetoothCodecStatus.Builder](https://developer.android.com/reference/android/bluetooth/BluetoothCodecStatus.Builder) | Builder for `BluetoothCodecStatus`. |
| [BluetoothCodecType](https://developer.android.com/reference/android/bluetooth/BluetoothCodecType) | Represents a supported source codec type for a Bluetooth A2DP device. |
| [BluetoothCsipSetCoordinator](https://developer.android.com/reference/android/bluetooth/BluetoothCsipSetCoordinator) | This class provides the public APIs to control the Bluetooth CSIP set coordinator. |
| [BluetoothDevice](https://developer.android.com/reference/android/bluetooth/BluetoothDevice) | Represents a remote Bluetooth device. |
| [BluetoothDevice.BluetoothAddress](https://developer.android.com/reference/android/bluetooth/BluetoothDevice.BluetoothAddress) | A data class for Bluetooth address and address type. |
| [BluetoothGatt](https://developer.android.com/reference/android/bluetooth/BluetoothGatt) | Public API for the Bluetooth GATT Profile. |
| [BluetoothGattCallback](https://developer.android.com/reference/android/bluetooth/BluetoothGattCallback) | This abstract class is used to implement `BluetoothGatt` callbacks. |
| [BluetoothGattCharacteristic](https://developer.android.com/reference/android/bluetooth/BluetoothGattCharacteristic) | Represents a Bluetooth GATT Characteristic A GATT characteristic is a basic data element used to construct a GATT service, `BluetoothGattService`. |
| [BluetoothGattConnectionSettings](https://developer.android.com/reference/android/bluetooth/BluetoothGattConnectionSettings) | Defines parameters for creating BluetoothGatt connection. |
| [BluetoothGattConnectionSettings.Builder](https://developer.android.com/reference/android/bluetooth/BluetoothGattConnectionSettings.Builder) | Builder for `BluetoothGattConnectionSettings`. |
| [BluetoothGattDescriptor](https://developer.android.com/reference/android/bluetooth/BluetoothGattDescriptor) | Represents a Bluetooth GATT Descriptor GATT Descriptors contain additional information and attributes of a GATT characteristic, `BluetoothGattCharacteristic`. |
| [BluetoothGattServer](https://developer.android.com/reference/android/bluetooth/BluetoothGattServer) | Public API for the Bluetooth GATT Profile server role. |
| [BluetoothGattServerCallback](https://developer.android.com/reference/android/bluetooth/BluetoothGattServerCallback) | This abstract class is used to implement `BluetoothGattServer` callbacks. |
| [BluetoothGattService](https://developer.android.com/reference/android/bluetooth/BluetoothGattService) | Represents a Bluetooth GATT Service Gatt Service contains a collection of `BluetoothGattCharacteristic`, as well as referenced services. |
| [BluetoothHeadset](https://developer.android.com/reference/android/bluetooth/BluetoothHeadset) | Public API for controlling the Bluetooth Headset Service. |
| [BluetoothHealth](https://developer.android.com/reference/android/bluetooth/BluetoothHealth) | *This class was deprecated in API level 29. Health Device Profile (HDP) and MCAP protocol are no longer used. New apps should use Bluetooth Low Energy based solutions such as `BluetoothGatt`, `BluetoothAdapter.listenUsingL2capChannel()`, or `BluetoothDevice.createL2capChannel(int)`* |
| [BluetoothHealthAppConfiguration](https://developer.android.com/reference/android/bluetooth/BluetoothHealthAppConfiguration) | *This class was deprecated in API level 29. Health Device Profile (HDP) and MCAP protocol are no longer used. New apps should use Bluetooth Low Energy based solutions such as `BluetoothGatt`, `BluetoothAdapter.listenUsingL2capChannel()`, or `BluetoothDevice.createL2capChannel(int)`* |
| [BluetoothHealthCallback](https://developer.android.com/reference/android/bluetooth/BluetoothHealthCallback) | *This class was deprecated in API level 29. Health Device Profile (HDP) and MCAP protocol are no longer used. New apps should use Bluetooth Low Energy based solutions such as `BluetoothGatt`, `BluetoothAdapter.listenUsingL2capChannel()`, or `BluetoothDevice.createL2capChannel(int)`* |
| [BluetoothHearingAid](https://developer.android.com/reference/android/bluetooth/BluetoothHearingAid) | This class provides the public APIs to control the Hearing Aid profile. |
| [BluetoothHidDevice](https://developer.android.com/reference/android/bluetooth/BluetoothHidDevice) | Provides the public APIs to control the Bluetooth HID Device profile. |
| [BluetoothHidDevice.Callback](https://developer.android.com/reference/android/bluetooth/BluetoothHidDevice.Callback) | The template class that applications use to call callback functions on events from the HID host. |
| [BluetoothHidDeviceAppQosSettings](https://developer.android.com/reference/android/bluetooth/BluetoothHidDeviceAppQosSettings) | Represents the Quality of Service (QoS) settings for a Bluetooth HID Device application. |
| [BluetoothHidDeviceAppSdpSettings](https://developer.android.com/reference/android/bluetooth/BluetoothHidDeviceAppSdpSettings) | Represents the Service Discovery Protocol (SDP) settings for a Bluetooth HID Device application. |
| [BluetoothLeAudio](https://developer.android.com/reference/android/bluetooth/BluetoothLeAudio) | This class provides the public APIs to control the LeAudio profile. |
| [BluetoothLeAudioCodecConfig](https://developer.android.com/reference/android/bluetooth/BluetoothLeAudioCodecConfig) | Represents the codec configuration for a Bluetooth LE Audio source device. |
| [BluetoothLeAudioCodecConfig.Builder](https://developer.android.com/reference/android/bluetooth/BluetoothLeAudioCodecConfig.Builder) | Builder for `BluetoothLeAudioCodecConfig`. |
| [BluetoothLeAudioCodecStatus](https://developer.android.com/reference/android/bluetooth/BluetoothLeAudioCodecStatus) | Represents the codec status (configuration and capability) for a Bluetooth Le Audio source device. |
| [BluetoothManager](https://developer.android.com/reference/android/bluetooth/BluetoothManager) | High level manager used to obtain an instance of an `BluetoothAdapter` and to conduct overall Bluetooth Management. |
| [BluetoothServerSocket](https://developer.android.com/reference/android/bluetooth/BluetoothServerSocket) | A listening Bluetooth socket. |
| [BluetoothSocket](https://developer.android.com/reference/android/bluetooth/BluetoothSocket) | A connected or connecting Bluetooth socket. |
| [BluetoothSocketSettings](https://developer.android.com/reference/android/bluetooth/BluetoothSocketSettings) | Defines parameters for creating Bluetooth server and client socket channels. |
| [BluetoothSocketSettings.Builder](https://developer.android.com/reference/android/bluetooth/BluetoothSocketSettings.Builder) | Builder for `BluetoothSocketSettings`. |
| [BluetoothStatusCodes](https://developer.android.com/reference/android/bluetooth/BluetoothStatusCodes) | A class with constants representing possible return values for Bluetooth APIs. |
| [BondStatus](https://developer.android.com/reference/android/bluetooth/BondStatus) | Represents the bond status of a Bluetooth device. |
| [EncryptionStatus](https://developer.android.com/reference/android/bluetooth/EncryptionStatus) | Represents the encryption status of a Bluetooth device. |

## Exceptions

|  |  |
| --- | --- |
| [BluetoothSocketException](https://developer.android.com/reference/android/bluetooth/BluetoothSocketException) | Thrown when an error occurs during a Bluetooth Socket related exception. |

* ## Interfaces

  + [BluetoothAdapter.LeScanCallback](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter.LeScanCallback)
  + [BluetoothProfile](https://developer.android.com/reference/android/bluetooth/BluetoothProfile)
  + [BluetoothProfile.ServiceListener](https://developer.android.com/reference/android/bluetooth/BluetoothProfile.ServiceListener)
* ## Classes

  + [BluetoothA2dp](https://developer.android.com/reference/android/bluetooth/BluetoothA2dp)
  + [BluetoothAdapter](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter)
  + [BluetoothAssignedNumbers](https://developer.android.com/reference/android/bluetooth/BluetoothAssignedNumbers)
  + [BluetoothClass](https://developer.android.com/reference/android/bluetooth/BluetoothClass)
  + [BluetoothClass.Device](https://developer.android.com/reference/android/bluetooth/BluetoothClass.Device)
  + [BluetoothClass.Device.Major](https://developer.android.com/reference/android/bluetooth/BluetoothClass.Device.Major)
  + [BluetoothClass.Service](https://developer.android.com/reference/android/bluetooth/BluetoothClass.Service)
  + [BluetoothCodecConfig](https://developer.android.com/reference/android/bluetooth/BluetoothCodecConfig)
  + [BluetoothCodecConfig.Builder](https://developer.android.com/reference/android/bluetooth/BluetoothCodecConfig.Builder)
  + [BluetoothCodecStatus](https://developer.android.com/reference/android/bluetooth/BluetoothCodecStatus)
  + [BluetoothCodecStatus.Builder](https://developer.android.com/reference/android/bluetooth/BluetoothCodecStatus.Builder)
  + [BluetoothCodecType](https://developer.android.com/reference/android/bluetooth/BluetoothCodecType)
  + [BluetoothCsipSetCoordinator](https://developer.android.com/reference/android/bluetooth/BluetoothCsipSetCoordinator)
  + [BluetoothDevice](https://developer.android.com/reference/android/bluetooth/BluetoothDevice)
  + [BluetoothDevice.BluetoothAddress](https://developer.android.com/reference/android/bluetooth/BluetoothDevice.BluetoothAddress)
  + [BluetoothGatt](https://developer.android.com/reference/android/bluetooth/BluetoothGatt)
  + [BluetoothGattCallback](https://developer.android.com/reference/android/bluetooth/BluetoothGattCallback)
  + [BluetoothGattCharacteristic](https://developer.android.com/reference/android/bluetooth/BluetoothGattCharacteristic)
  + [BluetoothGattConnectionSettings](https://developer.android.com/reference/android/bluetooth/BluetoothGattConnectionSettings)
  + [BluetoothGattConnectionSettings.Builder](https://developer.android.com/reference/android/bluetooth/BluetoothGattConnectionSettings.Builder)
  + [BluetoothGattDescriptor](https://developer.android.com/reference/android/bluetooth/BluetoothGattDescriptor)
  + [BluetoothGattServer](https://developer.android.com/reference/android/bluetooth/BluetoothGattServer)
  + [BluetoothGattServerCallback](https://developer.android.com/reference/android/bluetooth/BluetoothGattServerCallback)
  + [BluetoothGattService](https://developer.android.com/reference/android/bluetooth/BluetoothGattService)
  + [BluetoothHeadset](https://developer.android.com/reference/android/bluetooth/BluetoothHeadset)
  + [BluetoothHealth](https://developer.android.com/reference/android/bluetooth/BluetoothHealth)
  + [BluetoothHealthAppConfiguration](https://developer.android.com/reference/android/bluetooth/BluetoothHealthAppConfiguration)
  + [BluetoothHealthCallback](https://developer.android.com/reference/android/bluetooth/BluetoothHealthCallback)
  + [BluetoothHearingAid](https://developer.android.com/reference/android/bluetooth/BluetoothHearingAid)
  + [BluetoothHidDevice](https://developer.android.com/reference/android/bluetooth/BluetoothHidDevice)
  + [BluetoothHidDevice.Callback](https://developer.android.com/reference/android/bluetooth/BluetoothHidDevice.Callback)
  + [BluetoothHidDeviceAppQosSettings](https://developer.android.com/reference/android/bluetooth/BluetoothHidDeviceAppQosSettings)
  + [BluetoothHidDeviceAppSdpSettings](https://developer.android.com/reference/android/bluetooth/BluetoothHidDeviceAppSdpSettings)
  + [BluetoothLeAudio](https://developer.android.com/reference/android/bluetooth/BluetoothLeAudio)
  + [BluetoothLeAudioCodecConfig](https://developer.android.com/reference/android/bluetooth/BluetoothLeAudioCodecConfig)
  + [BluetoothLeAudioCodecConfig.Builder](https://developer.android.com/reference/android/bluetooth/BluetoothLeAudioCodecConfig.Builder)
  + [BluetoothLeAudioCodecStatus](https://developer.android.com/reference/android/bluetooth/BluetoothLeAudioCodecStatus)
  + [BluetoothManager](https://developer.android.com/reference/android/bluetooth/BluetoothManager)
  + [BluetoothServerSocket](https://developer.android.com/reference/android/bluetooth/BluetoothServerSocket)
  + [BluetoothSocket](https://developer.android.com/reference/android/bluetooth/BluetoothSocket)
  + [BluetoothSocketSettings](https://developer.android.com/reference/android/bluetooth/BluetoothSocketSettings)
  + [BluetoothSocketSettings.Builder](https://developer.android.com/reference/android/bluetooth/BluetoothSocketSettings.Builder)
  + [BluetoothStatusCodes](https://developer.android.com/reference/android/bluetooth/BluetoothStatusCodes)
  + [BondStatus](https://developer.android.com/reference/android/bluetooth/BondStatus)
  + [EncryptionStatus](https://developer.android.com/reference/android/bluetooth/EncryptionStatus)
* ## Exceptions

  + [BluetoothSocketException](https://developer.android.com/reference/android/bluetooth/BluetoothSocketException)
