# Handling NotNow status responses

Handle when a device won’t execute a command and instead returns a NotNow status.

## Discussion

Specific conditions prevent a device from executing a command. For example, a device won’t execute some commands before the first unlock after a device boot. When this occurs, a device can respond to the device management service with a `NotNow` status to indicate that later retries may succeed.

When the service receives a `NotNow` response from a device, it can either stop sending commands to the device or send another command to it on the same connection.

## Understand device polling

When a device management service stops sending commands to a device, the device automatically polls the service when conditions change. However, the device doesn’t cache the failed command. If you configure your device management service to instruct the device to retry the command, it must send the command again when the device polls the service. The device management service doesn’t need to send another push notification in response to this status, but it can send another one to instruct the device to poll the service immediately.

If the device management service sends another command to the client on the same connection, and this new command returns anything other than a `NotNow` response, the device won’t automatically poll the service as it would if the first command executed successfully. The service must send a push notification at a later time to instruct the device to reconnect. The device only polls the device management service in response to a `NotNow` status if that’s the last status sent by the device to the service.

## Handle NotNow responses

In macOS, a device may not execute commands, but instead respond with a `NotNow` status during these conditions:

- The device is running on battery power in Power Nap and the service sends any command other than [`DeleteUserCommand`](/documentation/DeviceManagement/DeleteUserCommand), [`DeviceLockCommand`](/documentation/DeviceManagement/DeviceLockCommand), [`EraseDeviceCommand`](/documentation/DeviceManagement/EraseDeviceCommand), [`RestartDeviceCommand`](/documentation/DeviceManagement/RestartDeviceCommand), [`ShutDownDeviceCommand`](/documentation/DeviceManagement/ShutDownDeviceCommand), [`UserListCommand`](/documentation/DeviceManagement/UserListCommand), [`ActivationLockBypassCodeCommand`](/documentation/DeviceManagement/ActivationLockBypassCodeCommand), [`ClearActivationLockBypassCodeCommand`](/documentation/DeviceManagement/ClearActivationLockBypassCodeCommand), or [`UnlockUserAccountCommand`](/documentation/DeviceManagement/UnlockUserAccountCommand).
- The device management service sends an `InstallProfile` or `RemoveProfile` command on the user connection and the user’s keychain is locked.
- The device is blocking the user’s login while it contacts the device management service and the service sends a request that can take a long time to process; for example, `InstalledApplicationList`.

The following commands don’t result in a `NotNow` status response on iOS devices:

- [`DeviceInformationCommand`](/documentation/DeviceManagement/DeviceInformationCommand)
- [`ProfileListCommand`](/documentation/DeviceManagement/ProfileListCommand)
- [`DeviceLockCommand`](/documentation/DeviceManagement/DeviceLockCommand)
- [`EraseDeviceCommand`](/documentation/DeviceManagement/EraseDeviceCommand)
- [`ClearPasscodeCommand`](/documentation/DeviceManagement/ClearPasscodeCommand)
- [`ProvisioningProfileListCommand`](/documentation/DeviceManagement/ProvisioningProfileListCommand)
- [`InstalledApplicationListCommand`](/documentation/DeviceManagement/InstalledApplicationListCommand)
- [`RestrictionsCommand`](/documentation/DeviceManagement/RestrictionsCommand)

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
