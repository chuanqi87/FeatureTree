# MIDI Bluetooth

Connect to Bluetooth Low Energy MIDI peripherals.

## Discussion

In macOS 13 or later and iOS 16 or later, the system automatically reconnects Bluetooth Low Energy (BLE) MIDI peripherals when powered on, if the device supports pairing. Previously, it was necessary to use Audio MIDI Setup to establish BLE MIDI connections.

For devices that don’t support pairing, [`Core MIDI`](/documentation/CoreMIDI) can enable <doc://com.apple.documentation/documentation/CoreBluetooth> connections for input/output (I/O).

This API enables connection of BLE MIDI peripherals that don’t support pairing using <doc://com.apple.documentation/documentation/CoreBluetooth> with the following steps:

1. Scan for and connect to a BLE MIDI peripheral.
2. Confirm the peripheral has a BLE MIDI service.
3. Confirm the BLE MIDI service on the peripheral has a MIDI I/O characteristic for the MIDI service.

Once a BLE MIDI peripheral connects — and you confirm that it possess both the BLE MIDI service and BLE MIDI I/O characteristic — call [`MIDIBluetoothDriverActivateAllConnections()`](/documentation/CoreMIDI/MIDIBluetoothDriverActivateAllConnections()) to have [`Core MIDI`](/documentation/CoreMIDI) enable I/O on those connections.

To disconnect a peripheral, obtain the <doc://com.apple.documentation/documentation/CoreBluetooth/CBUUID> of the peripheral and call [`MIDIBluetoothDriverDisconnect(_:)`](/documentation/CoreMIDI/MIDIBluetoothDriverDisconnect(_:)).

## Topics

### Managing Device Connections

[`MIDIBluetoothDriverActivateAllConnections`](/documentation/CoreMIDI/MIDIBluetoothDriverActivateAllConnections())

Promote all active Bluetooth connections into an online MIDI device capable of input and output.

[`MIDIBluetoothDriverDisconnect`](/documentation/CoreMIDI/MIDIBluetoothDriverDisconnect(_:))

Disconnect the Bluetooth MIDI driver from a Bluetooth Low Energy MIDI peripheral.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
