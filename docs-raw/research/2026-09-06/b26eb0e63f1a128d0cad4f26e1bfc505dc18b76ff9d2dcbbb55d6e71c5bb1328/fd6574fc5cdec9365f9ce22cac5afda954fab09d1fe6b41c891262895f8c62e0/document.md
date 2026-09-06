# HomeKit

Configure, control, and communicate with home automation accessories.

## Overview

HomeKit enables your app to coordinate and control home automation accessories from multiple vendors to present a coherent, user-focused interface.

![The diagram depicts a stylized phone emitting waves to indicate communication with a house pictured as a central icon. Four icons are arranged in a semi-circle to the right of the house icon, depicting connected accessories including a garage door, a thermometer, a sliding light switch, and a lamp.](images/com.apple.homekit/media-3111422@2x.png)

Using HomeKit, your app can:

- Discover HomeKit-compatible automation accessories and add them to a persistent, cross-device home configuration database.
- Display, edit, and act upon the data in the home configuration database.
- Communicate with configured accessories and services in order to perform actions like turning on the lights in the living room.

## Topics

### Essentials

[Enabling HomeKit in your app](/documentation/HomeKit/enabling-homekit-in-your-app)

Declare your app’s intention to use HomeKit, and get permission from the user to access home automation accessories.

  <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.homekit>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSHomeKitUsageDescription>

### Home Manager

[Configuring a home automation device](/documentation/HomeKit/configuring-a-home-automation-device)

Give users a familiar experience when they manage HomeKit accessories.

[Testing your app with the HomeKit Accessory Simulator](/documentation/HomeKit/testing-your-app-with-the-homekit-accessory-simulator)

Install the HomeKit Accessory Simulator to help you debug your HomeKit-enabled app.

[`HMHomeManager`](/documentation/HomeKit/HMHomeManager)

The manager for a collection of one or more of a user’s homes.

### Accessories

[`HMAccessorySetupManager`](/documentation/HomeKit/HMAccessorySetupManager)

An object that setups up new accessories.

[`HMAccessorySetupResult`](/documentation/HomeKit/HMAccessorySetupResult)

A result object describing information about a successful accessory setup request.

[`HMAccessorySetupRequest`](/documentation/HomeKit/HMAccessorySetupRequest)

An object that describes how to add and setup up new accessories.

[Interacting with a home automation network](/documentation/HomeKit/interacting-with-a-home-automation-network)

Find all the automation accessories in the primary home and control their state.

[`HMAccessory`](/documentation/HomeKit/HMAccessory)

A home automation accessory, like a garage door opener or a thermostat.

[`HMService`](/documentation/HomeKit/HMService)

A controllable feature of an accessory, like a light attached to a garage door opener.

[`HMCharacteristic`](/documentation/HomeKit/HMCharacteristic)

A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.

[`HMMediaSourceDisplayOrderProfile`](/documentation/HomeKit/HMMediaSourceDisplayOrderProfile)

An interface from which to read and, if allowed by the accessory, update the ordering of input sources.

### Action Sets

[`HMActionSet`](/documentation/HomeKit/HMActionSet)

A collection of actions that you trigger as a group.

[`HMTimerTrigger`](/documentation/HomeKit/HMTimerTrigger)

A trigger to activate an action set based on a periodic timer.

[`HMEventTrigger`](/documentation/HomeKit/HMEventTrigger)

A trigger to activate an action set based on a set of events and optional conditions.

### Errors

[`HMError`](/documentation/HomeKit/HMError)

An error HomeKit returns.

[`HMErrorDomain`](/documentation/HomeKit/HMErrorDomain)

A string that identifies the HomeKit error domain.

[`Code`](/documentation/HomeKit/HMError/Code)

Possible error values that can be returned from HomeKit APIs.

[`HMErrorBlock`](/documentation/HomeKit/HMErrorBlock)

A completion block that provides an error.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
