# Installation & Setup on Apple platforms

The Firebase Realtime Database is a cloud-hosted database. Data is stored as JSON
and synchronized in realtime to every connected client. When you build
cross-platform apps with our Android, iOS, and JavaScript SDKs, all of your
clients share one Realtime Database instance and automatically receive updates with
the newest data.

Firebase Realtime Database is available on all Apple platforms, including iOS,
macOS, macOS Catalyst, tvOS, and watchOS. It is not available for App Clips.
The setup instructions in this page reference iOS in specific examples, but are
generic and work for any Apple platform target.

## Prerequisites

1. [Install the Firebase SDK](https://firebase.google.com/docs/ios/setup).
2. Add your app to your Firebase project in the [Firebase console](https://console.firebase.google.com/).

## Create a Database

1. In the Firebase console, navigate to **Databases & Storage** >
   [**Realtime Database**](https://console.firebase.google.com/project/_/database/).
2. Click **Create database**.
3. Select a starting mode for your Firebase Security Rules:

   Test mode
   :   Good for getting started with the mobile and web client libraries,
       but allows anyone to read and overwrite your data. After testing, **make
       sure to review the [Understand Firebase Realtime Database Rules](https://firebase.google.com/docs/database/security)
       section.**
   :   **Note:** If you create a database in Test mode and make no changes to the
       default world-readable and world-writeable Security Rules within a trial
       period, you will be alerted by email, then your database rules will
       deny all requests. Note the expiration date during the Firebase console
       setup flow.
   :   To get started with the web, Apple, or Android SDK, select testmode.

   Locked mode
   :   Denies all reads and writes from mobile and web clients.
       Your authenticated application servers can still access your database.
4. Choose a location for the database.

   Depending on the
   [location of the database](https://firebase.google.com/docs/projects/locations#rtdb-locations), the
   URL for the new database will be in one of the following forms:

   * `DATABASE_NAME.firebaseio.com` (for
     databases in `us-central1`)
   * `DATABASE_NAME.REGION.firebasedatabase.app`
     (for databases in all other locations)
5. Click **Done**.

When you enable Realtime Database, it also enables the API in the
[Cloud API Manager](https://console.cloud.google.com/projectselector/apis/api/firebasedatabase.googleapis.com/overview).

## Add Firebase Realtime Database to your app

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
3. Choose the Realtime Database library.
4. Add the `-ObjC` flag to the *Other Linker Flags* section of your target's build settings.
5. When finished, Xcode will automatically begin resolving and downloading your
   dependencies in the background.

## Configure Realtime Database Security Rules

The Realtime Database provides a declarative rules language that allows you to
define how your data should be structured, how it should be indexed, and when
your data can be read from and written to.

**Note:** By default, read and write access to your database is restricted so only
authenticated users can read or write data. To get started without setting up
[Authentication](https://firebase.google.com/docs/auth), you can [configure your rules for public access](https://firebase.google.com/docs/rules/basics#default_rules_locked_mode). This does
make your database open to anyone, even people not using your app, so be sure
to restrict your database again when you set up authentication.


## Set up Firebase Realtime Database

You must initialize Firebase before any Firebase app reference is created or
used. If you have already done this for another Firebase feature, you can skip
this step.

1. Import the `FirebaseCore` module in your
   `UIApplicationDelegate`, as well as any other
   [Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods) your app delegate uses.
   For example, to use Cloud Firestore and Authentication:

   #### SwiftUI

   ```
   import SwiftUI
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
   ```

   #### Swift

   ```
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
   ```

   #### Objective-C

   ```
   @import FirebaseCore;
   @import FirebaseFirestore;
   @import FirebaseAuth;
   // ...
   ```
2. Configure a
   [`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp)
   shared instance in your app delegate's
   `application(_:didFinishLaunchingWithOptions:)` method:

   #### SwiftUI

   ```
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Swift

   ```
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Objective-C

   ```
   // Use Firebase library to configure APIs
   [FIRApp configure];
   ```
3. If you're using SwiftUI, you must create an application delegate and attach it
   to your `App` struct via `UIApplicationDelegateAdaptor` or
   `NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For
   more information, see the [SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).

   #### SwiftUI

   ```
   @main
   struct YourApp: App {
     // register app delegate for Firebase setup
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
4. Create a reference to your database and specify the location you want to
   write to.
   **Important**: To get a reference to a database other
   than a `us-central1` default database, you must pass the
   database URL to `database()` (or for Objective-C
   `databaseWithURL`). For a `us-central1` default
   database, you can call `database()` (or `database`)
   without arguments.

   You can find your Realtime Database URL in the *Realtime Database* section of the
   [Firebase console](https://console.firebase.google.com/). Depending on the
   [location of the database](https://firebase.google.com/docs/projects/locations#rtdb-locations),
   the database URL will be in one of the following forms:

   * `https://DATABASE_NAME.firebaseio.com`
     (for databases in `us-central1`)
   * `https://DATABASE_NAME.REGION.firebasedatabase.app`
     (for databases in all other locations)


   ### Swift

   **Note:** This Firebase product is not available on the App Clip target.

   ```
   var ref: DatabaseReference!

   ref = Database.database().reference()
   ```

   ### Objective-C

   **Note:** This Firebase product is not available on the App Clip target.

   ```
   @property (strong, nonatomic) FIRDatabaseReference *ref;

   self.ref = [[FIRDatabase database] reference];
   ```

## Next Steps

* Learn how to [structure data](https://firebase.google.com/docs/database/ios/structure-data) for Realtime Database.
* [Scale your data across multiple database
  instances.](https://firebase.google.com/docs/database/usage/sharding)
* [Read and write data.](https://firebase.google.com/docs/database/ios/read-and-write)
* [View your database in the
  Firebase console.](https://console.firebase.google.com/project/_/database/data)
* Prepare to launch your app:

  + Enable [App Check](https://firebase.google.com/docs/app-check/ios) to help ensure that only your
    apps can access your databases.
  + Set up [budget
    alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)
    for your project in the Google Cloud console.
  + Monitor the [*Usage and billing*
    dashboard](https://console.firebase.google.com/project/_/usage)
    in the Firebase console to get an overall picture of your project's
    usage across multiple Firebase services.
    You can also visit the [Realtime Database *Usage*
    dashboard](https://console.firebase.google.com/project/_/database/usage) for more
    detailed usage information.
  + Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).
