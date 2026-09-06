# Log events

|  |  |
| --- | --- |
| **Select platform:** | [iOS+](https://firebase.google.com/docs/analytics/ios/events) [Android](https://firebase.google.com/docs/analytics/android/events) [Web](https://firebase.google.com/docs/analytics/web/events) [Flutter](https://firebase.google.com/docs/analytics/flutter/events) [Unity](https://firebase.google.com/docs/analytics/unity/events) [C++](https://firebase.google.com/docs/analytics/cpp/events) |

Events provide insight on what is happening in your app, such as user
actions, system events, or errors.

Google Analytics automatically logs some
[events](https://support.google.com/analytics/answer/6317485) for you;
you don't need to add any code to receive them. If your app needs to collect
additional data, you can log up to 500 different Analytics event types
in your app. There is no limit on the total volume of events your app logs.
Note that event names are case-sensitive and that logging two events whose
names differ only in case results in two distinct events.

## Before you begin

Make sure that you've set up your project and can access Analytics as
described in
[Get Started with Analytics for C++](https://firebase.google.com/docs/analytics/cpp/get-started#before_you_begin).

## Log events

After you have initialized the `firebase::analytics` module, you can use it to log
events with the [`LogEvent()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#logevent) method.

To help you get started, the Analytics SDK defines a number of
recommended events that are common among different types of apps, including
retail and ecommerce, travel, and gaming apps. To learn more about these events
and when to use them, browse the [Events and properties](https://support.google.com/analytics/answer/9267735)
articles in the Firebase Help Center.

**Note:** To get the maximum detail in reports, log the suggested Analytics
Events that make sense for your app and their prescribed parameters. This also
ensures that you benefit from the latest Google Analytics features as
they become available.

You can find implementation details for recommended events in the following
locations:

* Suggested events: see the list of [`Event`](https://firebase.google.com/docs/reference/cpp/group/event-names) constants.
* Prescribed parameters: see the list of [`Parameters`](https://firebase.google.com/docs/reference/cpp/group/parameter-names) constants.

The following example demonstrates how to log a suggested
[`SELECT_CONTENT`](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#SELECT_CONTENT) Event:

```
  const analytics::Parameter kSelectContentParameters[] = {
    analytics::Parameter(analytics::kParameterItemID , id),
    analytics::Parameter(analytics::kParameterItemName, "name"),
    analytics::Parameter(analytics::kUserPropertySignUpMethod, "Google"),
    analytics::Parameter("favorite_food", mFavoriteFood),
    analytics::Parameter("user_id", mUserId),
  };
  analytics::LogEvent(
    analytics::kEventSelectContent, kSelectContentParameters,
    sizeof(kSelectContentParameters) / sizeof(kSelectContentParameters[0]));
```

In addition to the prescribed parameters, you can add the following parameters
to any event:

* Custom parameters: Custom parameters are not represented directly in your
  Analytics reports, but they can be used as filters in
  [Audience](https://support.google.com/firebase/answer/6317509) definitions that can be applied to every report. Custom
  parameters are also included in data [exported to BigQuery](https://support.google.com/firebase/answer/6318765) if
  your app is linked to a BigQuery project.
* `VALUE` Parameter: [`VALUE`](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE) is a general purpose parameter
  that is useful for accumulating a key metric that pertains to an
  Analytics Event. Examples include revenue, distance, time and points.

If your application has specific needs not covered by a suggested
Analytics Event type, you can log your own custom Analytics Events
as shown in this example:

```
// Copyright 2016 Google Inc. All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "firebase/analytics.h"
#include "firebase/analytics/event_names.h"
#include "firebase/analytics/parameter_names.h"
#include "firebase/analytics/user_property_names.h"
#include "firebase/app.h"

// Thin OS abstraction layer.
#include "main.h"  // NOLINT

// Execute all methods of the C++ Analytics API.
extern "C" int common_main(int argc, const char* argv[]) {
  namespace analytics = ::firebase::analytics;
  ::firebase::App* app;

  LogMessage("Initialize the Analytics library");
#if defined(__ANDROID__)
  app = ::firebase::App::Create(GetJniEnv(), GetActivity());
#else
  app = ::firebase::App::Create();
#endif  // defined(__ANDROID__)

  LogMessage("Created the firebase app %x",
             static_cast<int>(reinterpret_cast<intptr_t>(app)));
  analytics::Initialize(*app);
  LogMessage("Initialized the firebase analytics API");

  LogMessage("Enabling data collection.");
  analytics::SetAnalyticsCollectionEnabled(true);
  // App session times out after 30 minutes.
  // If the app is placed in the background and returns to the foreground after
  // the timeout is expired analytics will log a new session.
  analytics::SetSessionTimeoutDuration(1000 * 60 * 30);

  LogMessage("Get App Instance ID...");
  auto future_result = analytics::GetAnalyticsInstanceId();
  while (future_result.status() == firebase::kFutureStatusPending) {
    if (ProcessEvents(1000)) break;
  }
  if (future_result.status() == firebase::kFutureStatusComplete) {
    LogMessage("Analytics Instance ID %s", future_result.result()->c_str());
  } else {
    LogMessage("ERROR: Failed to fetch Analytics Instance ID %s (%d)",
               future_result.error_message(), future_result.error());
  }

  LogMessage("Set user properties.");
  // Set the user's sign up method.
  analytics::SetUserProperty(analytics::kUserPropertySignUpMethod, "Google");
  // Set the user ID.
  analytics::SetUserId("uber_user_510");

  LogMessage("Log current screen.");
  // Log the user's current screen.
  analytics::LogEvent(analytics::kEventScreenView, "Firebase Analytics C++ testapp", "testapp" );

  // Log an event with no parameters.
  LogMessage("Log login event.");
  analytics::LogEvent(analytics::kEventLogin);

  // Log an event with a floating point parameter.
  LogMessage("Log progress event.");
  analytics::LogEvent("progress", "percent", 0.4f);

  // Log an event with an integer parameter.
  LogMessage("Log post score event.");
  analytics::LogEvent(analytics::kEventPostScore, analytics::kParameterScore,
                      42);

  // Log an event with a string parameter.
  LogMessage("Log group join event.");
  analytics::LogEvent(analytics::kEventJoinGroup, analytics::kParameterGroupID,
                      "spoon_welders");

  // Log an event with multiple parameters.
  LogMessage("Log level up event.");
  {
    const analytics::Parameter kLevelUpParameters[] = {
        analytics::Parameter(analytics::kParameterLevel, 5),
        analytics::Parameter(analytics::kParameterCharacter, "mrspoon"),
        analytics::Parameter("hit_accuracy", 3.14f),
    };
    analytics::LogEvent(
        analytics::kEventLevelUp, kLevelUpParameters,
        sizeof(kLevelUpParameters) / sizeof(kLevelUpParameters[0]));
  }

  LogMessage("Complete");

  // Wait until the user wants to quit the app.
  while (!ProcessEvents(1000)) {
  }

  analytics::Terminate();
  delete app;

  LogMessage("Shutdown");

  return 0;
}
```



## View events in the Android Studio debug log

You can enable verbose logging to monitor logging of events by the SDK to help
verify that events are being logged properly. This includes both automatically
and manually logged events.

You can enable verbose logging with a series of adb commands:

```
adb shell setprop log.tag.FA VERBOSE
```

```
adb shell setprop log.tag.FA-SVC VERBOSE
```

```
adb logcat -v time -s FA FA-SVC
```

This command displays your events in the Android Studio logcat, helping you
immediately verify that events are being sent.

## View analytics events in the dashboard

In the Firebase console, you can view aggregated statistics about your events
in the **Analytics** >
[**Events** dashboard](https://console.firebase.google.com/project/_/analytics/events).

Note the following about this dashboard:

* The dashboard shows the event reports that are automatically created for
  each distinct type of event logged by your app.
* The dashboard updates periodically throughout the day. For immediate testing,
  use the Xcode debug console or logcat output as described in the previous
  section of this guide.

Read more about the [dashboard](https://support.google.com/analytics/answer/11014767).
