* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/replaykit#app-main)

Framework

# ReplayKit

Record or stream video from the screen, and audio from the app and microphone.

iOS 9.0+iPadOS 9.0+Mac Catalyst 13.0+macOS 11.0+tvOS 10.0+visionOS 1.0+

## [Overview](https://developer.apple.com/documentation/replaykit\#overview)

Using the ReplayKit framework, users can record video from the screen, and audio from the app and microphone. They can then share their recordings with other users through email, messages, and social media. You can build app extensions for live broadcasting your content to sharing services. ReplayKit is incompatible with [`AVPlayer`](https://developer.apple.com/documentation/avfoundation/avplayer) content.

## [Topics](https://developer.apple.com/documentation/replaykit\#topics)

### [Replay Sharing](https://developer.apple.com/documentation/replaykit\#Replay-Sharing)

[Recording and Streaming Your macOS App](https://developer.apple.com/documentation/replaykit/recording-and-streaming-your-macos-app)

Share screen recordings, or broadcast live audio and video of your app, by adding ReplayKit to your macOS apps and games.

[`class RPScreenRecorder`](https://developer.apple.com/documentation/replaykit/rpscreenrecorder)

The shared recorder object that provides the ability to record audio and video of your app.

Deprecated

[`class RPPreviewViewController`](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller)

An object that displays a user interface where users preview and edit a screen recording that you create with ReplayKit.

Deprecated

### [Media Clip Processing](https://developer.apple.com/documentation/replaykit\#Media-Clip-Processing)

[`class RPBroadcastController`](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller)

An object containing methods for starting and controlling a broadcast.

Deprecated

[`class RPBroadcastHandler`](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler)

An object that sends messages to the broadcasting app.

Deprecated

[`class RPBroadcastSampleHandler`](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler)

An object that processes buffer objects as received from ReplayKit.

Deprecated

[`class RPBroadcastMP4ClipHandler`](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler)

An object that processes MP4 movie clips from ReplayKit.

Deprecated

### [Live Broadcast Implementation](https://developer.apple.com/documentation/replaykit\#Live-Broadcast-Implementation)

[`class RPBroadcastActivityViewController`](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller)

A view controller that displays a user interface where users choose a broadcast service.

Deprecated

[`class RPSystemBroadcastPickerView`](https://developer.apple.com/documentation/replaykit/rpsystembroadcastpickerview)

A view displaying a broadcast button that, when tapped, shows a broadcast picker.

Deprecated

[`class RPBroadcastActivityController`](https://developer.apple.com/documentation/replaykit/rpbroadcastactivitycontroller)

A controller object that presents the macOS broadcast picker.

Deprecated

[`protocol RPBroadcastActivityControllerDelegate`](https://developer.apple.com/documentation/replaykit/rpbroadcastactivitycontrollerdelegate)

A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.

Deprecated

[`class RPBroadcastConfiguration`](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration)

An object used to configure the movie clips produced during a live broadcast.

Deprecated

### [Errors](https://developer.apple.com/documentation/replaykit\#Errors)

[`enum RPRecordingErrorCode`](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode)

The ReplayKit error domain codes.

Deprecated

[`let RPRecordingErrorDomain: String`](https://developer.apple.com/documentation/replaykit/rprecordingerrordomain)

The ReplayKit error domain.

Deprecated

[`let SCStreamErrorDomain: String`](https://developer.apple.com/documentation/replaykit/scstreamerrordomain)

Current page is ReplayKit