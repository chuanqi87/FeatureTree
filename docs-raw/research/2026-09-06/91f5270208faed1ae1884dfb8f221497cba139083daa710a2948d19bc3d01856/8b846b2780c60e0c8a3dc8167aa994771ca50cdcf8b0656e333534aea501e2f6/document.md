# Automatic SMS Verification with the SMS Retriever API

With the SMS Retriever API, you can perform SMS-based user verification in your
Android app automatically, without requiring the user to manually type
verification codes, and without requiring any extra app permissions. When you
implement automatic SMS verification in your app, the verification flow looks
like this:

[![](/static/identity/sms-retriever/flow-overview.png)](https://developers.google.com/static/identity/sms-retriever/flow-overview.png)

1. A user initiates SMS verification in your app. Your app might prompt the
   user to provide a phone number or use the
   [Smart Lock for Passwords hint selector](https://developers.google.com/identity/smartlock-passwords/android/retrieve-hints)
   if that information wasn't required to create the user's account.
2. Your app makes a request to your server to verify the user's phone number.
   Depending on what information is available in your user database, this
   request might include the user's ID, the user's phone number, or both.
3. At the same time, your app calls the SMS Retriever API to begin listening
   for an SMS response from your server.
4. Your server sends an SMS message to the user that includes a one-time code
   to be sent back to your server, and a hash that identifies your app.
5. When the user's device receives the SMS message, Google Play services uses
   the app hash to determine that the message is intended for your app, and
   makes the message text available to your app through the SMS Retriever API.
6. Your app parses out the one-time code from the message text and sends it
   back to your server.
7. Your server receives the one-time code from your app, verifies the code, and
   finally records that the user has successfully verified their account.

To implement automatic SMS verification in your app, see the Android and server
guides:

[Android Guide](https://developers.google.com/identity/sms-retriever/request)
[Server Guide](https://developers.google.com/identity/sms-retriever/verify)
