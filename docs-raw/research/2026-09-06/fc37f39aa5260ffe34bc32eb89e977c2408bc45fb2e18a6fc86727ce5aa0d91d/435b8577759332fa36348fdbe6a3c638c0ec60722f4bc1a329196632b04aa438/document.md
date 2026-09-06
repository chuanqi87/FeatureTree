# PKDrawing

A structure representing the drawing information captured by a canvas view.

```
struct PKDrawing
```

## Overview

A [`PKDrawing`](/documentation/PencilKit/PKDrawing-swift.struct) object stores the user-drawn content from a [`PKCanvasView`](/documentation/PencilKit/PKCanvasView) object. You use drawing objects to store the data associated with your user’s drawings. You can save this data with the rest of your app’s content, and you can use that saved data to create a new drawing object later. You can also generate an image based on the drawn content that you can copy to the pasteboard, save to disk, or share.

## Topics

### Creating a drawing object

[`init(strokes:)`](/documentation/PencilKit/PKDrawing-swift.struct/init(strokes:))

Creates a drawing object and populates it with a sequence of strokes the user provides.

[`init(data:)`](/documentation/PencilKit/PKDrawing-swift.struct/init(data:))

Creates a drawing object and populates it with previously drawn content.

[`init()`](/documentation/PencilKit/PKDrawing-swift.struct/init())

Creates an empty drawing object.

### Getting the canvas bounds

[`bounds`](/documentation/PencilKit/PKDrawing-swift.struct/bounds)

The smallest rectangle used to represent the content’s bounds, taking into account line widths of that content.

### Generating an image

[`image(from:scale:)`](/documentation/PencilKit/PKDrawing-swift.struct/image(from:scale:)-220d0)

Returns an image object that contains the specified portion of the drawing.

[`image(from:scale:)`](/documentation/PencilKit/PKDrawing-swift.struct/image(from:scale:)-6p3zc)

Returns an image object that contains the specified portion of the drawing.

### Getting the drawing data

[`strokes`](/documentation/PencilKit/PKDrawing-swift.struct/strokes)

The array of strokes that make up the drawing.

[`dataRepresentation()`](/documentation/PencilKit/PKDrawing-swift.struct/dataRepresentation())

Returns a raw data representation of the rendered content.

[`PKAppleDrawingTypeIdentifier`](/documentation/PencilKit/PKAppleDrawingTypeIdentifier)

The uniform type identifier for data associated with a drawing object.

### Modifying the drawing

[`transform(using:)`](/documentation/PencilKit/PKDrawing-swift.struct/transform(using:))

Applies the specified transform to the contents of this drawing.

[`transformed(using:)`](/documentation/PencilKit/PKDrawing-swift.struct/transformed(using:))

Applies the specified transform and returns a new drawing.

[`append(_:)`](/documentation/PencilKit/PKDrawing-swift.struct/append(_:))

Appends the contents of the specified drawing object to an existing drawing object that you provide.

[`appending(_:)`](/documentation/PencilKit/PKDrawing-swift.struct/appending(_:))

Returns a new drawing created by appending the current drawing with another drawing you provide.

### Erasing strokes

### Encoding the drawing object

### Supporting backward compatibility

[`requiredContentVersion`](/documentation/PencilKit/PKDrawing-swift.struct/requiredContentVersion)

The version of PencilKit necessary to use the drawing.

### Comparing drawing objects

### Using reference types

[`PKDrawingReference`](/documentation/PencilKit/PKDrawingReference)

A data structure that contains the drawing information captured by a canvas view.

## Relationships

### Conforms To

[`Escapable`](/documentation/Swift/Escapable)

[`Equatable`](/documentation/Swift/Equatable)

[`Sendable`](/documentation/Swift/Sendable)

[`Copyable`](/documentation/Swift/Copyable)

[`SendableMetatype`](/documentation/Swift/SendableMetatype)

[`Encodable`](/documentation/Swift/Encodable)

[`Decodable`](/documentation/Swift/Decodable)

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
