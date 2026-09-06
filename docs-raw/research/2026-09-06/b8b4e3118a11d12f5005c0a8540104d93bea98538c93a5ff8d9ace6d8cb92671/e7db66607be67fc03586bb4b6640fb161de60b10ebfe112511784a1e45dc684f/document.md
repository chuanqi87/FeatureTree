# Core Telephony

Access information about a user’s cellular service provider, such as its unique identifier and whether the carrier allows VoIP.

## Overview

Use the Core Telephony framework to obtain information about a user’s home cellular service provider. Carriers can use this information to write apps that provide services only for their own subscribers. You can also use this framework to obtain information about current cellular calls.

A [`CTCarrier`](/documentation/CoreTelephony/CTCarrier) object gives you information about the user’s cellular service provider, such as whether it allows use of VoIP (Voice over Internet Protocol) on its network. A [`CTCall`](/documentation/CoreTelephony/CTCall) object gives you information about a current call, including a unique identifier and state information such as dialing, incoming, connected, or disconnected.

> Note:
> VoIP and cellular services through Core Telephony are unavailable for compatible iPad and iPhone apps running in visionOS. You can still use the APIs of this framework, but services don’t return carrier information.

## Topics

### Service information

[`CTTelephonyNetworkInfo`](/documentation/CoreTelephony/CTTelephonyNetworkInfo)

An object that provides notifications of changes to the user’s cellular service provider.

[iPhone quick switch](/documentation/CoreTelephony/iphone-quick-switch)

Enable seamless app transition between multiple iPhones.

### eSIM

Carrier apps use the classes in this group to provision cellular plan eSIMs on supported devices.

[`CTCellularPlanProvisioning`](/documentation/CoreTelephony/CTCellularPlanProvisioning)

An object you use to download and install a carrier eSIM.

[`CTCellularPlanProvisioningRequest`](/documentation/CoreTelephony/CTCellularPlanProvisioningRequest)

A request specifying an eSIM to download and install.

[`CTCellularPlanProperties`](/documentation/CoreTelephony/CTCellularPlanProperties)

An object you use for an eSIM.

[`CTCellularPlanCapability`](/documentation/CoreTelephony/CTCellularPlanCapability)

The type of cellular plan available for an eSIM.

### SIM

Check the presence of a SIM based on authentication.

[`CTCellularPlanStatus`](/documentation/CoreTelephony/CTCellularPlanStatus)

An object that validates tokens for UPI device verification or checks the availability of cellular plans for a phone number.

### Subscriber information

[`CTSubscriber`](/documentation/CoreTelephony/CTSubscriber)

A cellular network subscriber.

[`CTSubscriberDelegate`](/documentation/CoreTelephony/CTSubscriberDelegate)

A protocol to handle changes to subscriber information.

[`CTSubscriberInfo`](/documentation/CoreTelephony/CTSubscriberInfo)

An object that provides an array of cellular network subscribers.

### Cellular data access

[`CTCellularData`](/documentation/CoreTelephony/CTCellularData)

An object indicating whether the app can access cellular data.

### Network slicing

[`CTSlicingManager`](/documentation/CoreTelephony/CTSlicingManager)

A manager that provides network-slicing capabilities for controlling and monitoring cellular network traffic routing.

### Errors

[`CTError`](/documentation/CoreTelephony/CTError)

A type representing a Core Telephony error.

### Reference

[Core Telephony Macros](/documentation/CoreTelephony/coretelephony-macros)

### Deprecated

Getting call information in Core Telephony is no longer supported. Use <doc://com.apple.documentation/documentation/CallKit> instead.

[`CTCarrier`](/documentation/CoreTelephony/CTCarrier)

Information about the user’s cellular service provider, such as its unique identifier and whether it allows VoIP calls on its network.

[`CTCall`](/documentation/CoreTelephony/CTCall)

An object used to identify a cellular call and determine its state.

[`CTCallCenter`](/documentation/CoreTelephony/CTCallCenter)

An object that provides a list of current cellular calls, and provides the ability to respond to state changes for calls.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
