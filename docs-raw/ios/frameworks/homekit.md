* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/homekit#app-main)

Framework

# HomeKit

Configure, control, and communicate with home automation accessories.

iOS 8.0+iPadOS 8.0+Mac Catalyst 14.0+tvOS 10.0+visionOS 1.0+watchOS 2.0+

## [Overview](https://developer.apple.com/documentation/homekit\#overview)

HomeKit enables your app to coordinate and control home automation accessories from multiple vendors to present a coherent, user-focused interface.

![The diagram depicts a stylized phone emitting waves to indicate communication with a house pictured as a central icon. Four icons are arranged in a semi-circle to the right of the house icon, depicting connected accessories including a garage door, a thermometer, a sliding light switch, and a lamp.](https://developer.apple.com/tutorials/images/com.apple.homekit/media-3111422@2x.png)

Using HomeKit, your app can:

- Discover HomeKit-compatible automation accessories and add them to a persistent, cross-device home configuration database.

- Display, edit, and act upon the data in the home configuration database.

- Communicate with configured accessories and services in order to perform actions like turning on the lights in the living room.


## [Topics](https://developer.apple.com/documentation/homekit\#topics)

### [Essentials](https://developer.apple.com/documentation/homekit\#Essentials)

[Enabling HomeKit in your app](https://developer.apple.com/documentation/homekit/enabling-homekit-in-your-app)

Declare your app’s intention to use HomeKit, and get permission from the user to access home automation accessories.

[`HomeKit Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.homekit)

A Boolean value that indicates whether users of the app may manage HomeKit-compatible accessories.

[`NSHomeKitUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nshomekitusagedescription)

A message that tells people why the app is requesting access to their HomeKit configuration data.

### [Home Manager](https://developer.apple.com/documentation/homekit\#Home-Manager)

[Configuring a home automation device](https://developer.apple.com/documentation/homekit/configuring-a-home-automation-device)

Give users a familiar experience when they manage HomeKit accessories.

[Testing your app with the HomeKit Accessory Simulator](https://developer.apple.com/documentation/homekit/testing-your-app-with-the-homekit-accessory-simulator)

Install the HomeKit Accessory Simulator to help you debug your HomeKit-enabled app.

[`class HMHomeManager`](https://developer.apple.com/documentation/homekit/hmhomemanager)

The manager for a collection of one or more of a user’s homes.

### [Accessories](https://developer.apple.com/documentation/homekit\#Accessories)

[`class HMAccessorySetupManager`](https://developer.apple.com/documentation/homekit/hmaccessorysetupmanager)

An object that setups up new accessories.

[`class HMAccessorySetupResult`](https://developer.apple.com/documentation/homekit/hmaccessorysetupresult)

A result object describing information about a successful accessory setup request.

[`class HMAccessorySetupRequest`](https://developer.apple.com/documentation/homekit/hmaccessorysetuprequest)

An object that describes how to add and setup up new accessories.

[Interacting with a home automation network](https://developer.apple.com/documentation/homekit/interacting-with-a-home-automation-network)

Find all the automation accessories in the primary home and control their state.

[`class HMAccessory`](https://developer.apple.com/documentation/homekit/hmaccessory)

A home automation accessory, like a garage door opener or a thermostat.

[`class HMService`](https://developer.apple.com/documentation/homekit/hmservice)

A controllable feature of an accessory, like a light attached to a garage door opener.

[`class HMCharacteristic`](https://developer.apple.com/documentation/homekit/hmcharacteristic)

A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.

[`class HMMediaSourceDisplayOrderProfile`](https://developer.apple.com/documentation/homekit/hmmediasourcedisplayorderprofile)

An interface from which to read and, if allowed by the accessory, update the ordering of input sources.

### [Action Sets](https://developer.apple.com/documentation/homekit\#Action-Sets)

[`class HMActionSet`](https://developer.apple.com/documentation/homekit/hmactionset)

A collection of actions that you trigger as a group.

[`class HMTimerTrigger`](https://developer.apple.com/documentation/homekit/hmtimertrigger)

A trigger to activate an action set based on a periodic timer.

[`class HMEventTrigger`](https://developer.apple.com/documentation/homekit/hmeventtrigger)

A trigger to activate an action set based on a set of events and optional conditions.

### [Errors](https://developer.apple.com/documentation/homekit\#Errors)

[`struct HMError`](https://developer.apple.com/documentation/homekit/hmerror)

An error HomeKit returns.

[`let HMErrorDomain: String`](https://developer.apple.com/documentation/homekit/hmerrordomain)

A string that identifies the HomeKit error domain.

[`enum Code`](https://developer.apple.com/documentation/homekit/hmerror/code)

Possible error values that can be returned from HomeKit APIs.

[`typealias HMErrorBlock`](https://developer.apple.com/documentation/homekit/hmerrorblock)

A completion block that provides an error.

### [Classes](https://developer.apple.com/documentation/homekit\#Classes)

[`class HMAccessorySetupPayload`](https://developer.apple.com/documentation/homekit/hmaccessorysetuppayload)

A payload for authenticating a HomeKit accessory.

Current page is HomeKit