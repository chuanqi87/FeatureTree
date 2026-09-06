# Generate smart replies with ML Kit on Android

ML Kit can generate short replies to messages using an on-device model.

To generate smart replies, you pass ML Kit a log of recent messages in a
conversation. If ML Kit determines the conversation is in English, and that
the conversation doesn't have potentially sensitive subject matter, ML Kit
generates up to three replies, which you can suggest to your user.

This API is available using either an unbundled library that must be downloaded before use or a
bundled library that increases your app size. See
[this guide](https://developers.google.com/ml-kit/tips/installation-paths) for more information on the differences
between the two installation options.


|  | Bundled | Unbundled |
| --- | --- | --- |
| **Library name** | `com.google.mlkit:smart-reply` | `com.google.android.gms:play-services-mlkit-smart-reply` |
| **Implementation** | Model is statically linked to your app at build time. | Model is dynamically downloaded via Google Play Services. |
| **App size impact** | About 5.7 MB size increase. | About 200 KB size increase. |
| **Initialization time** | Model is available immediately. | Might have to wait for model to download before first use. |

**Note:** The unbundled version of Smart Reply is currently offered in beta, which
means it might be changed in backward-incompatible ways and is not subject to
any SLA or deprecation policy.



## Try it out

* Play around with [the sample app](https://github.com/googlesamples/mlkit/tree/master/android/smartreply) to
  see an example usage of this API.

## Before you begin

This API requires Android API level 23 or above. Make sure that your app's build
file uses a `minSdkVersion` value of 23 or higher.

1. In your project-level `build.gradle` file, make sure to include Google's
   Maven repository in both your `buildscript` and `allprojects` sections.
2. Add the dependencies for the ML Kit Android libraries to your module's
   app-level gradle file, which is usually `app/build.gradle`. Choose one of
   the following dependencies based on your needs:

   * To bundle the model with your app:

   ```
   dependencies {
     // ...
     // Use this dependency to bundle the model with your app
     implementation 'com.google.mlkit:smart-reply:17.0.4'
   }
   ```

   * To use the model in Google Play Services:

   ```
   dependencies {
     // ...
     // Use this dependency to use the dynamically downloaded model in Google Play Services
     implementation 'com.google.android.gms:play-services-mlkit-smart-reply:16.0.0-beta1'
   }
   ```

   If you choose to use the model in Google Play Services, you can configure
   your app to automatically download the model to the device after your app is
   installed from the Play Store. By adding the following declaration to your
   app's `AndroidManifest.xml` file:

   ```
   <application ...>
         ...
         <meta-data
             android:name="com.google.mlkit.vision.DEPENDENCIES"
             android:value="smart_reply" >
         <!-- To use multiple models: android:value="smart_reply,model2,model3" -->
   </application>
   ```

   You can also explicitly check the model availability and request download through
   Google Play services [ModuleInstallClient API](https://developers.google.com/android/guides/module-install-apis).

   If you don't enable install-time model downloads or request explicit download,
   the model is downloaded the first time you run the smart reply generator.
   Requests you make before the download has completed produce no results.

   ## 1. Create a conversation history object

   To generate smart replies, you pass ML Kit a chronologically-ordered `List`
   of `TextMessage` objects, with the earliest timestamp first.

   Whenever the user sends a message, add the message and its timestamp to the
   conversation history:

   ### Kotlin

   ```
   conversation.add(TextMessage.createForLocalUser(
           "heading out now", System.currentTimeMillis()))
   ```

   ### Java

   ```
   conversation.add(TextMessage.createForLocalUser(
           "heading out now", System.currentTimeMillis()));
   ```

   Whenever the user receives a message, add the message, its timestamp, and the
   sender's user ID to the conversation history. The user ID can be any string that
   uniquely identifies the sender within the conversation. The user ID doesn't need
   to correspond to any user data, and the user ID doesn't need to be consistent
   between conversation or invocations of the smart reply generator.

   ### Kotlin

   ```
   conversation.add(TextMessage.createForRemoteUser(
           "Are you coming back soon?", System.currentTimeMillis(), userId))
   ```

   ### Java

   ```
   conversation.add(TextMessage.createForRemoteUser(
           "Are you coming back soon?", System.currentTimeMillis(), userId));
   ```

   A conversation history object looks like the following example:

   | Timestamp | userID | isLocalUser | Message |
   | --- | --- | --- | --- |
   | Thu Feb 21 13:13:39 PST 2019 |  | true | are you on your way? |
   | Thu Feb 21 13:15:03 PST 2019 | FRIEND0 | false | Running late, sorry! |

   ML Kit suggests replies to the last message in a conversation history. The last message
   should be from a non-local user. In the example above, the last message in the conversation
   is from the non-local user FRIEND0. When you use pass ML Kit this log, it suggests
   replies to FRIENDO's message: "Running late, sorry!"

   ## 2. Get message replies

   To generate smart replies to a message, get an instance of `SmartReplyGenerator`
   and pass the conversation history to its `suggestReplies()` method:

   ### Kotlin

   ```
   val smartReplyGenerator = SmartReply.getClient()
   smartReply.suggestReplies(conversation)
           .addOnSuccessListener { result ->
               if (result.getStatus() == SmartReplySuggestionResult.STATUS_NOT_SUPPORTED_LANGUAGE) {
                   // The conversation's language isn't supported, so
                   // the result doesn't contain any suggestions.
               } else if (result.getStatus() == SmartReplySuggestionResult.STATUS_SUCCESS) {
                   // Task completed successfully
                   // ...
               }
           }
           .addOnFailureListener {
               // Task failed with an exception
               // ...
           }
   ```

   ### Java

   ```
   SmartReplyGenerator smartReply = SmartReply.getClient();
   smartReply.suggestReplies(conversation)
           .addOnSuccessListener(new OnSuccessListener() {
               @Override
               public void onSuccess(SmartReplySuggestionResult result) {
                   if (result.getStatus() == SmartReplySuggestionResult.STATUS_NOT_SUPPORTED_LANGUAGE) {
                       // The conversation's language isn't supported, so
                       // the result doesn't contain any suggestions.
                   } else if (result.getStatus() == SmartReplySuggestionResult.STATUS_SUCCESS) {
                       // Task completed successfully
                       // ...
                   }
               }
           })
           .addOnFailureListener(new OnFailureListener() {
               @Override
               public void onFailure(@NonNull Exception e) {
                   // Task failed with an exception
                   // ...
               }
           });
   ```

   If the operation succeeds, a `SmartReplySuggestionResult` object is passed to
   the success handler. This object contains a list of up to three suggested replies,
   which you can present to your user:

   ### Kotlin

   ```
   for (suggestion in result.suggestions) {
       val replyText = suggestion.text
   }
   ```

   ### Java

   ```
   for (SmartReplySuggestion suggestion : result.getSuggestions()) {
       String replyText = suggestion.getText();
   }
   ```

   Note that ML Kit might not return results if the model isn't confident in
   the relevance of the suggested replies, the input conversation isn't in
   English, or if the model detects sensitive subject matter.
