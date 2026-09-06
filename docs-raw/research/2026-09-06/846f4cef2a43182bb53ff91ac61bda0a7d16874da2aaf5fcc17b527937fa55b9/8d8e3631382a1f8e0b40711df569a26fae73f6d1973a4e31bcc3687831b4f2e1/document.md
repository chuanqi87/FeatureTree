# Set up an Xcode project

After you enable billing and create an API key, you're ready to set up the Xcode
project that you use to develop your app.

[Release notes](https://developers.google.com/maps/documentation/navigation/ios-sdk/release-notes) are
available for each release.

## Step 1: Install the required software

To build a project using the Navigation SDK for iOS, you must download and install:

* [Xcode](https://developer.apple.com/xcode/)
  **version 26.0** or later

## Step 2: Create the Xcode project and install the Navigation SDK

### Swift Package Manager

The Navigation SDK can be installed via [Swift Package Manager](https://developer.apple.com/documentation/xcode/swift-packages). To add the SDK, ensure you have
removed any existing Navigation SDK dependencies.

To add the SDK to a new or existing project, follow these steps:

1. Open your Xcode `project` or `workspace`, then go to **File > Add Package Dependencies**.
2. Enter <https://github.com/googlemaps/ios-navigation-sdk> as the URL, press **Enter**
   to pull in the package, and click "Add Package".
3. To install a specific `version`, set the **Dependency Rule** field to one of
   the version-based options. For new projects, we recommend specifying the latest version and
   using the "Exact Version" option. Once complete, click "Add Package".
4. From the **Choose Package Products** window, verify `GoogleNavigation` will be added to
   your designated `main` target. Once complete, click "Add Package".
5. To verify your installation, navigate to your target's **General** pane.
   In the **Frameworks, Libraries, and Embedded Content** you should see the installed packages.
   You can also view the "Package Dependencies" section of "Project Navigator"
   to verify the package and its version.

To update the `package` for an existing project, follow these steps:

1. From Xcode, go to **File > Packages > Update To Latest Package Versions**.
2. To verify your installation, go to the **Package Dependencies** section of **Project Navigator**
   to verify the package and its version.

**Important:** Sometimes, artifacts cannot be resolved or errors can occur,
in this case select "File > Packages > Reset Package Cache".
To remove existing Navigation SDK for iOS installed manually,
follow these steps:

1. From your Xcode project configuration settings, find **Frameworks, Libraries,
   and Embedded Content**. Use the **minus sign(-)** to remove the following framework:
   * `GoogleMaps.xcframework`
   * `GoogleNavigation.xcframework`
2. From the top level directory of your Xcode project, remove the `GoogleMaps`
   bundle.

### Manual installation

This guide shows how to manually add the XCFrameworks containing the
Navigation SDK for iOS, and the [Maps SDK for iOS](https://developers.google.com/maps/documentation/ios-sdk) to your project and configure your build settings in Xcode. An XCFramework is a binary package that you can use on multiple platforms, including machines using the M1 chipset

Follow these steps to install the XCFrameworks for the Navigation SDK for iOS,
and the Maps SDK for iOS:

1. Download the following SDK binaries and resource files:
   * [GoogleMaps](https://dl.google.com/geosdk/swiftpm/11.1.0/GoogleMaps_3p.xcframework.zip)
   * [GoogleMapsResources](https://dl.google.com/geosdk/swiftpm/11.1.0/GoogleMapsResources.zip)
   * [GoogleNavigation](https://dl.google.com/geosdk/swiftpm/11.1.0/GoogleNavigation_3p.xcframework.zip)
   * [GoogleNavigationResources](https://dl.google.com/geosdk/swiftpm/11.1.0/GoogleNavigationResources.zip)
2. Launch Xcode and either open an existing project, or create a new
   project. If you're new to iOS, create a new project and select the
   **iOS App template**.
3. Remove all existing Maps, Navigation, and Places references from the project.
   **Important:** The
   Places SDK for iOS is not included with the Navigation SDK for iOS,
   and must be installed separately. This is true as of version 5.0 of the
   Places SDK for iOS. Google recommends that you download and
   install the same versions of the Places SDK for iOS and
   the Navigation SDK for iOS. See
   [Install the Places SDK for iOS](https://developers.google.com/maps/documentation/places/ios-sdk/start).
4. Drag the following XCFrameworks into your project under
   **Frameworks, Libraries, and Embedded Content** to install both the Maps
   and Navigation SDKs (when prompted, select **Copy items if needed**):
   * `GoogleMaps.xcframework`
   * `GoogleNavigation.xcframework`
5. Drag `GoogleMaps.bundle` from **GoogleMapsResources** you downloaded
   into the top level directory of your Xcode project. When prompted,
   ensure **Copy items if needed** is selected.
6. Drag `GoogleNavigation.bundle` from **GoogleNavigationResources** you downloaded
   into the top level directory of your Xcode project. When prompted, ensure
   **Copy items into destination group's folder** is selected.
7. Select your project from the Project Navigator, and choose your
   application's target.
8. Open the **Build Phases** tab, and within
   **Link Binary with Libraries**, add the following frameworks and libraries:
   * `Accelerate.framework`
   * `AudioToolbox.framework`
   * `AVFoundation.framework`
   * `CarPlay.framework`
   * `Contacts.framework`
   * `CoreData.framework`
   * `CoreGraphics.framework`
   * `CoreImage.framework`
   * `CoreLocation.framework`
   * `CoreTelephony.framework`
   * `CoreText.framework`
   * `GLKit.framework`
   * `ImageIO.framework`
   * `libc++.tbd`
   * `libxml2.tbd`
   * `libz.tbd`
   * `MapKit.framework`
   * `Metal.framework`
   * `OpenGLES.framework`
   * `QuartzCore.framework`
   * `Security.framework`
   * `SystemConfiguration.framework`
   * `UIKit.framework`
   * `UserNotifications.framework`
   * `WebKit.framework`
9. In your application's target, select the **Capabilities** tab,
   turn on **Background Modes**, and enable the following modes:
   * **Audio, AirPlay, and Picture in Picture**
   * **Location updates**
10. Choose your project, rather than a specific target, and open the **Build
    Settings** tab. In the **Other Linker Flags** section,
    add `‑ObjC` for both **debug** and **release**.
    If these settings are not visible, change the filter in the
    **Build Settings** bar from **Basic** to **All**.
    **Important:** The SDK contains Swift symbols. If you are creating a purely Objective-C project, you must also create an empty `.swift` file in your project, or add the following into the **Other Linker Flags** section of the Xcode project.

    ```
    -L$(DEVELOPER_DIR)/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/$(PLATFORM_NAME)
    ```
11. Open `Info.plist` and add the following key-value pairs:
    * **Key:** `NSLocationWhenInUseUsageDescription` (*Privacy - Location When In Use Usage Description*)  
      **Value:** "This app needs permission to use your location for turn-by-turn navigation."
    * **Key:** `NSLocationAlwaysAndWhenInUseUsageDescription` (*Privacy - Location Always and When In Use Usage Description*)  
      **Value:** "This app needs permission to use your location for turn-by-turn navigation."

## Step 3: Add your API key to the project

The following examples show how to add the API key to your project in Xcode:

### Swift

Add your API key to your `AppDelegate.swift` as follows:

1. Add the following import statements:

   ```
   import GoogleMaps
   import GoogleNavigation
   ```
2. Add the following to your `application(_:didFinishLaunchingWithOptions:)`
   method:

   ```
   GMSServices.provideAPIKey("YOUR_API_KEY")
   ```

### Objective-C

Add your API key to your `AppDelegate.m` as follows:

1. Add the following import statements:

   ```
   @import GoogleMaps;
   @import GoogleNavigation;
   ```
2. Add the following to your `application:didFinishLaunchingWithOptions:`
   method:

   ```
   [GMSServices provideAPIKey:@"YOUR_API_KEY"];
   ```

## Step 4 (optional): Inspect Apple Privacy Manifest file

**Note:** The following is relevant when you deploy your app to the web store.

Apple requires app privacy details for apps on the App Store. Visit the [Apple App Store Privacy Details page](https://developers.google.com/maps/documentation/ios-sdk/apple-privacy-policy) for updates and more information.

The Apple Privacy Manifest file is included in the resources bundle for the SDK. To verify that the Privacy Manifest File has been included, and to inspect its contents, create an archive of your app and [generate a privacy report](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187) from the archive.

## If you are a Mobility Services customer

If you are a Mobility Services customer, learn about billing
in the Mobility documentation. For more information about recording
transactions, see
[Set up billing](https://developers.google.com/maps/documentation/transportation-logistics-terms/mobility/set-up-billing).
To learn how to add transaction IDs to your Navigation SDK implementation, see
[Associate your service usage to Mobility transactions](https://developers.google.com/maps/documentation/transportation-logistics-terms/mobility/associate-service-usage).

## What's next

Now that you have an API key and an Xcode project, you can create and run apps.
The Navigation SDK for iOS provides tutorials that can help you
get started. For more details, see:

* Tutorials
  + [Navigate a route](https://developers.google.com/maps/documentation/navigation/ios-sdk/route)
  + [Listen for navigation events](https://developers.google.com/maps/documentation/navigation/ios-sdk/events)
* [Use App Check to secure your API key](https://developers.google.com/maps/documentation/navigation/ios-sdk/app-check)
* [Code samples and Codelab](https://developers.google.com/maps/documentation/navigation/ios-sdk/samples)
