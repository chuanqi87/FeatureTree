# Core Bluetooth

Communicate with Bluetooth low energy and BR/EDR (“Classic”) Devices.

## Overview

The Core Bluetooth framework provides the classes needed for your apps to communicate with Bluetooth-equipped low energy (LE) and Basic Rate / Enhanced Data Rate (BR/EDR) wireless technology.

Don’t subclass any of the classes of the Core Bluetooth framework. Overriding these classes isn’t supported and results in undefined behavior.

Core Bluetooth background execution modes aren’t supported in iPad apps running on macOS.

In iOS 26 and later, your app can continue certain activities in the background if the app starts a Live Activity before it goes to the background.
If your app has an instantiated [`CBManager`](/documentation/CoreBluetooth/CBManager) and starts a Live Activity, it can use the same privileges while in the background that it uses when it is in the foreground.
This means activities like scanning without providing service UUID’s and scanning with duplicates filter disabled will be allowed while in the background.
For more information about creating Live Activities, see [ActivityKit](https://developer.apple.com/documentation/ActivityKit).

> Important:
> Your app will crash if its `Info.plist` doesn’t include usage description keys for the types of data it needs to access. To access Core Bluetooth APIs on apps linked on or after iOS 13, include the <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSBluetoothAlwaysUsageDescription> key. In iOS 12 and earlier, include <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSBluetoothPeripheralUsageDescription> to access Bluetooth peripheral data.

## Topics

### Centrals

[`CBCentral`](/documentation/CoreBluetooth/CBCentral)

A remote device connected to a local app, which is acting as a peripheral.

[`CBCentralManager`](/documentation/CoreBluetooth/CBCentralManager)

An object that scans for, discovers, connects to, and manages peripherals.

[`CBCentralManagerDelegate`](/documentation/CoreBluetooth/CBCentralManagerDelegate)

A protocol that provides updates for the discovery and management of peripheral devices.

### Peripherals

[`CBPeripheral`](/documentation/CoreBluetooth/CBPeripheral)

A remote peripheral device.

[`CBPeripheralDelegate`](/documentation/CoreBluetooth/CBPeripheralDelegate)

A protocol that provides updates on the use of a peripheral’s services.

[`CBPeripheralManager`](/documentation/CoreBluetooth/CBPeripheralManager)

An object that manages and advertises peripheral services exposed by this app.

[`CBPeripheralManagerDelegate`](/documentation/CoreBluetooth/CBPeripheralManagerDelegate)

A protocol that provides updates for local peripheral state and interactions with remote central devices.

[`CBAttribute`](/documentation/CoreBluetooth/CBAttribute)

A representation of common aspects of services offered by a peripheral.

[`CBAttributePermissions`](/documentation/CoreBluetooth/CBAttributePermissions)

Values that represent the read, write, and encryption permissions for a characteristic’s value.

### Data Transfer

[Transferring Data Between Bluetooth Low Energy Devices](/documentation/CoreBluetooth/transferring-data-between-bluetooth-low-energy-devices)

Create a Bluetooth low energy central and peripheral device, and allow them to discover each other and exchange data.

### Channel Sounding

[Measuring distance between devices using Channel Sounding](/documentation/CoreBluetooth/measuring-distance-between-devices-using-channel-sounding)

Measure the distance between two Bluetooth Low Energy devices in real time with Channel Sounding.

[`CBChannelSoundingProcedureResults`](/documentation/CoreBluetooth/CBChannelSoundingProcedureResults)

[`CBChannelSoundingSessionConfiguration`](/documentation/CoreBluetooth/CBChannelSoundingSessionConfiguration)

[`CBUUIDCharacteristicObservationScheduleString`](/documentation/CoreBluetooth/CBUUIDCharacteristicObservationScheduleString)

### Services

[`CBService`](/documentation/CoreBluetooth/CBService)

A collection of data and associated behaviors that accomplish a function or feature of a device.

[`CBMutableService`](/documentation/CoreBluetooth/CBMutableService)

A service with writeable property values.

[`CBCharacteristic`](/documentation/CoreBluetooth/CBCharacteristic)

A characteristic of a remote peripheral’s service.

[`CBMutableCharacteristic`](/documentation/CoreBluetooth/CBMutableCharacteristic)

A characteristic of a local peripheral’s service.

[`CBDescriptor`](/documentation/CoreBluetooth/CBDescriptor)

An object that provides further information about a remote peripheral’s characteristic.

[`CBMutableDescriptor`](/documentation/CoreBluetooth/CBMutableDescriptor)

An object that provides additional information about a local peripheral’s characteristic.

### Supporting Types

[`CBManager`](/documentation/CoreBluetooth/CBManager)

The abstract base class that manages central and peripheral objects.

[`CBATTRequest`](/documentation/CoreBluetooth/CBATTRequest)

A request that uses the Attribute Protocol (ATT).

[`CBPeer`](/documentation/CoreBluetooth/CBPeer)

An object that represents a remote device.

[`CBUUID`](/documentation/CoreBluetooth/CBUUID)

A universally unique identifier, as defined by Bluetooth standards.

### Bluetooth Classic Support

[Using Core Bluetooth Classic](/documentation/CoreBluetooth/using-core-bluetooth-classic)

Discover and communicate with a Bluetooth Classic device by using the Core Bluetooth APIs.

### Errors

[`CBError`](/documentation/CoreBluetooth/CBError-swift.struct)

An error that Core Bluetooth returns during Bluetooth transactions.

[`CBErrorDomain`](/documentation/CoreBluetooth/CBErrorDomain)

The domain for Core Bluetooth errors.

[`Code`](/documentation/CoreBluetooth/CBError-swift.struct/Code)

The codes for errors that Core Bluetooth returns during Bluetooth transactions.

[`CBATTError`](/documentation/CoreBluetooth/CBATTError-swift.struct)

An error that Core Bluetooth returns while using Attribute Protocol (ATT).

[`CBATTErrorDomain`](/documentation/CoreBluetooth/CBATTErrorDomain)

The domain for Core Bluetooth ATT errors.

[`Code`](/documentation/CoreBluetooth/CBATTError-swift.struct/Code)

The possible errors returned by a GATT server (a remote peripheral) during Bluetooth low energy ATT transactions.

[`CBATTError`](/documentation/CoreBluetooth/CBATTError-swift.struct)

An error that Core Bluetooth returns while using Attribute Protocol (ATT).

### Deprecated

[`CBCentralManagerState`](/documentation/CoreBluetooth/CBCentralManagerState)

Values that represent the current state of a central manager object.

[`CBPeripheralManagerState`](/documentation/CoreBluetooth/CBPeripheralManagerState)

Values that represent the current state of the peripheral manager.

[Deprecated Constants](/documentation/CoreBluetooth/deprecated-constants)

This document describes the constants found in the Core Bluetooth framework.

## See Also

  [Core Bluetooth Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
