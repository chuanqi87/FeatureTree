# VPN On Demand Rules

Set up VPN On Demand.

## Discussion

VPN On Demand allows the system to automatically start or stop a VPN connection based on various criteria. For example, you can use VPN On Demand to configure an iPhone to start a VPN connection when it’s on Wi-Fi and stop the connection when it’s on cellular. Or, you can start the VPN connection when an app tries to connect to a specific service that’s only available via VPN.

For more information, see “VPN On Demand” in [Apple Platform Deployment Guide](https://support.apple.com/guide/deployment/welcome/web).

## Topics

### Settings

[`NEOnDemandRuleConnect`](/documentation/NetworkExtension/NEOnDemandRuleConnect)

A VPN On Demand rule that connects the VPN.

[`NEOnDemandRuleDisconnect`](/documentation/NetworkExtension/NEOnDemandRuleDisconnect)

A VPN On Demand rule that disconnects the VPN.

[`NEOnDemandRuleIgnore`](/documentation/NetworkExtension/NEOnDemandRuleIgnore)

A VPN On Demand rule that doesn’t change the status of the VPN.

[`NEOnDemandRuleEvaluateConnection`](/documentation/NetworkExtension/NEOnDemandRuleEvaluateConnection)

A VPN On Demand rule that evaluate the app’s connection to determine whether to run its action.

[`NEOnDemandRule`](/documentation/NetworkExtension/NEOnDemandRule)

A base class shared by all VPN On Demand rules.

## See Also

[Personal VPN](/documentation/NetworkExtension/personal-vpn)

Create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2).

[Packet tunnel provider](/documentation/NetworkExtension/packet-tunnel-provider)

Implement a VPN client for a packet-oriented, custom VPN protocol.

[App proxy provider](/documentation/NetworkExtension/app-proxy-provider)

Implement a VPN client for a flow-oriented, custom VPN protocol.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
