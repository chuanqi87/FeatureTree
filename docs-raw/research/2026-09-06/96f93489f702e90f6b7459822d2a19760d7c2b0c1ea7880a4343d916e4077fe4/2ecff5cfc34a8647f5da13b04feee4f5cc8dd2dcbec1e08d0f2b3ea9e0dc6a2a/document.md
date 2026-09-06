# Secure data in Cloud Firestore

**Note:** Many AI coding agents can help generate Firebase Security Rules for Cloud Firestore and
Cloud Storage for Firebase.
For a detailed, pre-written prompt you can use with your AI assistant, refer to
[AI Prompt: Write Firebase Security Rules](https://firebase.google.com/docs/ai-assistance/prompt-catalog/write-security-rules).

Cloud Firestore offers robust access management and authentication
through different mechanisms, depending on the client libraries you use.

## Mobile and web client libraries

For **mobile and web client libraries**, use Firebase Authentication and
Cloud Firestore Security Rules to handle serverless authentication,
authorization, and data validation. Learn how to use
[Cloud Firestore Security Rules](https://firebase.google.com/docs/firestore/security/get-started) to secure your data when using
the
Android, Apple, Web, Flutter, Unity, and C++ client libraries.

Use [Firebase App Check](https://firebase.google.com/docs/app-check) to help ensure that only your app
can access your Cloud Firestore data.

For your apps that use Cloud Storage for Firebase, use Cloud Firestore to
define conditions for access to your Cloud Storage resources in database
documents that can be
[accessed by Cloud Storage Security Rules](https://firebase.google.com/docs/storage/security/rules-conditions#enhance_with_firestore).

## Server client libraries

For **server client libraries**, use Identity and Access Management (IAM)
to manage access to your database. Learn how
to secure your data for the Java, Python, Node.js, and Go client libraries
with [IAM](https://cloud.google.com/firestore/docs/security/iam).
