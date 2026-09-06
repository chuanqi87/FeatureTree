# InstantApps

public final class **InstantApps** extends [Object](https://developer.android.com/reference/java/lang/Object.html)



**This class is deprecated.**  
Starting December 2025, Instant Apps cannot be published through Google Play, and all Google
Play services Instant APIs will no longer work. To continue optimizing for user growth, we
encourage developers to refer users to their regular app or game, and using deeplinks to
redirect them to specific journeys or features when relevant.

Entry point for Instant Apps APIs.

### Public Method Summary

|  |  |
| --- | --- |
| static [ActivityCompat](https://developers.google.com/android/reference/com/google/android/gms/instantapps/ActivityCompat) | [getActivityCompat](https://developers.google.com/android/reference/com/google/android/gms/instantapps/InstantApps#getActivityCompat(android.app.Activity))([Activity](https://developer.android.com/reference/android/app/Activity.html) activity) Returns a helper for Activity functionality that can be used to retrieve information about running instant apps or installed apps. |
| static [InstantAppsClient](https://developers.google.com/android/reference/com/google/android/gms/instantapps/InstantAppsClient) | [getInstantAppsClient](https://developers.google.com/android/reference/com/google/android/gms/instantapps/InstantApps#getInstantAppsClient(android.app.Activity))([Activity](https://developer.android.com/reference/android/app/Activity.html) activity) Creates a new instance of `InstantAppsClient` for use in an `Activity`. |
| static [InstantAppsClient](https://developers.google.com/android/reference/com/google/android/gms/instantapps/InstantAppsClient) | [getInstantAppsClient](https://developers.google.com/android/reference/com/google/android/gms/instantapps/InstantApps#getInstantAppsClient(android.content.Context))([Context](https://developer.android.com/reference/android/content/Context.html) context) Creates a new instance of `InstantAppsClient` for use in a non-activity `Context`. |
| static [Launcher](https://developers.google.com/android/reference/com/google/android/gms/instantapps/Launcher) | [getLauncher](https://developers.google.com/android/reference/com/google/android/gms/instantapps/InstantApps#getLauncher(android.content.Context))([Context](https://developer.android.com/reference/android/content/Context.html) context) Returns an API for launching instant apps by URL. |
| static [PackageManagerCompat](https://developers.google.com/android/reference/com/google/android/gms/instantapps/PackageManagerCompat) | [getPackageManagerCompat](https://developers.google.com/android/reference/com/google/android/gms/instantapps/InstantApps#getPackageManagerCompat(android.content.Context))([Context](https://developer.android.com/reference/android/content/Context.html) context) Returns a helper for PackageManager functionality that can be used to retrieve information about running instant apps or installed apps. |
| static boolean | [showInstallPrompt](https://developers.google.com/android/reference/com/google/android/gms/instantapps/InstantApps#showInstallPrompt(android.app.Activity,%20android.content.Intent,%20int,%20java.lang.String))([Activity](https://developer.android.com/reference/android/app/Activity.html) activity, [Intent](https://developer.android.com/reference/android/content/Intent.html) postInstallIntent, int requestCode, [String](https://developer.android.com/reference/java/lang/String.html) referrer) Shows a dialog that allows the user to install the current instant app. |



### Inherited Method Summary

From class java.lang.Object


|  |  |
| --- | --- |
| [Object](https://developer.android.com/reference/java/lang/Object.html) | clone() |
| boolean | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void | finalize() |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)<?> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| [String](https://developer.android.com/reference/java/lang/String.html) | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |













## Public Methods

#### public static [ActivityCompat](https://developers.google.com/android/reference/com/google/android/gms/instantapps/ActivityCompat) **getActivityCompat** ([Activity](https://developer.android.com/reference/android/app/Activity.html) activity)

Returns a helper for Activity functionality that can be used to retrieve information
about running instant apps or installed apps.

Information about instant apps will only be returned for currently running instant
apps that include the package name of the calling application in a
`<instant:uses-app>` element under the
`<application>` element in their manifest.

##### Parameters

|  |  |
| --- | --- |
| activity | the activity on which to query information. |

#### public static [InstantAppsClient](https://developers.google.com/android/reference/com/google/android/gms/instantapps/InstantAppsClient) **getInstantAppsClient** ([Activity](https://developer.android.com/reference/android/app/Activity.html) activity)

Creates a new instance of `InstantAppsClient`
for use in an `Activity`.
Error resolutions will be automatically launched from the provided Activity, displaying
UI when necessary.

#### public static [InstantAppsClient](https://developers.google.com/android/reference/com/google/android/gms/instantapps/InstantAppsClient) **getInstantAppsClient** ([Context](https://developer.android.com/reference/android/content/Context.html) context)

Creates a new instance of `InstantAppsClient`
for use in a non-activity `Context`.
Error resolutions will be automatically launched from the provided Context, displaying
system tray notifications when necessary.

#### public static [Launcher](https://developers.google.com/android/reference/com/google/android/gms/instantapps/Launcher) **getLauncher** ([Context](https://developer.android.com/reference/android/content/Context.html) context)

Returns an API for launching instant apps by URL.

This method will cache a Launcher instance for the application context; you can
invoke this method in many places in your code (without having to pass around a
Launcher interface) without incurring extra allocations.

##### Parameters

|  |  |
| --- | --- |
| context | the current context |

#### public static [PackageManagerCompat](https://developers.google.com/android/reference/com/google/android/gms/instantapps/PackageManagerCompat) **getPackageManagerCompat** ([Context](https://developer.android.com/reference/android/content/Context.html) context)

Returns a helper for PackageManager functionality that can be used to retrieve
information about running instant apps or installed apps.

This method will cache a PackageManagerCompat instance for the application context;
you can invoke this method in many places in your code (without having to pass around a
PackageManagerCompat interface) without incurring extra allocations.

##### Parameters

|  |  |
| --- | --- |
| context | the current context |

#### public static boolean **showInstallPrompt** ([Activity](https://developer.android.com/reference/android/app/Activity.html) activity, [Intent](https://developer.android.com/reference/android/content/Intent.html) postInstallIntent, int requestCode, [String](https://developer.android.com/reference/java/lang/String.html) referrer)

Shows a dialog that allows the user to install the current instant app. This method
is a no-op if the current running process is an installed app. If the app is currently
in Pre-Registration, it will allow the user to pre-register for the app and return to
the instant app upon completion. A post-install intent must be provided, which will be
used to start the application after install is complete (if applicable).

##### Parameters

|  |  |
| --- | --- |
| activity | The activity launching the dialog |
| postInstallIntent | The intent to launch after the instant app has been installed. If postInstallIntent is not provided or invalid, it falls back to the default launcher activity. |
| requestCode | The request code to pass to `Activity.startActivityForResult(Intent, int)` |
| referrer | The install referrer string |

##### Returns

* if the install prompt is successfully displayed
