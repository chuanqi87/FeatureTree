# FCM Architectural Overview

FCM relies on the following set of components that build, transport, and receive
messages:

1. Tooling to compose or build message requests. The Notifications composer
   provides a GUI-based option for creating notification requests.
   For full automation and support for all
   [message types](https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type),
   you must build message requests in a trusted
   [server environment](https://firebase.google.com/docs/cloud-messaging/server)
   that supports the Firebase Admin SDK or the FCM server protocol.
   This environment could be Cloud Functions for Firebase, App Engine,
   or your own app server.

   ![A diagram of the three architecture layers described in this page.](/static/docs/cloud-messaging/images/diagram-FCM.png)
2. The FCM backend, which (among other functions) accepts message requests,
   performs fanout of messages via topics, and generates message metadata such
   as the message ID.
3. A platform-level transport layer, which routes the message to the targeted
   device, handles message delivery, and applies platform-specific
   configuration where appropriate. This transport layer includes:

   * Android transport layer (ATL) for Android devices with Google Play services
   * Apple Push Notification service (APNs) for Apple devices
   * Web push protocol for web apps

     **Note:** Platform-level transport layers are outside the core FCM
     product. FCM messages routed to a platform-level transport layer
     may be subject to terms specific to that platform rather than FCM’s terms
     of service. Android message routing via ATL falls under the
     [Google APIs terms of service](https://www.google.com/url?q=https://developers.google.com/terms/&sa=D&ust=1558536676246000&usg=AFQjCNFrlRMLv51d1S9NkWxD0IoYSqJ2Ng).
4. The FCM SDK on the user’s device, where the notification is displayed or
   the message is handled according to the app’s foreground/background state
   and any relevant application logic.

## Lifecycle flow

* **Register devices to receive messages from FCM**. An instance of a client app registers to receive messages, obtaining a registration token that uniquely identifies the app instance.
* **Send and receive downstream messages**.
  + Send a message. The app server sends messages to the client app:
    1. The message is composed, either in the Notifications composer or a trusted environment, and a message request is sent to the FCM backend.
    2. The FCM backend receives the message request, generates a message ID and other metadata, and sends it to the platform specific transport layer.
    3. When the device is online, the message is sent via the platform-specific transport layer to the device.
    4. On the device, the client app receives the message or notification.
