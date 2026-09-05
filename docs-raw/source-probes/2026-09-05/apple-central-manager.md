<!--
{
  "availability" : [
    "iOS: 5.0.0 -",
    "iPadOS: 5.0.0 -",
    "macCatalyst: 13.1.0 -",
    "macOS: 10.7.0 -",
    "tvOS: 9.0.0 -",
    "visionOS: 1.0.0 -",
    "watchOS: 2.0.0 -"
  ],
  "documentType" : "symbol",
  "framework" : "CoreBluetooth",
  "identifier" : "/documentation/CoreBluetooth/CBCentralManager",
  "metadataVersion" : "0.1.0",
  "role" : "Class",
  "symbol" : {
    "kind" : "Class",
    "modules" : [
      "Core Bluetooth"
    ],
    "preciseIdentifier" : "c:objc(cs)CBCentralManager"
  },
  "title" : "CBCentralManager"
}
-->

# CBCentralManager

An object that scans for, discovers, connects to, and manages peripherals.

```
class CBCentralManager
```

## Overview

[`CBCentralManager`](/documentation/CoreBluetooth/CBCentralManager) objects manage discovered or connected remote peripheral devices (represented by [`CBPeripheral`](/documentation/CoreBluetooth/CBPeripheral) objects), including scanning for, discovering, and connecting to advertising peripherals.

Before calling the [`CBCentralManager`](/documentation/CoreBluetooth/CBCentralManager) methods, set the state of the central manager object to powered on, as indicated by the [`CBCentralManagerState.poweredOn`](/documentation/CoreBluetooth/CBCentralManagerState/poweredOn) constant. This state indicates that the central device (your iPhone or iPad, for instance) supports Bluetooth low energy and that Bluetooth is on and available for use.

## Topics

### Initializing a Central Manager

[`-  init`](/documentation/CoreBluetooth/CBCentralManager/init())

Initializes the central manager without a delegate.

[`-  initWithDelegate:queue:`](/documentation/CoreBluetooth/CBCentralManager/init(delegate:queue:))

Initializes the central manager with a specified delegate and dispatch queue.

[`-  initWithDelegate:queue:options:`](/documentation/CoreBluetooth/CBCentralManager/init(delegate:queue:options:))

Initializes the central manager with specified delegate, dispatch queue, and initialization options.

[Central Manager Initialization Options](/documentation/CoreBluetooth/central-manager-initialization-options)

Keys used to pass options when initializing a central manager.

[Central Manager State Restoration Options](/documentation/CoreBluetooth/central-manager-state-restoration-options)

Restore central manager state in scene-based apps.

### Establishing or Canceling Connections with Peripherals

[`-  connectPeripheral:options:`](/documentation/CoreBluetooth/CBCentralManager/connect(_:options:))

Establishes a local connection to a peripheral.

[Peripheral Connection Options](/documentation/CoreBluetooth/peripheral-connection-options)

Keys used to pass options when connecting to a peripheral.

[`-  cancelPeripheralConnection:`](/documentation/CoreBluetooth/CBCentralManager/cancelPeripheralConnection(_:))

Cancels an active or pending local connection to a peripheral.

### Retrieving Lists of Peripherals

[`-  retrieveConnectedPeripheralsWithServices:`](/documentation/CoreBluetooth/CBCentralManager/retrieveConnectedPeripherals(withServices:))

Returns a list of the peripherals connected to the system whose services match a given set of criteria.

[`-  retrievePeripheralsWithIdentifiers:`](/documentation/CoreBluetooth/CBCentralManager/retrievePeripherals(withIdentifiers:))

Returns a list of known peripherals by their identifiers.

### Scanning or Stopping Scans of Peripherals

[`-  scanForPeripheralsWithServices:options:`](/documentation/CoreBluetooth/CBCentralManager/scanForPeripherals(withServices:options:))

Scans for peripherals that are advertising services.

[Peripheral Scanning Options](/documentation/CoreBluetooth/peripheral-scanning-options)

Keys used to pass options when scanning for peripherals.

[`-  stopScan`](/documentation/CoreBluetooth/CBCentralManager/stopScan())

Asks the central manager to stop scanning for peripherals.

[`isScanning`](/documentation/CoreBluetooth/CBCentralManager/isScanning)

A Boolean value that indicates whether the central is currently scanning.

### Inspecting Feature Support

[`+  supportsFeatures:`](/documentation/CoreBluetooth/CBCentralManager/supports(_:))

Returns a Boolean that indicates whether the device supports a specific set of features.

[`Feature`](/documentation/CoreBluetooth/CBCentralManager/Feature)

An option set of device-specific features.

### Monitoring Properties

[`delegate`](/documentation/CoreBluetooth/CBCentralManager/delegate)

The delegate object that you want to receive central manager events.

### Receiving Connection Events

[`-  registerForConnectionEventsWithOptions:`](/documentation/CoreBluetooth/CBCentralManager/registerForConnectionEvents(options:))

Register for an event notification when the central manager makes a connection matching the given options.

[Peripheral Connection Options](/documentation/CoreBluetooth/peripheral-connection-options)

Keys used to pass options when connecting to a peripheral.

[`CBConnectionEvent`](/documentation/CoreBluetooth/CBConnectionEvent)

A change to the connection state of a peer.

[`CBConnectionEventMatchingOption`](/documentation/CoreBluetooth/CBConnectionEventMatchingOption)

A set of options to use when registering for connection events.

### Deprecated

[`CBCentralManagerState`](/documentation/CoreBluetooth/CBCentralManagerState)

Values that represent the current state of a central manager object.

## Relationships

### Conforms To

[`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)

[`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)

[`Equatable`](/documentation/Swift/Equatable)

[`CVarArg`](/documentation/Swift/CVarArg)

[`NSObjectProtocol`](/documentation/ObjectiveC/NSObjectProtocol)

[`Hashable`](/documentation/Swift/Hashable)

### Inherits From

[`CBManager`](/documentation/CoreBluetooth/CBManager)

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)