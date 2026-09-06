# SCPreferences

## Overview

The `SCPreferences` programming interface allows an application to load and store XML configuration data in a controlled manner and provide the necessary notifications to other applications that need to be aware of configuration changes.

To access configuration preferences, you must first establish a preferences session using the [`SCPreferencesCreate(_:_:_:)`](/documentation/SystemConfiguration/SCPreferencesCreate(_:_:_:)) function. To identify a specific set of preferences to access, you pass a value in the prefsID parameter. A `NULL` value indicates that the default system preferences are to be accessed. A string that starts with a leading “/” character specifies the absolute path to the file containing the preferences to be accessed. A string that does not start with a leading “/” character specifies a file relative to the default system preferences directory.

When you are finished with the preferences session, use the <doc://com.apple.documentation/documentation/CoreFoundation/CFRelease> function to release it.

## Topics

### Creating a Preferences Session

[`SCPreferencesCreate`](/documentation/SystemConfiguration/SCPreferencesCreate(_:_:_:))

Initiates access to the per-system set of configuration preferences.

[`SCPreferencesCreateWithAuthorization`](/documentation/SystemConfiguration/SCPreferencesCreateWithAuthorization(_:_:_:_:))

Initiates access to the per-system set of configuration preferences with the specified authorization.

### Getting Information About a Preferences Session

[`SCPreferencesGetTypeID`](/documentation/SystemConfiguration/SCPreferencesGetTypeID())

Returns the type identifier of all `SCPreferences` instances.

[`SCPreferencesCopyKeyList`](/documentation/SystemConfiguration/SCPreferencesCopyKeyList(_:))

Returns the currently defined preference keys.

[`SCPreferencesGetSignature`](/documentation/SystemConfiguration/SCPreferencesGetSignature(_:))

Returns a value that can be used to determine if the saved configuration preferences have changed.

### Adding, Getting, and Removing Values

[`SCPreferencesAddValue`](/documentation/SystemConfiguration/SCPreferencesAddValue(_:_:_:))

Associates the specified value with the specified preference key.

[`SCPreferencesGetValue`](/documentation/SystemConfiguration/SCPreferencesGetValue(_:_:))

Retrieves the value associated with the specified preference key.

[`SCPreferencesSetValue`](/documentation/SystemConfiguration/SCPreferencesSetValue(_:_:_:))

Updates the data associated with the specified preference key with the specified value.

[`SCPreferencesRemoveValue`](/documentation/SystemConfiguration/SCPreferencesRemoveValue(_:_:))

Removes the data associated with the specified preference key.

### Applying and Committing Changes

[`SCPreferencesApplyChanges`](/documentation/SystemConfiguration/SCPreferencesApplyChanges(_:))

Requests that the currently stored configuration preferences be applied to the active configuration.

[`SCPreferencesCommitChanges`](/documentation/SystemConfiguration/SCPreferencesCommitChanges(_:))

Commits changes made to the configuration preferences to persistent storage.

[`SCPreferencesSynchronize`](/documentation/SystemConfiguration/SCPreferencesSynchronize(_:))

Synchronizes accessed preferences with committed changes.

### Managing Notifications and Callbacks

[`SCPreferencesSetCallback`](/documentation/SystemConfiguration/SCPreferencesSetCallback(_:_:_:))

Assigns the specified callback to the specified preferences session.

[`SCPreferencesScheduleWithRunLoop`](/documentation/SystemConfiguration/SCPreferencesScheduleWithRunLoop(_:_:_:))

Schedules commit and apply notifications for the specified preferences session using the specified run loop and mode.

[`SCPreferencesUnscheduleFromRunLoop`](/documentation/SystemConfiguration/SCPreferencesUnscheduleFromRunLoop(_:_:_:))

Unschedules commit and apply notifications for the specified preferences session from the specified run loop and mode.

[`SCPreferencesSetDispatchQueue`](/documentation/SystemConfiguration/SCPreferencesSetDispatchQueue(_:_:))

Schedules commit and apply notifications for the specified preferences session using the specified dispatch queue.

### Managing Access to a Preferences Session

[`SCPreferencesLock`](/documentation/SystemConfiguration/SCPreferencesLock(_:_:))

Locks access to the configuration preferences.

[`SCPreferencesUnlock`](/documentation/SystemConfiguration/SCPreferencesUnlock(_:))

Releases exclusive access to the configuration preferences.

### Data Types

[`SCPreferences`](/documentation/SystemConfiguration/SCPreferences)

The handle to an open preferences session for accessing system configuration preferences.

[`SCPreferencesContext`](/documentation/SystemConfiguration/SCPreferencesContext)

A structure containing user-specified data and callbacks for accessing system configuration preferences.

[`SCPreferencesCallBack`](/documentation/SystemConfiguration/SCPreferencesCallBack)

Type of the callback function used when the preferences have been updated or applied.

### Constants

[`SCPreferencesNotification`](/documentation/SystemConfiguration/SCPreferencesNotification)

The type of notification (used with the [`SCPreferencesCallBack`](/documentation/SystemConfiguration/SCPreferencesCallBack) callback).



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
