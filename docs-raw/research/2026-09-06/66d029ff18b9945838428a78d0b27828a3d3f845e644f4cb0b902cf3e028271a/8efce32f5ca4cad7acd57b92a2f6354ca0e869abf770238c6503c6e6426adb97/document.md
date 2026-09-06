# Enrollment with Platform Single Sign-on

Authenticate users during Automated Device Enrollment using Platform Single Sign-on.

## Discussion

Platform Single Sign-on (Platform SSO) allows a device management service to configure SSO extensions that integrate with the macOS login window, enabling seamless access to apps and websites immediately after logging in without reentering credentials. Local account passwords can optionally stay in sync with the identity provider (IdP), and users can still unlock their Mac using Touch ID or Apple Watch.

A device management service can also use Platform SSO to improve the enrollment flow in two ways during macOS device setup after the administrator registers the device for Automated Device Enrollment.

In the first case, a device management service uses Platform SSO to allow the person to sign in before starting the enrollment process. This allows the service to validate the person’s credentials before enrollment, and then allows the device to automatically set up a local user account that it configures to use the SSO credentials. This provides people with a seamless enrollment and sign-in process that results in a Platform SSO-enabled managed device. For more information, see [Implementing Platform SSO during Automated Device Enrollment](/documentation/DeviceManagement/implementing-platform-sso-during-automated-device-enrollment).

In the second case, a device management service uses Platform SSO to perform an unattended enrollment that doesn’t require an administrator or user to manually click through Setup Assistant. When a user logs in to the device, the device uses the configured Platform SSO to sign them in. For more information, see [Implementing Platform SSO for unattended device enrollment](/documentation/DeviceManagement/implementing-platform-sso-for-unattended-device-enrollment).

Only macOS 26 devices that are registered for Automated Device Enrollment support these two Platform SSO flows.

## Topics

### Detailed flow instructions

[Implementing Platform SSO during Automated Device Enrollment](/documentation/DeviceManagement/implementing-platform-sso-during-automated-device-enrollment)

Streamline authentication during Automated Device Enrollment with Platform SSO.

[Implementing Platform SSO for unattended device enrollment](/documentation/DeviceManagement/implementing-platform-sso-for-unattended-device-enrollment)

Configure and enroll unattended devices with Platform SSO.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
