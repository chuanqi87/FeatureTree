# android.hardware.usb

Added in [API level 12](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# android.hardware.usb

---

[Kotlin](https://developer.android.com/reference/kotlin/android/hardware/usb/package-summary "View this page in Kotlin")
|Java

Provides support to communicate with USB hardware peripherals that are connected to
Android-powered devices.

For more information, see the
[USB](https://developer.android.com/guide/topics/connectivity/usb) guide.

Use `UsbManager` to access the state of the USB and to
communicate with connected hardware peripherals. Use `UsbDevice` to
communicate with the hardware peripheral if the Android-powered device is acting as the USB host.
Use `UsbAccessory` if the peripheral is acting as the USB host.

## Classes

|  |  |
| --- | --- |
| [UsbAccessory](https://developer.android.com/reference/android/hardware/usb/UsbAccessory) | A class representing a USB accessory, which is an external hardware component that communicates with an android application over USB. |
| [UsbConfiguration](https://developer.android.com/reference/android/hardware/usb/UsbConfiguration) | A class representing a configuration on a `UsbDevice`. |
| [UsbConstants](https://developer.android.com/reference/android/hardware/usb/UsbConstants) | Contains constants for the USB protocol. |
| [UsbDevice](https://developer.android.com/reference/android/hardware/usb/UsbDevice) | This class represents a USB device attached to the android device with the android device acting as the USB host. |
| [UsbDeviceConnection](https://developer.android.com/reference/android/hardware/usb/UsbDeviceConnection) | This class is used for sending and receiving data and control messages to a USB device. |
| [UsbEndpoint](https://developer.android.com/reference/android/hardware/usb/UsbEndpoint) | A class representing an endpoint on a `UsbInterface`. |
| [UsbInterface](https://developer.android.com/reference/android/hardware/usb/UsbInterface) | A class representing an interface on a `UsbDevice`. |
| [UsbManager](https://developer.android.com/reference/android/hardware/usb/UsbManager) | This class allows you to access the state of USB and communicate with USB devices. |
| [UsbRequest](https://developer.android.com/reference/android/hardware/usb/UsbRequest) | A class representing USB request packet. |

* ## Classes

  + [UsbAccessory](https://developer.android.com/reference/android/hardware/usb/UsbAccessory)
  + [UsbConfiguration](https://developer.android.com/reference/android/hardware/usb/UsbConfiguration)
  + [UsbConstants](https://developer.android.com/reference/android/hardware/usb/UsbConstants)
  + [UsbDevice](https://developer.android.com/reference/android/hardware/usb/UsbDevice)
  + [UsbDeviceConnection](https://developer.android.com/reference/android/hardware/usb/UsbDeviceConnection)
  + [UsbEndpoint](https://developer.android.com/reference/android/hardware/usb/UsbEndpoint)
  + [UsbInterface](https://developer.android.com/reference/android/hardware/usb/UsbInterface)
  + [UsbManager](https://developer.android.com/reference/android/hardware/usb/UsbManager)
  + [UsbRequest](https://developer.android.com/reference/android/hardware/usb/UsbRequest)
