# Frameworks and tooling for App Hosting

Firebase App Hosting is designed specifically to support framework-centered
modern web app development. Use this page as a reference to the tooling and
frameworks that App Hosting directly supports, as well as a jumping off
point to learn about related frameworks and tooling.

## Web frameworks and App Hosting

App Hosting provides two broad levels of support for modern web frameworks:
pre-configured build and deploy support, and community-level support through
open source contributions conforming to the output bundle specification. In both
cases, a *framework adapter* component enables the integration of a specific
framework with App Hosting.

### Frameworks with preconfigured build and deploy support

With pre-configured build and deploy support, Firebase identifies which
framework you're using by inspecting the `package-lock.json` file or other lock
file, and optimizes build and deployment processes for your app. Google is
committed to maintaining support for these frameworks, and the Firebase support
team can accept issue reports and feature requests.

This level of support is provided for:

* Next.js
* Angular

See the
[support schedules](https://firebase.google.com/docs/app-hosting/frameworks-tooling#next.js-support) for details on specific versions
and levels of support.

If you try to deploy a Node.js app that is missing a lock file, App Hosting
will fail to build and run your app. You can create `package-lock.json` by
running `npm install` in your root directory.

**Note:** Express apps with a "start" and "build" script configured generally work
in App Hosting, but support is not guaranteed. If there is a more
specific adapter available, we recommend setting your project up with that
adapter.


### Community-supported frameworks

In addition to Next.js and Angular, App Hosting also supports any web
framework that is able to provide a build output that matches our
[output bundle specification](https://github.com/firebase/apphosting-adapters#app-hosting-output-bundle).
Framework authors can take advantage of the output bundle specification to
ensure their framework is supported by App Hosting. For example, the popular
Nuxt framework is supported by the Nitro team, who built a
[Firebase adapter](https://nitro.build/deploy/providers/firebase)
to enable Nuxt app deployment on App Hosting.

If you would like to see additional frameworks supported by App Hosting, you
can create a framework adapter, or reach out to the framework's maintainers to
convert build outputs into the App Hosting format. The Next.js and Angular
adapters are good reference examples for anyone creating an adapter.

Information on community-supported frameworks can be found on
[Firebase Open Source](https://firebaseopensource.com/platform/app_hosting).
Issues and feature requests for community-supported frameworks
should be directed to the open source community or framework authors. In some
cases Google may be able to assist, but the community is the first line of
support for these adapters.

## App Hosting framework adapters

In App Hosting, support for both pre-configured and community-supported
frameworks is provided through *framework adapters*. App Hosting framework
adapters have two key roles:

* They parse your source code and any framework-specific config files (such as
  `next.config.js`) and generate an output bundle that can be processed by the
  rest of the App Hosting infrastructure.
* They run your app's build command to generate static assets and create an
  optimized version of your app for production.

Framework adapters build your Node.js app with `npm run build`, working best
with the default build scripts for each framework: `next build` for Next.js and
`ng build` for Angular. App Hosting will attempt builds with custom build
commands, but cannot dependably guarantee success. You can
[override build and run scripts](https://firebase.google.com/docs/app-hosting/configure#override-scripts)
in `apphosting.yaml`.

The source for Next.js and Angular adapters is available in
[firebase-framework-tools](https://github.com/firebase/apphosting-adapters).

## Runtimes for App Hosting

After it is built and rolled out by App Hosting, your Node.js app runs in a
Cloud Run revision. Accordingly, the runtime version for your app
should be within both
[Cloud Run's supported range](https://cloud.google.com/run/docs/runtime-support#node.js)
and the range of your chosen web framework. For the
preconfigured support for Angular and Next.js, this means that the
following Node.js versions are supported:

* Next.js 13.5.x and higher
* Angular 18.2.x and higher
* Node.js 20 and higher

App Hosting does not automatically provide active support for newly released
framework versions. Versions newer than our currently designated 'active'
version will be considered in a 'preview' state until officially marked as
'active' for App Hosting.

App Hosting supports long-term support (LTS) for the latest minor version of
a major release for one year from its active support period, provided that you
consistently update to the latest patch releases within that minor version.
Refer to the following tables for details for Next.js and Angular.

**Note:** Framework releases must abide by [semantic versioning](https://semver.org/).
A framework release that violates semantic versioning is subject to a
best-effort level of support.


### Next.js support schedule

| Version | Status | Deprecation |
| --- | --- | --- |
| 13.5.x | lts | 2026-10-9 |
| 14.2.x | lts | 2026-10-9 |
| 15.0.x | active | not before 2025-10-9 |
| 15.1.x | active | not before 2025-10-9 |
| 15.2.x | active | - |

### Angular support schedule

| Version | Status | Deprecation |
| --- | --- | --- |
| 18.2.x | lts | 2026-10-9 |
| 19.0.x | active | not before 2025-10-9 |
| 19.1.x | active | not before 2025-10-9 |
| 19.2.x | active | - |

**Note:** versions outside of these ranges may work but are not offically supported.


### Automatic Base Image Updates (ABIU)

Automatic Base Image Updates (ABIU) is a feature that automatically applies
security patches to your underlying runtime environment without requiring you to
trigger a new app rollout.

App Hosting defaults to enabling ABIU for new backends, with these
specific requirements:

* **Versioned Runtimes:** To use ABIU, you must specify a versioned runtime
  (such as `nodejs20`, `nodejs22`, `nodejs24`). App Hosting supports
  even-numbered Node.js versions, mirroring Cloud Run's support.
* **package.json matching:** The Node version you select for App Hosting
  must be compatible with the version specified in the `engines` field of your
  `package.json` file. If there is a mismatch, you will encounter a build-time
  error from Cloud Build. Any time you change the `engines` field, make
  sure to update your backend's runtime before deploying.

#### Disabling ABIU

If you want to opt out of ABIU, you can disable it during onboarding or by
selecting **"Not Specified"** for your runtime in the Firebase console. When
a versionless `nodejs` default is used, ABIU is automatically disabled.

#### Managing Runtime Versions

You can view and change your backend's runtime version and ABIU preference at
any time in the **Settings** tab of your App Hosting dashboard. However, be
aware that *changing your runtime version may break your application* if the
new version is incompatible with your code.

Runtime versions eventually reach the end of their support lifecycle. It is
important to keep your runtimes updated to avoid breaking changes:

* **Deprecated Runtimes:** If your chosen runtime becomes deprecated, your
  application will generally continue to work. You will receive a warning in
  the console, and you should move to a newer version as soon as possible.
  For more information, see the Cloud Run documentation of the [runtime
  lifecycle](https://docs.cloud.google.com/run/docs/runtime-support#runtime_lifecycle_2).
* **Decommissioned Runtimes:** Decommissioned runtimes are completely
  unsupported. You will not be allowed to create new builds or backends
  using a decommissioned version, and attempting to do so will throw a
  build error. Existing deployments running on decommissioned versions may
  stop working, and Cloud Run reserves the right to delete them.

For a full list of supported, deprecated, and decommissioned Node versions,
refer to the [Cloud Run Runtime Support
documentation](https://cloud.google.com/run/docs/runtime-support). For more
technical details on how base image updates work, see the [Cloud Run ABIU
documentation](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates).

## Package managers

App Hosting uses [Cloud Native
Buildpacks](https://cloud.google.com/docs/buildpacks/overview) to execute the
installation of dependencies and builds the app using npm, yarn, or pnpm. Other
package managers such as JSR are not supported.

### NPM

* NPM is the default package manager.
* Non-production dependencies are pruned after the build is successful.
* You can specify the npm version section using the `engines.npm` field in your
  `package.json` file.

### Yarn

* Yarn is used instead when you include the `yarn.lock` file in your project.
* You can specify the yarn version to use in the `engines.yarn` or
  `packageManager` field of your `package.json` file.
* App Hosting supports Yarn2 PnP mode.

### Pnpm

* Pnpm is used instead when you include the `pnpm-lock.yaml` file in your
  project.
* You can specify a version of pnpm in the `engines.pnpm` or
  `packageManager` field of your `package.json` file.
* For a working example, see the
  [sample-node-pnpm](https://github.com/GoogleCloudPlatform/buildpack-samples/tree/master/sample-node-pnpm).
  app.

## Monorepos for App Hosting

App Hosting supports Nx-based apps. See [Use monorepos with
App Hosting](https://firebase.google.com/docs/app-hosting/monorepos) for detailed guidance.

The following Nx versions are supported:

| Version | Status | Deprecation |
| --- | --- | --- |
| 19.5.x | maintenance | 2025-10-9 |
| 19.6.x | maintenance | 2025-10-9 |
| 19.7.x | maintenance | 2025-10-9 |
| 19.8.x | lts | 2026-10-9 |
| 20.0.x | active | not before 2025-10-9 |
| 20.1.x | active | not before 2025-10-9 |
| 20.2.x | active | not before 2025-10-9 |
| 20.3.x | active | not before 2025-10-9 |
| 20.4.x | active | not before 2025-10-9 |
| 20.5.x | active | not before 2025-10-9 |
| 20.6.x | active | not before 2025-10-9 |
| 20.7.x | active | — |

If you need support for other types of monorepo workspaces, let us know at
[Firebase UserVoice](https://firebase.uservoice.com/forums/948424-general).
