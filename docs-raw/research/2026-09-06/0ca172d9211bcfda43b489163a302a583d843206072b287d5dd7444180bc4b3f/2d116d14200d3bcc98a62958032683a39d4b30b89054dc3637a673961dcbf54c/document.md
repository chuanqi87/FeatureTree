# android.net.http

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# android.net.http

---

[Kotlin](https://developer.android.com/reference/kotlin/android/net/http/package-summary "View this page in Kotlin")
|Java

## Interfaces

|  |  |
| --- | --- |
| [BidirectionalStream.Callback](https://developer.android.com/reference/android/net/http/BidirectionalStream.Callback) | Callback interface used to receive callbacks from a `BidirectionalStream`. |
| [Proxy.HttpConnectCallback](https://developer.android.com/reference/android/net/http/Proxy.HttpConnectCallback) | Controls tunnels established via HTTP CONNECT. |
| [UrlRequest.Callback](https://developer.android.com/reference/android/net/http/UrlRequest.Callback) | Users of the HTTP stack extend this class to receive callbacks indicating the progress of a `UrlRequest` being processed. |
| [UrlRequest.StatusListener](https://developer.android.com/reference/android/net/http/UrlRequest.StatusListener) | Listener interface used with `UrlRequest.getStatus(StatusListener)` to receive the status of a `UrlRequest`. |

## Classes

|  |  |
| --- | --- |
| [BidirectionalStream](https://developer.android.com/reference/android/net/http/BidirectionalStream) | Class for bidirectional sending and receiving of data over HTTP/2 or QUIC connections. |
| [BidirectionalStream.Builder](https://developer.android.com/reference/android/net/http/BidirectionalStream.Builder) | Builder for `BidirectionalStream`s. |
| [ConnectionMigrationOptions](https://developer.android.com/reference/android/net/http/ConnectionMigrationOptions) | A class configuring the HTTP connection migration functionality. |
| [ConnectionMigrationOptions.Builder](https://developer.android.com/reference/android/net/http/ConnectionMigrationOptions.Builder) | Builder for `ConnectionMigrationOptions`. |
| [DnsOptions](https://developer.android.com/reference/android/net/http/DnsOptions) | A class configuring the host resolution functionality. |
| [DnsOptions.Builder](https://developer.android.com/reference/android/net/http/DnsOptions.Builder) | Builder for `DnsOptions`. |
| [DnsOptions.StaleDnsOptions](https://developer.android.com/reference/android/net/http/DnsOptions.StaleDnsOptions) | A class configuring the stale DNS functionality. |
| [DnsOptions.StaleDnsOptions.Builder](https://developer.android.com/reference/android/net/http/DnsOptions.StaleDnsOptions.Builder) | Builder for `StaleDnsOptions`. |
| [FinishedRequestTimings](https://developer.android.com/reference/android/net/http/FinishedRequestTimings) | Metrics collected for a single request. |
| [HeaderBlock](https://developer.android.com/reference/android/net/http/HeaderBlock) | Unmodifiable container of headers or trailers. |
| [HttpEngine](https://developer.android.com/reference/android/net/http/HttpEngine) | An engine to process `UrlRequest`s, which uses the best HTTP stack available on the current platform. |
| [HttpEngine.Builder](https://developer.android.com/reference/android/net/http/HttpEngine.Builder) | A builder for `HttpEngine`s, which allows runtime configuration of `HttpEngine`. |
| [HttpResponseCache](https://developer.android.com/reference/android/net/http/HttpResponseCache) | Caches HTTP and HTTPS responses to the filesystem so they may be reused, saving time and bandwidth. |
| [Proxy](https://developer.android.com/reference/android/net/http/Proxy) | Represents a proxy that can be used by `HttpEngine`. |
| [Proxy.HttpConnectCallback.Request](https://developer.android.com/reference/android/net/http/Proxy.HttpConnectCallback.Request) | Represents an HTTP CONNECT request being sent to the proxy server. |
| [ProxyOptions](https://developer.android.com/reference/android/net/http/ProxyOptions) | Defines a proxy configuration that can be used by `HttpEngine`. |
| [QuicOptions](https://developer.android.com/reference/android/net/http/QuicOptions) | Configuration options for QUIC. |
| [QuicOptions.Builder](https://developer.android.com/reference/android/net/http/QuicOptions.Builder) | Builder for `QuicOptions`. |
| [SslCertificate](https://developer.android.com/reference/android/net/http/SslCertificate) | SSL certificate info (certificate details) class |
| [SslCertificate.DName](https://developer.android.com/reference/android/net/http/SslCertificate.DName) | A distinguished name helper class: a 3-tuple of:  * the most specific common name (CN) * the most specific organization (O) * the most specific organizational unit (OU) |
| [SslError](https://developer.android.com/reference/android/net/http/SslError) | This class represents a set of one or more SSL errors and the associated SSL certificate. |
| [UploadDataProvider](https://developer.android.com/reference/android/net/http/UploadDataProvider) | Abstract class allowing the embedder to provide an upload body to `UrlRequest`. |
| [UploadDataSink](https://developer.android.com/reference/android/net/http/UploadDataSink) | Defines callbacks methods for `UploadDataProvider`. |
| [UrlRequest](https://developer.android.com/reference/android/net/http/UrlRequest) | Controls an HTTP request (GET, PUT, POST etc). |
| [UrlRequest.Builder](https://developer.android.com/reference/android/net/http/UrlRequest.Builder) | Builder for `UrlRequest`s. |
| [UrlRequest.Status](https://developer.android.com/reference/android/net/http/UrlRequest.Status) | Request status values returned by `UrlRequest.getStatus(StatusListener)`. |
| [UrlResponseInfo](https://developer.android.com/reference/android/net/http/UrlResponseInfo) | Basic information about a response. |
| [X509TrustManagerExtensions](https://developer.android.com/reference/android/net/http/X509TrustManagerExtensions) | X509TrustManager wrapper exposing Android-added features. |

## Exceptions

|  |  |
| --- | --- |
| [CallbackException](https://developer.android.com/reference/android/net/http/CallbackException) | Exception passed to `UrlRequest.Callback.onFailed()` when `UrlRequest.Callback` or `UploadDataProvider` method throws an exception. |
| [HttpException](https://developer.android.com/reference/android/net/http/HttpException) | Base exception passed to `UrlRequest.Callback.onFailed()`. |
| [InlineExecutionProhibitedException](https://developer.android.com/reference/android/net/http/InlineExecutionProhibitedException) | Thrown when an executor runs a submitted runnable inline in `java.util.concurrent.Executor.execute(Runnable)` and `UrlRequest.Builder.setDirectExecutorAllowed` was not called. |
| [NetworkException](https://developer.android.com/reference/android/net/http/NetworkException) | Exception passed to `UrlRequest.Callback.onFailed()` when the HTTP stack fails to process a network request. |
| [QuicException](https://developer.android.com/reference/android/net/http/QuicException) | Subclass of `NetworkException` which contains a detailed [QUIC](https://www.chromium.org/quic) error code from  [QuicErrorCode](https://cs.chromium.org/search/?q=symbol:%5CbQuicErrorCode%5Cb). |

* ## Interfaces

  + [BidirectionalStream.Callback](https://developer.android.com/reference/android/net/http/BidirectionalStream.Callback)
  + [Proxy.HttpConnectCallback](https://developer.android.com/reference/android/net/http/Proxy.HttpConnectCallback)
  + [UrlRequest.Callback](https://developer.android.com/reference/android/net/http/UrlRequest.Callback)
  + [UrlRequest.StatusListener](https://developer.android.com/reference/android/net/http/UrlRequest.StatusListener)
* ## Classes

  + [BidirectionalStream](https://developer.android.com/reference/android/net/http/BidirectionalStream)
  + [BidirectionalStream.Builder](https://developer.android.com/reference/android/net/http/BidirectionalStream.Builder)
  + [ConnectionMigrationOptions](https://developer.android.com/reference/android/net/http/ConnectionMigrationOptions)
  + [ConnectionMigrationOptions.Builder](https://developer.android.com/reference/android/net/http/ConnectionMigrationOptions.Builder)
  + [DnsOptions](https://developer.android.com/reference/android/net/http/DnsOptions)
  + [DnsOptions.Builder](https://developer.android.com/reference/android/net/http/DnsOptions.Builder)
  + [DnsOptions.StaleDnsOptions](https://developer.android.com/reference/android/net/http/DnsOptions.StaleDnsOptions)
  + [DnsOptions.StaleDnsOptions.Builder](https://developer.android.com/reference/android/net/http/DnsOptions.StaleDnsOptions.Builder)
  + [FinishedRequestTimings](https://developer.android.com/reference/android/net/http/FinishedRequestTimings)
  + [HeaderBlock](https://developer.android.com/reference/android/net/http/HeaderBlock)
  + [HttpEngine](https://developer.android.com/reference/android/net/http/HttpEngine)
  + [HttpEngine.Builder](https://developer.android.com/reference/android/net/http/HttpEngine.Builder)
  + [HttpResponseCache](https://developer.android.com/reference/android/net/http/HttpResponseCache)
  + [Proxy](https://developer.android.com/reference/android/net/http/Proxy)
  + [Proxy.HttpConnectCallback.Request](https://developer.android.com/reference/android/net/http/Proxy.HttpConnectCallback.Request)
  + [ProxyOptions](https://developer.android.com/reference/android/net/http/ProxyOptions)
  + [QuicOptions](https://developer.android.com/reference/android/net/http/QuicOptions)
  + [QuicOptions.Builder](https://developer.android.com/reference/android/net/http/QuicOptions.Builder)
  + [SslCertificate](https://developer.android.com/reference/android/net/http/SslCertificate)
  + [SslCertificate.DName](https://developer.android.com/reference/android/net/http/SslCertificate.DName)
  + [SslError](https://developer.android.com/reference/android/net/http/SslError)
  + [UploadDataProvider](https://developer.android.com/reference/android/net/http/UploadDataProvider)
  + [UploadDataSink](https://developer.android.com/reference/android/net/http/UploadDataSink)
  + [UrlRequest](https://developer.android.com/reference/android/net/http/UrlRequest)
  + [UrlRequest.Builder](https://developer.android.com/reference/android/net/http/UrlRequest.Builder)
  + [UrlRequest.Status](https://developer.android.com/reference/android/net/http/UrlRequest.Status)
  + [UrlResponseInfo](https://developer.android.com/reference/android/net/http/UrlResponseInfo)
  + [X509TrustManagerExtensions](https://developer.android.com/reference/android/net/http/X509TrustManagerExtensions)
* ## Exceptions

  + [CallbackException](https://developer.android.com/reference/android/net/http/CallbackException)
  + [HttpException](https://developer.android.com/reference/android/net/http/HttpException)
  + [InlineExecutionProhibitedException](https://developer.android.com/reference/android/net/http/InlineExecutionProhibitedException)
  + [NetworkException](https://developer.android.com/reference/android/net/http/NetworkException)
  + [QuicException](https://developer.android.com/reference/android/net/http/QuicException)
