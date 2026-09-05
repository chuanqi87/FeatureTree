* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/network#app-main)

Framework

# Network

Create network connections to send and receive data using transport and security protocols.

iOS 12.0+iPadOS 12.0+Mac Catalyst 13.0+macOS 10.14+tvOS 12.0+visionOS 1.0+watchOS 6.0+

## [Overview](https://developer.apple.com/documentation/network\#overview)

Use this framework when you need direct access to protocols like TLS, TCP, and UDP for your custom application protocols. Continue to use [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession), which is built upon this framework, for loading HTTP- and URL-based resources. For in-depth advice on where to start with networking, see [TN3151: Choosing the right networking API](https://developer.apple.com/documentation/technotes/tn3151-choosing-the-right-networking-api).

## [Topics](https://developer.apple.com/documentation/network\#topics)

### [Essentials](https://developer.apple.com/documentation/network\#Essentials)

[`enum NWEndpoint`](https://developer.apple.com/documentation/network/nwendpoint)

A local or remote endpoint in a network connection.

[`class NWParameters`](https://developer.apple.com/documentation/network/nwparameters)

An object that stores the protocols to use for connections, options for sending data, and network path constraints.

### [Connections and Listeners](https://developer.apple.com/documentation/network\#Connections-and-Listeners)

[`class NWConnection`](https://developer.apple.com/documentation/network/nwconnection)

A bidirectional data connection between a local endpoint and a remote endpoint.

[`class NWListener`](https://developer.apple.com/documentation/network/nwlistener)

An object you use to listen for incoming network connections.

[`class NWBrowser`](https://developer.apple.com/documentation/network/nwbrowser)

An object you use to browse for available network services.

[`class NWConnectionGroup`](https://developer.apple.com/documentation/network/nwconnectiongroup)

An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.

[`class NWEthernetChannel`](https://developer.apple.com/documentation/network/nwethernetchannel)

An object you use to send and receive custom Ethernet frames.

### [Network Protocols](https://developer.apple.com/documentation/network\#Network-Protocols)

Configure protocol options to use with connections and listeners, and inspect the results of protocol handshakes.

[Building a custom peer-to-peer protocol](https://developer.apple.com/documentation/network/building-a-custom-peer-to-peer-protocol)

Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.

[Connecting iPadOS and visionOS apps over the local network](https://developer.apple.com/documentation/visionos/connecting-ipados-and-visionos-apps-over-the-local-network)

Build an iPadOS companion app to control your visionOS app.

[`class NWProtocolTCP`](https://developer.apple.com/documentation/network/nwprotocoltcp)

A network protocol for connections that use the Transmission Control Protocol.

[`class NWProtocolTLS`](https://developer.apple.com/documentation/network/nwprotocoltls)

A network protocol for connections that use Transport Layer Security.

[`class NWProtocolQUIC`](https://developer.apple.com/documentation/network/nwprotocolquic)

A network protocol for connections that use the QUIC transport protocol.

[`class NWProtocolUDP`](https://developer.apple.com/documentation/network/nwprotocoludp)

A network protocol for connections that use the User Datagram Protocol.

[`class NWProtocolIP`](https://developer.apple.com/documentation/network/nwprotocolip)

A network protocol for configuring the Internet Protocol on connections.

[`class NWProtocolWebSocket`](https://developer.apple.com/documentation/network/nwprotocolwebsocket)

A network protocol for connections that use WebSocket.

[`class NWProtocolFramer`](https://developer.apple.com/documentation/network/nwprotocolframer)

A customizable network protocol for defining application message parsers.

### [Network Security and Privacy](https://developer.apple.com/documentation/network\#Network-Security-and-Privacy)

[API Reference\\
Security Options](https://developer.apple.com/documentation/network/security-options)

Configure security options for TLS handshakes.

[API Reference\\
Privacy Management](https://developer.apple.com/documentation/network/privacy-management)

Configure parameters related to user privacy.

[Creating an Identity for Local Network TLS](https://developer.apple.com/documentation/network/creating-an-identity-for-local-network-tls)

Learn how to create and use a digital identity in your application for local network TLS.

### [Paths and Interfaces](https://developer.apple.com/documentation/network\#Paths-and-Interfaces)

[`struct NWPath`](https://developer.apple.com/documentation/network/nwpath)

An object that contains information about the properties of the network that a connection uses, or that are available to your app.

[`class NWPathMonitor`](https://developer.apple.com/documentation/network/nwpathmonitor)

An observer that you use to monitor and react to network changes.

[`struct NWInterface`](https://developer.apple.com/documentation/network/nwinterface)

An interface that a network connection uses to send and receive data.

### [Errors](https://developer.apple.com/documentation/network\#Errors)

[`enum NWError`](https://developer.apple.com/documentation/network/nwerror)

The errors returned by objects in the Network framework.

### [Network Debugging](https://developer.apple.com/documentation/network\#Network-Debugging)

[Choosing a Network Debugging Tool](https://developer.apple.com/documentation/network/choosing-a-network-debugging-tool)

Decide which tool works best for your network debugging problem.

[Debugging HTTP Server-Side Errors](https://developer.apple.com/documentation/network/debugging-http-server-side-errors)

Understand HTTP server-side errors and how to debug them.

[Debugging HTTPS Problems with CFNetwork Diagnostic Logging](https://developer.apple.com/documentation/network/debugging-https-problems-with-cfnetwork-diagnostic-logging)

Use CFNetwork diagnostic logging to investigate HTTP and HTTPS problems.

[API Reference\\
Recording a Packet Trace](https://developer.apple.com/documentation/network/recording-a-packet-trace)

Learn how to record a low-level trace of network traffic.

[Taking Advantage of Third-Party Network Debugging Tools](https://developer.apple.com/documentation/network/taking-advantage-of-third-party-network-debugging-tools)

Learn about the available third-party network debugging tools.

[Testing and Debugging L4S in Your App](https://developer.apple.com/documentation/network/testing-and-debugging-l4s-in-your-app)

Learn how to verify your app on an L4S-capable host and network to improve your app’s responsiveness.

### [C-Language Symbols](https://developer.apple.com/documentation/network\#C-Language-Symbols)

Access Network framework symbols used in C.

[API Reference\\
C-Language Symbols](https://developer.apple.com/documentation/network/c-language-symbols)

### [Structures](https://developer.apple.com/documentation/network\#Structures)

[`struct nw_interface_radio_type_t`](https://developer.apple.com/documentation/network/nw_interface_radio_type_t)

[`struct nw_multipath_version_t`](https://developer.apple.com/documentation/network/nw_multipath_version_t)

[`struct nw_path_unsatisfied_reason_t`](https://developer.apple.com/documentation/network/nw_path_unsatisfied_reason_t)

[`struct nw_quic_stream_type_t`](https://developer.apple.com/documentation/network/nw_quic_stream_type_t)

[`struct Bonjour`](https://developer.apple.com/documentation/network/bonjour)

A browser that discovers Bonjour services.

[`struct BonjourListenerProvider`](https://developer.apple.com/documentation/network/bonjourlistenerprovider)

Advertise a Bonjour service.

[`struct Coder`](https://developer.apple.com/documentation/network/coder)

A protocol that frames and encodes/decodes Codable types.

[`struct DTLS`](https://developer.apple.com/documentation/network/dtls)

The system definition of the Datagram Transport Layer Security (DTLS) protocol.

Beta

[`struct DefaultProtocolStorage`](https://developer.apple.com/documentation/network/defaultprotocolstorage)

[`struct Framer`](https://developer.apple.com/documentation/network/framer)

An instance of a Framer protocol to load into a protocol stack.

[`struct IP`](https://developer.apple.com/documentation/network/ip)

The system definition of the Internet Protocol (IP).

[`struct NWParametersBuilder`](https://developer.apple.com/documentation/network/nwparametersbuilder)

An opaque class that is responsible for creating and configuring NWParameters based on the parameterized protocol stack.

[`struct NWTXTRecord`](https://developer.apple.com/documentation/network/nwtxtrecord)

A dictionary representing a TXT record in a DNS packet.

[`struct NetworkJSONCoder`](https://developer.apple.com/documentation/network/networkjsoncoder)

[`struct NetworkPropertyListCoder`](https://developer.apple.com/documentation/network/networkpropertylistcoder)

[`struct ProtocolMetadataBuilder`](https://developer.apple.com/documentation/network/protocolmetadatabuilder)

A resultBuilder for configuring metadata in send methods in a declarative way.

[`struct ProtocolStackBuilder`](https://developer.apple.com/documentation/network/protocolstackbuilder)

A resultBuilder for specifying and configuring protocol stacks in a declarative way

[`struct ProxyConfiguration`](https://developer.apple.com/documentation/network/proxyconfiguration)

A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.

[`struct QUIC`](https://developer.apple.com/documentation/network/quic)

The system definition of the QUIC protocol.

[`struct QUICDatagram`](https://developer.apple.com/documentation/network/quicdatagram)

Send and receive unreliable datagrams over QUIC via RFC 9221

[`struct QUICStream`](https://developer.apple.com/documentation/network/quicstream)

A QUIC stream that runs over a QUIC connection.

[`struct TCP`](https://developer.apple.com/documentation/network/tcp)

The system definition of the Transmission Control Protocol (TCP).

[`struct TLS`](https://developer.apple.com/documentation/network/tls)

The system definition of the Transport Layer Security (TLS) protocol.

[`struct TLV`](https://developer.apple.com/documentation/network/tlv)

A Type-Length-Value (TLV) framing protocol.

[`struct TXTRecordDecoder`](https://developer.apple.com/documentation/network/txtrecorddecoder)

[`struct UDP`](https://developer.apple.com/documentation/network/udp)

The system definition of the User Datagram Protocol (UDP).

[`struct UnexpectedEndpointType`](https://developer.apple.com/documentation/network/unexpectedendpointtype)

An error generated when an unexpected endpoint type is supplied.

[`struct WebSocket`](https://developer.apple.com/documentation/network/websocket)

The system definition of the WebSocket protocol.

[`struct nw_link_quality_t`](https://developer.apple.com/documentation/network/nw_link_quality_t)

### [Classes](https://developer.apple.com/documentation/network\#Classes)

[`class NWMultiplexGroup`](https://developer.apple.com/documentation/network/nwmultiplexgroup)

[`class NetworkBrowser`](https://developer.apple.com/documentation/network/networkbrowser)

Discover advertised services and devices on the network.

[`class NetworkChannel`](https://developer.apple.com/documentation/network/networkchannel)

A base class supporting sending and recieving data through an arbitrary network channel.

[`class NetworkConnection`](https://developer.apple.com/documentation/network/networkconnection)

Connect to an endpoint on the network to send and receive data.

[`class NetworkListener`](https://developer.apple.com/documentation/network/networklistener)

Listen for incoming network connections.

### [Reference](https://developer.apple.com/documentation/network\#Reference)

[API Reference\\
Network Constants](https://developer.apple.com/documentation/network/network-constants)

Access Network framework constants used in C.

[API Reference\\
Network Functions](https://developer.apple.com/documentation/network/network-functions)

Access Network framework functions used in C.

[API Reference\\
Network Data Types](https://developer.apple.com/documentation/network/network-data-types)

### [Protocols](https://developer.apple.com/documentation/network\#Protocols)

[`protocol BrowserProvider`](https://developer.apple.com/documentation/network/browserprovider)

BrowserProviders can be used when creating NetworkBrowsers.

[`protocol Connectable`](https://developer.apple.com/documentation/network/connectable)

Describes types that can be used to make NetworkConnections.

[`protocol ConnectionStorage`](https://developer.apple.com/documentation/network/connectionstorage)

Types that conform to ConnectionStorage can be used as additional storage within a connection.

[`protocol DatagramProtocol`](https://developer.apple.com/documentation/network/datagramprotocol)

Types that conform to DatagramProtocol send and receive messages with minimal or no metadata, usually constrained to a fixed maximum size.

[`protocol FramerProtocol`](https://developer.apple.com/documentation/network/framerprotocol)

Framer protocols allow custom framing and serialization of messages on a connection.

[`protocol ListenerProvider`](https://developer.apple.com/documentation/network/listenerprovider)

Extensible support for configuring advertise descriptors to define the service a listener should advertise.

[`protocol MessageProtocol`](https://developer.apple.com/documentation/network/messageprotocol)

Types that conform to MessageProtocol send and receive messages. The conforming type is responsible for specifying its message-specific metadata.

[`protocol MultiplexProtocol`](https://developer.apple.com/documentation/network/multiplexprotocol)

Types that conform to MultiplexProtocol are allowed to be the top protocol in a network protocol stack for multiplexing network connection objects.

[`protocol NWParametersProvider`](https://developer.apple.com/documentation/network/nwparametersprovider)

Types that conform to the NWParametersProvider protocol can be used to generate an NWParameters.

[`protocol NetworkCoder`](https://developer.apple.com/documentation/network/networkcoder)

[`protocol NetworkDecoder`](https://developer.apple.com/documentation/network/networkdecoder)

A type that conforms to the NetworkEncoder protocol can decode data to an Encodable object

[`protocol NetworkEncoder`](https://developer.apple.com/documentation/network/networkencoder)

A type that conforms to the NetworkEncoder protocol can encode a Encodable object to Data

[`protocol NetworkFixedWidthInteger`](https://developer.apple.com/documentation/network/networkfixedwidthinteger)

[`protocol NetworkMetadataProtocol`](https://developer.apple.com/documentation/network/networkmetadataprotocol)

Types that conform to NetworkProtocolOptions can be used when configuring protocol stacks.

[`protocol NetworkProtocolOptions`](https://developer.apple.com/documentation/network/networkprotocoloptions)

[`protocol OneToOneProtocol`](https://developer.apple.com/documentation/network/onetooneprotocol)

Types that conform to OneToOneProtocol are allowed to be the top protocol in a network protocol stack for non-multiplexed connections.

[`protocol StreamProtocol`](https://developer.apple.com/documentation/network/streamprotocol)

Types that conform to the StreamProtocol protocol expose methods for sending and receiving byte streams.

### [Variables](https://developer.apple.com/documentation/network\#Variables)

[`let kNWErrorDomainWiFiAware: CFString`](https://developer.apple.com/documentation/network/knwerrordomainwifiaware)

[`var nw_error_domain_wifi_aware: nw_error_domain_t`](https://developer.apple.com/documentation/network/nw_error_domain_wifi_aware)

[`var nw_link_quality_good: nw_link_quality_t`](https://developer.apple.com/documentation/network/nw_link_quality_good)

[`var nw_link_quality_minimal: nw_link_quality_t`](https://developer.apple.com/documentation/network/nw_link_quality_minimal)

[`var nw_link_quality_moderate: nw_link_quality_t`](https://developer.apple.com/documentation/network/nw_link_quality_moderate)

[`var nw_link_quality_unknown: nw_link_quality_t`](https://developer.apple.com/documentation/network/nw_link_quality_unknown)

### [Functions](https://developer.apple.com/documentation/network\#Functions)

[`func nw_parameters_get_allow_ultra_constrained(nw_parameters_t) -> Bool`](https://developer.apple.com/documentation/network/nw_parameters_get_allow_ultra_constrained(_:))

[`func nw_parameters_set_allow_ultra_constrained(nw_parameters_t, Bool)`](https://developer.apple.com/documentation/network/nw_parameters_set_allow_ultra_constrained(_:_:))

[`func nw_path_get_link_quality(nw_path_t) -> nw_link_quality_t`](https://developer.apple.com/documentation/network/nw_path_get_link_quality(_:))

[`func nw_path_is_ultra_constrained(nw_path_t) -> Bool`](https://developer.apple.com/documentation/network/nw_path_is_ultra_constrained(_:))

[`func nw_tcp_set_max_pacing_rate(nw_protocol_metadata_t, UInt64) -> Int32`](https://developer.apple.com/documentation/network/nw_tcp_set_max_pacing_rate(_:_:)) Beta

[`func withNetworkConnection<ApplicationProtocol>(to: NWEndpoint, using: () -> ApplicationProtocol, (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws`](https://developer.apple.com/documentation/network/withnetworkconnection(to:using:_:)-1sik8)

[`func withNetworkConnection<ApplicationProtocol>(to: NWEndpoint, using: () -> ApplicationProtocol, (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws`](https://developer.apple.com/documentation/network/withnetworkconnection(to:using:_:)-4wpc9)

[`func withNetworkConnection<ApplicationProtocol>(to: NWEndpoint, using: NWParametersBuilder<ApplicationProtocol>, (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws`](https://developer.apple.com/documentation/network/withnetworkconnection(to:using:_:)-7skhi)

[`func withNetworkConnection<ApplicationProtocol>(to: NWEndpoint, using: NWParametersBuilder<ApplicationProtocol>, (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws`](https://developer.apple.com/documentation/network/withnetworkconnection(to:using:_:)-887ho)

Current page is Network