# Screen Time Technology Frameworks

Empower users to manage their device settings and usage while maintaining user privacy.

## Overview

The Screen Time suite of frameworks includes Family Controls, Managed Settings, and Device Activity.
You can use these frameworks to perform Screen Time-related functions in your app.

For information related to sharing and managing web-usage data, see
<doc://com.apple.documentation/documentation/ScreenTime>.

![An image consisting of three framework icons. On the left is an icon that represents Managed Settings. In the center is an icon that represents Device Activity and on the right is an icon that represents Family Controls.](images/com.apple.ScreenTime-API/ScreenTime-Technology-Frameworks@2x.png)

With Managed Settings, guardians can use your app to perform actions like locking accounts, filtering web traffic, and restricting media access.
Because a child might never have a reason to open your app on their device, you can use the Device Activity framework to execute your code on their device without launching your app.
Device Activity also enables your app to create schedules and events that your app extension can monitor.
To implement privacy protections, the Family Controls framework requires guardian approval to authorize your app with Family Sharing.
Requiring guardian approval through Family Sharing protects the user from unauthorized access of their information outside of a single Family Sharing group.

## Topics

### Essentials

  <doc://com.apple.documentation/documentation/ManagedSettings/ConnectionWithFrameworks>

### Family Controls

  <doc://com.apple.documentation/documentation/FamilyControls>

  <doc://com.apple.documentation/documentation/Xcode/configuring-family-controls>

  <doc://com.apple.documentation/documentation/FamilyControls/requesting-the-family-controls-entitlement>

### Managed Settings

  <doc://com.apple.documentation/documentation/ManagedSettings>

  <doc://com.apple.documentation/documentation/ManagedSettingsUI>

### Device Activity

  <doc://com.apple.documentation/documentation/DeviceActivity>



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
