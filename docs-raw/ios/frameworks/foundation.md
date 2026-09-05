* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/foundation#app-main)

Framework

# Foundation

Access essential data types, collections, and operating-system services to define the base layer of functionality for your app.

iOS 2.0+iPadOS 2.0+Mac Catalyst 13.0+macOS 10.0+tvOS 9.0+visionOS 1.0+watchOS 2.0+

## [Overview](https://developer.apple.com/documentation/foundation\#overview)

The Foundation framework provides a base layer of functionality for apps and frameworks, including data storage and persistence, text processing, date and time calculations, sorting and filtering, and networking. The classes, protocols, and data types defined by Foundation are used throughout the macOS, iOS, watchOS, and tvOS SDKs.

## [Topics](https://developer.apple.com/documentation/foundation\#topics)

### [Fundamentals](https://developer.apple.com/documentation/foundation\#Fundamentals)

[API Reference\\
Numbers, Data, and Basic Values](https://developer.apple.com/documentation/foundation/numbers-data-and-basic-values)

Work with primitive values and other fundamental types used throughout Cocoa.

[API Reference\\
Strings and Text](https://developer.apple.com/documentation/foundation/strings-and-text)

Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.

[API Reference\\
Collections](https://developer.apple.com/documentation/foundation/collections)

Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.

[API Reference\\
Dates and Times](https://developer.apple.com/documentation/foundation/dates-and-times)

Compare dates and times, and perform calendar and time zone calculations.

[API Reference\\
Units and Measurement](https://developer.apple.com/documentation/foundation/units-and-measurement)

Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.

[API Reference\\
Data Formatting](https://developer.apple.com/documentation/foundation/data-formatting)

Convert numbers, dates, measurements, and other values to and from locale-aware string representations.

[API Reference\\
Filters and Sorting](https://developer.apple.com/documentation/foundation/filters-and-sorting)

Use predicates, expressions, and sort descriptors to examine elements in collections and other services.

### [App Support](https://developer.apple.com/documentation/foundation\#App-Support)

[API Reference\\
Task Management](https://developer.apple.com/documentation/foundation/task-management)

Manage your app’s work and how it interacts with system services like Handoff and Shortcuts.

[API Reference\\
Resources](https://developer.apple.com/documentation/foundation/resources)

Access assets and other data bundled with your app.

[API Reference\\
Notifications](https://developer.apple.com/documentation/foundation/notifications)

Design patterns for broadcasting information and for subscribing to broadcasts.

[API Reference\\
App Extension Support](https://developer.apple.com/documentation/foundation/app-extension-support)

Manage the interaction between an app extension and its hosting app.

[API Reference\\
Errors and Exceptions](https://developer.apple.com/documentation/foundation/errors-and-exceptions)

Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.

[API Reference\\
Scripting Support](https://developer.apple.com/documentation/foundation/scripting-support)

Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.

### [Files and Data Persistence](https://developer.apple.com/documentation/foundation\#Files-and-Data-Persistence)

[API Reference\\
File System](https://developer.apple.com/documentation/foundation/file-system)

Create, read, write, and examine files and folders in the file system.

[API Reference\\
Archives and Serialization](https://developer.apple.com/documentation/foundation/archives-and-serialization)

Convert objects and values to and from property list, JSON, and other flat binary representations.

[API Reference\\
Settings](https://developer.apple.com/documentation/foundation/settings)

Configure your app using data you store persistently on the local disk or in iCloud.

[API Reference\\
Spotlight](https://developer.apple.com/documentation/foundation/spotlight)

Search for files and other items on the local device, and index your app’s content for searching.

[API Reference\\
iCloud](https://developer.apple.com/documentation/foundation/icloud)

Manage files and key-value data that automatically synchronize among a user’s iCloud devices.

[Optimizing Your App’s Data for iCloud Backup](https://developer.apple.com/documentation/foundation/optimizing-your-app-s-data-for-icloud-backup)

Minimize the space and time that backups take to create by excluding purgeable and nonpurgeable data from backups.

### [Networking](https://developer.apple.com/documentation/foundation\#Networking)

[API Reference\\
URL Loading System](https://developer.apple.com/documentation/foundation/url-loading-system)

Interact with URLs and communicate with servers using standard Internet protocols.

[API Reference\\
Bonjour](https://developer.apple.com/documentation/foundation/bonjour)

Advertise services for easy discovery on local networks, or discover services advertised by others.

### [Low-Level Utilities](https://developer.apple.com/documentation/foundation\#Low-Level-Utilities)

[API Reference\\
XPC](https://developer.apple.com/documentation/foundation/xpc)

Manage secure interprocess communication.

[API Reference\\
Object Runtime](https://developer.apple.com/documentation/foundation/object-runtime)

Get low-level support for basic Objective-C features, Cocoa design patterns, and Swift integration.

[API Reference\\
Processes and Threads](https://developer.apple.com/documentation/foundation/processes-and-threads)

Manage your app’s interaction with the host operating system and other processes, and implement low-level concurrency features.

[API Reference\\
Streams, Sockets, and Ports](https://developer.apple.com/documentation/foundation/streams-sockets-and-ports)

Use low-level Unix features to manage input and output among files, processes, and the network.

### [Reference](https://developer.apple.com/documentation/foundation\#Reference)

[API Reference\\
Foundation Enumerations](https://developer.apple.com/documentation/foundation/foundation-enumerations)

[API Reference\\
Foundation Data Types](https://developer.apple.com/documentation/foundation/foundation-data-types)

This document describes the data types and constants found in the Foundation framework.

### [Classes](https://developer.apple.com/documentation/foundation\#Classes)

[`class ProgressManager`](https://developer.apple.com/documentation/foundation/progressmanager)

An object that conveys ongoing progress to the user for a specified task.

Beta

[`class ProgressReporter`](https://developer.apple.com/documentation/foundation/progressreporter)

ProgressReporter is a wrapper for ProgressManager that carries information about ProgressManager.

Beta

### [Protocols](https://developer.apple.com/documentation/foundation\#Protocols)

[`protocol NSPredicateValidating`](https://developer.apple.com/documentation/foundation/nspredicatevalidating)

### [Structures](https://developer.apple.com/documentation/foundation\#Structures)

[`struct Subprogress`](https://developer.apple.com/documentation/foundation/subprogress)

Subprogress is used to establish parent-child relationship between two instances of `ProgressManager`.

Beta

Current page is Foundation