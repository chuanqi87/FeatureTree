# Overview of environments

For production apps, you need to set up a clear development workflow, especially
if you have more than one person working on your app. A development workflow
usually involves setting up and managing multiple environments.

Firebase has varying levels of support for developer workflows and the
constituent environments. Once you're familiar with the developer workflow terms
and assumptions on this page, check out our
[general best practices](https://firebase.google.com/docs/projects/dev-workflows/general-best-practices)
and
[general security guidelines](https://firebase.google.com/docs/projects/dev-workflows/general-security-guidelines)
for setting up a Firebase project and your apps.

**Key Point:** We recommend reading our guides thoroughly, but here's the top
takeaway about development workflows:  
**Firebase recommends using a *separate* Firebase project for *each* environment
in your development workflow.**


## About environments

In software development, an ***environment*** is all the hardware and software
that are required to run an instance of an application or system of
applications.

A series of environments provides isolation for developing and testing software
without impacting users. As shown in the diagram below, environments at a
high-level are considered either *pre-production* or *production*, and you can
have as many pre-production environments as needed. The diagram also describes
common practices and features associated with each
[type of environment](https://firebase.google.com/docs/projects/dev-workflows/overview-environments#types).

The process of progressing a feature or release through these environments to
production is called a ***deployment pipeline***.

![Diagram showing the environments that usually make up the deployment pipeline, including development, test and QA, staging, and finally production](https://firebase.google.com/docs/projects/images/dev-workflows_environments-and-deployment-pipeline.png)

## Types of environments

An environment is composed of the underlying infrastructure that you need to run
and support your application, its code, and its data. Expand each of the
following terms to review descriptions of some common environments, including
tips on the types of data used in each environment type.

**Key Point:** Every app should have at least one *pre-production* environment
that's isolated from production data and resources.


### Development (dev) environments

Every developer needs a development environment — a safe, isolated place to test
changes as they're being built. Ideally, every developer on your team has access
to their own dev environment. Also, if the dev environment is a local instance,
a developer can iterate much faster.

The data in a dev environment is seeded with data that generally resembles the
production data, but should never contain any real users' data. It may also
contain data that has caused bugs in the past, like very long strings.

### Test and QA environments

If you have automated tests, you need an environment in which to run those
tests, and you need to reset the data each time you create the test environment.

If you have QA engineers, they may need one environment that they all use, or
they may need individual environments to test a new release candidate.

The data in test and QA environments is seeded with quality data that's
generally representative of the production data, along with data that represents
corner cases and examples of data that have caused bugs in the past.

### Staging environments

For realistic tests of how a release will work in production, you need a staging
environment that mimics production infrastructure as closely as possible. It's
common to have multiple staging instances if you need to test specific
integrations in isolation.

Here are common differences between staging and prod:

* Staging may be missing some features or integrations that could cause side
  effects. For example, staging may be set to not send email.
* Staging may have anonymized data; the data can be fake, but it should be
  realistic. Because staging is a place to safely debug problems, you might give
  broader team access to staging data than production data. So, to protect user
  privacy, you shouldn't use actual user data in staging.

### Production (prod) environments

For each application that you maintain, you need a single production
environment. This is the instance with which your users interact.

Unlike the other environments where you can change, delete, and/or recreate
data, the data in your prod environment is very important; losing or altering
your prod data will directly affect your users.

In the Firebase console, we recommend tagging the Firebase project associated
with your production environment as a
["production" environment type](https://firebase.google.com/support/faq#set-environment-type). This tag
can help remind you and your teammates that any changes could affect your
associated production apps and their data.

**Tip**: Integrations with analytics services, including
Google Analytics, often require special attention when you're setting up
a new environment. You also don't want your tests from pre-production
environments to impact production analytics.

We recommend not setting up analytics for most pre-production environments,
unless you want to specifically test analytics integrations, like making
sure the right parameters are being sent to your analytics service.



## Next steps

* Review our
  [general best practices](https://firebase.google.com/docs/projects/dev-workflows/general-best-practices)
  for setting up Firebase projects. This guide answers questions about Firebase
  project hierarchy, how to register your app variants, and multi-tenancy.
* Review the
  [general security guidelines](https://firebase.google.com/docs/projects/dev-workflows/general-security-guidelines)
  for different environments. You want to make sure each environment and its
  data are secure.
* Review the [Firebase launch checklist](https://firebase.google.com/support/guides/launch-checklist).
