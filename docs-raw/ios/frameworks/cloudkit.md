* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/cloudkit#app-main)

Framework

# CloudKit

Store structured app and user data in iCloud containers that all users of your app can share.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.0+macOS 10.10+tvOS 9.0+visionOS 1.0+watchOS 3.0+

## [Overview](https://developer.apple.com/documentation/cloudkit\#overview)

The CloudKit framework provides interfaces for moving data between your app and your iCloud containers. You use CloudKit to store your app’s existing data in the cloud so that the user can access it on multiple devices. You can also store data in a public area where all users can access it.

### [Using the CloudKit framework](https://developer.apple.com/documentation/cloudkit\#Using-the-CloudKit-framework)

CloudKit isn’t a replacement for your app’s existing data objects. Instead, CloudKit provides complementary services for managing the transfer of data to and from iCloud servers. Because it provides minimal offline caching support, CloudKit relies on the presence of the network and, optionally, a valid iCloud account. A valid iCloud account is only necessary when you want to save data that is specific to a single user. Apps can always store data in a public area that is readable by all users.

Records are at the heart of all data transactions in CloudKit. A record is a dictionary of key-value pairs that represents the data you want to save. You can add new keys and values to records at any time, and you can create links between related records to organize your data. The [`CKRecord`](https://developer.apple.com/documentation/cloudkit/ckrecord) class defines the interfaces for managing the contents of records. CloudKit also relies heavily on the use of [`Operation`](https://developer.apple.com/documentation/foundation/operation) objects to manage the asynchronous transfer of data to and from the server.

Before using CloudKit, make sure it’s the most suitable option for your app. For more information, see [Deciding whether CloudKit is right for your app](https://developer.apple.com/documentation/cloudkit/deciding-whether-cloudkit-is-right-for-your-app).

## [Topics](https://developer.apple.com/documentation/cloudkit\#topics)

### [Essentials](https://developer.apple.com/documentation/cloudkit\#Essentials)

[Deciding whether CloudKit is right for your app](https://developer.apple.com/documentation/cloudkit/deciding-whether-cloudkit-is-right-for-your-app)

Explore the various options you have for using iCloud to store and sync your app’s data.

[Enabling CloudKit in Your App](https://developer.apple.com/documentation/cloudkit/enabling-cloudkit-in-your-app)

Configure your app to store data in iCloud using CloudKit.

### [Schemas](https://developer.apple.com/documentation/cloudkit\#Schemas)

[Designing and Creating a CloudKit Database](https://developer.apple.com/documentation/cloudkit/designing-and-creating-a-cloudkit-database)

Create a schema to store your app’s objects as records in iCloud using CloudKit.

[API Reference\\
Managing iCloud Containers with CloudKit Database App](https://developer.apple.com/documentation/cloudkit/managing-icloud-containers-with-cloudkit-database-app)

Inspect and modify the schema and data for your app’s iCloud container.

[`class CKRecordZone`](https://developer.apple.com/documentation/cloudkit/ckrecordzone)

A database partition that contains related records.

[`class CKRecord`](https://developer.apple.com/documentation/cloudkit/ckrecord)

A collection of key-value pairs that store your app’s data.

[`class Reference`](https://developer.apple.com/documentation/cloudkit/ckrecord/reference)

A relationship between two records in a record zone.

[`class CKAsset`](https://developer.apple.com/documentation/cloudkit/ckasset)

An external file that belongs to a record.

[Integrating a Text-Based Schema into Your Workflow](https://developer.apple.com/documentation/cloudkit/integrating-a-text-based-schema-into-your-workflow)

Define and update your schema with the CloudKit Schema Language.

### [Records](https://developer.apple.com/documentation/cloudkit\#Records)

[API Reference\\
Local Records](https://developer.apple.com/documentation/cloudkit/local-records)

Manipulate records on-device and save changes to the server.

[API Reference\\
Remote Records](https://developer.apple.com/documentation/cloudkit/remote-records)

Use subscriptions and change tokens to efficiently manage modifications to remote records.

[`class CKSyncEngine`](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5)

An object that manages the synchronization of local and remote record data.

[API Reference\\
Shared Records](https://developer.apple.com/documentation/cloudkit/shared-records)

Share one or more records with other iCloud users.

### [User discovery](https://developer.apple.com/documentation/cloudkit\#User-discovery)

[`class CKUserIdentity`](https://developer.apple.com/documentation/cloudkit/ckuseridentity)

The identity of a user.

[`class LookupInfo`](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo-swift.class)

The criteria to use when searching for discoverable iCloud users.

### [Core objects](https://developer.apple.com/documentation/cloudkit\#Core-objects)

[`class CKContainer`](https://developer.apple.com/documentation/cloudkit/ckcontainer)

A conduit to your app’s databases.

[`class CKDatabase`](https://developer.apple.com/documentation/cloudkit/ckdatabase)

An object that represents a collection of record zones and subscriptions.

[`class CKOperationGroup`](https://developer.apple.com/documentation/cloudkit/ckoperationgroup)

An explicit association between two or more operations.

### [Privacy](https://developer.apple.com/documentation/cloudkit\#Privacy)

[Encrypting User Data](https://developer.apple.com/documentation/cloudkit/encrypting-user-data)

Deploy industry-standard security technologies using CloudKit encryption.

[Providing User Access to CloudKit Data](https://developer.apple.com/documentation/cloudkit/providing-user-access-to-cloudkit-data)

Provide users access to the data your app stores on their behalf.

[Changing Access Controls on User Data](https://developer.apple.com/documentation/cloudkit/changing-access-controls-on-user-data)

Restrict access to or remove restrictions from a user’s data at their request.

[`class CKFetchWebAuthTokenOperation`](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation)

An operation that creates an authentication token for use with CloudKit web services.

[Responding to Requests to Delete Data](https://developer.apple.com/documentation/cloudkit/responding-to-requests-to-delete-data)

Provide options for users to delete their CloudKit data from your app.

[Identifying an App’s Containers](https://developer.apple.com/documentation/cloudkit/identifying-an-app-s-containers)

Use Xcode’s Project navigator to find the identifiers of active CloudKit containers.

### [Errors](https://developer.apple.com/documentation/cloudkit\#Errors)

[`let CKErrorDomain: String`](https://developer.apple.com/documentation/cloudkit/ckerrordomain)

The error domain for CloudKit errors.

[`struct CKError`](https://developer.apple.com/documentation/cloudkit/ckerror)

A type that describes a CloudKit error.

[`enum Code`](https://developer.apple.com/documentation/cloudkit/ckerror/code)

The error codes that CloudKit returns.

[`let CKErrorRetryAfterKey: String`](https://developer.apple.com/documentation/cloudkit/ckerrorretryafterkey)

The key to retrieve the number of seconds to wait before you retry a request.

[`let CKErrorUserDidResetEncryptedDataKey: String`](https://developer.apple.com/documentation/cloudkit/ckerroruserdidresetencrypteddatakey)

The key that determines whether CloudKit deletes a record zone because of a user action.

[`let CKPartialErrorsByItemIDKey: String`](https://developer.apple.com/documentation/cloudkit/ckpartialerrorsbyitemidkey)

The key to retrieve partial errors.

[API Reference\\
Record Changed Error Keys](https://developer.apple.com/documentation/cloudkit/record-changed-error-keys)

Constants that represent conflicting records in a save operation.

### [Deprecated](https://developer.apple.com/documentation/cloudkit\#Deprecated)

[API Reference\\
Deprecated Symbols](https://developer.apple.com/documentation/cloudkit/deprecated-symbols)

Review unsupported symbols and their replacements.

### [Classes](https://developer.apple.com/documentation/cloudkit\#Classes)

[`class CKShareRequestAccessOperation`](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation)

### [Variables](https://developer.apple.com/documentation/cloudkit\#Variables)

[`let CKRecordParentKey: String`](https://developer.apple.com/documentation/cloudkit/ckrecordparentkey-1elhg)

[`let CKRecordShareKey: String`](https://developer.apple.com/documentation/cloudkit/ckrecordsharekey-gc8w)

[`let CKRecordTypeShare: String`](https://developer.apple.com/documentation/cloudkit/ckrecordtypeshare-7lec1)

[`let CKRecordTypeUserRecord: String`](https://developer.apple.com/documentation/cloudkit/ckrecordtypeuserrecord-6iwgn)

[`let CKRecordZoneDefaultName: String`](https://developer.apple.com/documentation/cloudkit/ckrecordzonedefaultname-1uuiu)

[`let CKShareThumbnailImageDataKey: String`](https://developer.apple.com/documentation/cloudkit/cksharethumbnailimagedatakey-rxjd)

[`let CKShareTitleKey: String`](https://developer.apple.com/documentation/cloudkit/cksharetitlekey-1cs9j)

[`let CKShareTypeKey: String`](https://developer.apple.com/documentation/cloudkit/cksharetypekey-5m83p)

Current page is CloudKit