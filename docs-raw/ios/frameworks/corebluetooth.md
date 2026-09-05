* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/corebluetooth#app-main)

Framework

# Core Bluetooth

Communicate with Bluetooth low energy and BR/EDR (“Classic”) Devices.

iOS 5.0+iPadOS 5.0+Mac Catalyst 13.0+macOS 10.10+tvOS 9.0+visionOS 1.0+watchOS 4.0+

## [Overview](https://developer.apple.com/documentation/corebluetooth\#overview)

The Core Bluetooth framework provides the classes needed for your apps to communicate with Bluetooth-equipped low energy (LE) and Basic Rate / Enhanced Data Rate (BR/EDR) wireless technology.

Don’t subclass any of the classes of the Core Bluetooth framework. Overriding these classes isn’t supported and results in undefined behavior.

Core Bluetooth background execution modes aren’t supported in iPad apps running on macOS.

In iOS 26 and later, your app can continue certain activities in the background if the app starts a Live Activity before it goes to the background. If your app has an instantiated [`CBManager`](https://developer.apple.com/documentation/corebluetooth/cbmanager) and starts a Live Activity, it can use the same privileges while in the background that it uses when it is in the foreground. This means activities like scanning without providing service UUID’s and scanning with duplicates filter disabled will be allowed while in the background. For more information about creating Live Activities, see [ActivityKit](https://developer.apple.com/documentation/ActivityKit).

## [Topics](https://developer.apple.com/documentation/corebluetooth\#topics)

### [Centrals](https://developer.apple.com/documentation/corebluetooth\#Centrals)

[`class CBCentral`](https://developer.apple.com/documentation/corebluetooth/cbcentral)

A remote device connected to a local app, which is acting as a peripheral.

[`class CBCentralManager`](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager)

An object that scans for, discovers, connects to, and manages peripherals.

[`protocol CBCentralManagerDelegate`](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate)

A protocol that provides updates for the discovery and management of peripheral devices.

### [Peripherals](https://developer.apple.com/documentation/corebluetooth\#Peripherals)

[`class CBPeripheral`](https://developer.apple.com/documentation/corebluetooth/cbperipheral)

A remote peripheral device.

[`protocol CBPeripheralDelegate`](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate)

A protocol that provides updates on the use of a peripheral’s services.

[`class CBPeripheralManager`](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager)

An object that manages and advertises peripheral services exposed by this app.

[`protocol CBPeripheralManagerDelegate`](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate)

A protocol that provides updates for local peripheral state and interactions with remote central devices.

[`class CBAttribute`](https://developer.apple.com/documentation/corebluetooth/cbattribute)

A representation of common aspects of services offered by a peripheral.

[`struct CBAttributePermissions`](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions)

Values that represent the read, write, and encryption permissions for a characteristic’s value.

### [Data Transfer](https://developer.apple.com/documentation/corebluetooth\#Data-Transfer)

[Transferring Data Between Bluetooth Low Energy Devices](https://developer.apple.com/documentation/corebluetooth/transferring-data-between-bluetooth-low-energy-devices)

Create a Bluetooth low energy central and peripheral device, and allow them to discover each other and exchange data.

### [Channel Sounding](https://developer.apple.com/documentation/corebluetooth\#Channel-Sounding)

[Measuring distance between devices using Channel Sounding](https://developer.apple.com/documentation/corebluetooth/measuring-distance-between-devices-using-channel-sounding)

Measure the distance between two Bluetooth Low Energy devices in real time with Channel Sounding.

[`class CBChannelSoundingProcedureResults`](https://developer.apple.com/documentation/corebluetooth/cbchannelsoundingprocedureresults) Beta

[`class CBChannelSoundingSessionConfiguration`](https://developer.apple.com/documentation/corebluetooth/cbchannelsoundingsessionconfiguration) Beta

[`let CBUUIDCharacteristicObservationScheduleString: String`](https://developer.apple.com/documentation/corebluetooth/cbuuidcharacteristicobservationschedulestring)

### [Services](https://developer.apple.com/documentation/corebluetooth\#Services)

[`class CBService`](https://developer.apple.com/documentation/corebluetooth/cbservice)

A collection of data and associated behaviors that accomplish a function or feature of a device.

[`class CBMutableService`](https://developer.apple.com/documentation/corebluetooth/cbmutableservice)

A service with writeable property values.

[`class CBCharacteristic`](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic)

A characteristic of a remote peripheral’s service.

[`class CBMutableCharacteristic`](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic)

A characteristic of a local peripheral’s service.

[`class CBDescriptor`](https://developer.apple.com/documentation/corebluetooth/cbdescriptor)

An object that provides further information about a remote peripheral’s characteristic.

[`class CBMutableDescriptor`](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor)

An object that provides additional information about a local peripheral’s characteristic.

### [Supporting Types](https://developer.apple.com/documentation/corebluetooth\#Supporting-Types)

[`class CBManager`](https://developer.apple.com/documentation/corebluetooth/cbmanager)

The abstract base class that manages central and peripheral objects.

[`class CBATTRequest`](https://developer.apple.com/documentation/corebluetooth/cbattrequest)

A request that uses the Attribute Protocol (ATT).

[`class CBPeer`](https://developer.apple.com/documentation/corebluetooth/cbpeer)

An object that represents a remote device.

[`class CBUUID`](https://developer.apple.com/documentation/corebluetooth/cbuuid)

A universally unique identifier, as defined by Bluetooth standards.

### [Bluetooth Classic Support](https://developer.apple.com/documentation/corebluetooth\#Bluetooth-Classic-Support)

[Using Core Bluetooth Classic](https://developer.apple.com/documentation/corebluetooth/using-core-bluetooth-classic)

Discover and communicate with a Bluetooth Classic device by using the Core Bluetooth APIs.

### [Errors](https://developer.apple.com/documentation/corebluetooth\#Errors)

[`struct CBError`](https://developer.apple.com/documentation/corebluetooth/cberror-swift.struct)

An error that Core Bluetooth returns during Bluetooth transactions.

[`let CBErrorDomain: String`](https://developer.apple.com/documentation/corebluetooth/cberrordomain)

The domain for Core Bluetooth errors.

[`enum Code`](https://developer.apple.com/documentation/corebluetooth/cberror-swift.struct/code)

The codes for errors that Core Bluetooth returns during Bluetooth transactions.

[`struct CBATTError`](https://developer.apple.com/documentation/corebluetooth/cbatterror-swift.struct)

An error that Core Bluetooth returns while using Attribute Protocol (ATT).

[`let CBATTErrorDomain: String`](https://developer.apple.com/documentation/corebluetooth/cbatterrordomain)

The domain for Core Bluetooth ATT errors.

[`enum Code`](https://developer.apple.com/documentation/corebluetooth/cbatterror-swift.struct/code)

The possible errors returned by a GATT server (a remote peripheral) during Bluetooth low energy ATT transactions.

[`struct CBATTError`](https://developer.apple.com/documentation/corebluetooth/cbatterror-swift.struct)

An error that Core Bluetooth returns while using Attribute Protocol (ATT).

### [Deprecated](https://developer.apple.com/documentation/corebluetooth\#Deprecated)

[`enum CBCentralManagerState`](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate)

Values that represent the current state of a central manager object.

Deprecated

[`enum CBPeripheralManagerState`](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate)

Values that represent the current state of the peripheral manager.

Deprecated

[API Reference\\
Deprecated Constants](https://developer.apple.com/documentation/corebluetooth/deprecated-constants)

This document describes the constants found in the Core Bluetooth framework.

## [See Also](https://developer.apple.com/documentation/corebluetooth\#see-also)

### [Related Documentation](https://developer.apple.com/documentation/corebluetooth\#Related-Documentation)

[Core Bluetooth Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257)

Current page is Core Bluetooth