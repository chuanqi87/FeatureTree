# Support private apps

**Note:** Additional guidance on private apps is available from the [managed
Google Play Help Center](https://support.google.com/googleplay/work/topic/6145152).

A private app is an app that’s only available to an enterprise’s users. Private
apps are fully compatible with managed Google Play. An enterprise can publish
private apps to its managed Google Play store and install private apps remotely
to users’ devices. To learn more, see [Distributing private apps to
users](https://developers.google.com/android/work/play/emm-api/distribute#distribute_private_apps_to_users).

## Google-hosted private apps

Enterprise customers aren't required to host their private apps on managed
Google Play, but it offers several key benefits. See [Google-hosted private
apps](https://support.google.com/googleplay/work/answer/6145197) for more
details.

Google-hosted private apps can be installed on devices running any mode of
operation (profile owner, device owner, or legacy), and there are no additional
features you need to implement in your EMM solution to support them.

## Self-hosted private apps

Enterprise customers also have the option of hosting their private apps
themselves and only using the managed Google Play infrastructure to manage app
installation.

Self-hosted private apps can be installed on devices running the profile owner
mode of operation, but they aren’t compatible with [legacy
devices](https://developers.google.com/android/work/play/emm-api/prov-devices#modes_of_operation) and can
only be push installed to devices running the device owner mode of operation.

To successfully publish a self-hosted private app, an enterprise customer must
first build an APK definition file that contains metadata captured from the
app's manifest in JSON format. This definition file replaces the APK within
Google Play and needs to be uploaded during the publishing process. More
detailed guidance on how to generate an APK definition file and access to
downloadable sample code is available on GitHub (see [externally hosted
APKs](https://github.com/google/play-work/tree/master/externally-hosted-apks)).

## Integrate private app management into your console

The simplest way to add private app publishing capabilities to your EMM console
is to embed the [managed Google Play iframe](https://developers.google.com/android/work/play/emm-api/managed-play-iframe#private-apps).
The iframe's Private apps page silently creates a Play Console account on behalf
of an enterprise and waives the $25 USD registration fee.

Another option is to add private app publishing to your console using the
[Google Play Custom App Publishing API](https://developers.google.com/android/work/play/custom-app-api).
This API is only compatible with Google-hosted private apps, and the apps
published through this method can't ever be made public. To integrate additional
publishing and app management tasks, use the [Google Play Publishing API](https://developers.google.com/android-publisher).

You or your enterprise customer can also [publish](https://support.google.com/googleplay/work/answer/6145139)
and [update](https://support.google.com/googleplay/android-developer/answer/113476)
private apps directly from the Google Play Console.
