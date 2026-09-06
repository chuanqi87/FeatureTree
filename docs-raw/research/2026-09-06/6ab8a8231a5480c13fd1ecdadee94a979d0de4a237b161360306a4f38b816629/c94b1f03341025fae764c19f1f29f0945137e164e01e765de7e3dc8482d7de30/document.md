# Personal VPN

Create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2).

## Discussion

With the Personal VPN feature in macOS and iOS, your app can create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2). The user must explicitly authorize your app the first time it saves a VPN configuration.

> Note:
> Personal VPN only supports recommended VPN protocols; it doesn’t support legacy VPN protocols, like PPTP and L2TP.

Before starting with Personal VPN, verify that the client is compatible with your VPN server. Use Apple Configurator to create a configuration profile with a VPN payload for your server. If you can connect using the VPN configuration from your configuration profile, you should be able to connect using Personal VPN.

To get started, call the [`shared()`](/documentation/NetworkExtension/NEVPNManager/shared()) class method to access the [`NEVPNManager`](/documentation/NetworkExtension/NEVPNManager) singleton. Then load the VPN configuration by calling [`loadFromPreferences(completionHandler:)`](/documentation/NetworkExtension/NEVPNManager/loadFromPreferences(completionHandler:)); if you haven’t previously saved a configuration, this call returns an empty configuration. Modify this configuration as you see fit, and save it using [`saveToPreferences(completionHandler:)`](/documentation/NetworkExtension/NEVPNManager/saveToPreferences(completionHandler:)).

Once you’ve set up a Personal VPN configuration, you can connect and disconnect the VPN using the [`NEVPNConnection`](/documentation/NetworkExtension/NEVPNConnection) class. Use the [`connection`](/documentation/NetworkExtension/NEVPNManager/connection) property of [`NEVPNManager`](/documentation/NetworkExtension/NEVPNManager) to get the correct instance of that class.

Both iOS and macOS also support managed VPN, meaning VPN configurations installed by a configuration profile. Managed VPN configurations take precedence over Personal VPN configurations. If there’s simultaneously a managed VPN configuration and Personal VPN configuration, both configured to act as the default route, the managed tunnel serves as the default route.

> Note:
> When a VPN configuration is active, connections use the VPN instead of iCloud Private Relay. Network Extension providers also don’t use iCloud Private Relay.

## Topics

### Essentials

  <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.networking.vpn.api>

### VPN configuration

[`NEVPNManager`](/documentation/NetworkExtension/NEVPNManager)

An object to create and manage a Personal VPN configuration.

[`NEVPNProtocolIKEv2`](/documentation/NetworkExtension/NEVPNProtocolIKEv2)

Settings for an IKEv2 VPN configuration.

[`NEVPNProtocolIPSec`](/documentation/NetworkExtension/NEVPNProtocolIPSec)

Settings for an IPsec VPN configuration.

[`NEVPNProtocol`](/documentation/NetworkExtension/NEVPNProtocol)

Settings common to both IKEv2 and IPsec VPN configurations.

[VPN On Demand Rules](/documentation/NetworkExtension/vpn-on-demand-rules)

Set up VPN On Demand.

### VPN control

[`NEVPNConnection`](/documentation/NetworkExtension/NEVPNConnection)

An object to start and stop a Personal VPN connection and get its status.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
