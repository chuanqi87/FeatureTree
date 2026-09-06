# Error codes

This page provides troubleshooting of common error codes for the Gemini API
and the Firebase AI Logic SDKs.

#### **400 error**: `API key not valid. Please pass a valid API key.`

If you receive a 400 error that says
`API key not valid. Please pass a valid API key.`, it usually means that the
API key in your Firebase configuration file/object doesn't exist or isn't setup
to be used with your app and/or Firebase project.

Check that the API key listed in your Firebase configuration file/object matches
the API key for your app. You can view all your API keys in the
[*APIs & Services* > *Credentials*](https://console.cloud.google.com/apis/credentials?project=_)
panel in the Google Cloud console.

If you discover that they don't match, then
[obtain a fresh Firebase configuration file/object](https://support.google.com/firebase/answer/7015592),
and then *replace* the one that's in your app. The fresh config file/object
should contain a valid API key for your app and Firebase project.

#### **400 error**: `Service agents are being provisioned ... Service agents are needed to read the Cloud Storage file provided.`

If you're trying to send a multimodal request with a Cloud Storage for Firebase
URL, you might encounter the following 400 error:  
`Service agents are being provisioned ... Service agents are needed to read the Cloud Storage file provided.`

This error is caused by a project that didn't have the required service agents
correctly auto-provisioned when the Agent Platform API was enabled in
the project. This is a known issue with some projects, and we're working on a
global fix.

Here's the workaround to fix your project and correctly provision these service
agents so that you can start including Cloud Storage for Firebase URLs in your
multimodal requests. You must be an
[Owner](https://firebase.google.com/docs/projects/iam/roles-basic) on the project, and you only need to
complete this set of tasks once for your project.

1. Access and authenticate with the gcloud CLI.  
   The easiest way to do this is from Cloud Shell. Learn more in the
   [Google Cloud documentation](https://cloud.google.com/shell/docs/launching-cloud-shell).
2. If prompted, follow the instructions displayed in the terminal to make the
   gcloud CLI run against your Firebase project.

   You'll need your Firebase project ID, which you can find at the top of the
   settings
   [*Project settings*](https://console.firebase.google.com/project/_/settings/general/)
   in the Firebase console.
3. Provision the required service agents in your project by running the
   following command:

   ```
   curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"  https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/endpoints -d ''
   ```
4. Wait a few minutes to ensure that the service agents are provisioned, and
   then retry sending your multimodal request that includes the
   Cloud Storage for Firebase URL.

If you're still getting this error after waiting several minutes, reach out to
[Firebase Support](https://firebase.google.com/support/troubleshooter/contact).

#### **403 error**: `PERMISSION_DENIED: To access this model, you must enforce Firebase App Check. Learn more: https://firebase.google.com/docs/ai-logic/app-check`

If you receive a `403 - PERMISSION_DENIED` error that says
`To access this model, you must enforce Firebase App Check. Learn more: https://firebase.google.com/docs/ai-logic/app-check`,
it means that your request doesn't have a valid App Check token and you're
attempting to access a model that's commonly abused.

Some generative models have been identified as common for malicious actors to
abuse.

Because you don't have App Check enforced for Firebase AI Logic, your
project is vulnerable to abuse of these models. To help protect our developers,
Firebase blocks access to these models unless the request includes a valid
App Check token (meaning App Check is enforced for
Firebase AI Logic).

**Warning:** **Starting November 2, 2026, Firebase App Check enforcement will be
*required* to use Firebase AI Logic**.
[Learn more.](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#security-app-check)

If you want to access the model that returned the error, do the following:

1. [**Set up App Check for Firebase AI Logic.**](https://firebase.google.com/docs/ai-logic/app-check#set-up-app-check)
   For local development, make sure that you set up the
   App Check *debug provider*.

   Enforcing App Check is critical to help protect the Gemini API and
   Gemini models from abuse, and its enforcement is required to clear
   this error.
2. **Resend the request from your app to Firebase AI Logic.**

   This request will send along a valid App Check token, and you'll no
   longer get this `403 - PERMISSION_DENIED` error.
3. Before you release your app to end-users, you need to
   [**set up a production attestation provider**](https://firebase.google.com/docs/ai-logic/app-check#configure-for-production)
   (like App Attest, Play Integrity, or reCAPTCHA Enterprise) so that
   your end-users can access your AI feature when App Check is enforced.

#### **403 error**: `PERMISSION_DENIED: Firebase AI Logic has been deactivated in this project. To resume using Firebase AI Logic, you must enforce Firebase App Check. Learn more: https://firebase.google.com/docs/ai-logic/app-check`

If you receive a `403 - PERMISSION_DENIED` error that says
`Firebase AI Logic has been deactivated in this project. To resume using
Firebase AI Logic, you must enforce Firebase App Check. Learn more:
https://firebase.google.com/docs/ai-logic/app-check`,
it means that your Firebase project has been identified as inactive and you
don't have App Check enforced for Firebase AI Logic.

"Inactive projects" are those that have Firebase AI Logic enabled, but don't
have any recent usage of Firebase AI Logic.

Because you don't have App Check enforced for Firebase AI Logic, your
project is vulnerable to abuse of the Gemini API. To help protect your
project, Firebase deactivated usage of Firebase AI Logic until you enforce
App Check for Firebase AI Logic.

**Warning:** **Starting November 2, 2026, Firebase App Check enforcement will be
*required* to use Firebase AI Logic**.
[Learn more.](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#security-app-check)

When you're ready to start using Firebase AI Logic again, do the
following:

1. [**Set up App Check for Firebase AI Logic.**](https://firebase.google.com/docs/ai-logic/app-check#set-up-app-check)
   For local development, make sure that you set up the
   App Check *debug provider*.

   Enforcing App Check is critical to help protect the Gemini API and
   Gemini models from abuse, and its enforcement is required to clear
   this error.
2. **Resend the request from your app to Firebase AI Logic.**

   This request will send along a valid App Check token, and you'll no
   longer get this `403 - PERMISSION_DENIED` error.
3. Before you release your app to end-users, you need to
   [**set up a production attestation provider**](https://firebase.google.com/docs/ai-logic/app-check#configure-for-production)
   (like App Attest, Play Integrity, or reCAPTCHA Enterprise) so that
   your end-users can access your AI feature when App Check is enforced.

#### **403 error**: `PERMISSION_DENIED: The caller does not have permission.`

If you receive a 403 error that says
`PERMISSION_DENIED: The caller does not have permission.`, it usually means that
the API key in your Firebase configuration file/object belongs to a different
Firebase project.

Check that the API key listed in your Firebase configuration file/object matches
the API key for your app. You can view all your API keys in the
[*APIs & Services* > *Credentials*](https://console.cloud.google.com/apis/credentials?project=_)
panel in the Google Cloud console.

If you discover that they don't match, then
[obtain a fresh Firebase configuration file/object](https://support.google.com/firebase/answer/7015592),
and then *replace* the one that's in your app. The fresh config file/object
should contain a valid API key for your app and Firebase project.

#### **403 error**: `Requests to this API firebasevertexai.googleapis.com ... are blocked.`

If you receive a 403 error that says
`Requests to this API firebasevertexai.googleapis.com ... are blocked.`, it
usually means that the API key in your Firebase configuration in your app has
restrictions that prevent it from calling the required API.

To fix this, you need to update your API key's restrictions in the
Google Cloud console to include the required API. For Firebase AI Logic,
you must ensure the *Firebase AI Logic API*
(`firebasevertexai.googleapis.com`) is included in the list of selected
APIs that can be called using the API key.

Follow these steps:

1. In the Google Cloud console, open the
   [*APIs & Services* > *Credentials*](https://console.cloud.google.com/apis/credentials?project=_)
   panel.
2. Select the API key that your application is configured to use (for example,
   the "iOS key" for an iOS app).
3. On the *Edit API key* page, find the *API restrictions* section.
4. Ensure the **Restrict key** option is selected. If it isn't, your key is
   unrestricted, and this is likely not the source of the error.

   **Note:** If you have an unrestricted API key, we strongly recommend that you
   apply
   ["API restrictions"](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key)
   to your Firebase API key.
5. In the *Selected APIs* drop-down menu, search for and select the
   *Firebase AI Logic API* to add it to the list of selected
   APIs that can be called using the API key.
6. Click **Save**.

   It may take up to five minutes for the changes to take effect.

**Note:** Firebase-related APIs use API keys only to *identify* the Firebase project
or app, *not for authorization* to call the API (like some other APIs allow).
Authorization for Firebase-related APIs is handled separately from the API key,
either through Google Cloud IAM permissions, Firebase Security Rules, or
Firebase App Check. Learn more about
[Firebase API keys](https://firebase.google.com/docs/projects/api-keys).

#### **404 error**: `Firebase AI Logic genai config not found`

If you receive a 404 error that says `Firebase AI Logic genai config not found`,
it usually means that a setting for Firebase AI Logic is misconfigured or
missing.

Here are the most likely causes of this error:

* You haven't yet set up your Firebase project for a Gemini API provider.

  What to do:  
  In the Firebase console, go to **AI Services** >
  [**AI Logic**](https://console.firebase.google.com/project/_/ailogic/?useAutoProject=true). Click **Get started**, and then select
  your chosen Gemini API provider. Enable the API, and Firebase will set up
  your project for that provider. After completing the workflow, try your
  request again.
* If you very recently went through the Firebase AI Logic setup workflow in
  the Firebase console, then the configuration for Firebase AI Logic
  might not yet be available to all required backend services in all applicable
  regions.

  What to do:  
  Wait a few minutes, and then try your request again.

#### **404 error**: the model "`was not found or your project does not have access to it`"?

For example: "`Publisher Model projects/PROJECT-ID/locations/us-central1/publishers/google/models/gemini-3.1-pro-preview was not found or your project does not have access to it. Please ensure you are using a valid model version.`"

There are a couple different reasons why you could get an error like this.

* **Invalid model name**

  + **Cause**: The model name you've provided isn't a valid model name.
  + **Fix**: Check your model name and model version against the list of all
    [supported and available models](https://firebase.google.com/docs/ai-logic/models#available-model-names).
    Be sure to check the segments and their order in the model name.
    For example:

    - Latest Gemini 3.x Pro
      model name: `gemini-3.1-pro-preview` (only available in preview)
    - Latest Gemini 3.x Flash
      model name: `gemini-3.7-flash`
    - Latest Gemini 3.x Flash‑Lite
      model name: `gemini-3.5-flash-lite`
    - Latest Gemini 3.x Pro Image (aka "Nano Banana Pro")
      model name: `gemini-3-pro-image`
    - Latest Gemini 3.x Flash Image (aka "Nano Banana 2")
      model name: `gemini-3.1-flash-image`
    - Latest Gemini 3.x Flash‑Lite Image (aka "Nano Banana 2 Lite")
      model name: `gemini-3.1-flash-lite-image`
    - Latest Gemini 2.5 Flash Image (aka "Nano Banana")
      model name: `gemini-2.5-flash-image`
* **Invalid location**
  *(only applicable if using the Agent Platform Gemini API (formerly Vertex AI) provider)*

  + **Cause**: Your request might be trying to access a model in a location
    where the model isn't available.
  + **Fix**: Make sure your request is trying to access the model where it's
    available.

    When using the Agent Platform Gemini API (formerly Vertex AI), you can optionally specify a
    location to access the model during initialization. If you don't specify a
    location, then Firebase AI Logic defaults to the following locations:

    - When using the "Agent Platform" initialization syntax: `global`
    - When using the legacy "Vertex AI" initialization syntax: `us-central1`

    However, not all models are supported in these default locations. This
    means that, depending on the model, it might be required to *explicitly*
    set a specific location during initialization.

    - **Gemini *preview* and *experimental* models:** Only available
      in the `global` location.
    - **Gemini 3.x stable models:** Available
      in the `global` location and often in the `us` and `eu` locations.
    - **Gemini 2.5 models:**
      [Available in many locations](https://firebase.google.com/docs/ai-logic/locations?api=vertex#available-locations-older-models).
      Note that Gemini Live API 2.5 models are *not* available in `global`.

  Learn more about how to
  [specify the location for accessing the model](https://firebase.google.com/docs/ai-logic/locations?api=vertex)
  (including code snippets).

#### **429 errors**: `"You exceeded your current quota, please check your plan and billing details"` or `"Resource exhausted, please try again later."`

There are a couple different reasons why you could get an error like this.

* **You're going over your quota or the model you're accessing is overloaded by
  requests from other people.**

  The action to take depends on whether you're using the
  Gemini Developer API or Agent Platform Gemini API (formerly Vertex AI). For more
  information about quotas and how to request additional quota, see
  [Rate limits and quotas](https://firebase.google.com/docs/ai-logic/quotas).

  If you're using the Agent Platform Gemini API (formerly Vertex AI), the Google Cloud
  documentation provides some additional context and guidance for
  [Error code 429](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/error-code-429).
* **You're attempting to use a model or a feature that requires billing, but
  your Firebase project is on the Spark pricing plan.**

  If you're using the Gemini Developer API, you can get limited access
  to certain models and access to many basic features while on the
  Gemini Developer API "free tier". This tier lets you get started
  without having to provide a payment method, which means you don't need to
  upgrade your Firebase project to the pay-as-you-go Blaze pricing plan.

  + Some models aren't available on the Gemini Developer API "free tier"
    and require the "paid tier", which means your project must be on the
    pay-as-you-go Blaze pricing plan. For example, the following models almost always
    require billing:

    - Most *preview* and *experimental* models
    - Image-generating models (the "Nano Banana" models)
  + Some models offer some basic features while on the
    Gemini Developer API "free tier", but then require the "paid tier"
    to use more advanced features. For example:

    - When using most of the Gemini 3.x models,
      Grounding with Google Search or Google Maps requires billing.

  Learn about the
  [Firebase pricing plans and the Gemini Developer API](https://firebase.google.com/docs/ai-logic/pricing?api=dev#api-provider-pricing-plans).

  For more details, see the Gemini Developer API
  [pricing documentation](https://ai.google.dev/gemini-api/docs/pricing)
  and
  [billing FAQ](https://ai.google.dev/gemini-api/docs/billing).
