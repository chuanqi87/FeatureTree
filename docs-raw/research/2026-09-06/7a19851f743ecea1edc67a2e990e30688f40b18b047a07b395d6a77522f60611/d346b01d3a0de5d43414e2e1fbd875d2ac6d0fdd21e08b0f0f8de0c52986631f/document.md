# Workgroup Management

Coordinate the activity of custom real-time audio threads with those of the system and other processes.

## Discussion

Real-time audio rendering often requires coordination between the threads of an app, the system, and the threads of any active Audio Unit plug-ins. Workgroups provide the mechanism to coordinate the efforts of these different processes, and ensure that they execute on the same schedule. In an Audio Unit, use a render context observer to retrieve the workgroup that the host app uses for real-time audio rendering. In an app, fetch the workgroup for a Core Audio device directly from the device or from your [`AUAudioUnit`](/documentation/AudioToolbox/AUAudioUnit) object.

If your app has real-time rendering threads that operate on their own deadlines, create your own workgroup using the [`AudioWorkIntervalCreate`](/documentation/AudioToolbox/AudioWorkIntervalCreate) function. Use your custom workgroup to set and update the rendering schedule for your threads.

## Topics

### Essentials

[Understanding Audio Workgroups](/documentation/AudioToolbox/understanding-audio-workgroups)

Learn how to optimize real-time rendering performance with the Audio Workgroups API.

[Adding Parallel Real-Time Threads to Audio Workgroups](/documentation/AudioToolbox/adding-parallel-real-time-threads-to-audio-workgroups)

Optimize the performance of real-time audio threads that run in sync with the I/O thread by adding them to the audio device workgroup.

[Adding Asynchronous Real-Time Threads to Audio Workgroups](/documentation/AudioToolbox/adding-asynchronous-real-time-threads-to-audio-workgroups)

Optimize system performance by adding real-time audio threads that run asynchronously to the I/O thread to custom audio workgroups.

[Adding Audio Unit Auxiliary Real-Time Threads to Audio Workgroups](/documentation/AudioToolbox/adding-audio-unit-auxiliary-real-time-threads-to-audio-workgroups)

If your Audio Unit plug-in creates auxiliary real-time rendering threads, add them to the host app’s audio workgroup so the system can schedule them appropriately.

### Host App Workgroup

[`kAudioUnitProperty_RenderContextObserver`](/documentation/AudioToolbox/kAudioUnitProperty_RenderContextObserver)

The block that the system calls when the rendering context changes.

[`AURenderContextObserver`](/documentation/AudioToolbox/AURenderContextObserver)

A custom block that tells the audio unit which thread context to use for the next render cycle.

[`AudioUnitRenderContext`](/documentation/AudioToolbox/AudioUnitRenderContext)

A structure that contains thread context information for a real-time rendering operation.

### Device Workgroup

  <doc://com.apple.documentation/documentation/CoreAudio/kAudioDevicePropertyIOThreadOSWorkgroup>

[`kAudioOutputUnitProperty_OSWorkgroup`](/documentation/AudioToolbox/kAudioOutputUnitProperty_OSWorkgroup)

The workgroup associated with the audio device underlying this Audio Unit.

### Custom Workgroups

[`AudioWorkIntervalCreate`](/documentation/AudioToolbox/AudioWorkIntervalCreate)

Creates a new interval workgroup for managing real-time audio threads.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
