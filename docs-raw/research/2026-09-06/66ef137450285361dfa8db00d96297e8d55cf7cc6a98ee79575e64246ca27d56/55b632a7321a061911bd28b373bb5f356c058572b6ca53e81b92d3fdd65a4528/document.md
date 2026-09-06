# Core Motion

Process accelerometer, gyroscope, pedometer, and environment-related events.

## Overview

Core Motion reports motion- and environment-related data from the available onboard hardware of iOS, iPadOS, watchOS, and visionOS devices. This hardware includes the device’s accelerometers and gyroscopes, and, when available, the pedometer, magnetometer, and barometer. Use this data in your app as input for user interactions, fitness tracking, health-related matters, and more. For example, a game might use accelerometer and gyroscope input to control onscreen game behavior.

The services of this framework provide access to motion data either as raw or processed values, and many services provide both types of values. Raw values reflect the unmodified data from the hardware, while processed values eliminate forms of bias that might adversely affect your usage of the data. For example, a processed accelerometer value reflects only the acceleration caused by the user and not the acceleration caused by gravity.

Not all services are available on all devices, and some services might be unavailable even on devices with the required hardware. For example, many Core Motion services are available to visionOS apps, but those services aren’t available to compatible iPad and iPhone apps running in visionOS. Before you try to use any motion-related services, check the availability of those services using a [`CMMotionManager`](/documentation/CoreMotion/CMMotionManager) object.

> Important:
> An iOS app must include usage description keys in its `Info.plist` file for the types of data it needs. If these keys aren’t present, the app crashes when you try to access the corresponding service. To access motion and fitness data, include <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription>. To access the fall-detection service, include <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSFallDetectionUsageDescription>.

## Topics

### Essentials

  <doc://com.apple.documentation/documentation/Updates/CoreMotion>

[`CMMotionManager`](/documentation/CoreMotion/CMMotionManager)

The object for starting and managing motion services.

### Device motion

Access acceleration, attitude, rotation, and magnetic field data that is adjusted for gravity and other forms of bias.

[Getting processed device-motion data](/documentation/CoreMotion/getting-processed-device-motion-data)

Retrieve motion data that the system processed to remove environmental bias, such as the effects of gravity.

[`CMDeviceMotion`](/documentation/CoreMotion/CMDeviceMotion)

Encapsulated measurements of the attitude, rotation rate, and acceleration of a device.

[`CMAttitude`](/documentation/CoreMotion/CMAttitude)

The device’s orientation relative to a known frame of reference at a point in time.

[`CMAttitudeReferenceFrame`](/documentation/CoreMotion/CMAttitudeReferenceFrame)

Constants that indicate the frame of reference for attitude-related motion data.

[`CMHeadphoneMotionManager`](/documentation/CoreMotion/CMHeadphoneMotionManager)

An object that starts and manages headphone motion services.

### Accelerometers

Access accelerometer data for all three axes of the device.

[Getting raw accelerometer events](/documentation/CoreMotion/getting-raw-accelerometer-events)

Retrieve data from the onboard accelerometers.

[`CMAccelerometerData`](/documentation/CoreMotion/CMAccelerometerData)

A data sample from the device’s three accelerometers.

[`CMRecordedAccelerometerData`](/documentation/CoreMotion/CMRecordedAccelerometerData)

A single piece of accelerometer data that was recorded by the device.

[`CMSensorRecorder`](/documentation/CoreMotion/CMSensorRecorder)

An object that gathers and retrieves accelerometer data from a device.

[`CMSensorDataList`](/documentation/CoreMotion/CMSensorDataList)

A list of the accelerometer data recorded by the system.

### Gyroscopes

Access the raw gyroscope data.

[Getting raw gyroscope events](/documentation/CoreMotion/getting-raw-gyroscope-events)

Retrieve data from the onboard gyroscopes.

[`CMGyroData`](/documentation/CoreMotion/CMGyroData)

A single measurement of the device’s rotation rate.

### Magnetometer

Access raw magnetometer data.

[`CMMagnetometerData`](/documentation/CoreMotion/CMMagnetometerData)

Measurements of the Earth’s magnetic field relative to the device.

### Altitude data

Access altitude data based on barometric sensor information.

[`CMAltimeter`](/documentation/CoreMotion/CMAltimeter)

An object that initiates the delivery of altitude-related changes.

[`CMAbsoluteAltitudeData`](/documentation/CoreMotion/CMAbsoluteAltitudeData)

Data that records a change in absolute altitude.

[`CMAltitudeData`](/documentation/CoreMotion/CMAltitudeData)

Data for a recorded change in altitude.

### Ambient pressure

[`CMRecordedPressureData`](/documentation/CoreMotion/CMRecordedPressureData)

A recorded measurement of pressure data.

[`CMAmbientPressureData`](/documentation/CoreMotion/CMAmbientPressureData)

A measurement of the ambient pressure and temperature.

### Water submersion

[Accessing submersion data](/documentation/CoreMotion/accessing-submersion-data)

Use a water-submersion manager to receive water pressure, temperature, and depth data on Apple Watch Ultra.

[`CMWaterSubmersionManager`](/documentation/CoreMotion/CMWaterSubmersionManager)

An object for managing the collection of pressure and temperature data during submersion.

[`CMWaterSubmersionManagerDelegate`](/documentation/CoreMotion/CMWaterSubmersionManagerDelegate)

A delegate that receives updates about ambient pressure, water pressure, water temperature, and submersion events.

[`CMWaterSubmersionEvent`](/documentation/CoreMotion/CMWaterSubmersionEvent)

An event indicating that the device’s submersion state has changed.

[`CMWaterSubmersionMeasurement`](/documentation/CoreMotion/CMWaterSubmersionMeasurement)

An update that contains data about the pressure and depth.

[`CMWaterTemperature`](/documentation/CoreMotion/CMWaterTemperature)

An update that contains data about the water temperature.

### Activity

[`CMMotionActivityManager`](/documentation/CoreMotion/CMMotionActivityManager)

An object that manages access to the motion data stored by the device.

[`CMHeadphoneActivityManager`](/documentation/CoreMotion/CMHeadphoneActivityManager)

An object that starts and manages headphone activity services.

[`CMMotionActivity`](/documentation/CoreMotion/CMMotionActivity)

The data for a single motion update event.

[Getting motion-activity data from headphones](/documentation/CoreMotion/getting-motion-activity-data-from-headphones)

Configure your app to listen for motion-activity changes from headphones.

### Pedometer and fitness

Access step-counting data from the built-in motion processor.

[`CMPedometer`](/documentation/CoreMotion/CMPedometer)

An object for fetching the system-generated live walking data.

[`CMPedometerData`](/documentation/CoreMotion/CMPedometerData)

Information about the distance traveled by a user on foot.

[`CMPedometerEvent`](/documentation/CoreMotion/CMPedometerEvent)

A change in the user’s pedestrian activity.

[`CMStepCounter`](/documentation/CoreMotion/CMStepCounter)

The number of steps the user has taken with the device.

[`CMOdometerData`](/documentation/CoreMotion/CMOdometerData)

A class that represents odometer data for workouts.

[`CMHighFrequencyHeartRateData`](/documentation/CoreMotion/CMHighFrequencyHeartRateData)

A class that represents heart rate data collected at 1 Hz.

### Movement disorder

[Getting movement disorder symptom data](/documentation/CoreMotion/getting-movement-disorder-symptom-data)

Retrieve data from the Apple Watch’s movement disorder manager.

[Adhering to the movement disorder data collection requirements](/documentation/CoreMotion/adhering-to-the-movement-disorder-data-collection-requirements)

Ensure that your users understand and have control over the data your app collects.

[Movement disorder algorithm changelog](/documentation/CoreMotion/movement-disorder-algorithm-changelog)

A chronological log of notable changes to the movement disorder algorithm.

[`CMMovementDisorderManager`](/documentation/CoreMotion/CMMovementDisorderManager)

A manager for recording and querying movement disorder data.

[`CMTremorResult`](/documentation/CoreMotion/CMTremorResult)

A result object that contains data about the presence and strength of tremors during a one-minute interval.

[`CMDyskineticSymptomResult`](/documentation/CoreMotion/CMDyskineticSymptomResult)

A result object that contains data about the likely presence of dyskinetic symptoms during a one-minute interval.

### Fall detection

[`CMFallDetectionManager`](/documentation/CoreMotion/CMFallDetectionManager)

An object for managing fall detection events.

[`CMFallDetectionDelegate`](/documentation/CoreMotion/CMFallDetectionDelegate)

A delegate that receives information about fall detection events and authorization status changes.

[`CMFallDetectionEvent`](/documentation/CoreMotion/CMFallDetectionEvent)

An object that contains data about a fall detection event.

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSFallDetectionUsageDescription>

### Historical data

Access recorded motion events to help you analyze movement patterns.

[`CMBatchedSensorManager`](/documentation/CoreMotion/CMBatchedSensorManager)

### Common data

[`CMLogItem`](/documentation/CoreMotion/CMLogItem)

The base class for all motion-related data objects.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
