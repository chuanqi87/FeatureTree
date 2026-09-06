# App Screenshot Sets

Create sets of app screenshots to upload to App Store Connect.

## Discussion

An `appScreenshotSets` resource represents a set of screenshots that you intend to upload to App Store Connect. Create an `appScreenshotSets` resource as a container for all screenshots associated with a locale and display target, for example, screenshots for Simplified Chinese on an iPhone with a 6.5” display. Next, upload individual screenshots using the [App Screenshots](/documentation/AppStoreConnectAPI/app-screenshots) resource.

> Important:
> Some screenshot sizes are required to submit your app for review. For more information, see [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/screenshot-specifications).

## Topics

### Getting Screenshot Sets and Reading Information

[`GET /v1/appScreenshotSets/{id}`](/documentation/AppStoreConnectAPI/GET-v1-appScreenshotSets-_id_)

Get an app screenshot set including its display target, language, and the screenshot it contains.

### Creating and Deleting Screenshot Sets

[`POST /v1/appScreenshotSets`](/documentation/AppStoreConnectAPI/POST-v1-appScreenshotSets)

Add a new screenshot set to an App Store version localization for a specific screenshot type and display size.

[`DELETE /v1/appScreenshotSets/{id}`](/documentation/AppStoreConnectAPI/DELETE-v1-appScreenshotSets-_id_)

Delete an app screenshot set and all of its screenshots.

### Listing and Reordering All Screenshots in a Set

[`GET /v1/appScreenshotSets/{id}/relationships/appScreenshots`](/documentation/AppStoreConnectAPI/GET-v1-appScreenshotSets-_id_-relationships-appScreenshots)

Get the ordered screenshot IDs in a screenshot set.

[`GET /v1/appScreenshotSets/{id}/appScreenshots`](/documentation/AppStoreConnectAPI/GET-v1-appScreenshotSets-_id_-appScreenshots)

List all ordered screenshots in a screenshot set.

[`PATCH /v1/appScreenshotSets/{id}/relationships/appScreenshots`](/documentation/AppStoreConnectAPI/PATCH-v1-appScreenshotSets-_id_-relationships-appScreenshots)

Change the order of the screenshots in a screenshot set.

### Objects and Data Types

[`AppScreenshotSet`](/documentation/AppStoreConnectAPI/AppScreenshotSet)

The data structure that represent an app screenshot set resource.

[`AppScreenshotSetCreateRequest`](/documentation/AppStoreConnectAPI/AppScreenshotSetCreateRequest)

The request body you use to create an app screenshot set.

[`AppScreenshotSetResponse`](/documentation/AppStoreConnectAPI/AppScreenshotSetResponse)

The response body for endpoints that create or read a set of app screenshots for a display size.

[`AppScreenshotSetsResponse`](/documentation/AppStoreConnectAPI/AppScreenshotSetsResponse)

The response body for endpoints that list app screenshot sets for an App Store version localization.

[`AppScreenshotSetAppScreenshotsLinkagesRequest`](/documentation/AppStoreConnectAPI/AppScreenshotSetAppScreenshotsLinkagesRequest)

A request body you use to reorder the screenshots in a screenshot set.

[`AppScreenshotSetAppScreenshotsLinkagesResponse`](/documentation/AppStoreConnectAPI/AppScreenshotSetAppScreenshotsLinkagesResponse)

A response body that contains a list of related resource IDs.

[`ScreenshotDisplayType`](/documentation/AppStoreConnectAPI/ScreenshotDisplayType)

A string that represents the display type of an app screenshot.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
