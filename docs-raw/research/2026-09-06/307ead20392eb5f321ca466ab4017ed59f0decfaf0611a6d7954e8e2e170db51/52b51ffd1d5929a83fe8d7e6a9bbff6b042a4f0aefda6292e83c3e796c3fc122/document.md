# Analytics FAQ and troubleshooting

This page provides troubleshooting help and answers to frequently asked
questions about using Analytics. If you
can't find what you're looking for or need additional help, contact
[Firebase support](https://support.google.com/firebase/contact/support).

#### Why is Google Analytics a recommended part of using Firebase products?

Google Analytics is a no-cost and unlimited analytics solution that
works with Firebase features to deliver powerful insights. It lets you
view event logs in Crashlytics, notification effectiveness in
FCM, deep link performance for Dynamic Links, and in-app purchase data
from Google Play. It powers advanced audience targeting in
Remote Config, Remote Config personalization, and more.

Google Analytics acts as a layer of intelligence in the
Firebase console to provide you with more actionable insights about how
to develop a high-quality app, grow your user base, and earn more money.

To get started,
[read the documentation](https://firebase.google.com/docs/analytics).

#### How do I control how my Analytics data is shared with the rest of Firebase?

By default, your Google Analytics data is used to enhance other
Firebase and Google features. You can control how your
Google Analytics data is shared in your project settings anytime.
Learn more about
[Data sharing settings](https://support.google.com/firebase/answer/6383877).

#### How do I update my Analytics property settings?

From the [*Admin* page](https://support.google.com/analytics/answer/6132368)
in your Google Analytics property, you can update your property settings,
such as:

* Data sharing settings
* Data retention settings
* Time zone and currency settings

To update your property settings, follow these steps:

1. In the Firebase console, go to your
   settings >
   [**Project settings**](https://console.firebase.google.com/project/_/settings/general/).
2. Go to the *Integrations* tab, and then in the Google Analytics
   card, click **Manage** or **View link**.
3. Click the link for your Google Analytics account to
   [open the account and property settings](https://support.google.com/analytics/answer/9355666).

#### How was the Analytics SDK updated for on-device conversion measurement support, and am I required to upgrade?

Before our release updating on-device conversion measurement using event
data, developers had to manually include multiple SDK modules to use
on-device measurement capabilities, a time-consuming process. As a result,
we updated the existing default SDK module (`FirebaseAnalytics`)
to include on-device conversion measurement capabilities as well for
Google Ads.

If you install the default Google Analytics for
Firebase iOS SDK, your app can also benefit from
[on-device conversion measurement capabilities](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement).

If you've pinned the SDK to a specific version, update to version
11.14.0 or higher and release a new version of your app.

**Note:** The modules deprecated in
Firebase 11.14.0 have been removed in Firebase 12.0.

| Target Capabilities | Old module(s)  (SDK versions < 11.14.0) | New module(s)  (SDK versions >= 11.14.0) |
| --- | --- | --- |
| Analytics  IDFA   On-Device Conversion Measurement (First-Party Data)  On-Device Conversion Measurement (Event Data) | N/A | FirebaseAnalytics |
| Analytics  IDFA | FirebaseAnalytics | FirebaseAnalytics/Core  FirebaseAnalytics/IdentitySupport |
| Analytics | FirebaseAnalytics/WithoutAdIdSupport (deprecated) | FirebaseAnalytics/Core |
| Analytics  On-Device Conversion Measurement (First-Party Data) | FirebaseAnalytics/WithoutAdIdSupport (deprecated)  FirebaseAnalyticsOnDeviceConversion (deprecated) | FirebaseAnalytics/Core  GoogleAdsOnDeviceConversion\* |
| Analytics  On-Device Conversion Measurement (Event Data) | N/A | FirebaseAnalytics/Core  GoogleAdsOnDeviceConversion |
| Analytics  On-Device Conversion Measurement (First-Party Data)  On-Device Conversion Measurement (Event Data) | N/A | FirebaseAnalytics/Core  GoogleAdsOnDeviceConversion |
| Analytics  IDFA  On-Device Conversion Measurement (First-Party Data) | FirebaseAnalytics  FirebaseAnalyticsOnDeviceConversion (deprecated) | FirebaseAnalytics\* |
| Analytics  IDFA  On-Device Conversion Measurement (Event Data) | N/A | FirebaseAnalytics |

**\*** This configuration will include On-Device Conversion Measurement
(Event Data) as well. If needed, you can disable the feature by setting the
value of `GOOGLE_ADS_ON_DEVICE_CONVERSION_EVENT_DATA_ENABLED` to
`NO` (Boolean) in your app's `Info.plist` file.

#### Can I install Analytics without ad attribution and IDFA collection features?

Yes. See the
[Configure Data Collection and Usage](https://firebase.google.com/docs/analytics/configure-data-collection?platform=ios#disable-idfa-collection) page for more details.

#### How do I enable the AdSupport framework?

Some Analytics features, such as audiences and campaign attribution, and
some user properties, such as age and interests, require the
[AdSupport framework](https://developer.apple.com/reference/adsupport)
to be enabled. Without this framework, Analytics can't collect information
needed for these features to function properly.

To enable the AdSupport framework:

1. In your Xcode project, select your project's target.
2. Select the **General** tab for your target.
3. Expand the **Linked Frameworks and Libraries** section.
4. Click **+** to add a framework.
5. Select **AdSupport.framework**.
6. Add the `-ObjC` linker flag to your project's build settings under
   `Other Linker Flags`.

Before submitting your app for review, ensure your app complies with
[IDFA usage guidelines](https://developer.apple.com/library/content/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/SubmittingTheApp.html#//apple_ref/doc/uid/TP40011225-CH33-SW8).

#### What changed in the Google Analytics section with the October 2021 update?

You can find a summary of these changes in the Firebase Help Center article
[New Google Analytics 4 functionality in Google Analytics
for Firebase](https://support.google.com/firebase/answer/11091821).

#### Why don't I see any Analytics data in the Firebase console after unlinking Firebase from Google Analytics?

Analytics data resides within the Google Analytics property — not
within the Firebase project. If you delete or unlink the property, then the
Analytics data won't be accessible to Firebase and you'll see an
empty *Analytics* dashboard in the Firebase console. Note that
because the data still resides in the previously linked property, you can
always relink the property to Firebase and see the Analytics data in the
Firebase console.

Linking a brand new Google Analytics account (and thus a new Google
Analytics property) to your Firebase project will result in an empty
*Analytics* dashboard in the Firebase console until additional
data is collected. Alternatively, you can consider to [move your existing Google Analytics property into a different
Google Analytics account](https://support.google.com/analytics/answer/9305872#zippy=%2Cin-this-article), which doesn't require unlinking from Firebase
and won't disrupt data collection.

#### If my Analytics property and its data were deleted, is there any way to get them back?

No. If your property has been deleted, it isn't possible to undelete the
property or retrieve the previously collected Analytics data stored in
that property.

If you'd like to start using Google Analytics again, you can link either a
new property or an existing property to your Firebase project. You can do
this linking in either the Firebase console or the Google Analytics UI.
Learn more about
[linking a Google Analytics property to your
Firebase project.](https://support.google.com/firebase/answer/9289399#linkga)

#### If my Analytics property was deleted, can I link a new Google Analytics property to my Firebase project and start using Analytics again?

If you'd like to start using Google Analytics again, you can link either a
new property or an existing property to your Firebase project. You can do
this linking in either the Firebase console or the Google Analytics UI.
Learn more about
[linking a Google Analytics property to your
Firebase project.](https://support.google.com/firebase/answer/9289399#linkga)

Note that because all Analytics data is stored in the property (not the
Firebase project), the previously collected Analytics data can't be
retrieved.

#### How will Firebase products or integrated Google products be affected by the deletion of my Analytics property?

Several Firebase products rely on the Google Analytics integration. If your
Analytics property and its data are deleted, the following will happen if
you use the following products:

* Crashlytics — You can no longer see crash-free users, breadcrumb
  logs, or velocity alerts.
* Cloud Messaging and In-App Messaging — You can no longer use
  targeting, campaign metrics, audience segmentation, and analytics labels.
* Remote Config — You can no longer use targeted configurations or
  Personalization.
* A/B Testing — You can no longer use A/B Testing because the
  experiment measurement is supplied by Google Analytics.
* Dynamic Links — Any feature that relies on data from Google Analytics will be
  disrupted.

In addition, the following integrations will be affected:

* You can no longer
  [export Analytics data to
  BigQuery](https://firebase.google.com/docs/projects/bigquery-export).
* You can no longer take advantage of
  [Google Ads integrations](https://support.google.com/google-ads/answer/6397604) or
  [Google AdMob integrations](https://support.google.com/admob/answer/6360054).

#### Can I move Analytics data from one Firebase project to another project?

No, it isn't possible to directly move Analytics data from one
Firebase project to another project.
However, you can export and combine data from both projects into a single
location, such as
[BigQuery](https://support.google.com/firebase/answer/6318765)
for analysis.

While moving existing data isn't possible, you can link an existing
Analytics property to a new Firebase project and start collecting data
from then on in that new project. You can do this linking in either the
Firebase console or the Google Analytics UI. Learn more about
[linking a property to your Firebase project](https://support.google.com/firebase/answer/9289399#linkga).

#### How do I segment users who have *not* met some criterion?

You can reframe the problem by "negatively targeting" these users. For
example, reframe the problem as "Don't show ads to people who have bought
something", and form an
[audience](https://support.google.com/firebase/answer/6317509) of those users to target.

#### Are audiences and/or events defined in the Google Analytics interface also available in the Firebase console?

Your audiences and user properties will be synced. For some features,
you'll need to use the Google Analytics interface, such as segmentation and
closed funnels. You can access the Google Analytics interface directly using
deep-links from the Firebase console.

Any changes you make from the Firebase console can also be performed in
Google Analytics, and those changes will be reflected in Firebase.
