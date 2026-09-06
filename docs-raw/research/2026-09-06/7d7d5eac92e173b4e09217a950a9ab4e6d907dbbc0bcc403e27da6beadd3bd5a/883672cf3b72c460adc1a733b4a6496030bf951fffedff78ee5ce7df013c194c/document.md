# Deploying apps with declarative management

Use declarative app configurations to deploy managed apps to devices.

## Discussion

Device management services can install, manage, update, configure, and remove apps using the [`AppManaged`](/documentation/DeviceManagement/AppManaged) configuration. Devices can report managed app status using the [`StatusAppManagedList`](/documentation/DeviceManagement/StatusAppManagedList) status item.

If a device management service already manages an app using the [`Install Application`](/documentation/DeviceManagement/Install-Application-Command) or [`Install Enterprise Application`](/documentation/DeviceManagement/Install-Enterprise-Application-Command) commands, it can convert the app to declarative app management.

In macOS, device management services can install, update, and remove packages using the [`Package`](/documentation/DeviceManagement/Package) configuration. A device management service can then manage apps that a package installs using an [`AppManaged`](/documentation/DeviceManagement/AppManaged) configuration targeting the app. Devices can report package status using the [`StatusPackageList`](/documentation/DeviceManagement/StatusPackageList) status item.

## Topics

### Supporting managed apps

[Installing, managing, updating, and removing apps](/documentation/DeviceManagement/installing-managing-updating-and-removing-apps)

Use declarative management to handle all aspects of managing apps on devices.

[Displaying managed apps and packages](/documentation/DeviceManagement/displaying-managed-apps-and-packages)

Use a management app to display managed apps and packages to the user.

[Configuring managed apps and extensions](/documentation/DeviceManagement/configuring-managed-apps-and-extensions)

Provide managed apps and extensions with app configuration and secrets.

[Transferring management of apps to declarative management](/documentation/DeviceManagement/transferring-management-of-apps-to-declarative-management)

Transition apps to declarative management.

[Processing status for managed apps](/documentation/DeviceManagement/processing-status-for-managed-apps)

Process the status that declarative management reports for managed apps.

[Installing packages](/documentation/DeviceManagement/installing-packages)

Use declarative package management to install and remove packages in macOS.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
