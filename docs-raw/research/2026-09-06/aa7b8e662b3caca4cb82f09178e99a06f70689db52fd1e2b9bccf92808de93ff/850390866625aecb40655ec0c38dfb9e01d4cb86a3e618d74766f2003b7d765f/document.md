# Logging

Capture telemetry from your app for debugging and performance analysis using the unified logging system.

## Discussion

When debugging problems in your app, it’s helpful to record the exact sequence of events that occurred, along with supplemental data about those events. Log messages provide a continuous record of your app’s runtime behavior, and make it easier to identify problems that can’t be caught easily using other techniques. Specifically, you might use log messages:

- When you are unable to attach a debugger to the app, such as when you’re diagnosing problems on a user’s machine.
- When the problem is intermittent, and is difficult to catch in the debugger.
- When you want to get a general sense of your app’s behavior—for example, you want to know when certain tasks start and end.

The unified logging system provides a comprehensive and performant API to capture telemetry across all levels of the system. This system centralizes the storage of log data in memory and on disk, rather than writing that data to a text-based log file. You view log messages using the Console app, `log` command-line tool, or Xcode debug console. You can also access log messages programmatically using the <doc://com.apple.documentation/documentation/OSLog> framework.

> Important:
> The unified logging system is available in iOS 10.0 and later, macOS 10.12 and later, tvOS 10.0 and later, and watchOS 3.0 and later. This system supersedes the Apple System Logger (ASL) and Syslog APIs.

## Topics

### Essentials

[Generating Log Messages from Your Code](/documentation/os/generating-log-messages-from-your-code)

Record useful debugging and analysis information, and include dynamic content in your messages.

[Viewing Log Messages](/documentation/os/viewing-log-messages)

Use various tools to retrieve log information.

[Customizing Logging Behavior While Debugging](/documentation/os/customizing-logging-behavior-while-debugging)

Control which log events are recorded.

### Log Messages

[Message Argument Formatters](/documentation/os/message-argument-formatters)

Manage the privacy and presentation of the message’s interpolated values using type-aware formatters.

[Legacy Logging Symbols](/documentation/os/legacy-logging-symbols)

Migrate your code away from using these legacy symbols.

[os_log_t](/documentation/os/os-log-t)

A log object that you pass to logging functions to send messages to that log.

[`os_log_with_type`](/documentation/os/os_log_with_type)

Sends a message at a specific logging level, such as default, info, debug, error, or fault, to the logging system.

[`OSLogType`](/documentation/os/OSLogType)

The various log levels that the unified logging system provides.

[`os_log`](/documentation/os/os_log)

Sends a default-level message to the logging system.

[`os_log_info`](/documentation/os/os_log_info)

Sends an info-level message to the logging system.

[`os_log_debug`](/documentation/os/os_log_debug)

Sends a debug-level message to the logging system.

[`os_log_error`](/documentation/os/os_log_error)

Sends an error-level message to the logging system.

[`os_log_fault`](/documentation/os/os_log_fault)

Sends a fault-level message to the logging system.

### Log Messages

[`Logger`](/documentation/os/Logger)

An object for writing interpolated string messages to the unified logging system.

[Message Argument Formatters](/documentation/os/message-argument-formatters)

Manage the privacy and presentation of the message’s interpolated values using type-aware formatters.

[`os_log_with_type`](/documentation/os/os_log_with_type)

Sends a message at a specific logging level, such as default, info, debug, error, or fault, to the logging system.

[`OSLogType`](/documentation/os/OSLogType)

The various log levels that the unified logging system provides.

### Measure Events

[Recording Performance Data](/documentation/os/recording-performance-data)

Add signposts to record interesting time-based events.

[`OSSignposter`](/documentation/os/OSSignposter)

An object for measuring task performance using the unified logging system.

[Legacy Signpost Symbols](/documentation/os/legacy-signpost-symbols)

Migrate your code away from using these legacy symbols.

[`os_signpost_emit_with_type`](/documentation/os/os_signpost_emit_with_type)

Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments.

[`OSSignpostType`](/documentation/os/OSSignpostType)

The different kinds of signpost.

[`os_signpost_interval_begin`](/documentation/os/os_signpost_interval_begin)

Marks the start of a time interval in your code using a signpost.

[`os_signpost_interval_end`](/documentation/os/os_signpost_interval_end)

Marks the end of a time interval in your code using a signpost.

[`os_signpost_event_emit`](/documentation/os/os_signpost_event_emit)

Marks a point of interest in time.

[`os_signpost_id_t`](/documentation/os/os_signpost_id_t)

An identifier you use to distinguish between signposts that have the same name and destination log.

### Trace Activities

[Collecting Log Messages in Activities](/documentation/os/collecting-log-messages-in-activities)

Find messages related to a specific user action or application event.

[os_activity_t](/documentation/os/os-activity-t)

An object that represents an activity triggered by the user.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
