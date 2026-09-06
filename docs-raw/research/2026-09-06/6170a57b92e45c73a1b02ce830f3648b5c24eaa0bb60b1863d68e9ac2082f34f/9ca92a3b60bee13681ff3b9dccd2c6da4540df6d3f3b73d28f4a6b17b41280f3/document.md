# Wi-Fi configuration

Add persistent Wi-Fi configurations, or temporarily move the device to a specific Wi-Fi network.

## Discussion

Using [`NEHotspotConfigurationManager`](/documentation/NetworkExtension/NEHotspotConfigurationManager), you can programmatically create two different types of Wi-Fi configurations:

- Persistent configurations, which are equivalent to the user joining a Wi-Fi network using the Settings app
- Join-once configurations, which temporarily move the device to a specific Wi-Fi network

The user must explicitly authorize both of these operations.

This API can help with a wide variety of tasks. For example, you can use it to help a user join a specific Wi-Fi network, like the hotspot at a local coffee shop, or to set up an accessory that uses Wi-Fi.

[`NEHotspotConfigurationManager`](/documentation/NetworkExtension/NEHotspotConfigurationManager) supports a variety of authentication models:

- SSID with no authentication
- SSID with password-based authentication (WEP, WPA, and WPA2)
- SSID with EAP authentication
- Hotspot 2.0 with EAP authentication

[`NEHotspotConfigurationManager`](/documentation/NetworkExtension/NEHotspotConfigurationManager) is only supported on iOS. For macOS, use the <doc://com.apple.documentation/documentation/CoreWLAN> framework, which provides a full-featured Wi-Fi configuration and management API.

## Topics

### Essentials

  <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.networking.HotspotConfiguration>

### Wi-Fi network configuration

[`NEHotspotConfigurationManager`](/documentation/NetworkExtension/NEHotspotConfigurationManager)

A manager that applies and removes hotspot configurations of Wi-Fi networks.

[`NEHotspotConfiguration`](/documentation/NetworkExtension/NEHotspotConfiguration)

Configuration settings for a Wi-Fi network.

[`NEHotspotEAPSettings`](/documentation/NetworkExtension/NEHotspotEAPSettings)

Extensible Authentication Protocol settings for configuring WPA and WPA2 enterprise Wi-Fi networks.

[`NEHotspotHS20Settings`](/documentation/NetworkExtension/NEHotspotHS20Settings)

Settings for configuring Hotspot 2.0 Wi-Fi networks.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
