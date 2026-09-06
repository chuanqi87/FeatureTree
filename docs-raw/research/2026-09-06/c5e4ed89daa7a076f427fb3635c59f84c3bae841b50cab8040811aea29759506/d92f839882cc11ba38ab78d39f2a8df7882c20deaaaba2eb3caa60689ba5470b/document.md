# Where do I start with Firebase Authentication?

## I already have an authentication system

If your app already has a sign-in implementation and you want to use it to
authenticate with Firebase backend services, use **Custom Authentication**. This
includes apps that use any of the following:

* Custom-built solutions, such as custom password-based systems.
* Third-party identity management services, such as Auth0 or Okta.
* Existing integrations with federated identity providers, such as Google,
  Facebook, or Apple. (And if you don't yet support federated identity, but you
  want to, see the next section.)

With custom authentication, you sign users in with the system of your choice,
create a Firebase token for the user on your backend, and then use the token
from the client to authenticate with Firebase.

See the docs for
[iOS+](https://firebase.google.com/docs/auth/ios/custom-auth),
[Android](https://firebase.google.com/docs/auth/android/custom-auth),
[Web](https://firebase.google.com/docs/auth/web/custom-auth),
[Flutter](https://firebase.google.com/docs/auth/flutter/custom-auth),
[Unity](https://firebase.google.com/docs/auth/unity/custom-auth), or
[C++](https://firebase.google.com/docs/auth/cpp/custom-auth).

## I want to build my authentication system with Firebase

If you're building a new app or adding sign-in to an existing app, Firebase has
libraries and services that can help you implement secure authentication without
having to build the authentication backend yourself. Firebase Authentication is a
complete backend solution for signing in with passwords, federated identity
providers, email links, and text messages.

#### I want a drop-in solution that's easy to use

The fastest and easiest way to add authentication to an app is to use
**FirebaseUI Auth**, a drop-in UI library. FirebaseUI implements complete user
flows for all of Firebase Authentication's supported sign-in methods.

Because FirebaseUI Auth is a drop-in solution, it has a specific UX that might
not meet your needs. If you want to change the UX, you can fork the library,
which is open source, and use your own version. However, for substantially
different sign-in flows, you might prefer to implement your own flows with the
Firebase SDK as discussed in the next section.

See the FirebaseUI Auth docs for
[iOS](https://firebase.google.com/docs/auth/ios/firebaseui),
[Android](https://firebase.google.com/docs/auth/android/firebaseui), or
[Web](https://firebase.google.com/docs/auth/web/firebaseui).

#### I want full control over the sign-in experience

For more control over your app's sign-in experience, you can implement your own
authentication flows and use the Firebase SDK to work with Firebase's
authentication services. For example, build your own email address and password
flow or Google Sign-in flow, and pass the user's email address and password or
Google ID token to Firebase to authenticate the user.

See the Firebase Authentication SDK docs:

| Firebase services | |
| --- | --- |
| **Email address and password sign-in** | [iOS+](https://firebase.google.com/docs/auth/ios/password-auth) | [Android](https://firebase.google.com/docs/auth/android/password-auth) | [Web](https://firebase.google.com/docs/auth/web/password-auth) | [Flutter](https://firebase.google.com/docs/auth/flutter/password-auth) | [Unity](https://firebase.google.com/docs/auth/unity/password-auth) | [C++](https://firebase.google.com/docs/auth/cpp/password-auth) |
| **Phone number sign-in** | [iOS+](https://firebase.google.com/docs/auth/ios/phone-auth) | [Android](https://firebase.google.com/docs/auth/android/phone-auth) | [Web](https://firebase.google.com/docs/auth/web/phone-auth) | [Flutter](https://firebase.google.com/docs/auth/flutter/phone-auth) | [Unity](https://firebase.google.com/docs/auth/unity/phone-auth) | [C++](https://firebase.google.com/docs/auth/cpp/phone-auth) |
| **Email link sign-in** | [iOS+](https://firebase.google.com/docs/auth/ios/email-link-auth) | [Android](https://firebase.google.com/docs/auth/android/email-link-auth) | [Web](https://firebase.google.com/docs/auth/web/email-link-auth) | [Flutter](https://firebase.google.com/docs/auth/flutter/email-link-auth) | [Unity](https://firebase.google.com/docs/auth/unity/email-link-auth) | [C++](https://firebase.google.com/docs/auth/cpp/email-link-auth) |
| Federated identity | |
| **Google** | [iOS+](https://firebase.google.com/docs/auth/ios/google-signin) | [Android](https://firebase.google.com/docs/auth/android/google-signin) | [Web](https://firebase.google.com/docs/auth/web/google-signin) | [Flutter](https://firebase.google.com/docs/auth/flutter/federated-auth#google) | [Unity](https://firebase.google.com/docs/auth/unity/google-signin) | [C++](https://firebase.google.com/docs/auth/cpp/google-signin) |
| **Facebook** | [iOS+](https://firebase.google.com/docs/auth/ios/facebook-login) | [Android](https://firebase.google.com/docs/auth/android/facebook-login) | [Web](https://firebase.google.com/docs/auth/web/facebook-login) | [Flutter](https://firebase.google.com/docs/auth/flutter/federated-auth#facebook) | [Unity](https://firebase.google.com/docs/auth/unity/facebook-login) | [C++](https://firebase.google.com/docs/auth/cpp/facebook-login) |
| **Apple** | [iOS+](https://firebase.google.com/docs/auth/ios/apple) | [Android](https://firebase.google.com/docs/auth/android/apple) | [Web](https://firebase.google.com/docs/auth/web/apple) | [Flutter](https://firebase.google.com/docs/auth/flutter/federated-auth#apple) | [Unity](https://firebase.google.com/docs/auth/unity/apple) | [C++](https://firebase.google.com/docs/auth/cpp/apple) |
| **Play Games** | [Android](https://firebase.google.com/docs/auth/android/play-games) | [Unity](https://firebase.google.com/docs/auth/unity/play-games) | [C++](https://firebase.google.com/docs/auth/cpp/play-games) |
| **Game Center** | [iOS+](https://firebase.google.com/docs/auth/ios/game-center) |
| **GitHub** | [iOS+](https://firebase.google.com/docs/auth/ios/github-auth) | [Android](https://firebase.google.com/docs/auth/android/github-auth) | [Web](https://firebase.google.com/docs/auth/web/github-auth) | [Flutter](https://firebase.google.com/docs/auth/flutter/federated-auth#github) | [Unity](https://firebase.google.com/docs/auth/unity/github-auth) | [C++](https://firebase.google.com/docs/auth/cpp/github-auth) |
| **Microsoft** | [iOS+](https://firebase.google.com/docs/auth/ios/microsoft-oauth) | [Android](https://firebase.google.com/docs/auth/android/microsoft-oauth) | [Web](https://firebase.google.com/docs/auth/web/microsoft-oauth) | [Unity](https://firebase.google.com/docs/auth/unity/microsoft-oauth) | [C++](https://firebase.google.com/docs/auth/cpp/microsoft-oauth) |
| **Twitter** | [iOS+](https://firebase.google.com/docs/auth/ios/twitter-login) | [Android](https://firebase.google.com/docs/auth/android/twitter-login) | [Web](https://firebase.google.com/docs/auth/web/twitter-login) | [Flutter](https://firebase.google.com/docs/auth/flutter/federated-auth#twitter) | [Unity](https://firebase.google.com/docs/auth/unity/twitter-login) | [C++](https://firebase.google.com/docs/auth/cpp/twitter-login) |
| **Yahoo** | [iOS+](https://firebase.google.com/docs/auth/ios/yahoo-oauth) | [Android](https://firebase.google.com/docs/auth/android/yahoo-oauth) | [Web](https://firebase.google.com/docs/auth/web/yahoo-oauth) | [Unity](https://firebase.google.com/docs/auth/unity/yahoo-oauth) | [C++](https://firebase.google.com/docs/auth/cpp/yahoo-oauth) |

## I want to build rich pre-sign-in experiences

You can enable users to use the signed-in features of your app before they
actually sign in using **Anonymous Auth**. With anonymous "sign-in", you create
temporary single-session accounts, which you can use like a real account. Then,
after the user signs in or signs up, link the temporary account to the real
account to let them continue where they left off.

Anonymous Auth works well alongside either Custom Auth or any of Firebase's
authentication services.

See the docs for
[iOS+](https://firebase.google.com/docs/auth/ios/anonymous-auth),
[Android](https://firebase.google.com/docs/auth/android/anonymous-auth),
[Web](https://firebase.google.com/docs/auth/web/anonymous-auth),
[Flutter](https://firebase.google.com/docs/auth/flutter/anonymous-auth),
[Unity](https://firebase.google.com/docs/auth/unity/anonymous-auth), or
[C++](https://firebase.google.com/docs/auth/cpp/anonymous-auth).

## I want to access Firebase services from my backend

To access Firebase services from a server, you don't need to use
Firebase Authentication. Instead, use the [Admin SDK](https://firebase.google.com/docs/admin/setup). When you
initialize the Admin SDK, you authenticate with service account credentials,
which represent your Firebase project rather than a particular user, and which
grant full access to your project's resources.
