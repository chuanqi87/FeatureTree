# Set up EMM notifications

Google Play generates notifications, referred to as **EMM notifications**, in
response to various events that affect an enterprise. For example, when an app
is approved, the system sends a `ProductApprovalEvent` notification.

EMM notifications are associated with a specific [enterprise service account
(ESA)](https://developers.google.com/android/work/overview#service_accounts). As an EMM, you can set up your
console to display alerts or messages to enterprise IT administrators based on
the notifications that you receive.

EMM notifications are sent using [Google Cloud
Pub/Sub](https://cloud.google.com/pubsub/overview). For detailed information on how to
set up a Pub/Sub notifications, see the [Subscriber
Overview](https://cloud.google.com/pubsub/docs/subscriber) and [Pull Subscriber
Guide](https://cloud.google.com/pubsub/docs/pull).

To confirm that you have successfully set up your system to receive EMM
notifications from Google Play and to retrieve the name of the Cloud Pub/Sub
topic that you need to connect your subscription to, call
[`Enterprises.sendTestPushNotification`](https://developers.google.com/android/work/play/emm-api/v1/enterprises/sendTestPushNotification).

Sending a test notification validates your EMM integration with the Google Cloud
Pub/Sub service for the enterprise. If EMM notifications are properly
configured, the API returns the following:

```
    {
        topic_name: "/projects/project-name/topics/play-work-012345",
        message_id: "128976912439"
    }
```



## Pull notifications

Google Cloud Pub/Sub supports two different notification mechanisms: pull and
push. However, only pull notifications are recommended. The pull approach
doesn't require any external server setup, and works with both programmatically
and manually created ESAs. Another advantage of pull notifications is that they
require little to no additional configuration or maintenance by your customers.
use
[`Enterprises.pullNotificationSet`](https://developers.google.com/android/work/play/emm-api/v1/enterprises/pullNotificationSet)
and
[`Enterprises.acknowledgeNotificationSet`](https://developers.google.com/android/work/play/emm-api/v1/enterprises/acknowledgeNotificationSet)
to receive and acknowledge EMM notifications over long-running outgoing
connections.

When calling
[`Enterprises.pullNotificationSet`](https://developers.google.com/android/work/play/emm-api/v1/enterprises/pullNotificationSet),
we recommend leaving the `requestMode` to its default value
(`waitForNotifications`). This causes the request to wait until one or more
notifications are present before returning a response. If no notifications are
present after some time, the request returns an empty notification list, after
which you can try the request again.

After you receive notifications, call
[`Enterprises.acknowledgeNotificationSet`](https://developers.google.com/android/work/play/emm-api/v1/enterprises/acknowledgeNotificationSet)
to ensure that the same notifications aren't returned the next time you call
`Enterprises.pullNotificationSet`.

You also have the option of setting `requestMode` to `returnImmediately` when
calling `Enterprises.pullNotificationSet`. You'll receive a response to the
request immediately, containing any pending notifications or an empty list if no
notifications are present. This `requestMode` option may be useful when you
initially test your notifications implementation.

## Examples of EMM notifications

Here are some examples of events and the notification types that they generate:

**Note:** The following notification types have been deprecated:
`ProductApprovalEvent`, `AppUpdateEvent`, `NewPermissionsEvent`,
`AppRestrictionsSchemaChangeEvent`, `ProductAvailabilityChangeEvent`, and
`NewDeviceEvent`. For `AppUpdateEvent`, you must use
 [high-priority update mode](https://developers.google.com/android/work/play/emm-api/update)  as
per our recommendations.

| Description | Notification |
| --- | --- |
| A test notification is requested via the [Google Play EMM API](https://developers.google.com/android/work/play/emm-api/v1/enterprises/sendTestPushNotification). You need to send a test notification to confirm that your system can receive the notifications that Google Play publishes, and to learn the topic name used for all notifications associated with Google Play. | `TestPushNotification` |
| A newly provisioned device is ready to be managed by the [Google Play EMM API](https://developers.google.com/android/work/play/emm-api/v1). You can now call APIs that require the device’s `deviceId` ([Installs](https://developers.google.com/android/work/play/emm-api/v1/installs), for example) and APIs that return a [Devices](https://developers.google.com/android/work/play/emm-api/v1/devices) resource. This notification is only sent after the first account is provisioned on a managed device. **DEPRECATED** | `NewDeviceEvent` |
| An administrator marks an application as approved or unapproved in the managed Google Play console. **DEPRECATED** | `ProductApprovalEvent` |
| A pending installation to a device times out. For example, a push install request is accepted, but the device is not reachable for several days, so the install cannot be confirmed. The system sends an install timeout notification. | `InstallFailureEvent` |
| A new version of an app is published. The update is available to one or more, but not necessarily all, devices. **DEPRECATED** | `AppUpdateEvent` |
| An app update requires a new permission to be approved by the admin, so that an update or a new install can occur. This notification is sent when the application’s accepted permission set differs from the application’s requested permissions set. **DEPRECATED** | `NewPermissionsEvent` |
| A new version of an app is published that includes a new or modified [managed configurations schema](https://developer.android.com/work/managed-configurations.html#%0Adefine-configuration). When a developer uploads a new APK, Google Play compares the schema in the manifest to the schema in the previous version of the app. If the schema has changed, it notifies enterprises that have approved the app. **DEPRECATED** | `AppRestrictionsSchemaChangeEvent` |
| An available app becomes unavailable, or an unavailable app is re-added to Google Play. The availability of the app changes if a developer unpublishes it, or it is removed from Google Play. The availability also changes if an unavailable app is re-added to Google Play. **DEPRECATED** | `ProductAvailabilityChangeEvent` |
| A notification related to an enterprise upgrade. An enterprise upgrade is a process that upgrades a managed Google Play Accounts enterprise to a managed Google Domain. | `EnterpriseUpgradeEvent` |
