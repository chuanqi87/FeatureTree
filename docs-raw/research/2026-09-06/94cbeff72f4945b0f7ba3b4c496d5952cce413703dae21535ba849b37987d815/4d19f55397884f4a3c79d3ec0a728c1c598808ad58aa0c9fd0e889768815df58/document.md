# Manage data retention with TTL policies

This page describes how to use the Google Cloud console and the Google Cloud CLI
to configure time to live (TTL) policies. Before you read this page,
you should understand the
[Cloud Firestore data model](https://firebase.google.com/docs/firestore/data-model).

## Time to live overview

Use TTL policies to automatically
remove stale data from your databases. A TTL policy designates a given field as
the expiration time for documents in a given collection group. With TTL, you can
decrease storage costs by cleaning out obsolete data. Data is typically deleted
within 24 hours after its expiration date.

### Pricing

TTL delete operations count towards your document delete costs. For pricing
of delete operations, see [Cloud Firestore pricing](https://firebase.google.com/docs/firestore/pricing).

### Limits and constraints

* You can mark only one field per collection group as a TTL field.
* You can have a maximum of 1000 field level configurations. One field configuration
  can contain multiple configurations for the same field. For example,
  a single-field indexing exemption and a TTL policy on the same field count as
  one field configuration towards the limit.
* For Firestore in Datastore mode customers, TTL cannot be used with a concurrency mode of
  [Optimistic With Entity Groups](https://cloud.google.com/datastore/docs/concepts/transactions#concurrency_modes).
  Consider changing the concurrency mode to the [Optimistic concurrency mode](https://cloud.google.com/datastore/docs/upgrade-to-firestore#optimistic_with_entity_groups_concurrency_mode).

### TTL deletion

Note the following key behaviors of TTL-driven deletion:

* Deletion through TTL is not an instantaneous process. Expired documents
  continue to appear in queries and lookup requests until the TTL process
  actually deletes them. TTL trades deletion timeliness for the benefit of
  reduced total cost of ownership for deletions.
  Data is typically deleted within 24 hours after its expiration date.
* Deleting a document through TTL does not delete subcollections under that
  document.
* Applying a TTL policy on an existing collection group results in a bulk
  deletion of all expired data according to the new TTL policy. Note
  that this bulk deletion is also not instantaneous and depends on how much data
  exists for that collection group.
* If a document has an expiration time in the past and you add a new TTL policy
  to the collection, the document will be deleted within 24 hours
  of when the TTL policy finishes setup and becomes active.
* TTL does not necessarily delete documents in the same order as their
  expiration timestamps.
* Deletions are not done transactionally. Documents with the same expiration
  time are not necessarily deleted at the same time. If you require this
  behavior, perform the deletions using a client library.
* Cloud Firestore will always honor the latest TTL field to determine the
  expiration. For example, if an expired but not-yet-deleted document has its
  TTL field updated to a later date, the document won't be expired and the
  new date will be used.
* Cloud Firestore expires a document only when the TTL field is set to
  specific value types. For Standard edition databases, the field must be set to
  a `Date and time` value. For Enterprise edition databases, the field must be
  set to either a `Date and time` value or an `Array` value containing a
  `Date and time` value. Leaving the field absent or set to a value like `null`
  allows expirations to be disabled on a per-document basis.
* TTL is designed to minimize impact on other database activities. Deletions
  driven by TTL are treated with a lower priority. Other strategies are
  also in place to smooth out traffic spikes from TTL-driven deletes.
* Deletion through TTL calls all active
  snapshot listeners and triggers Cloud Functions
  Cloud Firestore triggers.

### TTL fields and indexes

A TTL field can be indexed or unindexed. However, because a TTL field is a
timestamp, indexing the field can affect performance at higher traffic rates.
Indexing a timestamp field can create
[hotspots](https://firebase.google.com/docs/firestore/best-practices#hotspots) which is against best practices. Hotspots are
high read, write, and delete rates to a narrow document range.

By default, Cloud Firestore Standard edition creates a single-field index for all fields.
You can
[create a single-field index exemption](https://firebase.google.com/docs/firestore/query-data/indexing#add_a_single-field_index_exemption)
to disable indexes on a TTL field.

## Permissions

The principal configuring a TTL policy requires the following permission in the
project:

* Viewing TTL policies requires the `datastore.indexes.list`
  and `datastore.indexes.get` permissions.
* Modifying TTL policies requires the `datastore.indexes.update`
  permission.
* Checking the status of TTL operations requires `datastore.operations.list` and `datastore.operations.get`.

For roles that assign these permissions, see [Cloud Firestore Identity and Access Management roles](https://firebase.google.com/docs/firestore/security/iam#predefined_roles).

## Create a TTL policy

When you create a TTL policy, you designate a document field as the expiration
time for documents in a collection group.

TTL uses a specified field to identify documents that are eligible for deletion.
For Standard edition databases, the TTL field must be set to a `Date and time` value.
For Enterprise edition databases, it must be set to either a `Date and time` value or an `Array` value
containing a `Date and time` value. You can select a field that
already exists or you can designate a field that you plan to add later.

**Note:** Some TTL policies in Enterprise edition databases created before February
2026 don't apply to `Date and time` values inside of `Array` values. To update
the policy to apply to `Array` values, disable and re-enable the policy.

Consider the following before you set the TTL field value:

* The TTL field value can be a time in the future, now, or in the past. If the value is a time
  in the past, the document is immediately eligible for deletion. For example, you
  might create a TTL policy with the field `expireAt`, which you then add to
  existing documents.
* Using any other data type or not setting the TTL field value will disable the TTL for the individual document.

To create a TTL policy, follow these steps:

### Google Cloud Console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. Select the required database from the list of databases.
3. In the navigation menu, click **Time-to-live**.
4. Click **Create Policy**.
5. Enter a collection group name and a timestamp field name.
6. Optional: Configure an **Expiration offset**. Enter a value and select
   a unit (days, hours, minutes, or seconds). By default, the offset
   is 0.
7. Click **Create**.

The console returns to the **Time-to-live** page. If the operation
successfully starts, the page adds an entry to the TTL policies table. On
failure, the page displays an error message.

### gcloud

Use the [`firestore fields ttls
update`](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/update)
command to configure a TTL policy. Add the `--async` flag to prevent the
gcloud CLI from waiting for the operation to complete.

```
 gcloud firestore fields ttls update   

      ttl_field   

      --collection-group=collection_group_name   

      --enable-ttl
```

To enable TTL with an expiration offset, add the
`--expiration-offset` flag:

```
 gcloud firestore fields ttls update   

      ttl_field   

      --collection-group=collection_group_name   

      --enable-ttl   

      --expiration-offset=expiration_offset
```

Replace expiration\_offset with a duration, for example, `7d`
for 7 days or `24h` for 24 hours. If you omit this flag, the expiration
offset defaults to 0.

### TTL policy enablement duration

It can take a minimum of ten minutes or more to enable a TTL policy. Once you
start an operation, closing the terminal does not cancel the operation.

## View TTL policies

To view TTL policies and their statuses, follow these steps:

### Google Cloud Console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. Select the required database from the list of databases.
3. In the navigation menu, click **Time-to-live**.

The console lists TTL policies for your database and includes each policy's
status.

### gcloud

Use the
[`firestore fields ttls list`](https://firebase.google.com/sdk/gcloud/reference/firestore/fields/ttls/list)
command to configure a TTL policy. The following command lists all TTL
policies.

```
   gcloud firestore fields ttls list
```

To list TTL policies under a specific collection group, use the following:

```
   gcloud firestore fields ttls list  --collection-group=collection_group_name
```

### View operation details

You can use the gcloud CLI to view more details about a TTL policy
that is in the `CREATING` state.

Use the [`operations list`](https://firebase.google.com/sdk/gcloud/reference/firestore/operations/list) command to see all running and
recently completed operations:

```
gcloud firestore operations list
```

The response includes an estimate of the operation's progress.

## Disable a TTL policy

To disable a TTL policy, follow these steps:

### Google Cloud Console

1. In the Google Cloud console, go to the **Databases** page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. Select the required database from the list of databases.
3. In the navigation menu, click **Time-to-live**.
4. In the TTL policy table, find the row for the TTL policy. Within this
   table row, click the **Delete** (trashcan) button.
5. Confirm by clicking **Delete**.

The console returns to the **Time-to-live** page. On success,
Cloud Firestore removes the TTL policy from the table.

### gcloud

1. Use the
[`firestore fields ttls update`](https://firebase.google.com/sdk/gcloud/reference/firestore/fields/ttls/update)
command to configure a TTL policy. Add the `--async` flag to prevent the
gcloud CLI from waiting for the operation to complete.

```
   gcloud firestore fields ttls update ttl_field --collection-group=collection_group_name --disable-ttl
```

## Monitor TTL deletions

You can use Cloud Monitoring to view metrics about TTL-driven deletions.
Cloud Firestore provides the following metrics for TTL:

| Metric type | Metric name | Metric description |
| --- | --- | --- |
| firestore.googleapis.com/document/ttl\_deletion\_count | Time-to-live deletion count | Total count of documents deleted by TTL policies. |
| firestore.googleapis.com/document/ttl\_expiration\_to\_deletion\_delays | Time-to-live expiration to deletion delays | Time elapsed between when a document expired under a TTL policy and when it was actually deleted. |

To set up a dashboard with Cloud Firestore metrics, see
[manage custom dashboard](https://cloud.google.com/monitoring/charts/dashboards) and
[add dashboard widgets](https://cloud.google.com/monitoring/charts).
