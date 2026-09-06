# Sync, async, and promises

It's important to manage the lifecycle of a function to ensure that it resolves
properly. By terminating functions correctly, you can avoid excessive charges
from functions that run for too long or loop infinitely. Also, you can make sure
that the Cloud Functions instance running your function does not shut down
before your function successfully reaches its terminating condition or state.

Use these recommended approaches to manage the lifecycle of your functions:

* Resolve functions that perform **asynchronous** processing (also known as "background functions") by returning a
  [JavaScript
  promise](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Promise).
* Terminate **HTTP functions** with `res.redirect()`, `res.send()`, or
  `res.end()`.
* Terminate a **synchronous** function with a `return;` statement.

**Caution:** In all cases, be careful to avoid any situation in which the function's
result actually retriggers the function — for example, a function
triggered by writes to a specific Realtime Database path that concludes by writing
to that same path.


## Simplify asynchronous code with JavaScript promises

Promises are a modern alternative to callbacks for asynchronous code. A promise
represents an operation and the future value it may return. It also lets you
propagate errors similar to try/catch in synchronous code. You can read about
promises in the Firebase SDK on [The Firebase
Blog](https://firebase.googleblog.com/2016/01/keeping-our-promises-and-callbacks_76.html),
and promises in general on
[MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Promise).

## How promises work with functions

When you return a JavaScript promise to a function, that function
keeps running until the promise is resolved or rejected. To indicate that a
function has completed its work successfully, the promise should be resolved. To
indicate an error, the promise should be rejected. This means you only need to
handle errors that you want to.

The following code takes a Firebase Realtime Database `ref` and sets its value to
`"world!"`. By returning the result of `set`, your function is guaranteed to
keep running until the asynchronous work of writing the string to the database
is fully completed:

```
// Always change the value of "/hello" to "world!"
exports.hello = functions.database.ref('/hello').onWrite(event => {
  // set() returns a promise. We keep the function alive by returning it.
  return event.data.ref.set('world!').then(() => {
    console.log('Write succeeded!');
  });
});
```



## Examples in context

Most of our Cloud Functions [code
samples](https://github.com/firebase/functions-samples)
include examples of proper function termination. Here are a few that demonstrate
typical cases:

* [Realtime Database
  trigger](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/quickstarts/uppercase-rtdb/functions/index.js):
  an HTTP function followed by a redirect
* [Cloud Storage
  trigger](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/quickstarts/thumbnails/functions/index.js):
  A storage download followed by `then`
* [Webhook on Realtime Database
  write](https://github.com/firebase/functions-samples//tree/main/Node-1st-gen/minimal-webhook/functions/index.js):
  An error thrown inside a `then` clause
* [Periodically delete unused
  accounts](https://github.com/firebase/functions-samples//tree/main/Node-1st-gen/delete-unused-accounts-cron/functions/index.js):
  A rejected promise
