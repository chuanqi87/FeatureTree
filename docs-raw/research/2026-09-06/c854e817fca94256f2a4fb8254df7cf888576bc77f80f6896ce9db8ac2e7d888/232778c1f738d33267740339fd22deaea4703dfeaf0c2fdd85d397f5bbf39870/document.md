# Retry asynchronous functions

This document describes how you can request asynchronous (non-HTTPS)
background functions to retry on failure.

## Why event-driven functions fail to complete

On rare occasions, a function might exit prematurely due to an internal error,
and by default the function might or might not be automatically retried.

More typically, an event-driven function might fail to successfully complete due
to errors thrown in the function code itself. The reasons this might
happen include:

* The function contains a bug and the runtime throws an exception.
* The function cannot reach a service endpoint, or times out while trying to
  do so.
* The function intentionally throws an exception (for example, when a parameter
  fails validation).
* A Node.js function returns a rejected promise, or passes a non-`null` value to
  a callback.

In any of the above cases, the function will stop executing and return an error.
Event triggers producing the messages have retry policies that you can customize
to meet the needs of your function.

## Semantics of retry

Cloud Functions provides at-least-once execution of an event-driven function
for each event emitted by an event source.
By default, if a function
invocation terminates with an error, the function is not invoked again and the
event is dropped. When you enable retries on an event-driven function,
Cloud Functions retries a failed function invocation until it completes
successfully or the retry window expires.

**Warning:** Setting "retry on failure" causes your function to be retried
repeatedly until it either successfully executes or the maximum retry period has
elapsed, which can be multiple days. If the failure is due to a bug or any other
sort of permanent error, your function can get stuck in a retry loop.
You should only use this setting when dealing with transient failures (such as an
unreliable endpoint or intermittent timeouts), and only after pressure-testing your
code without this property set. If your function does become stuck in a retry
loop, you must either redeploy it or delete it to end execution.

When retries are not enabled for a function, which is the default, the function
always reports that it executed successfully, and `200 OK` response codes might
appear in its logs. This occurs even if the function encountered an error. To
make it clear when your function encounters an error, be sure to
[report errors](https://firebase.google.com/docs/functions/reporting-errors)
appropriately.

#### Configure retries from your function code

With Cloud Functions for Firebase, you can enable retries in the code for a
function. To do this for a background event such as the creation of a new
Firestore document, set the [`failurePolicy`](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionsfailurepolicy) (1st gen) or [`retry`](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptionsretry)
policy (2nd gen) option to `true`:

1st gen

```
exports.docCreated = functions
  .runWith({
    // retry on failure
    failurePolicy: true,
  })
  .firestore.document("my-collection/{docId}")
  .onCreate((change, context) => {
    /* ... */
  });
```

2nd gen

```
const { onDocumentCreated } = require("firebase-functions/firestore");

exports.docCreated = onDocumentCreated(
  {
    // retry on failure
    retry: true,
  },
  "my-collection/{docId}",
  (event) => {
    /* ... */
  },
);
```

Setting `true` as shown configures a function to retry on failure.

### Retry window

For 2nd gen functions,
this retry window expires after 24 hours. For 1st gen functions, it expires
after 7 days.
Cloud Functions retries newly created event-driven functions using
an exponential backoff strategy, with an increasing backoff of between 10
and 600 seconds.
This policy is applied to new functions
the first time you deploy them. It is not retroactively applied to existing
functions that were first deployed before the changes described in
[this release note](https://cloud.google.com/functions/docs/release-notes#April_20_2023)
took effect, even if you redeploy the functions.

## Best practices

This section describes best practices for using retries.

### Use retry to handle transient errors

Because your function is retried continuously until successful execution,
permanent errors like bugs should be eliminated from your code through testing
before enabling retries. Retries are best used to handle intermittent or transient
failures that have a high likelihood of resolution upon retrying, such as a
flaky service endpoint or timeout.

### Set an end condition to avoid infinite retry loops

It is best practice to protect your function against continuous looping when
using retries. You can do this by including a well-defined end condition,
*before* the function begins processing. Note that this technique only works if
your function starts successfully and is able to evaluate the end condition.

A simple yet effective approach is to discard events with timestamps older than
a certain time. This helps to avoid excessive executions when failures are
either persistent or longer-lived than expected.

For example, this code snippet discards all events older than 10 seconds:

```
const eventAgeMs = Date.now() - Date.parse(event.timestamp);
const eventMaxAgeMs = 10000;
if (eventAgeMs > eventMaxAgeMs) {
  console.log(`Dropping event ${event} with age[ms]: ${eventAgeMs}`);
  callback();
  return;
}
```



### Use `catch` with Promises

If your function has retries enabled, any unhandled error will trigger a retry.
Make sure that your code captures any errors that shouldn't result in a retry.

Here is an example of what you should do:

```
return doFooAsync().catch((err) => {
    if (isFatal(err)) {
        console.error(`Fatal error ${err}`);
    }
    return Promise.reject(err);
});
```



### Make retryable event-driven functions idempotent

Event-driven functions that can be retried must be idempotent. Here are some
general guidelines for making such a function idempotent:

* Many external APIs (such as Stripe) let you supply an idempotency key
  as a parameter. If you are using such an API, you should use the event ID as
  the idempotency key.
* Idempotency works well with at-least-once delivery, because it makes it safe to
  retry. So a general best practice for writing reliable code is to combine
  idempotency with retries.
* Make sure that your code is internally idempotent. For example:
  + Make sure that mutations can happen more than once without changing the
    outcome.
  + Query database state in a transaction before mutating the state.
  + Make sure that all side effects are themselves idempotent.
* Impose a transactional check outside the function, independent of the code.
  For example, persist state somewhere recording that a given event ID has
  already been processed.
* Deal with duplicate function calls out-of-band. For example, have a separate clean up
  process that cleans up after duplicate function calls.

## Configure the retry policy

Depending on the needs of your function, you may want to configure the
retry policy directly. This would allow you to set up any combination of the
following:

* Shorten the retry window from 7 days to as little as 10 minutes.
* Change the minimum and maximum backoff time for the exponential backoff
  retry strategy.
* Change the retry strategy to retry immediately.
* Configure a
  [dead-letter topic](https://cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic).
* Set a maximum and minimum number of delivery attempts.

To configure the retry policy:

1. Write an HTTP function.
2. Use the Pub/Sub API to create a Pub/Sub subscription, specifying the URL of
   the function as the target.

See [Pub/Sub documentation on handling failures](https://cloud.google.com/pubsub/docs/handling-failures)
for a more information on configuring Pub/Sub directly.
