# Device Management

Manage your organization’s devices remotely.

## Overview

Deploying a device management service allows administrators to securely and remotely configure enrolled devices. Administrators use Apple School Manager or Apple Business Manager to enroll organization-owned devices, and users can enroll their own devices. After enrolling a device, administrators can update software and device settings; monitor compliance with organizational policies; remotely erase or lock devices; and install apps, books, and subscriptions developed in-house or purchased through Apple School Manager or Apple Business Manager.

A device management service uses the Mobile Device Management (MDM) protocol to establish a communication channel with devices and declarative configurations, as well as configuration profiles to deploy settings.

Device management works with Managed App Distribution and Managed App Configuration to provide a seamless app download and launch experience. For more information, see <doc://com.apple.documentation/documentation/ManagedAppDistribution> and <doc://com.apple.documentation/documentation/ManagedApp>.

## Topics

### Implementing device management

[Device management essentials](/documentation/DeviceManagement/device-management-essentials)

Set up and maintain connectivity with devices and leverage declarative device management.

[Device enrollment](/documentation/DeviceManagement/device-enrollment)

Implement Automated Device Enrollment and account-driven enrollments.

[Identity management](/documentation/DeviceManagement/identity-management)

Use Platform Single Sign-on and Managed Device Attestation on managed devices.

[Content management](/documentation/DeviceManagement/content-management)

Deploy apps and books to managed devices.

[Device life cycle](/documentation/DeviceManagement/device-life-cycle)

Manage software updates, migrate managed devices, and return them into service.

### MDM protocol

[Commands and queries](/documentation/DeviceManagement/commands-and-queries)

Remotely execute management commands and queries on managed devices.

[Check-in](/documentation/DeviceManagement/check-in)

Authenticate devices and maintain push tokens.

### Declarative management

[Declarations](/documentation/DeviceManagement/devicemanagement-declarations)

Configure devices using declarative device management.

[Status items](/documentation/DeviceManagement/status-items)

Monitor device state using status reports.

### Configuration profiles

[Profile-specific payload keys](/documentation/DeviceManagement/profile-specific-payload-keys)

Apply settings to devices using configuration profiles.

### Miscellaneous data formats

[`ManifestURL`](/documentation/DeviceManagement/ManifestURL)

The URL to the app manifest.

[`PasswordHash`](/documentation/DeviceManagement/PasswordHash)

A dictionary that contains the password hash for the account.

### Deployment services

[Device assignment](/documentation/DeviceManagement/device-assignment)

Manage devices for your students and employees.

[Roster management](/documentation/DeviceManagement/roster-management)

Manage classes for your students and teachers.

[App, Book, and Subscription Management](/documentation/DeviceManagement/app-book-and-subscription-management)

Manage apps, books, and subscriptions for your students and employees.

  <doc://com.apple.documentation/documentation/apple-school-and-business-manager-api>

### Removed items

[Removed commands and profiles](/documentation/DeviceManagement/removed-commands-and-profiles)

Commands and configuration profiles that have been removed and are no longer supported.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
