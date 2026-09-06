# Use the Google Play Billing Library with Unity

The Google Play Billing plugin extends Unity's built-in services and
assets for in-app purchases, called [Unity
IAP](https://docs.unity3d.com/Manual/UnityIAP.html), to provide
your game with all the latest features of the Google Play Billing Library. This
guide explains how to set up your project to use the plugin. This guide also
describes how to implement Google Play Billing Library features in your game in Unity.

### Set up the Google Play Billing plugin

To set up the plugin, complete the steps in each of these linked sections:

1. [Enable the Unity IAP abstraction layer](https://developer.android.com/google/play/billing/unity#abstraction-layer).
2. [Download and import the plugin](https://developer.android.com/google/play/billing/unity#import-plugin).
3. [Configure the plugin's build settings](https://developer.android.com/google/play/billing/unity#plugin-build-settings).
4. [Enable the plugin](https://developer.android.com/google/play/billing/unity#enable-plugin).

#### Enable the Unity IAP abstraction layer

The Google Play Billing plugin is built on an abstraction layer included with
Unity IAP, so you need to enable this abstraction layer before you download
and import the plugin. To enable the Unity IAP abstraction layer, do the
following:

1. Complete all the steps in the following Unity tutorial: [Set up your project
   for Unity Services](https://docs.unity3d.com/Manual/SettingUpProjectServices.html).
2. Complete all the steps in the following Unity tutorial: [Enable the Unity IAP
   service](https://docs.unity3d.com/Manual/UnityIAPSettingUp.html).

#### Download and import the plugin

The plugin is shipped as a Unity package in the
`.unitypackage` format. To download and import the plugin, follow these steps:

1. Download the latest release of the Google Play Plugins for Unity from the repository's
   [releases page on GitHub](https://github.com/google/play-unity-plugins/releases).
2. From the Unity menu bar, click **Assets > Import Package > Custom Package**.

   ![](/static/images/google/play/billing/unity-import-custom-package.png)
3. Locate where you downloaded the `.unitypackage` file and select it.
4. In the **Import Unity Package** dialog, leave all assets selected and click
   **Import**.

   ![](/static/images/google/play/billing/import-unity-package.png)

After the package imports, a new folder called **GooglePlayPlugins** (at the
root of the Assets folder) is added to your project's assets. This folder
contains all of the Google Play Billing Library assets for the plugin.

#### Configure build settings

Because the plugin extends Unity IAP, Unity will encounter conflicts and fail to
build an Android APK unless some older, overlapping dependencies in Unity IAP
are removed from the build. The plugin provides an automatic way to remove the
conflicting libraries from your project. To resolve these conflicts, follow
these steps:

1. From the Unity menu bar, select **Google > Play Billing > Build Settings**.

   ![](/static/images/google/play/billing/unity-plugin-build-settings.png)
2. In the Play Billing Build Settings window, click **Fix**. This resolves the
   conflict and moves the conflicting Unity IAP files to a backup directory. After
   you click **Fix**, the button changes to **Restore**, which you can click to
   restore the original, conflicting files.

   ![](/static/images/google/play/billing/unity-resolve-plugin-conflicts.png)

#### Enable the plugin

To enable the plugin, replace Unity IAP’s implementation of Google Play with the
Google Play Billing plugin. For example, when using the [Unity IAP Purchaser
Script](https://learn.unity.com/tutorial/unity-iap#5c7f8528edbc2a002053b46e),
you would change the `StandardPurchaseModule` that's passed into the IAP builder
to use the `Google.Play.Billing.GooglePlayStoreModule`:

```
// Create a builder using the GooglePlayStoreModule.
var configurationBuilder =
    ConfigurationBuilder.Instance(Google.Play.Billing.GooglePlayStoreModule.Instance());
```

**Note:** To avoid any potential conflicts with Unity's standard IAP implementation,
you should fully specify the namespace by including `Google.Play.Billing`
whenever your code refers to the public classes in Google Play Billing plugin.
All of the code examples in this guide use this approach.

If your game uses the same Purchaser Script for multiple platforms, then you
should add a platform check to make sure that Unity will continue to use its
own IAP solution for other platforms:

```
ConfigurationBuilder builder;
if (Application.platform == RuntimePlatform.Android)
{
  builder = ConfigurationBuilder.Instance(
      Google.Play.Billing.GooglePlayStoreModule.Instance());
}
else
{
  builder = ConfigurationBuilder.Instance(StandardPurchasingModule.Instance());
}
```

If you publish your game on other Android app stores besides the Google Play
Store, then you should replace the default Unity IAP implementation only when
you’re selecting the Google Play Store:

```
ConfigurationBuilder builder;
if (Application.platform == RuntimePlatform.Android
       && SelectedAndoidAppStore == AppStore.GooglePlay)
{
  builder = ConfigurationBuilder.Instance(
      Google.Play.Billing.GooglePlayStoreModule.Instance());
}
else
{
  builder = ConfigurationBuilder.Instance(StandardPurchasingModule.Instance());
}
```



## Implement Google Play Billing Library features in your game

The Google Play Billing plugin extends Unity IAP services, so you can use the
same Unity APIs to manage common purchasing workflows. Note that there are some
[minor changes to API behavior](https://developer.android.com/google/play/billing/unity#behavior-changes)
due to differences between the Google Play Billing Library and Unity's standard IAP
implementation for other app stores. If you're new to the Unity IAP APIs, see
the "Making a Purchase Script" section in the [Unity IAP
tutorial](https://learn.unity.com/tutorial/unity-iap#5c7f8528edbc2a002053b46e)
for an example of how to implement basic purchasing flows.

The Google Play Billing Library also includes some features that are unique to the Google
Play store. You can access these features through an extended interface. The
rest of this section describes how to implement these unique Google Play Billing Library
features in your game.

### Enable deferred purchases

Google Play supports deferred purchases—also called [pending
trasacations](https://developer.android.com/google/play/billing/billing_library_overview#pending) or pending
purchases—where users can create a purchase and complete it later using cash in
stores.

To enable deferred purchases, use your IAP builder to modify your module's
configuration by calling the `EnableDeferredPurchase()` method:

```
// Create a builder using a GooglePlayStoreModule.
var configurationBuilder =
    ConfigurationBuilder.Instance(Google.Play.Billing.GooglePlayStoreModule.Instance());
// Enable deferred purchases
configurationBuilder.Configure<Google.Play.Billing.IGooglePlayConfiguration>()
    .EnableDeferredPurchase();
```

Next, implement a deferred purchases callback using the Play Store extensions:

```
// Get the plugin extensions for the Google Play Store.
_playStoreExtensions =
    extensions.GetExtension<Google.Play.Billing.IGooglePlayStoreExtensions>();

// Set the deferred purchases callback.
_playStoreExtensions.SetDeferredPurchaseListener(
    delegate(Product product)
    {
        // Do not grant the item here. Instead, record the purchase and remind
        // the user to complete the transaction in the Play Store.
    });
```



### Pass obfuscated account IDs to Google Play

You can pass obfuscated user account IDs to Google Play to facilitate abuse
detection, such as detecting if many devices are making purchases on the same
account in a short period of time.

**Note:** This account ID is also returned with purchase data. If you were using
developer payload to identify users, you can use this account ID as an
alternative.

To pass an obfuscated account ID, call the `SetObfuscatedAccountId()` method
from the extensions API:

```
// Get the plugin extensions for the Google Play Store.
_playStoreExtensions =
    extensions.GetExtension<Google.Play.Billing.IGooglePlayStoreExtensions>();

// Pass an obfuscated account ID.
_playStoreExtensions.SetObfuscatedAccountId(obfuscatedAccountId);
```



### Pass obfuscated profile IDs to Google Play

You can pass an obfuscated profile ID to Google Play to facilitate fraud
detection, such as detecting if many devices are making purchases on the same
account in a short period of time. This is similar to [passing an obfuscated
user account ID](https://developer.android.com/google/play/billing/unity#obfuscated-account-ids). In both cases the ID represents a
single user, but the profile ID lets you uniquely identify a single user across
multiple profiles that they have within a single app. After you send an
obfuscated profile ID to Google Play, you can retrieve that ID later in a
purchase receipt.

To pass an obfuscated profile ID, use your
IAP builder to modify your module's configuration by calling the
`SetObfuscatedProfileId()` method:

```
// Get the plugin extensions for the Google Play Store.
_playStoreExtensions =
    extensions.GetExtension<Google.Play.Billing.IGooglePlayStoreExtensions>();

// Pass an obfuscated profile ID.
_playStoreExtensions.SetObfuscatedProfileId(obfuscatedProfileId);
```



### Confirm price changes for subscriptions

Google Play allows you to [change the price of an active
subscription](https://developer.android.com/google/play/billing/billing_subscriptions#change-price-sub). Your
game's users must confirm any price change before the change can take effect. To
prompt users to confirm a price change for their subscription, call the
`ConfirmSubscriptionPriceChange()` method:

```
// Get the plugin extensions for the Google Play Store.
_playStoreExtensions =
    extensions.GetExtension<Google.Play.Billing.IGooglePlayStoreExtensions>();

_playStoreExtensions.ConfirmSubscriptionPriceChange(productId,
    delegate (bool success)
    {
        // Returns whether the user has accepted the new price or not.
    });
```



## Changes to Unity API behavior

When you are using the Google Play Billing plugin, most of the APIs behave the
same way as Unity's standard IAP implementation for other app stores. However,
there are some cases where the APIs will behave differently. This section
describes these behavior differences.

### Developer payload is not supported

Google Play deprecated developer payload and is replacing it with alternatives
that are more meaningful and contextual. For this reason, developer payload is
not supported. For more information on alternatives, see the page about
[Developer payload](https://developer.android.com/google/play/billing/developer-payload).

You can continue to use the same interfaces that are defined by Unity's standard
IAP implementation for other app stores, including `IStoreController`. When you
initiate a purchase, you can still use `IStoreController` and call the
`InitiatePurchase()` method:

```
public void InitiatePurchase(Purchasing.Product product, string payload);
```

However, any payload that you pass in won’t take effect (won’t appear in the
final receipt).

### SubscriptionManager is not supported

Unity IAP provides the [`SubscriptionManager`](https://docs.unity3d.com/Manual/UnityIAPSubscriptionProducts.html)
class for managing subscriptions. Because Unity's standard IAP implementation of
this class uses developer payload, this class is not supported. You can still
create this class, but you might receive unreliable data when using any of the
class's getter methods.

### UpdateSubscription has small API changes

The Google Play Billing plugin does not support using the
`SubscriptionManager.UpdateSubscription()` and
`SubscriptionManager.UpdateSubscriptionInGooglePlayStore()` methods to upgrade
and downgrade your subscriptions. If your game calls these methods, a
`GooglePlayStoreUnsupportedException` is thrown.

The Google Play Billing Library provides an alternative API to use in place of these
methods. To upgrade or downgrade a subscription, call the `UpdateSubscription()`
method using proration mode:

```
void UpdateSubscription(Product oldProduct, Product newProduct,
           GooglePlayStoreProrationMode prorationMode = GooglePlayStoreProrationMode.Unknown);
```

You can either wrap this method call with a platform check or in a catch block
when `GooglePlayStoreUnsupportedException` is caught.

For more information and examples of how to use proration mode, see [Set
proration mode](https://developer.android.com/google/play/billing/billing_subscriptions#prorate).
