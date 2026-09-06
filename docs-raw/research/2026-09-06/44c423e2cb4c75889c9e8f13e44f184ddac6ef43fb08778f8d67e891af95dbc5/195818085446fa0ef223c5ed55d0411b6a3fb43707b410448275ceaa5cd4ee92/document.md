# Example policies: Work profile devices

This page contains example policies for devices with work profiles.

## Personally-owned devices

After provisioning a [personally-owned device with a work profile](https://developers.google.com/android/management/provision-device#personally-owned_devices), Android Device Policy automatically applies policy settings to
the work profile only. This makes it possible to apply the same policy to
devices with work profiles and [fully managed devices](https://developers.google.com/android/management/policies/fully-managed-devices).

```
// Applies to the work profile.
"passwordRequirements": {
  "passwordMinimumLength": 6,
  "passwordQuality": "ALPHABETIC"
},
"applications": [{
  "defaultPermissionPolicy": "GRANT",
  "installType": "FORCE_INSTALLED",  // Auto-installs app in the work profile
  "packageName": "com.google.android.gm"
   },
  {
  "installType": "AVAILABLE",  // Adds app to the work profile's managed Play Store
  "packageName": "com.google.android.apps.docs"
}],

// Applies to the whole device.
"parentProfilePasswordRequirements": {
  "passwordMinimumLength": 4,
  "passwordQuality": "NUMERIC_COMPLEX"
}
```



## Company-owned devices

After a provisioning a [company-owned device with a work profile](https://developers.google.com/android/management/provision-device#company-owned_devices_for_work_and_personal_use),
Android Device Policy automatically applies most policy settings to the work
profile only. While the personal profile maintains user privacy, enterprises can
enforce select restrictions and settings in the personal profile and across the
whole the device.

### Work Profile Widgets

`workProfilewidgets` provides greater control for IT admins over what widgets display on the home screen of a device.
This is currently set to disallowed as default but can be allowed using the application level [`workProfileWidgets`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#workprofilewidgets) and device level [`workProfileWidgetsDefault`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#crossprofilepolicies) APIs.

### Personal usage policies

Enterprise can enforce certain restrictions in the personal profile of a
company-owned device, such as blocking the installation of specific apps,
disabling the camera, and setting a limit for how long a user can pause their
work profile. See [`personalUsagePolicies`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#personalusagepolicies)
for more information.

### Device-wide policies

The policies in this table apply to an entire device.

| Policy name |  |  |
| --- | --- | --- |
| `frpAdminEmails` | `deviceOwnerLockScreenInfo` | `systemUpdate` |
| `addUserDisabled` | `bluetoothDisabled` | `bluetoothConfigDisabled` |
| `cellBroadcastsConfigDisabled` | `mobileNetworksConfigDisabled` | `tetheringConfigDisabled` |
| `wifiConfigDisabled` | `dataRoamingDisabled` | `shareLocationDisabled` |
| `smsDisabled` | `usbFileTransferDisabled` | `autoTimeRequired` |
| `mountPhysicalMediaDisabled` | `outgoingCallsDisabled` | `setWallpaperDisabled` |
| `unmuteMicrophoneDisabled` |  |  |

### Example policy

```
// Applies to the work profile
"passwordRequirements": {
  "passwordMinimumLength": 6,
  "passwordQuality": "ALPHABETIC"
},
"applications": [{
  "defaultPermissionPolicy": "GRANT",
  "installType": "FORCE_INSTALLED",  // Auto-installs app in the work profile
  "packageName": "com.google.android.gm"
   },
  {
  "installType": "AVAILABLE",  // Adds app to the work profile's managed Play Store
  "packageName": "com.google.android.apps.docs"
}],

// Applies to the personal profile
"personalUsagePolicies": {
  "personalPlayStoreMode": "BLACKLIST",
  "personalApplicationPolicy": [{
     "packageName": "com.example.app",
     "installType": "BLOCKED"
  }],
  "maxDaysWithWorkOff": 3,
  "cameraDisabled": true,
  "screenCaptureDisabled": true
},

// Applies to the whole device.
"bluetoothDisabled": true,
"usbFileTransferDisabled": true
```



### Known Issue

On a company-owned device, retrieving and updating the personal usage policy may not be immediate (the delay should be no longer than ten minutes); until this has occured the "No result found" screen is displayed. Otherwise a user could install any app from the Play store, between phone start up and the personal usage policy being loaded and applied.

After applying a personal usage policy, wait ten minutes, then trigger a cache update (e.g. by selecting an app) and then re-open the personal Play app. The personal usage policy should then have been applied correctly.
