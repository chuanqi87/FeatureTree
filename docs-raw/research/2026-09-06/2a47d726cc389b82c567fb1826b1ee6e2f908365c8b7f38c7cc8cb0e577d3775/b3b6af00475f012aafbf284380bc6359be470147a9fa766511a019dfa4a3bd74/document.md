# Preferences Utilities

## Overview

Several functions return a preference value as a Core Foundation property list object.

You can use the function [`CFGetTypeID(_:)`](/documentation/CoreFoundation/CFGetTypeID(_:)) to determine the value’s type. For more information about property lists, see [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i).

### Overview

Core Foundation provides a simple, standard way to manage user (and application) preferences. Core Foundation stores preferences as key-value pairs that are assigned a scope using a combination of user name, application ID, and host (computer) names. This makes it possible to save and retrieve preferences that apply to different classes of users. Core Foundation preferences is useful to all applications that support user preferences. Note that modification of some preferences domains (those not belonging to the “Current User”) requires root privileges (or Admin privileges prior to OS X v10.6)—see [Authorization Services Programming Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000995) for information on how to gain suitable privileges.

Unlike some other Core Foundation types, CFPreferences is not toll-free bridged to its corresponding Cocoa Foundation framework class (`NSUserDefaults`). CFPreferences is thread-safe.

## Topics

### Getting Preference Values

[`CFPreferencesCopyAppValue`](/documentation/CoreFoundation/CFPreferencesCopyAppValue(_:_:))

Obtains a preference value for the specified key and application.

[`CFPreferencesCopyKeyList`](/documentation/CoreFoundation/CFPreferencesCopyKeyList(_:_:_:))

Constructs and returns the list of all keys set in the specified domain.

[`CFPreferencesCopyMultiple`](/documentation/CoreFoundation/CFPreferencesCopyMultiple(_:_:_:_:))

Returns a dictionary containing preference values for multiple keys.

[`CFPreferencesCopyValue`](/documentation/CoreFoundation/CFPreferencesCopyValue(_:_:_:_:))

Returns a preference value for a given domain.

[`CFPreferencesGetAppBooleanValue`](/documentation/CoreFoundation/CFPreferencesGetAppBooleanValue(_:_:_:))

Convenience function that directly obtains a Boolean preference value for the specified key.

[`CFPreferencesGetAppIntegerValue`](/documentation/CoreFoundation/CFPreferencesGetAppIntegerValue(_:_:_:))

Convenience function that directly obtains an integer preference value for the specified key.

### Setting Preference Values

[`CFPreferencesSetAppValue`](/documentation/CoreFoundation/CFPreferencesSetAppValue(_:_:_:))

Adds, modifies, or removes a preference.

[`CFPreferencesSetMultiple`](/documentation/CoreFoundation/CFPreferencesSetMultiple(_:_:_:_:_:))

Convenience function that allows you to set and remove multiple preference values.

[`CFPreferencesSetValue`](/documentation/CoreFoundation/CFPreferencesSetValue(_:_:_:_:_:))

Adds, modifies, or removes a preference value for the specified domain.

### Synchronizing Preferences

[`CFPreferencesAppSynchronize`](/documentation/CoreFoundation/CFPreferencesAppSynchronize(_:))

Writes to permanent storage all pending changes to the preference data for the application, and reads the latest preference data from permanent storage.

[`CFPreferencesSynchronize`](/documentation/CoreFoundation/CFPreferencesSynchronize(_:_:_:))

For the specified domain, writes all pending changes to preference data to permanent storage, and reads latest preference data from permanent storage.

### Adding and Removing Suite Preferences

[`CFPreferencesAddSuitePreferencesToApp`](/documentation/CoreFoundation/CFPreferencesAddSuitePreferencesToApp(_:_:))

Adds suite preferences to an application’s preference search chain.

[`CFPreferencesRemoveSuitePreferencesFromApp`](/documentation/CoreFoundation/CFPreferencesRemoveSuitePreferencesFromApp(_:_:))

Removes suite preferences from an application’s search chain.

### Miscellaneous Functions

[`CFPreferencesAppValueIsForced`](/documentation/CoreFoundation/CFPreferencesAppValueIsForced(_:_:))

Determines whether or not a given key has been imposed on the user.

[`CFPreferencesCopyApplicationList`](/documentation/CoreFoundation/CFPreferencesCopyApplicationList(_:_:))

Constructs and returns the list of all applications that have preferences in the scope of the specified user and host.

### Constants

[Application, Host, and User Keys](/documentation/CoreFoundation/application-host-and-user-keys)

Keys used to specify the common preference domains.

## See Also

  [Preferences Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPreferences/CFPreferences.html#//apple_ref/doc/uid/10000129i)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
