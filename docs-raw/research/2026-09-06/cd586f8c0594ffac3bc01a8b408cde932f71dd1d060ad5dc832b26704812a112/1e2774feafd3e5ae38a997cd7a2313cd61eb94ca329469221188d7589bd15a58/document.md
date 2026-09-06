# Get started with Google Analytics for iOS+

|  |  |
| --- | --- |
| **Select platform:** | [iOS+](https://firebase.google.com/docs/analytics/ios/get-started) [Android](https://firebase.google.com/docs/analytics/android/get-started) [Web](https://firebase.google.com/docs/analytics/web/get-started) [Flutter](https://firebase.google.com/docs/analytics/flutter/get-started) [Unity](https://firebase.google.com/docs/analytics/unity/get-started) [C++](https://firebase.google.com/docs/analytics/cpp/get-started) |

This quickstart shows you how to add Google Analytics to your app and begin
logging events.

Google Analytics collects usage and behavior data for your app. The SDK
logs two primary types of information:

* **Events:** What is happening in your app, such as user actions, system
  events, or errors.
* **User properties:** Attributes you define to describe segments of your
  user base, such as language preference or geographic location.

Analytics automatically logs some
[events](https://support.google.com/firebase/answer/6317485) and
[user properties](https://support.google.com/firebase/answer/6317486);
you don't need to add any code to enable them.

## Before you begin

1. If you haven't already, [add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup)
   and make sure that Google Analytics is enabled in your Firebase
   project:

   * If you're creating a new Firebase project, enable Google Analytics
     during the project creation workflow.
   * If you're using an existing Firebase project that doesn't have
     Google Analytics enabled, you can enable it in the
     settings **Settings** >
     [**Integrations** tab](https://console.firebase.google.com/project/_/settings/integrations).

   When you enable Google Analytics in your project, your Firebase apps
   are linked to Google Analytics data streams.
2. *(Recommended)*
   [Add the AdSupport framework to your project](https://firebase.google.com/docs/analytics/faq-and-troubleshooting#analytics-adsupport-framework)
   to enable additional features such as audiences and campaign attribution.

## Add the Analytics SDK to your app

Use Swift Package Manager to install and manage Firebase dependencies.

Visit [our installation guide](https://firebase.google.com/docs/ios/installation-methods)
to learn about the different ways you can add Firebase SDKs to your Apple project.

1. In Xcode, with your app project open, navigate to **File > Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:

```
  https://github.com/firebase/firebase-ios-sdk.git
```


**Note:** New projects should use the default (latest) SDK version, but you can
choose an older version if needed.
3. Choose the Analytics library.
4. Add the `-ObjC` flag to the *Other Linker Flags* section of your target's build settings.
5. For an optimal experience with Analytics, we recommend
   [enabling Google Analytics](https://support.google.com/firebase/answer/9289399#linkga)
   in your Firebase project and adding the Firebase SDK for Google Analytics to your app. You can
   select either the library without IDFA collection or with IDFA collection. See our FAQ on the
   [latest organization of modules in the Google Analytics for Firebase SDK](https://firebase.google.com/docs/analytics/faq-and-troubleshooting#analytics-odm2-sdk-refactor-ios).
6. When finished, Xcode will automatically begin resolving and downloading your
   dependencies in the background.

Learn more about IDFA, the device-level advertising identifier, in Apple's
[User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/)
and
[App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency)
documentation.

Next, perform some configuration steps:

1. Import the `FirebaseCore` module in your
   `UIApplicationDelegate`, as well as any other
   [Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods) your app delegate uses.
   For example, to use Cloud Firestore and Authentication:

   #### SwiftUI

   ```
   import SwiftUI
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
   ```

   #### Swift

   ```
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
   ```

   #### Objective-C

   ```
   @import FirebaseCore;
   @import FirebaseFirestore;
   @import FirebaseAuth;
   // ...
   ```
2. Configure a
   [`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp)
   shared instance in your app delegate's
   `application(_:didFinishLaunchingWithOptions:)` method:

   #### SwiftUI

   ```
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Swift

   ```
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Objective-C

   ```
   // Use Firebase library to configure APIs
   [FIRApp configure];
   ```
3. If you're using SwiftUI, you must create an application delegate and attach it
   to your `App` struct via `UIApplicationDelegateAdaptor` or
   `NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For
   more information, see the [SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).

   #### SwiftUI

   ```
   @main
   struct YourApp: App {
     // register app delegate for Firebase setup
     @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

     var body: some Scene {
       WindowGroup {
         NavigationView {
           ContentView()
         }
       }
     }
   }
   ```

If you're tracking in-app purchases, you must
initialize your transaction observer in `application:didFinishLaunchingWithOptions:`
before initializing Firebase, or your observer may not receive all purchase
notifications. See Apple's [In-App Purchase Best Practices](https://developer.apple.com/library/content/technotes/tn2387/_index.html) for more information.



### (Optional) Disable Apple ad network attribution registration

For your convenience, the SDK automatically
[registers](https://developer.apple.com/documentation/storekit/skadnetwork/2943654-registerappforadnetworkattributi)
your app with Apple for ad network attribution with
[SKAdNetwork](https://developer.apple.com/documentation/storekit/skadnetwork).
If you wish to disable this feature, set the value of
`GOOGLE_ANALYTICS_REGISTRATION_WITH_AD_NETWORK_ENABLED` to `NO` (Boolean) in
your app's `info.plist` file.

## Start logging events

After you have configured the `FirebaseApp` instance, you can begin to log
events with the
[`logEvent()`](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#logevent_:parameters:)
method.

Certain events are
[recommended for all apps](https://support.google.com/firebase/answer/6317498);
others are recommended for specific business types or verticals. You should send
suggested events along with their prescribed parameters, to ensure maximum
available detail in your reports and to benefit from future features and
integrations as they become available. This section demonstrates logging a
pre-defined event, for more information on
logging events, see [Log events](https://firebase.google.com/docs/analytics/ios/events).

The following example demonstrates how to log a recommended event to indicate a
user has clicked on a specific element in your app:

### Swift

```
Analytics.logEvent("share_image", parameters: [
  "name": name,
  "full_text": text,
])

MigratedSnippets.swift
```

### Objective-C

```
[FIRAnalytics logEventWithName:@"share_image"
                    parameters:@{
                                 @"name": name,
                                 @"full_text": text
                                 }];

ObjCMigratedSnippets.m
```

To view this event in the Xcode debug console, enable Analytics debugging:

1. In Xcode, select **Product > Scheme > Edit scheme...**
2. Select **Run** from the left menu.
3. Select the **Arguments** tab.
4. In the **Arguments Passed On Launch** section, add
   `-FIRAnalyticsDebugEnabled`.

## Next steps

* Understand [each Analytics report](https://firebase.google.com/docs/analytics/reports).
* Use the [DebugView](https://firebase.google.com/docs/analytics/debugview) to verify your events.
* Explore your data in the
  [Firebase console](https://console.firebase.google.com/project/_/analytics/).
* Explore the guides on [events](https://firebase.google.com/docs/analytics/ios/events) and
  [user properties.](https://firebase.google.com/docs/analytics/ios/user-properties)
* Learn how to export your data to [BigQuery.](https://support.google.com/firebase/answer/7030014)
