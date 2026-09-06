# Bundle Resources updates

Learn about important changes to Bundle Resources.

## Overview

Browse notable changes in <doc://com.apple.documentation/documentation/BundleResources>.

## June 2026

### New entitlements

- Access Private Cloud Compute in your <doc://com.apple.documentation/documentation/FoundationModels> app using the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.private-cloud-compute> entitlement.
- Request insights relating to transactional activities using the <doc://com.apple.documentation/documentation/TrustInsights> framework with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.trustinsights.base> entitlement.
- Display energy device names and usage statistics in the Home app using the <doc://com.apple.documentation/documentation/EnergyKit> framework with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.energykit.loadevents-experience> entitlement.
- Add suggested actions to your messaging app based on message content with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.suggested-actions> entitlement and the <doc://com.apple.documentation/documentation/SuggestedActions> framework.
- Integrate a third-party media sharing protocol into the system route picker with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.media-device-extension> entitlement.
- Manage access to connected USB devices for macOS and Linux virtual machines with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.accessory-access.usb> entitlement.
- Protect your app against use-after-free vulnerabilities with guard objects, which the system enables automatically when you set <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.enhanced-security-version> to version `2` or greater. To turn off guard objects if they impact performance, use the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.no-guard-objects> entitlement.

### New information property list keys

- Declare the media device extension protocols your app supports with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/MDESupportedProtocols>.
- Indicate that your app supports URL-based playback through a media device extension with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/MDESupportsUniversalURLPlayback>.
- Control whether only one view’s gesture recognizers can be active at a time with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSViewGestureRecognizerIsExclusive>.
- Declare that your app handles touch input natively, without relying on AppKit’s extra mouse emulation, with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSIsTouchNative>.
- Suppress keyboard shortcuts for menu items while any non-exclusive gesture recognizer is active with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSGestureRecognizerSuppressesMainMenuActions>.

### Updated entitlements

- Define the app category to enable Cellular Network Slicing with <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.networking.slicing.appcategory>. To set the application category for web browser apps, use `browser-9003`. You can also set the category to `mc-9500` for mission-critical apps that need access to ultra-constrained cellular networks.
- Define the app category for carrier-constrained satellite network access with <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.networking.carrier-constrained.appcategory>. To set the application category for payment apps, use `payment-8015`. You can also set the category to `health-fitness-8014` for health and fitness apps.

## June 2025

### New entitlements

- Include passthrough in screen capture on visionOS with the  <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.screen-capture.include-passthrough> entitlement.
- Enable low-latency wireless networking for streaming game content on visionOS with the  <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.low-latency-streaming> entitlement.
- Manage home device electricity usage with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.energykit> entitlement.
- Access the GPU from a background task with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.background-tasks.continued-processing.gpu> entitlement.
- Opt in to additional security checks with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.security.hardened-process> entitlement.
- Enable security hardening protections with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.enhanced-security-version> entitlement.
- Mark memory the system uses for internal platform state as read only with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.dyld-ro> entitlement.
- Protect memory you use for pointers by opting in to type-aware memory allocation with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.hardened-heap> entitlement.
- Opt in to additional platform restrictions with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.platform-restrictions> entitlement.
- Access subscribable or publishable Wi-Fi Aware services with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.wifi-aware> entitlement.
- Indicate that your app is optimized for a carrier-constrained network with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.networking.carrier-constrained.app-optimized> entitlement.
- Define the category in which your app accesses a carrier-constrained network with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.networking.carrier-constrained.appcategory> entitlement.
- Report the types of identity documents your app provides with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.identity-document-services.document-provider.mobile-document-types> entitlement.
- Indicate that your app can be the default dialer app on someone’s device with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.dialing-app> entitlement.
- Obtain wireless service predictions with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.wireless-insights.service-predictions> entitlement.
- Indicate that your app can be the default carrier messaging app on someone’s device with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.carrier-messaging-app> entitlement.
- Access the camera region in your visionOS app with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.arkit.camera-region.allow> entitlement.
- Share a coordinate space with other devices with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.arkit.shared-coordinate-space.allow> entitlement.
- Stop the system from capturing your app’s content with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.protected-content> entitlement.
- Lock your app’s windows in place relative to a person with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.window-body-follow> entitlement.
- Indicate that your app can be the default dialer app on someone’s device with the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.dialing-app> entitlement.

### New information property list keys

- Describe why your app tracks an accessory’s position and location with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSAccessoryTrackingUsageDescription>.
- Indicate that the system should automatically download your asset packs and keep them up to date with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/BAHasManagedAssetPacks>.
- Use Apple’s service to host your asset packs with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/BAUsesAppleHosting>.
- Identify the app group that your app and extension use to share asset packs with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/BAAppGroupID>.
- Describe Wi-Fi Aware services your app publishes and subscribes to with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/WiFiAwareServices>.
- Indicate that your app supports game mode with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/LSSupportsGameMode>.

### Updated entitlements

- Add the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.kernel.increased-memory-limit> entitlement to your visionOS app.

### Updated information property list keys

- Indicate that your visionOS app supports spatial gamepads with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/GCSupportedGameControllers>.

## June 2024

### New entitlements

- Enable access to a Personalized Sound Profile to allow the app to use the information in the profile to render audio with <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.spatial-audio.profile-access>.
- Enable access to head tracking info to allow an app to render audio with head tracking with <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.coremotion.head-pose>.
- Allow CoreMIDI to match MIDIDriverKit drivers with devices that support MIDI with <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.midi>.

### Updated entitlement

- Define the app category to enable Cellular Network Slicing with <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.networking.slicing.appcategory>. To set the application category for streaming apps, use `streaming-9001`. You can also set the category to `gaming-6014` for gaming apps, and `communication-9000` for communication apps.

### New Info.plist keys

- Indicate if the game app bypasses system spatial audio with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/AVGameBypassSystemSpatialAudio>.
- Indicate to the system that your app receives copies of re-engagement postbacks, a type of postback introduced in iOS 17.5, with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/EligibleForAdAttributionKitReengagementPostbackCopies>.
- Indicate to the system that your app supports the Music Haptics feature with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/MusicHapticsSupported>.
- Indicate to the system the interfaces AccessorySetupKit uses to discover and configure accessories using Bluetooth or Wi-Fi with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSAccessorySetupSupports>.
- Provide the company identifier for a Bluetooth accessory when enabling the use of AccessorySetupKit via `NSAccessorySetupKitEnabled` with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSAccessorySetupBluetoothCompanyIdentifiers>.
- Provide the name for a Bluetooth accessory when enabling the use of AccessorySetupKit via `NSAccessorySetupKitEnabled` with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSAccessorySetupBluetoothNames>.
- Provide the services for a Bluetooth accessory when enabling the use of AccessorySetupKit via `NSAccessorySetupKitEnabled` with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSAccessorySetupBluetoothServices>.
- Provide a message that tells the user why the app requests access to financial data stored in Wallet with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSFinancialDataUsageDescription>.
- Track “finished” consumable in-app purchases in StoreKit and return the transactions when iterating the `Transaction` APIs with <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/SKIncludeConsumableInAppPurchaseHistory>.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
