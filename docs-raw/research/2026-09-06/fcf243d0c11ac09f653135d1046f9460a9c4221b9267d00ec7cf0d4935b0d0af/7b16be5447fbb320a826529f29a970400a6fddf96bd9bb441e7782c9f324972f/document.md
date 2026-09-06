# Get started with AdMob in your C++ project

consider using the iOS and Android SDKs from AdMob.

**DEPRECATED:**
The Google Mobile Ads C++ SDK is *deprecated* as of June 17, 2024 and
should not be adopted in projects that don't already use it. It will enter
*End-of-Maintenance (EoM)* on June 17, 2025. Note that versions of the
SDK released before the EoM date will continue to function, but no further bug
fixes or changes will be released after the EoM date.

Instead of the Google Mobile Ads C++ SDK, consider using the
[iOS](https://firebase.google.com/docs/admob/ios/quick-start) and
[Android](https://firebase.google.com/docs/admob/android/quick-start) SDKs from AdMob.
For support, reach out to the
[Google Mobile Ads SDK Technical Forum](https://groups.google.com/g/google-admob-ads-sdk).

This quickstart guide is for publishers and developers who want to use AdMob
to monetize an app that's built with Firebase.
If you don't plan to include Firebase in your app, visit the
[standalone AdMob
guide](https://developers.google.com/admob/cpp/quick-start) instead.

If you haven't yet, learn about all the
[benefits](https://firebase.google.com/docs/admob/analytics-and-firebase) of using AdMob, Firebase,
and Google Analytics together.

If this is your first time going through this guide, we recommend that you
download and follow along using the [Google Mobile Ads C++ SDK test
app](https://github.com/firebase/quickstart-cpp/tree/main/gma/testapp).

## Before you begin

* If you don't already have a Firebase project and a Firebase app, follow the
  Firebase getting started guide:
  [Add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup).
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

1. Register each platform variant of your app as an AdMob app.

   1. [Sign into](https://admob.google.com/home/) or
      [sign up](https://support.google.com/admob/answer/7356219) for an
      AdMob account.
   2. [Register each platform variant of your app with
      AdMob](https://support.google.com/admob/answer/2773509). This
      step creates an AdMob app with a unique [AdMob
      App ID](https://support.google.com/admob/answer/7356431)
      that you'll need later in this guide.

   You'll be asked to add the Mobile Ads SDK to your app. Find
   detailed instructions for this task later in this guide.
2. Link your each of your AdMob apps to the corresponding Firebase app.

   This step is optional but strongly recommended. Learn more about the
   [benefits](https://firebase.google.com/docs/admob/analytics-and-firebase)
   of enabling user metrics and linking your AdMob apps to Firebase.

   For each platform variant, complete the following two steps in the *Apps*
   dashboard of your AdMob account:

   1. [Enable
      *User Metrics*](https://support.google.com/admob/answer/9263723)
      to allow AdMob to process and display curated analytics data in your
      AdMob account. It's also a required setting for you to link your
      AdMob app to Firebase.
   2. [Link your
      AdMob app](https://support.google.com/admob/answer/6383165)
      to your existing Firebase project and corresponding Firebase app.

      Make sure that you enter the same package name (Android) or bundle ID
      (iOS) as you entered for your Firebase app. Find your Firebase app's
      package name or bundle ID in the *Your apps* card of your
      settings >
      [*Project settings*](https://console.firebase.google.com/project/_/settings/general).

## **Step 2:** Add your AdMob App ID to your app

### Android

Add your
[AdMob App ID](https://support.google.com/admob/answer/7356431)
to your app's `AndroidManifest.xml` file by adding the `<meta-data>` tag as
shown below.

```
<manifest>
    <application>
        <!-- Sample AdMob App ID: ca-app-pub-3940256099942544~3347511713 -->
        <meta-data
            android:name="com.google.android.gms.ads.APPLICATION_ID"
            android:value="ADMOB_APP_ID"/>
    </application>
</manifest>
```



### iOS

In your app's `Info.plist` file, add a `GADApplicationIdentifier` key with a
string value of your
[AdMob App ID](https://support.google.com/admob/answer/7356431).

You can make this change programmatically:

```
<!-- Sample AdMob App ID: ca-app-pub-3940256099942544~1458002511 -->
<key>GADApplicationIdentifier</key>
<string>ADMOB_APP_ID</string>
```

Or, edit it in the property list editor:

![Property List Editor](//developers.google.com/admob/images/ios/admob_app_id_plist.png)

## **Step 3:** Add the Google Mobile Ads SDK

Since the Google Mobile Ads C++ SDK resides in the `firebase::gma` namespace,
download the [Firebase C++ SDK](https://firebase.google.com/download/cpp),
and then unzip it to a directory of your choice.

The Firebase C++ SDK is not platform-specific, but it does require
platform-specific library configurations.

### Android

**Note:** We recommend using CMake, but you can find instructions for ndk-build in
our general [Firebase C++ SDK Get Started
Guide](https://firebase.google.com/docs/cpp/setup?platform=android#ndk-build) to
link `libfirebase_app.a` and `libfirebase_gma.a` to your app.

1. In your project's `gradle.properties` file, specify the location of the
   unzipped SDK:

   ```
   systemProp.firebase_cpp_sdk.dir=FULL/PATH/TO/SDK
   ```
2. To your project's `settings.gradle` file, add the following content:

   ```
   def firebase_cpp_sdk_dir = System.getProperty('firebase_cpp_sdk.dir')

   gradle.ext.firebase_cpp_sdk_dir = "$firebase_cpp_sdk_dir"
   includeBuild "$firebase_cpp_sdk_dir"
   ```
3. To your module (app-level) Gradle file (usually `app/build.gradle`), add the
   following content, which includes the library dependency for the
   Google Mobile Ads C++ SDK.

   ```
   android.defaultConfig.externalNativeBuild.cmake {
     arguments "-DFIREBASE_CPP_SDK_DIR=$gradle.firebase_cpp_sdk_dir"
   }

   # Add the dependency for the Google Mobile Ads C++ SDK
   apply from: "$gradle.firebase_cpp_sdk_dir/Android/firebase_dependencies.gradle"
   firebaseCpp.dependencies {
     gma
   }
   ```
4. To your project's `CMakeLists.txt` file, add the following content.

   ```
   # Add Firebase libraries to the target using the function from the SDK.
   add_subdirectory(${FIREBASE_CPP_SDK_DIR} bin/ EXCLUDE_FROM_ALL)

   # Add the Google Mobile Ads C++ SDK.

   # The Firebase C++ library `firebase_app` is required,
   # and it must always be listed last.

   set(firebase_libs
     firebase_gma
     firebase_app
   )

   target_link_libraries(${target_name} "${firebase_libs}")
   ```
5. Sync your app to ensure that all dependencies have the necessary versions.

You're all set! Your C++ app is configured to use the Google Mobile Ads C++ SDK.

### iOS

The steps in this section are an example of how to add the Google Mobile Ads C++ SDK
to your iOS project.

1. Get CocoaPods version 1 or later by running:

   ```
   sudo gem install cocoapods --pre
   ```
2. Add Google Mobile Ads pod from the unzipped SDK.

   1. Create a Podfile if you don't already have one:

      ```
      cd YOUR_APP_DIRECTORY
      pod init
      ```
   2. To your Podfile, add the pod for the Google Mobile Ads C++ SDK:

      ```
      pod 'Google-Mobile-Ads-SDK'
      ```
   3. Install the pod, then open the `.xcworkspace` file in Xcode.

      ```
      pod install
      open YOUR_APP.xcworkspace
      ```
   4. Add the following frameworks from the Firebase C++ SDK to the project:

      * `xcframeworks/firebase.xcframework`
      * `xcframeworks/firebase_gma.xcframework`

You're all set! Your C++ app is configured to use the Google Mobile Ads C++ SDK.

## **Step 4:** Initialize the Google Mobile Ads SDK

**Note:** If you're using the Google Mobile Ads C++ SDK test app, the following steps have
already been done for you. You should now be able to run the test app.

Before loading ads, initialize the Mobile Ads SDK by calling
`firebase::gma::Initialize()`.

This call returns a `firebase::Future` that completes once initialization
finishes (or after a 30-second timeout). Call this method only once and as
early as possible, ideally at app launch.

**Warning:** Ads may be preloaded by the
Mobile Ads SDK or mediation partner SDKs upon calling
`Initialize()`. If you do need to take action before loading
ads, ensure you do so by invoking
`firebase::gma::SetRequestConfiguration()` *before*
initializing the Mobile Ads SDK. Here are some examples of
actions that might be needed prior to initialization:

* Obtain consent from users in the European Economic Area (EEA)
* Set any request-specific flags (such as
  `tag_for_child_directed_treatment` or
  `tag_for_under_age_of_consent`)

For more information, see our
[Targeting guide](https://developers.google.com/admob/cpp/targeting).

Here's an example of how to call `Initialize()`:

### Android

```
// Initialize the Google Mobile Ads library
firebase::InitResult result;
Future<AdapterInitializationStatus> future =
  firebase::gma::Initialize(jni_env, j_activity, &result);

if (result != kInitResultSuccess) {
  // Initialization immediately failed, most likely due to a missing dependency.
  // Check the device logs for more information.
  return;
}

// Monitor the status of the future.
// See "Use a Future to monitor the completion status of a method call" below.
if (future.status() == firebase::kFutureStatusComplete &&
    future.error() == firebase::gma::kAdErrorCodeNone) {
  // Initialization completed.
} else {
  // Initialization on-going, or an error has occurred.
}
```

### iOS

```
// Initialize the Google Mobile Ads library.
firebase::InitResult result;
Future<AdapterInitializationStatus> future =
  firebase::gma::Initialize(&result);

if (result != kInitResultSuccess) {
  // Initialization immediately failed, most likely due to a missing dependency.
  // Check the device logs for more information.
  return;
}

// Monitor the status of the future.
// See "Use a Future to monitor the completion status of a method call" below.
if (future.status() == firebase::kFutureStatusComplete &&
    future.error() == firebase::gma::kAdErrorCodeNone) {
  // Initialization completed.
} else {
  // Initialization on-going, or an error has occurred.
}
```

### Use a `Future` to monitor the completion status of a method call

A `Future` provides you a way to determine the completion status of your
asynchronous method calls.

For example, when your app calls `firebase::gma::Initialize()`, a new
`firebase::Future` is created and returned. Your app can then poll the
`status()` of the `Future` to determine when the initialization has completed.
Once complete, your app can invoke `result()` to obtain the resulting
`AdapterInitializationStatus`.

Methods that return a `Future` have a corresponding "last result" method that
apps can use to retrieve the most recent `Future` for a given action. For
example, `firebase::gma::Initialize()` has a corresponding method called
`firebase::gma::InitializeLastResult()`, which returns a `Future` that your app
can use to check the status of the last call to `firebase::gma::Initialize()`.

If the status of the `Future` is complete and its error code is
`firebase::gma::kAdErrorCodeNone`, then the operation has completed
successfully.

You can also register callbacks to be invoked when a `Future` is completed. In
some cases, the callback will be running in a different thread, so make sure
your code is thread-safe. This code snippet uses a function pointer for the
callback:

```
// Registers the OnCompletion callback. user_data is a pointer that is passed verbatim
// to the callback as a void*. This allows you to pass any custom data to the callback
// handler. In this case, the app has no data, so you must pass nullptr.
firebase::gma::InitializeLastResult().OnCompletion(OnCompletionCallback,
  /*user_data=*/nullptr);

// The OnCompletion callback function.
static void OnCompletionCallback(
  const firebase::Future<AdapterInitializationStatus>& future, void* user_data) {
  // Called when the Future is completed for the last call to firebase::gma::Initialize().
  // If the error code is firebase::gma::kAdErrorCodeNone,
  // then the SDK has been successfully initialized.
  if (future.error() == firebase::gma::kAdErrorCodeNone) {
    // success!
  } else {
    // failure.
  }
}
```



## **Step 5:** Choose an ad format to implement in your app

AdMob offers a number of different ad formats, so you can choose the format that
best fits the user experience of your app. Click a button for an ad format to
view detailed implementation instructions in the AdMob documentation.

### Banner

![](//developers.google.com/admob/images/format-banner.svg)

Rectangular ads that appear at the top or bottom of the device screen

Banner ads stay on screen while users are interacting with the app, and can
refresh automatically after a certain period of time. If you're new to mobile
advertising, they're a great place to start.

[Implement banner ads](https://developers.google.com/admob/cpp/banner)


### Interstitial

![](//developers.google.com/admob/images/format-interstitial.svg)

Full-screen ads that cover the interface of an app until closed by the user

Interstitial ads are best used at natural pauses in the flow of an app's
execution, such as between levels of a game or just after a task is completed.

[Implement interstitial ads](https://developers.google.com/admob/cpp/interstitial)


### Rewarded

![](//developers.google.com/admob/images/format-rewarded.svg)

Ads that reward users for watching short videos and interacting with playable
ads and surveys

Rewarded (or "reward-based") ads can help monetize free-to-play users.

[Implement rewarded ads](https://developers.google.com/admob/cpp/rewarded)

## Other topics of interest

### View user metrics and analytics data

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


### *(Optional)* Use more features of Google Analytics and Firebase

Take advantage of more opportunities and features to improve app monetization and
user engagement:

* **Add and use the Firebase SDK for Google Analytics**

  + Implement [custom event logging](https://firebase.google.com/docs/analytics/cpp/events)
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
