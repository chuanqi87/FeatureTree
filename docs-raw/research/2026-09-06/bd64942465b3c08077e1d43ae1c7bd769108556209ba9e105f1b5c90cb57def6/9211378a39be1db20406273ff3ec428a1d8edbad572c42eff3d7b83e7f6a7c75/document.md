# Export Firebase data into Cloud Logging

Exporting data from various Firebase products into Cloud Logging lets you
view, search, filter, and query logs from your project and apps.
Using the exported data, you can create and use log-based metrics,
build charts and custom dashboards, and set up custom alerts.

The following products support data export to Cloud Logging:

* [**Firebase Crashlytics**](https://firebase.google.com/docs/crashlytics/cloud-logging-export):
  After you set up export, Firebase exports Crashlytics-collected events
  and (optionally) Firebase sessions data to Cloud Logging.
* [**Firebase Hosting**](https://firebase.google.com/docs/hosting/web-request-logs-and-metrics):
  After you set up export, Firebase exports web
  request logs from your Firebase Hosting sites to Cloud Logging.
* **Firebase App Hosting**:
  No need to set up export; Firebase automatically exports logs for
  Firebase App Hosting to Cloud Logging.
* [**Cloud Functions for Firebase**](https://firebase.google.com/docs/functions/writing-and-viewing-logs):
  No need to set up export; Firebase automatically exports logs for functions
  to Cloud Logging.

This page helps you with the following:

* [Understand what you can do with data exported to Cloud Logging](https://firebase.google.com/docs/projects/cloud-logging-export#understand-exports)
* [Set up export to Cloud Logging](https://firebase.google.com/docs/projects/cloud-logging-export#set-up-export)
* [Understand what happens after you set up export](https://firebase.google.com/docs/projects/cloud-logging-export#what-happens-after-setup)
* [Cloud Logging quotas, pricing, and retention](https://firebase.google.com/docs/projects/cloud-logging-export#quotas-pricing-retention)

## What can you do with data exported to Cloud Logging

Cloud Logging is provided by the
[Google Cloud Observability Suite](https://cloud.google.com/products/operations).

Here are some ways that you can work with data exported to Cloud Logging:

* You can use the
  [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface)
  in the Google Cloud console to view, search, and filter these logs.
* You can query your logs, create and use log-based metrics, build charts and
  custom dashboards, set up custom alerts, and store your logs data.
* You can export your data to other service providers.

Learn more about these options in the general
[Cloud Logging documentation](https://docs.cloud.google.com/logging/docs/overview),
as well as in the product-specific pages for
[Firebase Crashlytics](https://firebase.google.com/docs/crashlytics/cloud-logging-export) and
[Firebase Hosting](https://firebase.google.com/docs/hosting/web-request-logs-and-metrics).

Note that for Cloud Functions for Firebase, you can also view your logs in the
**Hosting & Serverless** >
[**Functions** dashboard](https://console.firebase.google.com/project/_/functions/list?useAutoProject=true)
of the Firebase console.

---



## Set up export to Cloud Logging

Here's how to set up export to Cloud Logging:

1. Sign in to the Firebase console, then select your project.
2. Go to the
   settings **Settings** >
   [**Integrations** tab](https://console.firebase.google.com/project/_/settings/integrations?useAutoProject=true).
3. On the **Cloud Logging** card, click **Link**.
4. Follow the on-screen instructions to set up export to Cloud Logging.

   If you already have one or more active apps or
   Firebase Hosting sites, the linking workflow displays an estimated
   data usage level for logs from each of your apps or sites. This value is
   estimated based on the volume of data from the previous 30 days.

### Unlink from Cloud Logging

Unlinking from Cloud Logging stops any new logs from being exported.

Unlinking from Cloud Logging can only stop export for
Firebase App Hosting, Firebase Hosting, and Firebase Crashlytics.
You cannot stop export of logs for Cloud Functions for Firebase.

Be aware of the following:

* Any data already exported into Cloud Logging will persist for the allowed
  retention time, and storage charges may still apply. You can manually delete
  your logs to prevent any further billing.
* If you have Cloud Logging data stored in other services (like
  BigQuery), that data might be governed by different terms for data
  persistence.

You can unlink from Cloud Logging at the Firebase project
level, at the product-level, or at the backend-, site-, or app-level for a
specific product.
**Caution:** Unlinking your Firebase project from Cloud Logging stops ***all***
data export from any Firebase product for which you've set up export to
Cloud Logging (except Cloud Functions for Firebase).

**Here's how to unlink from Cloud Logging:**

1. In the Firebase console, go to the
   settings **Settings** >
   [**Integrations** tab](https://console.firebase.google.com/project/_/settings/integrations?useAutoProject=true).
2. In the **Cloud Logging** card, click **Manage**.
3. Choose to unlink a specific product or to unlink a specific
   backend, site, or app for a specific product.

   To unlink your Firebase project entirely, find the button at the bottom of
   the page.
4. When prompted, confirm that you want to stop exports.

---



## What happens after you set up export?

After setting up data export, you can expect the following.

#### Firebase Crashlytics

* View logs for any new events within a few minutes of Crashlytics
  receiving the event.
* Monitor your data usage levels:

  + In the Firebase console, view the data usage level for logs from your
    linked apps in the
    settings **Settings** >
    **Integrations** >
    [**Cloud Logging** card](https://console.firebase.google.com/project/_/settings/integrations/cloudlogging?useAutoProject=true).
  + In the Google Cloud console, view your current and previous month's data
    usage in the
    [**Logs Storage** page](https://docs.cloud.google.com/logging/docs/store-log-entries).

#### Firebase Hosting

* View logs for any new requests to your Hosting sites usually within
  30 minutes of a request being made.
* Monitor your data usage levels:

  + In the Firebase console, view the data usage level for logs from your
    Hosting sites in the
    settings **Settings** >
    **Integrations** >
    [**Cloud Logging** card](https://console.firebase.google.com/project/_/settings/integrations/cloudlogging?useAutoProject=true).
  + In the Google Cloud console, view your per-site data usage level in the
    [**Logs Explorer**](https://cloud.google.com/logging/docs/view/logs-viewer-interface#getting_started)
    (specifically, the `log_bytes` metric). If your project uses
    Cloud Logging for other products, you can also view *total* usage
    in the Logs Explorer.

---



## Cloud Logging quotas, pricing, and retention

Cloud Logging offers a no-cost level of usage per month (per project).
The usage can be from any Google or Firebase product using Cloud Logging. You
can upgrade your project to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) to unlock additional
paid usage and features. Learn more about
[pricing for Cloud Logging](https://cloud.google.com/stackdriver/pricing).

You can monitor and manage Cloud Logging and billing:

* Estimate your Cloud Logging bills using the
  [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).
* Throttle logs by creating
  [exclusion filters for log sinks](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).
* Set up
  [alerts](https://docs.cloud.google.com/stackdriver/docs/observability/pricing-optimize-and-monitor#monitor)
  to help control costs.

Logs are automatically deleted after 30 days, with the option to set
[custom retention](https://docs.cloud.google.com/logging/docs/buckets#custom-retention).

Note that the log entry for a particular request or event may be delayed or, in
rare cases, dropped. While logs can be used to understand requests or events,
they may not reflect the true usage that appears in your project usage and
billing.
