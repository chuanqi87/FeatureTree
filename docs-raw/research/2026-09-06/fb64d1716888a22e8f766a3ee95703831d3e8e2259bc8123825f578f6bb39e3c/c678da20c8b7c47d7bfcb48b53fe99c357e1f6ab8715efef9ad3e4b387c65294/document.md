# SCSIPeripheralsDriverKit

Develop drivers for peripherals that use SCSI Block Command and Multimedia Command protocols.

## Overview

The SCSIPeripheralsDriverKit framework supports the development of drivers for external devices that communicate using SCSI protocols. This framework operates at the logical unit level. For block-level driver development, use <doc://com.apple.documentation/documentation/BlockStorageDeviceDriverKit>. For protocol-level driver development, use <doc://com.apple.documentation/documentation/SCSIControllerDriverKit>.

Develop your driver by subclassing [`IOUserSCSIPeripheralDeviceType00`](/documentation/SCSIPeripheralsDriverKit/IOUserSCSIPeripheralDeviceType00) or [`IOUserSCSIPeripheralDeviceType05`](/documentation/SCSIPeripheralsDriverKit/IOUserSCSIPeripheralDeviceType05), depending on whether your device works with SCSI Block Commands (SBC) or SCSI Multimedia Commands (SMC), respectively. In your subclass, override all methods the framework declares as pure virtual. Then package your driver in an app that uses the <doc://com.apple.documentation/documentation/SystemExtensions> framework to install and upgrade the driver on the user’s Mac.

> Note:
> SCSIPeripheralsDriverKit is available on macOS.

## Topics

### Driver interfaces

[`IOUserSCSIPeripheralDeviceType00`](/documentation/SCSIPeripheralsDriverKit/IOUserSCSIPeripheralDeviceType00)

A DriverKit provider object that works with type 00 devices, those that use SCSI Block Commands (SBC).

[`IOUserSCSIPeripheralDeviceType05`](/documentation/SCSIPeripheralsDriverKit/IOUserSCSIPeripheralDeviceType05)

A DriverKit provider object that works with type 05 devices, those that use SCSI Multimedia Commands (SMC).

### Device commands

[SCSI commands](/documentation/SCSIPeripheralsDriverKit/scsi-commands)

Call the framework’s free functions to populate Command Descriptor Blocks (CDBs) to send to your peripheral.

### Classes

[`IOUserSCSIPeripheralDeviceType07`](/documentation/SCSIPeripheralsDriverKit/IOUserSCSIPeripheralDeviceType07)

### Reference

[SCSIPeripheralsDriverKit Enumerations](/documentation/SCSIPeripheralsDriverKit/scsiperipheralsdriverkit-enumerations)

[SCSIPeripheralsDriverKit Data Types](/documentation/SCSIPeripheralsDriverKit/scsiperipheralsdriverkit-data-types)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
