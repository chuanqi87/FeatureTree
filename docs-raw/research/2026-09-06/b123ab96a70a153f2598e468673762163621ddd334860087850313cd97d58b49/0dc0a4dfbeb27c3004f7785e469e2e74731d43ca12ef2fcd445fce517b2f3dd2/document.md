# In-Provider Networking

Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.

## Discussion

NetworkExtension providers and hotspot helpers run in an unusual network environment that can cause problems for general-purpose networking APIs. For example, <doc://com.apple.documentation/documentation/Foundation/URLSession> typically sends requests via the default route, which is inappropriate for a hotspot helper that must always use the Wi-Fi interface. The NetworkExtension framework includes a number of APIs that are useful in such situations.

These APIs have the following key characteristics:

- They aren’t general-purpose APIs; they can only be used in the context of a NetworkExtension provider or hotspot helper.
- In many cases, you don’t need to use them. For example, it’s possible for a packet tunnel provider to use a general-purpose networking API, like BSD Sockets, for its tunnel connection.

The recommended general-purpose networking APIs are the <doc://com.apple.documentation/documentation/Foundation/url-loading-system> for HTTP and the <doc://com.apple.documentation/documentation/Network> framework for TCP and UDP.

## Topics

### TCP connections

[`NWTCPConnection`](/documentation/NetworkExtension/NWTCPConnection)

An object to manage a TCP connection, with or without TLS.

[`NWTLSParameters`](/documentation/NetworkExtension/NWTLSParameters)

TLS properties for creating a connection.

[`NWTCPConnectionAuthenticationDelegate`](/documentation/NetworkExtension/NWTCPConnectionAuthenticationDelegate)

A delegate protocol to customize the TLS authentication done by a connection.

### UDP sessions

[`NWUDPSession`](/documentation/NetworkExtension/NWUDPSession)

An object to manage a UDP session to a network endpoint.

### Endpoints

[`NWHostEndpoint`](/documentation/NetworkExtension/NWHostEndpoint)

A network endpoint specified by DNS name (or IP address) and port.

[`NWBonjourServiceEndpoint`](/documentation/NetworkExtension/NWBonjourServiceEndpoint)

A network endpoint specified as a Bonjour service name, type, and domain.

[`NWEndpoint`](/documentation/NetworkExtension/NWEndpoint)

An abstract base class, shared by [`NWHostEndpoint`](/documentation/NetworkExtension/NWHostEndpoint) or [`NWBonjourServiceEndpoint`](/documentation/NetworkExtension/NWBonjourServiceEndpoint), that represents the source or destination of a network connection.

### Network path information

[`NWPath`](/documentation/NetworkExtension/NWPath)

The path made by a network connection, including information about its viability.

## See Also

[Packet tunnel provider](/documentation/NetworkExtension/packet-tunnel-provider)

Implement a VPN client for a packet-oriented, custom VPN protocol.

[App proxy provider](/documentation/NetworkExtension/app-proxy-provider)

Implement a VPN client for a flow-oriented, custom VPN protocol.

[Hotspot helper](/documentation/NetworkExtension/hotspot-helper)

Integrate your app with the iOS hotspot network subsystem.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
