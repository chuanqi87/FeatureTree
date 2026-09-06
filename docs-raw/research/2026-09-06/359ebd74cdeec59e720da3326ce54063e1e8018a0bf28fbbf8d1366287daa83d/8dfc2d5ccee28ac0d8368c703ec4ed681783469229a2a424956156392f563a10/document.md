# AdSupport

Provide apps with access to an advertising identifier.

## Overview

Use the AdSupport framework to obtain an advertising identifier. The [`advertisingIdentifier`](/documentation/AdSupport/ASIdentifierManager/advertisingIdentifier)
is an alphanumeric string that’s unique to each device, and which you only use for
advertising. On devices running iOS 14.5 and later and iPadOS 14.5 and later, your
app must support <doc://com.apple.documentation/documentation/AppTrackingTransparency> and define the purpose string <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSUserTrackingUsageDescription>
before it can get the [`advertisingIdentifier`](/documentation/AdSupport/ASIdentifierManager/advertisingIdentifier) property.

### Get an Advertising Identifier

Before requesting the advertising identifier for the first time, your app must make
a one-time call to <doc://com.apple.documentation/documentation/AppTrackingTransparency/ATTrackingManager/requestTrackingAuthorization(completionHandler:)>.
That method presents the app-tracking authorization request to the user. The user
chooses whether to allow tracking, but can change your app’s authorization at any
time in Settings > Privacy > Tracking. You can determine the user’s intent
by checking your app’s authorization status with <doc://com.apple.documentation/documentation/AppTrackingTransparency/ATTrackingManager/trackingAuthorizationStatus>.

To get the advertising identifier, follow these steps:

1. Use the AdSupport framework to call the [`shared()`](/documentation/AdSupport/ASIdentifierManager/shared())
   class method to retrieve an instance of [`ASIdentifierManager`](/documentation/AdSupport/ASIdentifierManager).
2. Use the [`advertisingIdentifier`](/documentation/AdSupport/ASIdentifierManager/advertisingIdentifier) property to obtain
   the UUID.

The code below shows how to retrieve the advertising identifier.

```swift
import AdSupport

let sharedASIdentifierManager = ASIdentifierManager.shared()
var adID = sharedASIdentifierManager.advertisingIdentifier
```

The advertising identifier returns either a unique UUID, or all zeros. For more information
on the returned value, see [`advertisingIdentifier`](/documentation/AdSupport/ASIdentifierManager/advertisingIdentifier).

For more information about asking users for permission to track, see 
[User Privacy
and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/).

## Topics

### Essentials

[`ASIdentifierManager`](/documentation/AdSupport/ASIdentifierManager)

The object that contains the advertising identifier.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
