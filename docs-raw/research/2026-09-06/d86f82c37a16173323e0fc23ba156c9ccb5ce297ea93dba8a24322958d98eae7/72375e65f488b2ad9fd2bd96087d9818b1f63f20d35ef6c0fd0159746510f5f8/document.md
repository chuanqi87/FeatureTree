# Analytics

Get data about your apps and usage.

## Discussion

Use the Analytics Reports API to analyze your app’s performance on iOS and the App Store and find opportunities for improvement. To learn more about interpreting the data using the glossary of report fields and definitions, see <doc://com.apple.documentation/documentation/analytics-reports>.

To help protect user privacy, where appropriate, Apple is applying measures to protect personally identifable infomation. For specific reports, Apple adds noise or applies crowd anonymity, and uses both approaches for other reports. Apple only reports totals when a specific number of data points are available. For more infomation about these measures, see <doc://com.apple.documentation/documentation/Analytics-Reports/privacy>.

To download analytics reports, be sure you have one of the following user roles:

- ADMIN
- SALES AND REPORTS
- FINANCE

This table outlines which roles can use which resources:

|Role             |Manage requests                                                                                                                                                                                                           |List and download reports                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
|Admin            |``doc://com.apple.appstoreconnectapi/documentation/AppStoreConnectAPI/POST-v1-analyticsReportRequests`` and ``doc://com.apple.appstoreconnectapi/documentation/AppStoreConnectAPI/DELETE-v1-analyticsReportRequests-_id_``|``doc://com.apple.appstoreconnectapi/documentation/AppStoreConnectAPI/GET-v1-analyticsReportRequests-_id_-reports``|
|Finance          |                                                                                                                                                                                                                          |``doc://com.apple.appstoreconnectapi/documentation/AppStoreConnectAPI/GET-v1-analyticsReportRequests-_id_-reports``|
|Sales and Reports|                                                                                                                                                                                                                          |``doc://com.apple.appstoreconnectapi/documentation/AppStoreConnectAPI/GET-v1-analyticsReportRequests-_id_-reports``|

The Sales and Reports role can also read [`Download sales and trends reports`](/documentation/AppStoreConnectAPI/GET-v1-salesReports) in addition to Analytics Reports.

To learn more about roles, see [Program Roles](https://developer.apple.com/support/roles/).

> Note:
> If you have any questions about the data made available in this API, including about how Apple applies privacy measures to protect user privacy and complies with legal obligations, contact Apple through Feedback Assistant by selecting the following option:
> 
> Developer Tools & Resources > App Store Connect API > Data Request
> 
> [Learn more](https://support.apple.com/guide/feedback-assistant/welcome/mac) about how to use Feedback Assistant.

## Topics

### Essentials

[Downloading Analytics Reports](/documentation/AppStoreConnectAPI/downloading-analytics-reports)

Learn how to request and review data about your apps, their usage, engagement, and performance.

### Making, Reading, and Deleting Requests

[`POST /v1/analyticsReportRequests`](/documentation/AppStoreConnectAPI/POST-v1-analyticsReportRequests)

Request analytics reports for your apps.

[`GET /v1/apps/{id}/analyticsReportRequests`](/documentation/AppStoreConnectAPI/GET-v1-apps-_id_-analyticsReportRequests)

Read analytics report requests for a specific app.

[`GET /v1/analyticsReportRequests/{id}`](/documentation/AppStoreConnectAPI/GET-v1-analyticsReportRequests-_id_)

Get details for and the state of a specific analytics report request.

[`GET /v1/analyticsReportRequests/{id}/reports`](/documentation/AppStoreConnectAPI/GET-v1-analyticsReportRequests-_id_-reports)

Get a list of reports generated from a specific analytics report request.

[`GET /v1/analyticsReportRequests/{id}/relationships/reports`](/documentation/AppStoreConnectAPI/GET-v1-analyticsReportRequests-_id_-relationships-reports)

Get a list of reports Ids from a specific analytics report request.

[`DELETE /v1/analyticsReportRequests/{id}`](/documentation/AppStoreConnectAPI/DELETE-v1-analyticsReportRequests-_id_)

Remove a specific analytics report request.

### Reading Reports, Instances, and Segments

[`GET /v1/analyticsReports/{id}`](/documentation/AppStoreConnectAPI/GET-v1-analyticsReports-_id_)

Get details for a specific analytics report.

[`GET /v1/analyticsReports/{id}/instances`](/documentation/AppStoreConnectAPI/GET-v1-analyticsReports-_id_-instances)

Read list of all the granularity options for a specific type of analytics report.

[`GET /v1/analyticsReportInstances/{id}`](/documentation/AppStoreConnectAPI/GET-v1-analyticsReportInstances-_id_)

Get details for a specific instance of an analytics report.

[`GET /v1/analyticsReportInstances/{id}/segments`](/documentation/AppStoreConnectAPI/GET-v1-analyticsReportInstances-_id_-segments)

Get details for a specific analytics report segment.

[`GET /v1/analyticsReportInstances/{id}/relationships/segments`](/documentation/AppStoreConnectAPI/GET-v1-analyticsReportInstances-_id_-relationships-segments)

Get Ids for a specific analytics report segment.

[`GET /v1/analyticsReportSegments/{id}`](/documentation/AppStoreConnectAPI/GET-v1-analyticsReportSegments-_id_)

Get details and download information for a specific analytics report segment.

[`GET /v1/analyticsReports/{id}/relationships/instances`](/documentation/AppStoreConnectAPI/GET-v1-analyticsReports-_id_-relationships-instances)

Read list of all the instance IDs for a specific type of analytics report.

### Objects

[`AnalyticsReportRequest`](/documentation/AppStoreConnectAPI/AnalyticsReportRequest)

A request to generate ongoing analytics reports for an app, specifying the report type and access frequency.

[`AnalyticsReportRequestCreateRequest`](/documentation/AppStoreConnectAPI/AnalyticsReportRequestCreateRequest)

The request body you use to create an analytics report request.

[`AnalyticsReportRequestResponse`](/documentation/AppStoreConnectAPI/AnalyticsReportRequestResponse)

The response body for endpoints that create or read an analytics report request.

[`AnalyticsReportRequestsResponse`](/documentation/AppStoreConnectAPI/AnalyticsReportRequestsResponse)

The response body for endpoints that list analytics report requests for an app.

[`AnalyticsReport`](/documentation/AppStoreConnectAPI/AnalyticsReport)

A generated analytics report containing App Store performance data produced from a report request.

[`AnalyticsReportResponse`](/documentation/AppStoreConnectAPI/AnalyticsReportResponse)

The response body for endpoints that read a single analytics report.

[`AnalyticsReportsResponse`](/documentation/AppStoreConnectAPI/AnalyticsReportsResponse)

The response body for endpoints that list analytics reports for a report request.

[`AnalyticsReportInstance`](/documentation/AppStoreConnectAPI/AnalyticsReportInstance)

A time-bounded instance of an analytics report, representing data for a specific reporting period.

[`AnalyticsReportInstanceResponse`](/documentation/AppStoreConnectAPI/AnalyticsReportInstanceResponse)

The response body for endpoints that read a single analytics report instance.

[`AnalyticsReportInstancesResponse`](/documentation/AppStoreConnectAPI/AnalyticsReportInstancesResponse)

The response body for endpoints that list instances of an analytics report.

[`AnalyticsReportSegment`](/documentation/AppStoreConnectAPI/AnalyticsReportSegment)

A downloadable segment within an analytics report instance, containing a portion of the report’s CSV data.

[`AnalyticsReportSegmentResponse`](/documentation/AppStoreConnectAPI/AnalyticsReportSegmentResponse)

The response body for endpoints that read a single downloadable segment of an analytics report.

[`AnalyticsReportSegmentsResponse`](/documentation/AppStoreConnectAPI/AnalyticsReportSegmentsResponse)

The response body for endpoints that list the downloadable segments of an analytics report instance.

[`AnalyticsReportInstanceSegmentsLinkagesResponse`](/documentation/AppStoreConnectAPI/AnalyticsReportInstanceSegmentsLinkagesResponse)

[`AnalyticsReportInstancesLinkagesResponse`](/documentation/AppStoreConnectAPI/AnalyticsReportInstancesLinkagesResponse)

[`AnalyticsReportRequestReportsLinkagesResponse`](/documentation/AppStoreConnectAPI/AnalyticsReportRequestReportsLinkagesResponse)

[`AppAnalyticsReportRequestsLinkagesResponse`](/documentation/AppStoreConnectAPI/AppAnalyticsReportRequestsLinkagesResponse)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
