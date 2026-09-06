# PencilKit

Capture touch and Apple Pencil input as a drawing, and display that content from your app.

## Overview

PencilKit makes it easy to incorporate hand-drawn content into your iPadOS or macOS apps. PencilKit provides a drawing environment for your iOS app that receives input from Apple Pencil or the user’s finger, and turns it into images you display in iPadOS, iOS, or macOS. The environment comes with tools for creating, erasing, and selecting lines.

You capture content in your iPad app using a [`PKCanvasView`](/documentation/PencilKit/PKCanvasView) object that you integrate into your existing view hierarchy. It supports the low-latency capture of touches originating from Apple Pencil or your finger. The canvas object sends final results as a [`PKDrawing`](/documentation/PencilKit/PKDrawing-swift.struct) object, whose contents you can save with your app’s content. You can also convert the drawn content into an image for display in iOS or macOS app.

For information about handling user interactions on Apple Pencil in your UIKit app, see <doc://com.apple.documentation/documentation/UIKit/apple-pencil-interactions>.

## Topics

### Canvas

[Drawing with PencilKit](/documentation/PencilKit/drawing-with-pencilkit)

Add expressive, low-latency drawing to your app using PencilKit.

[Customizing Scribble with Interactions](/documentation/PencilKit/customizing-scribble-with-interactions)

Enable writing on a non-text-input view by adding interactions.

[Inspecting, Modifying, and Constructing PencilKit Drawings](/documentation/PencilKit/inspecting-modifying-and-constructing-pencilkit-drawings)

Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.

[Importing Bézier path data into PencilKit](/documentation/PencilKit/importing-external-drawing-data-into-pencilkit)

Convert existing Bézier-based stroke data into PencilKit drawing strokes.

[Controlling stroke rendering for animation and editing](/documentation/PencilKit/controlling-stroke-rendering-for-animation-and-editing)

Slice, animate, and blend PencilKit strokes in code, while keeping grain texture and wet ink intact.

[`PKCanvasView`](/documentation/PencilKit/PKCanvasView)

A view that captures Apple Pencil input and displays the rendered results in an iOS app.

[`PKDrawing`](/documentation/PencilKit/PKDrawing-swift.struct)

A structure representing the drawing information captured by a canvas view.

[`PKStroke`](/documentation/PencilKit/PKStroke-swift.struct)

A structure that represents the paths, boundaries, and other properties of a stroke drawn on a canvas.

[`PKStrokePath`](/documentation/PencilKit/PKStrokePath-swift.struct)

A structure that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.

[`PKStrokePoint`](/documentation/PencilKit/PKStrokePoint-swift.struct)

A structure that represents the properties of a specific point along a stroke’s path.

[`PKInk`](/documentation/PencilKit/PKInk-swift.struct)

A structure that represents an ink that specifies its type, color, and width.

### Canvas

[Drawing with PencilKit](/documentation/PencilKit/drawing-with-pencilkit)

Add expressive, low-latency drawing to your app using PencilKit.

[Customizing Scribble with Interactions](/documentation/PencilKit/customizing-scribble-with-interactions)

Enable writing on a non-text-input view by adding interactions.

[Inspecting, Modifying, and Constructing PencilKit Drawings](/documentation/PencilKit/inspecting-modifying-and-constructing-pencilkit-drawings)

Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.

[Importing Bézier path data into PencilKit](/documentation/PencilKit/importing-external-drawing-data-into-pencilkit)

Convert existing Bézier-based stroke data into PencilKit drawing strokes.

[Controlling stroke rendering for animation and editing](/documentation/PencilKit/controlling-stroke-rendering-for-animation-and-editing)

Slice, animate, and blend PencilKit strokes in code, while keeping grain texture and wet ink intact.

[`PKCanvasView`](/documentation/PencilKit/PKCanvasView)

A view that captures Apple Pencil input and displays the rendered results in an iOS app.

[`PKDrawingReference`](/documentation/PencilKit/PKDrawingReference)

A data structure that contains the drawing information captured by a canvas view.

[`PKStrokeReference`](/documentation/PencilKit/PKStrokeReference)

A class that represents the paths, boundaries and other properties of a stroke drawn on a canvas.

[`PKStrokePathReference`](/documentation/PencilKit/PKStrokePathReference)

A class that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.

[`PKStrokePointReference`](/documentation/PencilKit/PKStrokePointReference)

A class that represents the properties of a specific point along a stroke’s path.

[`PKInkReference`](/documentation/PencilKit/PKInkReference)

Provides a description of the creation and rendering of marks on a canvas.

[`PKStrokeRenderStateReference`](/documentation/PencilKit/PKStrokeRenderStateReference)

An object that captures the render-time state of a stroke, such as grain texture position.

[`PKConvertedBezierPointReference`](/documentation/PencilKit/PKConvertedBezierPointReference)

An object that provides information about a B-spline control point converted from a Bézier path.

[`PKFloatRange`](/documentation/PencilKit/PKFloatRange)

A utility class that represents range components of a stroke.

[`PKInkTypeReed`](/documentation/PencilKit/PKInkTypeReed)

### Handwriting recognition

[Building a handwriting recognition experience with PencilKit](/documentation/PencilKit/building-a-handwriting-recognition-experience-with-pencilkit)

Integrate handwriting recognition into your app to identify written text across multiple languages, and explore path conversion and substrokes to enhance the drawing experience.

[Recognizing handwriting and converting it to text](/documentation/PencilKit/recognizing-handwriting-and-converting-to-text)

Analyze handwritten strokes in a PencilKit canvas using on-device recognition, and convert them to text that your app can display, copy, or index.

[`PKStrokeRecognizer`](/documentation/PencilKit/PKStrokeRecognizer)

An actor that recognizes handwriting and searches for text within a PencilKit drawing.

### Handwriting recognition

[Building a handwriting recognition experience with PencilKit](/documentation/PencilKit/building-a-handwriting-recognition-experience-with-pencilkit)

Integrate handwriting recognition into your app to identify written text across multiple languages, and explore path conversion and substrokes to enhance the drawing experience.

[Recognizing handwriting and converting it to text](/documentation/PencilKit/recognizing-handwriting-and-converting-to-text)

Analyze handwritten strokes in a PencilKit canvas using on-device recognition, and convert them to text that your app can display, copy, or index.

### Tools

[Configuring the PencilKit tool picker](/documentation/PencilKit/configuring-the-pencilkit-tool-picker)

Incorporate a custom PencilKit tool picker with a variety of system and custom tools into a drawing app.

[`PKToolPicker`](/documentation/PencilKit/PKToolPicker)

A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from.

[`PKInkingTool`](/documentation/PencilKit/PKInkingTool-swift.struct)

A structure that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.

[`PKEraserTool`](/documentation/PencilKit/PKEraserTool-swift.struct)

A tool for erasing previously drawn content in a canvas view.

[`PKLassoTool`](/documentation/PencilKit/PKLassoTool-swift.struct)

A tool for selecting stroked lines and shapes in a canvas view.

[`PKTool`](/documentation/PencilKit/PKTool-swift.protocol)

An interface adopted by drawing and writing tools used by a canvas view.

### Tools

[Configuring the PencilKit tool picker](/documentation/PencilKit/configuring-the-pencilkit-tool-picker)

Incorporate a custom PencilKit tool picker with a variety of system and custom tools into a drawing app.

[`PKToolPicker`](/documentation/PencilKit/PKToolPicker)

A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from.

[`PKInkingToolReference`](/documentation/PencilKit/PKInkingToolReference)

An object that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.

[`PKEraserToolReference`](/documentation/PencilKit/PKEraserToolReference)

A tool for erasing previously drawn content in a canvas view.

[`PKLassoToolReference`](/documentation/PencilKit/PKLassoToolReference)

A tool for selecting stroked lines and shapes in a canvas view.

[`PKTool`](/documentation/PencilKit/PKTool-c.class)

An abstract base class for tools used by a canvas view.

[`PKResponderState`](/documentation/PencilKit/PKResponderState)

An object that controls PencilKit behavior associated with a responder.

[`PKToolPickerVisibility`](/documentation/PencilKit/PKToolPickerVisibility)

Constants that describe the visibility state of a tool picker.

[`Delegate`](/documentation/PencilKit/PKToolPicker/Delegate-swift.protocol)

[`ControlOptions`](/documentation/PencilKit/PKToolPickerCustomItem/ControlOptions)

Options for which controls to present.

### Backward compatibility

[Supporting backward compatibility for ink types](/documentation/PencilKit/supporting-backward-compatibility-for-ink-types)

Leverage the latest PencilKit features while providing a good user experience in earlier versions of the OS that don’t support those features.

[`PKContentVersion`](/documentation/PencilKit/PKContentVersion)

Constants that represent versions of PencilKit for backward compatibility.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
