# Cloud Logging

Fleet Engine offers a basic logging service for its API requests and
response payloads. You can use these logs to analyze, monitor, and debug your
applications. For details about Fleet Engine, see [What is the Fleet
Engine service?](https://developers.google.com/maps/documentation/mobility/fleet-engine/essentials).

Fleet Engine sends service-specific logs to Cloud Logging, so
that you can use the Google Cloud console Logs Explorer, the
Cloud Logging API, or command-line commands to access and analyze them.
The following list describes these key aspects of Cloud Logging.

* **Cloud Logging** is a managed service that lets you store, search,
  analyze, monitor, and alert on logging data and events from Google Cloud and
  other sources. For more information, see the [Cloud Logging
  documentation](https://cloud.google.com/logging/docs) and [Cloud platform logs](https://cloud.google.com/logging/docs/api/platform-logs) in
  the Cloud documentation.
* **Logs Explorer** is a tool of the Google Cloud console that
  lets you retrieve, view, and analyze log entries. For details, see [View
  logs by using the Logs Explorer](https://cloud.google.com/logging/docs/view/logs-explorer-interface).
* The **Cloud Logging API** lets you programmatically accomplish
  logging-related tasks, including reading and writing log entries and
  creating log-based metrics. To learn more, see [Cloud Logging API
  overview](https://cloud.google.com/logging/docs/reference/api-overview).
* The **Google Cloud CLI** has a group of commands that provide a command-line
  interface to the Cloud Logging API. For details, see [Google Cloud
  Command Line Interface](https://cloud.google.com/cli) and [gcloud logging](https://cloud.google.com/sdk/gcloud/reference/logging)

**Note:** Cloud Logging has usage and retention limits. To understand how
to manage your logging costs and avoid unexpected charges, see [Google Cloud
Observability pricing](https://cloud.google.com/stackdriver/pricing#logging-costs).


## Fleet Engine logs

Fleet Engine sends the following information to
Cloud Logging:

* All Authenticated REST and gRPC requests and responses.
* Error responses.
* Requests, responses, and error messages from calls initiated to
  Fleet Engine by the [Driver SDK](https://developers.google.com/maps/documentation/mobility/driver-sdk).

For a list of all available log messages and schema, see the [Fleet Engine API
Logging Integration Reference for on-demand trips](https://developers.google.com/maps/documentation/mobility/operations/cloud-logging/reference/tasks/rest) and the [Fleet Engine API
Logging Integration Reference for scheduled tasks](https://developers.google.com/maps/documentation/mobility/operations/cloud-logging/reference/trips/rest).

## What's next

To get started with Cloud Logging, see [Set up
Cloud Logging](https://developers.google.com/maps/documentation/mobility/operations/cloud-logging/setup).
