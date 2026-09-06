# Passing State in Email Actions

**Note**: The legacy implementation of email link authentication and actions in SDK versions
lower than Android SDK v23.2.0 and iOS SDK 11.8.0 uses Firebase Dynamic Links, which will be
shut down on August 25, 2025.

This guide has been updated to refer to the new solution in later SDK versions.

For specific information and migration guidance, visit the
[Dynamic Links
Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq#impacts-on-email-link-authentication).

You can pass state via a continue URL when sending email actions for password
resets or verifying a user's email. This provides the user the ability to be
returned to the app after the action is completed. In addition, you can specify
whether to handle the email action link directly from a mobile application when
it is installed instead of a web page.

This can be extremely useful in the following common scenarios:

* A user, not currently logged in, may be trying to access content that
  requires the user to be signed in. However, the user might have forgotten
  their password and therefore trigger the reset password flow. At the end of
  the flow, the user expects to go back to the section of the app they were
  trying to access.
* An application may only offer access to verified accounts. For
  example, a newsletter app may require the user to verify their email before
  subscribing. The user would go through the email verification flow and expect
  to be returned to the app to complete their subscription.
* In general, when a user begins a password reset or email verification flow on
  an Apple app they expect to complete the flow within the app; the ability to
  pass state via continue URL makes this possible.

Having the ability to pass state via a continue URL is a powerful feature that
Firebase Auth provides and which can significantly enhance the user experience.

## Passing state of a continue URL in email actions

In order to securely pass a continue URL, you need to add the domain for the
URL as an authorized domain:

1. In the Firebase console, go to the
   **Security** > **Authentication** >
   [**Settings** tab](https://console.firebase.google.com/project/_/authentication/settings).
2. In the **Authorized domains** section, click **Add domain**, and add
   the URL.

A `FIRActionCodeSettings` instance needs to be provided when sending
a password reset email or a verification email. This interface takes the
following parameters:

#### Swift

| Parameter | Type | Description |
| --- | --- | --- |
| `URL` | String | Sets the link (state/continue URL) which has different meanings in different contexts:   * When the link is handled in the web action widgets, this is the deep   link in the `continueUrl` query parameter. * When the link is handled in the app directly, this is the   `continueUrl` query parameter in the deep link of the   Hosting link. |
| `iOSBundleID` | String | Sets the iOS bundle ID to help Firebase Authentication determine if it should create a web-only or mobile link which is opened on an Apple device |
| `androidPackageName` | String | Sets the Android package name to help Firebase Authentication determine if it should create a web-only or mobile link which is opened on an Android device |
| `handleCodeInApp` | Bool | Whether the email action link will be opened in a mobile app or a web link first. The default is false. When set to true, the action code link will be be sent as a Universal Link or Android App Link and will be opened by the app if installed. In the false case, the code will be sent to the web widget first and then on continue will redirect to the app if installed. |
| `linkDomain` | String | When custom Hosting link domains are defined for a project, specify which one to use when the link is to be opened by a specified mobile app. Otherwise, the default domain is automatically selected (for example, `PROJECT_ID.firebaseapp.com`). |
| `dynamicLinkDomain` | String | Deprecated. Don't specify this parameter. |

#### Objective-C

| Parameter | Type | Description |
| --- | --- | --- |
| `URL` | NSString | Sets the link (state/continue URL) which has different meanings in different contexts:   * When the link is handled in the web action widgets, this is the deep   link in the `continueUrl` query parameter. * When the link is handled in the app directly, this is the   `continueUrl` query parameter in the deep link of the   Hosting link. |
| `iOSBundleID` | NSString | Sets the iOS bundle ID to help Firebase Authentication determine if it should create a web-only or mobile link which is opened on an Android or Apple device |
| `androidPackageName` | NSString | Sets the Android package name to help Firebase Authentication determine if it should create a web-only or mobile link which is opened on an Android or Apple device |
| `handleCodeInApp` | BOOL | Whether the email action link will be opened in a mobile app or a web link first. The default is false. When set to true, the action code link will be be sent as a Universal Link or Android App Link and will be opened by the app if installed. In the false case, the code will be sent to the web widget first and then on continue will redirect to the app if installed. |
| `linkDomain` | NSString | When custom Hosting link domains are defined for a project, specify which one to use when the link is to be opened by a specified mobile app. Otherwise, the default domain is automatically selected (for example, `PROJECT_ID.firebaseapp.com`). |
| `dynamicLinkDomain` | NSString | Deprecated. Don't specify this parameter. |

The following example illustrates how to send an email verification link that
will open in a mobile app first using the custom Hosting link domain
`custom-domain.com`. The deep link will contain the continue URL payload
`https://www.example.com/?email=user@example.com`.

#### Swift

```
var actionCodeSettings =  ActionCodeSettings.init()
actionCodeSettings.canHandleInApp = true
let user = Auth.auth().currentUser()
actionCodeSettings.URL =
    String(format: "https://www.example.com/?email=%@", user.email)
actionCodeSettings.iOSbundleID = Bundle.main.bundleIdentifier!
actionCodeSettings.setAndroidPakageName("com.example.android")
// Specify a custom Hosting link domain to use. The domain must be
// configured in Firebase Hosting and owned by the project.
actionCodeSettings.linkDomain = "custom-domain.com"
user.sendEmailVerification(withActionCodeSettings:actionCodeSettings { error in
  if error {
    // Error occurred. Inspect error.code and handle error.
    return
  }
  // Email verification sent.
})
```

#### Objective-C

```
 FIRActionCodeSettings *actionCodeSettings = [[FIRActionCodeSettings alloc] init];
 actionCodeSettings.handleCodeInApp = YES;
 FIRUser *user = [FIRAuth auth].currentUser;
 NSString *urlString =
     [NSString stringWithFormat:@"https://www.example.com/?email=%@", user.email];
 actionCodeSettings.URL = [NSURL URLWithString:urlString];
 actionCodeSettings.iOSBundleID = [NSBundle mainBundle].bundleIdentifier;
// Specify a custom Hosting link domain to use. The domain must be
// configured in Firebase Hosting and owned by the project.
 actionCodeSettings.linkDomain = @"custom-domain.com";
 [actionCodeSettings setAndroidPackageName:@"com.example.android"];
 [user sendEmailVerificationWithActionCodeSettings:actionCodeSettings
                                        completion:^(NSError *_Nullable error) {
   if (error) {
     // Error occurred. Inspect error.code and handle error.
     return;
   }
   // Email verification sent.
 }];
```

## Configuring Firebase Hosting links

Firebase Authentication uses [Firebase Hosting](https://firebase.google.com/docs/hosting) when sending a
link that is meant to be opened in a mobile application. In order to use this
feature, Hosting links need to be configured in the Firebase console.

1. Configuring Apple applications:

   1. If you plan on handling these links from your application, you will
      need to configure the Hosting link domain as an Associated Domain in
      your application capabilities.
   2. For more on this, refer to
      [Receiving iOS Hosting links instructions](https://firebase.google.com/docs/auth/ios/email-link-migration).
2. Configuring Android applications:

   1. If you plan on handling these links from your Android application, your
      app's package name needs to be specified in the Firebase console
      project settings. In addition, the SHA-1 and SHA-256 of the application
      certificate need to be provided.
   2. You will also need to configure the intent filter for the deep link in
      your `AndroidManifest.xml` file.
   3. For more on this, refer to
      [Receiving Android Hosting links instructions](https://firebase.google.com/docs/auth/android/email-link-migration).

## Handling email actions in a web application

You can specify whether you want to handle the action code link from a web
application first and then redirect to another web page or mobile application
after successful completion, provided the mobile application is available.
This is done by setting `handleCodeInApp` to `false` in the
`FIRActionCodeSettings` (Obj-C) or `ActionCodeSettings` (Swift) object. While
a bundle ID
or Android package name are not required, providing them will allow the user
to redirect back to the specified app on email action code completion.

The web URL used here, is the one configured in the email action templates
section. A default one is provisioned for all projects. Refer to
[customizing email handlers](https://firebase.google.com/docs/auth/custom-email-handler) to learn more on
how to customize the email action handler.

In this case, the link within the `continueURL` query parameter will be
a Hosting link whose payload is the `URL` specified in the
`ActionCodeSettings` object.

When handling email actions such as email verification, the action code from the
`oobCode` query parameter needs to be parsed from the deep link and then applied
via `applyActionCode` for the change to take effect, i.e. email to be verified.

## Handling email actions in a mobile application

You can specify whether you want to handle the action code link within your
mobile application first, provided it is installed. If the link is clicked from
a device that does not support the mobile application, it is opened from a web
page instead. This is done by setting `handleCodeInApp` to `true` in the
`FIRActionCodeSettings` (Obj-C) or `ActionCodeSettings` (Swift) object. The
mobile application's Android package name or bundle ID will also need to be
specified. The fallback web URL used here, when no mobile app is available, is
the one configured in the email action templates section. A default one is
provisioned for all projects. Refer to
[customizing email handlers](https://firebase.google.com/docs/auth/custom-email-handler) to learn more on
how to customize the email action handler.

In this case, the mobile app link sent to the user will be a Hosting link
whose payload is the action code URL, configured in the Console, with the query
parameters `oobCode`, `mode`, `apiKey` and `continueUrl`. The latter will be the
original `URL` specified in the `FIRActionCodeSettings` (Obj-C) or
`ActionCodeSettings` (Swift) object. The action code can be applied directly
from a mobile application similar to how it is handled from the web flow
described in the [customizing email handlers](https://firebase.google.com/docs/auth/custom-email-handler)
section.

When handling email actions such as email verification, the action code from the
`oobCode` query parameter needs to be parsed from the deep link and then applied
via `applyActionCode` for the change to take effect, i.e. email to be verified.
