# Authenticate with Firebase Anonymously on Apple Platforms

You can use Firebase Authentication to create and use temporary anonymous accounts
to authenticate with Firebase. These temporary anonymous accounts can be used to
allow users who haven't yet signed up to your app to work with data protected
by security rules. If an anonymous user decides to sign up to your app, you can
[link their sign-in credentials to the anonymous
account](https://firebase.google.com/docs/auth/ios/account-linking) so that they can continue to work with their protected data in
future sessions.

## Before you begin

1. Use Swift Package Manager to install and manage Firebase dependencies.

   Visit [our installation guide](https://firebase.google.com/docs/ios/installation-methods)
   to learn about the different ways you can add Firebase SDKs to your Apple project.
   1. In Xcode, with your app project open, navigate to **File > Add Packages**.
   2. When prompted, add the Firebase Apple platforms SDK repository:

   ```
     https://github.com/firebase/firebase-ios-sdk.git
   ```


   **Note:** New projects should use the default (latest) SDK version, but you can
   choose an older version if needed.
   3. Choose the Firebase Authentication library.
   4. Add the `-ObjC` flag to the *Other Linker Flags* section of your target's build settings.
   5. When finished, Xcode will automatically begin resolving and downloading your
      dependencies in the background.
2. If you haven't yet connected your app to your Firebase project, do so from
   the [Firebase console](https://console.firebase.google.com/).
3. Enable anonymous authentication:
   1. In the [Firebase console](https://console.firebase.google.com/), go to
      **Security** > [**Authentication**](https://console.firebase.google.com/project/_/authentication/).
   2. In the **Sign-in method** tab, enable the **Anonymous** sign-in
      provider.
   3. **Optional**: If you've upgraded your project to
      [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can enable
      automatic clean-up. When you enable this setting, anonymous accounts
      older than 30 days will be automatically deleted. In projects with
      automatic clean-up enabled, anonymous authentication will no longer
      count toward usage limits or billing quotas. See
      [Automatic clean-up](https://firebase.google.com/docs/auth/ios/anonymous-auth#auto-cleanup).

## Authenticate with Firebase anonymously

When a signed-out user uses an app feature that requires authentication with
Firebase, sign in the user anonymously by completing the following steps:

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
4. Call the `signInAnonymouslyWithCompletion:` method:

   #### Swift

   ```
   Auth.auth().signInAnonymously { authResult, error in
     // ...
   }
   ```

   #### Objective-C

   ```
   [[FIRAuth auth] signInAnonymouslyWithCompletion:^(FIRAuthDataResult * _Nullable authResult,
                                                     NSError * _Nullable error) {
      // ...
    }];
   ```
5. If the `signInAnonymouslyWithCompletion:` method completes
   without error, you can get the anonymous user's account data from the
   `FIRAuthDataResult` object:

   #### Swift

   ```
   guard let user = authResult?.user else { return }
   let isAnonymous = user.isAnonymous  // true
   let uid = user.uid
   ```

   #### Objective-C

   ```
   FIRUser *user = authResult.user;
   BOOL isAnonymous = user.anonymous;  // YES
   NSString *uid = user.uid;
   ```

To protect your project from abuse, Firebase limits the number of new
email/password and anonymous sign-ups that your application can have from the
same IP address in a short period of time. You can request and schedule
temporary changes to this quota from the Firebase console (go to the
**Security** > **Authentication** >
[**Sign-in method** tab](https://console.firebase.google.com/project/_/authentication/providers)).


## Convert an anonymous account to a permanent account

When an anonymous user signs up to your app, you might want to allow them to
continue their work with their new account—for example, you might want to
make the items the user added to their shopping cart before they signed up
available in their new account's shopping cart. To do so, complete the following
steps:

1. When the user signs up, complete the sign-in flow for the user's
   authentication provider up to, but not including, calling one of the
   [`FIRAuth.signInWith`](https://firebase.google.com/docs/reference/ios/firebaseauth/interface_f_i_r_auth) methods. For example, get the user's Google ID token,
   Facebook access token, or email address and password.
2. Get an `FIRAuthCredential` for the new authentication provider:

   ##### Google Sign-In

   ###### Swift

   ```
   guard
     let authentication = user?.authentication,
     let idToken = authentication.idToken
   else {
     return
   }

   let credential = GoogleAuthProvider.credential(withIDToken: idToken,
                                                  accessToken: authentication.accessToken)
   ```

   ###### Objective-C

   ```
   FIRAuthCredential *credential =
   [FIRGoogleAuthProvider credentialWithIDToken:result.user.idToken.tokenString
                                    accessToken:result.user.accessToken.tokenString];
   ```

   ##### Facebook Login

   ###### Swift

   ```
   let credential = FacebookAuthProvider
     .credential(withAccessToken: AccessToken.current!.tokenString)
   ```

   ###### Objective-C

   ```
   FIRAuthCredential *credential = [FIRFacebookAuthProvider
       credentialWithAccessToken:[FBSDKAccessToken currentAccessToken].tokenString];
   ```

   ##### Email-password sign-in

   ###### Swift

   ```
   let credential = EmailAuthProvider.credential(withEmail: email, password: password)
   ```

   ###### Objective-C

   ```
   FIRAuthCredential *credential =
       [FIREmailAuthProvider credentialWithEmail:email
                                                password:password];
   ```
3. Pass the `FIRAuthCredential` object to the sign-in user's
   `linkWithCredential:completion:` method:

   ###### Swift

   ```
       user.link(with: credential) { authResult, error in
     // ...
   }
   }
   ```

   ###### Objective-C

   ```
       [[FIRAuth auth].currentUser linkWithCredential:credential
       completion:^(FIRAuthDataResult *result, NSError *_Nullable error) {
     // ...
   }];
   ```

If the call to `linkWithCredential:completion:` succeeds, the user's new account can
access the anonymous account's Firebase data.

This technique can also be used to
[link any two accounts](https://firebase.google.com/docs/auth/ios/account-linking).


## Automatic clean-up

If you've upgraded your project to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can
enable automatic clean-up in the Firebase console. When you enable this feature you allow
Firebase to automatically delete anonymous accounts older than 30 days. In projects with automatic
clean-up enabled, anonymous authentication will not count toward usage limits or billing quotas.

* Any anonymous accounts created after enabling automatic clean-up might be automatically
  deleted any time after 30 days post-creation.
* Existing anonymous accounts will be eligible for automatic deletion 30 days after
  enabling automatic clean-up.
* If you turn automatic clean-up off, any anonymous accounts scheduled to be deleted will remain
  scheduled to be deleted.
* If you "upgrade" an anonymous account by linking it to any sign-in method, the account will
  not get automatically deleted.

If you want to see how many users will be affected before you enable this feature, and you've
upgraded your project to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform), you can filter by
`is_anon` in [Cloud
Logging](https://cloud.google.com/logging/docs).

## Next steps

Now that users can authenticate with Firebase, you can control their access to
data in your Firebase database using
[Firebase rules](https://firebase.google.com/docs/database/security#section-authorization).
