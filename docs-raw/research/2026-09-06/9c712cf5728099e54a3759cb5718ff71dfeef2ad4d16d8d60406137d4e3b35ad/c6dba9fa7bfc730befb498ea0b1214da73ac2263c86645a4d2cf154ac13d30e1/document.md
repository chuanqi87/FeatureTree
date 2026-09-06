# Customize crash reports for Apple platforms

|  |  |
| --- | --- |
| **Select platform:** | [iOS+](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports) [Android](https://firebase.google.com/docs/crashlytics/android/customize-crash-reports) [Flutter](https://firebase.google.com/docs/crashlytics/flutter/customize-crash-reports) [Unity](https://firebase.google.com/docs/crashlytics/unity/customize-crash-reports) |

You can click into an issue and get a detailed event report in the
**DevOps & Engagement** > [**Crashlytics** dashboard](https://console.firebase.google.com/project/_/crashlytics) of the
Firebase console. You can customize those reports to help you better
understand what's happening in your app and the circumstances around events
reported to Crashlytics.

* Instrument your app to log [custom keys](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#add-keys),
  [custom log messages](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#add-logs), and [user identifiers](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#set-user-ids).
* Report [exceptions](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#log-excepts) to Crashlytics.
* Automatically get [breadcrumb logs](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#get-breadcrumb-logs) if your app uses the
  Firebase SDK for Google Analytics. These logs give you visibility into
  user actions leading up to a Crashlytics-collected event in your app.
* Turn off automatic crash reporting and
  [enable opt-in reporting](https://firebase.google.com/docs/crashlytics/ios/customize-crash-reports#enable-reporting) for your users. Note that, by
  default, Crashlytics automatically collects crash reports for all your
  app's users.

## Add custom keys

Custom keys help you get the specific state of your app leading up to a crash.
You can associate arbitrary key-value pairs with your crash reports, then use
the custom keys to search and filter crash reports in the
**DevOps & Engagement** > [**Crashlytics** dashboard](https://console.firebase.google.com/project/_/crashlytics) of the
Firebase console.

* You can search for issues that match a custom key.
* When you're reviewing a specific issue in the console, you can view the
  associated custom keys for each event (**Keys** subtab) and even filter the
  events by custom keys (**Filter** menu at the top of the page).

**Note:** Crashlytics supports a maximum of 64 key-value pairs. After you
reach this threshold, additional values are not saved. Each key-value pair can
be up to 1 kB in size.

Use the `setCustomValue` method to set key-value pairs. For example:

### Swift

```
// Set int_key to 100.
Crashlytics.crashlytics().setCustomValue(100, forKey: "int_key")

// Set str_key to "hello".
Crashlytics.crashlytics().setCustomValue("hello", forKey: "str_key")
```

### Objective-C

When setting integers, booleans, or floats, box the value as `@(value)`.

```
// Set int_key to 100.
[[FIRCrashlytics crashlytics] setCustomValue:@(100) forKey:@"int_key"];

// Set str_key to "hello".
[[FIRCrashlytics crashlytics] setCustomValue:@"hello" forKey:@"str_key"];
```

You can also modify the value of an existing key by calling the key and setting
it to a different value. For example:

### Swift

```
Crashlytics.crashlytics().setCustomValue(100, forKey: "int_key")

// Set int_key to 50 from 100.
Crashlytics.crashlytics().setCustomValue(50, forKey: "int_key")
```

### Objective-C

```
[[FIRCrashlytics crashlytics] setCustomValue:@(100) forKey:@"int_key"];

// Set int_key to 50 from 100.
[[FIRCrashlytics crashlytics] setCustomValue:@(50) forKey:@"int_key"];
```

Add key-value pairs in bulk by using the `setCustomKeysAndValues` method with an
NSDictionary as the only parameter:

### Swift

```
let keysAndValues = [
                 "string key" : "string value",
                 "string key 2" : "string value 2",
                 "boolean key" : true,
                 "boolean key 2" : false,
                 "float key" : 1.01,
                 "float key 2" : 2.02
                ] as [String : Any]

Crashlytics.crashlytics().setCustomKeysAndValues(keysAndValues)
```

### Objective-C

```
NSDictionary *keysAndValues =
    @{@"string key" : @"string value",
      @"string key 2" : @"string value 2",
      @"boolean key" : @(YES),
      @"boolean key 2" : @(NO),
      @"float key" : @(1.01),
      @"float key 2" : @(2.02)};

[[FIRCrashlytics crashlytics] setCustomKeysAndValues: keysAndValues];
```

## Add custom log messages

To give yourself more context for the events leading up to a crash, you can add
custom Crashlytics logs to your app. Crashlytics associates the logs
with your crash data and displays them in the **Logs** tab when you view the
details of an issue (see all your issues in the **DevOps & Engagement** >
[**Crashlytics** dashboard](https://console.firebase.google.com/project/_/crashlytics) of the Firebase console).

**Note:** To avoid slowing down your app, Crashlytics limits logs to 64kB
and deletes older log entries when logs for a session go over that limit.

### Swift

Use `log()` or `log(format:, arguments:)` to help pinpoint issues. If you
want to get a useful log output with messages, the object that you pass to
`log()` must conform to the
[`CustomStringConvertible`](https://developer.apple.com/documentation/swift/customstringconvertible)
property. `log()` returns the description property you define for
the object. For example:

```
Crashlytics.crashlytics().log("Higgs-Boson detected! Bailing out…, \(attributesDict)")
```

`.log(format:, arguments:)` formats values returned from calling
`getVaList()`. For example:

```
Crashlytics.crashlytics().log(format: "%@, %@", arguments: getVaList(["Higgs-Boson detected! Bailing out…", attributesDict]))
```

For more details on how to use `log()` or `log(format:, arguments:)`,
refer to the Crashlytics
[reference documentation](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics).

### Objective-C

Use `log` or `logWithFormat` to help pinpoint issues. Note that if you
want to get a useful log output with messages, the object that you pass
to either method must override the `description` instance property.
For example:

```
[[FIRCrashlytics crashlytics] log:@"Simple string message"];

[[FIRCrashlytics crashlytics] logWithFormat:@"Higgs-Boson detected! Bailing out... %@", attributesDict];

[[FIRCrashlytics crashlytics] logWithFormat:@"Logging a variable argument list %@" arguments:va_list_arg];
```

For more details on how to use `log` and `logWithFormat`, refer to the
Crashlytics [reference documentation](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics).

## Set user identifiers

To diagnose an issue, it’s often helpful to know which of your users experienced
a given crash. Crashlytics includes a way to anonymously identify users in
your crash reports.

To add user IDs to your reports, assign each user a unique identifier in the
form of an ID number, token, or hashed value:

### Swift

```
Crashlytics.crashlytics().setUserID("123456789")
```

### Objective-C

```
[[FIRCrashlytics crashlytics] setUserID:@"123456789"];
```

If you ever need to clear a user identifier after you set it, reset the value to
a blank string. Clearing a user identifier does not remove existing
Crashlytics records. If you need to delete records associated with a user
ID, [contact Firebase support](https://firebase.google.com/support/troubleshooter/contact).

## Report non-fatal exceptions

In addition to automatically reporting your app's crashes, Crashlytics lets
you record non-fatal exceptions and sends them to you the next time your app
launches.

**Note:** Crashlytics only stores the most recent eight exceptions in a given
app session. If your app throws more than eight exceptions in a session, older
exceptions are lost.

You can record non-fatal exceptions by recording `NSError` objects with the
`recordError` method. `recordError` captures the thread's call stack by calling
`[NSThread callStackReturnAddresses]`.

### Swift

```
Crashlytics.crashlytics().record(error: error)
```

### Objective-C

```
[[FIRCrashlytics crashlytics] recordError:error];
```

When using the `recordError` method, it's important to understand the `NSError`
structure and how Crashlytics uses the data to group crashes. Incorrect
usage of the `recordError` method can cause unpredictable behavior and may
cause Crashlytics to limit reporting of logged errors for your app.

An `NSError` object has three arguments:

* `domain: String`
* `code: Int`
* `userInfo: [AnyHashable : Any]? = nil`

Unlike fatal crashes, which are grouped via stack trace analysis, logged errors
are grouped by `domain` and `code`. This is an important distinction
between fatal crashes and logged errors. For example:

### Swift

```
let userInfo = [
  NSLocalizedDescriptionKey: NSLocalizedString("The request failed.", comment: ""),
  NSLocalizedFailureReasonErrorKey: NSLocalizedString("The response returned a 404.", comment: ""),
  NSLocalizedRecoverySuggestionErrorKey: NSLocalizedString("Does this page exist?", comment: ""),
  "ProductID": "123456",
  "View": "MainView"
]

let error = NSError.init(domain: NSCocoaErrorDomain,
                         code: -1001,
                         userInfo: userInfo)
```

### Objective-C

```
NSDictionary *userInfo = @{
  NSLocalizedDescriptionKey: NSLocalizedString(@"The request failed.", nil),
  NSLocalizedFailureReasonErrorKey: NSLocalizedString(@"The response returned a 404.", nil),
  NSLocalizedRecoverySuggestionErrorKey: NSLocalizedString(@"Does this page exist?", nil),
  @"ProductID": @"123456",
  @"View": @"MainView",
};

NSError *error = [NSError errorWithDomain:NSCocoaErrorDomain
                                     code:-1001
                                 userInfo:userInfo];
```

When you log the error above, it creates a new issue that is grouped by
`NSSomeErrorDomain` and `-1001`. Additional logged errors that use the same
domain and code values are grouped under the same issue. Data contained within
the `userInfo` object are converted to key-value pairs and displayed in the
keys/logs section within an individual issue.

**Caution:** Avoid using unique values, such as user ID, product ID, and timestamps
in the domain and code fields. Using unique values in these fields causes a high
cardinality of issues and may result in Crashlytics needing to limit the
reporting of logged errors in your app. Unique values should instead be added to
the `userInfo` dictionary object.


### Logs and custom keys

Just like crash reports, you can embed logs and custom keys to add context to
the `NSError`. However, there is a difference in what logs are attached to
crashes versus logged errors. When a crash occurs and the app is relaunched, the
logs Crashlytics retrieves from disk are those that were written right up to
the time of the crash. When you log an `NSError`, the app does not immediately
terminate. Because Crashlytics only sends the logged error report on the
next app launch and must limit the amount of space allocated for logs on disk,
it is possible to log enough after an `NSError` is recorded so that all relevant
logs are rotated out by the time Crashlytics sends the report from the
device. Keep this balance in mind when logging `NSErrors` and using logs and
custom keys in your app.

### Performance considerations

Keep in mind that logging an `NSError` can be fairly expensive. At the time you
make the call, Crashlytics captures the current thread’s call stack using a
process called stack unwinding. This process can be CPU and I/O intensive,
particularly on architectures that support DWARF unwinding (arm64 and x86).
After the unwind is complete, the information is written to disk synchronously.
This prevents data loss if the next line were to crash.

While it is safe to call
this API on a background thread, remember that dispatching this call to another
queue loses the context of the current stack trace.

### What about NSExceptions?

Crashlytics doesn't offer a facility for logging and recording `NSException`
instances directly. Generally speaking, the Cocoa and Cocoa Touch APIs are not
exception-safe. That means the use of `@catch` can have very serious unintended
side-effects in your process, even when used with extreme care. You should never
use `@catch` statements in your code. Refer to
[Apple's documentation](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Exceptions/Articles/ExceptionsAndCocoaFrameworks.html)
on the topic.

## Customize stack traces

If your app runs in a non-native environment (such as C++ or Unity), you can use
the Exception Model API to report crash metadata in your app's native exception
format. Reported exceptions are marked as non-fatals.

### Swift

```
var  ex = ExceptionModel(name:"FooException", reason:"There was a foo.")
ex.stackTrace = [
  StackFrame(symbol:"makeError", file:"handler.js", line:495),
  StackFrame(symbol:"then", file:"routes.js", line:102),
  StackFrame(symbol:"main", file:"app.js", line:12),
]

crashlytics.record(exceptionModel:ex)
```

### Objective-C

```
FIRExceptionModel *model =
    [FIRExceptionModel exceptionModelWithName:@"FooException" reason:@"There was a foo."];
model.stackTrace = @[
  [FIRStackFrame stackFrameWithSymbol:@"makeError" file:@"handler.js" line:495],
  [FIRStackFrame stackFrameWithSymbol:@"then" file:@"routes.js" line:102],
  [FIRStackFrame stackFrameWithSymbol:@"main" file:@"app.js" line:12],
];

[[FIRCrashlytics crashlytics] recordExceptionModel:model];
```

Custom stack frames can also be initialized with just addresses:

### Swift

```
var  ex = ExceptionModel.init(name:"FooException", reason:"There was a foo.")
ex.stackTrace = [
  StackFrame(address:0xfa12123),
  StackFrame(address:12412412),
  StackFrame(address:194129124),
]

crashlytics.record(exceptionModel:ex)
```

### Objective-C

```
FIRExceptionModel *model =
    [FIRExceptionModel exceptionModelWithName:@"FooException" reason:@"There was a foo."];
model.stackTrace = @[
  [FIRStackFrame stackFrameWithAddress:0xfa12123],
  [FIRStackFrame stackFrameWithAddress:12412412],
  [FIRStackFrame stackFrameWithAddress:194129124],
];


[[FIRCrashlytics crashlytics] recordExceptionModel:model];
```

## Get breadcrumb logs

Breadcrumb logs give you a better understanding of the interactions that a user
had with your app leading up to a crash, non-fatal, or ANR event. These logs can
be helpful when trying to reproduce and debug an issue.

Breadcrumb logs are powered by Google Analytics, so to get breadcrumb logs, you
need to
[enable Google Analytics](https://support.google.com/firebase/answer/9289399#linkga)
for your Firebase project and
[add the Firebase SDK for Google Analytics](https://firebase.google.com/docs/analytics/get-started#add-sdk)
to your app. Once these requirements are met, breadcrumb logs are automatically
included with an event's data within the **Logs** tab when you view the details
of an issue (see all your issues in the **DevOps & Engagement** >
[**Crashlytics** dashboard](https://console.firebase.google.com/project/_/crashlytics) of the Firebase console).

The Analytics SDK
[automatically logs the `screen_view` event](https://firebase.google.com/docs/analytics/screenviews)
which enables the breadcrumb logs to show a list of screens viewed before the
crash, non-fatal, or ANR event. A `screen_view` breadcrumb log contains a
`firebase_screen_class` parameter.

Breadcrumb logs are also populated with any
[custom events](https://firebase.google.com/docs/analytics/events) that you manually log within the user’s
session, including the event's parameter data. This data can help show a series
of user actions leading up to a crash, non-fatal, or ANR event.

Note that you can
[control the collection and use of Google Analytics data](https://firebase.google.com/docs/analytics/configure-data-collection),
which includes the data that populates breadcrumb logs.

## Enable opt-in reporting

If you enable opt-in reporting by disabling automatic
reporting, you will reduce the accuracy of your app's event count and
crash-free metrics, which makes them less reflective of the overall stability
of your app.
[Learn more.](https://firebase.google.com/docs/crashlytics/crash-free-metrics#impact-of-data-collection-settings)

By default, Crashlytics automatically collects crash reports for all your
app's users. To give users more control over the data they send, you can enable
opt-in reporting by disabling automatic reporting and only sending data to
Crashlytics when you choose to in your code.

1. Turn off automatic collection by adding a new key to your `Info.plist` file:

   * Key: `FirebaseCrashlyticsCollectionEnabled`
   * Value: `false`
2. Enable collection for select users by calling the Crashlytics data
   collection override at runtime. The override value persists across all
   subsequent launches of your app so Crashlytics can automatically collect
   reports for that user.

   ### Swift

   ```
   Crashlytics.crashlytics().setCrashlyticsCollectionEnabled(true)
   ```

   ### Objective-C

   ```
   [[FIRCrashlytics crashlytics] setCrashlyticsCollectionEnabled:YES];
   ```

   If the user later opts-out of data collection, you can pass `false` as the
   override value, which will apply the next time the user launches the app and
   will persist across all subsequent launches for that user.

**Note:** When data collection is disabled for a user, Crashlytics will
store crash information locally on the device. If data collection is
subsequently enabled, any crash information stored on the device will be
sent to Crashlytics for processing.


## Manage Crash Insights data

Crash Insights helps you resolve issues by comparing your anonymized stack
traces to traces from other Firebase apps and letting you know if your issue is
part of a larger trend. For many issues, Crash Insights even provides resources
to help you debug the crash.

Crash Insights uses aggregated crash data to identify common stability trends.
If you'd prefer not to share your app's data, you can opt-out of Crash Insights
from the **Crash Insights** menu at the top of the issue list in the
**DevOps & Engagement** > [**Crashlytics** dashboard](https://console.firebase.google.com/project/_/crashlytics) of the
Firebase console.

**Note:** Disabling data sharing also removes insights on your issues. Changes may
take up to 24 hours to take effect.


## Next steps

* [Export your data to BigQuery or Cloud Logging](https://firebase.google.com/docs/crashlytics/export-data-to-cloud)
  for advanced analysis and features, like
  querying your data, building custom dashboards, and setting up custom alerts.
