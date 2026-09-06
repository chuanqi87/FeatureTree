# Quickstart

To get started with the Android Management API, we've created a **Colab**
notebook that you can follow to enroll an enterprise, create a policy, and
provision a device.

**Colab** is a free cloud service offered by Google.
Colab notebooks can be used to store and run code samples, and are compatible
with Google Drive.

To use the quickstart guide, you need:

* An Android 6.0+ device.
* A Gmail account. This account cannot be associated with an existing
  enterprise.
* A [Cloud Platform](https://console.cloud.google.com/project) project that you
  own or can edit:
  1. Go to the [Projects Page](https://console.cloud.google.com/project).
  2. Click **CREATE PROJECT**.
  3. Take note of the project ID.
* Request initial [device quota](https://developers.google.com/android/management/permissible-usage#quotas_and_restrictions).

[Open quickstart guide](https://colab.research.google.com/github/google/android-management-api-samples/blob/master/notebooks/quickstart.ipynb)

## Cleanup (optional)

To reset your device and unbind your Gmail account from the `enterprise` you
created, follow these steps:

### 1. Deprovision a device

Before you can deprovision a device, you need the device's `deviceId`. To get a
list of all your provisioned devices, call `enterprises.devices.list` and
specify:

* `parent`: The enterprise name in the form of `enterprises/{enterprise-id}`.

A successful response contains an array of [`devices`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices)
resources. Because you only need the `name` field to deprovision a device, the
example response here is shortened.

```
{
  "devices": [
    {
      "name": "enterprises/{enterprise-id}/devices/{device-id}",
      "state": "ACTIVE",
      // Additional device resource fields
    }
  ]
}
```

To deprovision and factory-reset a device, call `enterprises.devices.delete` and
specify:

* `name`: The device ID in the form of
  `enterprises/{enterprise-id}/devices/{device-id}`.

If successful, the request returns an empty response body.

### 2. Delete an enterprise

You can only associate your Gmail account with a single enterprise. To unbind
your account from an enterprise, you need to delete the enterprise:

1. Visit [play.google.com/work](https://play.google.com/work) with the account
   used to create the enterprise.
2. Select **Admin Settings**.
3. In Organization information, select the three vertical dots.
4. Click **Delete Organization**.

You can now use your Gmail account to create another
enterprise.


## Start developing

* For more detailed information on how to develop an Android management
  solution, review the [Introduction](https://developers.google.com/android/management/introduction),
  [Developer's guide](https://developers.google.com/android/management/create-enterprise),
  [API reference](https://developers.google.com/android/management/reference/rest) and
  [Permissible Usage guidelines](https://developers.google.com/android/management/permissible-usage).
* Download the Android Management API client library for
  [Java](https://developers.google.com/api-client-library/java/apis/androidmanagement/v1),
  [.NET](https://developers.google.com/api-client-library/dotnet/apis/androidmanagement/v1),
  [Python](https://developers.google.com/api-client-library/python/apis/androidmanagement/v1),
  or [Ruby](https://developers.google.com/api-client-library/ruby/apis/androidmanagement/v1) (Alpha).
