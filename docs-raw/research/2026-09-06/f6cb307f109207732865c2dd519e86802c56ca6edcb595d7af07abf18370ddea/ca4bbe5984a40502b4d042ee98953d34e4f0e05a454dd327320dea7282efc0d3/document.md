# Matter

Communicate with and control smart home devices from a variety of manufacturers.

## Overview

The [Matter](https://csa-iot.org/all-solutions/matter/) smart home connectivity standard enables interoperability between various smart home devices and ecosystems. Use  <doc://com.apple.documentation/documentation/MatterSupport>  to bring accessories onto a local network, then commission and control those accessories using Matter.

![A diagram showing communication between Matter and non-Matter devices within a home. At the center is a Matter-enabled iOS device that connects to a Matter garage door controller on the left and a Matter light switch on the right. The Matter light switch connects to a Matter lamp controller. There are also non-Matter devices in the diagram: an outlet switch, a HomePod, and an Apple TV.](images/com.apple.matter/media-4199669@2x.png)

To access a Matter accessory on a network, you must commission it. Commissioning provides credentials to enable secure communication and performs initial accessory configuration. Once you commission an accessory, it exposes areas of functionality called clusters that you use to control it. For example, a light exposes the On/Off cluster to control whether it’s on or off. A dimmable light also exposes the Level Control cluster to control its brightness.

## Topics

### Matter device onboarding

[Onboarding a Matter device](/documentation/Matter/onboarding-a-matter-device)

Prepare your app to discover and control a Matter device.

### Matter device interactions

[Controller initialization](/documentation/Matter/controller-initialization)

Initialize the object that controls Matter accessories.

[Accessory commissioning](/documentation/Matter/accessory-commissioning)

Commission a Matter accessory onto a network.

[Accessory control](/documentation/Matter/accessory-control)

Communicate with commissioned Matter accessories.

[Clusters](/documentation/Matter/clusters)

Interact with groups of related functionality that Matter accessories expose.

### Reference

[Other symbols](/documentation/Matter/other-symbols)

[Matter Constants](/documentation/Matter/matter-constants)

[Matter Functions](/documentation/Matter/matter-functions)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
