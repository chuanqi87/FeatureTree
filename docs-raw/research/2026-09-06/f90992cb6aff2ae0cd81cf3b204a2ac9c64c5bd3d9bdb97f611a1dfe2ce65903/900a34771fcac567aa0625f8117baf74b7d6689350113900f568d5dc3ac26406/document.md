# CVDisplayLink

A high-priority thread that notifies your app when a given display will need each frame.

## Overview

A Core Video display link provides a separate high-priority thread to notify your application when a given display will need each frame. You can use a display link to easily synchronize with the refresh rate of a display. The display link API uses the Core Foundation class system internally to provide reference counting behavior and other useful properties.

## Topics

### Creating Display Links

[`CVDisplayLinkCreateWithCGDisplay`](/documentation/CoreVideo/CVDisplayLinkCreateWithCGDisplay(_:_:))

Creates a display link for a single display.

[`CVDisplayLinkCreateWithCGDisplays`](/documentation/CoreVideo/CVDisplayLinkCreateWithCGDisplays(_:_:_:))

Creates a display link for an array of displays.

[`CVDisplayLinkCreateWithActiveCGDisplays`](/documentation/CoreVideo/CVDisplayLinkCreateWithActiveCGDisplays(_:))

Creates a display link capable of being used with all active displays.

[`CVDisplayLinkCreateWithOpenGLDisplayMask`](/documentation/CoreVideo/CVDisplayLinkCreateWithOpenGLDisplayMask(_:_:))

Creates a display link from an OpenGL display mask.

### Configuring Display Links

[`CVDisplayLinkSetCurrentCGDisplay`](/documentation/CoreVideo/CVDisplayLinkSetCurrentCGDisplay(_:_:))

Sets the current display of a display link.

[`CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext`](/documentation/CoreVideo/CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(_:_:_:))

Selects the display link most optimal for the current renderer of an OpenGL context.

[`CVDisplayLinkSetOutputCallback`](/documentation/CoreVideo/CVDisplayLinkSetOutputCallback(_:_:_:))

Sets the renderer output callback function.

[`CVDisplayLinkSetOutputHandler`](/documentation/CoreVideo/CVDisplayLinkSetOutputHandler(_:_:))

[`CVDisplayLinkOutputHandler`](/documentation/CoreVideo/CVDisplayLinkOutputHandler)

### Inspecting Display Links

[`CVDisplayLinkGetCurrentCGDisplay`](/documentation/CoreVideo/CVDisplayLinkGetCurrentCGDisplay(_:))

Gets the current display associated with a display link.

[`CVDisplayLinkGetCurrentTime`](/documentation/CoreVideo/CVDisplayLinkGetCurrentTime(_:_:))

Retrieves the current (“now”) time of a given display link.

[`CVDisplayLinkTranslateTime`](/documentation/CoreVideo/CVDisplayLinkTranslateTime(_:_:_:))

Translates the time in the display link’s time base from one representation to another.

[`CVDisplayLinkGetActualOutputVideoRefreshPeriod`](/documentation/CoreVideo/CVDisplayLinkGetActualOutputVideoRefreshPeriod(_:))

Retrieves the actual output refresh period of a display as measured by the system time.

[`CVDisplayLinkGetNominalOutputVideoRefreshPeriod`](/documentation/CoreVideo/CVDisplayLinkGetNominalOutputVideoRefreshPeriod(_:))

Retrieves the nominal refresh period of a display link.

[`CVDisplayLinkGetOutputVideoLatency`](/documentation/CoreVideo/CVDisplayLinkGetOutputVideoLatency(_:))

Retrieves the nominal latency of a display link.

[`CVDisplayLinkIsRunning`](/documentation/CoreVideo/CVDisplayLinkIsRunning(_:))

Indicates whether a given display link is running.

[`CVDisplayLinkGetTypeID`](/documentation/CoreVideo/CVDisplayLinkGetTypeID())

Obtains the Core Foundation ID for the display link data type.

### Retaining and Releasing Display Links

[`CVDisplayLinkRelease`](/documentation/CoreVideo/CVDisplayLinkRelease)

Releases a display link.

[`CVDisplayLinkRetain`](/documentation/CoreVideo/CVDisplayLinkRetain)

Retains a display link.

### Managing Display Links

[`CVDisplayLinkStart`](/documentation/CoreVideo/CVDisplayLinkStart(_:))

Activates a display link.

[`CVDisplayLinkStop`](/documentation/CoreVideo/CVDisplayLinkStop(_:))

Stops a display link.

### Data Types

[`CVDisplayLink`](/documentation/CoreVideo/CVDisplayLink)

A reference to a display link object.

[`CVOptionFlags`](/documentation/CoreVideo/CVOptionFlags)

The flags to be used for the display link output callback function.

### Callbacks

[`CVDisplayLinkOutputCallback`](/documentation/CoreVideo/CVDisplayLinkOutputCallback)

A type for a display link callback function that the system invokes when it’s time for the app to output a video frame.

[`CVDisplayLinkOutputHandler`](/documentation/CoreVideo/CVDisplayLinkOutputHandler)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
