# Network Extension

Customize and extend core networking features.

## Overview

With the NetworkExtension framework, you can customize and extend the system’s core networking features. Specifically, you can:

- Change the system’s Wi-Fi configuration
- Integrate your app with the hotspot network subsystem (Hotspot Helper)
- Create and manage VPN configurations, using the built-in VPN protocols (Personal VPN) or a custom VPN protocol
- Create and manage network relay configurations
- Implement an on-device content filter
- Create and manage system-wide DNS configurations, using the built-in DNS protocols or a custom on-device DNS proxy

The NetworkExtension framework is available in macOS, iOS, tvOS, and visionOS, but not all features are available on all platforms and some features have specific restrictions (for example, some features only work on supervised iOS devices). The documentation for each feature describes these restrictions.

### Options for implementing VPN

The NetworkExtension framework has extensive support for virtual private networks (VPN).  A VPN is a form of network tunnel, where a VPN client uses the public Internet to create a connection to a VPN server and then passes private network traffic over that connection.

VPNs have many different uses.  For example, an enterprise might set up a VPN to give remote employees access to enterprise network resources that are not available on the public Internet.  Or a consumer wanting to access the Internet from an untrusted network, such as the free Wi-Fi at an airport, might set up VPN to secure their traffic.

The supported operating systems include a number of different VPN APIs, distinguished by the protocols they support:

- Use [Personal VPN](/documentation/NetworkExtension/personal-vpn) to create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2).
- Create a [Packet tunnel provider](/documentation/NetworkExtension/packet-tunnel-provider) to implement a VPN client for a packet-oriented, custom VPN protocol.
- Create an [App proxy provider](/documentation/NetworkExtension/app-proxy-provider) to implement a VPN client for a flow-oriented, custom VPN protocol.

### About Always-on VPN

iOS supports Always-on VPN to ensure all IP traffic is tunneled back to the organization. See the [iOS Deployment Reference](https://support.apple.com/guide/deployment-reference-ios/always-on-vpn-iore8b083096/1/web/1) for information about how to configure Always-on VPN.

## Topics

### Wi-Fi management

[Wi-Fi configuration](/documentation/NetworkExtension/wi-fi-configuration)

Add persistent Wi-Fi configurations, or temporarily move the device to a specific Wi-Fi network.

[Configuring a Wi-Fi accessory to join a network](/documentation/NetworkExtension/configuring-a-wi-fi-accessory-to-join-a-network)

Associate an iOS device with an accessory’s network to deliver network configuration information.

[Hotspot helper](/documentation/NetworkExtension/hotspot-helper)

Integrate your app with the iOS hotspot network subsystem.

### Virtual private networks

[Routing your VPN network traffic](/documentation/NetworkExtension/routing-your-vpn-network-traffic)

Configure your VPN to include and exclude some network traffic.

[Personal VPN](/documentation/NetworkExtension/personal-vpn)

Create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2).

[Packet tunnel provider](/documentation/NetworkExtension/packet-tunnel-provider)

Implement a VPN client for a packet-oriented, custom VPN protocol.

[App proxy provider](/documentation/NetworkExtension/app-proxy-provider)

Implement a VPN client for a flow-oriented, custom VPN protocol.

### Network relays

[Relays](/documentation/NetworkExtension/relays)

Create and manage a system-wide network relay configuration that uses built-in proxying for TCP and UDP traffic over HTTP/3 and HTTP/2.

### Content filters

[Content filter providers](/documentation/NetworkExtension/content-filter-providers)

Create an on-device network content filter.

[Filtering Network Traffic](/documentation/NetworkExtension/filtering-network-traffic)

Use the Network Extension framework to allow or deny network connections.

### Content filters

[Content filter providers](/documentation/NetworkExtension/content-filter-providers)

Create an on-device network content filter.

### URL filters

[URL filters](/documentation/NetworkExtension/url-filters)

Create a filter that analyzes full URLs, while preserving privacy.

### DNS configurations

[DNS settings](/documentation/NetworkExtension/dns-settings)

Create and manage a system-wide DNS configuration that uses built-in encrypted DNS protocols.

[DNS proxy provider](/documentation/NetworkExtension/dns-proxy-provider)

Create an on-device DNS proxy using a custom protocol.

### Local networking

[Local push connectivity](/documentation/NetworkExtension/local-push-connectivity)

Provide functionality similar to Apple Push Notification Service when access to the wider internet is unavailable.

### App extensions

[`NEAppExtensionConfiguration`](/documentation/NetworkExtension/NEAppExtensionConfiguration)

A class that defines configuration options for use in NetworkExtension app extensions.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
