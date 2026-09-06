# Android Management API

**Note:** If you use the [Google Play EMM API](https://developers.google.com/android/work/play/emm-api),
see the [guide for existing EMM partners](https://developers.google.com/android/management/existing-emms).

The Android Management API is available as part of [Android
Enterprise](https://developers.google.com/android/work), an initiative providing developers with tools to
build solutions for organizations to manage their Android device fleets. The
program is intended for enterprise mobility management providers (EMMs). To
deploy a production solution that uses the Android Management API, EMMs need to
follow the steps outlined in [Release your
solution](https://developers.google.com/android/work/release-solution).

You can use the Android Management API to support the
[work profile on personally-owned device](https://developers.google.com/android/work/requirements/work-profile),
[work profile on company-owned device](https://developers.google.com/android/work/requirements/work-profile-corporate),
[fully managed device](https://developers.google.com/android/work/requirements/fully-managed-device), and
[dedicated device](https://developers.google.com/android/work/requirements/dedicated-device) solution sets.

See the [Quickstart guide](https://developers.google.com/android/management/quickstart) to try out the API.

---



## How it works

The Android Management API supports the full enterprise mobility management
lifecycle, from initial customer enrollment to setting up and managing devices.

![EMM consoles use Android Management API to set policies on devices.](/static/android/management/images/android-management-api.png)

As an EMM developer, you supply your customers with an on-premise or cloud-based
EMM console. In your console, your customers generate device enrollment tokens
and create management policies. They use the tokens to enroll devices and apply
management policies to the devices they enrolled.

In the backend, your console uses the Android Management API to create
enrollment tokens, policies, and other management resources. During enrollment,
each device installs the API's companion app,
[Android Device Policy](https://play.google.com/store/apps/details?id=com.google.android.apps.work.clouddpc).
When policies are linked to a device in the API, Android Device Policy automatically
enforces the policy settings on the device.

**Note:** Android Device Policy is the **only** device policy controller compatible
with Android Management API.


---



## API resources

This section describes the primary resources used in the Android Management API.

### Enterprises

An [`enterprises`](https://developers.google.com/android/management/reference/rest/v1/enterprises) resource
typically represents a single organization. You [create an
enterprise](https://developers.google.com/android/management/create-enterprise) as part of an online setup flow that your
customers use to bind their organization with your EMM solution. Policies,
enrollment tokens, and devices belong to an enterprise.

### Policies

The Android Management API follows a policy-driven model. A
[`policies`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies)
resource contains a group of device and app management settings that govern the
behavior of a device. The range and flexibility of the settings supported in
`policies` allow you to set up devices for a variety of different [use
cases](https://developers.google.com/android/work/overview#android_devices_enterprise_use_cases).

See [Create a policy](https://developers.google.com/android/management/create-policy) for more information.

### Enrollment tokens

You use [`enrollmentTokens`](https://developers.google.com/android/management/reference/rest/v1/enterprises.enrollmentTokens)
to bind devices to an enterprise—a process called enrollment and provisioning.
Enrollment tokens can optionally contain extra details (e.g. corporate WiFi credentials)
, a `policyName` linked to a `policies` resource, and a user account identifier.

After [creating an enrollment token](https://developers.google.com/android/management/provision-device), you
can pass the token to a device using one of several different [provisioning
methods](https://developers.google.com/android/management/provision-device#provisioning_methods). Devices
install Android Device Policy as part of the provisioning process. If a
`policyName` is specified in the enrollment token, then the policy will be
applied immediately after provisioning is complete.

The Android Management API simplifies user management—you can enroll a device
with or without specifying a user in the enrollment token.

* If you don't specify a user, a new user will be created automatically.
* If you specify an existing user, the existing user will be associated with
  the device. You can associate a user with up to 10 devices.

See [Provision a device](https://developers.google.com/android/management/provision-device) for more
information.

### Devices

A [`devices`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices)
resource is created when a device is successfully enrolled. The resource
contains read-only details about a device, including its associated user,
policy, and management mode.

Device management is carried out through policy, but you can use
[`enterprises.devices.issueCommand`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/issueCommand)
to lock, reboot, or reset the password on a device. To wipe a device, call
[`enterprises.devices.delete`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices/delete)
.

---



## Get started

Test out the API—use the [Quickstart guide](https://developers.google.com/android/management/quickstart) to
set up a device in minutes. Ensure that you understand the steps required to
[release your solution](https://developers.google.com/android/work/release-solution) in a production
environment before using the developer's guide and [API
reference](https://developers.google.com/android/management/reference/rest) on this site to build your
solution.
