# Get started with Cloud Storage on Apple platforms

Cloud Storage for Firebase lets you upload and share user generated content, such
as images and video, which allows you to build rich media content into your
apps. Your data is stored in a
[Google Cloud Storage](https://cloud.google.com/storage) bucket — an
exabyte scale object storage solution with high availability and global
redundancy. Cloud Storage for Firebase lets you securely upload these files
directly from mobile devices and web browsers, handling spotty networks with
ease.

## Before you begin

1. If you haven't already, make sure you've completed the
   [getting started guide for Apple platforms apps](https://firebase.google.com/docs/ios/setup).
   This includes:

   * Creating a Firebase project.
   * Registering your Apple platforms app with the project,
     and connecting your app to Firebase by adding the Firebase library and
     your Firebase config file (`GoogleService-Info.plist`) to your app.
2. Make sure your Firebase project is on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), which
   is a requirement to use Cloud Storage for Firebase. If you're new to Firebase
   and Google Cloud, check if you're eligible for a
   [$300 Free Trial credit](https://firebase.google.com/support/faq#pricing-free-trial).

## Create a default Cloud Storage bucket

1. In the Firebase console, navigate to **Databases & Storage** >
   [**Storage**](https://console.firebase.google.com/project/_/storage/).

   If your project is not yet on the pay-as-you-go Blaze pricing plan, then you'll be
   prompted to upgrade your project.
2. Click **Get started**.
3. Select a [location](https://firebase.google.com/docs/storage/locations) for your default bucket.

   * Buckets in `US-CENTRAL1`, `US-EAST1`, and `US-WEST1` can take advantage of the
     ["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free) for Google Cloud Storage.
     Buckets in all other locations follow
     [Google Cloud Storage pricing and usage](https://cloud.google.com/storage/pricing).
   * If you'd like, you can later
     [create multiple buckets](https://firebase.google.com/docs/storage/ios/start#use_multiple_storage_buckets), each with its
     own location.
4. Configure the Firebase Security Rules for your default bucket. During development,
   consider [setting up your rules for public access](https://firebase.google.com/docs/storage/ios/start#set_up_public_access).
5. Click **Done**.

You can now view the bucket in the Firebase console (navigate to the
**Databases & Storage** > **Storage** >
[**Files** tab](https://console.firebase.google.com/project/_/storage/)).
Your default bucket name format is `PROJECT_ID.firebasestorage.app`.

**Note:** All new default Cloud Storage buckets have the name format
`PROJECT_ID.firebasestorage.app`. Legacy default buckets (created
*before* September 2024) have the name format
`PROJECT_ID.appspot.com`. Learn more in the
[FAQs](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-default-storage-bucket).


## Set up public access

Cloud Storage for Firebase provides a declarative rules language that lets you
define how your data should be structured, how it should be indexed, and when
your data can be read from and written to. By default, read and write access to
Cloud Storage is restricted so only authenticated users can read or write
data. To get started without setting up [Authentication](https://firebase.google.com/docs/auth), you can
[configure your rules for public access](https://firebase.google.com/docs/storage/security/rules-conditions#public).

This does make Cloud Storage open to anyone, even people not using your
app, so be sure to restrict your Cloud Storage again when you set up
authentication.

## Add Cloud Storage to your app

Use Swift Package Manager to install and manage Firebase dependencies.

Visit [our installation guide](https://firebase.google.com/docs/ios/installation-methods)
to learn about the different ways you can add Firebase SDKs to your Apple project.

1. In Xcode, with your app project open, navigate to **File > Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:

```
  https://github.com/firebase/firebase-ios-sdk.git
```


**Note:** New projects should use the default (latest) SDK version, but you can
choose an older version if needed.
3. Choose the Cloud Storage library.
4. Add the `-ObjC` flag to the *Other Linker Flags* section of your target's build settings.
5. When finished, Xcode will automatically begin resolving and downloading your
   dependencies in the background.

## Set up Cloud Storage in your app

1. Initialize Firebase before any Firebase reference is created or used.

   You may have already done this if you've already set up another Firebase
   product, but you need to make sure to add the `FirebaseStorage` library to
   your list of imports.

   1. Import the `FirebaseCore` module and the `FirebaseStorage` module in
      your `UIApplicationDelegate`. We also recommend adding `FirebaseAuth`.

      ### SwiftUI

      ```
      import SwiftUI
      import FirebaseCore
      import FirebaseStorage
      import FirebaseAuth
      // ...
      ```

      ### Swift

      ```
      import FirebaseCore
      import FirebaseStorage
      import FirebaseAuth
      // ...
      ```

      ### Objective-C

      ```
      @import FirebaseCore;
      @import FirebaseStorage;
      @import FirebaseAuth;
      // ...
      ```
   2. Configure a
      [`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp)
      shared instance in your app delegate's
      `application(_:didFinishLaunchingWithOptions:)` method:

      ### SwiftUI

      ```
      // Use Firebase library to configure APIs
      FirebaseApp.configure()
      ```

      ### Swift

      ```
      // Use Firebase library to configure APIs
      FirebaseApp.configure()
      ```

      ### Objective-C

      ```
      // Use Firebase library to configure APIs
      [FIRApp configure];
      ```
   3. *(SwiftUI only)* Create an application delegate and attach it to your
      `App` struct using `UIApplicationDelegateAdaptor` or
      `NSApplicationDelegateAdaptor`. You must also disable app delegate
      swizzling. For more information, see the
      [SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).

      ### SwiftUI

      ```
      @main
      struct YourApp: App {
        // Register app delegate for Firebase setup
        @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

        var body: some Scene {
          WindowGroup {
            NavigationView {
              ContentView()
            }
          }
        }
      }
      ```
2. Get a reference to the Cloud Storage service, using the default Firebase App.

   1. Make sure the Firebase config file (`GoogleService-Info.plist`) in your
      app's codebase is updated with the name of your default Cloud Storage
      bucket.

      1. [Obtain your updated config file.](https://support.google.com/firebase/answer/7015592#ios).
      2. Use this downloaded config file to *replace* the existing
         `GoogleService-Info.plist` file in the root of your Xcode project.
         If prompted, select to add the config file to all targets.

         Make sure that you only have this most recent downloaded config file
         in your app and that its filename isn't appended with additional
         characters, like `(2)`.**Note:** Alternatively to replacing your config file, you can explicitly
      specify the bucket name when you create a reference to the Cloud Storage
      service (see next step). You can find the bucket name in the
      **Databases & Storage** > **Storage** >
      [**Files** tab](https://console.firebase.google.com/project/_/storage/)
      in the Firebase console.
   2. Get a reference to the Cloud Storage service, using the default
      Firebase App:

      ### Swift

      ```
      let storage = Storage.storage()
      ```

      ```
      // Alternatively, explicitly specify the bucket name URL.
      storage = Storage.storage(url:"gs://BUCKET_NAME")
      ```

      ### Objective-C

      ```
      FIRStorage *storage = [FIRStorage storage];
      ```

      ```
      // Alternatively, explicitly specify the bucket name URL.
      // FIRStorage storage = [FIRStorage storageWithURL:@"gs://BUCKET_NAME"];
      ```

You're ready to start using Cloud Storage!

Next step? Learn how to
[create a Cloud Storage reference](https://firebase.google.com/docs/storage/ios/create-reference).

## Advanced setup

There are a few use cases that require additional setup:

* Using Cloud Storage buckets in
  [multiple geographic regions](https://cloud.google.com/storage/docs/bucket-locations)
* Using Cloud Storage buckets in
  [different storage classes](https://cloud.google.com/storage/docs/storage-classes)
* Using Cloud Storage buckets with multiple authenticated users in the same app

The first use case is perfect if you have users across the world, and want to
store their data near them. For instance, you can create buckets in the US,
Europe, and Asia to store data for users in those regions to reduce latency.

The second use case is helpful if you have data with different access patterns.
For instance: you can set up a multi-regional or regional bucket that stores
pictures or other frequently accessed content, and a nearline or coldline bucket
that stores user backups or other infrequently accessed content.

In either of these use cases, you'll want to
[use multiple Cloud Storage buckets](https://firebase.google.com/docs/storage/ios/start#use_multiple_storage_buckets).

The third use case is useful if you're building an app, like Google Drive, which
lets users have multiple logged in accounts (for instance, a personal account
and a work account). You can [use a custom Firebase App](https://firebase.google.com/docs/storage/ios/start#use_a_custom_firebase_app)
instance to authenticate each additional account.

### Use multiple Cloud Storage buckets

If you want to use a Cloud Storage bucket other than the default provided above,
or use multiple Cloud Storage buckets in a single app, you can create an instance
of `FIRStorage` that references your custom bucket:

### Swift

```
// Get a non-default Cloud Storage bucket
storage = Storage.storage(url:"gs://my-custom-bucket")
```

### Objective-C

```
// Get a non-default Cloud Storage bucket
FIRStorage storage = [FIRStorage storageWithURL:@"gs://my-custom-bucket"];
```

### Working with imported buckets

When importing an existing Cloud Storage bucket into Firebase, you'll
have to grant Firebase the ability to access these files using the
`gsutil` tool, included in the
[Google Cloud SDK](https://cloud.google.com/sdk/docs/):

```
gsutil -m acl ch -r -u service-PROJECT_NUMBER@gcp-sa-firebasestorage.iam.gserviceaccount.com gs://BUCKET_NAME
```

You can find your project number as described in the
[introduction to Firebase projects](https://firebase.google.com/docs/projects/learn-more#project-number).

This does not affect newly created buckets, as those have the default access
control set to allow Firebase. This is a temporary measure, and will be
performed automatically in the future.

### Use a custom Firebase App

If you're building a more complicated app using a custom `FirebaseApp`, you can
create an instance of `Storage` initialized with that app:

### Swift

```
// Get the default bucket from a custom FirebaseApp
storage = Storage.storage(app:customApp)

// Get a non-default bucket from a custom FirebaseApp
storage = Storage.storage(app:customApp, url:"gs://my-custom-bucket")
```

### Objective-C

```
// Get the default bucket from a custom FIRApp
FIRStorage storage = [FIRStorage storageForApp:customApp];

// Get a non-default bucket from a custom FIRApp
FIRStorage storage = [FIRStorage storageForApp:customApp withURL:@"gs://my-custom-bucket"];
```

## Next steps

* Prepare to launch your app:

  + Enable [App Check](https://firebase.google.com/docs/app-check/ios) to help ensure that only
    your apps can access your storage buckets.
  + Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)
    for your project in the Google Cloud console.
  + Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage)
    in the Firebase console to get an overall picture of your project's
    usage across multiple Firebase services.
    You can also visit the [Cloud Storage *Usage*
    dashboard](https://console.firebase.google.com/project/_/storage/usage) for more
    detailed usage information.
  + Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).
