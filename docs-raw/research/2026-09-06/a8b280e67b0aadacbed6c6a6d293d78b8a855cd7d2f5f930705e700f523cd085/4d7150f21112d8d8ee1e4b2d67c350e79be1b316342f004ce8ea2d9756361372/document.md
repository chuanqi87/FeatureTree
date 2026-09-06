# Transferring management of apps to declarative management

Transition apps to declarative management.

## Discussion

A device management service can transfer management of an MDM-managed app to declarative management. With this feature, you can seamlessly transition to declarative management and not have to remove the app before managing it again.

## Transfer app management

To transfer management of an existing MDM-managed app, a device management service provides a [`AppManaged`](/documentation/DeviceManagement/AppManaged) configuration to the device. If the app is from the App Store, the service sets the configuration’s `AppStoreID` or `BundleID` key to match the app. If the app is an enterprise app, the service sets the configuration’s `ManifestURL` key to the same manifest document URL from the MDM [`Install Application`](/documentation/DeviceManagement/Install-Application-Command) command that installed the app. The device takes over management of the app when it applies the configuration.

MDM commands for installing, listing, and removing managed apps don’t operate on declarative managed apps, including those transferred from MDM. Instead, the device management service uses the [`AppManaged`](/documentation/DeviceManagement/AppManaged) configuration to control app updates and removal. The service also subscribes to the [`StatusAppManagedList`](/documentation/DeviceManagement/StatusAppManagedList) status item to receive reports on all declarative managed apps.

The device management service detects the app’s management transfer by subscribing to two status items: [`StatusMDMApp`](/documentation/DeviceManagement/StatusMDMApp), which reports MDM-managed app status, and [`StatusAppManagedList`](/documentation/DeviceManagement/StatusAppManagedList), which reports declarative managed app status. When the transfer occurs, the managed app’s entry in [`StatusMDMApp`](/documentation/DeviceManagement/StatusMDMApp) indicates its removal, and a new entry for the app appears in [`StatusAppManagedList`](/documentation/DeviceManagement/StatusAppManagedList).

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
