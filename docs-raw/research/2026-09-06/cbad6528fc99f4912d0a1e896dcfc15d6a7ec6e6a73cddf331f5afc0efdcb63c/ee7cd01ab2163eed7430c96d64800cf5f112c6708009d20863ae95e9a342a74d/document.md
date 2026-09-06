# Hotspot helper

Integrate your app with the iOS hotspot network subsystem.

## Discussion

[`NEHotspotHelper`](/documentation/NetworkExtension/NEHotspotHelper) allows your app to participate in the process of authenticating with hotspot networks, that is, Wi-Fi networks where the user must interact with the network to gain access to the wider Internet. Hotspot helpers are only supported on iOS.

> Important:
> ``doc://com.apple.networkextension/documentation/NetworkExtension/NEHotspotHelper`` is *only* useful for hotspot integration. There are both technical and business restrictions that prevent it from being used for other tasks, such as accessory integration or Wi-Fi based location. Before using ``doc://com.apple.networkextension/documentation/NetworkExtension/NEHotspotHelper``, you must first be granted a special entitlement (`com.apple.developer.networking.HotspotHelper`) by Apple. For more information, see [Hotspot Helper Request](https://developer.apple.com/contact/request/network-extension/).

For more about creating a hotspot helper, see the [Hotspot Network Subsystem Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/Hotspot_Network_Subsystem_Guide/Contents/Introduction.html#//apple_ref/doc/uid/TP40016639).

## Topics

### Registration

[`NEHotspotHelper`](/documentation/NetworkExtension/NEHotspotHelper)

A class to register a hotspot helper.

### Commands

[`NEHotspotHelperCommand`](/documentation/NetworkExtension/NEHotspotHelperCommand)

A command for the hotspot helper to handle.

[`NEHotspotHelperResponse`](/documentation/NetworkExtension/NEHotspotHelperResponse)

The hotspot helper’s response to a command.

[`NEHotspotNetwork`](/documentation/NetworkExtension/NEHotspotNetwork)

Information about a Wi-Fi network associated with a command or a response.

### Hotspot communication

Hotspot helpers can use these APIs to communicate with the hotspot even when Wi-Fi is not the default route.

  <doc://com.apple.documentation/documentation/Foundation/NSMutableURLRequest/bind(to:)>

[In-Provider Networking](/documentation/NetworkExtension/in-provider-networking)

Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.

### Hotspot helper extension

Implement hotspot evaluation and authentication in an app extension for better performance and security.

[`NEHotspotManager`](/documentation/NetworkExtension/NEHotspotManager)

A class that you use to enable or disable the hotspot evaluation and authentication provider extensions.

[`NEHotspotEvaluationProvider`](/documentation/NetworkExtension/NEHotspotEvaluationProvider)

A protocol that defines methods and properties your extension implements to handle evaluate and filter scan list commands.

[`NEHotspotAuthenticationProvider`](/documentation/NetworkExtension/NEHotspotAuthenticationProvider)

A protocol that defines methods that your extension adopts to start and stop the extension, and to handle commands to authenticate with the hotspot network.

[`NEHotspotEvaluationProviderConfiguration`](/documentation/NetworkExtension/NEHotspotEvaluationProviderConfiguration)

A class that defines configuration options for use in NetworkExtension evaluation providers.

[`NEHotspotAuthenticationProviderConfiguration`](/documentation/NetworkExtension/NEHotspotAuthenticationProviderConfiguration)

A class that defines configuration options for use in NetworkExtension authentication providers.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
