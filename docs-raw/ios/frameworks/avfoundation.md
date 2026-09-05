* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/avfoundation#app-main)

Framework

# AVFoundation

Work with audiovisual assets, control device cameras, process audio, and configure system audio interactions.

iOS 2.2+iPadOS 13.1+Mac Catalyst 13.1+macOS 10.7+tvOS 9.0+visionOS 1.0+watchOS 3.0+

## [Overview](https://developer.apple.com/documentation/avfoundation\#overview)

AVFoundation combines several major technology areas that together encompass a wide range of tasks for inspecting, playing, capturing, and processing audiovisual media on Apple platforms.

## [Topics](https://developer.apple.com/documentation/avfoundation\#topics)

### [Essentials](https://developer.apple.com/documentation/avfoundation\#Essentials)

[AVFoundation updates](https://developer.apple.com/documentation/updates/avfoundation)

Learn about important changes to AVFoundation.

### [Common](https://developer.apple.com/documentation/avfoundation\#Common)

[API Reference\\
Media assets](https://developer.apple.com/documentation/avfoundation/media-assets)

Load media assets from files and streams to inspect their attributes, tracks, and embedded metadata.

[API Reference\\
Media reading and writing](https://developer.apple.com/documentation/avfoundation/media-reading-and-writing)

Read images from video, export to alternative formats, and perform sample-level reading and writing of media data.

[API Reference\\
Media types and utilities](https://developer.apple.com/documentation/avfoundation/media-types-and-utilities)

Identify the types of content and file formats that AVFoundation supports.

[API Reference\\
Video settings](https://developer.apple.com/documentation/avfoundation/video-settings)

Configure video processing settings using standard key and value constants.

[API Reference\\
Audio settings](https://developer.apple.com/documentation/avfoundation/audio-settings)

Configure audio processing settings using standard key and value constants.

### [Playback](https://developer.apple.com/documentation/avfoundation\#Playback)

[API Reference\\
Media playback](https://developer.apple.com/documentation/avfoundation/media-playback)

Manage the playback of media assets and interstitial content, independent of how you present that content in your interface.

[API Reference\\
Offline playback and storage](https://developer.apple.com/documentation/avfoundation/offline-playback-and-storage)

Download streamed content to disk to allow offline playback, and define policies to automatically remove downloaded assets.

[API Reference\\
Streaming and AirPlay](https://developer.apple.com/documentation/avfoundation/streaming-and-airplay)

Stream content wirelessly to other devices using AirPlay, and handle requests involving FairPlay-protected assets.

[API Reference\\
Sample buffer playback](https://developer.apple.com/documentation/avfoundation/sample-buffer-playback)

Create custom controllers to play and synchronize the timing of sample buffer streams.

### [Capture](https://developer.apple.com/documentation/avfoundation\#Capture)

[API Reference\\
Capture setup](https://developer.apple.com/documentation/avfoundation/capture-setup)

Configure built-in cameras and microphones, and external capture devices, for media capture.

[API Reference\\
Photo capture](https://developer.apple.com/documentation/avfoundation/photo-capture)

Capture high-quality still images, Live Photos, and supporting photo data.

[API Reference\\
Audio and video capture](https://developer.apple.com/documentation/avfoundation/audio-and-video-capture)

Capture audio and video directly to media files, or capture streams of media for direct access to media sample buffers.

[API Reference\\
Additional data capture](https://developer.apple.com/documentation/avfoundation/additional-data-capture)

Capture additional data including depth and metadata, and synchronize capture from multiple outputs.

### [Editing](https://developer.apple.com/documentation/avfoundation\#Editing)

[API Reference\\
Composite assets](https://developer.apple.com/documentation/avfoundation/composite-assets)

Combine tracks and segments of tracks from multiple assets into a composite asset that you can play or process.

[API Reference\\
QuickTime movies](https://developer.apple.com/documentation/avfoundation/quicktime-movies)

Access the contents of a QuickTime movie file, and perform sample-level edits of its media tracks.

[API Reference\\
Video effects](https://developer.apple.com/documentation/avfoundation/video-effects)

Define standard video transition effects, synchronize layer animations with media timing, and create custom video compositors.

[API Reference\\
Audio mixing](https://developer.apple.com/documentation/avfoundation/audio-mixing)

Define how to mix the audio levels from multiple audio tracks over an asset’s duration.

### [Audio](https://developer.apple.com/documentation/avfoundation\#Audio)

[API Reference\\
Audio playback, recording, and processing](https://developer.apple.com/documentation/avfoundation/audio-playback-recording-and-processing)

Play, record, and process audio; configure your app’s system audio behavior.

[API Reference\\
Speech synthesis](https://developer.apple.com/documentation/avfoundation/speech-synthesis)

Configure voices to speak strings of text.

### [Errors](https://developer.apple.com/documentation/avfoundation\#Errors)

[`let AVFoundationErrorDomain: String`](https://developer.apple.com/documentation/avfoundation/avfoundationerrordomain)

The error domain of AVFoundation errors.

[`struct AVError`](https://developer.apple.com/documentation/avfoundation/averror-swift.struct)

A structure that defines the errors that framework operations can generate.

### [Macros](https://developer.apple.com/documentation/avfoundation\#Macros)

[API Reference\\
Macros](https://developer.apple.com/documentation/avfoundation/avfoundation-macros)

Current page is AVFoundation