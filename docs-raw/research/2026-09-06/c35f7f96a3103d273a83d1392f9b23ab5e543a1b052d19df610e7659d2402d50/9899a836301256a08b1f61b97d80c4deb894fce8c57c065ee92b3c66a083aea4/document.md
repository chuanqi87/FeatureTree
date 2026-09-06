# Query Business Categories

Retrieve a paginated list of business categories using filters and sorting.

## Discussion

This endpoint returns a paginated list of business categories from the Maps taxonomy. Categories classify brands and locations. You use them to scope targeting and discovery within Apple Maps campaigns. An empty request body returns all categories with default pagination.

Each category has a `qualifiedId` using a dot to separate each level of the taxonomy hierarchy (for example, `dining.restaurant`). A single hierarchy level’s own name can itself contain underscores (for example, `association_or_organization`), so a dot always marks a hierarchy boundary, but an underscore doesn’t. Use the `text` value on a `CATEGORY` match-type [`Keyword`](/documentation/Apple-Ads-Platform-API/Keyword) to target Apple Maps searches within that category.

See [`QueryFilterOperator`](/documentation/Apple-Ads-Platform-API/QueryFilterOperator) for the full set of supported comparison operators.

### Filterable Fields

|Field |Type  |Operators    |Sortable|Description                          |
|------|:----:|:-----------:|:------:|-------------------------------------|
|`name`|string|`STARTS_WITH`|        |English display name of the category.|

Only `name` is confirmed filterable; other category fields (`id`, `qualifiedId`, `eligibility`) aren’t documented as query filters. The request body is a [`QueryRequest`](/documentation/Apple-Ads-Platform-API/QueryRequest) composed of [`QueryFilter`](/documentation/Apple-Ads-Platform-API/QueryFilter) conditions and [`QuerySort`](/documentation/Apple-Ads-Platform-API/QuerySort) directives ([`QuerySortOrder`](/documentation/Apple-Ads-Platform-API/QuerySortOrder)), controlled by [`QueryPagination`](/documentation/Apple-Ads-Platform-API/QueryPagination).

## Request Body

See [`QueryRequest`](/documentation/Apple-Ads-Platform-API/QueryRequest).

Each category record returned includes the following fields:

|Field             |Type  |Description                                                                                                                             |
|------------------|------|----------------------------------------------------------------------------------------------------------------------------------------|
|`id`              |string|Unique category identifier (MUID).                                                                                                      |
|`name`            |string|English display name of the category.                                                                                                   |
|`qualifiedId`     |string|Dot-delimited taxonomy path. Example: `dining.restaurant`.                                                                              |
|`eligibility`     |object|Ad serving eligibility for this category. See <doc://com.apple.apple-ads-platform-api/documentation/Apple-Ads-Platform-API/Eligibility>.|
|`creationTime`    |string|ISO-8601 creation timestamp. Read-only.                                                                                                 |
|`modificationTime`|string|ISO-8601 last-modified timestamp. Read-only.                                                                                            |

The `qualifiedId` format and eligibility status both carry specific rules:

|Constraint          |Detail                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|`qualifiedId` format|Dot-delimited hierarchy string. A dot always marks a hierarchy boundary, but an individual level’s name can itself contain underscores. Use this value as the `text` on a `CATEGORY` match-type Keyword.|
|Eligibility check   |Only categories with `ELIGIBLE` status can be used in active Apple Maps campaigns.                                                                                                                      |

## Payload Examples

**Query All Categories:**

Retrieve all business categories with default pagination.

### Request

```json
{}
```

### Response

```json
{
 "result": [
   {
     "id": "cat-din-001",
     "name": "Restaurant",
     "qualifiedId": "dining.restaurant",
     "creationTime": "2024-06-01T00:00:00Z",
     "modificationTime": "2024-06-01T00:00:00Z",
     "eligibility": {
       "status": "ELIGIBLE",
       "blockedGroups": [],
       "allowedGroups": []
     }
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Filter by Name:**

Find categories with a specific name prefix.

### Request

```json
{
 "filters": [
   {
     "field": "name",
     "operator": "STARTS_WITH",
     "value": "Dining"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "fetchTotalCount": true
 }
}
```

### Response

```json
{
 "result": [
   {
     "id": "cat-din-001",
     "name": "Dining",
     "qualifiedId": "dining",
     "eligibility": {
       "status": "ELIGIBLE"
     }
   },
   {
     "id": "cat-din-002",
     "name": "Dining - Restaurant",
     "qualifiedId": "dining.restaurant",
     "eligibility": {
       "status": "ELIGIBLE"
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
