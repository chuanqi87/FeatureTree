* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/usernotifications#app-main)

Framework

# User Notifications

Push user-facing notifications to the user’s device from a server, or generate them locally from your app.

iOS 10.0+iPadOS 10.0+Mac Catalyst 13.0+macOS 10.14+tvOS 10.0+visionOS 1.0+watchOS 3.0+

## [Overview](https://developer.apple.com/documentation/usernotifications\#overview)

User-facing notifications communicate important information to users of your app, regardless of whether your app is running on the user’s device. For example, a sports app can let the user know when their favorite team scores. Notifications can also tell your app to download information and update its interface. Notifications can display an alert, play a sound, or badge the app’s icon.

![A notification interface displayed on the lock screen and on the Home screen of an iOS device.](https://developer.apple.com/tutorials/images/com.apple.usernotifications/media-4182210@2x.png)

You can generate notifications locally from your app or remotely from a server that you manage. For _local notifications_, the app creates the notification content and specifies a condition, like a time or location, that triggers the delivery of the notification. For _remote notifications_, your company’s server generates push notifications, and Apple Push Notification service (APNs) handles the delivery of those notifications to the user’s devices.

Use this framework to do the following:

- Define the types of notifications that your app supports.

- Define any custom actions associated with your notification types.

- Schedule local notifications for delivery.

- Process already delivered notifications.

- Respond to user-selected actions.


The system makes every attempt to deliver local and remote notifications in a timely manner, but delivery isn’t guaranteed. The PushKit framework offers a more timely delivery mechanism for specific types of notifications, such as those VoIP and watchOS complications use. For more information, see [PushKit](https://developer.apple.com/documentation/pushkit).

For webpages in Safari version 16.0 and higher, generate remote notifications from a server that you manage using [Push API](https://www.w3.org/TR/push-api/) code that works in Safari and other browsers.

For design guidance, see [Human Interface Guidelines > Notifications](https://developer.apple.com/design/human-interface-guidelines/ios/system-capabilities/notifications/).

## [Topics](https://developer.apple.com/documentation/usernotifications\#topics)

### [Essentials](https://developer.apple.com/documentation/usernotifications\#Essentials)

[User Notifications updates](https://developer.apple.com/documentation/updates/usernotifications)

Learn about important changes in User Notifications.

[Asking permission to use notifications](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications)

Request permission to display alerts, play sounds, or badge the app’s icon in response to a notification.

### [Notification management](https://developer.apple.com/documentation/usernotifications\#Notification-management)

[`class UNUserNotificationCenter`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter)

The central object for managing notification-related activities for your app or app extension.

[`protocol UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate)

An interface for processing incoming notifications and responding to notification actions.

[`class UNNotificationSettings`](https://developer.apple.com/documentation/usernotifications/unnotificationsettings)

The object for managing notification-related settings and the authorization status of your app.

### [Remote notifications](https://developer.apple.com/documentation/usernotifications\#Remote-notifications)

Generate notifications from your company’s servers, and deliver those notifications using APNs.

[API Reference\\
Setting up a remote notification server](https://developer.apple.com/documentation/usernotifications/setting-up-a-remote-notification-server)

Generate notifications and push them to user devices.

[Sending push notifications using command-line tools](https://developer.apple.com/documentation/usernotifications/sending-push-notifications-using-command-line-tools)

Use basic macOS command-line tools to send push notifications to Apple Push Notification service (APNs).

[Testing notifications using the Push Notification Console](https://developer.apple.com/documentation/usernotifications/testing-notifications-using-the-push-notification-console)

Send test notifications and access delivery logs to test your app’s integration with Apple Push Notification service (APNs).

### [Notification requests](https://developer.apple.com/documentation/usernotifications\#Notification-requests)

Create delivery requests for local notifications, and access the content of delivered local and remote notifications.

[API Reference\\
Scheduling a notification locally from your app](https://developer.apple.com/documentation/usernotifications/scheduling-a-notification-locally-from-your-app)

Create and schedule notifications from your app when you want to get the user’s attention.

[`class UNNotificationRequest`](https://developer.apple.com/documentation/usernotifications/unnotificationrequest)

A request to schedule a local notification, which includes the content of the notification and the trigger conditions for delivery.

[`class UNNotification`](https://developer.apple.com/documentation/usernotifications/unnotification)

The data for a local or remote notification the system delivers to your app.

### [Web push notifications](https://developer.apple.com/documentation/usernotifications\#Web-push-notifications)

[Sending web push notifications in web apps and browsers](https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers)

Update your web server and website to send push notifications that work in Safari, other browsers, and web apps, following cross-browser standards.

### [Notification content](https://developer.apple.com/documentation/usernotifications\#Notification-content)

Modify and examine the payload of a notification.

[Implementing communication notifications](https://developer.apple.com/documentation/usernotifications/implementing-communication-notifications)

Configure and display your app’s communication notifications by using intents.

[`protocol UNNotificationContentProviding`](https://developer.apple.com/documentation/usernotifications/unnotificationcontentproviding)

A protocol the system uses to provide context relevant to user notifications.

[`class UNNotificationActionIcon`](https://developer.apple.com/documentation/usernotifications/unnotificationactionicon)

An icon associated with an action.

[`class UNMutableNotificationContent`](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent)

The editable content for a notification.

[`class UNNotificationContent`](https://developer.apple.com/documentation/usernotifications/unnotificationcontent)

The uneditable content of a notification.

[`class UNNotificationAttachment`](https://developer.apple.com/documentation/usernotifications/unnotificationattachment)

A media file associated with a notification.

[`class UNNotificationSound`](https://developer.apple.com/documentation/usernotifications/unnotificationsound)

The sound played upon delivery of a notification.

[`struct UNNotificationSoundName`](https://developer.apple.com/documentation/usernotifications/unnotificationsoundname)

A string providing the name of a sound file.

### [Triggers](https://developer.apple.com/documentation/usernotifications\#Triggers)

Define the trigger conditions for delivering notifications. Detect when a remote notification was delivered from APNs.

[`class UNCalendarNotificationTrigger`](https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger)

A trigger condition that causes a notification the system delivers at a specific date and time.

[`class UNTimeIntervalNotificationTrigger`](https://developer.apple.com/documentation/usernotifications/untimeintervalnotificationtrigger)

A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.

[`class UNLocationNotificationTrigger`](https://developer.apple.com/documentation/usernotifications/unlocationnotificationtrigger)

A trigger condition that causes the system to deliver a notification when the user’s device enters or exits a geographic region you specify.

[`class UNPushNotificationTrigger`](https://developer.apple.com/documentation/usernotifications/unpushnotificationtrigger)

A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.

[`class UNNotificationTrigger`](https://developer.apple.com/documentation/usernotifications/unnotificationtrigger)

The common behavior for subclasses that trigger the delivery of a local or remote notification.

### [Notification categories and user actions](https://developer.apple.com/documentation/usernotifications\#Notification-categories-and-user-actions)

Define the types of notifications that your app supports, and define how users can respond.

[Declaring your actionable notification types](https://developer.apple.com/documentation/usernotifications/declaring-your-actionable-notification-types)

Differentiate your notifications and add action buttons to the notification interface.

[`class UNNotificationCategory`](https://developer.apple.com/documentation/usernotifications/unnotificationcategory)

A type of notification your app supports and the custom actions that the system displays.

[`class UNNotificationAction`](https://developer.apple.com/documentation/usernotifications/unnotificationaction)

A task your app performs in response to a notification that the system delivers.

[`class UNTextInputNotificationAction`](https://developer.apple.com/documentation/usernotifications/untextinputnotificationaction)

An action that accepts user-typed text.

### [Notification responses](https://developer.apple.com/documentation/usernotifications\#Notification-responses)

[Handling notifications and notification-related actions](https://developer.apple.com/documentation/usernotifications/handling-notifications-and-notification-related-actions)

Respond to user interactions with the system’s notification interfaces, including handling your app’s custom actions.

[`class UNNotificationResponse`](https://developer.apple.com/documentation/usernotifications/unnotificationresponse)

The user’s response to an actionable notification.

[`class UNTextInputNotificationResponse`](https://developer.apple.com/documentation/usernotifications/untextinputnotificationresponse)

The user’s response to an actionable notification, including any custom text that the user typed or dictated.

### [Notification service app extension](https://developer.apple.com/documentation/usernotifications\#Notification-service-app-extension)

Use a notification service app extension to modify the content of a notification before it’s delivered to your app.

[Modifying content in newly delivered notifications](https://developer.apple.com/documentation/usernotifications/modifying-content-in-newly-delivered-notifications)

Modify the payload of a remote notification before it’s displayed on the user’s iOS device.

[`class UNNotificationServiceExtension`](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension)

An object that modifies the content of a remote notification before it’s delivered to the user.

### [Entitlements](https://developer.apple.com/documentation/usernotifications\#Entitlements)

[`APS Environment Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment)

The environment for push notifications.

[`APS Environment (macOS) Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.aps-environment)

The environment for push notifications in macOS apps.

### [Sample code](https://developer.apple.com/documentation/usernotifications\#Sample-code)

[Handling Communication Notifications and Focus Status Updates](https://developer.apple.com/documentation/usernotifications/handling-communication-notifications-and-focus-status-updates)

Create a richer calling and messaging experience in your app by implementing communication notifications and Focus status updates.

[Implementing Alert Push Notifications](https://developer.apple.com/documentation/usernotifications/implementing-alert-push-notifications)

Add visible alert notifications to your app by using the UserNotifications framework.

[Implementing Background Push Notifications](https://developer.apple.com/documentation/usernotifications/implementing-background-push-notifications)

Add background notifications to your app by using the UserNotifications framework.

### [Classes](https://developer.apple.com/documentation/usernotifications\#Classes)

[`class UNNotificationAttributedMessageContext`](https://developer.apple.com/documentation/usernotifications/unnotificationattributedmessagecontext)

Current page is User Notifications