* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/coremotion#app-main)

Framework

# Core Motion

Process accelerometer, gyroscope, pedometer, and environment-related events.

iOS 4.0+iPadOS 4.0+Mac Catalyst 13.0+macOS 10.15+visionOS 1.0+watchOS 2.0+

## [Overview](https://developer.apple.com/documentation/coremotion\#overview)

Core Motion reports motion- and environment-related data from the available onboard hardware of iOS, iPadOS, watchOS, and visionOS devices. This hardware includes the device’s accelerometers and gyroscopes, and, when available, the pedometer, magnetometer, and barometer. Use this data in your app as input for user interactions, fitness tracking, health-related matters, and more. For example, a game might use accelerometer and gyroscope input to control onscreen game behavior.

The services of this framework provide access to motion data either as raw or processed values, and many services provide both types of values. Raw values reflect the unmodified data from the hardware, while processed values eliminate forms of bias that might adversely affect your usage of the data. For example, a processed accelerometer value reflects only the acceleration caused by the user and not the acceleration caused by gravity.

Not all services are available on all devices, and some services might be unavailable even on devices with the required hardware. For example, many Core Motion services are available to visionOS apps, but those services aren’t available to compatible iPad and iPhone apps running in visionOS. Before you try to use any motion-related services, check the availability of those services using a [`CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager) object.

## [Topics](https://developer.apple.com/documentation/coremotion\#topics)

### [Essentials](https://developer.apple.com/documentation/coremotion\#Essentials)

[Core Motion updates](https://developer.apple.com/documentation/updates/coremotion)

Learn about important changes to Core Motion.

[`class CMMotionManager`](https://developer.apple.com/documentation/coremotion/cmmotionmanager)

The object for starting and managing motion services.

### [Device motion](https://developer.apple.com/documentation/coremotion\#Device-motion)

Access acceleration, attitude, rotation, and magnetic field data that is adjusted for gravity and other forms of bias.

[Getting processed device-motion data](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data)

Retrieve motion data that the system processed to remove environmental bias, such as the effects of gravity.

[`class CMDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmdevicemotion)

Encapsulated measurements of the attitude, rotation rate, and acceleration of a device.

[`class CMAttitude`](https://developer.apple.com/documentation/coremotion/cmattitude)

The device’s orientation relative to a known frame of reference at a point in time.

[`struct CMAttitudeReferenceFrame`](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)

Constants that indicate the frame of reference for attitude-related motion data.

[`class CMHeadphoneMotionManager`](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager)

An object that starts and manages headphone motion services.

### [Accelerometers](https://developer.apple.com/documentation/coremotion\#Accelerometers)

Access accelerometer data for all three axes of the device.

[Getting raw accelerometer events](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events)

Retrieve data from the onboard accelerometers.

[`class CMAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata)

A data sample from the device’s three accelerometers.

[`class CMRecordedAccelerometerData`](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)

A single piece of accelerometer data that was recorded by the device.

[`class CMSensorRecorder`](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)

An object that gathers and retrieves accelerometer data from a device.

[`class CMSensorDataList`](https://developer.apple.com/documentation/coremotion/cmsensordatalist)

A list of the accelerometer data recorded by the system.

### [Gyroscopes](https://developer.apple.com/documentation/coremotion\#Gyroscopes)

Access the raw gyroscope data.

[Getting raw gyroscope events](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events)

Retrieve data from the onboard gyroscopes.

[`class CMGyroData`](https://developer.apple.com/documentation/coremotion/cmgyrodata)

A single measurement of the device’s rotation rate.

### [Magnetometer](https://developer.apple.com/documentation/coremotion\#Magnetometer)

Access raw magnetometer data.

[`class CMMagnetometerData`](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata)

Measurements of the Earth’s magnetic field relative to the device.

### [Altitude data](https://developer.apple.com/documentation/coremotion\#Altitude-data)

Access altitude data based on barometric sensor information.

[`class CMAltimeter`](https://developer.apple.com/documentation/coremotion/cmaltimeter)

An object that initiates the delivery of altitude-related changes.

[`class CMAbsoluteAltitudeData`](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata)

Data that records a change in absolute altitude.

[`class CMAltitudeData`](https://developer.apple.com/documentation/coremotion/cmaltitudedata)

Data for a recorded change in altitude.

### [Ambient pressure](https://developer.apple.com/documentation/coremotion\#Ambient-pressure)

[`class CMRecordedPressureData`](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata)

A recorded measurement of pressure data.

[`class CMAmbientPressureData`](https://developer.apple.com/documentation/coremotion/cmambientpressuredata)

A measurement of the ambient pressure and temperature.

### [Water submersion](https://developer.apple.com/documentation/coremotion\#Water-submersion)

[Accessing submersion data](https://developer.apple.com/documentation/coremotion/accessing-submersion-data)

Use a water-submersion manager to receive water pressure, temperature, and depth data on Apple Watch Ultra.

[`class CMWaterSubmersionManager`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager)

An object for managing the collection of pressure and temperature data during submersion.

[`protocol CMWaterSubmersionManagerDelegate`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate)

A delegate that receives updates about ambient pressure, water pressure, water temperature, and submersion events.

[`class CMWaterSubmersionEvent`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent)

An event indicating that the device’s submersion state has changed.

[`class CMWaterSubmersionMeasurement`](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement)

An update that contains data about the pressure and depth.

[`class CMWaterTemperature`](https://developer.apple.com/documentation/coremotion/cmwatertemperature)

An update that contains data about the water temperature.

### [Activity](https://developer.apple.com/documentation/coremotion\#Activity)

[`class CMMotionActivityManager`](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)

An object that manages access to the motion data stored by the device.

[`class CMHeadphoneActivityManager`](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)

An object that starts and manages headphone activity services.

[`class CMMotionActivity`](https://developer.apple.com/documentation/coremotion/cmmotionactivity)

The data for a single motion update event.

[Getting motion-activity data from headphones](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones)

Configure your app to listen for motion-activity changes from headphones.

### [Pedometer and fitness](https://developer.apple.com/documentation/coremotion\#Pedometer-and-fitness)

Access step-counting data from the built-in motion processor.

[`class CMPedometer`](https://developer.apple.com/documentation/coremotion/cmpedometer)

An object for fetching the system-generated live walking data.

[`class CMPedometerData`](https://developer.apple.com/documentation/coremotion/cmpedometerdata)

Information about the distance traveled by a user on foot.

[`class CMPedometerEvent`](https://developer.apple.com/documentation/coremotion/cmpedometerevent)

A change in the user’s pedestrian activity.

[`class CMStepCounter`](https://developer.apple.com/documentation/coremotion/cmstepcounter)

The number of steps the user has taken with the device.

Deprecated

[`class CMOdometerData`](https://developer.apple.com/documentation/coremotion/cmodometerdata)

A class that represents odometer data for workouts.

[`class CMHighFrequencyHeartRateData`](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata)

A class that represents heart rate data collected at 1 Hz.

### [Movement disorder](https://developer.apple.com/documentation/coremotion\#Movement-disorder)

[Getting movement disorder symptom data](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)

Retrieve data from the Apple Watch’s movement disorder manager.

[Adhering to the movement disorder data collection requirements](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements)

Ensure that your users understand and have control over the data your app collects.

[Movement disorder algorithm changelog](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog)

A chronological log of notable changes to the movement disorder algorithm.

[`class CMMovementDisorderManager`](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)

A manager for recording and querying movement disorder data.

[`class CMTremorResult`](https://developer.apple.com/documentation/coremotion/cmtremorresult)

A result object that contains data about the presence and strength of tremors during a one-minute interval.

[`class CMDyskineticSymptomResult`](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult)

A result object that contains data about the likely presence of dyskinetic symptoms during a one-minute interval.

### [Fall detection](https://developer.apple.com/documentation/coremotion\#Fall-detection)

[`class CMFallDetectionManager`](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager)

An object for managing fall detection events.

[`protocol CMFallDetectionDelegate`](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate)

A delegate that receives information about fall detection events and authorization status changes.

[`class CMFallDetectionEvent`](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent)

An object that contains data about a fall detection event.

[`NSFallDetectionUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsfalldetectionusagedescription)

A message to the user that explains the app’s request for permission to access fall detection event data.

### [Historical data](https://developer.apple.com/documentation/coremotion\#Historical-data)

Access recorded motion events to help you analyze movement patterns.

[`class CMBatchedSensorManager`](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager)

### [Common data](https://developer.apple.com/documentation/coremotion\#Common-data)

[`class CMLogItem`](https://developer.apple.com/documentation/coremotion/cmlogitem)

The base class for all motion-related data objects.

### [Classes](https://developer.apple.com/documentation/coremotion\#Classes)

[`class CMRecordedDeviceMotion`](https://developer.apple.com/documentation/coremotion/cmrecordeddevicemotion) Beta

### [Protocols](https://developer.apple.com/documentation/coremotion\#Protocols)

[`protocol CMBodyIdentifiable`](https://developer.apple.com/documentation/coremotion/cmbodyidentifiable) Beta

Current page is Core Motion