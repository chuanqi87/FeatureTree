* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/corelocation#app-main)

Framework

# Core Location

Obtain the geographic location and orientation of a device.

iOS 2.0+iPadOS 2.0+Mac Catalyst 13.0+macOS 10.6+tvOS 9.0+visionOS 1.0+watchOS 2.0+

## [Overview](https://developer.apple.com/documentation/corelocation\#overview)

Core Location provides services that determine a device’s geographic location, altitude, and orientation, or its position relative to a nearby iBeacon device. The framework gathers data using all available components on the device, including the Wi-Fi, GPS, Bluetooth, magnetometer, barometer, and cellular hardware.

You use instances of the [`CLLocationManager`](https://developer.apple.com/documentation/corelocation/cllocationmanager) class to configure, start, and stop the Core Location services. A location manager object supports the following location-related activities:

Standard and significant location updates

Track large or small changes in the user’s current location with a configurable degree of accuracy.

Region monitoring

Monitor distinct regions of interest and generate location events when the user enters or leaves those regions.

Beacon ranging

Detect and locate nearby beacons.

Compass headings

Report heading changes from the onboard compass.

To use location services, call [`liveUpdates(_:)`](https://developer.apple.com/documentation/corelocation/cllocationupdate/liveupdates(_:)) to obtain an update stream, then asynchronously iterate over that stream to receive and process location updates, and receive diagnostic properties to understand if and why location updates don’t arrive.

If needed, the system prompts the user to grant or deny the request. An initial prompt is shown in the example below:

![A screenshot of an iPhone showing a prompt asking the user if they allow the “Park Finder” app to have access to their location. The options are “OK” and “Not now”.](https://developer.apple.com/tutorials/images/com.apple.corelocation/core-location-overview@2x.png)

On iOS devices, users can change location service settings at any time in the Settings app, affecting individual apps or the device as a whole. Your app receives events, including authorization changes, by observing asynchronous sequences from [`CLLocationUpdate`](https://developer.apple.com/documentation/corelocation/cllocationupdate) and [`CLMonitor`](https://developer.apple.com/documentation/corelocation/clmonitor-6ynwz).

## [Topics](https://developer.apple.com/documentation/corelocation\#topics)

### [Essentials](https://developer.apple.com/documentation/corelocation\#Essentials)

[Configuring your app to use location services](https://developer.apple.com/documentation/corelocation/configuring-your-app-to-use-location-services)

Prepare your app to start collecting location data.

[Supporting live updates in SwiftUI and Mac Catalyst apps](https://developer.apple.com/documentation/corelocation/supporting-live-updates-in-swiftui-and-mac-catalyst-apps)

Enable background events by adding lifecycle event support.

[`class CLLocationManager`](https://developer.apple.com/documentation/corelocation/cllocationmanager)

The object you use to start and stop the delivery of location-related events to your app.

[`class CLBackgroundActivitySession`](https://developer.apple.com/documentation/corelocation/clbackgroundactivitysession-3mzv3)

An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.

[`struct CLLocationUpdate`](https://developer.apple.com/documentation/corelocation/cllocationupdate)

A structure that contains the location information the framework delivers with each update.

[Adopting live updates in Core Location](https://developer.apple.com/documentation/corelocation/adopting-live-updates-in-core-location)

Simplify location delivery using asynchronous events in Swift.

[Monitoring location changes with Core Location](https://developer.apple.com/documentation/corelocation/monitoring-location-changes-with-core-location)

Define boundaries and act on user location updates.

### [Authorization](https://developer.apple.com/documentation/corelocation\#Authorization)

[Requesting authorization to use location services](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services)

Obtain authorization to use location services and manage changes to your app’s authorization status.

[Suspending authorization requests](https://developer.apple.com/documentation/corelocation/suspending-authorization-requests)

Defer the system’s authorization request dialog until your app is ready.

[`enum CLAuthorizationStatus`](https://developer.apple.com/documentation/corelocation/clauthorizationstatus)

Constants that indicate the app’s authorization to use location services.

[`enum CLAccuracyAuthorization`](https://developer.apple.com/documentation/corelocation/claccuracyauthorization)

Constants that indicate the level of location accuracy the app has authorization to use.

[`NSLocationAlwaysAndWhenInUseUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription)

A message that tells people why the app is requesting access to their location information at all times.

[`NSLocationWhenInUseUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationwheninuseusagedescription)

A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

[`NSLocationUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationusagedescription)

A message that tells people why the app is requesting access to their location information.

Deprecated

[`NSLocationDefaultAccuracyReduced`](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationdefaultaccuracyreduced)

A Boolean value that indicates whether the app requests reduced location accuracy by default.

[`NSLocationAlwaysUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription)

A message that tells people why the app is requesting access to their location at all times.

Deprecated

### [Monitoring](https://developer.apple.com/documentation/corelocation\#Monitoring)

[`actor CLMonitor`](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v)

An object that monitors the conditions you add to it.

### [Location updates](https://developer.apple.com/documentation/corelocation\#Location-updates)

[Getting the current location of a device](https://developer.apple.com/documentation/corelocation/getting-the-current-location-of-a-device)

Start location services and provide information the system needs to optimize power usage for those services.

[Handling location updates in the background](https://developer.apple.com/documentation/corelocation/handling-location-updates-in-the-background)

Configure your app to receive location updates when it isn’t running in the foreground.

[Creating a location push service extension](https://developer.apple.com/documentation/corelocation/creating-a-location-push-service-extension)

Add and configure an extension to enable your location-sharing app to access a person’s location in response to a request from someone else.

[`class CLLocation`](https://developer.apple.com/documentation/corelocation/cllocation)

The latitude, longitude, and course information reported by the system.

[`struct CLLocationCoordinate2D`](https://developer.apple.com/documentation/corelocation/cllocationcoordinate2d)

The latitude and longitude associated with a location, specified using the WGS 84 reference frame.

[`class CLFloor`](https://developer.apple.com/documentation/corelocation/clfloor)

The floor of a building on which the user’s device is located.

[`class CLVisit`](https://developer.apple.com/documentation/corelocation/clvisit)

Information about the user’s location during a specific period of time.

[`class CLLocationSourceInformation`](https://developer.apple.com/documentation/corelocation/cllocationsourceinformation)

Information about the source that provides a location.

[Monitoring location changes with Core Location](https://developer.apple.com/documentation/corelocation/monitoring-location-changes-with-core-location)

Define boundaries and act on user location updates.

[`class CLServiceSession`](https://developer.apple.com/documentation/corelocation/clservicesession-pt7n)

An object that provides diagnostics about an app’s authorization to use location services.

### [Region monitoring](https://developer.apple.com/documentation/corelocation\#Region-monitoring)

Configure geofences and receive notifications when the user’s device crosses the fence’s boundaries.

[Monitoring the user’s proximity to geographic regions](https://developer.apple.com/documentation/corelocation/monitoring-the-user-s-proximity-to-geographic-regions)

Use condition monitoring to determine when the user enters or leaves a geographic region.

[`class CLRegion`](https://developer.apple.com/documentation/corelocation/clregion)

A base class representing an area that can be monitored.

### [iBeacon](https://developer.apple.com/documentation/corelocation\#iBeacon)

[Ranging for Beacons](https://developer.apple.com/documentation/corelocation/ranging-for-beacons)

Configure a device to act as a beacon and to detect surrounding beacons.

[Determining the proximity to an iBeacon device](https://developer.apple.com/documentation/corelocation/determining-the-proximity-to-an-ibeacon-device)

Detect beacons and determine the relative distance to them.

[Turning an iOS device into an iBeacon device](https://developer.apple.com/documentation/corelocation/turning-an-ios-device-into-an-ibeacon-device)

Broadcast iBeacon signals from an iOS device.

[`class CLBeacon`](https://developer.apple.com/documentation/corelocation/clbeacon)

Information about an observed iBeacon device and its relative distance to a person’s device.

[`protocol CLCondition`](https://developer.apple.com/documentation/corelocation/clcondition-swift.protocol)

The abstract base class for all other monitor conditions.

### [Compass headings](https://developer.apple.com/documentation/corelocation\#Compass-headings)

Determine the device’s orientation relative to magnetic or true north.

[Getting heading and course information](https://developer.apple.com/documentation/corelocation/getting-heading-and-course-information)

Use a device’s orientation and course information for navigation.

[`class CLHeading`](https://developer.apple.com/documentation/corelocation/clheading)

The orientation of the user’s device, relative to true or magnetic north.

### [Geocoding](https://developer.apple.com/documentation/corelocation\#Geocoding)

[Converting between coordinates and user-friendly place names](https://developer.apple.com/documentation/corelocation/converting-between-coordinates-and-user-friendly-place-names)

Convert between a latitude and longitude pair and a more user-friendly description of that location.

[Converting a user’s location to a descriptive placemark](https://developer.apple.com/documentation/corelocation/converting-a-user-s-location-to-a-descriptive-placemark)

Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.

[`class CLGeocoder`](https://developer.apple.com/documentation/corelocation/clgeocoder)

An interface for converting between geographic coordinates and place names.

Deprecated

[`class CLPlacemark`](https://developer.apple.com/documentation/corelocation/clplacemark)

A user-friendly description of a geographic coordinate, often containing the name of the place, its address, and other relevant information.

Deprecated

### [Location push service extension](https://developer.apple.com/documentation/corelocation\#Location-push-service-extension)

[`Location Push Service Extension`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.location.push)

An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.

[`protocol CLLocationPushServiceExtension`](https://developer.apple.com/documentation/corelocation/cllocationpushserviceextension)

The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.

[`struct CLLocationPushServiceError`](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct)

Error codes the location manager returns if starting to monitor for location push notifications fails.

[`let CLLocationPushServiceErrorDomain: String`](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerrordomain)

The domain for Location Push Service Extension errors.

[`enum Code`](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/code)

Error codes the location manager returns if starting to monitor for location push notifications fails.

### [Errors](https://developer.apple.com/documentation/corelocation\#Errors)

[`struct CLError`](https://developer.apple.com/documentation/corelocation/clerror-swift.struct)

A Core Location error.

[`let kCLErrorDomain: String`](https://developer.apple.com/documentation/corelocation/kclerrordomain)

The domain for Core Location errors.

[`let kCLErrorUserInfoAlternateRegionKey: String`](https://developer.apple.com/documentation/corelocation/kclerroruserinfoalternateregionkey)

A key in the user information dictionary of an error relating to a delayed region-monitoring response.

### [Deprecated](https://developer.apple.com/documentation/corelocation\#Deprecated)

[API Reference\\
Deprecated](https://developer.apple.com/documentation/corelocation/deprecated)

### [Reference](https://developer.apple.com/documentation/corelocation\#Reference)

[API Reference\\
Core Location Constants](https://developer.apple.com/documentation/corelocation/core-location-constants)

This document describes the constants found in the Core Location framework.

[API Reference\\
Core Location Functions](https://developer.apple.com/documentation/corelocation/core-location-functions)

The Core Location framework provides functions to help you work with coordinate values.

### [Protocols](https://developer.apple.com/documentation/corelocation\#Protocols)

[`protocol CLBodyIdentifiable`](https://developer.apple.com/documentation/corelocation/clbodyidentifiable) Beta

Current page is Core Location