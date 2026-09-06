# Shared directories

Configure devices that share directories from the host into the guest system.

## Discussion

Shared directories allow you expose specific directories in the macOS file system to the guest operating system running in a VM, this allows your user to share files between the host and guest operating system. To enable shared directory device support in Linux, configure the Linux guest kernel to enable the `CONFIG_VIRTIO_FS` support.

Configure a VIRTIO file system device using a [`VZVirtioFileSystemDeviceConfiguration`](/documentation/Virtualization/VZVirtioFileSystemDeviceConfiguration). The guest can use the [`tag`](/documentation/Virtualization/VZVirtioFileSystemDeviceConfiguration/tag) label to mount and access the host resources.

The [`VZDirectoryShare`](/documentation/Virtualization/VZDirectoryShare) on the configuration defines the host directories to expose to the guest. To limit or expose new directories to the guest while the VM is running, you can update the directory share with [`VZVirtioFileSystemDevice`](/documentation/Virtualization/VZVirtioFileSystemDevice).

Use [`VZSingleDirectoryShare`](/documentation/Virtualization/VZSingleDirectoryShare) to share the immediate contents of a single directory on the host, or use [`VZMultipleDirectoryShare`](/documentation/Virtualization/VZMultipleDirectoryShare) to share multiple directories from the host and include a specific name for each shared directory.

> Note:
> Shared directories in macOS VMs are only available in macOS 13 and later.

## Topics

### Configurations

[`VZVirtioFileSystemDeviceConfiguration`](/documentation/Virtualization/VZVirtioFileSystemDeviceConfiguration)

An object that represents the configuration of a Virtio file system device.

[`VZDirectorySharingDeviceConfiguration`](/documentation/Virtualization/VZDirectorySharingDeviceConfiguration)

The base class for a directory sharing device configuration.

[`VZLinuxRosettaDirectoryShare`](/documentation/Virtualization/VZLinuxRosettaDirectoryShare)

The Linux directory share for Rosetta.

### Shared directory devices

[`VZVirtioFileSystemDevice`](/documentation/Virtualization/VZVirtioFileSystemDevice)

An object the defines a VIRTIO file system device.

[`VZDirectorySharingDevice`](/documentation/Virtualization/VZDirectorySharingDevice)

The base class that represents a directory sharing device in a VM.

### Directory Shares

[`VZMultipleDirectoryShare`](/documentation/Virtualization/VZMultipleDirectoryShare)

An object that describes a directory share for multiple directories.

[`VZSingleDirectoryShare`](/documentation/Virtualization/VZSingleDirectoryShare)

An object that defines the directory share for a single directory.

[`VZSharedDirectory`](/documentation/Virtualization/VZSharedDirectory)

A directory on the host that you can expose to a guest.

[`VZDirectoryShare`](/documentation/Virtualization/VZDirectoryShare)

The base class for a directory share.

[`VZLinuxRosettaDirectoryShare`](/documentation/Virtualization/VZLinuxRosettaDirectoryShare)

The Linux directory share for Rosetta.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
