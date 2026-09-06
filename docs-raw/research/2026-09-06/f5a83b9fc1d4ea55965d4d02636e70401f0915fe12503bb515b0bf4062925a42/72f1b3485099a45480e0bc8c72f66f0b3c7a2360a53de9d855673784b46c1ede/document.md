# Query App Locale Details

Return the default product page locale details for an app identified by its adamId.

## Discussion

This endpoint returns the default product page locale details for an app identified by its `adamId`. The default product page represents the app’s main App Store listing: the page that all users see unless directed to a custom product page.

In App Store Connect, there is no explicit “default product page” entity. The app’s main listing is the default. This endpoint surfaces that listing through the same `AppLocaleDetails` structure, so the response format is consistent across both endpoints.

To quickly fetch the default page content for an app without needing to first look up the product page ID, use this endpoint. Each object in the result corresponds to one supported language for the default product page.

Keep the following constraints in mind when querying default locale details:

|Constraint              |Detail                                                                                                                                                                                                                      |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Default page only       |This endpoint returns only the default product page. Custom product pages require the Query Product Page Locale Details endpoint.                                                                                           |
|All locales returned    |This endpoint returns all locales configured for the default product page. Filter by `languageCode` in the request body `filters` array if you need a specific locale.                                                      |
|assetsByDevice structure|The `assetsByDevice` field maps each specific device type (for example, `iphone_6_5`, `iphone_6_7`) to a `DeviceAssetGroup` containing an `assets` array of asset references and an `appPreviewDeviceFallBackDevices` array.|

See [`QueryFilterOperator`](/documentation/Apple-Ads-Platform-API/QueryFilterOperator) for the full set of supported comparison operators.

### Filterable Fields

|Field         |Type  |Operators|Sortable|Description                                             |
|--------------|:----:|:-------:|:------:|--------------------------------------------------------|
|`languageCode`|string|         |        |Filter to a specific locale, such as `en-US` or `fr-FR`.|

The `adamId` field identifies the app via the URL path (`/v1/apps/{adamId}/locale-details/query`), not a request body filter. The request body is a [`QueryRequest`](/documentation/Apple-Ads-Platform-API/QueryRequest) composed of [`QueryFilter`](/documentation/Apple-Ads-Platform-API/QueryFilter) conditions and [`QuerySort`](/documentation/Apple-Ads-Platform-API/QuerySort) directives ([`QuerySortOrder`](/documentation/Apple-Ads-Platform-API/QuerySortOrder)), controlled by [`QueryPagination`](/documentation/Apple-Ads-Platform-API/QueryPagination).

## Payload Examples

**Get App Locale Details:**

### Request

Returns the default product page locale details for an app identified by its `adamId`. The default product page represents the app’s main App Store listing: the page that all users see unless directed to a custom product page.

```
POST https://api.ads.apple.com/v1/apps/123456789/locale-details/query
```

### Response

```json
{
 "result": [
   {
     "adamId": 123456789,
     "language": "en",
     "languageCode": "en-US",
     "isPrimaryLocale": true,
     "appName": "AwayFinder",
     "subTitle": "Find your next adventure",
     "promotionalText": "Now with personalized travel recommendations",
     "shortDescription": "The all-in-one travel discovery app.",
     "deviceClasses": [
       "IPHONE",
       "IPAD"
     ],
     "assetsByDevice": {
       "iphone_6_5": {
         "assets": [
           {
             "assetId": "41a91e19-e021-45bb-ac5a-5faec02f9445"
           },
           {
             "assetId": "52b02f2a-f132-56cc-bd6b-6gbfd13g0556"
           }
         ],
         "appPreviewDeviceFallBackDevices": []
       },
       "iphone_6_7": {
         "assets": [
           {
             "assetId": "63c13g3b-g243-67dd-ce7c-7hcge24h1667"
           }
         ],
         "appPreviewDeviceFallBackDevices": [
           "iphone_6_5"
         ]
       }
     }
   },
   {
     "adamId": 123456789,
     "language": "fr",
     "languageCode": "fr-FR",
     "isPrimaryLocale": false,
     "appName": "AwayFinder",
     "subTitle": "Trouvez votre prochaine aventure",
     "promotionalText": "Avec des recommandations de voyage personnalisées",
     "shortDescription": "L'application de découverte de voyages tout-en-un.",
     "deviceClasses": [
       "IPHONE"
     ],
     "assetsByDevice": {
       "iphone_6_5": {
         "assets": [
           {
             "assetId": "c5c641c8-026a-44fb-a3ce-0f78cab73cad"
           }
         ],
         "appPreviewDeviceFallBackDevices": []
       }
     }
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
