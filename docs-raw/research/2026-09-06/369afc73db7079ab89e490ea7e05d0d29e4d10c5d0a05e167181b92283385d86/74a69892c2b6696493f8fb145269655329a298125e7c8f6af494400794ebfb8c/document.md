# Core Graphics

Harness the power of Quartz technology to perform lightweight 2D rendering with high-fidelity output. Handle path-based drawing, antialiased rendering, gradients, images, color management, PDF documents, and more.

## Overview

The Core Graphics framework is based on the Quartz advanced drawing engine. It provides low-level, lightweight 2D rendering with unmatched output fidelity. You use this framework to handle path-based drawing, transformations, color management, offscreen rendering, patterns, gradients and shadings, image data management, image creation, and image masking, as well as PDF document creation, display, and parsing.

In macOS, Core Graphics also includes services for working with display hardware, low-level user input events, and the windowing system.

## Topics

### Geometric Data Types

  <doc://com.apple.documentation/documentation/CoreFoundation/CGFloat-swift.struct>

  <doc://com.apple.documentation/documentation/CoreFoundation/CGPoint>

  <doc://com.apple.documentation/documentation/CoreFoundation/CGSize>

  <doc://com.apple.documentation/documentation/CoreFoundation/CGRect>

  <doc://com.apple.documentation/documentation/CoreFoundation/CGVector>

  <doc://com.apple.documentation/documentation/CoreFoundation/CGAffineTransform>

### Opaque Types

[`CGContext`](/documentation/CoreGraphics/CGContext)

A Quartz 2D drawing environment.

[`CGColor`](/documentation/CoreGraphics/CGColor)

A set of components that define a color, with a color space specifying how to interpret them.

[`CGColorConversionInfo`](/documentation/CoreGraphics/CGColorConversionInfo)

An object that describes how to convert between color spaces for use by other system services.

[`CGColorSpace`](/documentation/CoreGraphics/CGColorSpace)

A profile that specifies how to interpret a color value for display.

[`CGDataConsumer`](/documentation/CoreGraphics/CGDataConsumer)

An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.

[`CGDataProvider`](/documentation/CoreGraphics/CGDataProvider)

An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.

[`CGFont`](/documentation/CoreGraphics/CGFont)

A set of character glyphs and layout information for drawing text.

[`CGFunction`](/documentation/CoreGraphics/CGFunction)

A general facility for defining and using callback functions.

[`CGGradient`](/documentation/CoreGraphics/CGGradient)

A definition for a smooth transition between colors for drawing radial and axial gradient fills.

[`CGImage`](/documentation/CoreGraphics/CGImage)

A bitmap image or image mask.

[`CGLayer`](/documentation/CoreGraphics/CGLayer)

An offscreen context for reusing content drawn with Core Graphics.

[`CGPath`](/documentation/CoreGraphics/CGPath)

An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.

[`CGPattern`](/documentation/CoreGraphics/CGPattern)

A 2D pattern to be used for drawing graphics paths.

[CGPDFArray](/documentation/CoreGraphics/cgpdfarray)

An array structure within a PDF document.

[CGPDFContentStream](/documentation/CoreGraphics/cgpdfcontentstream)

A representation of one or more content data streams in a PDF page.

[CGPDFDictionary](/documentation/CoreGraphics/cgpdfdictionary)

A dictionary structure within a PDF document.

[`CGPDFDocument`](/documentation/CoreGraphics/CGPDFDocument)

A document that contains PDF (Portable Document Format) drawing information.

[CGPDFObject](/documentation/CoreGraphics/cgpdfobject)

An object representing content within a PDF document.

[CGPDFOperatorTable](/documentation/CoreGraphics/cgpdfoperatortable)

A set of callback functions for operators used when scanning content in a PDF document.

[`CGPDFPage`](/documentation/CoreGraphics/CGPDFPage)

A type that represents a page in a PDF document.

[CGPDFScanner](/documentation/CoreGraphics/cgpdfscanner)

A parser object for handling content and operators in a PDF content stream.

[CGPDFStream](/documentation/CoreGraphics/cgpdfstream)

A stream or sequence of data bytes in a PDF document.

[CGPDFString](/documentation/CoreGraphics/cgpdfstring)

A text string in a PDF document.

[`CGPSConverter`](/documentation/CoreGraphics/CGPSConverter)

An opaque data type used to convert PostScript data to PDF data.

[`CGShading`](/documentation/CoreGraphics/CGShading)

A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.

### 2D Drawing

[`CGContext`](/documentation/CoreGraphics/CGContext)

A Quartz 2D drawing environment.

[`CGImage`](/documentation/CoreGraphics/CGImage)

A bitmap image or image mask.

[`CGPath`](/documentation/CoreGraphics/CGPath)

An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.

[`CGMutablePath`](/documentation/CoreGraphics/CGMutablePath)

A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.

[`CGLayer`](/documentation/CoreGraphics/CGLayer)

An offscreen context for reusing content drawn with Core Graphics.

### Colors and Fonts

[`CGColor`](/documentation/CoreGraphics/CGColor)

A set of components that define a color, with a color space specifying how to interpret them.

[`CGColorConversionInfo`](/documentation/CoreGraphics/CGColorConversionInfo)

An object that describes how to convert between color spaces for use by other system services.

[`CGColorSpace`](/documentation/CoreGraphics/CGColorSpace)

A profile that specifies how to interpret a color value for display.

[`CGFont`](/documentation/CoreGraphics/CGFont)

A set of character glyphs and layout information for drawing text.

### Working with PDF Documents

[`CGPDFDocument`](/documentation/CoreGraphics/CGPDFDocument)

A document that contains PDF (Portable Document Format) drawing information.

### Utility and Support Classes

[`CGDataConsumer`](/documentation/CoreGraphics/CGDataConsumer)

An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.

[`CGDataProvider`](/documentation/CoreGraphics/CGDataProvider)

An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.

[`CGShading`](/documentation/CoreGraphics/CGShading)

A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.

[`CGGradient`](/documentation/CoreGraphics/CGGradient)

A definition for a smooth transition between colors for drawing radial and axial gradient fills.

[`CGFunction`](/documentation/CoreGraphics/CGFunction)

A general facility for defining and using callback functions.

[`CGPattern`](/documentation/CoreGraphics/CGPattern)

A 2D pattern to be used for drawing graphics paths.

### Services

[Quartz Display Services](/documentation/CoreGraphics/quartz-display-services)

Provides direct access to features in the macOS window server for configuring and controlling display hardware.

[Quartz Event Services](/documentation/CoreGraphics/quartz-event-services)

Provides features for managing *event taps*—filters for observing and altering the stream of low-level user input events in macOS.

[Quartz Window Services](/documentation/CoreGraphics/quartz-window-services)

Provides information about the windows managed by the macOS window server.

### Reference

[CGAffineTransform](/documentation/CoreGraphics/cgaffinetransform)

An affine transformation matrix for use in drawing 2D graphics.

[CGGeometry](/documentation/CoreGraphics/cggeometry)

Various structures and associated functions for 2D geometric primitives.

[Core Graphics Structures](/documentation/CoreGraphics/core-graphics-structures)

[Core Graphics Enumerations](/documentation/CoreGraphics/core-graphics-enumerations)

[Core Graphics Constants](/documentation/CoreGraphics/core-graphics-constants)

[Core Graphics Functions](/documentation/CoreGraphics/core-graphics-functions)

[Core Graphics Data Types](/documentation/CoreGraphics/core-graphics-data-types)

[Core Graphics Macros](/documentation/CoreGraphics/core-graphics-macros)

### Reference

[Core Graphics Structures](/documentation/CoreGraphics/core-graphics-structures)

[Core Graphics Enumerations](/documentation/CoreGraphics/core-graphics-enumerations)

[Core Graphics Constants](/documentation/CoreGraphics/core-graphics-constants)

[Core Graphics Functions](/documentation/CoreGraphics/core-graphics-functions)

[Core Graphics Data Types](/documentation/CoreGraphics/core-graphics-data-types)

## See Also

  [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
