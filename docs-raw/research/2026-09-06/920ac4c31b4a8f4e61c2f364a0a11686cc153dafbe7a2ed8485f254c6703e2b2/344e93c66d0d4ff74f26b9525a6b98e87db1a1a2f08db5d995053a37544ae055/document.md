# android.media

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# android.media

---

[Kotlin](https://developer.android.com/reference/kotlin/android/media/package-summary "View this page in Kotlin")
|Java

Provides classes that manage various media interfaces in audio and video.

The Media APIs are used to play and, in some cases, record media files. This includes
audio (e.g., play MP3s or other music files, ringtones, game sound effects, or DTMF tones)
and video (e.g., play a video streamed over the web or from local storage).

Other special classes in the package offer the ability to detect the faces of people
in Bitmaps (`FaceDetector`), control audio routing (to the device or a headset)
and control alerts such as ringtones and phone vibrations (`AudioManager`).

## Interfaces

|  |  |
| --- | --- |
| [AudioManager.OnAudioFocusChangeListener](https://developer.android.com/reference/android/media/AudioManager.OnAudioFocusChangeListener) | Interface definition for a callback to be invoked when the audio focus of the system is updated. |
| [AudioManager.OnCommunicationDeviceChangedListener](https://developer.android.com/reference/android/media/AudioManager.OnCommunicationDeviceChangedListener) | Listener registered by client to be notified upon communication audio device change. |
| [AudioManager.OnModeChangedListener](https://developer.android.com/reference/android/media/AudioManager.OnModeChangedListener) | Interface definition of a callback that is notified when the audio mode changes |
| [AudioManager.OnPreferredMixerAttributesChangedListener](https://developer.android.com/reference/android/media/AudioManager.OnPreferredMixerAttributesChangedListener) | Interface to be notified of changes in the preferred mixer attributes. |
| [AudioMetadata.Key](https://developer.android.com/reference/android/media/AudioMetadata.Key)<T> | Key interface for the `AudioMetadata` map. |
| [AudioMetadataMap](https://developer.android.com/reference/android/media/AudioMetadataMap) | AudioMetadataMap is a writeable `Map`-style interface of `AudioMetadata.Key` value pairs. |
| [AudioMetadataReadMap](https://developer.android.com/reference/android/media/AudioMetadataReadMap) | A read only `Map`-style interface of `AudioMetadata.Key` value pairs used for `AudioMetadata`. |
| [AudioRecord.OnRecordPositionUpdateListener](https://developer.android.com/reference/android/media/AudioRecord.OnRecordPositionUpdateListener) | Interface definition for a callback to be invoked when an AudioRecord has reached a notification marker set by `AudioRecord.setNotificationMarkerPosition(int)` or for periodic updates on the progress of the record head, as set by `AudioRecord.setPositionNotificationPeriod(int)`. |
| [AudioRecord.OnRoutingChangedListener](https://developer.android.com/reference/android/media/AudioRecord.OnRoutingChangedListener) | *This interface was deprecated in API level 24. users should switch to the general purpose `AudioRouting.OnRoutingChangedListener` class instead.* |
| [AudioRecordingMonitor](https://developer.android.com/reference/android/media/AudioRecordingMonitor) | AudioRecordingMonitor defines an interface implemented by `AudioRecord` and `MediaRecorder` allowing applications to install a callback and be notified of changes in the capture path while recoding is active. |
| [AudioRouting](https://developer.android.com/reference/android/media/AudioRouting) | AudioRouting defines an interface for controlling routing and routing notifications in AudioTrack and AudioRecord objects. |
| [AudioRouting.OnRoutingChangedListener](https://developer.android.com/reference/android/media/AudioRouting.OnRoutingChangedListener) | Defines the interface by which applications can receive notifications of routing changes for the associated `AudioRouting`. |
| [AudioTrack.OnCodecFormatChangedListener](https://developer.android.com/reference/android/media/AudioTrack.OnCodecFormatChangedListener) | Interface definition for a listener for codec format changes. |
| [AudioTrack.OnPlaybackPositionUpdateListener](https://developer.android.com/reference/android/media/AudioTrack.OnPlaybackPositionUpdateListener) | Interface definition for a callback to be invoked when the playback head position of an AudioTrack has reached a notification marker or has increased by a certain period. |
| [AudioTrack.OnRoutingChangedListener](https://developer.android.com/reference/android/media/AudioTrack.OnRoutingChangedListener) | *This interface was deprecated in API level 24. users should switch to the general purpose `AudioRouting.OnRoutingChangedListener` class instead.* |
| [ImageReader.OnImageAvailableListener](https://developer.android.com/reference/android/media/ImageReader.OnImageAvailableListener) | Callback interface for being notified that a new image is available. |
| [ImageWriter.OnImageReleasedListener](https://developer.android.com/reference/android/media/ImageWriter.OnImageReleasedListener) | ImageWriter callback interface, used to to asynchronously notify the application of various ImageWriter events. |
| [JetPlayer.OnJetEventListener](https://developer.android.com/reference/android/media/JetPlayer.OnJetEventListener) | Handles the notification when the JET engine generates an event. |
| [LoudnessCodecController.OnLoudnessCodecUpdateListener](https://developer.android.com/reference/android/media/LoudnessCodecController.OnLoudnessCodecUpdateListener) | Listener used for receiving asynchronous loudness metadata updates. |
| [MediaCas.EventListener](https://developer.android.com/reference/android/media/MediaCas.EventListener) | An interface registered by the caller to `MediaCas.setEventListener(EventListener, Handler)` to receives scheme-specific notifications from a MediaCas instance. |
| [MediaCodec.OnFirstTunnelFrameReadyListener](https://developer.android.com/reference/android/media/MediaCodec.OnFirstTunnelFrameReadyListener) | Listener to be called when the first output frame has been decoded and is ready to be rendered for a codec configured for tunnel mode with `KEY_AUDIO_SESSION_ID`. |
| [MediaCodec.OnFrameRenderedListener](https://developer.android.com/reference/android/media/MediaCodec.OnFrameRenderedListener) | Listener to be called when an output frame has rendered on the output surface |
| [MediaDrm.OnEventListener](https://developer.android.com/reference/android/media/MediaDrm.OnEventListener) | Interface definition for a callback to be invoked when a drm event occurs |
| [MediaDrm.OnExpirationUpdateListener](https://developer.android.com/reference/android/media/MediaDrm.OnExpirationUpdateListener) | Interface definition for a callback to be invoked when a drm session expiration update occurs |
| [MediaDrm.OnKeyStatusChangeListener](https://developer.android.com/reference/android/media/MediaDrm.OnKeyStatusChangeListener) | Interface definition for a callback to be invoked when the keys in a drm session change states. |
| [MediaDrm.OnSessionLostStateListener](https://developer.android.com/reference/android/media/MediaDrm.OnSessionLostStateListener) | Interface definition for a callback to be invoked when the session state has been lost and is now invalid |
| [MediaDrmThrowable](https://developer.android.com/reference/android/media/MediaDrmThrowable) | A @`Throwable` thrown from `MediaDrm` or @`MediaCrypto` APIs |
| [MediaParser.InputReader](https://developer.android.com/reference/android/media/MediaParser.InputReader) | Provides input data to `MediaParser`. |
| [MediaParser.OutputConsumer](https://developer.android.com/reference/android/media/MediaParser.OutputConsumer) | Receives extracted media sample data and metadata from `MediaParser`. |
| [MediaParser.SeekableInputReader](https://developer.android.com/reference/android/media/MediaParser.SeekableInputReader) | `InputReader` that allows setting the read position. |
| [MediaPlayer.OnBufferingUpdateListener](https://developer.android.com/reference/android/media/MediaPlayer.OnBufferingUpdateListener) | Interface definition of a callback to be invoked indicating buffering status of a media resource being streamed over the network. |
| [MediaPlayer.OnCompletionListener](https://developer.android.com/reference/android/media/MediaPlayer.OnCompletionListener) | Interface definition for a callback to be invoked when playback of a media source has completed. |
| [MediaPlayer.OnDrmConfigHelper](https://developer.android.com/reference/android/media/MediaPlayer.OnDrmConfigHelper) | Interface definition of a callback to be invoked when the app can do DRM configuration (get/set properties) before the session is opened. |
| [MediaPlayer.OnDrmInfoListener](https://developer.android.com/reference/android/media/MediaPlayer.OnDrmInfoListener) | Interface definition of a callback to be invoked when the DRM info becomes available |
| [MediaPlayer.OnDrmPreparedListener](https://developer.android.com/reference/android/media/MediaPlayer.OnDrmPreparedListener) | Interface definition of a callback to notify the app when the DRM is ready for key request/response |
| [MediaPlayer.OnErrorListener](https://developer.android.com/reference/android/media/MediaPlayer.OnErrorListener) | Interface definition of a callback to be invoked when there has been an error during an asynchronous operation (other errors will throw exceptions at method call time). |
| [MediaPlayer.OnInfoListener](https://developer.android.com/reference/android/media/MediaPlayer.OnInfoListener) | Interface definition of a callback to be invoked to communicate some info and/or warning about the media or its playback. |
| [MediaPlayer.OnMediaTimeDiscontinuityListener](https://developer.android.com/reference/android/media/MediaPlayer.OnMediaTimeDiscontinuityListener) | Interface definition of a callback to be invoked when discontinuity in the normal progression of the media time is detected. |
| [MediaPlayer.OnPreparedListener](https://developer.android.com/reference/android/media/MediaPlayer.OnPreparedListener) | Interface definition for a callback to be invoked when the media source is ready for playback. |
| [MediaPlayer.OnSeekCompleteListener](https://developer.android.com/reference/android/media/MediaPlayer.OnSeekCompleteListener) | Interface definition of a callback to be invoked indicating the completion of a seek operation. |
| [MediaPlayer.OnSubtitleDataListener](https://developer.android.com/reference/android/media/MediaPlayer.OnSubtitleDataListener) | Interface definition of a callback to be invoked when a player subtitle track has new subtitle data available. |
| [MediaPlayer.OnTimedMetaDataAvailableListener](https://developer.android.com/reference/android/media/MediaPlayer.OnTimedMetaDataAvailableListener) | Interface definition of a callback to be invoked when a track has timed metadata available. |
| [MediaPlayer.OnTimedTextListener](https://developer.android.com/reference/android/media/MediaPlayer.OnTimedTextListener) | Interface definition of a callback to be invoked when a timed text is available for display. |
| [MediaPlayer.OnVideoSizeChangedListener](https://developer.android.com/reference/android/media/MediaPlayer.OnVideoSizeChangedListener) | Interface definition of a callback to be invoked when the video size is first known or updated |
| [MediaRecorder.OnErrorListener](https://developer.android.com/reference/android/media/MediaRecorder.OnErrorListener) | Interface definition for a callback to be invoked when an error occurs while recording. |
| [MediaRecorder.OnInfoListener](https://developer.android.com/reference/android/media/MediaRecorder.OnInfoListener) | Interface definition of a callback to be invoked to communicate some info and/or warning about the recording. |
| [MediaRouter2.DeviceSuggestionsUpdatesCallback](https://developer.android.com/reference/android/media/MediaRouter2.DeviceSuggestionsUpdatesCallback) | Callback for receiving events about device suggestions |
| [MediaRouter2.OnGetControllerHintsListener](https://developer.android.com/reference/android/media/MediaRouter2.OnGetControllerHintsListener) | A listener interface to send optional app-specific hints when creating a `RoutingController`. |
| [MediaScannerConnection.MediaScannerConnectionClient](https://developer.android.com/reference/android/media/MediaScannerConnection.MediaScannerConnectionClient) | An interface for notifying clients of MediaScannerConnection when a connection to the MediaScanner service has been established and when the scanning of a file has completed. |
| [MediaScannerConnection.OnScanCompletedListener](https://developer.android.com/reference/android/media/MediaScannerConnection.OnScanCompletedListener) | Interface for notifying clients of the result of scanning a requested media file. |
| [MediaSync.OnErrorListener](https://developer.android.com/reference/android/media/MediaSync.OnErrorListener) | Interface definition of a callback to be invoked when there has been an error during an asynchronous operation (other errors will throw exceptions at method call time). |
| [MicrophoneDirection](https://developer.android.com/reference/android/media/MicrophoneDirection) | Interface defining mechanism for controlling the directionality and field width of audio capture. |
| [RemoteControlClient.OnGetPlaybackPositionListener](https://developer.android.com/reference/android/media/RemoteControlClient.OnGetPlaybackPositionListener) | Interface definition for a callback to be invoked when the media playback position is queried. |
| [RemoteControlClient.OnMetadataUpdateListener](https://developer.android.com/reference/android/media/RemoteControlClient.OnMetadataUpdateListener) | Interface definition for a callback to be invoked when one of the metadata values has been updated. |
| [RemoteControlClient.OnPlaybackPositionUpdateListener](https://developer.android.com/reference/android/media/RemoteControlClient.OnPlaybackPositionUpdateListener) | Interface definition for a callback to be invoked when the media playback position is requested to be updated. |
| [RemoteController.OnClientUpdateListener](https://developer.android.com/reference/android/media/RemoteController.OnClientUpdateListener) | Interface definition for the callbacks to be invoked whenever media events, metadata and playback status are available. |
| [SoundPool.OnLoadCompleteListener](https://developer.android.com/reference/android/media/SoundPool.OnLoadCompleteListener) |  |
| [Spatializer.OnHeadTrackerAvailableListener](https://developer.android.com/reference/android/media/Spatializer.OnHeadTrackerAvailableListener) | Interface to be notified of changes to the availability of a head tracker on the audio device to be used by the spatializer effect. |
| [Spatializer.OnSpatializerStateChangedListener](https://developer.android.com/reference/android/media/Spatializer.OnSpatializerStateChangedListener) | An interface to be notified of changes to the state of the spatializer effect. |
| [VolumeAutomation](https://developer.android.com/reference/android/media/VolumeAutomation) | `VolumeAutomation` defines an interface for automatic volume control of `AudioTrack` and `MediaPlayer` objects. |

## Classes

|  |  |
| --- | --- |
| [ApplicationMediaCapabilities](https://developer.android.com/reference/android/media/ApplicationMediaCapabilities) | ApplicationMediaCapabilities is an immutable class that encapsulates an application's capabilities for handling newer video codec format and media features. |
| [ApplicationMediaCapabilities.Builder](https://developer.android.com/reference/android/media/ApplicationMediaCapabilities.Builder) | Builder class for `ApplicationMediaCapabilities` objects. |
| [AsyncPlayer](https://developer.android.com/reference/android/media/AsyncPlayer) | Plays a series of audio URIs, but does all the hard work on another thread so that any slowness with preparing or loading doesn't block the calling thread. |
| [AudioAttributes](https://developer.android.com/reference/android/media/AudioAttributes) | A class to encapsulate a collection of attributes describing information about an audio stream. |
| [AudioAttributes.Builder](https://developer.android.com/reference/android/media/AudioAttributes.Builder) | Builder class for `AudioAttributes` objects. |
| [AudioDescriptor](https://developer.android.com/reference/android/media/AudioDescriptor) | The AudioDescriptor contains the information to describe the audio playback/capture capabilities. |
| [AudioDeviceCallback](https://developer.android.com/reference/android/media/AudioDeviceCallback) | AudioDeviceCallback defines the mechanism by which applications can receive notifications of audio device connection and disconnection events. |
| [AudioDeviceInfo](https://developer.android.com/reference/android/media/AudioDeviceInfo) | Provides information about an audio device. |
| [AudioFocusRequest](https://developer.android.com/reference/android/media/AudioFocusRequest) | A class to encapsulate information about an audio focus request. |
| [AudioFocusRequest.Builder](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder) | Builder class for `AudioFocusRequest` objects. |
| [AudioFormat](https://developer.android.com/reference/android/media/AudioFormat) | The `AudioFormat` class is used to access a number of audio format and channel configuration constants. |
| [AudioFormat.Builder](https://developer.android.com/reference/android/media/AudioFormat.Builder) | Builder class for `AudioFormat` objects. |
| [AudioManager](https://developer.android.com/reference/android/media/AudioManager) | AudioManager provides access to volume and ringer mode control. |
| [AudioManager.AudioPlaybackCallback](https://developer.android.com/reference/android/media/AudioManager.AudioPlaybackCallback) | Interface for receiving update notifications about the playback activity on the system. |
| [AudioManager.AudioRecordingCallback](https://developer.android.com/reference/android/media/AudioManager.AudioRecordingCallback) | Interface for receiving update notifications about the recording configuration. |
| [AudioMetadata](https://developer.android.com/reference/android/media/AudioMetadata) | AudioMetadata class is used to manage typed key-value pairs for configuration and capability requests within the Audio Framework. |
| [AudioMetadata.Format](https://developer.android.com/reference/android/media/AudioMetadata.Format) | A container class for AudioMetadata Format keys. |
| [AudioMixerAttributes](https://developer.android.com/reference/android/media/AudioMixerAttributes) | Class to represent the attributes of the audio mixer: its format, which represents by an `AudioFormat` object and mixer behavior. |
| [AudioMixerAttributes.Builder](https://developer.android.com/reference/android/media/AudioMixerAttributes.Builder) | Builder class for `AudioMixerAttributes` objects. |
| [AudioPlaybackCaptureConfiguration](https://developer.android.com/reference/android/media/AudioPlaybackCaptureConfiguration) | Configuration for capturing audio played by other apps. |
| [AudioPlaybackCaptureConfiguration.Builder](https://developer.android.com/reference/android/media/AudioPlaybackCaptureConfiguration.Builder) | Builder for creating `AudioPlaybackCaptureConfiguration` instances. |
| [AudioPlaybackConfiguration](https://developer.android.com/reference/android/media/AudioPlaybackConfiguration) | The AudioPlaybackConfiguration class collects the information describing an audio playback session. |
| [AudioPresentation](https://developer.android.com/reference/android/media/AudioPresentation) | The AudioPresentation class encapsulates the information that describes an audio presentation which is available in next generation audio content. |
| [AudioPresentation.Builder](https://developer.android.com/reference/android/media/AudioPresentation.Builder) | A builder class for creating `AudioPresentation` objects. |
| [AudioProfile](https://developer.android.com/reference/android/media/AudioProfile) | An AudioProfile is specific to an audio format and lists supported sampling rates and channel masks for that format. |
| [AudioRecord](https://developer.android.com/reference/android/media/AudioRecord) | The AudioRecord class manages the audio resources for Java applications to record audio from the audio input hardware of the platform. |
| [AudioRecord.Builder](https://developer.android.com/reference/android/media/AudioRecord.Builder) | Builder class for `AudioRecord` objects. |
| [AudioRecord.MetricsConstants](https://developer.android.com/reference/android/media/AudioRecord.MetricsConstants) |  |
| [AudioRecordingConfiguration](https://developer.android.com/reference/android/media/AudioRecordingConfiguration) | The AudioRecordingConfiguration class collects the information describing an audio recording session. |
| [AudioTimestamp](https://developer.android.com/reference/android/media/AudioTimestamp) | Structure that groups a position in frame units relative to an assumed audio stream, together with the estimated time when that frame enters or leaves the audio processing pipeline on that device. |
| [AudioTrack](https://developer.android.com/reference/android/media/AudioTrack) | The AudioTrack class manages and plays a single audio resource for Java applications. |
| [AudioTrack.Builder](https://developer.android.com/reference/android/media/AudioTrack.Builder) | Builder class for `AudioTrack` objects. |
| [AudioTrack.MetricsConstants](https://developer.android.com/reference/android/media/AudioTrack.MetricsConstants) |  |
| [AudioTrack.StreamEventCallback](https://developer.android.com/reference/android/media/AudioTrack.StreamEventCallback) | Abstract class to receive event notifications about the stream playback in offloaded mode. |
| [CamcorderProfile](https://developer.android.com/reference/android/media/CamcorderProfile) | Retrieves the predefined camcorder profile settings for camcorder applications. |
| [CameraProfile](https://developer.android.com/reference/android/media/CameraProfile) | The CameraProfile class is used to retrieve the pre-defined still image capture (jpeg) quality levels (0-100) used for low, medium, and high quality settings in the Camera application. |
| [DrmInitData](https://developer.android.com/reference/android/media/DrmInitData) | Encapsulates initialization data required by a `MediaDrm` instance. |
| [DrmInitData.SchemeInitData](https://developer.android.com/reference/android/media/DrmInitData.SchemeInitData) | Scheme initialization data. |
| [EncoderProfiles](https://developer.android.com/reference/android/media/EncoderProfiles) | Describes a set of encoding profiles for a given media (audio and/or video) profile. |
| [EncoderProfiles.AudioProfile](https://developer.android.com/reference/android/media/EncoderProfiles.AudioProfile) | Configuration for an audio encoder. |
| [EncoderProfiles.VideoProfile](https://developer.android.com/reference/android/media/EncoderProfiles.VideoProfile) | Configuration for a video encoder. |
| [ExifInterface](https://developer.android.com/reference/android/media/ExifInterface) | This is a class for reading and writing Exif tags in various image file formats. |
| [FaceDetector](https://developer.android.com/reference/android/media/FaceDetector) | Identifies the faces of people in a `Bitmap` graphic object. |
| [FaceDetector.Face](https://developer.android.com/reference/android/media/FaceDetector.Face) | A Face contains all the information identifying the location of a face in a bitmap. |
| [Image](https://developer.android.com/reference/android/media/Image) | A single complete image buffer to use with a media source such as a `MediaCodec` or a `CameraDevice`. |
| [Image.Plane](https://developer.android.com/reference/android/media/Image.Plane) | A single color plane of image data. |
| [ImageReader](https://developer.android.com/reference/android/media/ImageReader) | The ImageReader class allows direct application access to image data rendered into a `Surface`  Several Android media API classes accept Surface objects as targets to render to, including `MediaPlayer`, `MediaCodec`, `CameraDevice`, `ImageWriter` and `RenderScript Allocations`. |
| [ImageReader.Builder](https://developer.android.com/reference/android/media/ImageReader.Builder) | Builder class for `ImageReader` objects. |
| [ImageWriter](https://developer.android.com/reference/android/media/ImageWriter) | The ImageWriter class allows an application to produce Image data into a `Surface`, and have it be consumed by another component like `CameraDevice`. |
| [ImageWriter.Builder](https://developer.android.com/reference/android/media/ImageWriter.Builder) | Builder class for `ImageWriter` objects. |
| [JetPlayer](https://developer.android.com/reference/android/media/JetPlayer) | JetPlayer provides access to JET content playback and control. |
| [LoudnessCodecController](https://developer.android.com/reference/android/media/LoudnessCodecController) | Class for getting recommended loudness parameter updates for audio decoders as they are used to play back media content according to the encoded format and current audio routing. |
| [MediaActionSound](https://developer.android.com/reference/android/media/MediaActionSound) | A class for producing sounds that match those produced by various actions taken by the media and camera APIs. |
| [MediaCas](https://developer.android.com/reference/android/media/MediaCas) | MediaCas can be used to obtain keys for descrambling protected media streams, in conjunction with `MediaDescrambler`. |
| [MediaCas.PluginDescriptor](https://developer.android.com/reference/android/media/MediaCas.PluginDescriptor) | Describe a CAS plugin with its CA\_system\_ID and string name. |
| [MediaCas.Session](https://developer.android.com/reference/android/media/MediaCas.Session) | Class for an open session with the CA system. |
| [MediaCodec](https://developer.android.com/reference/android/media/MediaCodec) | MediaCodec class can be used to access low-level media codecs, i.e. |
| [MediaCodec.BufferInfo](https://developer.android.com/reference/android/media/MediaCodec.BufferInfo) | Per buffer metadata includes an offset and size specifying the range of valid data in the associated codec (output) buffer. |
| [MediaCodec.Callback](https://developer.android.com/reference/android/media/MediaCodec.Callback) | MediaCodec callback interface. |
| [MediaCodec.CryptoInfo](https://developer.android.com/reference/android/media/MediaCodec.CryptoInfo) | Metadata describing the structure of an encrypted input sample. |
| [MediaCodec.CryptoInfo.Pattern](https://developer.android.com/reference/android/media/MediaCodec.CryptoInfo.Pattern) | Metadata describing an encryption pattern for the protected bytes in a subsample. |
| [MediaCodec.LinearBlock](https://developer.android.com/reference/android/media/MediaCodec.LinearBlock) | Section of memory that represents a linear block. |
| [MediaCodec.MetricsConstants](https://developer.android.com/reference/android/media/MediaCodec.MetricsConstants) |  |
| [MediaCodec.OutputFrame](https://developer.android.com/reference/android/media/MediaCodec.OutputFrame) | A single output frame and its associated metadata. |
| [MediaCodec.ParameterDescriptor](https://developer.android.com/reference/android/media/MediaCodec.ParameterDescriptor) | Contains description of a parameter. |
| [MediaCodec.QueueRequest](https://developer.android.com/reference/android/media/MediaCodec.QueueRequest) | Builder-like class for queue requests. |
| [MediaCodecInfo](https://developer.android.com/reference/android/media/MediaCodecInfo) | Provides information about a given media codec available on the device. |
| [MediaCodecInfo.AudioCapabilities](https://developer.android.com/reference/android/media/MediaCodecInfo.AudioCapabilities) | A class that supports querying the audio capabilities of a codec. |
| [MediaCodecInfo.CodecCapabilities](https://developer.android.com/reference/android/media/MediaCodecInfo.CodecCapabilities) | Encapsulates the capabilities of a given codec component. |
| [MediaCodecInfo.CodecProfileLevel](https://developer.android.com/reference/android/media/MediaCodecInfo.CodecProfileLevel) | Encapsulates the profiles available for a codec component. |
| [MediaCodecInfo.EncoderCapabilities](https://developer.android.com/reference/android/media/MediaCodecInfo.EncoderCapabilities) | A class that supports querying the encoding capabilities of a codec. |
| [MediaCodecInfo.VideoCapabilities](https://developer.android.com/reference/android/media/MediaCodecInfo.VideoCapabilities) | A class that supports querying the video capabilities of a codec. |
| [MediaCodecInfo.VideoCapabilities.PerformancePoint](https://developer.android.com/reference/android/media/MediaCodecInfo.VideoCapabilities.PerformancePoint) | Video performance points are a set of standard performance points defined by number of pixels, pixel rate and frame rate. |
| [MediaCodecList](https://developer.android.com/reference/android/media/MediaCodecList) | Allows you to enumerate available codecs, each specified as a `MediaCodecInfo` object, find a codec supporting a given format and query the capabilities of a given codec. |
| [MediaCommunicationManager](https://developer.android.com/reference/android/media/MediaCommunicationManager) | *This class was deprecated in API level 37. Use `MediaSessionManager` instead.* |
| [MediaController2](https://developer.android.com/reference/android/media/MediaController2) | *This class was deprecated in API level 37. Use the Media3 support library's `androidx.media3.session.MediaController` instead.* |
| [MediaController2.Builder](https://developer.android.com/reference/android/media/MediaController2.Builder) | *This class was deprecated in API level 37. Use the Media3 support library's `androidx.media3.session.MediaController` instead.* |
| [MediaController2.ControllerCallback](https://developer.android.com/reference/android/media/MediaController2.ControllerCallback) | *This class was deprecated in API level 37. Use the Media3 support library's `androidx.media3.session.MediaController` instead.* |
| [MediaCrypto](https://developer.android.com/reference/android/media/MediaCrypto) | MediaCrypto class can be used in conjunction with `MediaCodec` to decode encrypted media data. |
| [MediaDataSource](https://developer.android.com/reference/android/media/MediaDataSource) | For supplying media data to the framework. |
| [MediaDescrambler](https://developer.android.com/reference/android/media/MediaDescrambler) | MediaDescrambler class can be used in conjunction with `MediaCodec` and `MediaExtractor` to decode media data scrambled by conditional access (CA) systems such as those in the ISO/IEC13818-1. |
| [MediaDescription](https://developer.android.com/reference/android/media/MediaDescription) | A simple set of metadata for a media item suitable for display. |
| [MediaDescription.Builder](https://developer.android.com/reference/android/media/MediaDescription.Builder) | Builder for `MediaDescription` objects. |
| [MediaDrm](https://developer.android.com/reference/android/media/MediaDrm) | MediaDrm can be used to obtain keys for decrypting protected media streams, in conjunction with `MediaCrypto`. |
| [MediaDrm.CryptoSession](https://developer.android.com/reference/android/media/MediaDrm.CryptoSession) | In addition to supporting decryption of DASH Common Encrypted Media, the MediaDrm APIs provide the ability to securely deliver session keys from an operator's session key server to a client device, based on the factory-installed root of trust, and then perform encrypt, decrypt, sign and verify operations with the session key on arbitrary user data. |
| [MediaDrm.ErrorCodes](https://developer.android.com/reference/android/media/MediaDrm.ErrorCodes) | Error codes that may be returned from `MediaDrmStateException.getErrorCode()` and `MediaCodec.CryptoException.getErrorCode()` The description of each error code includes steps that may be taken to resolve the error condition. |
| [MediaDrm.KeyRequest](https://developer.android.com/reference/android/media/MediaDrm.KeyRequest) | Contains the opaque data an app uses to request keys from a license server. |
| [MediaDrm.KeyStatus](https://developer.android.com/reference/android/media/MediaDrm.KeyStatus) | Defines the status of a key. |
| [MediaDrm.LogMessage](https://developer.android.com/reference/android/media/MediaDrm.LogMessage) | A `LogMessage` records an event in the `MediaDrm` framework or vendor plugin. |
| [MediaDrm.MetricsConstants](https://developer.android.com/reference/android/media/MediaDrm.MetricsConstants) | Definitions for the metrics that are reported via the `MediaDrm.getMetrics()` call. |
| [MediaDrm.PlaybackComponent](https://developer.android.com/reference/android/media/MediaDrm.PlaybackComponent) | This class contains the Drm session ID and log session ID |
| [MediaDrm.ProvisionRequest](https://developer.android.com/reference/android/media/MediaDrm.ProvisionRequest) | Contains the opaque data an app uses to request a certificate from a provisioning server |
| [MediaExtractor](https://developer.android.com/reference/android/media/MediaExtractor) | MediaExtractor facilitates extraction of demuxed, typically encoded, media data from a data source. |
| [MediaExtractor.CasInfo](https://developer.android.com/reference/android/media/MediaExtractor.CasInfo) | Describes the conditional access system used to scramble a track. |
| [MediaExtractor.MetricsConstants](https://developer.android.com/reference/android/media/MediaExtractor.MetricsConstants) |  |
| [MediaFeature](https://developer.android.com/reference/android/media/MediaFeature) | MediaFeature defines various media features, e.g. hdr type. |
| [MediaFeature.HdrType](https://developer.android.com/reference/android/media/MediaFeature.HdrType) | Defines the type of HDR (high dynamic range) video. |
| [MediaFormat](https://developer.android.com/reference/android/media/MediaFormat) | Encapsulates the information describing the format of media data, be it audio or video, as well as optional feature metadata. |
| [MediaFormat.QpOffsetRect](https://developer.android.com/reference/android/media/MediaFormat.QpOffsetRect) | QpOffsetRect constitutes the metadata required for encoding a region of interest in an image or a video frame. |
| [MediaMetadata](https://developer.android.com/reference/android/media/MediaMetadata) | Contains metadata about an item, such as the title, artist, etc. |
| [MediaMetadata.Builder](https://developer.android.com/reference/android/media/MediaMetadata.Builder) | Use to build MediaMetadata objects. |
| [MediaMetadataEditor](https://developer.android.com/reference/android/media/MediaMetadataEditor) | *This class was deprecated in API level 21. Use `MediaMetadata` instead together with `MediaSession`.* |
| [MediaMetadataRetriever](https://developer.android.com/reference/android/media/MediaMetadataRetriever) | MediaMetadataRetriever class provides a unified interface for retrieving frame and meta data from an input media file. |
| [MediaMetadataRetriever.BitmapParams](https://developer.android.com/reference/android/media/MediaMetadataRetriever.BitmapParams) |  |
| [MediaMuxer](https://developer.android.com/reference/android/media/MediaMuxer) | MediaMuxer facilitates muxing elementary streams. |
| [MediaMuxer.OutputFormat](https://developer.android.com/reference/android/media/MediaMuxer.OutputFormat) | Defines the output format. |
| [MediaParser](https://developer.android.com/reference/android/media/MediaParser) | Parses media container formats and extracts contained media samples and metadata. |
| [MediaParser.SeekMap](https://developer.android.com/reference/android/media/MediaParser.SeekMap) | Maps seek positions to `SeekPoints` in the stream. |
| [MediaParser.SeekPoint](https://developer.android.com/reference/android/media/MediaParser.SeekPoint) | Defines a seek point in a media stream. |
| [MediaParser.TrackData](https://developer.android.com/reference/android/media/MediaParser.TrackData) | Holds information associated with a track. |
| [MediaPlayer](https://developer.android.com/reference/android/media/MediaPlayer) | MediaPlayer class can be used to control playback of audio/video files and streams. |
| [MediaPlayer.DrmInfo](https://developer.android.com/reference/android/media/MediaPlayer.DrmInfo) | Encapsulates the DRM properties of the source. |
| [MediaPlayer.MetricsConstants](https://developer.android.com/reference/android/media/MediaPlayer.MetricsConstants) |  |
| [MediaPlayer.TrackInfo](https://developer.android.com/reference/android/media/MediaPlayer.TrackInfo) | Class for MediaPlayer to return each audio/video/subtitle track's metadata. |
| [MediaRecorder](https://developer.android.com/reference/android/media/MediaRecorder) | Used to record audio and video. |
| [MediaRecorder.AudioEncoder](https://developer.android.com/reference/android/media/MediaRecorder.AudioEncoder) | Defines the audio encoding. |
| [MediaRecorder.AudioSource](https://developer.android.com/reference/android/media/MediaRecorder.AudioSource) | Defines the audio source. |
| [MediaRecorder.MetricsConstants](https://developer.android.com/reference/android/media/MediaRecorder.MetricsConstants) |  |
| [MediaRecorder.OutputFormat](https://developer.android.com/reference/android/media/MediaRecorder.OutputFormat) | Defines the output format. |
| [MediaRecorder.VideoEncoder](https://developer.android.com/reference/android/media/MediaRecorder.VideoEncoder) | Defines the video encoding. |
| [MediaRecorder.VideoSource](https://developer.android.com/reference/android/media/MediaRecorder.VideoSource) | Defines the video source. |
| [MediaRoute2Info](https://developer.android.com/reference/android/media/MediaRoute2Info) | Describes the properties of a route. |
| [MediaRoute2Info.Builder](https://developer.android.com/reference/android/media/MediaRoute2Info.Builder) | Builder for `media route info`. |
| [MediaRoute2ProviderService](https://developer.android.com/reference/android/media/MediaRoute2ProviderService) | Base class for media route provider services. |
| [MediaRouter](https://developer.android.com/reference/android/media/MediaRouter) | This API is not recommended for new applications. |
| [MediaRouter.Callback](https://developer.android.com/reference/android/media/MediaRouter.Callback) | Interface for receiving events about media routing changes. |
| [MediaRouter.RouteCategory](https://developer.android.com/reference/android/media/MediaRouter.RouteCategory) | Definition of a category of routes. |
| [MediaRouter.RouteGroup](https://developer.android.com/reference/android/media/MediaRouter.RouteGroup) | Information about a route that consists of multiple other routes in a group. |
| [MediaRouter.RouteInfo](https://developer.android.com/reference/android/media/MediaRouter.RouteInfo) | Information about a media route. |
| [MediaRouter.SimpleCallback](https://developer.android.com/reference/android/media/MediaRouter.SimpleCallback) | Stub implementation of `MediaRouter.Callback`. |
| [MediaRouter.UserRouteInfo](https://developer.android.com/reference/android/media/MediaRouter.UserRouteInfo) | Information about a route that the application may define and modify. |
| [MediaRouter.VolumeCallback](https://developer.android.com/reference/android/media/MediaRouter.VolumeCallback) | Interface for receiving events about volume changes. |
| [MediaRouter2](https://developer.android.com/reference/android/media/MediaRouter2) | This API is not generally intended for third party application developers. |
| [MediaRouter2.ControllerCallback](https://developer.android.com/reference/android/media/MediaRouter2.ControllerCallback) | Callback for receiving `RoutingController` updates. |
| [MediaRouter2.RouteCallback](https://developer.android.com/reference/android/media/MediaRouter2.RouteCallback) | Callback for receiving events about media route discovery. |
| [MediaRouter2.RoutingController](https://developer.android.com/reference/android/media/MediaRouter2.RoutingController) | Controls a media routing session. |
| [MediaRouter2.ScanRequest](https://developer.android.com/reference/android/media/MediaRouter2.ScanRequest) | Represents a set of parameters for scanning requests. |
| [MediaRouter2.ScanRequest.Builder](https://developer.android.com/reference/android/media/MediaRouter2.ScanRequest.Builder) | Builder class for `ScanRequest`. |
| [MediaRouter2.ScanToken](https://developer.android.com/reference/android/media/MediaRouter2.ScanToken) | Represents an active scan request registered in the system. |
| [MediaRouter2.TransferCallback](https://developer.android.com/reference/android/media/MediaRouter2.TransferCallback) | Callback for receiving events on media transfer. |
| [MediaScannerConnection](https://developer.android.com/reference/android/media/MediaScannerConnection) | MediaScannerConnection provides a way for applications to pass a newly created or downloaded media file to the media scanner service. |
| [MediaSession2](https://developer.android.com/reference/android/media/MediaSession2) | *This class was deprecated in API level 37. Use the Media3 support library's `androidx.media3.session.MediaSession` instead.* |
| [MediaSession2.Builder](https://developer.android.com/reference/android/media/MediaSession2.Builder) | *This class was deprecated in API level 37. Use the Media3 support library's `androidx.media3.session.MediaSession` instead.* |
| [MediaSession2.ControllerInfo](https://developer.android.com/reference/android/media/MediaSession2.ControllerInfo) | *This class was deprecated in API level 37. Use the Media3 support library's `androidx.media3.session.MediaSession` instead.* |
| [MediaSession2.SessionCallback](https://developer.android.com/reference/android/media/MediaSession2.SessionCallback) | *This class was deprecated in API level 37. Use the Media3 support library's `androidx.media3.session.MediaSession` instead.* |
| [MediaSession2Service](https://developer.android.com/reference/android/media/MediaSession2Service) | *This class was deprecated in API level 37. Use the Media3 support library's `androidx.media3.session.MediaSessionService` instead.* |
| [MediaSession2Service.MediaNotification](https://developer.android.com/reference/android/media/MediaSession2Service.MediaNotification) | *This class was deprecated in API level 37. Use the Media3 support library's `androidx.media3.session.MediaSessionService` instead.* |
| [MediaSync](https://developer.android.com/reference/android/media/MediaSync) | MediaSync class can be used to synchronously play audio and video streams. |
| [MediaSync.Callback](https://developer.android.com/reference/android/media/MediaSync.Callback) | MediaSync callback interface. |
| [MediaSyncEvent](https://developer.android.com/reference/android/media/MediaSyncEvent) | The MediaSyncEvent class defines events that can be used to synchronize playback or capture actions between different players and recorders. |
| [MediaTimestamp](https://developer.android.com/reference/android/media/MediaTimestamp) | An immutable object that represents the linear correlation between the media time and the system time. |
| [MicrophoneInfo](https://developer.android.com/reference/android/media/MicrophoneInfo) | Class providing information on a microphone. |
| [MicrophoneInfo.Coordinate3F](https://developer.android.com/reference/android/media/MicrophoneInfo.Coordinate3F) |  |
| [PlaybackParams](https://developer.android.com/reference/android/media/PlaybackParams) | Structure for common playback params. |
| [Rating](https://developer.android.com/reference/android/media/Rating) | A class to encapsulate rating information used as content metadata. |
| [RemoteControlClient](https://developer.android.com/reference/android/media/RemoteControlClient) | *This class was deprecated in API level 21. Use `MediaSession` instead.* |
| [RemoteControlClient.MetadataEditor](https://developer.android.com/reference/android/media/RemoteControlClient.MetadataEditor) | *This class was deprecated in API level 21. Use `MediaMetadata` and `MediaSession` instead.* |
| [RemoteController](https://developer.android.com/reference/android/media/RemoteController) | *This class was deprecated in API level 21. Use `MediaController` instead.* |
| [RemoteController.MetadataEditor](https://developer.android.com/reference/android/media/RemoteController.MetadataEditor) | A class to read the metadata published by a `RemoteControlClient`, or send a `RemoteControlClient` new values for keys that can be edited. |
| [Ringtone](https://developer.android.com/reference/android/media/Ringtone) | Ringtone provides a quick method for playing a ringtone, notification, or other similar types of sounds. |
| [RingtoneManager](https://developer.android.com/reference/android/media/RingtoneManager) | RingtoneManager provides access to ringtones, notification, and other types of sounds. |
| [RouteDiscoveryPreference](https://developer.android.com/reference/android/media/RouteDiscoveryPreference) | A media route discovery preference describing the features of routes that media router would like to discover and whether to perform active scanning. |
| [RouteDiscoveryPreference.Builder](https://developer.android.com/reference/android/media/RouteDiscoveryPreference.Builder) | Builder for `RouteDiscoveryPreference`. |
| [RouteListingPreference](https://developer.android.com/reference/android/media/RouteListingPreference) | Allows applications to customize the list of routes used for media routing (for example, in the System UI Output Switcher). |
| [RouteListingPreference.Builder](https://developer.android.com/reference/android/media/RouteListingPreference.Builder) | Builder for `RouteListingPreference`. |
| [RouteListingPreference.Item](https://developer.android.com/reference/android/media/RouteListingPreference.Item) | Holds preference information for a specific route in a `RouteListingPreference`. |
| [RouteListingPreference.Item.Builder](https://developer.android.com/reference/android/media/RouteListingPreference.Item.Builder) | Builder for `Item`. |
| [RoutingSessionInfo](https://developer.android.com/reference/android/media/RoutingSessionInfo) | Describes a routing session which is created when a media route is selected. |
| [RoutingSessionInfo.Builder](https://developer.android.com/reference/android/media/RoutingSessionInfo.Builder) | Builder class for `RoutingSessionInfo`. |
| [Session2Command](https://developer.android.com/reference/android/media/Session2Command) | *This class was deprecated in API level 37. Use the Media3 support library instead.* |
| [Session2Command.Result](https://developer.android.com/reference/android/media/Session2Command.Result) | *This class was deprecated in API level 37. Use the Media3 support library instead.* |
| [Session2CommandGroup](https://developer.android.com/reference/android/media/Session2CommandGroup) | *This class was deprecated in API level 37. Use the Media3 support library instead.* |
| [Session2CommandGroup.Builder](https://developer.android.com/reference/android/media/Session2CommandGroup.Builder) | *This class was deprecated in API level 37. Use the Media3 support library instead.* |
| [Session2Token](https://developer.android.com/reference/android/media/Session2Token) | *This class was deprecated in API level 37. Use the Media3 support library instead.* |
| [SoundPool](https://developer.android.com/reference/android/media/SoundPool) | The SoundPool class manages and plays audio resources for applications. |
| [SoundPool.Builder](https://developer.android.com/reference/android/media/SoundPool.Builder) | Builder class for `SoundPool` objects. |
| [Spatializer](https://developer.android.com/reference/android/media/Spatializer) | Spatializer provides access to querying capabilities and behavior of sound spatialization on the device. |
| [SubtitleData](https://developer.android.com/reference/android/media/SubtitleData) | Class encapsulating subtitle data, as received through the `MediaPlayer.OnSubtitleDataListener` interface. |
| [SuggestedDeviceInfo](https://developer.android.com/reference/android/media/SuggestedDeviceInfo) | Allows applications to suggest routes to the system UI (for example, in the System UI Output Switcher). |
| [SuggestedDeviceInfo.Builder](https://developer.android.com/reference/android/media/SuggestedDeviceInfo.Builder) | Builder for `SuggestedDeviceInfo`. |
| [SyncParams](https://developer.android.com/reference/android/media/SyncParams) | Structure for common A/V sync params. |
| [ThumbnailUtils](https://developer.android.com/reference/android/media/ThumbnailUtils) | Utilities for generating visual thumbnails from files. |
| [TimedMetaData](https://developer.android.com/reference/android/media/TimedMetaData) | Class that embodies one timed metadata access unit, including  * a time stamp, and * raw uninterpreted byte-array extracted directly from the container. |
| [TimedText](https://developer.android.com/reference/android/media/TimedText) | Class to hold the timed text's metadata, including:  * The characters for rendering * The rendering position for the timed text   To render the timed text, applications need to do the following:   * Implement the `MediaPlayer.OnTimedTextListener` interface * Register the `MediaPlayer.OnTimedTextListener` callback on a MediaPlayer object that is used for playback * When a onTimedText callback is received, do the following:   + call `getText()` to get the characters for rendering   + call `getBounds()` to get the text rendering area/region |
| [ToneGenerator](https://developer.android.com/reference/android/media/ToneGenerator) | This class provides methods to play DTMF tones (ITU-T Recommendation Q.23), call supervisory tones (3GPP TS 22.001, CEPT) and proprietary tones (3GPP TS 31.111). |
| [VolumeProvider](https://developer.android.com/reference/android/media/VolumeProvider) | Handles requests to adjust or set the volume on a session. |
| [VolumeShaper](https://developer.android.com/reference/android/media/VolumeShaper) | The `VolumeShaper` class is used to automatically control audio volume during media playback, allowing simple implementation of transition effects and ducking. |
| [VolumeShaper.Configuration](https://developer.android.com/reference/android/media/VolumeShaper.Configuration) | The `VolumeShaper.Configuration` class contains curve and duration information. |
| [VolumeShaper.Configuration.Builder](https://developer.android.com/reference/android/media/VolumeShaper.Configuration.Builder) | Builder class for a `VolumeShaper.Configuration` object. |
| [VolumeShaper.Operation](https://developer.android.com/reference/android/media/VolumeShaper.Operation) | The `VolumeShaper.Operation` class is used to specify operations to the `VolumeShaper` that affect the volume change. |

## Exceptions

|  |  |
| --- | --- |
| [DeniedByServerException](https://developer.android.com/reference/android/media/DeniedByServerException) | Exception thrown when the provisioning server or key server denies a certficate or license for a device. |
| [MediaCasException](https://developer.android.com/reference/android/media/MediaCasException) | Base class for MediaCas exceptions |
| [MediaCasException.DeniedByServerException](https://developer.android.com/reference/android/media/MediaCasException.DeniedByServerException) | Exception thrown when the provisioning server or key server denies a license for a device. |
| [MediaCasException.InsufficientResourceException](https://developer.android.com/reference/android/media/MediaCasException.InsufficientResourceException) | Exception thrown when an operation on a MediaCas object is attempted and hardware resources are not sufficient to allocate, due to client's lower priority. |
| [MediaCasException.NotProvisionedException](https://developer.android.com/reference/android/media/MediaCasException.NotProvisionedException) | Exception thrown when an operation on a MediaCas object is attempted before it's provisioned successfully. |
| [MediaCasException.ResourceBusyException](https://developer.android.com/reference/android/media/MediaCasException.ResourceBusyException) | Exception thrown when an operation on a MediaCas object is attempted and hardware resources are not available, due to being in use. |
| [MediaCasException.UnsupportedCasException](https://developer.android.com/reference/android/media/MediaCasException.UnsupportedCasException) | Exception thrown when an attempt is made to construct a MediaCas object using a CA\_system\_id that is not supported by the device |
| [MediaCasStateException](https://developer.android.com/reference/android/media/MediaCasStateException) | Base class for MediaCas runtime exceptions |
| [MediaCodec.CodecException](https://developer.android.com/reference/android/media/MediaCodec.CodecException) | Thrown when an internal codec error occurs. |
| [MediaCodec.CryptoException](https://developer.android.com/reference/android/media/MediaCodec.CryptoException) | Thrown when a crypto error occurs while queueing a secure input buffer. |
| [MediaCodec.IncompatibleWithBlockModelException](https://developer.android.com/reference/android/media/MediaCodec.IncompatibleWithBlockModelException) | Thrown when the codec is configured for block model and an incompatible API is called. |
| [MediaCodec.InvalidBufferFlagsException](https://developer.android.com/reference/android/media/MediaCodec.InvalidBufferFlagsException) | Thrown when a buffer is marked with an invalid combination of flags (e.g. both `MediaCodec.BUFFER_FLAG_END_OF_STREAM` and `MediaCodec.BUFFER_FLAG_DECODE_ONLY`) |
| [MediaCryptoException](https://developer.android.com/reference/android/media/MediaCryptoException) | Exception thrown if MediaCrypto object could not be instantiated or if unable to perform an operation on the MediaCrypto object. |
| [MediaDrm.MediaDrmStateException](https://developer.android.com/reference/android/media/MediaDrm.MediaDrmStateException) | Thrown when a general failure occurs during a MediaDrm operation. |
| [MediaDrm.SessionException](https://developer.android.com/reference/android/media/MediaDrm.SessionException) | `SessionException` is a misnomer because it may occur in methods **without** a session context. |
| [MediaDrmException](https://developer.android.com/reference/android/media/MediaDrmException) | Base class for MediaDrm exceptions |
| [MediaDrmResetException](https://developer.android.com/reference/android/media/MediaDrmResetException) | This exception is thrown when the MediaDrm instance has become unusable due to a restart of the mediaserver process. |
| [MediaParser.ParsingException](https://developer.android.com/reference/android/media/MediaParser.ParsingException) | Thrown when an error occurs while parsing a media stream. |
| [MediaParser.UnrecognizedInputFormatException](https://developer.android.com/reference/android/media/MediaParser.UnrecognizedInputFormatException) | Thrown if all parser implementations provided to `MediaParser.create(OutputConsumer, String)` failed to sniff the input content. |
| [MediaPlayer.NoDrmSchemeException](https://developer.android.com/reference/android/media/MediaPlayer.NoDrmSchemeException) | Thrown when a DRM method is called before preparing a DRM scheme through prepareDrm(). |
| [MediaPlayer.ProvisioningNetworkErrorException](https://developer.android.com/reference/android/media/MediaPlayer.ProvisioningNetworkErrorException) | Thrown when the device requires DRM provisioning but the provisioning attempt has failed due to a network error (Internet reachability, timeout, etc.). |
| [MediaPlayer.ProvisioningServerErrorException](https://developer.android.com/reference/android/media/MediaPlayer.ProvisioningServerErrorException) | Thrown when the device requires DRM provisioning but the provisioning attempt has failed due to the provisioning server denying the request. |
| [NotProvisionedException](https://developer.android.com/reference/android/media/NotProvisionedException) | Exception thrown when an operation on a MediaDrm object is attempted and the device does not have a certificate. |
| [ResourceBusyException](https://developer.android.com/reference/android/media/ResourceBusyException) | Exception thrown when an operation on a MediaDrm object is attempted and hardware resources are not available, due to being in use. |
| [UnsupportedSchemeException](https://developer.android.com/reference/android/media/UnsupportedSchemeException) | Exception thrown when an attempt is made to construct a MediaDrm object using a crypto scheme UUID that is not supported by the device |

* ## Interfaces

  + [AudioManager.OnAudioFocusChangeListener](https://developer.android.com/reference/android/media/AudioManager.OnAudioFocusChangeListener)
  + [AudioManager.OnCommunicationDeviceChangedListener](https://developer.android.com/reference/android/media/AudioManager.OnCommunicationDeviceChangedListener)
  + [AudioManager.OnModeChangedListener](https://developer.android.com/reference/android/media/AudioManager.OnModeChangedListener)
  + [AudioManager.OnPreferredMixerAttributesChangedListener](https://developer.android.com/reference/android/media/AudioManager.OnPreferredMixerAttributesChangedListener)
  + [AudioMetadata.Key](https://developer.android.com/reference/android/media/AudioMetadata.Key)
  + [AudioMetadataMap](https://developer.android.com/reference/android/media/AudioMetadataMap)
  + [AudioMetadataReadMap](https://developer.android.com/reference/android/media/AudioMetadataReadMap)
  + [AudioRecord.OnRecordPositionUpdateListener](https://developer.android.com/reference/android/media/AudioRecord.OnRecordPositionUpdateListener)
  + [AudioRecord.OnRoutingChangedListener](https://developer.android.com/reference/android/media/AudioRecord.OnRoutingChangedListener)
  + [AudioRecordingMonitor](https://developer.android.com/reference/android/media/AudioRecordingMonitor)
  + [AudioRouting](https://developer.android.com/reference/android/media/AudioRouting)
  + [AudioRouting.OnRoutingChangedListener](https://developer.android.com/reference/android/media/AudioRouting.OnRoutingChangedListener)
  + [AudioTrack.OnCodecFormatChangedListener](https://developer.android.com/reference/android/media/AudioTrack.OnCodecFormatChangedListener)
  + [AudioTrack.OnPlaybackPositionUpdateListener](https://developer.android.com/reference/android/media/AudioTrack.OnPlaybackPositionUpdateListener)
  + [AudioTrack.OnRoutingChangedListener](https://developer.android.com/reference/android/media/AudioTrack.OnRoutingChangedListener)
  + [ImageReader.OnImageAvailableListener](https://developer.android.com/reference/android/media/ImageReader.OnImageAvailableListener)
  + [ImageWriter.OnImageReleasedListener](https://developer.android.com/reference/android/media/ImageWriter.OnImageReleasedListener)
  + [JetPlayer.OnJetEventListener](https://developer.android.com/reference/android/media/JetPlayer.OnJetEventListener)
  + [LoudnessCodecController.OnLoudnessCodecUpdateListener](https://developer.android.com/reference/android/media/LoudnessCodecController.OnLoudnessCodecUpdateListener)
  + [MediaCas.EventListener](https://developer.android.com/reference/android/media/MediaCas.EventListener)
  + [MediaCodec.OnFirstTunnelFrameReadyListener](https://developer.android.com/reference/android/media/MediaCodec.OnFirstTunnelFrameReadyListener)
  + [MediaCodec.OnFrameRenderedListener](https://developer.android.com/reference/android/media/MediaCodec.OnFrameRenderedListener)
  + [MediaDrm.OnEventListener](https://developer.android.com/reference/android/media/MediaDrm.OnEventListener)
  + [MediaDrm.OnExpirationUpdateListener](https://developer.android.com/reference/android/media/MediaDrm.OnExpirationUpdateListener)
  + [MediaDrm.OnKeyStatusChangeListener](https://developer.android.com/reference/android/media/MediaDrm.OnKeyStatusChangeListener)
  + [MediaDrm.OnSessionLostStateListener](https://developer.android.com/reference/android/media/MediaDrm.OnSessionLostStateListener)
  + [MediaDrmThrowable](https://developer.android.com/reference/android/media/MediaDrmThrowable)
  + [MediaParser.InputReader](https://developer.android.com/reference/android/media/MediaParser.InputReader)
  + [MediaParser.OutputConsumer](https://developer.android.com/reference/android/media/MediaParser.OutputConsumer)
  + [MediaParser.SeekableInputReader](https://developer.android.com/reference/android/media/MediaParser.SeekableInputReader)
  + [MediaPlayer.OnBufferingUpdateListener](https://developer.android.com/reference/android/media/MediaPlayer.OnBufferingUpdateListener)
  + [MediaPlayer.OnCompletionListener](https://developer.android.com/reference/android/media/MediaPlayer.OnCompletionListener)
  + [MediaPlayer.OnDrmConfigHelper](https://developer.android.com/reference/android/media/MediaPlayer.OnDrmConfigHelper)
  + [MediaPlayer.OnDrmInfoListener](https://developer.android.com/reference/android/media/MediaPlayer.OnDrmInfoListener)
  + [MediaPlayer.OnDrmPreparedListener](https://developer.android.com/reference/android/media/MediaPlayer.OnDrmPreparedListener)
  + [MediaPlayer.OnErrorListener](https://developer.android.com/reference/android/media/MediaPlayer.OnErrorListener)
  + [MediaPlayer.OnInfoListener](https://developer.android.com/reference/android/media/MediaPlayer.OnInfoListener)
  + [MediaPlayer.OnMediaTimeDiscontinuityListener](https://developer.android.com/reference/android/media/MediaPlayer.OnMediaTimeDiscontinuityListener)
  + [MediaPlayer.OnPreparedListener](https://developer.android.com/reference/android/media/MediaPlayer.OnPreparedListener)
  + [MediaPlayer.OnSeekCompleteListener](https://developer.android.com/reference/android/media/MediaPlayer.OnSeekCompleteListener)
  + [MediaPlayer.OnSubtitleDataListener](https://developer.android.com/reference/android/media/MediaPlayer.OnSubtitleDataListener)
  + [MediaPlayer.OnTimedMetaDataAvailableListener](https://developer.android.com/reference/android/media/MediaPlayer.OnTimedMetaDataAvailableListener)
  + [MediaPlayer.OnTimedTextListener](https://developer.android.com/reference/android/media/MediaPlayer.OnTimedTextListener)
  + [MediaPlayer.OnVideoSizeChangedListener](https://developer.android.com/reference/android/media/MediaPlayer.OnVideoSizeChangedListener)
  + [MediaRecorder.OnErrorListener](https://developer.android.com/reference/android/media/MediaRecorder.OnErrorListener)
  + [MediaRecorder.OnInfoListener](https://developer.android.com/reference/android/media/MediaRecorder.OnInfoListener)
  + [MediaRouter2.DeviceSuggestionsUpdatesCallback](https://developer.android.com/reference/android/media/MediaRouter2.DeviceSuggestionsUpdatesCallback)
  + [MediaRouter2.OnGetControllerHintsListener](https://developer.android.com/reference/android/media/MediaRouter2.OnGetControllerHintsListener)
  + [MediaScannerConnection.MediaScannerConnectionClient](https://developer.android.com/reference/android/media/MediaScannerConnection.MediaScannerConnectionClient)
  + [MediaScannerConnection.OnScanCompletedListener](https://developer.android.com/reference/android/media/MediaScannerConnection.OnScanCompletedListener)
  + [MediaSync.OnErrorListener](https://developer.android.com/reference/android/media/MediaSync.OnErrorListener)
  + [MicrophoneDirection](https://developer.android.com/reference/android/media/MicrophoneDirection)
  + [RemoteControlClient.OnGetPlaybackPositionListener](https://developer.android.com/reference/android/media/RemoteControlClient.OnGetPlaybackPositionListener)
  + [RemoteControlClient.OnMetadataUpdateListener](https://developer.android.com/reference/android/media/RemoteControlClient.OnMetadataUpdateListener)
  + [RemoteControlClient.OnPlaybackPositionUpdateListener](https://developer.android.com/reference/android/media/RemoteControlClient.OnPlaybackPositionUpdateListener)
  + [RemoteController.OnClientUpdateListener](https://developer.android.com/reference/android/media/RemoteController.OnClientUpdateListener)
  + [SoundPool.OnLoadCompleteListener](https://developer.android.com/reference/android/media/SoundPool.OnLoadCompleteListener)
  + [Spatializer.OnHeadTrackerAvailableListener](https://developer.android.com/reference/android/media/Spatializer.OnHeadTrackerAvailableListener)
  + [Spatializer.OnSpatializerStateChangedListener](https://developer.android.com/reference/android/media/Spatializer.OnSpatializerStateChangedListener)
  + [VolumeAutomation](https://developer.android.com/reference/android/media/VolumeAutomation)
* ## Classes

  + [ApplicationMediaCapabilities](https://developer.android.com/reference/android/media/ApplicationMediaCapabilities)
  + [ApplicationMediaCapabilities.Builder](https://developer.android.com/reference/android/media/ApplicationMediaCapabilities.Builder)
  + [AsyncPlayer](https://developer.android.com/reference/android/media/AsyncPlayer)
  + [AudioAttributes](https://developer.android.com/reference/android/media/AudioAttributes)
  + [AudioAttributes.Builder](https://developer.android.com/reference/android/media/AudioAttributes.Builder)
  + [AudioDescriptor](https://developer.android.com/reference/android/media/AudioDescriptor)
  + [AudioDeviceCallback](https://developer.android.com/reference/android/media/AudioDeviceCallback)
  + [AudioDeviceInfo](https://developer.android.com/reference/android/media/AudioDeviceInfo)
  + [AudioFocusRequest](https://developer.android.com/reference/android/media/AudioFocusRequest)
  + [AudioFocusRequest.Builder](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder)
  + [AudioFormat](https://developer.android.com/reference/android/media/AudioFormat)
  + [AudioFormat.Builder](https://developer.android.com/reference/android/media/AudioFormat.Builder)
  + [AudioManager](https://developer.android.com/reference/android/media/AudioManager)
  + [AudioManager.AudioPlaybackCallback](https://developer.android.com/reference/android/media/AudioManager.AudioPlaybackCallback)
  + [AudioManager.AudioRecordingCallback](https://developer.android.com/reference/android/media/AudioManager.AudioRecordingCallback)
  + [AudioMetadata](https://developer.android.com/reference/android/media/AudioMetadata)
  + [AudioMetadata.Format](https://developer.android.com/reference/android/media/AudioMetadata.Format)
  + [AudioMixerAttributes](https://developer.android.com/reference/android/media/AudioMixerAttributes)
  + [AudioMixerAttributes.Builder](https://developer.android.com/reference/android/media/AudioMixerAttributes.Builder)
  + [AudioPlaybackCaptureConfiguration](https://developer.android.com/reference/android/media/AudioPlaybackCaptureConfiguration)
  + [AudioPlaybackCaptureConfiguration.Builder](https://developer.android.com/reference/android/media/AudioPlaybackCaptureConfiguration.Builder)
  + [AudioPlaybackConfiguration](https://developer.android.com/reference/android/media/AudioPlaybackConfiguration)
  + [AudioPresentation](https://developer.android.com/reference/android/media/AudioPresentation)
  + [AudioPresentation.Builder](https://developer.android.com/reference/android/media/AudioPresentation.Builder)
  + [AudioProfile](https://developer.android.com/reference/android/media/AudioProfile)
  + [AudioRecord](https://developer.android.com/reference/android/media/AudioRecord)
  + [AudioRecord.Builder](https://developer.android.com/reference/android/media/AudioRecord.Builder)
  + [AudioRecord.MetricsConstants](https://developer.android.com/reference/android/media/AudioRecord.MetricsConstants)
  + [AudioRecordingConfiguration](https://developer.android.com/reference/android/media/AudioRecordingConfiguration)
  + [AudioTimestamp](https://developer.android.com/reference/android/media/AudioTimestamp)
  + [AudioTrack](https://developer.android.com/reference/android/media/AudioTrack)
  + [AudioTrack.Builder](https://developer.android.com/reference/android/media/AudioTrack.Builder)
  + [AudioTrack.MetricsConstants](https://developer.android.com/reference/android/media/AudioTrack.MetricsConstants)
  + [AudioTrack.StreamEventCallback](https://developer.android.com/reference/android/media/AudioTrack.StreamEventCallback)
  + [CamcorderProfile](https://developer.android.com/reference/android/media/CamcorderProfile)
  + [CameraProfile](https://developer.android.com/reference/android/media/CameraProfile)
  + [DrmInitData](https://developer.android.com/reference/android/media/DrmInitData)
  + [DrmInitData.SchemeInitData](https://developer.android.com/reference/android/media/DrmInitData.SchemeInitData)
  + [EncoderProfiles](https://developer.android.com/reference/android/media/EncoderProfiles)
  + [EncoderProfiles.AudioProfile](https://developer.android.com/reference/android/media/EncoderProfiles.AudioProfile)
  + [EncoderProfiles.VideoProfile](https://developer.android.com/reference/android/media/EncoderProfiles.VideoProfile)
  + [ExifInterface](https://developer.android.com/reference/android/media/ExifInterface)
  + [FaceDetector](https://developer.android.com/reference/android/media/FaceDetector)
  + [FaceDetector.Face](https://developer.android.com/reference/android/media/FaceDetector.Face)
  + [Image](https://developer.android.com/reference/android/media/Image)
  + [Image.Plane](https://developer.android.com/reference/android/media/Image.Plane)
  + [ImageReader](https://developer.android.com/reference/android/media/ImageReader)
  + [ImageReader.Builder](https://developer.android.com/reference/android/media/ImageReader.Builder)
  + [ImageWriter](https://developer.android.com/reference/android/media/ImageWriter)
  + [ImageWriter.Builder](https://developer.android.com/reference/android/media/ImageWriter.Builder)
  + [JetPlayer](https://developer.android.com/reference/android/media/JetPlayer)
  + [LoudnessCodecController](https://developer.android.com/reference/android/media/LoudnessCodecController)
  + [MediaActionSound](https://developer.android.com/reference/android/media/MediaActionSound)
  + [MediaCas](https://developer.android.com/reference/android/media/MediaCas)
  + [MediaCas.PluginDescriptor](https://developer.android.com/reference/android/media/MediaCas.PluginDescriptor)
  + [MediaCas.Session](https://developer.android.com/reference/android/media/MediaCas.Session)
  + [MediaCodec](https://developer.android.com/reference/android/media/MediaCodec)
  + [MediaCodec.BufferInfo](https://developer.android.com/reference/android/media/MediaCodec.BufferInfo)
  + [MediaCodec.Callback](https://developer.android.com/reference/android/media/MediaCodec.Callback)
  + [MediaCodec.CryptoInfo](https://developer.android.com/reference/android/media/MediaCodec.CryptoInfo)
  + [MediaCodec.CryptoInfo.Pattern](https://developer.android.com/reference/android/media/MediaCodec.CryptoInfo.Pattern)
  + [MediaCodec.LinearBlock](https://developer.android.com/reference/android/media/MediaCodec.LinearBlock)
  + [MediaCodec.MetricsConstants](https://developer.android.com/reference/android/media/MediaCodec.MetricsConstants)
  + [MediaCodec.OutputFrame](https://developer.android.com/reference/android/media/MediaCodec.OutputFrame)
  + [MediaCodec.ParameterDescriptor](https://developer.android.com/reference/android/media/MediaCodec.ParameterDescriptor)
  + [MediaCodec.QueueRequest](https://developer.android.com/reference/android/media/MediaCodec.QueueRequest)
  + [MediaCodecInfo](https://developer.android.com/reference/android/media/MediaCodecInfo)
  + [MediaCodecInfo.AudioCapabilities](https://developer.android.com/reference/android/media/MediaCodecInfo.AudioCapabilities)
  + [MediaCodecInfo.CodecCapabilities](https://developer.android.com/reference/android/media/MediaCodecInfo.CodecCapabilities)
  + [MediaCodecInfo.CodecProfileLevel](https://developer.android.com/reference/android/media/MediaCodecInfo.CodecProfileLevel)
  + [MediaCodecInfo.EncoderCapabilities](https://developer.android.com/reference/android/media/MediaCodecInfo.EncoderCapabilities)
  + [MediaCodecInfo.VideoCapabilities](https://developer.android.com/reference/android/media/MediaCodecInfo.VideoCapabilities)
  + [MediaCodecInfo.VideoCapabilities.PerformancePoint](https://developer.android.com/reference/android/media/MediaCodecInfo.VideoCapabilities.PerformancePoint)
  + [MediaCodecList](https://developer.android.com/reference/android/media/MediaCodecList)
  + [MediaCommunicationManager](https://developer.android.com/reference/android/media/MediaCommunicationManager)
  + [MediaController2](https://developer.android.com/reference/android/media/MediaController2)
  + [MediaController2.Builder](https://developer.android.com/reference/android/media/MediaController2.Builder)
  + [MediaController2.ControllerCallback](https://developer.android.com/reference/android/media/MediaController2.ControllerCallback)
  + [MediaCrypto](https://developer.android.com/reference/android/media/MediaCrypto)
  + [MediaDataSource](https://developer.android.com/reference/android/media/MediaDataSource)
  + [MediaDescrambler](https://developer.android.com/reference/android/media/MediaDescrambler)
  + [MediaDescription](https://developer.android.com/reference/android/media/MediaDescription)
  + [MediaDescription.Builder](https://developer.android.com/reference/android/media/MediaDescription.Builder)
  + [MediaDrm](https://developer.android.com/reference/android/media/MediaDrm)
  + [MediaDrm.CryptoSession](https://developer.android.com/reference/android/media/MediaDrm.CryptoSession)
  + [MediaDrm.ErrorCodes](https://developer.android.com/reference/android/media/MediaDrm.ErrorCodes)
  + [MediaDrm.KeyRequest](https://developer.android.com/reference/android/media/MediaDrm.KeyRequest)
  + [MediaDrm.KeyStatus](https://developer.android.com/reference/android/media/MediaDrm.KeyStatus)
  + [MediaDrm.LogMessage](https://developer.android.com/reference/android/media/MediaDrm.LogMessage)
  + [MediaDrm.MetricsConstants](https://developer.android.com/reference/android/media/MediaDrm.MetricsConstants)
  + [MediaDrm.PlaybackComponent](https://developer.android.com/reference/android/media/MediaDrm.PlaybackComponent)
  + [MediaDrm.ProvisionRequest](https://developer.android.com/reference/android/media/MediaDrm.ProvisionRequest)
  + [MediaExtractor](https://developer.android.com/reference/android/media/MediaExtractor)
  + [MediaExtractor.CasInfo](https://developer.android.com/reference/android/media/MediaExtractor.CasInfo)
  + [MediaExtractor.MetricsConstants](https://developer.android.com/reference/android/media/MediaExtractor.MetricsConstants)
  + [MediaFeature](https://developer.android.com/reference/android/media/MediaFeature)
  + [MediaFeature.HdrType](https://developer.android.com/reference/android/media/MediaFeature.HdrType)
  + [MediaFormat](https://developer.android.com/reference/android/media/MediaFormat)
  + [MediaFormat.QpOffsetRect](https://developer.android.com/reference/android/media/MediaFormat.QpOffsetRect)
  + [MediaMetadata](https://developer.android.com/reference/android/media/MediaMetadata)
  + [MediaMetadata.Builder](https://developer.android.com/reference/android/media/MediaMetadata.Builder)
  + [MediaMetadataEditor](https://developer.android.com/reference/android/media/MediaMetadataEditor)
  + [MediaMetadataRetriever](https://developer.android.com/reference/android/media/MediaMetadataRetriever)
  + [MediaMetadataRetriever.BitmapParams](https://developer.android.com/reference/android/media/MediaMetadataRetriever.BitmapParams)
  + [MediaMuxer](https://developer.android.com/reference/android/media/MediaMuxer)
  + [MediaMuxer.OutputFormat](https://developer.android.com/reference/android/media/MediaMuxer.OutputFormat)
  + [MediaParser](https://developer.android.com/reference/android/media/MediaParser)
  + [MediaParser.SeekMap](https://developer.android.com/reference/android/media/MediaParser.SeekMap)
  + [MediaParser.SeekPoint](https://developer.android.com/reference/android/media/MediaParser.SeekPoint)
  + [MediaParser.TrackData](https://developer.android.com/reference/android/media/MediaParser.TrackData)
  + [MediaPlayer](https://developer.android.com/reference/android/media/MediaPlayer)
  + [MediaPlayer.DrmInfo](https://developer.android.com/reference/android/media/MediaPlayer.DrmInfo)
  + [MediaPlayer.MetricsConstants](https://developer.android.com/reference/android/media/MediaPlayer.MetricsConstants)
  + [MediaPlayer.TrackInfo](https://developer.android.com/reference/android/media/MediaPlayer.TrackInfo)
  + [MediaRecorder](https://developer.android.com/reference/android/media/MediaRecorder)
  + [MediaRecorder.AudioEncoder](https://developer.android.com/reference/android/media/MediaRecorder.AudioEncoder)
  + [MediaRecorder.AudioSource](https://developer.android.com/reference/android/media/MediaRecorder.AudioSource)
  + [MediaRecorder.MetricsConstants](https://developer.android.com/reference/android/media/MediaRecorder.MetricsConstants)
  + [MediaRecorder.OutputFormat](https://developer.android.com/reference/android/media/MediaRecorder.OutputFormat)
  + [MediaRecorder.VideoEncoder](https://developer.android.com/reference/android/media/MediaRecorder.VideoEncoder)
  + [MediaRecorder.VideoSource](https://developer.android.com/reference/android/media/MediaRecorder.VideoSource)
  + [MediaRoute2Info](https://developer.android.com/reference/android/media/MediaRoute2Info)
  + [MediaRoute2Info.Builder](https://developer.android.com/reference/android/media/MediaRoute2Info.Builder)
  + [MediaRoute2ProviderService](https://developer.android.com/reference/android/media/MediaRoute2ProviderService)
  + [MediaRouter](https://developer.android.com/reference/android/media/MediaRouter)
  + [MediaRouter.Callback](https://developer.android.com/reference/android/media/MediaRouter.Callback)
  + [MediaRouter.RouteCategory](https://developer.android.com/reference/android/media/MediaRouter.RouteCategory)
  + [MediaRouter.RouteGroup](https://developer.android.com/reference/android/media/MediaRouter.RouteGroup)
  + [MediaRouter.RouteInfo](https://developer.android.com/reference/android/media/MediaRouter.RouteInfo)
  + [MediaRouter.SimpleCallback](https://developer.android.com/reference/android/media/MediaRouter.SimpleCallback)
  + [MediaRouter.UserRouteInfo](https://developer.android.com/reference/android/media/MediaRouter.UserRouteInfo)
  + [MediaRouter.VolumeCallback](https://developer.android.com/reference/android/media/MediaRouter.VolumeCallback)
  + [MediaRouter2](https://developer.android.com/reference/android/media/MediaRouter2)
  + [MediaRouter2.ControllerCallback](https://developer.android.com/reference/android/media/MediaRouter2.ControllerCallback)
  + [MediaRouter2.RouteCallback](https://developer.android.com/reference/android/media/MediaRouter2.RouteCallback)
  + [MediaRouter2.RoutingController](https://developer.android.com/reference/android/media/MediaRouter2.RoutingController)
  + [MediaRouter2.ScanRequest](https://developer.android.com/reference/android/media/MediaRouter2.ScanRequest)
  + [MediaRouter2.ScanRequest.Builder](https://developer.android.com/reference/android/media/MediaRouter2.ScanRequest.Builder)
  + [MediaRouter2.ScanToken](https://developer.android.com/reference/android/media/MediaRouter2.ScanToken)
  + [MediaRouter2.TransferCallback](https://developer.android.com/reference/android/media/MediaRouter2.TransferCallback)
  + [MediaScannerConnection](https://developer.android.com/reference/android/media/MediaScannerConnection)
  + [MediaSession2](https://developer.android.com/reference/android/media/MediaSession2)
  + [MediaSession2.Builder](https://developer.android.com/reference/android/media/MediaSession2.Builder)
  + [MediaSession2.ControllerInfo](https://developer.android.com/reference/android/media/MediaSession2.ControllerInfo)
  + [MediaSession2.SessionCallback](https://developer.android.com/reference/android/media/MediaSession2.SessionCallback)
  + [MediaSession2Service](https://developer.android.com/reference/android/media/MediaSession2Service)
  + [MediaSession2Service.MediaNotification](https://developer.android.com/reference/android/media/MediaSession2Service.MediaNotification)
  + [MediaSync](https://developer.android.com/reference/android/media/MediaSync)
  + [MediaSync.Callback](https://developer.android.com/reference/android/media/MediaSync.Callback)
  + [MediaSyncEvent](https://developer.android.com/reference/android/media/MediaSyncEvent)
  + [MediaTimestamp](https://developer.android.com/reference/android/media/MediaTimestamp)
  + [MicrophoneInfo](https://developer.android.com/reference/android/media/MicrophoneInfo)
  + [MicrophoneInfo.Coordinate3F](https://developer.android.com/reference/android/media/MicrophoneInfo.Coordinate3F)
  + [PlaybackParams](https://developer.android.com/reference/android/media/PlaybackParams)
  + [Rating](https://developer.android.com/reference/android/media/Rating)
  + [RemoteControlClient](https://developer.android.com/reference/android/media/RemoteControlClient)
  + [RemoteControlClient.MetadataEditor](https://developer.android.com/reference/android/media/RemoteControlClient.MetadataEditor)
  + [RemoteController](https://developer.android.com/reference/android/media/RemoteController)
  + [RemoteController.MetadataEditor](https://developer.android.com/reference/android/media/RemoteController.MetadataEditor)
  + [Ringtone](https://developer.android.com/reference/android/media/Ringtone)
  + [RingtoneManager](https://developer.android.com/reference/android/media/RingtoneManager)
  + [RouteDiscoveryPreference](https://developer.android.com/reference/android/media/RouteDiscoveryPreference)
  + [RouteDiscoveryPreference.Builder](https://developer.android.com/reference/android/media/RouteDiscoveryPreference.Builder)
  + [RouteListingPreference](https://developer.android.com/reference/android/media/RouteListingPreference)
  + [RouteListingPreference.Builder](https://developer.android.com/reference/android/media/RouteListingPreference.Builder)
  + [RouteListingPreference.Item](https://developer.android.com/reference/android/media/RouteListingPreference.Item)
  + [RouteListingPreference.Item.Builder](https://developer.android.com/reference/android/media/RouteListingPreference.Item.Builder)
  + [RoutingSessionInfo](https://developer.android.com/reference/android/media/RoutingSessionInfo)
  + [RoutingSessionInfo.Builder](https://developer.android.com/reference/android/media/RoutingSessionInfo.Builder)
  + [Session2Command](https://developer.android.com/reference/android/media/Session2Command)
  + [Session2Command.Result](https://developer.android.com/reference/android/media/Session2Command.Result)
  + [Session2CommandGroup](https://developer.android.com/reference/android/media/Session2CommandGroup)
  + [Session2CommandGroup.Builder](https://developer.android.com/reference/android/media/Session2CommandGroup.Builder)
  + [Session2Token](https://developer.android.com/reference/android/media/Session2Token)
  + [SoundPool](https://developer.android.com/reference/android/media/SoundPool)
  + [SoundPool.Builder](https://developer.android.com/reference/android/media/SoundPool.Builder)
  + [Spatializer](https://developer.android.com/reference/android/media/Spatializer)
  + [SubtitleData](https://developer.android.com/reference/android/media/SubtitleData)
  + [SuggestedDeviceInfo](https://developer.android.com/reference/android/media/SuggestedDeviceInfo)
  + [SuggestedDeviceInfo.Builder](https://developer.android.com/reference/android/media/SuggestedDeviceInfo.Builder)
  + [SyncParams](https://developer.android.com/reference/android/media/SyncParams)
  + [ThumbnailUtils](https://developer.android.com/reference/android/media/ThumbnailUtils)
  + [TimedMetaData](https://developer.android.com/reference/android/media/TimedMetaData)
  + [TimedText](https://developer.android.com/reference/android/media/TimedText)
  + [ToneGenerator](https://developer.android.com/reference/android/media/ToneGenerator)
  + [VolumeProvider](https://developer.android.com/reference/android/media/VolumeProvider)
  + [VolumeShaper](https://developer.android.com/reference/android/media/VolumeShaper)
  + [VolumeShaper.Configuration](https://developer.android.com/reference/android/media/VolumeShaper.Configuration)
  + [VolumeShaper.Configuration.Builder](https://developer.android.com/reference/android/media/VolumeShaper.Configuration.Builder)
  + [VolumeShaper.Operation](https://developer.android.com/reference/android/media/VolumeShaper.Operation)
* ## Exceptions

  + [DeniedByServerException](https://developer.android.com/reference/android/media/DeniedByServerException)
  + [MediaCasException](https://developer.android.com/reference/android/media/MediaCasException)
  + [MediaCasException.DeniedByServerException](https://developer.android.com/reference/android/media/MediaCasException.DeniedByServerException)
  + [MediaCasException.InsufficientResourceException](https://developer.android.com/reference/android/media/MediaCasException.InsufficientResourceException)
  + [MediaCasException.NotProvisionedException](https://developer.android.com/reference/android/media/MediaCasException.NotProvisionedException)
  + [MediaCasException.ResourceBusyException](https://developer.android.com/reference/android/media/MediaCasException.ResourceBusyException)
  + [MediaCasException.UnsupportedCasException](https://developer.android.com/reference/android/media/MediaCasException.UnsupportedCasException)
  + [MediaCasStateException](https://developer.android.com/reference/android/media/MediaCasStateException)
  + [MediaCodec.CodecException](https://developer.android.com/reference/android/media/MediaCodec.CodecException)
  + [MediaCodec.CryptoException](https://developer.android.com/reference/android/media/MediaCodec.CryptoException)
  + [MediaCodec.IncompatibleWithBlockModelException](https://developer.android.com/reference/android/media/MediaCodec.IncompatibleWithBlockModelException)
  + [MediaCodec.InvalidBufferFlagsException](https://developer.android.com/reference/android/media/MediaCodec.InvalidBufferFlagsException)
  + [MediaCryptoException](https://developer.android.com/reference/android/media/MediaCryptoException)
  + [MediaDrm.MediaDrmStateException](https://developer.android.com/reference/android/media/MediaDrm.MediaDrmStateException)
  + [MediaDrm.SessionException](https://developer.android.com/reference/android/media/MediaDrm.SessionException)
  + [MediaDrmException](https://developer.android.com/reference/android/media/MediaDrmException)
  + [MediaDrmResetException](https://developer.android.com/reference/android/media/MediaDrmResetException)
  + [MediaParser.ParsingException](https://developer.android.com/reference/android/media/MediaParser.ParsingException)
  + [MediaParser.UnrecognizedInputFormatException](https://developer.android.com/reference/android/media/MediaParser.UnrecognizedInputFormatException)
  + [MediaPlayer.NoDrmSchemeException](https://developer.android.com/reference/android/media/MediaPlayer.NoDrmSchemeException)
  + [MediaPlayer.ProvisioningNetworkErrorException](https://developer.android.com/reference/android/media/MediaPlayer.ProvisioningNetworkErrorException)
  + [MediaPlayer.ProvisioningServerErrorException](https://developer.android.com/reference/android/media/MediaPlayer.ProvisioningServerErrorException)
  + [NotProvisionedException](https://developer.android.com/reference/android/media/NotProvisionedException)
  + [ResourceBusyException](https://developer.android.com/reference/android/media/ResourceBusyException)
  + [UnsupportedSchemeException](https://developer.android.com/reference/android/media/UnsupportedSchemeException)
