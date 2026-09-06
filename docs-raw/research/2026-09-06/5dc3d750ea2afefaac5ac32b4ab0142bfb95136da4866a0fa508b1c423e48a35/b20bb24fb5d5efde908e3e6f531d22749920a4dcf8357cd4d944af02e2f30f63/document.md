# ColorSync

Reproduce colors accurately across a range of input, output, and display devices.

## Overview

ColorSync is the color-management engine on Apple platforms. For most apps, color management happens automatically through higher-level frameworks such as
<doc://com.apple.documentation/documentation/CoreGraphics> and <doc://com.apple.documentation/documentation/CoreImage>. Use ColorSync directly when your app needs to manage color itself; for example,
a professional photo, print, or video app that builds custom transforms, or a tool that inspects and
calibrates the profiles assigned to devices and displays.

> Note: To pass a profile to Core Graphics, create a
> <doc://com.apple.documentation/documentation/CoreGraphics/CGColorSpace> from a ``doc://com.apple.colorsync/documentation/ColorSync/ColorSyncProfile`` with
> <doc://com.apple.documentation/documentation/CoreGraphics/CGColorSpaceCreateWithColorSyncProfile(_:_:)>.

A [`ColorSyncProfile`](/documentation/ColorSync/ColorSyncProfile) describes the
color behavior of a device or a working color space, and a [`ColorSyncTransform`](/documentation/ColorSync/ColorSyncTransform) converts color from
one profile to another. Use ColorSync to match color across color spaces and to read, author, and
embed the International Color Consortium (ICC) profiles that describe them. You can also create
Headroom Adaptive Gain Curve (HAGC) metadata, which controls how the system adapts HDR content when a display
can’t show its full brightness range.

## Topics

### Color conversion

[Color transforms](/documentation/ColorSync/color-transforms)

Convert color from one profile’s color space to another.

[Pixel format and data layout](/documentation/ColorSync/pixel-format)

Describe the memory layout of the pixel buffers a color transform reads and writes.

### Profile and HDR metadata

[Color profiles](/documentation/ColorSync/color-profiles)

Work with the ICC profiles that describe device and working color spaces.

[Headroom Adaptive Gain Curve](/documentation/ColorSync/headroom-adaptive-gain-curve)

Work with SMPTE ST 2094-50 tone-mapping metadata shared between HDR stills and video.

### System color management

[Color devices](/documentation/ColorSync/color-devices)

Manage the color profiles assigned to displays, printers, scanners, and cameras.

[Color management modules](/documentation/ColorSync/color-management-modules)

Work with the Color Management Modules that perform color conversions.

### Supporting types and conventions

[Supporting types and conventions](/documentation/ColorSync/supporting-types-and-conventions)

Reference the signatures and conventions that support the color-management APIs.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
