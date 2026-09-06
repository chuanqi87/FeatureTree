# Creating a media device extension

Provide a way for people to find, connect to, and control your media device by adding a device extension in your iOS app.

## Overview

A media device extension brings TVs, speakers, and streaming devices into systems’s media device picker, the picker that opens when someone taps an <doc://com.apple.documentation/documentation/AVKit/AVRoutePickerView> in an app. Your extension implements a media sharing protocol that handles discovery, connection, and playback for these devices.

When a person opens the media device picker, the system launches your extension and asks it discover available devices. Your extension scans for nearby devices and reports each one to the system, so they appear in the picker.

When the person selects a device, the system calls [`activateDevice(_:session:for:)`](/documentation/MediaDevice/MediaDeviceExtension/activateDevice(_:session:for:)). Your extension connects to the device and reports the result through [`routingManager(for:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/routingManager(for:)): call [`activatedDevice(_:session:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/activatedDevice(_:session:)) on success, or [`failedToActivateDevice(_:session:error:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/failedToActivateDevice(_:session:error:)) on failure.

> Important: Only maintain connections to devices the system has activated. Don’t make persistent connections that extend beyond the purpose of discovery before the system notifies you that the person has made a selection and activated a device.

When the device is active, your extension is ready to receive media. Media apps that support your protocol use <doc://com.apple.documentation/documentation/AVSystemRouting/AVSystemRoute-5s2um> to start playback on the device. If your extension conforms to [`RealtimeSampleHandling`](/documentation/MediaDevice/RealtimeSampleHandling), the system also routes real-time audio or video samples to it.

Your extension works with <doc://com.apple.documentation/documentation/AVSystemRouting>, the framework media apps use to observe routes and control playback. Apps observe route changes through <doc://com.apple.documentation/documentation/AVSystemRouting/AVSystemRouteController-18ns8> and control playback through <doc://com.apple.documentation/documentation/AVSystemRouting/AVSystemRoute-5s2um>. Your extension handles the protocol-specific communication with the hardware.

## Create and configure the extension target

In Xcode, choose File > New > Target, select Generic Extension. Xcode adds the new extension to your project.

Both the extension and its container app require the <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.media-device-extension> entitlement set to Media Sharing Protocol ID that uniquely names your protocol:

```xml
<key>com.apple.developer.media-device-extension</key>
<string>com.example.sharingprotocol</string>
```

In the extension’s Info pane in Xcode, set `EXExtensionPointIdentifier` to `com.apple.media-device-extension` inside the `EXAppExtensionAttributes` dictionary.

## Declare your protocol type

Your Media Sharing Protocol ID identifies your protocol throughout the system, and you set it in three places that must all use the same value:

1. The string value of the `com.apple.developer.media-device-extension` entitlement (set above).
2. The `UTTypeIdentifier` of a `UTExportedTypeDeclarations` entry in the extension’s Info pane in Xcode.
3. The identifier your extension’s [`protocolType`](/documentation/MediaDevice/MediaDeviceExtension/protocolType) property returns.

Declare a custom Uniform Type Identifier in the extension’s Info pane in Xcode using the same identifier. The type must conform to `public.media-sharing-protocol`:

```xml
<key>UTExportedTypeDeclarations</key>
<array>
    <dict>
        <key>UTTypeIdentifier</key>
        <string>com.example.sharingprotocol</string>
        <key>UTTypeDescription</key>
        <string>My Sharing Protocol</string>
        <key>UTTypeConformsTo</key>
        <array>
            <string>public.media-sharing-protocol</string>
        </array>
    </dict>
</array>
```

The system uses the `UTTypeDescription` value as your protocol’s display name. It appears in the media device picker, in the Settings interface that lets people choose a preferred protocol, and in system-surfaced error screens. Choose a name that is short, recognizable, and appropriate for people to easily identify your device.

## Implement the media device extension

In the new target, create a class that conforms to [`MediaDeviceExtension`](/documentation/MediaDevice/MediaDeviceExtension) and mark it with `@main`:

```swift
import MediaDevice
import UniformTypeIdentifiers

@main
@available(iOS 27.0, *)
class MyDeviceExtension: MediaDeviceExtension {

    var protocolType: UTType {
        UTType(exportedAs: "com.example.sharingprotocol")
    }

    var supportsSimultaneousSessions: Bool { false }

    lazy var routingManager: MediaDeviceRoutingManager = .routingManager(for: self)

    required init() {}

    func startDeviceDiscovery() {
        // Start protocol-specific network discovery here.
    }

    func stopDeviceDiscovery() {
        // Stop protocol-specific network discovery here.
    }

    func activateDevice(
        _ device: MediaOutputDevice,
        session: MediaOutputSession,
        for deviceFeatures: MediaOutputDevice.Capabilities
    ) {
        // Connect to the device and report the result through the routing manager.
    }

    func connectUsingPairingCode(
        _ pairingCode: String?,
        to device: MediaOutputDevice,
        session: MediaOutputSession
    ) {
        // Authenticate the device with the person's pairing input.
    }

    func deactivateDevice(
        _ device: MediaOutputDevice,
        session: MediaOutputSession
    ) {
        // Disconnect the device and release any session-scoped resources.
    }

    func setVolume(_ volume: Float, for device: MediaOutputDevice) {
        // Set the device's volume to the requested level in the range 0.0 - 1.0.
    }

    func volume(for device: MediaOutputDevice) -> Float {
        // Return the device's current volume level in the range 0.0 - 1.0.
        0
    }

    func changeVolume(by increments: Int, for device: MediaOutputDevice) {
        // Apply a relative volume change to the device.
    }

    func muteDevice(_ device: MediaOutputDevice) {
        // Mute the device.
    }

    func isDeviceMuted(_ device: MediaOutputDevice) -> Bool {
        // Return the device's current mute state.
        false
    }

    func startSession(
        _ session: MediaOutputSession,
        identifier: String?,
        url: URL
    ) {
        // Begin playback of the URL on the remote device.
    }

    func stopSession(_ session: MediaOutputSession) {
        // Stop playback for this session.
    }

    func sendData(
        _ data: Data,
        toApplication applicationIdentifier: String,
        session: MediaOutputSession
    ) {
        // Forward the data payload to the target app on the remote device.
    }
}
```

The `routingManager` property is how your extension communicates with the system. Obtain an instance by calling [`routingManager(for:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/routingManager(for:)), then use it throughout your extension to report discovered devices, activation results, sessions, and pairing requests.

The `supportsSimultaneousSessions` property tells the system whether your extension can handle multiple [`MediaOutputSession`](/documentation/MediaDevice/MediaOutputSession) instances at the same time.

## Discover devices on the network

When a person opens the media device picker, the system calls [`startDeviceDiscovery()`](/documentation/MediaDevice/MediaDeviceExtension/startDeviceDiscovery()). Use your protocol’s discovery mechanism to find devices, then report them to the system through [`routingManager(for:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/routingManager(for:)).

```swift
func startDeviceDiscovery() {
    // Start protocol-specific network discovery here.
    // As you find devices, create a `MediaOutputDevice` and report it
    // to make the device available to the system.
    // Use a stable identifier (for example, derived from your protocol's
    // device ID) so the same physical device produces the same ID
    // across discoveries.

    guard let device = MediaOutputDevice(
        id: deviceID,
        displayName: "Living Room TV",
        capabilities: [.urlPlayback],
        requiredNetworkEndpoints: endpoints
    ) else { return }

    routingManager.foundDevice(device)
}

func stopDeviceDiscovery() {
    // Stop protocol-specific network discovery here.
}
```

Report discovery events through [`routingManager(for:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/routingManager(for:)) as devices appear and disappear on the network:

- [`foundDevice(_:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/foundDevice(_:)) — Reports a newly discovered device so the system can include it in the device list.
- [`lostDevice(_:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/lostDevice(_:)) — Removes a previously discovered device from the device list.
- [`updateDevices(_:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/updateDevices(_:)) — Refreshes the state of one or more devices after their properties change.
- [`discoveryFailed(_:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/discoveryFailed(_:)) — Reports an unexpected discovery failure. Don’t call this when no devices are found.

The system caches the devices your extension reports so it can bring them up quickly in future sessions, like it does for AirPlay. When you call [`foundDevice(_:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/foundDevice(_:)), the system stores and associates the device’s details with both the current network and your extension.

The next time someone opens the picker on the same network, the system uses the cache to surface those devices before your extension rediscovers them. Each time your extension reports a device with the same [`id`](/documentation/MediaDevice/MediaOutputDevice/id), the system refreshes the cached entry with the updated details. Devices that go several days without discovery drop out of the cache.

Because of this caching, a device your extension hasn’t reported yet in the current session might appear in the picker. This is expected behavior, and the system removes the device if your extension calls [`lostDevice(_:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/lostDevice(_:)) or the device isn’t found when the person picks it.

## Activate a device

When a person selects a device, the system calls [`activateDevice(_:session:for:)`](/documentation/MediaDevice/MediaDeviceExtension/activateDevice(_:session:for:)). Connect to the device and report the result through [`routingManager(for:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/routingManager(for:)).

```swift
func activateDevice(
    _ device: MediaOutputDevice,
    session: MediaOutputSession,
    for deviceFeatures: MediaOutputDevice.Capabilities
) {
    // Handle possible device authorization here.

    do {
        try myProtocolClient.connect(to: device)
        routingManager.activatedDevice(device, session: session)
    } catch {
        routingManager.failedToActivateDevice(
            device,
            session: session,
            error: MediaDeviceError(.connectionFailed)
        )
    }
}
```

When the person disconnects from the device, the system calls [`deactivateDevice(_:session:)`](/documentation/MediaDevice/MediaDeviceExtension/deactivateDevice(_:session:)). Disconnect and release any resources associated with the session.

## Handle device authorization

Some devices require pairing before activation. When a device needs authorization, call [`requestPairingCode(for:session:reason:authorizationMethod:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/requestPairingCode(for:session:reason:authorizationMethod:)) to present a pairing interface. The [`MediaOutputDevice.AuthorizationMethod`](/documentation/MediaDevice/MediaOutputDevice/AuthorizationMethod) type defines the available pairing interfaces:

- [`numericCode(length:)`](/documentation/MediaDevice/MediaOutputDevice/AuthorizationMethod/numericCode(length:)) — A numeric PIN code with a fixed digit count. Pass [`fourCharacter`](/documentation/MediaDevice/MediaOutputDevice/AuthorizationMethod/CodeLength/fourCharacter) or [`sixCharacter`](/documentation/MediaDevice/MediaOutputDevice/AuthorizationMethod/CodeLength/sixCharacter).
- [`password`](/documentation/MediaDevice/MediaOutputDevice/AuthorizationMethod/password) — A text password.
- [`none`](/documentation/MediaDevice/MediaOutputDevice/AuthorizationMethod/none) — No authorization required.

The system collects the person’s input and delivers it to [`connectUsingPairingCode(_:to:session:)`](/documentation/MediaDevice/MediaDeviceExtension/connectUsingPairingCode(_:to:session:)):

```swift
func activateDevice(
    _ device: MediaOutputDevice,
    session: MediaOutputSession,
    for deviceFeatures: MediaOutputDevice.Capabilities
) {
    if myProtocolClient.requiresPairing(device) {
        routingManager.requestPairingCode(
            for: device,
            session: session,
            reason: "Enter the code shown on your TV.",
            authorizationMethod: .numericCode(length: .fourCharacter)
        )
    } else {
        // Handle regular device activation here.
        do {
            try myProtocolClient.connect(to: device)
            routingManager.activatedDevice(device, session: session)
        } catch {
            routingManager.failedToActivateDevice(
                device,
                session: session,
                error: MediaDeviceError(.connectionFailed)
            )
        }
    }
}

func connectUsingPairingCode(
    _ pairingCode: String?,
    to device: MediaOutputDevice,
    session: MediaOutputSession
) {
    guard let code = pairingCode else {
        // The person canceled pairing with their iPhone.
        routingManager.failedToActivateDevice(
            device,
            session: session,
            error: MediaDeviceError(.authorizationFailed)
        )
        return
    }

    do {
        try myProtocolClient.authenticate(with: code, device: device)
        routingManager.activatedDevice(device, session: session)
    } catch {
        routingManager.failedToActivateDevice(
            device,
            session: session,
            error: MediaDeviceError(.authorizationFailed)
        )
    }
}
```

## Start media playback

After activation, the system calls [`startSession(_:identifier:url:)`](/documentation/MediaDevice/MediaDeviceExtension/startSession(_:identifier:url:)) to begin playback. Send the URL to the device and report success through [`routingManager(for:)`](/documentation/MediaDevice/MediaDeviceRoutingManager/routingManager(for:)):

```swift
func startSession(
    _ session: MediaOutputSession,
    identifier: String?,
    url: URL
) {
    do {
        let playbackControl = try myProtocolClient.startPlayback(
            url: url,
            applicationIdentifier: identifier
        )
        routingManager.started(
            application: identifier,
            playbackControl: playbackControl,
            session: session
        )
    } catch {
        routingManager.sessionFailed(
            session,
            error: MediaDeviceError(.sessionFailed)
        )
    }
}

func stopSession(_ session: MediaOutputSession) {
    myProtocolClient.stopPlayback()
}
```

The `playbackControl` parameter conforms to <doc://com.apple.documentation/documentation/AVKit/AVPlaybackUserInterfaceControllable>, which models the full playback state of the remote session. Update its properties to keep the system in sync as playback progresses: for example, `isPlaying`, `state`, `currentPlaybackPosition`, `playbackSpeed`, `timeRange`, and `metadata`.

The system observes these properties and drives the shared playback UI from them, including Now Playing, the media device picker, and any controls surfaced by media apps. The system also uses the object’s conformance to `AVInterfacePlaybackControllable` to deliver play, pause, and seek commands back to your extension.

### Stream real-time samples

Some devices receive audio or video samples directly instead of fetching a URL. Real-time sample delivery is orthogonal to URL playback, and a device can support any combination of the two:

- For devices that receive audio samples directly, set the device’s capabilities to include [`realtimeAudioStreaming`](/documentation/MediaDevice/MediaOutputDevice/Capabilities-swift.struct/realtimeAudioStreaming). The system routes audio destined for that device through your extension.
- For devices that receive video frames directly to support screen-mirroring, set the device’s capabilities to include [`realtimeVideoStreaming`](/documentation/MediaDevice/MediaOutputDevice/Capabilities-swift.struct/realtimeVideoStreaming). The system routes screen frames to your extension only while screen mirroring is active. A device that supports real-time video streaming must also support real-time audio streaming, so include [`realtimeAudioStreaming`](/documentation/MediaDevice/MediaOutputDevice/Capabilities-swift.struct/realtimeAudioStreaming) in its capabilities as well.

Ensure your extension class conforms to [`RealtimeSampleHandling`](/documentation/MediaDevice/RealtimeSampleHandling). The system calls [`startRealtimeSampleDelivery(session:)`](/documentation/MediaDevice/RealtimeSampleHandling/startRealtimeSampleDelivery(session:)) when samples start flowing, and [`stopRealtimeSampleDelivery(session:)`](/documentation/MediaDevice/RealtimeSampleHandling/stopRealtimeSampleDelivery(session:)) to stop them.

Whether you stream audio or mirror the screen, your extension must publish an audio server driver plug-in when the system activates the device. Build it by following <doc://com.apple.documentation/documentation/CoreAudio/creating-an-audio-server-driver-plug-in>, then publish it from [`startRealtimeSampleDelivery(session:)`](/documentation/MediaDevice/RealtimeSampleHandling/startRealtimeSampleDelivery(session:)) by calling `AudioServerPlugInRegisterMediaDeviceExtension`. The plug-in must present a single output device whose unique identifier matches the device’s [`id`](/documentation/MediaDevice/MediaOutputDevice/id) and whose transport type is `kAudioDeviceTransportTypeRemoteScreen` for screen mirroring or `kAudioDeviceTransportTypeRemoteStreaming` for audio streaming.

> Important: The audio device must appear promptly upon activation, or the system deactivates your device and playback fails with an “Unable to Connect” message.

To capture the samples themselves, use the appropriate system framework:

- For audio, receive the system audio through the audio server driver plug-in you publish (its I/O callbacks deliver the mixed audio), then use <doc://com.apple.documentation/documentation/AudioToolbox> to encode it.
- For video, use <doc://com.apple.documentation/documentation/ScreenCaptureKit> to receive system video, then <doc://com.apple.documentation/documentation/VideoToolbox> to encode it.

```swift
@main
@available(iOS 27.0, *)
class MyDeviceExtension: MediaDeviceExtension, RealtimeSampleHandling {

    // Implement the `MediaDeviceExtension` requirements above.

    func startRealtimeSampleDelivery(session: MediaOutputSession) {
        // Start capturing samples and send them to the remote device.
    }

    func stopRealtimeSampleDelivery(session: MediaOutputSession) {
        // Stop capturing samples and remove any encoders.
    }
}
```

## Provide volume control

Configure volume support when you create a [`MediaOutputDevice`](/documentation/MediaDevice/MediaOutputDevice) by setting its [`MediaOutputDevice.VolumeControl`](/documentation/MediaDevice/MediaOutputDevice/VolumeControl-swift.enum) mode:

- [`MediaOutputDevice.VolumeControl.absolute`](/documentation/MediaDevice/MediaOutputDevice/VolumeControl-swift.enum/absolute) — The device supports direct volume levels. The system calls [`setVolume(_:for:)`](/documentation/MediaDevice/MediaDeviceExtension/setVolume(_:for:)) and [`volume(for:)`](/documentation/MediaDevice/MediaDeviceExtension/volume(for:)) to set and read the volume.
- [`MediaOutputDevice.VolumeControl.relative`](/documentation/MediaDevice/MediaOutputDevice/VolumeControl-swift.enum/relative) — The device supports only incremental adjustments. The system calls [`changeVolume(by:for:)`](/documentation/MediaDevice/MediaDeviceExtension/changeVolume(by:for:)) to raise or lower the volume.
- [`MediaOutputDevice.VolumeControl.none`](/documentation/MediaDevice/MediaOutputDevice/VolumeControl-swift.enum/none) — The device doesn’t support volume control.

Absolute volume levels must be represented in the range of 0.0 - 1.0.

```swift
func setVolume(_ volume: Float, for device: MediaOutputDevice) {
    myProtocolClient.setVolume(volume, on: device)
}

func volume(for device: MediaOutputDevice) -> Float {
    myProtocolClient.currentVolume(for: device)
}

func changeVolume(by increments: Int, for device: MediaOutputDevice) {
    myProtocolClient.adjustVolume(by: increments, on: device)
}

func muteDevice(_ device: MediaOutputDevice) {
    myProtocolClient.mute(device)
}

func isDeviceMuted(_ device: MediaOutputDevice) -> Bool {
    myProtocolClient.isMuted(device)
}
```

> Important: Only call ``doc://com.apple.mediadevice/documentation/MediaDevice/MediaDeviceRoutingManager/volumeChanged(for:)`` when the device’s volume changes externally, such as from a physical button press or another app. Don’t call it in response to system-initiated calls like ``doc://com.apple.mediadevice/documentation/MediaDevice/MediaDeviceExtension/setVolume(_:for:)`` or ``doc://com.apple.mediadevice/documentation/MediaDevice/MediaDeviceExtension/changeVolume(by:for:)``.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
