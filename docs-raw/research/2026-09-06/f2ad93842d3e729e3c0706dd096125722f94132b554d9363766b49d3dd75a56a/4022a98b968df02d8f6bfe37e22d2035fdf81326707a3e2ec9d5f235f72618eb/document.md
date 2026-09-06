# Extension publisher overview

A Firebase Extension performs a specific task or set of tasks in response to
HTTP requests or triggering events from other Firebase and Google products, like
Firebase Cloud Messaging, Cloud Firestore, or Pub/Sub.

You can build your own extension for personal use or to share with the world in
the Firebase Extensions Hub. For example, your extension can perform a specific
task that your app regularly needs, or it can make it easier to access one of
your company's APIs. After you build your extension, you can share it with
others. Those users can install and configure the extension for use in their own
Firebase projects.

## Structure of an extension

You can think of an extension as having three main components:

* Cloud Functions code, in JavaScript or TypeScript
* Metadata that describes your extension
* Documentation to help your users configure and use your extension

To develop an extension, you assemble these components into the following
structure:

```
example-extension
├── functions
│   ├── integration-tests
│   │   ├── extensions
│   │   │   └── example-extension.env
│   │   ├── firebase.json
│   │   └── integration-test.spec.js
│   ├── index.js
│   └── package.json
├── README.md
├── PREINSTALL.md
├── POSTINSTALL.md
├── CHANGELOG.md
├── icon.png
└── extension.yaml
```

* The `functions` directory contains your Cloud Functions code in JavaScript
  or TypeScript. This is the code that performs the extension's tasks in
  response to events triggered by Firebase and Google services.
* The `extension.yaml` file contains metadata about your extension, such as
  its triggers and IAM access roles, as well as any parameters you want to be
  user-configurable.
* The `PREINSTALL`, `POSTINSTALL`, and `CHANGELOG` files are the minimum
  documentation your extension must have. These files help your users learn
  what your extension does, how to use it, and what updates you've made. You
  should also provide an icon to help users recognize your extension. The
  Firebase console, Firebase CLI, and Extensions Hub display the contents of
  these files when users explore, install, and manage your extension.

After you have created your extension, you can use the Firebase CLI to install
it into a project or publish it to the Extensions Hub, where anyone can discover
and install it into their projects.

## What products can my extension interact with?

Because a Firebase extension does its work using Cloud Functions, you can think
of the question of possible integrations in two ways: *What products can trigger
my extension's functions?* and *Once triggered, what products can my extension's
functions interact with?*

### Supported function triggers

#### Manual triggers

First of all, you can manually trigger a function. Firebase Extensions and Cloud
Functions support two ways of manually triggering functions:

* HTTP triggers: deploy a function to an HTTP endpoint
* Callable functions: call your Cloud Functions directly from your iOS,
  Android, or web client code, using the Firebase client SDKs.

By exposing HTTP endpoints from your extension, your extension can potentially
integrate with any web service that supports webhooks. With callable functions,
users who install your extension can use the Firebase SDKs as a client library
for accessing the API your extension implements.

#### Firebase service triggers

Most Firebase products emit events that can trigger an extension's Cloud
Functions.

* **Analytics:** trigger functions when Analytics logs an event
* **App Distribution:** trigger functions when App Distribution triggers an
  alert
* **Authentication:** trigger functions when users create and delete accounts
* **Cloud Firestore:** trigger functions when pages are created, updated, or
  deleted
* **Cloud Storage**: trigger functions when objects are uploaded, archived, or
  deleted from buckets
* **Crashlytics:** trigger functions when Crashlytics triggers an alert
* **Performance Monitoring:** trigger functions when Performance Monitoring
  triggers an alert
* **Realtime Database:** trigger functions when data is created, updated, or
  deleted
* **Remote Config:** trigger functions when a parameter is updated
* **Test Lab:** trigger functions when Test Lab triggers an alert

#### Google Cloud service triggers

An extension can also include functions that trigger off several non-Firebase
Google Cloud services:

* **Cloud Pub/Sub**: an extension can include functions that trigger when
  events are posted to a configurable Pub/Sub topic.
* **Cloud Scheduler**: an extension can include functions that run on a set
  schedule
* **Cloud Tasks**: an extension can include functions that can be queued using
  Cloud Tasks. Firebase Extensions uses this capability to let you, as an
  extension author, write functions that respond to an extension's "lifecycle"
  events: being installed in a project for the first time, being upgraded to a
  new version, and being reconfigured.
* **Eventarc**: an extension can include functions that trigger when events
  are published to a configurable Eventarc channel; conversely, an extension
  can publish its own events to an Eventarc channel in order to enable users
  to define their own functions that trigger from an *extension's* events.

### Supported from functions

Once an extension's Cloud Function has been triggered, the range of possible
integrations is generally open ended. Here are some highlights of what you can
do from a Cloud Function:

* Read, write, and otherwise interact with any **Firebase** or **Google Cloud**
  service that uses a
  [supported IAM role](https://firebase.google.com/docs/extensions/publishers/access#supported-roles).
* Work with any **third-party service** that provides a web API.
* Work with your **custom services** if you provide a web API.
* Run most JavaScript libraries, including **TensorFlow.js**, **Express.js,**
  and so on.

## How to build an extension

The [Get Started](https://firebase.google.com/docs/extensions/publishers/get-started) tutorial walks you through
the process of building, testing, and publishing a complete extension, and is
the recommended way to learn how to build one.

[Get Started](https://firebase.google.com/docs/extensions/publishers/get-started)

After you've gone through the getting started guide once, you can refer to the
individual topic guides, which explain each of the tasks involved in building
your own extension:

* [Write functions for an extension](https://firebase.google.com/docs/extensions/publishers/functions)
* [Use parameters in an extension](https://firebase.google.com/docs/extensions/publishers/parameters)
* [Set up appropriate access for an extension](https://firebase.google.com/docs/extensions/publishers/access)
* [Respond to extension lifecycle events](https://firebase.google.com/docs/extensions/publishers/lifecycle-events)
* [Add user hooks to an extension](https://firebase.google.com/docs/extensions/publishers/user-hooks)
* [Create user documentation for your extension](https://firebase.google.com/docs/extensions/publishers/user-documentation)
* [Publish an extension on Extensions Hub](https://firebase.google.com/docs/extensions/publishers/upload-and-publish)
* [Complete extension.yaml reference](https://firebase.google.com/docs/extensions/reference/extension-yaml)
