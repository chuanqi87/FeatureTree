# Create an enterprise binding

**Note:** EMM partners intending to manage devices for an organization using the
Google Play EMM API **must use** the Google Play EMM API to create the
enterprise binding. For more information, see the
[Guide for Existing EMM Partners](https://developers.google.com/android/management/existing-emms).

An [`Enterprise`](https://developers.google.com/android/management/reference/rest/v1/enterprises)
resource binds an organization to your Android Management solution.
[`Devices`](https://developers.google.com/android/management/reference/rest/v1/enterprises.devices)
and [`Policies`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies)
both belong to an enterprise. Multiple enterprise bindings can be
associated with a single organization. For example, an organization may want
separate enterprise bindings for its different departments or regions.

The basic steps on how to create an enterprise binding are described in the
[Quickstart guide](https://developers.google.com/android/management/quickstart#create_an_enterprise).
This page outlines the process in more detail.

### 1. Retrieve the sign up url

Call [`signupUrls.create`](https://developers.google.com/android/management/reference/rest/v1/signupUrls/create)
to retrieve the sign up URL and specify the following two parameters:

* `callbackUrl`: An https URL the setup wizard redirects to after
  sign-up is complete. This is typically your management console.
* `projectId`: Your project ID.

The response contains a `url` and `name`. Open the `url` and note the `name`.

### 2. Enterprise IT admin completes the sign up flow

The `url` guides the IT admin through the sign-up process. If your EMM has not
been enabled for the BTE sign-up flow, then advise the IT admin that they need a
Gmail account that's not already associated with an enterprise binding.
After successfully registering their organization, the sign-up flow redirects to
your `callbackUrl`. An `enterpriseToken` is appended to the
`callbackUrl`.

#### Example

```
https://example.com/?enterpriseToken=EAH2pBTtGCs2K28dqhq5uw0uCyVzYMqGivap4wdlH7KNlPtCmlC8uyl
```



### 3. Create an enterprise binding

To create an enterprise binding, call
[`enterprises.create`](https://developers.google.com/android/management/reference/rest/v1/enterprises/create).
In addition to creating a unique enterprise binding ID, this method allows you
to define certain binding-specific settings. For instance, you can set the
predominant color displayed during device provisioning (`primaryColor`), along
with the name or title (`enterpriseDisplayName`) and logo
(`logo`) that’s shown to end users.

### Example

The following example uses the [Java client library](https://developers.google.com/android/management/create-enterprise) to create an enterprise
binding and return its name. See the [sample](https://developers.google.com/android/management/sample-app)
page for more details about using the library.

```
private String createEnterprise(AndroidManagement androidManagementClient)
    throws IOException {
  SignupUrl signupUrl =
      androidManagementClient
          .signupUrls()
          .create()
          .setProjectId("myProject")
          .setCallbackUrl("https://example.com/myEmmConsole")
          .execute();

  String enterpriseToken = displayUrlToAdmin(signupUrl.getUrl());

  Enterprise enterprise =
      androidManagementClient
          .enterprises()
          .create(new Enterprise())
          .setProjectId("myProject")
          .setSignupUrlName(signupUrl.getName())
          .setEnterpriseToken(enterpriseToken)
          .execute();

  return enterprise.getName();
}

/**
 * Displays the signup URL to the admin and returns the enterprise token which
 * is generated after the admin goes through the signup flow. This functionality
 * must be implemented by your management console.
 */
private String displayUrlToAdmin(String url) {
  ...
}
```
