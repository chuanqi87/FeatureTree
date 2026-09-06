# android.telephony.mbms

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# android.telephony.mbms

---

[Kotlin](https://developer.android.com/reference/kotlin/android/telephony/mbms/package-summary "View this page in Kotlin")
|Java

## Interfaces

|  |  |
| --- | --- |
| [GroupCallCallback](https://developer.android.com/reference/android/telephony/mbms/GroupCallCallback) | A callback class for use when the application is in a group call. |
| [MbmsGroupCallSessionCallback](https://developer.android.com/reference/android/telephony/mbms/MbmsGroupCallSessionCallback) | A callback class that is used to receive information from the middleware on MBMS group-call services. |

## Classes

|  |  |
| --- | --- |
| [DownloadProgressListener](https://developer.android.com/reference/android/telephony/mbms/DownloadProgressListener) | A optional listener class used by download clients to track progress. |
| [DownloadRequest](https://developer.android.com/reference/android/telephony/mbms/DownloadRequest) | Describes a request to download files over cell-broadcast. |
| [DownloadRequest.Builder](https://developer.android.com/reference/android/telephony/mbms/DownloadRequest.Builder) |  |
| [DownloadStatusListener](https://developer.android.com/reference/android/telephony/mbms/DownloadStatusListener) | A optional listener class used by download clients to track progress. |
| [FileInfo](https://developer.android.com/reference/android/telephony/mbms/FileInfo) | Describes a single file that is available over MBMS. |
| [FileServiceInfo](https://developer.android.com/reference/android/telephony/mbms/FileServiceInfo) | Describes a file service available from the carrier from which files can be downloaded via cell-broadcast. |
| [GroupCall](https://developer.android.com/reference/android/telephony/mbms/GroupCall) | Class used to represent a single MBMS group call. |
| [MbmsDownloadReceiver](https://developer.android.com/reference/android/telephony/mbms/MbmsDownloadReceiver) | The `BroadcastReceiver` responsible for handling intents sent from the middleware. |
| [MbmsDownloadSessionCallback](https://developer.android.com/reference/android/telephony/mbms/MbmsDownloadSessionCallback) | A callback class that apps should use to receive information on file downloads over cell-broadcast. |
| [MbmsErrors](https://developer.android.com/reference/android/telephony/mbms/MbmsErrors) |  |
| [MbmsErrors.DownloadErrors](https://developer.android.com/reference/android/telephony/mbms/MbmsErrors.DownloadErrors) | Indicates the errors that are applicable only to the file-download use-case |
| [MbmsErrors.GeneralErrors](https://developer.android.com/reference/android/telephony/mbms/MbmsErrors.GeneralErrors) | Indicates the errors that may occur at any point and are applicable to both streaming and file-download. |
| [MbmsErrors.GroupCallErrors](https://developer.android.com/reference/android/telephony/mbms/MbmsErrors.GroupCallErrors) | Indicates the errors that are applicable only to the group call use-case. |
| [MbmsErrors.InitializationErrors](https://developer.android.com/reference/android/telephony/mbms/MbmsErrors.InitializationErrors) | Indicates errors that may be generated during initialization by the middleware. |
| [MbmsErrors.StreamingErrors](https://developer.android.com/reference/android/telephony/mbms/MbmsErrors.StreamingErrors) | Indicates the errors that are applicable only to the streaming use-case |
| [MbmsStreamingSessionCallback](https://developer.android.com/reference/android/telephony/mbms/MbmsStreamingSessionCallback) | A callback class that is used to receive information from the middleware on MBMS streaming services. |
| [ServiceInfo](https://developer.android.com/reference/android/telephony/mbms/ServiceInfo) | Describes a cell-broadcast service. |
| [StreamingService](https://developer.android.com/reference/android/telephony/mbms/StreamingService) | Class used to represent a single MBMS stream. |
| [StreamingServiceCallback](https://developer.android.com/reference/android/telephony/mbms/StreamingServiceCallback) | A callback class for use when the application is actively streaming content. |
| [StreamingServiceInfo](https://developer.android.com/reference/android/telephony/mbms/StreamingServiceInfo) | Describes a single MBMS streaming service. |

* ## Interfaces

  + [GroupCallCallback](https://developer.android.com/reference/android/telephony/mbms/GroupCallCallback)
  + [MbmsGroupCallSessionCallback](https://developer.android.com/reference/android/telephony/mbms/MbmsGroupCallSessionCallback)
* ## Classes

  + [DownloadProgressListener](https://developer.android.com/reference/android/telephony/mbms/DownloadProgressListener)
  + [DownloadRequest](https://developer.android.com/reference/android/telephony/mbms/DownloadRequest)
  + [DownloadRequest.Builder](https://developer.android.com/reference/android/telephony/mbms/DownloadRequest.Builder)
  + [DownloadStatusListener](https://developer.android.com/reference/android/telephony/mbms/DownloadStatusListener)
  + [FileInfo](https://developer.android.com/reference/android/telephony/mbms/FileInfo)
  + [FileServiceInfo](https://developer.android.com/reference/android/telephony/mbms/FileServiceInfo)
  + [GroupCall](https://developer.android.com/reference/android/telephony/mbms/GroupCall)
  + [MbmsDownloadReceiver](https://developer.android.com/reference/android/telephony/mbms/MbmsDownloadReceiver)
  + [MbmsDownloadSessionCallback](https://developer.android.com/reference/android/telephony/mbms/MbmsDownloadSessionCallback)
  + [MbmsErrors](https://developer.android.com/reference/android/telephony/mbms/MbmsErrors)
  + [MbmsErrors.DownloadErrors](https://developer.android.com/reference/android/telephony/mbms/MbmsErrors.DownloadErrors)
  + [MbmsErrors.GeneralErrors](https://developer.android.com/reference/android/telephony/mbms/MbmsErrors.GeneralErrors)
  + [MbmsErrors.GroupCallErrors](https://developer.android.com/reference/android/telephony/mbms/MbmsErrors.GroupCallErrors)
  + [MbmsErrors.InitializationErrors](https://developer.android.com/reference/android/telephony/mbms/MbmsErrors.InitializationErrors)
  + [MbmsErrors.StreamingErrors](https://developer.android.com/reference/android/telephony/mbms/MbmsErrors.StreamingErrors)
  + [MbmsStreamingSessionCallback](https://developer.android.com/reference/android/telephony/mbms/MbmsStreamingSessionCallback)
  + [ServiceInfo](https://developer.android.com/reference/android/telephony/mbms/ServiceInfo)
  + [StreamingService](https://developer.android.com/reference/android/telephony/mbms/StreamingService)
  + [StreamingServiceCallback](https://developer.android.com/reference/android/telephony/mbms/StreamingServiceCallback)
  + [StreamingServiceInfo](https://developer.android.com/reference/android/telephony/mbms/StreamingServiceInfo)
