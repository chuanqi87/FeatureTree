# CloudKit JS

Provide access from your web app to your CloudKit app’s containers and databases.

## Overview

Use CloudKit JS to build a web interface that lets users access the same public and private databases as your CloudKit app running on iOS or macOS. You must have an existing CloudKit app and enable web services to use CloudKit JS.

### Before You Begin

Set up your app’s containers and configure CloudKit JS.

1. Create your app’s containers and schema.
   
   If you’re new to CloudKit, start by reading [CloudKit Quick Start](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014987). You’ll use Xcode to create your app’s containers and use CloudKit Dashboard to view the containers. Then create an iOS or Mac app that uses CloudKit to store your app’s data.
2. In CloudKit Dashboard, enable web services by creating either an API token or server-to-server key.
   
   Use an API Token from a website or an embedded web view in a native app, or when you need to authenticate the user. To create an API token, read <doc://com.apple.documentation/documentation/CloudKit/obtaining-an-api-token-for-an-icloud-container>.
   
   Use a server-to-server key to access the public database from a server process or script as an administrator. To create a server-to-server key, read [Accessing CloudKit Using a Server-to-Server Key](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/SettingUpWebServices.html#//apple_ref/doc/uid/TP40015240-CH24-SW6) in [CloudKit Web Services Reference](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240). See [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript) ](https://developer.apple.com/library/archive/samplecode/CloudAtlas/Introduction/Intro.html#//apple_ref/doc/uid/TP40014599) for a JavaScript sample that uses a server-to-server key.
3. Embed CloudKit JS in your webpage.
   
   Embed CloudKit JS in your webpage using the `script` tag and link to Apple’s hosted version of CloudKit JS at `https://cdn.apple-CloudKit.com/ck/2/CloudKit.js`.
   
   ```javascript
   <script src="https://cdn.apple-CloudKit.com/ck/2/CloudKit.js">
   ```

> Note:
> The CloudKit JS version number is in the URL. For example, `2` specifies CloudKit JS 2.0.
4. Enable JavaScript strict mode.
   
   To enable strict mode for an entire script, put “use strict” before any other statements.
   
   ```javascript
   "use strict";
   ```
5. Configure CloudKit JS.
   
   Use the `CloudKit`.[`configure`](/documentation/CloudKitJS/CloudKit/configure) method to provide information about your app’s containers to CloudKit JS. Also, specify whether to use the development or production environment. See [`CloudKit`](/documentation/CloudKitJS/CloudKit) for an example, and see [CloudKit JS Data Types](/documentation/CloudKitJS/cloudkit-js-data-types) for details on the [`CloudKit.CloudKitConfig`](/documentation/CloudKitJS/CloudKit.CloudKitConfig) properties you can set.

Now you can use the `CloudKit`.[`getDefaultContainer`](/documentation/CloudKitJS/CloudKit/getDefaultContainer) method in your JavaScript code to get the app container ([`CloudKit.Container`](/documentation/CloudKitJS/CloudKit.Container)) and its database objects ([`CloudKit.Database`](/documentation/CloudKitJS/CloudKit.Database)).

### Next Steps

To learn CloudKit JS, download the [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript) ](https://developer.apple.com/library/archive/samplecode/CloudAtlas/Introduction/Intro.html#//apple_ref/doc/uid/TP40014599) sample code project and refer to the CloudKit JS class reference documents for API details. For the hosted version of this sample code project, which allows you to execute CloudKit JS code and see the CloudKit server responses, go to [CloudKit Catalog](https://cdn.apple-CloudKit.com/CloudKit-catalog/).

The following resources provide more information about CloudKit:

- [CloudKit Quick Start](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014987) gets you started creating a CloudKit native app.
- [`CloudKit`](/documentation/CloudKitJS/CloudKit) teaches you how to write native app code.
- [CloudKit Web Services Reference](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240) describes the HTTP interface to CloudKit containers and databases.
- [iCloud Design Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/Introduction.html#//apple_ref/doc/uid/TP40012094) provides an overview of all the iCloud services available to apps submitted to the App Store or Mac App Store.

## Topics

### Classes

[`CloudKit`](/documentation/CloudKitJS/CloudKit)

Use the `CloudKit` namespace to configure CloudKit JS, and to access app containers and global constants.

[`CloudKit.CKError`](/documentation/CloudKitJS/CloudKit.CKError)

A [`CloudKit.CKError`](/documentation/CloudKitJS/CloudKit.CKError) object encapsulates an error that may occur when you use CloudKit JS. This includes CloudKit server errors and local errors.

[`CloudKit.Container`](/documentation/CloudKitJS/CloudKit.Container)

A [`CloudKit.Container`](/documentation/CloudKitJS/CloudKit.Container) object provides access to an app container, and through the app container, access to its databases. It also contains methods for authenticating and fetching users.

[`CloudKit.Database`](/documentation/CloudKitJS/CloudKit.Database)

A [`CloudKit.Database`](/documentation/CloudKitJS/CloudKit.Database) object represents a public or private database in an app container.

[`CloudKit.DatabaseChangesResponse`](/documentation/CloudKitJS/CloudKit.DatabaseChangesResponse)

A [`CloudKit.DatabaseChangesResponse`](/documentation/CloudKitJS/CloudKit.DatabaseChangesResponse) object encapsulates the results of fetching changed record zones in a database.

[`CloudKit.Notification`](/documentation/CloudKitJS/CloudKit.Notification)

A [`CloudKit.Notification`](/documentation/CloudKitJS/CloudKit.Notification) object represents a push notification that was sent to your app. Notifications are triggered by subscriptions that you save to the database. To subscribe to record changes and handle push notifications, see the `saveSubscription` method in [`CloudKit.Database`](/documentation/CloudKitJS/CloudKit.Database).

[`CloudKit.QueryNotification`](/documentation/CloudKitJS/CloudKit.QueryNotification)

A [`CloudKit.QueryNotification`](/documentation/CloudKitJS/CloudKit.QueryNotification) object represents a push notification that was generated by a subscription object. A query notification is triggered by subscriptions where the `subscriptionType` key is `query`. Use a [`CloudKit.QueryNotification`](/documentation/CloudKitJS/CloudKit.QueryNotification) object to get information about the record that changed. To create query subscriptions and handle push notifications, see the [`saveSubscriptions`](/documentation/CloudKitJS/CloudKit.Database/saveSubscriptions) method in [`CloudKit.Database`](/documentation/CloudKitJS/CloudKit.Database).

[`CloudKit.QueryResponse`](/documentation/CloudKitJS/CloudKit.QueryResponse)

A [`CloudKit.QueryResponse`](/documentation/CloudKitJS/CloudKit.QueryResponse) object encapsulates the results of using a query to fetch records

[`CloudKit.RecordInfosResponse`](/documentation/CloudKitJS/CloudKit.RecordInfosResponse)

A [`CloudKit.RecordInfosResponse`](/documentation/CloudKitJS/CloudKit.RecordInfosResponse) object encapsulates the results of fetching information about records in general and shared records in particular.

[`CloudKit.RecordsBatchBuilder`](/documentation/CloudKitJS/CloudKit.RecordsBatchBuilder)

A [`CloudKit.RecordsBatchBuilder`](/documentation/CloudKitJS/CloudKit.RecordsBatchBuilder) object encapsulates the results of changes to multiple records in a single database operation.

[`CloudKit.RecordsResponse`](/documentation/CloudKitJS/CloudKit.RecordsResponse)

A [`CloudKit.RecordsResponse`](/documentation/CloudKitJS/CloudKit.RecordsResponse) object encapsulates the results of fetching records.

[`CloudKit.RecordZoneChangesResponse`](/documentation/CloudKitJS/CloudKit.RecordZoneChangesResponse)

The [`CloudKit.RecordZoneChangesResponse`](/documentation/CloudKitJS/CloudKit.RecordZoneChangesResponse) object encapsulates the results of fetching changes to one or more record zones.

[`CloudKit.RecordZoneNotification`](/documentation/CloudKitJS/CloudKit.RecordZoneNotification)

A [`CloudKit.RecordZoneNotification`](/documentation/CloudKitJS/CloudKit.RecordZoneNotification) object represents a push notification that was caused by changes to the contents of a record zone. A zone notification is triggered by subscriptions where the `subscriptionType` key is `zone`. Use a [`CloudKit.RecordZoneNotification`](/documentation/CloudKitJS/CloudKit.RecordZoneNotification) object to get information about the record that changed. To create zone subscriptions and handle push notifications, see the [`saveSubscriptions`](/documentation/CloudKitJS/CloudKit.Database/saveSubscriptions) method in [`CloudKit.Database`](/documentation/CloudKitJS/CloudKit.Database).

[`CloudKit.RecordZonesResponse`](/documentation/CloudKitJS/CloudKit.RecordZonesResponse)

A [`CloudKit.RecordZonesResponse`](/documentation/CloudKitJS/CloudKit.RecordZonesResponse) object encapsulates the results of database operations on a record zone.

[`CloudKit.Response`](/documentation/CloudKitJS/CloudKit.Response)

The [`CloudKit.Response`](/documentation/CloudKitJS/CloudKit.Response) class is an abstract superclass for subclasses that encapsulate the response from server requests. Don’t create instances of this class. Instances of subclasses are returned by methods in the [`CloudKit.Container`](/documentation/CloudKitJS/CloudKit.Container) and [`CloudKit.Database`](/documentation/CloudKitJS/CloudKit.Database) classes. Most of these methods return a `Promise` object that resolves to a subclass of [`CloudKit.Response`](/documentation/CloudKitJS/CloudKit.Response) if the operation is successful.

[`CloudKit.ShareRecordType`](/documentation/CloudKitJS/CloudKit.ShareRecordType)

Display information about the record type of a shared record.

[`CloudKit.SubscriptionsResponse`](/documentation/CloudKitJS/CloudKit.SubscriptionsResponse)

A [`CloudKit.SubscriptionsResponse`](/documentation/CloudKitJS/CloudKit.SubscriptionsResponse) object encapsulates the results of database operations on subscriptions.

[`CloudKit.UserIdentitiesResponse`](/documentation/CloudKitJS/CloudKit.UserIdentitiesResponse)

A [`CloudKit.UserIdentitiesResponse`](/documentation/CloudKitJS/CloudKit.UserIdentitiesResponse) object encapsulates the results of fetching user identities.

### Reference

[CloudKit JS Data Types](/documentation/CloudKitJS/cloudkit-js-data-types)

This document describes the CloudKit JS data types that are not described in individual class reference documents.

[CloudKit JS Enumerations](/documentation/CloudKitJS/cloudkit-js-enumerations)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
