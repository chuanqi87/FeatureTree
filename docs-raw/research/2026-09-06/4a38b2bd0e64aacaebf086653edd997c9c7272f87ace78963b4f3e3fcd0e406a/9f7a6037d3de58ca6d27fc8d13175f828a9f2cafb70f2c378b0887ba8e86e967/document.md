# Get started with AdMob in your iOS project

This quickstart guide is for publishers and developers who want to use AdMob
to monetize an app that's built with Firebase.
If you don't plan to include Firebase in your app, visit the
[standalone AdMob
guide](https://developers.google.com/admob/ios/quick-start) instead.

If you haven't yet, learn about all the
[benefits](https://firebase.google.com/docs/admob/analytics-and-firebase) of using AdMob, Firebase,
and Google Analytics together.

## Before you begin

* If you don't already have a Firebase project and a Firebase app, follow the
  Firebase getting started guide:
  [Add Firebase to your iOS project](https://firebase.google.com/docs/ios/setup).
* Make sure that Google Analytics is enabled in your Firebase project:

  + If you're creating a new Firebase project, enable Google Analytics
    during the project creation workflow.
  + If you have an existing Firebase project that doesn't have
    Google Analytics enabled, you can enable Google Analytics from
    the
    [*Integrations*](https://console.firebase.google.com/project/_/settings/integrations)
    tab of your settings >
    *Project settings*.**Note:** Adding the Firebase SDK for Google Analytics to your app is
  optional but strongly recommended. Learn more about the [benefits of adding
  the Firebase SDK for Google Analytics](https://firebase.google.com/docs/admob/analytics-and-firebase).

## **Step 1:** Set up your app in your AdMob account

1. Register your app as an AdMob app.

   1. [Sign into](https://admob.google.com/home/) or
      [sign up](https://support.google.com/admob/answer/7356219) for an
      AdMob account.
   2. [Register your app with
      AdMob](https://support.google.com/admob/answer/2773509). This
      step creates an AdMob app with a unique [AdMob
      App ID](https://support.google.com/admob/answer/7356431)
      that you'll need later in this guide.

   You'll be asked to add the Mobile Ads SDK to your app. Find
   detailed instructions for this task later in this guide.
2. Link your AdMob app to your Firebase app.

   This step is optional but strongly recommended. Learn more about the
   [benefits](https://firebase.google.com/docs/admob/analytics-and-firebase)
   of enabling user metrics and linking your AdMob app to Firebase.

   Complete the following two steps in the *Apps* dashboard of your AdMob
   account:

   1. [Enable
      *User Metrics*](https://support.google.com/admob/answer/9263723)
      to allow AdMob to process and display curated analytics data in your
      AdMob account. It's also a required setting for you to link your
      AdMob app to Firebase.
   2. [Link your
      AdMob app](https://support.google.com/admob/answer/6383165)
      to your existing Firebase project and Firebase app.

      Make sure that you enter the same bundle ID as you entered for your
      Firebase app. Find your Firebase app's bundle ID in the *Your apps* card
      of your settings >
      [*Project settings*](https://console.firebase.google.com/project/_/settings/general).

## **Step 2:** Add your AdMob App ID to your `Info.plist` file

In your app's `Info.plist` file, add a `GADApplicationIdentifier` key with a
string value of your
[AdMob App ID](https://support.google.com/admob/answer/7356431).

**Important:** This step is required as of Google Mobile Ads SDK v7.42.0. If you
don't add this `Info.plist` entry, your app will crash with the message:
`"The Google Mobile Ads SDK was initialized incorrectly."`

You can make this change programmatically:

```
<!-- Sample AdMob App ID: ca-app-pub-3940256099942544~1458002511 -->
<key>GADApplicationIdentifier</key>
<string>ADMOB_APP_ID</string>
```

Or, edit it in the property list editor:

![Property List Editor](//developers.google.com/admob/images/ios/admob_app_id_plist.png)

## **Step 3:** Add and initialize the Mobile Ads SDK

1. Add the dependency for the Google Mobile Ads SDK to your project's
   Podfile:

   ```
   pod 'Google-Mobile-Ads-SDK'
   ```
2. Before loading ads, call the `startWithCompletionHandler:` method on the
   [`GADMobileAds.sharedInstance`](https://developers.google.com/admob/ios/api/reference/Classes/GADMobileAds#sharedinstance).

   This call initializes the SDK and calls back a completion handler once
   initialization is complete (or after a 30-second timeout). Call this method
   only once and as early as possible, ideally at app launch but after
   initializing Firebase.

   **Warning:** Ads may be preloaded by the
   Mobile Ads SDK or mediation partner SDKs upon calling
   `startWithCompletionHandler:`. If you need to take any action
   before loading ads, make sure that you do so before initializing the
   Mobile Ads SDK. Here are some examples of actions that might
   be needed prior to initialization:
   * Obtain consent from users in the European Economic Area (EEA)
   * Set any request-specific flags (such as
     `tagForChildDirectedTreatment` or
     `tag_for_under_age_of_consent`)

   Learn more in the
   [AdMob
   documentation](https://developers.google.com/admob/ios/eu-consent).

   Here's an example of how to call the `startWithCompletionHandler:` method in
   your `AppDelegate`:

   ### Swift

   ```
   import Firebase
   import GoogleMobileAds
   ...

   @UIApplicationMain
   class AppDelegate: UIResponder, UIApplicationDelegate {

     var window: UIWindow?

     func application(_ application: UIApplication,
         didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

       // Use Firebase library to configure APIs.
       FirebaseApp.configure()

       // Initialize the Google Mobile Ads SDK.
       GADMobileAds.sharedInstance().start(completionHandler: nil)

       return true
     }

   }
   ```

   ### Objective-C

   ```
   @import Firebase;
   @import GoogleMobileAds;
   ...

   @implementation AppDelegate

   - (BOOL)application:(UIApplication *)application
       didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
     // Use Firebase library to configure APIs.
     [FIRApp configure];
     // Initialize the Google Mobile Ads SDK.
     [[GADMobileAds sharedInstance] startWithCompletionHandler:nil];
     return YES;
   }

   @end
   ```

## **Step 4:** View user metrics and analytics data

After its initialization, the Mobile Ads SDK automatically starts
logging analytics
[events](https://support.google.com/admob/answer/9755157) and
[user properties](https://support.google.com/admob/answer/9755590)
from your app. You can view this data without adding any additional code to your
app or implementing any ads. Here's where you can see this analytics data:

* In the *User metrics* card of your AdMob account (*Home* or *Apps*
  dashboard), you can view curated [user
  metrics](https://support.google.com/admob/answer/9281746) derived from
  the collected analytics data, like average session duration,
  ARPU, and retention.
* In the [*Analytics*
  dashboard](https://console.firebase.google.com/project/_/analytics/) of
  the Firebase console, you can view aggregated statistics and [summaries of
  key metrics](https://support.google.com/firebase/answer/6317517).
  If you
  [add the Firebase SDK for Google Analytics](https://firebase.google.com/docs/admob/analytics-and-firebase),
  you can also
  [mark conversions for ad campaigns](https://support.google.com/analytics/answer/9267568)
  and
  [build custom audiences](https://support.google.com/analytics/answer/9267572)
  in the Firebase console.

Note that to better represent
ARPU and
ARPPU metrics, you
might want to include data from an analytics *custom* event called
[`ecommerce_purchase`](https://support.google.com/firebase/answer/6317517#revenue)
in the revenue calculation for these metrics
([learn how](https://firebase.google.com/docs/admob/analytics-and-firebase#arpu-and-arppu)).

Data typically appears within an hour but can take up to 48
hours to appear.


## **Step 5:** *(Optional)* Use more features of Google Analytics and Firebase

Take advantage of more opportunities and features to improve app monetization and
user engagement:

* **Add and use the Firebase SDK for Google Analytics**

  + Implement [custom event logging](https://firebase.google.com/docs/analytics/events?platform=ios)
    in your app.
  + Mark conversions for [custom ad
    campaigns](https://support.google.com/firebase/answer/6317518#custom).
  + [Include `ecommerce_purchase` event
    data](https://firebase.google.com/docs/admob/analytics-and-firebase#arpu-and-arppu) in the revenue
    calculation for
    ARPU and
    ARPPU metrics.

  To learn more, visit the guide for [using Google Analytics and Firebase
  with AdMob apps](https://firebase.google.com/docs/admob/analytics-and-firebase).
* **Use other Firebase products in your app**

  After you add the Firebase SDK for Google Analytics, use other Firebase
  products to optimize ads in your app.

  + [Remote Config](https://firebase.google.com/docs/remote-config) enables you to change the behavior
    and appearance of your app without publishing an app update.
  + [A/B Testing](https://firebase.google.com/docs/ab-testing) gives you the power to test changes to
    your app’s UI, features, or engagement campaigns to learn if they make an
    impact on your key metrics (like revenue and retention) before rolling the
    changes out widely.

* **Optimize ad monetization for your app**

  Try out different ad formats or configurations with a small subset of users,
  and then make data driven decisions about implementing the ad for all your
  users. To learn more, check out the following tutorials:

  + *Test new ad format adoption*
    ([overview](https://firebase.google.com/docs/tutorials/admob_test-new-ad-format-adoption_solution-overview) |
    [implementation](https://firebase.google.com/docs/tutorials/admob_test-new-ad-format-adoption_implementation-guide)).
  + *Optimize ad frequency*
    ([overview](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/solution-overview) |
    [implementation](https://firebase.google.com/docs/tutorials/optimize-ad-frequency)).

## **Step 6:** Choose an ad format to implement in your app

AdMob offers a number of different ad formats, so you can choose the format that
best fits the user experience of your app. Click a button for an ad format to
view detailed implementation instructions in the AdMob documentation.

### Banner

![](//developers.google.com/admob/images/format-banner.svg)

Rectangular ads that appear at the top or bottom of the device screen

Banner ads stay on screen while users are interacting with the app, and can
refresh automatically after a certain period of time. If you're new to mobile
advertising, they're a great place to start.

[Implement Banner Ads](https://developers.google.com/admob/ios/banner)


### Interstitial

![](//developers.google.com/admob/images/format-interstitial.svg)

Full-screen ads that cover the interface of an app until closed by the user

Interstitial ads are best used at natural pauses in the flow of an app's
execution, such as between levels of a game or just after a task is completed.

[Implement Interstitial Ads](https://developers.google.com/admob/ios/interstitial)


### Native

![](//developers.google.com/admob/images/format-native.svg)

Customizable ads that match the look and feel of your app

Native ads are a component-based ad format. You decide how and where Native ads
are placed so that the layout is more consistent with your app's design. By
choosing fonts, colors, and other details for yourself, you can create natural,
unobtrusive ad presentations that can add to a rich user experience.

[Implement Native Advanced Ads](https://developers.google.com/admob/ios/native-advanced)


### Rewarded

![](//developers.google.com/admob/images/format-rewarded.svg)

Ads that reward users for watching short videos and interacting with playable
ads and surveys

Rewarded (or "reward-based") ads can help monetize free-to-play users.

|  |  |
| --- | --- |
| [Implement Rewarded Ads](https://firebase.google.com/docs/admob/ios/rewarded-video) | [Implement Rewarded Ads (New APIs)](https://firebase.google.com/docs/admob/ios/rewarded-ads) |
