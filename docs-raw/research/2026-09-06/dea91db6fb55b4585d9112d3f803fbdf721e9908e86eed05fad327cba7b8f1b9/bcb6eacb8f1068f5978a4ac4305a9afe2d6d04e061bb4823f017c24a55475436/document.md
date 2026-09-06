# Updating widgets with WidgetKit push notifications

Use WidgetKit to receive push tokens and reload your widgets with remote push notifications.

## Discussion

In addition to requesting a widget timeline refresh from your app, widgets can receive a push notification to refresh their data that compliments timeline updates. If data for your widget changes on your server, your widgets can receive a WidgetKit push notifications you send using the Apple Push Notification service (APNs). Use WidgetKit push notification updates in addition to timeline updates.

To update your widget with WidgetKit push notifications:

1. Add the capability to use remote push notifications to your widget extension target in Xcode.
2. Set up a remote notification server or make changes to your existing server to support WidgetKit push notifications. If you’re new to using remote push notifications, plan to spend time implementing your remote notification server. For more information, refer to <doc://com.apple.documentation/documentation/UserNotifications/registering-your-app-with-apns>.
3. Update your app to obtain push tokens, handle token updates, update or invalidate them on your remote push notification server, and use the tokens to establish a token-based connection to APNs, as described in <doc://com.apple.documentation/documentation/UserNotifications/establishing-a-token-based-connection-to-apns>.
4. Send WidgetKit push notifications from your remote notification server with APNs using the push tokens, HTTP header fields, and JSON payload to update your widget.
5. When WidgetKit receives a push notification, it reloads your timelines, similar to when you call [`reloadAllTimelines()`](/documentation/WidgetKit/WidgetCenter/reloadAllTimelines()).

> Important: Like timeline updates, the system budgets WidgetKit push notifications and delivers them opportunistically, making push updates an additional update mechanism for your widgets that doesn’t replace timeline updates.

### Add the Push Notifications capability and create a remote notification server

In your Xcode project, start by adding the Push Notifications capability to your app in Xcode as described in <doc://com.apple.documentation/documentation/UserNotifications/registering-your-app-with-apns>. Note that you can’t use the User Notifications framework to register your widget for push notifications. Instead, you use WidgetKit to obtain a push token as described below.

> Note: You can’t update widgets with broadcast push notifications you send on a channel.

### Manage push tokens and send them to your server

To update your widgets with push notifications, your app needs to receive and manage push tokens, send them to your remote notification server, and configure the widget to receive push updates.

First, create an object that conforms to the [`WidgetPushHandler`](/documentation/WidgetKit/WidgetPushHandler) protocol and that handles:

- Updates to the push tokens that allow your remote notification server to send notifications to the widget using APNs
- Changes to a person’s configured widgets; for example, when they add or remove a widget

In your widget push handler, implement the  [`pushTokenDidChange(_:widgets:)`](/documentation/WidgetKit/WidgetPushHandler/pushTokenDidChange(_:widgets:)) requirement, access the updated push token using the [`WidgetPushInfo`](/documentation/WidgetKit/WidgetPushInfo) object, and the [`WidgetInfo`](/documentation/WidgetKit/WidgetInfo) objects, and send updated information to your remote notification server as needed.

> Note: The system calls `pushTokenDidChange(_:widgets:)` for all push token updates and for the first push token you receive from WidgetKit.

The following example shows a template for the `pushTokenDidChange(_:widgets:)` requirement:

```swift
// Handle push token and widget configuration changes.
struct CaffeineTrackerPushHandler: WidgetPushHandler {
    func pushTokenDidChange(_ pushInfo: WidgetPushInfo, widgets: [WidgetInfo]) {
        // Send the push token and subscription info
        // to your remote notification server.
        // ...
    }
}
```

### Configure your widget to receive push updates

When you implement the push handler, tell WidgetKit which widget you want to update with remote push notifications by adding the handler to your <doc://com.apple.documentation/documentation/SwiftUI/WidgetConfiguration> using the <doc://com.apple.documentation/documentation/SwiftUI/WidgetConfiguration/pushHandler(_:)> API:

```swift
// Add the pushHandler to the WidgetConfiguration.
struct CaffeineTrackerWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(
            kind: Constants.widgetKind,
            provider: Provider()
        ) { entry in
            CaffeineTrackerWidgetView(entry: entry)
        }
        .configurationDisplayName("Caffeine Tracker")
        .pushHandler(CaffeineTrackerPushHandler.self)
    }
}
```

### Send the WidgetKit notification payload that updates your widget

Sending a remote push notification to your widget works the same as other remote push notifications, as described in <doc://com.apple.documentation/documentation/UserNotifications/sending-notification-requests-to-apns>. To send WidgetKit push notification updates, make sure your remote notification server constructs a JSON payload that conforms to the following requirements:

- Set the value for the `apns-push-type` header field to `widgets`.
- Set the value for the `apns-topic` header field to `<your bundleID>.push-type.widgets`.
- In your request’s `apn` dictionary, set the `content-changed` property to `true`.

The following sample shows what a POST request for a widget update might look like:

```
:method = POST
:scheme = https
:path = /3/device/<DEVICE_TOKEN>

// Request headers
host = api.sandbox.push.apple.com
apns-push-type = widgets
apns-topic = com.example.CaffeineTracker.push-type.widgets

// Request body
{
    "aps": {
        "content-changed": true,     
    }
}
```

For information about testing push notifications, refer to <doc://com.apple.documentation/documentation/UserNotifications/sending-push-notifications-using-command-line-tools> and <doc://com.apple.documentation/documentation/UserNotifications/testing-notifications-using-the-push-notification-console>.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
