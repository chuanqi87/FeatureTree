# Monitor costs, usage, and other metrics

Monitoring the costs, usage, and other metrics of your AI features is an
important part of running a production app. You need to know what normal usage
patterns look like for your app and make sure you're staying within thresholds
that matter to you.

This page describes some recommended options to monitor your costs, usage,
and other metrics in both the Firebase console and the Google Cloud console.

## Monitor costs

In the
[*Usage and Billing* dashboard](https://console.firebase.google.com/u/0/project/_/usage?useAutoProject=true)
of the Firebase console, you can view your project's costs for calling the
Agent Platform Gemini API (formerly Vertex AI) and the Gemini Developer API (when you're
on the Blaze pricing plan).

**The costs displayed on the dashboard are *not* necessarily specific to calls
using the Firebase AI Logic client SDKs.** The displayed costs
are associated with *any* calls to those "Gemini APIs", whether they be using
the Firebase AI Logic client SDKs, the
Google GenAI server SDKs, Genkit, the Firebase Extensions for the
Gemini API, REST calls, one of the AI Studios, or other API clients.

Learn more about [pricing](https://firebase.google.com/docs/ai-logic/pricing) for the products associated
with your use of Firebase AI Logic.

### Set up budget alerts and spend caps

When you're on Blaze pricing plan, avoid surprise bills by setting up
budgets, and then specifically setting up
[**budget alerts**](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budgets)
and
[**budget spend caps**](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-spend-cap).

Note that budget alerts are *not* budget caps. An alert will send you
communications when you're approaching or surpassed your configured threshold so
that you can take action in your app or project. **You need to set a
*budget spend cap* if you want the service to be paused when your budget is
reached.**

## Observe usage of your AI features in the Firebase console

You can enable AI monitoring in the [**Firebase AI Logic** page](https://console.firebase.google.com/project/_/ailogic/?useAutoProject=true) of the
Firebase console so that you can observe various app-level metrics and usage
to gain comprehensive visibility into your requests from the
Firebase AI Logic client SDKs. These dashboards are more
in-depth than the basic token counts you get from a call to the
[Count Tokens API](https://firebase.google.com/docs/ai-logic/count-tokens).

**Note:** AI monitoring in the Firebase console doesn't support calls to the
Gemini Live API models.

**Key capabilities of AI monitoring in the Firebase console include:**

* Viewing quantitative metrics like request volume, latency, errors, and
  per modality token usage for each of your apps.
* Inspecting traces to see your requests' attributes, inputs, and outputs,
  which can help with debugging and quality improvement.
* Slicing data by dimensions like request status, minimum latency, model
  name, and more.

All of these features are built using Google Cloud Observability Suite (see
[detailed product information](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-products-used) below).

### Enable AI monitoring

All our docs assume that you're using the
[latest versions](https://firebase.google.com/support/releases)
of the Firebase AI Logic SDKs.

**Here are the ways that you can enable AI monitoring in the
Firebase console:**

* When you go through the initial guided setup workflow from the
  **AI Services** > [**Firebase AI Logic** page](https://console.firebase.google.com/project/_/ailogic/?useAutoProject=true)
* At any time in the **AI Services** > **AI Logic** >
  [**Settings** tab](https://console.firebase.google.com/project/_/ailogic/settings?useAutoProject=true)

**Requirements for enabling and using AI monitoring:**

* You must be a project Owner, Editor, or
  Firebase Vertex AI Admin.
* Your app must use *at minimum* these Firebase library versions:  
  **iOS+**: v11.13.0+ |
  **Android**: v16.0.0+ (BoM: v33.14.0+) |
  **Web**: v11.8.0+ |
  **Flutter**: v2.0.0+ (BoM: v3.11.0+) |
  **Unity**: v12.9.0+
* Your app must have opt-in data collection ***enabled*** (this is enabled by
  default).

After your app meets these requirements and you enable AI monitoring in the
console, you don't need to do anything else in your app or the console to start
seeing data populate the dashboards in the **AI Services** > **AI Logic** >
[**AI monitoring** tab](https://console.firebase.google.com/project/_/ailogic/monitoring?useAutoProject=true).
There might be a slight delay (sometimes up to 5 minutes) before telemetry from
a request is available in the Firebase console.

### Advanced usage

This section describes the sampling rate configuration, as well as different
options for viewing and working with your data.

#### Sampling rate

If you're making a large number of requests, we recommend taking advantage of
the sampling rate configuration. The sampling rate indicates the proportion of
requests for which *trace details* are actually collected.

In the **AI Services** > **AI Logic** >
[**Settings** tab](https://console.firebase.google.com/project/_/ailogic/settings?useAutoProject=true)
of the Firebase console, you can configure sampling rate for your project to
a value from 1 to 100%, where 100% means AI monitoring will collect traces from
all of your traffic. The default is 100%. Collecting fewer traces will reduce
your costs, but it will also reduce the number of traces you can monitor. Note
that regardless of your sampling rate, the graphs shown in the monitoring
dashboard will always reflect the true volume of traffic.

#### Additional options outside of the Firebase console

In addition to the AI monitoring available in the Firebase console, consider
these options:

* Explore
  [Vertex AI Model Garden](https://console.cloud.google.com/monitoring/dashboards/integration/vertex_ai.vertex-ai-model-garden).  
  These dashboards provide further trend insights into latency and throughput
  for the managed models, complementing your insights from AI monitoring in
  the Firebase console.
* Explore and use your data with
  [Google Cloud Observability Suite](https://cloud.google.com/products/observability)  
  Since telemetry data for AI monitoring is stored in Google Cloud Observability Suite
  associated with your project, you can explore your data in its dashboards,
  including Trace Explorer and Logs Explorer, which are linked to when
  you inspect your individual traces in the Firebase console. You can also
  use your data to build custom dashboards, set up alerts, and more.

### Detailed information about products used for AI monitoring

AI monitoring stores your telemetry data in various products available in
[Google Cloud Observability Suite](https://cloud.google.com/products/observability),
including Cloud Monitoring, Cloud Trace, and Cloud Logging.

* **Cloud Monitoring**: Stores metrics, including number of requests,
  success rate, and request latency.
* **Cloud Trace**: Stores traces for each of your requests so that you can
  view details individually, instead of in aggregate. A trace is typically
  associated with logs so that you can examine the content and timing of each
  interaction.
* **Cloud Logging**: Captures input, output, and configuration metadata to
  provide rich detail about each part of your AI request.

Since your telemetry data is stored in these products, you can specify your
retention and access settings directly within each product (learn more in the
documentation for
[Cloud Monitoring](https://cloud.google.com/monitoring/quotas#data_retention_policy),
[Cloud Trace](https://cloud.google.com/trace/docs/trace-export-overview)
, and
[Cloud Logging](https://cloud.google.com/logging/docs/buckets)).

Note that AI monitoring stores the *actual* prompts and generated output from
each sampled request in Cloud Logging so that this data is accessible in the
Firebase console. You can optionally
[disable storing prompts and responses](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-disable-storing-prompts-responses).

**Important:** If you use
[Grounding with Google Search](https://firebase.google.com/docs/ai-logic/grounding-google-search#ai-monitoring),
it's your responsibility to ensure that the retention period, or any custom
period you set, fully aligns with your specific use case and any additional
compliance requirements for your chosen Gemini API provider:
[Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search)
or Agent Platform Gemini API (formerly Vertex AI) (see
[Service Terms](https://cloud.google.com/terms/service-terms)
section within the Service Specific Terms). You may need to
[adjust the retention period in Cloud Logging](https://cloud.google.com/logging/docs/buckets)
to meet these requirements.


#### Pricing

* **Projects on the no-cost Spark pricing plan** (available only when using the
  Gemini Developer API):
  Usage of the underlying services for AI monitoring is free of charge.
* **Projects on the pay-as-you-go Blaze pricing plan**:
  You'll be charged for the usage of the underlying Google Cloud Observability Suite products that
  AI monitoring uses (regardless of your chosen
  Gemini API provider). However, each Google Cloud Observability Suite product has generous
  no-cost tiers. Learn more in the
  [Google Cloud Observability Suite pricing documentation](https://cloud.google.com/products/observability#pricing).

#### *(Optional)* Disable storing prompts and responses

By default, AI monitoring captures the *actual* prompts sent to the model and
the responses generated by the model, including any *sensitive information (like
Personally Identifiable Information (PII))* in those prompts and responses. All
this data is stored in Cloud Logging so that it's accessible in the
Firebase console.

To disable the storage of prompts and responses, add the following
**exclusion filter** to your
[Cloud Logging sink](https://cloud.google.com/logging/docs/export/configure_export_v2#filter-examples)
(typically the `_Default` sink):
`resource.type="firebasevertexai.googleapis.com/Model"`.

## View project-level API metrics in the Google Cloud console

For each API, you can view project-level metrics, like usage, in the
Google Cloud console.

Note that the Google Cloud console pages described in this section do *not*
include information like request and response content and token count.
To monitor that type of information, consider using
[AI monitoring in the Firebase console](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console)
(see previous section).

1. In the Google Cloud console, go to the **Metrics** page of the API you
   want to view:

   * [**Agent Platform API**](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=_):
     View the usage associated with *any* request to the
     Agent Platform Gemini API (formerly Vertex AI).

     + Includes requests using
       Firebase AI Logic client SDKs,
       the Google GenAI server SDKs, Genkit, the Firebase Extensions
       for the Gemini API, REST API, Agent  Studio, etc.
   * [**Gemini Developer API**](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?project=_):
     View the usage associated with *any* request to the
     Gemini Developer API.

     + Includes requests using the
       Firebase AI Logic client SDKs,
       the Google GenAI server SDKs, Genkit, the Firebase Extensions
       for the Gemini API, REST API, Google AI Studio, etc.
     + The display name of this API in the Google Cloud console
       is "Generative Language API".

   If you find yourself on an "overview page" for the API, click
   **Manage**, and then click the **Metrics** tab.

   **Note:** In the Google Cloud console, you can also view project-level metrics
   for the
   [Firebase AI Logic API](https://console.cloud.google.com/apis/library/firebasevertexai.googleapis.com?project=_),
   which is the proxy service for Firebase AI Logic. These metrics will
   reflect requests *only* from the
   Firebase AI Logic client SDKs.
2. Use the drop-down menus to view the metrics of interest, like traffic
   by response code, errors by API method, overall latency, and latency by API
   method.
