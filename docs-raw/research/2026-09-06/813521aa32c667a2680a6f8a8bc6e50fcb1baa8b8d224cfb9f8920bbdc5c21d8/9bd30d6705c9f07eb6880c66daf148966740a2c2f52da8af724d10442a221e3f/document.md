# Core Location

Obtain the geographic location and orientation of a device.

## Overview

Core Location provides services that determine a device’s geographic location, altitude, and orientation, or its position relative to a nearby iBeacon device. The framework gathers data using all available components on the device, including the Wi-Fi, GPS, Bluetooth, magnetometer, barometer, and cellular hardware.

You use instances of the [`CLLocationManager`](/documentation/CoreLocation/CLLocationManager) class to configure, start, and stop the Core Location services. A location manager object supports the following location-related activities:

- Standard and significant location updates: Track large or small changes in the user’s current location with a configurable degree of accuracy.
- Region monitoring: Monitor distinct regions of interest and generate location events when the user enters or leaves those regions.
- Beacon ranging: Detect and locate nearby beacons.
- Compass headings: Report heading changes from the onboard compass.

To use location services, call [`liveUpdates(_:)`](/documentation/CoreLocation/CLLocationUpdate/liveUpdates(_:)) to obtain an update stream, then asynchronously iterate over that stream to receive and process location updates, and receive diagnostic properties to understand if and why location updates don’t arrive.

If needed, the system prompts the user to grant or deny the request. An initial prompt is shown in the example below:

![A screenshot of an iPhone showing a prompt asking the user if they allow the “Park Finder” app to have access to their location. The options are “OK” and “Not now”.](images/com.apple.corelocation/core-location-overview@2x.png)

On iOS devices, users can change location service settings at any time in the Settings app, affecting individual apps or the device as a whole. Your app receives events, including authorization changes, by observing asynchronous sequences from [`CLLocationUpdate`](/documentation/CoreLocation/CLLocationUpdate) and [`CLMonitor`](/documentation/CoreLocation/CLMonitor-6ynwz).

## Topics

### Essentials

[Configuring your app to use location services](/documentation/CoreLocation/configuring-your-app-to-use-location-services)

Prepare your app to start collecting location data.

[Supporting live updates in SwiftUI and Mac Catalyst apps](/documentation/CoreLocation/supporting-live-updates-in-swiftui-and-mac-catalyst-apps)

Enable background events by adding lifecycle event support.

[`CLLocationManager`](/documentation/CoreLocation/CLLocationManager)

The object you use to start and stop the delivery of location-related events to your app.

[`CLBackgroundActivitySession`](/documentation/CoreLocation/CLBackgroundActivitySession-3mzv3)

An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.

[`CLBackgroundActivitySession`](/documentation/CoreLocation/CLBackgroundActivitySession-4nl4y)

An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.

[`CLLocationUpdate`](/documentation/CoreLocation/CLLocationUpdate)

A structure that contains the location information the framework delivers with each update.

[Adopting live updates in Core Location](/documentation/CoreLocation/adopting-live-updates-in-core-location)

Simplify location delivery using asynchronous events in Swift.

[Monitoring location changes with Core Location](/documentation/CoreLocation/monitoring-location-changes-with-core-location)

Define boundaries and act on user location updates.

### Authorization

[Requesting authorization to use location services](/documentation/CoreLocation/requesting-authorization-to-use-location-services)

Obtain authorization to use location services and manage changes to your app’s authorization status.

[Suspending authorization requests](/documentation/CoreLocation/suspending-authorization-requests)

Defer the system’s authorization request dialog until your app is ready.

[`CLAuthorizationStatus`](/documentation/CoreLocation/CLAuthorizationStatus)

Constants that indicate the app’s authorization to use location services.

[`CLAccuracyAuthorization`](/documentation/CoreLocation/CLAccuracyAuthorization)

Constants that indicate the level of location accuracy the app has authorization to use.

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSLocationAlwaysAndWhenInUseUsageDescription>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSLocationWhenInUseUsageDescription>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSLocationUsageDescription>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSLocationDefaultAccuracyReduced>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSLocationAlwaysUsageDescription>

### Monitoring

[`CLMonitor`](/documentation/CoreLocation/CLMonitor-6ynwz)

An object that monitors the conditions you add to it.

[`CLMonitor`](/documentation/CoreLocation/CLMonitor-2r51v)

An object that monitors the conditions you add to it.

[`CLUpdate`](/documentation/CoreLocation/CLUpdate)

An object that represents a location update.

### Location updates

[Getting the current location of a device](/documentation/CoreLocation/getting-the-current-location-of-a-device)

Start location services and provide information the system needs to optimize power usage for those services.

[Handling location updates in the background](/documentation/CoreLocation/handling-location-updates-in-the-background)

Configure your app to receive location updates when it isn’t running in the foreground.

[Creating a location push service extension](/documentation/CoreLocation/creating-a-location-push-service-extension)

Add and configure an extension to enable your location-sharing app to access a person’s location in response to a request from someone else.

[`CLLocation`](/documentation/CoreLocation/CLLocation)

The latitude, longitude, and course information reported by the system.

[`CLLocationCoordinate2D`](/documentation/CoreLocation/CLLocationCoordinate2D)

The latitude and longitude associated with a location, specified using the WGS 84 reference frame.

[`CLFloor`](/documentation/CoreLocation/CLFloor)

The floor of a building on which the user’s device is located.

[`CLVisit`](/documentation/CoreLocation/CLVisit)

Information about the user’s location during a specific period of time.

[`CLLocationSourceInformation`](/documentation/CoreLocation/CLLocationSourceInformation)

Information about the source that provides a location.

[Monitoring location changes with Core Location](/documentation/CoreLocation/monitoring-location-changes-with-core-location)

Define boundaries and act on user location updates.

[`CLServiceSession`](/documentation/CoreLocation/CLServiceSession-2ddhd)

[`CLServiceSession`](/documentation/CoreLocation/CLServiceSession-pt7n)

An object that provides diagnostics about an app’s authorization to use location services.

[`CLServiceSessionDiagnostic`](/documentation/CoreLocation/CLServiceSessionDiagnostic)

[`CLBackgroundActivitySessionDiagnostic`](/documentation/CoreLocation/CLBackgroundActivitySessionDiagnostic)

[`CLLocationUpdater`](/documentation/CoreLocation/CLLocationUpdater)

An object that provides device location updates.

### Region monitoring

Configure geofences and receive notifications when the user’s device crosses the fence’s boundaries.

[Monitoring the user’s proximity to geographic regions](/documentation/CoreLocation/monitoring-the-user-s-proximity-to-geographic-regions)

Use condition monitoring to determine when the user enters or leaves a geographic region.

[`CLRegion`](/documentation/CoreLocation/CLRegion)

A base class representing an area that can be monitored.

### iBeacon

[Ranging for Beacons](/documentation/CoreLocation/ranging-for-beacons)

Configure a device to act as a beacon and to detect surrounding beacons.

[Determining the proximity to an iBeacon device](/documentation/CoreLocation/determining-the-proximity-to-an-ibeacon-device)

Detect beacons and determine the relative distance to them.

[Turning an iOS device into an iBeacon device](/documentation/CoreLocation/turning-an-ios-device-into-an-ibeacon-device)

Broadcast iBeacon signals from an iOS device.

[`CLBeacon`](/documentation/CoreLocation/CLBeacon)

Information about an observed iBeacon device and its relative distance to a person’s device.

[`CLCondition`](/documentation/CoreLocation/CLCondition-swift.protocol)

The abstract base class for all other monitor conditions.

[`CLCondition`](/documentation/CoreLocation/CLCondition-c.class)

The abstract base class that all other conditions derive from.

[`CLBeaconIdentityCondition`](/documentation/CoreLocation/CLBeaconIdentityCondition)

A condition that describes the identity characteristics of a beacon.

[`CLCircularGeographicCondition`](/documentation/CoreLocation/CLCircularGeographicCondition)

A circular geographic condition that a center point and radius define.

### Compass headings

Determine the device’s orientation relative to magnetic or true north.

[Getting heading and course information](/documentation/CoreLocation/getting-heading-and-course-information)

Use a device’s orientation and course information for navigation.

[`CLHeading`](/documentation/CoreLocation/CLHeading)

The orientation of the user’s device, relative to true or magnetic north.

### Geocoding

[Converting between coordinates and user-friendly place names](/documentation/CoreLocation/converting-between-coordinates-and-user-friendly-place-names)

Convert between a latitude and longitude pair and a more user-friendly description of that location.

[Converting a user’s location to a descriptive placemark](/documentation/CoreLocation/converting-a-user-s-location-to-a-descriptive-placemark)

Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.

[`CLGeocoder`](/documentation/CoreLocation/CLGeocoder)

An interface for converting between geographic coordinates and place names.

[`CLPlacemark`](/documentation/CoreLocation/CLPlacemark)

A user-friendly description of a geographic coordinate, often containing the name of the place, its address, and other relevant information.

### Location push service extension

  <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.location.push>

[`CLLocationPushServiceExtension`](/documentation/CoreLocation/CLLocationPushServiceExtension)

The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.

[`CLLocationPushServiceError`](/documentation/CoreLocation/CLLocationPushServiceError-swift.struct)

Error codes the location manager returns if starting to monitor for location push notifications fails.

[`CLLocationPushServiceErrorDomain`](/documentation/CoreLocation/CLLocationPushServiceErrorDomain)

The domain for Location Push Service Extension errors.

[`Code`](/documentation/CoreLocation/CLLocationPushServiceError-swift.struct/Code)

Error codes the location manager returns if starting to monitor for location push notifications fails.

### Errors

[`CLError`](/documentation/CoreLocation/CLError-swift.struct)

A Core Location error.

[`kCLErrorDomain`](/documentation/CoreLocation/kCLErrorDomain)

The domain for Core Location errors.

[`kCLErrorUserInfoAlternateRegionKey`](/documentation/CoreLocation/kCLErrorUserInfoAlternateRegionKey)

A key in the user information dictionary of an error relating to a delayed region-monitoring response.

### Deprecated

[Deprecated](/documentation/CoreLocation/deprecated)

### Reference

[Core Location Constants](/documentation/CoreLocation/core-location-constants)

This document describes the constants found in the Core Location framework.

[Core Location Functions](/documentation/CoreLocation/core-location-functions)

The Core Location framework provides functions to help you work with coordinate values.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
