# Log events

|  |  |
| --- | --- |
| **Select platform:** | [iOS+](https://firebase.google.com/docs/analytics/ios/events) [Android](https://firebase.google.com/docs/analytics/android/events) [Web](https://firebase.google.com/docs/analytics/web/events) [Flutter](https://firebase.google.com/docs/analytics/flutter/events) [Unity](https://firebase.google.com/docs/analytics/unity/events) [C++](https://firebase.google.com/docs/analytics/cpp/events) |

[Events](https://support.google.com/analytics/answer/9322688)
provide insight on what is happening in your app, such as user actions, system
events, or errors.

Analytics automatically logs some
[events](https://support.google.com/analytics/answer/9234069) for
you; you don't need to add any code to receive them. If your app needs to
collect additional data, you can log up to 500 different Analytics Event
*types* in your app. There is no limit on the total volume of events your app
logs. Note that event names are case-sensitive and that logging two events
whose names differ only in case results in two distinct events.

## Before you begin

Make sure that you've set up your project and can access Analytics as
described in
[Get Started with Analytics](https://firebase.google.com/docs/analytics/ios/get-started).

If you'd like to gather campaign attribution data, make sure to
[add the AdSupport framework to your project](https://firebase.google.com/docs/analytics/faq-and-troubleshooting#analytics-adsupport-framework).

## Log events

After you have configured the `FirebaseApp` instance, you can begin to log
events with the
[`logEvent()`](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#logevent_:parameters:) method.

To help you get started, the Analytics SDK defines a number of
recommended events that are common among different types of apps, including
retail and ecommerce, travel, and gaming apps. To learn more
[about these events](https://support.google.com/analytics/answer/9322688)
and when to use them, see [Recommended events](https://support.google.com/analytics/answer/9267735).

**Note:** To get the maximum detail in reports, log the recommended events that make
sense for your app and their prescribed parameters. This also ensures that you
benefit from the latest Google Analytics features as
they become available.

You can find implementation details in the constants reference for
[Swift](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants) and
[Objective-C](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants).

The following example demonstrates how to log a recommended
`kFIRSelectContent` event:

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

In addition to the prescribed parameters, you can add the following parameters
to any event:

* Custom parameters: Custom parameters can be used as
  [dimensions or metrics](https://support.google.com/analytics/answer/10075209)
  in [Analytics reports](https://support.google.com/analytics/answer/9212670).
  You can use custom dimensions for non-numerical event parameter data and
  custom metrics for any parameter data better represented numerically. Once
  you've logged a custom parameter using the SDK, register the dimension or
  metric to ensure those custom parameters appear in Analytics
  reports. To do this, in the Firebase console, go to **Analytics** >
  **Custom Definitions**.

  Custom parameters can be used in
  [audience](https://support.google.com/firebase/answer/6317509)
  definitions that may be applied to every report.
  Custom parameters are also included in data
  [exported to BigQuery](https://support.google.com/firebase/answer/7030014)
  if your app is linked to a BigQuery project. Find sample queries and much more
  at [Google Analytics 4 BigQuery Export](https://developers.google.com/analytics/bigquery).
* `kFIRParameterValue` parameter: `kFIRParameterValue`
  is a general purpose parameter that is useful for accumulating a key metric
  that pertains to an event. Examples include revenue, distance, time, and
  points.

If your application has specific needs not covered by a recommended
event type, you can log your own custom events as shown in this example:

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

## Set default event parameters

You can log parameters across events using
[`setDefaultEventParameters`](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#setdefaulteventparameters_:).
Default parameters are associated with all future events that are logged.

As with custom parameters, register the default event parameters to ensure those
custom parameters appear in Analytics reports.

### Swift

```
Analytics.setDefaultEventParameters([
  "level_name": "Caverns01",
  "level_difficulty": 4
])
```

### Objective-C

```
[FIRAnalytics setDefaultEventParameters:
  @{
  @"level_name": "Caverns01",
  @"level_difficulty": @(4)
}];
```

If a parameter is specified in the
[`logEvent()`](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#logevent_:parameters:)
method, that value is used instead of the default.

To clear a default parameter, call the
[`setDefaultEventParameters`](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#setdefaulteventparameters_:)
method with the parameter set to `nil`.

## View events in the Xcode debug console

You can enable verbose logging to monitor logging of events by the SDK to help
verify that events are being logged properly. This includes both automatically
and manually logged events.

You can enable verbose logging as follows:

1. In Xcode, select **Product > Scheme > Edit scheme...**
2. Select **Run** from the left menu.
3. Select the **Arguments** tab.
4. In the **Arguments Passed On Launch** section, add
   `-FIRAnalyticsVerboseLoggingEnabled`.

The next time you run your app, your events will display in the Xcode debug
console, helping you immediately verify that events are being sent.

## View events in the dashboard

In the Firebase console, you can view aggregated statistics about your events
in the **Analytics** >
[**Events** dashboard](https://console.firebase.google.com/project/_/analytics/events).

Note the following about this dashboard:

* The dashboard shows the event reports that are automatically created for
  each distinct type of event logged by your app.
* The dashboard updates periodically throughout the day. For immediate testing,
  use the Xcode debug console output as described in the previous section of
  this guide.
