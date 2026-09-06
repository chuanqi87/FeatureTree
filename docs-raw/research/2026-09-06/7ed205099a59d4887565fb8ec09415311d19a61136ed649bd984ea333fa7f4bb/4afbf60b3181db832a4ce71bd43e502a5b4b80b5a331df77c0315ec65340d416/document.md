# android.net

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# android.net

---

[Kotlin](https://developer.android.com/reference/kotlin/android/net/package-summary "View this page in Kotlin")
|Java

Classes that help with network access, beyond the normal java.net.\* APIs.

## Interfaces

|  |  |
| --- | --- |
| [ConnectivityManager.OnNetworkActiveListener](https://developer.android.com/reference/android/net/ConnectivityManager.OnNetworkActiveListener) | Callback for use with `ConnectivityManager.addDefaultNetworkActiveListener` to find out when the system default network has gone in to a high power state. |
| [DnsResolver.Callback](https://developer.android.com/reference/android/net/DnsResolver.Callback)<T> | Base interface for answer callbacks |
| [TetheringManager.StartTetheringCallback](https://developer.android.com/reference/android/net/TetheringManager.StartTetheringCallback) | Callback for use with `TetheringManager.startTethering(TetheringRequest, Executor, StartTetheringCallback)` to find out whether tethering succeeded. |
| [TetheringManager.StopTetheringCallback](https://developer.android.com/reference/android/net/TetheringManager.StopTetheringCallback) | Callback for use with `TetheringManager.stopTethering(TetheringRequest, Executor, StopTetheringCallback)` to find out whether stop tethering succeeded. |
| [TetheringManager.TetheringEventCallback](https://developer.android.com/reference/android/net/TetheringManager.TetheringEventCallback) | Callback for use with `ERROR(/registerTetheringEventCallback)` to find out tethering upstream status. |
| [TransportInfo](https://developer.android.com/reference/android/net/TransportInfo) | A container for transport-specific capabilities which is returned by `NetworkCapabilities.getTransportInfo()`. |
| [UrlQuerySanitizer.ValueSanitizer](https://developer.android.com/reference/android/net/UrlQuerySanitizer.ValueSanitizer) | A functor used to sanitize a single query value. |

## Classes

|  |  |
| --- | --- |
| [CaptivePortal](https://developer.android.com/reference/android/net/CaptivePortal) | A class allowing apps handling the `ConnectivityManager.ACTION_CAPTIVE_PORTAL_SIGN_IN` activity to indicate to the system different outcomes of captive portal sign in. |
| [ConnectivityDiagnosticsManager](https://developer.android.com/reference/android/net/ConnectivityDiagnosticsManager) | Class that provides utilities for collecting network connectivity diagnostics information. |
| [ConnectivityDiagnosticsManager.ConnectivityDiagnosticsCallback](https://developer.android.com/reference/android/net/ConnectivityDiagnosticsManager.ConnectivityDiagnosticsCallback) | Abstract base class for Connectivity Diagnostics callbacks. |
| [ConnectivityDiagnosticsManager.ConnectivityReport](https://developer.android.com/reference/android/net/ConnectivityDiagnosticsManager.ConnectivityReport) | Class that includes connectivity information for a specific Network at a specific time. |
| [ConnectivityDiagnosticsManager.DataStallReport](https://developer.android.com/reference/android/net/ConnectivityDiagnosticsManager.DataStallReport) | Class that includes information for a suspected data stall on a specific Network |
| [ConnectivityManager](https://developer.android.com/reference/android/net/ConnectivityManager) | Class that answers queries about the state of network connectivity. |
| [ConnectivityManager.NetworkCallback](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback) | Base class for `NetworkRequest` callbacks. |
| [Credentials](https://developer.android.com/reference/android/net/Credentials) | A class for representing UNIX credentials passed via ancillary data on UNIX domain sockets. |
| [DhcpInfo](https://developer.android.com/reference/android/net/DhcpInfo) | A simple object for retrieving the results of a DHCP request. |
| [DnsResolver](https://developer.android.com/reference/android/net/DnsResolver) | Dns resolver class for asynchronous dns querying Note that if a client sends a query with more than 1 record in the question section but the remote dns server does not support this, it may not respond at all, leading to a timeout. |
| [EthernetNetworkSpecifier](https://developer.android.com/reference/android/net/EthernetNetworkSpecifier) | A `NetworkSpecifier` used to identify ethernet interfaces. |
| [Ikev2VpnProfile](https://developer.android.com/reference/android/net/Ikev2VpnProfile) | The Ikev2VpnProfile is a configuration for the platform setup of IKEv2/IPsec VPNs. |
| [Ikev2VpnProfile.Builder](https://developer.android.com/reference/android/net/Ikev2VpnProfile.Builder) | A incremental builder for IKEv2 VPN profiles |
| [InetAddresses](https://developer.android.com/reference/android/net/InetAddresses) | Utility methods for `InetAddress` implementations. |
| [IpConfiguration](https://developer.android.com/reference/android/net/IpConfiguration) | A class representing the IP configuration of a network. |
| [IpConfiguration.Builder](https://developer.android.com/reference/android/net/IpConfiguration.Builder) | Builder used to construct `IpConfiguration` objects. |
| [IpPrefix](https://developer.android.com/reference/android/net/IpPrefix) | This class represents an IP prefix, i.e., a contiguous block of IP addresses aligned on a power of two boundary (also known as an "IP subnet"). |
| [IpSecAlgorithm](https://developer.android.com/reference/android/net/IpSecAlgorithm) | This class represents a single algorithm that can be used by an `IpSecTransform`. |
| [IpSecManager](https://developer.android.com/reference/android/net/IpSecManager) | This class contains methods for managing IPsec sessions. |
| [IpSecManager.SecurityParameterIndex](https://developer.android.com/reference/android/net/IpSecManager.SecurityParameterIndex) | This class represents a reserved SPI. |
| [IpSecManager.UdpEncapsulationSocket](https://developer.android.com/reference/android/net/IpSecManager.UdpEncapsulationSocket) | This class provides access to a UDP encapsulation Socket. |
| [IpSecTransform](https://developer.android.com/reference/android/net/IpSecTransform) | This class represents a transform, which roughly corresponds to an IPsec Security Association. |
| [IpSecTransform.Builder](https://developer.android.com/reference/android/net/IpSecTransform.Builder) | This class is used to build `IpSecTransform` objects. |
| [IpSecTransformState](https://developer.android.com/reference/android/net/IpSecTransformState) | This class represents a snapshot of the state of an IpSecTransform This class provides the current state of an IpSecTransform, enabling link metric analysis by the caller. |
| [IpSecTransformState.Builder](https://developer.android.com/reference/android/net/IpSecTransformState.Builder) | Builder class for testing purposes Except for testing, IPsec callers normally do not instantiate `IpSecTransformState` themselves but instead get a reference via `IpSecTransformState` |
| [L2capNetworkSpecifier](https://developer.android.com/reference/android/net/L2capNetworkSpecifier) | A `NetworkSpecifier` used to identify an L2CAP network over BLE. |
| [L2capNetworkSpecifier.Builder](https://developer.android.com/reference/android/net/L2capNetworkSpecifier.Builder) | A builder class for L2capNetworkSpecifier. |
| [LinkAddress](https://developer.android.com/reference/android/net/LinkAddress) | Identifies an IP address on a network link. |
| [LinkProperties](https://developer.android.com/reference/android/net/LinkProperties) | Describes the properties of a network link. |
| [LocalServerSocket](https://developer.android.com/reference/android/net/LocalServerSocket) | Non-standard class for creating an inbound UNIX-domain socket in the Linux abstract namespace. |
| [LocalSocket](https://developer.android.com/reference/android/net/LocalSocket) | Creates a (non-server) socket in the UNIX-domain namespace. |
| [LocalSocketAddress](https://developer.android.com/reference/android/net/LocalSocketAddress) | A UNIX-domain (AF\_LOCAL) socket address. |
| [MacAddress](https://developer.android.com/reference/android/net/MacAddress) | Representation of a MAC address. |
| [MailTo](https://developer.android.com/reference/android/net/MailTo) | MailTo URL parser This class parses a mailto scheme URL and then can be queried for the parsed parameters. |
| [Network](https://developer.android.com/reference/android/net/Network) | Identifies a `Network`. |
| [NetworkCapabilities](https://developer.android.com/reference/android/net/NetworkCapabilities) | Representation of the capabilities of an active network. |
| [NetworkInfo](https://developer.android.com/reference/android/net/NetworkInfo) | *This class was deprecated in API level 29. Callers should instead use the `ConnectivityManager.NetworkCallback` API to learn about connectivity changes, or switch to use `ConnectivityManager.getNetworkCapabilities` or `ConnectivityManager.getLinkProperties` to get information synchronously. Keep in mind that while callbacks are guaranteed to be called for every event in order, synchronous calls have no such constraints, and as such it is unadvisable to use the synchronous methods inside the callbacks as they will often not offer a view of networking that is consistent (that is: they may return a past or a future state with respect to the event being processed by the callback). Instead, callers are advised to only use the arguments of the callbacks, possibly memorizing the specific bits of information they need to keep from one callback to another.* |
| [NetworkRequest](https://developer.android.com/reference/android/net/NetworkRequest) | An object describing a network that the application is interested in. |
| [NetworkRequest.Builder](https://developer.android.com/reference/android/net/NetworkRequest.Builder) | Builder used to create `NetworkRequest` objects. |
| [NetworkSpecifier](https://developer.android.com/reference/android/net/NetworkSpecifier) | Describes specific properties of a requested network for use in a `NetworkRequest`. |
| [PlatformVpnProfile](https://developer.android.com/reference/android/net/PlatformVpnProfile) | PlatformVpnProfile represents a configuration for a platform-based VPN implementation. |
| [Proxy](https://developer.android.com/reference/android/net/Proxy) | A convenience class for accessing the user and default proxy settings. |
| [ProxyInfo](https://developer.android.com/reference/android/net/ProxyInfo) | Describes a proxy configuration. |
| [RouteInfo](https://developer.android.com/reference/android/net/RouteInfo) | Represents a network route. |
| [SocketKeepalive](https://developer.android.com/reference/android/net/SocketKeepalive) | Allows applications to request that the system periodically send specific packets on their behalf, using hardware offload to save battery power. |
| [SocketKeepalive.Callback](https://developer.android.com/reference/android/net/SocketKeepalive.Callback) | The callback which app can use to learn the status changes of `SocketKeepalive`. |
| [SSLCertificateSocketFactory](https://developer.android.com/reference/android/net/SSLCertificateSocketFactory) | *This class was deprecated in API level 29. This class has less error-prone replacements using standard APIs. To create an `SSLSocket`, obtain an `SSLSocketFactory` from `SSLSocketFactory.getDefault()` or `SSLContext.getSocketFactory()`. To verify hostnames, pass `"HTTPS"` to `javax.net.ssl.SSLParameters.setEndpointIdentificationAlgorithm(String)`. To enable ALPN, use `javax.net.ssl.SSLParameters.setApplicationProtocols(String[])`. To enable SNI, use `SSLParameters.setServerNames(java.util.List)`.* |
| [SSLSessionCache](https://developer.android.com/reference/android/net/SSLSessionCache) | File-based cache of established SSL sessions. |
| [StaticIpConfiguration](https://developer.android.com/reference/android/net/StaticIpConfiguration) | Class that describes static IP configuration. |
| [StaticIpConfiguration.Builder](https://developer.android.com/reference/android/net/StaticIpConfiguration.Builder) | Helper class to build a new instance of `StaticIpConfiguration`. |
| [TelephonyNetworkSpecifier](https://developer.android.com/reference/android/net/TelephonyNetworkSpecifier) | NetworkSpecifier object for cellular network request. |
| [TelephonyNetworkSpecifier.Builder](https://developer.android.com/reference/android/net/TelephonyNetworkSpecifier.Builder) | Builder to create `TelephonyNetworkSpecifier` object. |
| [TetheringInterface](https://developer.android.com/reference/android/net/TetheringInterface) | The mapping of tethering interface and type. |
| [TetheringManager](https://developer.android.com/reference/android/net/TetheringManager) | This class provides the APIs to control the tethering service. |
| [TetheringManager.TetheringRequest](https://developer.android.com/reference/android/net/TetheringManager.TetheringRequest) | Use with `TetheringManager.startTethering(TetheringRequest, Executor, StartTetheringCallback)` to specify additional parameters when starting tethering. |
| [TetheringManager.TetheringRequest.Builder](https://developer.android.com/reference/android/net/TetheringManager.TetheringRequest.Builder) | Builder used to create TetheringRequest. |
| [TrafficStats](https://developer.android.com/reference/android/net/TrafficStats) | Class that provides network traffic statistics. |
| [Uri](https://developer.android.com/reference/android/net/Uri) | Immutable URI reference. |
| [Uri.Builder](https://developer.android.com/reference/android/net/Uri.Builder) | Helper class for building or manipulating URI references. |
| [UrlQuerySanitizer](https://developer.android.com/reference/android/net/UrlQuerySanitizer) | Sanitizes the Query portion of a URL. |
| [UrlQuerySanitizer.IllegalCharacterValueSanitizer](https://developer.android.com/reference/android/net/UrlQuerySanitizer.IllegalCharacterValueSanitizer) | Sanitize values based on which characters they contain. |
| [UrlQuerySanitizer.ParameterValuePair](https://developer.android.com/reference/android/net/UrlQuerySanitizer.ParameterValuePair) | A simple tuple that holds parameter-value pairs. |
| [VpnManager](https://developer.android.com/reference/android/net/VpnManager) | This class provides an interface for apps to manage platform VPN profiles Apps can use this API to provide profiles with which the platform can set up a VPN without further app intermediation. |
| [VpnProfileState](https://developer.android.com/reference/android/net/VpnProfileState) | Describe the state of VPN. |
| [VpnService](https://developer.android.com/reference/android/net/VpnService) | VpnService is a base class for applications to extend and build their own VPN solutions. |
| [VpnService.Builder](https://developer.android.com/reference/android/net/VpnService.Builder) | Helper class to create a VPN interface. |

## Enums

|  |  |
| --- | --- |
| [LocalSocketAddress.Namespace](https://developer.android.com/reference/android/net/LocalSocketAddress.Namespace) | The namespace that this address exists in. |
| [NetworkInfo.DetailedState](https://developer.android.com/reference/android/net/NetworkInfo.DetailedState) | *This enum was deprecated in API level 29. See `NetworkInfo`.* |
| [NetworkInfo.State](https://developer.android.com/reference/android/net/NetworkInfo.State) | *This enum was deprecated in API level 29. See `NetworkInfo`.* |

## Exceptions

|  |  |
| --- | --- |
| [DnsResolver.DnsException](https://developer.android.com/reference/android/net/DnsResolver.DnsException) | Class to represent DNS error |
| [IpSecManager.ResourceUnavailableException](https://developer.android.com/reference/android/net/IpSecManager.ResourceUnavailableException) | Thrown to indicate that an IPsec resource is unavailable. |
| [IpSecManager.SpiUnavailableException](https://developer.android.com/reference/android/net/IpSecManager.SpiUnavailableException) | Thrown to indicate that a requested SPI is in use. |
| [ParseException](https://developer.android.com/reference/android/net/ParseException) | Thrown when parsing failed. |

* ## Interfaces

  + [ConnectivityManager.OnNetworkActiveListener](https://developer.android.com/reference/android/net/ConnectivityManager.OnNetworkActiveListener)
  + [DnsResolver.Callback](https://developer.android.com/reference/android/net/DnsResolver.Callback)
  + [TetheringManager.StartTetheringCallback](https://developer.android.com/reference/android/net/TetheringManager.StartTetheringCallback)
  + [TetheringManager.StopTetheringCallback](https://developer.android.com/reference/android/net/TetheringManager.StopTetheringCallback)
  + [TetheringManager.TetheringEventCallback](https://developer.android.com/reference/android/net/TetheringManager.TetheringEventCallback)
  + [TransportInfo](https://developer.android.com/reference/android/net/TransportInfo)
  + [UrlQuerySanitizer.ValueSanitizer](https://developer.android.com/reference/android/net/UrlQuerySanitizer.ValueSanitizer)
* ## Classes

  + [CaptivePortal](https://developer.android.com/reference/android/net/CaptivePortal)
  + [ConnectivityDiagnosticsManager](https://developer.android.com/reference/android/net/ConnectivityDiagnosticsManager)
  + [ConnectivityDiagnosticsManager.ConnectivityDiagnosticsCallback](https://developer.android.com/reference/android/net/ConnectivityDiagnosticsManager.ConnectivityDiagnosticsCallback)
  + [ConnectivityDiagnosticsManager.ConnectivityReport](https://developer.android.com/reference/android/net/ConnectivityDiagnosticsManager.ConnectivityReport)
  + [ConnectivityDiagnosticsManager.DataStallReport](https://developer.android.com/reference/android/net/ConnectivityDiagnosticsManager.DataStallReport)
  + [ConnectivityManager](https://developer.android.com/reference/android/net/ConnectivityManager)
  + [ConnectivityManager.NetworkCallback](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback)
  + [Credentials](https://developer.android.com/reference/android/net/Credentials)
  + [DhcpInfo](https://developer.android.com/reference/android/net/DhcpInfo)
  + [DnsResolver](https://developer.android.com/reference/android/net/DnsResolver)
  + [EthernetNetworkSpecifier](https://developer.android.com/reference/android/net/EthernetNetworkSpecifier)
  + [Ikev2VpnProfile](https://developer.android.com/reference/android/net/Ikev2VpnProfile)
  + [Ikev2VpnProfile.Builder](https://developer.android.com/reference/android/net/Ikev2VpnProfile.Builder)
  + [InetAddresses](https://developer.android.com/reference/android/net/InetAddresses)
  + [IpConfiguration](https://developer.android.com/reference/android/net/IpConfiguration)
  + [IpConfiguration.Builder](https://developer.android.com/reference/android/net/IpConfiguration.Builder)
  + [IpPrefix](https://developer.android.com/reference/android/net/IpPrefix)
  + [IpSecAlgorithm](https://developer.android.com/reference/android/net/IpSecAlgorithm)
  + [IpSecManager](https://developer.android.com/reference/android/net/IpSecManager)
  + [IpSecManager.SecurityParameterIndex](https://developer.android.com/reference/android/net/IpSecManager.SecurityParameterIndex)
  + [IpSecManager.UdpEncapsulationSocket](https://developer.android.com/reference/android/net/IpSecManager.UdpEncapsulationSocket)
  + [IpSecTransform](https://developer.android.com/reference/android/net/IpSecTransform)
  + [IpSecTransform.Builder](https://developer.android.com/reference/android/net/IpSecTransform.Builder)
  + [IpSecTransformState](https://developer.android.com/reference/android/net/IpSecTransformState)
  + [IpSecTransformState.Builder](https://developer.android.com/reference/android/net/IpSecTransformState.Builder)
  + [L2capNetworkSpecifier](https://developer.android.com/reference/android/net/L2capNetworkSpecifier)
  + [L2capNetworkSpecifier.Builder](https://developer.android.com/reference/android/net/L2capNetworkSpecifier.Builder)
  + [LinkAddress](https://developer.android.com/reference/android/net/LinkAddress)
  + [LinkProperties](https://developer.android.com/reference/android/net/LinkProperties)
  + [LocalServerSocket](https://developer.android.com/reference/android/net/LocalServerSocket)
  + [LocalSocket](https://developer.android.com/reference/android/net/LocalSocket)
  + [LocalSocketAddress](https://developer.android.com/reference/android/net/LocalSocketAddress)
  + [MacAddress](https://developer.android.com/reference/android/net/MacAddress)
  + [MailTo](https://developer.android.com/reference/android/net/MailTo)
  + [Network](https://developer.android.com/reference/android/net/Network)
  + [NetworkCapabilities](https://developer.android.com/reference/android/net/NetworkCapabilities)
  + [NetworkInfo](https://developer.android.com/reference/android/net/NetworkInfo)
  + [NetworkRequest](https://developer.android.com/reference/android/net/NetworkRequest)
  + [NetworkRequest.Builder](https://developer.android.com/reference/android/net/NetworkRequest.Builder)
  + [NetworkSpecifier](https://developer.android.com/reference/android/net/NetworkSpecifier)
  + [PlatformVpnProfile](https://developer.android.com/reference/android/net/PlatformVpnProfile)
  + [Proxy](https://developer.android.com/reference/android/net/Proxy)
  + [ProxyInfo](https://developer.android.com/reference/android/net/ProxyInfo)
  + [RouteInfo](https://developer.android.com/reference/android/net/RouteInfo)
  + [SocketKeepalive](https://developer.android.com/reference/android/net/SocketKeepalive)
  + [SocketKeepalive.Callback](https://developer.android.com/reference/android/net/SocketKeepalive.Callback)
  + [SSLCertificateSocketFactory](https://developer.android.com/reference/android/net/SSLCertificateSocketFactory)
  + [SSLSessionCache](https://developer.android.com/reference/android/net/SSLSessionCache)
  + [StaticIpConfiguration](https://developer.android.com/reference/android/net/StaticIpConfiguration)
  + [StaticIpConfiguration.Builder](https://developer.android.com/reference/android/net/StaticIpConfiguration.Builder)
  + [TelephonyNetworkSpecifier](https://developer.android.com/reference/android/net/TelephonyNetworkSpecifier)
  + [TelephonyNetworkSpecifier.Builder](https://developer.android.com/reference/android/net/TelephonyNetworkSpecifier.Builder)
  + [TetheringInterface](https://developer.android.com/reference/android/net/TetheringInterface)
  + [TetheringManager](https://developer.android.com/reference/android/net/TetheringManager)
  + [TetheringManager.TetheringRequest](https://developer.android.com/reference/android/net/TetheringManager.TetheringRequest)
  + [TetheringManager.TetheringRequest.Builder](https://developer.android.com/reference/android/net/TetheringManager.TetheringRequest.Builder)
  + [TrafficStats](https://developer.android.com/reference/android/net/TrafficStats)
  + [Uri](https://developer.android.com/reference/android/net/Uri)
  + [Uri.Builder](https://developer.android.com/reference/android/net/Uri.Builder)
  + [UrlQuerySanitizer](https://developer.android.com/reference/android/net/UrlQuerySanitizer)
  + [UrlQuerySanitizer.IllegalCharacterValueSanitizer](https://developer.android.com/reference/android/net/UrlQuerySanitizer.IllegalCharacterValueSanitizer)
  + [UrlQuerySanitizer.ParameterValuePair](https://developer.android.com/reference/android/net/UrlQuerySanitizer.ParameterValuePair)
  + [VpnManager](https://developer.android.com/reference/android/net/VpnManager)
  + [VpnProfileState](https://developer.android.com/reference/android/net/VpnProfileState)
  + [VpnService](https://developer.android.com/reference/android/net/VpnService)
  + [VpnService.Builder](https://developer.android.com/reference/android/net/VpnService.Builder)
* ## Enums

  + [LocalSocketAddress.Namespace](https://developer.android.com/reference/android/net/LocalSocketAddress.Namespace)
  + [NetworkInfo.DetailedState](https://developer.android.com/reference/android/net/NetworkInfo.DetailedState)
  + [NetworkInfo.State](https://developer.android.com/reference/android/net/NetworkInfo.State)
* ## Exceptions

  + [DnsResolver.DnsException](https://developer.android.com/reference/android/net/DnsResolver.DnsException)
  + [IpSecManager.ResourceUnavailableException](https://developer.android.com/reference/android/net/IpSecManager.ResourceUnavailableException)
  + [IpSecManager.SpiUnavailableException](https://developer.android.com/reference/android/net/IpSecManager.SpiUnavailableException)
  + [ParseException](https://developer.android.com/reference/android/net/ParseException)
