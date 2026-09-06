# Capturing screen content on iOS

Record and share screen captures on iOS by presenting the system content-sharing picker.

## Overview

This sample shows how to capture screen content on iOS using [`ScreenCaptureKit`](/documentation/ScreenCaptureKit). ScreenCaptureKit supports screen streaming and mirroring on all available platforms. You present the system content-sharing picker to let a person choose between capturing the entire display or content from within the sample, then stream that content with fine-grained control over audio, recording, and the camera.

You use the sample to record the screen to a file, to buffer up to 15 seconds of rolling video and export a clip on demand, and to show a live camera preview during in-app captures. When a recording finishes, the sample saves the file to Photos and offers it through the standard share sheet.

> Note: This sample requires a device running iOS 27 or later. The sample requests camera and photo library access at runtime.

## Configure the sample code project

The sample declares two background modes so ScreenCaptureKit continues to run while the app isn’t frontmost:

- `screen-capture` in <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/UIBackgroundModes>, so the stream survives backgrounding for full-display capture.
- `audio`, so the microphone tap keeps producing samples.

The Info property list also declares <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription> and <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSPhotoLibraryAddUsageDescription>. Verify both prompts appear the first time you exercise the in-app capture and recording flows.

## Present the content-sharing picker

The sample offers two entry points into the system picker: a full-display capture and an in-app capture. Both configure the shared [`SCContentSharingPicker`](/documentation/ScreenCaptureKit/SCContentSharingPicker) and register an observer before presenting the picker, so the app receives the resulting [`SCContentFilter`](/documentation/ScreenCaptureKit/SCContentFilter) regardless of which mode the person chooses.

For full-display capture, the sample calls [`present()`](/documentation/ScreenCaptureKit/SCContentSharingPicker/present()). For in-app capture, it calls [`presentForCurrentApplication()`](/documentation/ScreenCaptureKit/SCContentSharingPicker/presentForCurrentApplication()), which limits the picker to windows and layers owned by the running app.

```swift
func presentFullDisplayPicker() {
    picker.defaultConfiguration = fullDisplayPickerConfiguration
    activatePicker()
    captureMode = .fullDisplay
    picker.present()
}

func presentInAppPicker() {
    picker.defaultConfiguration = inAppPickerConfiguration
    activatePicker()
    captureMode = .inApp
    picker.presentForCurrentApplication()
}
```

Activating the picker registers the sample’s [`SCContentSharingPickerObserver`](/documentation/ScreenCaptureKit/SCContentSharingPickerObserver), so the app receives the selected filter through [`contentSharingPicker(_:didUpdateWith:for:)`](/documentation/ScreenCaptureKit/SCContentSharingPickerObserver/contentSharingPicker(_:didUpdateWith:for:)) and starts the stream from that callback.

## Configure the picker’s controls

The sample uses two [`SCContentSharingPickerConfiguration`](/documentation/ScreenCaptureKit/SCContentSharingPickerConfiguration-c.class) instances so it can tailor the picker to each capture mode. Both configurations allow toggling the microphone; only the in-app configuration enables the camera toggle, because ScreenCaptureKit doesn’t support a camera overlay for full-display captures.

```swift
var fullDisplayPickerConfiguration: SCContentSharingPickerConfiguration {
    var config = SCContentSharingPickerConfiguration()
    config.showsMicrophoneControl = showsMicrophoneControl
    return config
}

var inAppPickerConfiguration: SCContentSharingPickerConfiguration {
    var config = SCContentSharingPickerConfiguration()
    config.showsMicrophoneControl = showsMicrophoneControl
    config.showsCameraControl = showsCameraControl
    return config
}
```

The picker records the person’s choices in the returned filter’s [`isMicrophoneEnabled`](/documentation/ScreenCaptureKit/SCContentFilter/isMicrophoneEnabled) and [`isCameraEnabled`](/documentation/ScreenCaptureKit/SCContentFilter/isCameraEnabled) properties, which the sample checks when it attaches stream outputs.

## Start a stream from the filter

Once the picker returns a filter, the sample tears down any prior stream and builds a fresh [`SCStream`](/documentation/ScreenCaptureKit/SCStream) with a new [`SCStreamConfiguration`](/documentation/ScreenCaptureKit/SCStreamConfiguration). Screen frames flow through an output attached with the [`SCStreamOutputType.screen`](/documentation/ScreenCaptureKit/SCStreamOutputType/screen) type. The sample attaches a microphone output only when the filter’s [`isMicrophoneEnabled`](/documentation/ScreenCaptureKit/SCContentFilter/isMicrophoneEnabled) is `true`, mirroring the person’s selection in the picker.

```swift
let newStream = SCStream(filter: filter,
                         configuration: config,
                         delegate: self)
// Add screen stream output for every new stream.
try newStream.addStreamOutput(self, type: .screen,
                              sampleHandlerQueue: .main)
if filter.isMicrophoneEnabled {
    try newStream.addStreamOutput(self, type: .microphone,
                                  sampleHandlerQueue: .main)
}
...
try await newStream.startCapture()
```

Before starting a full-display capture, the sample activates an <doc://com.apple.documentation/documentation/AVFAudio/AVAudioSession> in the <doc://com.apple.documentation/documentation/AVFAudio/AVAudioSession/Category-swift.struct/playAndRecord> category so the microphone tap keeps producing samples while the app runs in the background.

## Record the stream to a file

The sample uses [`SCRecordingOutput`](/documentation/ScreenCaptureKit/SCRecordingOutput) to encode the stream directly to an MP4 file, so the code doesn’t need to handle sample buffers manually. It configures an output URL in the temporary directory through [`SCRecordingOutputConfiguration`](/documentation/ScreenCaptureKit/SCRecordingOutputConfiguration), adds the output to the running stream, and lets ScreenCaptureKit encode the file in place.

```swift
let config = SCRecordingOutputConfiguration()
config.outputURL = outputURL
...
let output = SCRecordingOutput(configuration: config,
                               delegate: delegate)
try stream.addRecordingOutput(output)
```

When the person stops the recording, the sample removes the output and awaits its finalization through a <doc://com.apple.documentation/documentation/Swift/CheckedContinuation>. The delegate’s [`recordingOutputDidFinishRecording(_:)`](/documentation/ScreenCaptureKit/SCRecordingOutputDelegate/recordingOutputDidFinishRecording(_:)) callback resumes the continuation, at which point the sample hands the file to Photos. The Recent tab later reads [`recordedDuration`](/documentation/ScreenCaptureKit/SCRecordingOutput/recordedDuration) and [`recordedFileSize`](/documentation/ScreenCaptureKit/SCRecordingOutput/recordedFileSize) from the finished `SCRecordingOutput` to display the recording’s duration and size.

## Save clips from a rolling buffer

For quick clips, the sample attaches an [`SCClipBufferingOutput`](/documentation/ScreenCaptureKit/SCClipBufferingOutput) to the same stream. The buffering output holds up to 15 seconds of rolling capture in memory without writing anything to disk. When the person taps Export Current Clip, the sample asks the output to write the most recent N seconds to a file.

```swift
let output = SCClipBufferingOutput(delegate: delegate)
try stream.addClipBufferingOutput(output)
...
// Later, in response to a user action:
output.exportClip(to: clipURL, duration: duration) { [weak self] error in
    ...
    // Save the clip to Photos on success.
    await self?.saveClipToPhotos(url: clipURL)
    ...
}
```

Exporting a clip doesn’t interrupt buffering, so the person can capture overlapping clips while the buffer continues to accumulate new frames.

## Preview the camera during capture

In-app capture mode supports an overlay of the device’s camera. When the filter’s [`isCameraEnabled`](/documentation/ScreenCaptureKit/SCContentFilter/isCameraEnabled) is `true`, the sample attaches an [`SCVideoEffectOutput`](/documentation/ScreenCaptureKit/SCVideoEffectOutput) and stores the <doc://com.apple.documentation/documentation/UIKit/UIView> the output vends. A <doc://com.apple.documentation/documentation/SwiftUI/UIViewRepresentable> wrapper embeds that view in the SwiftUI hierarchy so it renders as a floating rounded rectangle anchored to the bottom-trailing corner of the app.

```swift
if captureMode == .inApp && filter.isCameraEnabled,
    let device = AVCaptureDevice.default(.builtInWideAngleCamera,
                                         for: .video,
                                         position: .front) {
    let effectOutput = SCVideoEffectOutput(cameraDevice: device)
    try newStream.addVideoEffectOutput(effectOutput)
    videoEffectOutput = effectOutput
}
```

The sample re-attaches the preview when the app returns to the foreground, because the camera view’s underlying capture session pauses on backgrounding.

## Save recordings to Photos

When a recording or clip finishes, the sample writes it to Photos through <doc://com.apple.documentation/documentation/Photos/PHPhotoLibrary>. Because the sample only writes to Photos, it requests the narrower <doc://com.apple.documentation/documentation/Photos/PHAccessLevel/addOnly> authorization scope rather than full library access — the data-minimization pattern of requesting only what the feature needs. The sample hands the file off with <doc://com.apple.documentation/documentation/Photos/PHAssetResourceCreationOptions/shouldMoveFile> set to `true` so the temporary file doesn’t linger on disk.

```swift
let status = await PHPhotoLibrary.requestAuthorization(for: .addOnly)
guard status == .authorized || status == .limited else { return }
...
try await PHPhotoLibrary.shared().performChanges {
    let options = PHAssetResourceCreationOptions()
    options.shouldMoveFile = true
    let request = PHAssetCreationRequest.forAsset()
    request.addResource(with: .video, fileURL: url, options: options)
}
```

The Recent tab surfaces the last saved recording and clip and exposes both through <doc://com.apple.documentation/documentation/SwiftUI/ShareLink>, so the person can pass a file to another app without leaving the sample.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
