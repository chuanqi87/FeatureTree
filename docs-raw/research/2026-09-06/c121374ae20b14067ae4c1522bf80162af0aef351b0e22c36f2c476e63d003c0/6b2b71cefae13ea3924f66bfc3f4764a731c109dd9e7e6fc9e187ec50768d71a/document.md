# Capture setup

Configure built-in cameras and microphones, and external capture devices, for media capture.

## Discussion

The AVFoundation Capture subsystem provides a common high-level architecture for video, photo, and audio capture services in iOS and macOS. Use this system if you want to:

- Build a custom camera UI to integrate shooting photos or videos into your app’s user experience.
- Give users more direct control over photo and video capture, such as focus, exposure, and stabilization options.
- Produce different results than the system camera UI, such as RAW format photos, depth maps, or videos with custom timed metadata.
- Get live access to pixel or audio data streaming directly from a capture device.

> Note:
> To instead let the user capture media with the system camera UI within your app, see <doc://com.apple.documentation/documentation/UIKit/UIImagePickerController>.

The main parts of the capture architecture are sessions, inputs, and outputs: Capture sessions connect one or more inputs to one or more outputs. Inputs are sources of media, including capture devices like the cameras and microphones built into an iOS device or Mac. Outputs acquire media from inputs to produce useful data, such as movie files written to disk or raw pixel buffers available for live processing.

![Block diagram of the basic capture session architecture: an AVCaptureSession acquires data from an AVCaptureDevice through AVCaptureDeviceInput, and provides data to one or more AVCaptureOutput objects.](images/com.apple.avfoundation/media-2970476.png)

## Topics

### Essentials

[Requesting authorization to capture and save media](/documentation/AVFoundation/requesting-authorization-to-capture-and-save-media)

Prompt the user to authorize access to the camera, microphone, and photo library.

### Capture sessions

[Setting up a capture session](/documentation/AVFoundation/setting-up-a-capture-session)

Configure input devices, output media, preview views, and basic settings before capturing photos or video.

  <doc://com.apple.documentation/documentation/AVKit/accessing-the-camera-while-multitasking-on-ipad>

[AVCam: Building a camera app](/documentation/AVFoundation/avcam-building-a-camera-app)

Capture photos and record video using the front and rear iPhone and iPad cameras.

[Building a responsive camera app that launches quickly](/documentation/AVFoundation/building-a-responsive-camera-app-that-launches-quickly)

Show a camera preview sooner by deferring capture output setup and postponing noncritical interface elements.

[Capturing Cinematic video](/documentation/AVFoundation/capturing-cinematic-video)

Capture video with an adjustable depth of field and focus points.

[Supporting Center Stage front camera in your iOS app](/documentation/AVFoundation/supporting-center-stage-front-camera-in-your-ios-app)

Enable Center Stage for photos and videos on the iPhone front camera.

[AVMultiCamPiP: Capturing from Multiple Cameras](/documentation/AVFoundation/avmulticampip-capturing-from-multiple-cameras)

Simultaneously record the output from the front and back cameras into a single movie file by using a multi-camera capture session.

[AVCamBarcode: detecting barcodes and faces](/documentation/AVFoundation/avcambarcode-detecting-barcodes-and-faces)

Identify machine readable codes or faces by using the camera.

[`AVCaptureSession`](/documentation/AVFoundation/AVCaptureSession)

An object that configures capture behavior and coordinates the flow of data from input devices to capture outputs.

[`AVCaptureMultiCamSession`](/documentation/AVFoundation/AVCaptureMultiCamSession)

A capture session that supports simultaneous capture from multiple inputs of the same media type.

[`AVCaptureInput`](/documentation/AVFoundation/AVCaptureInput)

An abstract superclass for objects that provide input data to a capture session.

[`AVCaptureOutput`](/documentation/AVFoundation/AVCaptureOutput)

An abstract superclass for objects that provide media output destinations for a capture session.

[`AVCaptureConnection`](/documentation/AVFoundation/AVCaptureConnection)

An object that represents a connection from a capture input to a capture output.

### Capture devices

[Choosing a capture device](/documentation/AVFoundation/choosing-a-capture-device)

Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.

[Adopting smart framing in your camera app](/documentation/AVFoundation/adopting-smart-framing-in-your-camera-app)

Capture the optimal shot by providing automatic framing recommendations.

[`AVCaptureDevice`](/documentation/AVFoundation/AVCaptureDevice)

An object that represents a hardware or virtual capture device like a camera or microphone.

[`AVCaptureDeviceInput`](/documentation/AVFoundation/AVCaptureDeviceInput)

An object that provides media input from a capture device to a capture session.

[`AVContinuityDevice`](/documentation/AVFoundation/AVContinuityDevice)

A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.

[`AVExternalStorageDevice`](/documentation/AVFoundation/AVExternalStorageDevice)

Represents a physical external storage device that stores media assets.

[`AVExternalStorageDeviceDiscoverySession`](/documentation/AVFoundation/AVExternalStorageDeviceDiscoverySession)

Informs your app when the external storage devices connect to and disconnect from the system.

### Capture preview

[`AVCaptureVideoPreviewLayer`](/documentation/AVFoundation/AVCaptureVideoPreviewLayer)

A Core Animation layer that displays video from a camera device.

[`AVCaptureAudioPreviewOutput`](/documentation/AVFoundation/AVCaptureAudioPreviewOutput)

A capture output that provides a preview of the captured audio.

### Continuity Camera

  <doc://com.apple.documentation/documentation/AVKit/supporting-continuity-camera-in-your-tvos-app>

[Supporting Continuity Camera in your macOS app](/documentation/AVFoundation/supporting-continuity-camera-in-your-macos-app)

Enable high-quality photo and video capture by using an iPhone camera as an external capture device.

[`AVCaptureDeskViewApplication`](/documentation/AVFoundation/AVCaptureDeskViewApplication)

An object that programmatically presents Desk View.

### Capture controls

[Enhancing your app experience with the Camera Control](/documentation/AVFoundation/enhancing-your-app-experience-with-the-camera-control)

Provide direct access to your camera app’s features to help people quickly capture the perfect shot.

[`AVCaptureControl`](/documentation/AVFoundation/AVCaptureControl)

An abstract base class for controls that interact with the camera system.

[`AVCaptureSystemZoomSlider`](/documentation/AVFoundation/AVCaptureSystemZoomSlider)

A control that adjusts the video zoom factor of a capture device within the system-recommended range.

[`AVCaptureSystemExposureBiasSlider`](/documentation/AVFoundation/AVCaptureSystemExposureBiasSlider)

A control that adjusts the exposure bias of a capture device within the system-recommended range.

[`AVCaptureSlider`](/documentation/AVFoundation/AVCaptureSlider)

A slider control that selects a value from a bounded range.

[`AVCaptureIndexPicker`](/documentation/AVFoundation/AVCaptureIndexPicker)

A control for selecting from a set of mutually exclusive values by index.

### External display output

[`AVCaptureExternalDisplayConfiguration`](/documentation/AVFoundation/AVCaptureExternalDisplayConfiguration)

A class you use to specify a configuration to your external display configurator.

[`AVCaptureExternalDisplayConfigurator`](/documentation/AVFoundation/AVCaptureExternalDisplayConfigurator)

A configurator class allowing you to configure properties of an external display to match the camera’s active video format.

### Timecode generation

[`AVCaptureTimecodeGenerator`](/documentation/AVFoundation/AVCaptureTimecodeGenerator)

Generates and synchronizes timecode data from various sources for precise video and audio synchronization.

[`AVCaptureTimecodeGeneratorDelegate`](/documentation/AVFoundation/AVCaptureTimecodeGeneratorDelegate)

A protocol for receiving real-time timecode updates and error notifications from a timecode generator.

[`SynchronizationStatus`](/documentation/AVFoundation/AVCaptureTimecodeGenerator/SynchronizationStatus)

Constants defining the synchronization status of a timecode generator .

[`Source`](/documentation/AVFoundation/AVCaptureTimecode/Source)

Describes a timecode source that a timecode generator can synchronize to.

[`SourceType`](/documentation/AVFoundation/AVCaptureTimecode/SourceType-swift.enum)

Defines possible sources for generating timecode in using a timecode generator.

[`AVCaptureTimecode`](/documentation/AVFoundation/AVCaptureTimecode)

This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.

[`AVCaptureTimecodeAdvancedByFrames`](/documentation/AVFoundation/AVCaptureTimecode/advanced(_:by:))

Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.

[`AVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp`](/documentation/AVFoundation/AVCaptureTimecode/createMetadataSampleBuffer(from:associatedWithPresentationTimeStamp:))

Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.

[`AVCaptureTimecodeCreateMetadataSampleBufferForDuration`](/documentation/AVFoundation/AVCaptureTimecode/createMetadataSampleBuffer(from:forDuration:))

Creates a sample buffer containing Timecode Media Description metadata for a specified duration.

### External synchronization

[`AVExternalSyncDevice`](/documentation/AVFoundation/AVExternalSyncDevice)

An external sync device connected to a host device that can be used to drive the timing of an internal component, such as a camera sensor.

[`AVExternalSyncDeviceDelegate`](/documentation/AVFoundation/AVExternalSyncDeviceDelegate)

Defines an interface for delegates of [`AVCaptureDeviceInput`](/documentation/AVFoundation/AVCaptureDeviceInput) to respond to events that occur when connecting, calibrating, and disconnecting external sync devices.

[`AVExternalSyncDeviceStatus`](/documentation/AVFoundation/AVExternalSyncDeviceStatus)

Connection state of an external sync device

[`DiscoverySession`](/documentation/AVFoundation/AVExternalSyncDevice/DiscoverySession)

A means of discovering and monitoring connection / disconnection of external sync devices to the host.

### Video analytics

### Pro video storage

[`AVProVideoStorage`](/documentation/AVFoundation/AVProVideoStorage)

A class to track and manage pre-allocated storage for high data rate video capture.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
