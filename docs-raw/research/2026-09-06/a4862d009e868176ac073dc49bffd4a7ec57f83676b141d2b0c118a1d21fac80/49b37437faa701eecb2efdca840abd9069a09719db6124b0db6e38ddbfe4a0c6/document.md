# Installs

For a list of [methods](https://developers.google.com/android/work/play/emm-api/v1/installs#methods) for this resource, see the end of this page.

## Resource representations

The existence of an Installs resource indicates that an app is installed on a particular device (or that an install is pending).   
  
 The API can be used to create an install resource using the [update](https://developers.google.com/android/work/play/emm-api/v1/installs/update) method. This triggers the actual install of the app on the device. If the user does not already have an entitlement for the app, then an attempt is made to create one. If this fails (for example, because the app is not free and there is no available license), then the creation of the install fails.   
  
 The API can also be used to update an installed app. If the [update](https://developers.google.com/android/work/play/emm-api/v1/installs/update) method is used on an existing install, then the app will be updated to the latest available version.   
  
 Note that it is not possible to force the installation of a specific version of an app: the version code is read-only.   
  
 If a user installs an app themselves (as permitted by the enterprise), then again an install resource and possibly an entitlement resource are automatically created.   
  
 The API can also be used to delete an install resource, which triggers the removal of the app from the device. Note that deleting an install does not automatically remove the corresponding entitlement, even if there are no remaining installs. The install resource will also be deleted if the user uninstalls the app themselves.

```
{
  "kind": "androidenterprise#install",
  "productId": string,
  "versionCode": integer,
  "installState": string
}
```



| Property name | Value | Description | Notes |
| --- | --- | --- | --- |
| `installState` | `string` | Install state. The state `"installPending"` means that an install request has recently been made and download to the device is in progress. The state `"installed"` means that the app has been installed. This field is read-only.   Acceptable values are:  * "`installPending`" * "`installed`" |  |
| `kind` | `string` |  |  |
| `productId` | `string` | The ID of the product that the install is for. For example, `"app:com.google.android.gm"`. |  |
| `versionCode` | `integer` | The version of the installed product. Guaranteed to be set only if the install state is `"installed"`. |  |

## Methods

[delete](https://developers.google.com/android/work/play/emm-api/v1/installs/delete)
:   Requests to remove an app from a device. A call to `get` or
    `list` will still show the app as installed on the device until
    it is actually removed.

[get](https://developers.google.com/android/work/play/emm-api/v1/installs/get)
:   **Deprecated:** New integrations cannot use this method and can refer to
    our  [new
    recommendations](https://developers.google.com/android/work/deprecations#recommended_alternative_3).  
    **This method will no longer be accessible by
    anyone after September 30, 2025.**
    Retrieves details of an installation of an app on a device.

[list](https://developers.google.com/android/work/play/emm-api/v1/installs/list)
:   **Deprecated:** New integrations cannot use this method and can refer to
    our  [new
    recommendations](https://developers.google.com/android/work/deprecations#recommended_alternative_3).  
    **This method will no longer be accessible by
    anyone after September 30, 2025.**
    Retrieves the details of all apps installed on the specified device.

[update](https://developers.google.com/android/work/play/emm-api/v1/installs/update)
:   **Deprecated:** New integrations cannot use this method and can refer to
    our  [new
    recommendations](https://developers.google.com/android/work/deprecations#recommended_alternative_3).  
    **This method will no longer be accessible by
    anyone after September 30, 2025.**
    Requests to install the latest version of an app to a device. If the app
    is already installed, then it is updated to the latest version if
    necessary.
