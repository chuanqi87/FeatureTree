# App services

Configure services provided by the app, like support for giving directions or using game controllers.

## Discussion

Add keys to your app’s [`Information Property List`](/documentation/BundleResources/Information-Property-List) file that tell the system about services that your app provides.

## Topics

### Accessibility

[`MusicHapticsSupported`](/documentation/BundleResources/Information-Property-List/MusicHapticsSupported)

A Boolean value that indicates to the system that your app supports the Music Haptics feature.

### Accessories

[`NSAccessorySetupSupports`](/documentation/BundleResources/Information-Property-List/NSAccessorySetupSupports)

An array of strings that indicates the wireless technologies AccessorySetupKit uses when discovering and configuring accessories.

[`NSAccessorySetupBluetoothCompanyIdentifiers`](/documentation/BundleResources/Information-Property-List/NSAccessorySetupBluetoothCompanyIdentifiers)

An array of strings that represent the Bluetooth company identifiers for accessories that your app configures.

[`NSAccessorySetupBluetoothNames`](/documentation/BundleResources/Information-Property-List/NSAccessorySetupBluetoothNames)

An array of strings that represent the Bluetooth device names or substrings for accessories that your app configures.

[`NSAccessorySetupBluetoothServices`](/documentation/BundleResources/Information-Property-List/NSAccessorySetupBluetoothServices)

An array of strings that represent the hexadecimal values of Bluetooth SIG-defined services or custom services for accessories your app configures.

### Ad attributions

[`AdNetworkIdentifiers`](/documentation/BundleResources/Information-Property-List/AdNetworkIdentifiers)

An array of strings that identifies the ad networks a publisher app shows advertisements for.

[`AttributionCopyEndpoint`](/documentation/BundleResources/Information-Property-List/AttributionCopyEndpoint)

A key that defines a URL that AdAttributionKit uses to deliver copies of ad attribution postbacks.

[`EligibleForAdAttributionKitReengagementPostbackCopies`](/documentation/BundleResources/Information-Property-List/EligibleForAdAttributionKitReengagementPostbackCopies)

A Boolean value that indicates whether the developer receives copies of AdAttributionKit reengagement postbacks.

### AlarmKit

[`NSAlarmKitUsageDescription`](/documentation/BundleResources/Information-Property-List/NSAlarmKitUsageDescription)

A message that tells people why the app is requesting access to schedule alarms.

### Alterantive app marketplaces

[`MKSellsDigitalGoods`](/documentation/BundleResources/Information-Property-List/MKSellsDigitalGoods)

A Boolean value that indicates whether an alternative distribution app sells digital goods or services.

### Alternative browser engines

[`BEEmbeddedWebBrowserEngine`](/documentation/BundleResources/Information-Property-List/BEEmbeddedWebBrowserEngine)

A string name of the alternative browser engine that your app embeds.

[`BEEmbeddedWebBrowserEngineVersion`](/documentation/BundleResources/Information-Property-List/BEEmbeddedWebBrowserEngineVersion)

A string version number for the alternative browser engine that your app embeds.

### Always On display

[`WKSupportsAlwaysOnDisplay`](/documentation/BundleResources/Information-Property-List/WKSupportsAlwaysOnDisplay)

A Boolean value that determines whether the system displays the app in the Always On state.

### Authentication

[`ASAccountAuthenticationModificationOptOutOfSecurityPromptsOnSignIn`](/documentation/BundleResources/Information-Property-List/ASAccountAuthenticationModificationOptOutOfSecurityPromptsOnSignIn)

A Boolean value that indicates the system shouldn’t show security recommendation prompts when users sign in using the app.

[`ASWebAuthenticationSessionWebBrowserSupportCapabilities`](/documentation/BundleResources/Information-Property-List/ASWebAuthenticationSessionWebBrowserSupportCapabilities)

A collection of keys that a browser app uses to declare its ability to handle authentication requests from other apps.

### CallKit

[`NSVoIPUsageDescription`](/documentation/BundleResources/Information-Property-List/NSVoIPUsageDescription)

A message that tells people why your app receives voice-over-IP (VoIP) calls in the background.

### Core spotlight

[`CoreSpotlightActions`](/documentation/BundleResources/Information-Property-List/CoreSpotlightActions)

A dictionary that contains details about actions available to users for Spotlight search results.

### Exposure notification

[`ENAPIVersion`](/documentation/BundleResources/Information-Property-List/ENAPIVersion)

A number that specifies the version of the API to use.

[`ENDeveloperRegion`](/documentation/BundleResources/Information-Property-List/ENDeveloperRegion)

A string that specifies the region that the app supports.

### External accessories

[`UIApplicationSupportsPrintCommand`](/documentation/BundleResources/Information-Property-List/UIApplicationSupportsPrintCommand)

A Boolean value that indicates whether the app supports the Command-P keyboard shortcut.

[`UISupportedExternalAccessoryProtocols`](/documentation/BundleResources/Information-Property-List/UISupportedExternalAccessoryProtocols)

The protocols that the app uses to communicate with external accessory hardware.

### Games

[`AVGameBypassSystemSpatialAudio`](/documentation/BundleResources/Information-Property-List/AVGameBypassSystemSpatialAudio)

A key that ignores the system spatial-audio toggle in Control Center.

[`GKGameCenterBadgingDisabled`](/documentation/BundleResources/Information-Property-List/GKGameCenterBadgingDisabled)

A Boolean value indicating whether GameKit can add badges to a turn-based game icon.

[`GCDisableInferringGameMetadata`](/documentation/BundleResources/Information-Property-List/GCDisableInferringGameMetadata)

A Boolean value that indicates whether the Games app excludes game information
for non-App Store games.

[`GCSupportedGameControllers`](/documentation/BundleResources/Information-Property-List/GCSupportedGameControllers)

The types of game controller profiles that the app supports or requires.

[`GCSupportsControllerUserInteraction`](/documentation/BundleResources/Information-Property-List/GCSupportsControllerUserInteraction)

A Boolean value indicating whether the app supports a game controller.

[`GCRequiresControllerUserInteraction`](/documentation/BundleResources/Information-Property-List/GCRequiresControllerUserInteraction)

The platforms for which your app requires or you recommend a game controller.

[`GCSupportsMultipleMicroGamepads`](/documentation/BundleResources/Information-Property-List/GCSupportsMultipleMicroGamepads)

A Boolean value indicating whether the physical Apple TV Remote and the Apple TV Remote app operate as separate game controllers.

[`LSSupportsGameMode`](/documentation/BundleResources/Information-Property-List/LSSupportsGameMode)

A Boolean value indicating whether the app supports Game Mode.

[`GCSupportsGameMode`](/documentation/BundleResources/Information-Property-List/GCSupportsGameMode)

A Boolean value indicating whether the app supports game mode.

[`GKShowChallengeBanners`](/documentation/BundleResources/Information-Property-List/GKShowChallengeBanners)

A Boolean value that indicates whether GameKit can display challenge banners in a game.

### Intents

[`INIntentsSupported`](/documentation/BundleResources/Information-Property-List/INIntentsSupported)

The names of the intent classes your app handles directly.

[`INIntentsRestrictedWhileLocked`](/documentation/BundleResources/Information-Property-List/INIntentsRestrictedWhileLocked)

The names of the intent classes your app can’t handle when the user locks the device.

[`INIntentsRestrictedWhileProtectedDataUnavailable`](/documentation/BundleResources/Information-Property-List/INIntentsRestrictedWhileProtectedDataUnavailable)

The names of the intent classes your app can’t handle when the user locks the device or the system blocks access to protected data.

[`INSupportedMediaCategories`](/documentation/BundleResources/Information-Property-List/INSupportedMediaCategories)

Types of media supported by your app’s media-playing intents.

[`NSFocusStatusUsageDescription`](/documentation/BundleResources/Information-Property-List/NSFocusStatusUsageDescription)

A message that tells people why your app requests access to a person’s focus status.

### Interprocess communication

[`XPCService`](/documentation/BundleResources/Information-Property-List/XPCService)

### Live Activities

[`NSSupportsLiveActivities`](/documentation/BundleResources/Information-Property-List/NSSupportsLiveActivities)

A Boolean value that indicates whether an app supports Live Activities.

[`NSSupportsLiveActivitiesFrequentUpdates`](/documentation/BundleResources/Information-Property-List/NSSupportsLiveActivitiesFrequentUpdates)

A Boolean value that indicates whether an app can update its Live Activities frequently.

### Maps

[`MKDirectionsApplicationSupportedModes`](/documentation/BundleResources/Information-Property-List/MKDirectionsApplicationSupportedModes)

The modes of transportation for which the app is capable of giving directions.

### Messages

[`NSStickerSharingLevel`](/documentation/BundleResources/Information-Property-List/NSStickerSharingLevel)

[`NSCriticalMessagingUsageDescription`](/documentation/BundleResources/Information-Property-List/NSCriticalMessagingUsageDescription)

A message that tells people why the app needs to send SMS messages.

### Network

[`NSApplicationServices`](/documentation/BundleResources/Information-Property-List/NSApplicationServices)

A list of service providers and the devices that they support.

### Journaling Suggestions

[`JSNotificationURLFormat`](/documentation/BundleResources/Information-Property-List/JSNotificationURLFormat)

A universal link that determines how the system provides Journaling Suggestion notifications to your app.

### Safari services

[`SFSafariCorrespondingIOSAppBundleIdentifier`](/documentation/BundleResources/Information-Property-List/SFSafariCorrespondingIOSAppBundleIdentifier)

A string bundle ID that identifies the corresponding iOS app that contains a content blocker or Safari web extension.

[`SFSafariCorrespondingIOSExtensionBundleIdentifier`](/documentation/BundleResources/Information-Property-List/SFSafariCorrespondingIOSExtensionBundleIdentifier)

A string bundle ID that identifies the corresponding content blocker extension or Safari web extension on iOS.

[`SFSafariCorrespondingMacOSAppBundleIdentifier`](/documentation/BundleResources/Information-Property-List/SFSafariCorrespondingMacOSAppBundleIdentifier)

A string bundle ID that identifies the corresponding macOS app that contains a content blocker or Safari web extension.

[`SFSafariCorrespondingMacOSExtensionBundleIdentifier`](/documentation/BundleResources/Information-Property-List/SFSafariCorrespondingMacOSExtensionBundleIdentifier)

A string bundle ID that identifies the corresponding content blocker extension or Safari web extension on macOS.

### Sensors

[`SRResearchDataGeneration`](/documentation/BundleResources/Information-Property-List/SRResearchDataGeneration)

A Boolean value that indicates whether use of an app contributes data to SensorKit while the user is enrolled in a health research study.

### Service management

[`SMAuthorizedClients`](/documentation/BundleResources/Information-Property-List/SMAuthorizedClients)

The Service Management clients authorized to add and remove tools.

[`SMPrivilegedExecutables`](/documentation/BundleResources/Information-Property-List/SMPrivilegedExecutables)

The Service Management tools owned by the app.

### StoreKit

[`SKAdNetworkItems`](/documentation/BundleResources/Information-Property-List/SKAdNetworkItems)

An array of dictionaries containing a list of ad network IDs.

[`SKExternalLinkAccount`](/documentation/BundleResources/Information-Property-List/SKExternalLinkAccount)

A dictionary that contains localized URLs to an external website for account creation or management.

[`SKExternalPurchase`](/documentation/BundleResources/Information-Property-List/SKExternalPurchase)

A string array of country codes that indicates your app supports external purchases.

[`SKExternalPurchaseCustomLinkRegions`](/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions)

An array of country code strings that indicate the regions where your app supports custom links for the communication and promotion of offers.

[`SKExternalPurchaseLink`](/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLink)

A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.

[`SKExternalPurchaseMultiLink`](/documentation/BundleResources/Information-Property-List/SKExternalPurchaseMultiLink)

A dictionary that contains an array of URLs to websites where people using your app can make external purchases.

[`SKIncludeConsumableInAppPurchaseHistory`](/documentation/BundleResources/Information-Property-List/SKIncludeConsumableInAppPurchaseHistory)

A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.

[`SKExternalPurchaseLinkStreamingRegions`](/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLinkStreamingRegions)

A list of country codes that indicate the regions where your music-streaming app communicates and promotes offers.

### User activities

[`NSUserActivityTypes`](/documentation/BundleResources/Information-Property-List/NSUserActivityTypes)

The user activity types that the app supports.

### Wi-Fi Aware

[`WiFiAwareServices`](/documentation/BundleResources/Information-Property-List/WiFiAwareServices)

Dictionaries of Wi-Fi Aware services that the app can publish or subscribe to.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
