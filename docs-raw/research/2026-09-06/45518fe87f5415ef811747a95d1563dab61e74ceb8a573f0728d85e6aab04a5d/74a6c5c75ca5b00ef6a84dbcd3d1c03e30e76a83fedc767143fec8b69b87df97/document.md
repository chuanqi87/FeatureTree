# One-tap SMS verification with the SMS User Consent API

The SMS User Consent API complements the SMS Retriever API by allowing an app
to prompt the user to grant access to the content of a single SMS message. When
a user gives consent, the app will then have access to the entire message body
to automatically complete SMS verification.

**Note:** The [SMS Retriever API](https://developers.google.com/identity/sms-retriever/overview)
offers the best user experience for automating the SMS-based user verification
process. However, there are situations where you don't control the format of the
SMS message and cannot support the SMS Retriever API. In this case, you can use
this API to streamline the process.


## User Flow for SMS User Consent API

When using the SMS User Consent API to automatically fill in one-time codes the
user will be prompted to allow your app to have permission to read a single SMS
message. The user will see the following screens when using the SMS User
Consent API.

![](/static/identity/sms-retriever/user-consent/user-consent-1.png)
![](/static/identity/sms-retriever/user-consent/user-consent-2.png)
![](/static/identity/sms-retriever/user-consent/user-consent-3.png)

When the user initiates an SMS verification flow they will be prompted to enter
the one-time code using the keyboard. It is important to do this to handle a
situation where the user receives the SMS on a different device than the app is
running on.

Then, if your app has requested SMS User Consent, an incoming SMS message
containing a one-time code will be shown to the user with an option to to share
the entire content of a single SMS message. This will only happen if your app
has requested SMS User Consent and is running on the device that received the
SMS message.

If the user chooses to provide the content of the SMS message to your app, the
entire text of the SMS message will be shared. The user sees the SMS
verification flow automatically complete.

If the user decides not to share, the user will then manually type the one-time
code to complete the SMS verification flow.

## Developer Flow for SMS User Consent API

To implement a full SMS verification flow using the SMS User Consent API you
need to interact with both a backend server to send the SMS as well as the SMS
User Consent API to prompt the user for access to a single message containing a
one-time code.

Step by step, your app and server must do the following to implement an SMS
verification flow using the SMS User Consent API:

1. Your app calls the SMS User Consent API to begin listening for an SMS
   response from the server. An SMS message received prior to starting SMS
   User Consent will not be forwarded to your app.
2. After you start the SMS User Consent API, your app makes a request to a
   server to verify a user's phone number using SMS verification.
3. When the user's device receives the SMS message containing a one-time
   code, Google Play services displays the contents of the message to the user
   and asks for consent to make that text available to your app.
4. If the user consents, the entire SMS message is made available to your app.
5. Your app parses out the one-time code from the message text and sends it
   to the server.

See [Request one-time consent to read an SMS verification code](https://developers.google.com/identity/sms-retriever/user-consent/request) for
details.
