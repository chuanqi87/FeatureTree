# HealthKit

Access and share health and fitness data while maintaining the user’s privacy and control.

## Overview

HealthKit provides a central repository for health and fitness data on iPhone and Apple Watch. With the user’s permission, apps communicate with the HealthKit store to access and share this data.

![An image showing the Health app summary screen.](images/com.apple.healthkit/health-summary@2x.png)

Creating a complete, personalized health and fitness experience includes a variety of tasks:

- Collecting and storing health and fitness data
- Analyzing and visualizing the data
- Enabling social interactions

HealthKit apps take a collaborative approach to building this experience. Your app doesn’t need to provide all of these features. Instead, you can focus just on the subset of tasks that most interests you.

For example, users can select their favorite weight-tracking, step-counting, and health challenge app, each calibrated to their personal needs. Because HealthKit apps freely exchange data (with user permission), the combined suite provides a more customized experience than any single app on its own. For example, when a group of friends joins a daily step-counting challenge, each person can use their preferred hardware device and app to track their steps, while everyone in the group uses the same social app for the challenge.

HealthKit is also designed to manage and merge data from multiple sources. For example, users can view and manage all of their data in the Health App, including adding data, deleting data, and changing an app’s permissions. Therefore, your app needs to handle these changes, even when they occur outside your app.

> Note:
> Because health data may contain sensitive, personal information, apps must receive permission from the user to read data from or write data to the HealthKit store. They must also take steps to protect that data at all times. For more information, see <doc://com.apple.healthkit/documentation/HealthKit/protecting-user-privacy>.

## Topics

### Essentials

  <doc://com.apple.healthkit/documentation/HealthKit/about-the-healthkit-framework>

  <doc://com.apple.healthkit/documentation/HealthKit/setting-up-healthkit>

  <doc://com.apple.healthkit/documentation/HealthKit/authorizing-access-to-health-data>

  <doc://com.apple.healthkit/documentation/HealthKit/protecting-user-privacy>

  <doc://com.apple.documentation/documentation/Updates/HealthKit>

[`HealthKitUI`](/documentation/HealthKitUI)

Display user interface that enables a person to view and interact with their health data.

### Health data

  <doc://com.apple.healthkit/documentation/HealthKit/saving-data-to-healthkit>

  <doc://com.apple.healthkit/documentation/HealthKit/reading-data-from-healthkit>

[`HKHealthStore`](/documentation/HealthKit/HKHealthStore)

The access point for all data managed by HealthKit.

  <doc://com.apple.healthkit/documentation/HealthKit/creating-a-mobility-health-app>

  <doc://com.apple.healthkit/documentation/HealthKit/data-types>

  <doc://com.apple.healthkit/documentation/HealthKit/samples>

  <doc://com.apple.healthkit/documentation/HealthKit/queries>

  <doc://com.apple.healthkit/documentation/HealthKit/visualizing-healthkit-state-of-mind-in-visionos>

  <doc://com.apple.healthkit/documentation/HealthKit/logging-symptoms-associated-with-a-medication>

### Workout data

  <doc://com.apple.healthkit/documentation/HealthKit/workouts-and-activity-rings>

### Errors

[`HKError`](/documentation/HealthKit/HKError)

An error returned from a HealthKit method.

[`HKErrorDomain`](/documentation/HealthKit/HKErrorDomain)

The domain for all HealthKit errors.

[`Code`](/documentation/HealthKit/HKError/Code)

Error codes returned by HealthKit.

### Reference

  <doc://com.apple.healthkit/documentation/HealthKit/healthkit-enumerations>

  <doc://com.apple.healthkit/documentation/HealthKit/healthkit-classes>

  <doc://com.apple.healthkit/documentation/HealthKit/healthkit-constants>

  <doc://com.apple.healthkit/documentation/HealthKit/healthkit-data-types>

  <doc://com.apple.healthkit/documentation/HealthKit/healthkit-functions>

  <doc://com.apple.healthkit/documentation/HealthKit/HealthKit-macros>

  <doc://com.apple.healthkit/documentation/HealthKit/healthkit-variables>



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
