# Responding to power notifications

Adopt more power-efficient strategies to prolong the device’s battery life.

## Overview

Certain situations cause a device to reduce the amount of work it does and the amount of power it uses.
People who want to increase the time before their device needs charging can turn on Low Power Mode.
When a device is in Low Power Mode, the system enacts energy-saving measures, including reducing animations, and increasing the time between certain power-consuming actions like fetching data over the network.

Additionally, if the system detects that the temperature is too high, it reduces the amount of power it uses until the temperature decreases.

Register for system notifications about power- and thermal-state changes so you can take steps to help the system conserve energy and reduce its temperature.

### Detect and react to power-state notifications

In your app, register for <doc://com.apple.documentation/documentation/Foundation/NSNotification/Name-swift.struct/NSProcessInfoPowerStateDidChange> to discover when the device’s power state changes.
When you receive the notification, query the value of <doc://com.apple.documentation/documentation/Foundation/ProcessInfo/isLowPowerModeEnabled> to determine if the system’s in Low Power Mode.

If Low Power Mode is active, take additional steps to help the system conserve energy, including:

- Pausing any optional activities
- Reducing display updates
- Minimizing animations
- Reducing the frequency of network connections
- Stopping location updates

### Detect and react to thermal-state notifications

In your app, register for <doc://com.apple.documentation/documentation/Foundation/ProcessInfo/thermalStateDidChangeNotification> to discover when the device’s thermal state changes.
When you receive the notification, adjust your app’s behavior according to the value of <doc://com.apple.documentation/documentation/Foundation/ProcessInfo/thermalState-swift.property>:

- <doc://com.apple.documentation/documentation/Foundation/ProcessInfo/ThermalState-swift.enum/nominal>: Enable all of your app’s functionality.
- <doc://com.apple.documentation/documentation/Foundation/ProcessInfo/ThermalState-swift.enum/fair>: Defer work for which a person doesn’t immediately need the results; for example, background video processing.
- <doc://com.apple.documentation/documentation/Foundation/ProcessInfo/ThermalState-swift.enum/serious>: Reduce networking and location activity, screen updates, and animations.
- <doc://com.apple.documentation/documentation/Foundation/ProcessInfo/ThermalState-swift.enum/critical>: To prevent the device becoming hotter and potentially unusable, reduce or stop all work that your app is doing. Minimize computation, and stop or significantly reduce use of the camera, Bluetooth, location, and other power-intensive subsystems.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
