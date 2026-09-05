* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/networkextension#app-main)

Framework

# Network Extension

Customize and extend core networking features.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.10+tvOS 17.0+visionOS 1.0+watchOS 7.0+

## [Overview](https://developer.apple.com/documentation/networkextension\#overview)

With the NetworkExtension framework, you can customize and extend the system’s core networking features. Specifically, you can:

- Change the system’s Wi-Fi configuration

- Integrate your app with the hotspot network subsystem (Hotspot Helper)

- Create and manage VPN configurations, using the built-in VPN protocols (Personal VPN) or a custom VPN protocol

- Create and manage network relay configurations

- Implement an on-device content filter

- Create and manage system-wide DNS configurations, using the built-in DNS protocols or a custom on-device DNS proxy


The NetworkExtension framework is available in macOS, iOS, tvOS, and visionOS, but not all features are available on all platforms and some features have specific restrictions (for example, some features only work on supervised iOS devices). The documentation for each feature describes these restrictions.

### [Options for implementing VPN](https://developer.apple.com/documentation/networkextension\#Options-for-implementing-VPN)

The NetworkExtension framework has extensive support for virtual private networks (VPN). A VPN is a form of network tunnel, where a VPN client uses the public Internet to create a connection to a VPN server and then passes private network traffic over that connection.

VPNs have many different uses. For example, an enterprise might set up a VPN to give remote employees access to enterprise network resources that are not available on the public Internet. Or a consumer wanting to access the Internet from an untrusted network, such as the free Wi-Fi at an airport, might set up VPN to secure their traffic.

The supported operating systems include a number of different VPN APIs, distinguished by the protocols they support:

- Use [Personal VPN](https://developer.apple.com/documentation/networkextension/personal-vpn) to create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2).

- Create a [Packet tunnel provider](https://developer.apple.com/documentation/networkextension/packet-tunnel-provider) to implement a VPN client for a packet-oriented, custom VPN protocol.

- Create an [App proxy provider](https://developer.apple.com/documentation/networkextension/app-proxy-provider) to implement a VPN client for a flow-oriented, custom VPN protocol.


### [About Always-on VPN](https://developer.apple.com/documentation/networkextension\#About-Always-on-VPN)

iOS supports Always-on VPN to ensure all IP traffic is tunneled back to the organization. See the [iOS Deployment Reference](https://support.apple.com/guide/deployment-reference-ios/always-on-vpn-iore8b083096/1/web/1) for information about how to configure Always-on VPN.

## [Topics](https://developer.apple.com/documentation/networkextension\#topics)

### [Wi-Fi management](https://developer.apple.com/documentation/networkextension\#Wi-Fi-management)

[API Reference\\
Wi-Fi configuration](https://developer.apple.com/documentation/networkextension/wi-fi-configuration)

Add persistent Wi-Fi configurations, or temporarily move the device to a specific Wi-Fi network.

[Configuring a Wi-Fi accessory to join a network](https://developer.apple.com/documentation/networkextension/configuring-a-wi-fi-accessory-to-join-a-network)

Associate an iOS device with an accessory’s network to deliver network configuration information.

[API Reference\\
Hotspot helper](https://developer.apple.com/documentation/networkextension/hotspot-helper)

Integrate your app with the iOS hotspot network subsystem.

### [Virtual private networks](https://developer.apple.com/documentation/networkextension\#Virtual-private-networks)

[Routing your VPN network traffic](https://developer.apple.com/documentation/networkextension/routing-your-vpn-network-traffic)

Configure your VPN to include and exclude some network traffic.

[API Reference\\
Personal VPN](https://developer.apple.com/documentation/networkextension/personal-vpn)

Create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2).

[API Reference\\
Packet tunnel provider](https://developer.apple.com/documentation/networkextension/packet-tunnel-provider)

Implement a VPN client for a packet-oriented, custom VPN protocol.

[API Reference\\
App proxy provider](https://developer.apple.com/documentation/networkextension/app-proxy-provider)

Implement a VPN client for a flow-oriented, custom VPN protocol.

### [Network relays](https://developer.apple.com/documentation/networkextension\#Network-relays)

[API Reference\\
Relays](https://developer.apple.com/documentation/networkextension/relays)

Create and manage a system-wide network relay configuration that uses built-in proxying for TCP and UDP traffic over HTTP/3 and HTTP/2.

### [Content filters](https://developer.apple.com/documentation/networkextension\#Content-filters)

[API Reference\\
Content filter providers](https://developer.apple.com/documentation/networkextension/content-filter-providers)

Create an on-device network content filter.

[Filtering Network Traffic](https://developer.apple.com/documentation/networkextension/filtering-network-traffic)

Use the Network Extension framework to allow or deny network connections.

### [URL filters](https://developer.apple.com/documentation/networkextension\#URL-filters)

[API Reference\\
URL filters](https://developer.apple.com/documentation/networkextension/url-filters)

Create a filter that analyzes full URLs, while preserving privacy.

### [DNS configurations](https://developer.apple.com/documentation/networkextension\#DNS-configurations)

[API Reference\\
DNS settings](https://developer.apple.com/documentation/networkextension/dns-settings)

Create and manage a system-wide DNS configuration that uses built-in encrypted DNS protocols.

[API Reference\\
DNS proxy provider](https://developer.apple.com/documentation/networkextension/dns-proxy-provider)

Create an on-device DNS proxy using a custom protocol.

### [Local networking](https://developer.apple.com/documentation/networkextension\#Local-networking)

[API Reference\\
Local push connectivity](https://developer.apple.com/documentation/networkextension/local-push-connectivity)

Provide functionality similar to Apple Push Notification Service when access to the wider internet is unavailable.

### [App extensions](https://developer.apple.com/documentation/networkextension\#App-extensions)

[`class NEAppExtensionConfiguration`](https://developer.apple.com/documentation/networkextension/neappextensionconfiguration)

A class that defines configuration options for use in NetworkExtension app extensions.

### [Protocols](https://developer.apple.com/documentation/networkextension\#Protocols)

[`protocol NEAppProxyUDPFlowHandling`](https://developer.apple.com/documentation/networkextension/neappproxyudpflowhandling)

### [Structures](https://developer.apple.com/documentation/networkextension\#Structures)

[`struct NETunnelProviderError`](https://developer.apple.com/documentation/networkextension/netunnelprovidererror-swift.struct)

An error that the tunnel provider encounters.

[`struct NEVPNError`](https://developer.apple.com/documentation/networkextension/nevpnerror-swift.struct)

Information about an error encountered while configuring or using a VPN.

### [Variables](https://developer.apple.com/documentation/networkextension\#Variables)

[`let NERelayClientErrorDomain: String`](https://developer.apple.com/documentation/networkextension/nerelayclienterrordomain)

### [Enumerations](https://developer.apple.com/documentation/networkextension\#Enumerations)

[`enum NERelayManagerClientError`](https://developer.apple.com/documentation/networkextension/nerelaymanagerclienterror)

Current page is Network Extension