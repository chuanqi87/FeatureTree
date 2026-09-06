# Quartz Display Services

Provides direct access to features in the macOS window server for configuring and controlling display hardware.

## Discussion

You can use Quartz Display Services to:

- Examine and change display mode properties such as width, height, and pixel depth
- Configure a set of displays in a single operation
- Capture one or more displays for exclusive use
- Stream the contents of a display
- Perform fade effects
- Activate display mirroring
- Configure gamma color correction tables
- Receive notification of screen update operations

## Topics

### Finding Displays

[`CGMainDisplayID`](/documentation/CoreGraphics/CGMainDisplayID())

Returns the display ID of the main display.

[`CGGetOnlineDisplayList`](/documentation/CoreGraphics/CGGetOnlineDisplayList(_:_:_:))

Provides a list of displays that are online (active, mirrored, or sleeping).

[`CGGetActiveDisplayList`](/documentation/CoreGraphics/CGGetActiveDisplayList(_:_:_:))

Provides a list of displays that are active for drawing.

[`CGGetDisplaysWithOpenGLDisplayMask`](/documentation/CoreGraphics/CGGetDisplaysWithOpenGLDisplayMask(_:_:_:_:))

Provides a list of displays that corresponds to the bits set in an OpenGL display mask.

[`CGGetDisplaysWithPoint`](/documentation/CoreGraphics/CGGetDisplaysWithPoint(_:_:_:_:))

Provides a list of online displays with bounds that include the specified point.

[`CGGetDisplaysWithRect`](/documentation/CoreGraphics/CGGetDisplaysWithRect(_:_:_:_:))

Gets a list of online displays with bounds that intersect the specified rectangle.

[`CGOpenGLDisplayMaskToDisplayID`](/documentation/CoreGraphics/CGOpenGLDisplayMaskToDisplayID(_:))

Maps an OpenGL display mask to a display ID.

[`CGDisplayIDToOpenGLDisplayMask`](/documentation/CoreGraphics/CGDisplayIDToOpenGLDisplayMask(_:))

Maps a display ID to an OpenGL display mask.

### Capturing and Releasing Displays

[`CGDisplayCapture`](/documentation/CoreGraphics/CGDisplayCapture(_:))

Obtains exclusive use of a display, preventing other applications and system services from using the display or changing its configuration.

[`CGDisplayCaptureWithOptions`](/documentation/CoreGraphics/CGDisplayCaptureWithOptions(_:_:))

Obtains exclusive use of a display for an application using the options you specify.

[`CGDisplayRelease`](/documentation/CoreGraphics/CGDisplayRelease(_:))

Releases a captured display.

[`CGDisplayIsCaptured`](/documentation/CoreGraphics/CGDisplayIsCaptured(_:))

Returns a Boolean value indicating whether a display is captured.

[`CGCaptureAllDisplays`](/documentation/CoreGraphics/CGCaptureAllDisplays())

Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.

[`CGCaptureAllDisplaysWithOptions`](/documentation/CoreGraphics/CGCaptureAllDisplaysWithOptions(_:))

Captures all attached displays, using the specified options.

[`CGReleaseAllDisplays`](/documentation/CoreGraphics/CGReleaseAllDisplays())

Releases all captured displays.

[`CGShieldingWindowID`](/documentation/CoreGraphics/CGShieldingWindowID(_:))

Returns the window ID of the shield window for a captured display.

[`CGShieldingWindowLevel`](/documentation/CoreGraphics/CGShieldingWindowLevel())

Returns the window level of the shield window for a captured display.

[`CGDisplayGetDrawingContext`](/documentation/CoreGraphics/CGDisplayGetDrawingContext(_:))

Returns a graphics context suitable for drawing to a captured display.

### Creating Images from the Display

### Configuring Displays

[`CGBeginDisplayConfiguration`](/documentation/CoreGraphics/CGBeginDisplayConfiguration(_:))

Begins a new set of display configuration changes.

[`CGCancelDisplayConfiguration`](/documentation/CoreGraphics/CGCancelDisplayConfiguration(_:))

Cancels a set of display configuration changes.

[`CGCompleteDisplayConfiguration`](/documentation/CoreGraphics/CGCompleteDisplayConfiguration(_:_:))

Completes a set of display configuration changes.

[`CGConfigureDisplayMirrorOfDisplay`](/documentation/CoreGraphics/CGConfigureDisplayMirrorOfDisplay(_:_:_:))

Changes the configuration of a mirroring set.

[`CGConfigureDisplayMode`](/documentation/CoreGraphics/CGConfigureDisplayMode(_:_:_:))

Configures the display mode of a display.

[`CGConfigureDisplayOrigin`](/documentation/CoreGraphics/CGConfigureDisplayOrigin(_:_:_:_:))

Configures the origin of a display relative to the global display coordinate space.

[`CGRestorePermanentDisplayConfiguration`](/documentation/CoreGraphics/CGRestorePermanentDisplayConfiguration())

Restores the permanent display configuration settings for the current user.

[`CGConfigureDisplayStereoOperation`](/documentation/CoreGraphics/CGConfigureDisplayStereoOperation(_:_:_:_:))

Enables or disables stereo operation for a display, as part of a display configuration.

[`CGDisplaySetStereoOperation`](/documentation/CoreGraphics/CGDisplaySetStereoOperation(_:_:_:_:))

Immediately enables or disables stereo operation for a display.

[`CGConfigureDisplayWithDisplayMode`](/documentation/CoreGraphics/CGConfigureDisplayWithDisplayMode(_:_:_:_:))

Configures the display mode of a display.

### Getting the Display Configuration

[`CGDisplayCopyColorSpace`](/documentation/CoreGraphics/CGDisplayCopyColorSpace(_:))

Returns the color space for a display.

[`CGDisplayIOServicePort`](/documentation/CoreGraphics/CGDisplayIOServicePort(_:))

Returns the I/O Kit service port of the specified display.

[`CGDisplayIsActive`](/documentation/CoreGraphics/CGDisplayIsActive(_:))

Returns a Boolean value indicating whether a display is active.

[`CGDisplayIsAlwaysInMirrorSet`](/documentation/CoreGraphics/CGDisplayIsAlwaysInMirrorSet(_:))

Returns a Boolean value indicating whether a display is always in a mirroring set.

[`CGDisplayIsAsleep`](/documentation/CoreGraphics/CGDisplayIsAsleep(_:))

Returns a Boolean value indicating whether a display is sleeping (and is therefore not drawable).

[`CGDisplayIsBuiltin`](/documentation/CoreGraphics/CGDisplayIsBuiltin(_:))

Returns a Boolean value indicating whether a display is built-in, such as the internal display in portable systems.

[`CGDisplayIsInHWMirrorSet`](/documentation/CoreGraphics/CGDisplayIsInHWMirrorSet(_:))

Returns a Boolean value indicating whether a display is in a hardware mirroring set.

[`CGDisplayIsInMirrorSet`](/documentation/CoreGraphics/CGDisplayIsInMirrorSet(_:))

Returns a Boolean value indicating whether a display is in a mirroring set.

[`CGDisplayIsMain`](/documentation/CoreGraphics/CGDisplayIsMain(_:))

Returns a Boolean value indicating whether a display is the main display.

[`CGDisplayIsOnline`](/documentation/CoreGraphics/CGDisplayIsOnline(_:))

Returns a Boolean value indicating whether a display is connected or online.

[`CGDisplayIsStereo`](/documentation/CoreGraphics/CGDisplayIsStereo(_:))

Returns a Boolean value indicating whether a display is running in a stereo graphics mode.

[`CGDisplayMirrorsDisplay`](/documentation/CoreGraphics/CGDisplayMirrorsDisplay(_:))

For a secondary display in a mirroring set, returns the primary display.

[`CGDisplayModelNumber`](/documentation/CoreGraphics/CGDisplayModelNumber(_:))

Returns the model number of a display monitor.

[`CGDisplayPrimaryDisplay`](/documentation/CoreGraphics/CGDisplayPrimaryDisplay(_:))

Returns the primary display in a hardware mirroring set.

[`CGDisplayRotation`](/documentation/CoreGraphics/CGDisplayRotation(_:))

Returns the rotation angle of a display in degrees.

[`CGDisplayScreenSize`](/documentation/CoreGraphics/CGDisplayScreenSize(_:))

Returns the width and height of a display in millimeters.

[`CGDisplaySerialNumber`](/documentation/CoreGraphics/CGDisplaySerialNumber(_:))

Returns the serial number of a display monitor.

[`CGDisplayUnitNumber`](/documentation/CoreGraphics/CGDisplayUnitNumber(_:))

Returns the logical unit number of a display.

[`CGDisplayUsesOpenGLAcceleration`](/documentation/CoreGraphics/CGDisplayUsesOpenGLAcceleration(_:))

Returns a Boolean value indicating whether Quartz is using OpenGL-based window acceleration (Quartz Extreme) to render in a display.

[`CGDisplayVendorNumber`](/documentation/CoreGraphics/CGDisplayVendorNumber(_:))

Returns the vendor number of the specified display’s monitor.

### Registering for Notification of Display Configuration Changes

These functions are used to register and unregister a callback function for notification of display configuration changes.

[`CGDisplayRegisterReconfigurationCallback`](/documentation/CoreGraphics/CGDisplayRegisterReconfigurationCallback(_:_:))

Registers a callback function to be invoked whenever a local display is reconfigured.

[`CGDisplayRemoveReconfigurationCallback`](/documentation/CoreGraphics/CGDisplayRemoveReconfigurationCallback(_:_:))

Removes the registration of a callback function that’s invoked whenever a local display is reconfigured.

### Retrieving Display Parameters

[`CGDisplayBounds`](/documentation/CoreGraphics/CGDisplayBounds(_:))

Returns the bounds of a display in the global display coordinate space.

[`CGDisplayPixelsHigh`](/documentation/CoreGraphics/CGDisplayPixelsHigh(_:))

Returns the display height in pixel units.

[`CGDisplayPixelsWide`](/documentation/CoreGraphics/CGDisplayPixelsWide(_:))

Returns the display width in pixel units.

### Creating and Managing Display Modes

[`CGDisplayAvailableModes`](/documentation/CoreGraphics/CGDisplayAvailableModes(_:))

Returns information about the currently available display modes.

[`CGDisplayBestModeForParameters`](/documentation/CoreGraphics/CGDisplayBestModeForParameters(_:_:_:_:_:))

Returns information about the display mode closest to a specified depth and screen size.

[`CGDisplayBestModeForParametersAndRefreshRate`](/documentation/CoreGraphics/CGDisplayBestModeForParametersAndRefreshRate(_:_:_:_:_:_:))

Returns information about the display mode closest to a specified depth, screen size, and refresh rate.

[`CGDisplayCurrentMode`](/documentation/CoreGraphics/CGDisplayCurrentMode(_:))

Returns information about the current display mode.

[`CGDisplaySwitchToMode`](/documentation/CoreGraphics/CGDisplaySwitchToMode(_:_:))

Switches a display to a different mode.

[`CGDisplayCopyDisplayMode`](/documentation/CoreGraphics/CGDisplayCopyDisplayMode(_:))

Returns information about a display’s current configuration.

[`CGDisplayCopyAllDisplayModes`](/documentation/CoreGraphics/CGDisplayCopyAllDisplayModes(_:_:))

Returns information about the currently available display modes.

[`CGDisplaySetDisplayMode`](/documentation/CoreGraphics/CGDisplaySetDisplayMode(_:_:_:))

Switches a display to a different mode.

[`CGDisplayModeRetain`](/documentation/CoreGraphics/CGDisplayModeRetain)

Retains a Core Graphics display mode.

[`CGDisplayModeRelease`](/documentation/CoreGraphics/CGDisplayModeRelease)

Releases a Core Graphics display mode.

### Getting Information About a Display Mode

[`CGDisplayModeGetWidth`](/documentation/CoreGraphics/CGDisplayMode/width)

Returns the width of the specified display mode.

[`CGDisplayModeGetHeight`](/documentation/CoreGraphics/CGDisplayMode/height)

Returns the height of the specified display mode.

[`CGDisplayModeCopyPixelEncoding`](/documentation/CoreGraphics/CGDisplayMode/pixelEncoding)

Returns the pixel encoding of the specified display mode.

[`CGDisplayModeGetRefreshRate`](/documentation/CoreGraphics/CGDisplayMode/refreshRate)

Returns the refresh rate of the specified display mode.

[`CGDisplayModeGetIOFlags`](/documentation/CoreGraphics/CGDisplayMode/ioFlags)

Returns the I/O Kit flags of the specified display mode.

[`CGDisplayModeGetIODisplayModeID`](/documentation/CoreGraphics/CGDisplayMode/ioDisplayModeID)

Returns the I/O Kit display mode ID of the specified display mode.

[`CGDisplayModeIsUsableForDesktopGUI`](/documentation/CoreGraphics/CGDisplayMode/isUsableForDesktopGUI())

Returns a Boolean value indicating whether the specified display mode is usable for a desktop graphical user interface.

[`CGDisplayModeGetTypeID`](/documentation/CoreGraphics/CGDisplayMode/typeID)

Returns the type identifier of Quartz display modes.

### Adjusting the Display Gamma

[`CGSetDisplayTransferByFormula`](/documentation/CoreGraphics/CGSetDisplayTransferByFormula(_:_:_:_:_:_:_:_:_:_:))

Sets the gamma function for a display by specifying the coefficients of the gamma transfer formula.

[`CGGetDisplayTransferByFormula`](/documentation/CoreGraphics/CGGetDisplayTransferByFormula(_:_:_:_:_:_:_:_:_:_:))

Gets the coefficients of the gamma transfer formula for a display.

[`CGSetDisplayTransferByTable`](/documentation/CoreGraphics/CGSetDisplayTransferByTable(_:_:_:_:_:))

Sets the color gamma function for a display by specifying the values in the RGB gamma tables.

[`CGGetDisplayTransferByTable`](/documentation/CoreGraphics/CGGetDisplayTransferByTable(_:_:_:_:_:_:))

Gets the values in the RGB gamma tables for a display.

[`CGSetDisplayTransferByByteTable`](/documentation/CoreGraphics/CGSetDisplayTransferByByteTable(_:_:_:_:_:))

Sets the byte values in the 8-bit RGB gamma tables for a display.

[`CGDisplayRestoreColorSyncSettings`](/documentation/CoreGraphics/CGDisplayRestoreColorSyncSettings())

Restores the gamma tables to the values in the user’s ColorSync display profile.

[`CGDisplayGammaTableCapacity`](/documentation/CoreGraphics/CGDisplayGammaTableCapacity(_:))

Returns the capacity, or number of entries, in the gamma table for a display.

### Display Fade Effects

[`CGConfigureDisplayFadeEffect`](/documentation/CoreGraphics/CGConfigureDisplayFadeEffect(_:_:_:_:_:_:))

Modifies the settings of the built-in fade effect that occurs during a display configuration.

[`CGAcquireDisplayFadeReservation`](/documentation/CoreGraphics/CGAcquireDisplayFadeReservation(_:_:))

Reserves the fade hardware for a specified time interval.

[`CGDisplayFade`](/documentation/CoreGraphics/CGDisplayFade(_:_:_:_:_:_:_:_:))

Performs a single fade operation.

[`CGDisplayFadeOperationInProgress`](/documentation/CoreGraphics/CGDisplayFadeOperationInProgress())

Returns a Boolean value indicating whether a fade operation is currently in progress.

[`CGReleaseDisplayFadeReservation`](/documentation/CoreGraphics/CGReleaseDisplayFadeReservation(_:))

Releases a display fade reservation, and unfades the display if needed.

### Controlling the Mouse Cursor

[`CGDisplayHideCursor`](/documentation/CoreGraphics/CGDisplayHideCursor(_:))

Hides the mouse cursor, and increments the hide cursor count.

[`CGDisplayShowCursor`](/documentation/CoreGraphics/CGDisplayShowCursor(_:))

Decrements the hide cursor count, and shows the mouse cursor if the count is `0`.

[`CGDisplayMoveCursorToPoint`](/documentation/CoreGraphics/CGDisplayMoveCursorToPoint(_:_:))

Moves the mouse cursor to a specified point relative to the upper-left corner of the display.

[`CGCursorIsVisible`](/documentation/CoreGraphics/CGCursorIsVisible())

Returns a Boolean value indicating whether the mouse cursor is visible.

[`CGCursorIsDrawnInFramebuffer`](/documentation/CoreGraphics/CGCursorIsDrawnInFramebuffer())

Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory.

[`CGAssociateMouseAndMouseCursorPosition`](/documentation/CoreGraphics/CGAssociateMouseAndMouseCursorPosition(_:))

Connects or disconnects the mouse and cursor while an application is in the foreground.

[`CGWarpMouseCursorPosition`](/documentation/CoreGraphics/CGWarpMouseCursorPosition(_:))

Moves the mouse cursor without generating events.

[`CGGetLastMouseDelta()`](/documentation/CoreGraphics/CGGetLastMouseDelta())

Reports the change in mouse position since the last mouse movement event received by the application.

[`CGGetLastMouseDelta`](/documentation/CoreGraphics/CGGetLastMouseDelta)

Reports the change in mouse position since the last mouse movement event received by the application.

### Getting Window Server Information

[`CGSessionCopyCurrentDictionary`](/documentation/CoreGraphics/CGSessionCopyCurrentDictionary())

Returns information about the caller’s window server session.

[`CGWindowServerCFMachPort`](/documentation/CoreGraphics/CGWindowServerCFMachPort())

Returns a Core Foundation Mach port (CFMachPort) that corresponds to the macOS window server.

[`CGWindowLevelForKey`](/documentation/CoreGraphics/CGWindowLevelForKey(_:))

Returns the window level that corresponds to one of the standard window types.

### Getting Information About Refresh and Move Operations

You can use these functions to find out what areas on local displays are changing their appearance as the result of operations such as drawing, window movement or scrolling, and display reconfiguration.

[`CGRegisterScreenRefreshCallback`](/documentation/CoreGraphics/CGRegisterScreenRefreshCallback(_:_:))

Registers a callback function to be invoked when local displays are refreshed or modified.

[`CGUnregisterScreenRefreshCallback`](/documentation/CoreGraphics/CGUnregisterScreenRefreshCallback(_:_:))

Removes a previously registered callback function invoked when local displays are refreshed or modified.

[`CGWaitForScreenRefreshRects`](/documentation/CoreGraphics/CGWaitForScreenRefreshRects(_:_:))

Waits for screen refresh operations.

[`CGScreenRegisterMoveCallback`](/documentation/CoreGraphics/CGScreenRegisterMoveCallback(_:_:))

Registers a callback function to be invoked when an area of the display is moved.

[`CGScreenUnregisterMoveCallback`](/documentation/CoreGraphics/CGScreenUnregisterMoveCallback(_:_:))

Removes a previously registered callback function invoked when an area of the display is moved.

[`CGWaitForScreenUpdateRects`](/documentation/CoreGraphics/CGWaitForScreenUpdateRects(_:_:_:_:_:))

Waits for screen update operations.

[`CGReleaseScreenRefreshRects`](/documentation/CoreGraphics/CGReleaseScreenRefreshRects(_:))

Deallocates a list of rectangles that represent changed areas on local displays.

### Streaming the Contents of a Display

### Callbacks

[`CGDisplayReconfigurationCallBack`](/documentation/CoreGraphics/CGDisplayReconfigurationCallBack)

A client-supplied callback function that’s invoked whenever the configuration of a local display is changed.

[`CGScreenRefreshCallback`](/documentation/CoreGraphics/CGScreenRefreshCallback)

A client-supplied callback function that’s invoked when an area of the display is modified or refreshed.

[`CGScreenUpdateMoveCallback`](/documentation/CoreGraphics/CGScreenUpdateMoveCallback)

A client-supplied callback function invoked when an area of the display is moved.

### Data Types

[`CGDirectDisplayID`](/documentation/CoreGraphics/CGDirectDisplayID)

A unique identifier for an attached display.

[`CGDisplayBlendFraction`](/documentation/CoreGraphics/CGDisplayBlendFraction)

The percentage of blend color used in a fade operation.

[`CGDisplayConfigRef`](/documentation/CoreGraphics/CGDisplayConfigRef)

A reference to a display configuration transaction.

[`CGDisplayCount`](/documentation/CoreGraphics/CGDisplayCount)

The number of displays in various lists.

[`CGDisplayErr`](/documentation/CoreGraphics/CGDisplayErr)

A uniform type for result codes returned by functions in Quartz Display Services.

[`CGDisplayFadeInterval`](/documentation/CoreGraphics/CGDisplayFadeInterval)

The duration in seconds of a fade operation or a fade hardware reservation.

[`CGDisplayFadeReservationToken`](/documentation/CoreGraphics/CGDisplayFadeReservationToken)

A token issued by Quartz when reserving one or more displays for a fade operation during a specified interval.

[`CGDisplayMode`](/documentation/CoreGraphics/CGDisplayMode)

A reference to a display mode object.

[`CGDisplayReservationInterval`](/documentation/CoreGraphics/CGDisplayReservationInterval)

The time interval for a fade reservation.

[`CGGammaValue`](/documentation/CoreGraphics/CGGammaValue)

A value used to map a color generated in software to a color supported by the display hardware.

[`CGOpenGLDisplayMask`](/documentation/CoreGraphics/CGOpenGLDisplayMask)

A bitmask used in OpenGL to specify a set of attached displays.

[`CGRectCount`](/documentation/CoreGraphics/CGRectCount)

The size of an array of Quartz rectangles.

[`CGRefreshRate`](/documentation/CoreGraphics/CGRefreshRate)

A display’s refresh rate in frames per second.

[`CGScreenUpdateMoveDelta`](/documentation/CoreGraphics/CGScreenUpdateMoveDelta)

The distance, in pixel units, that an onscreen region moves.

[`CGWindowLevel`](/documentation/CoreGraphics/CGWindowLevel)

A level assigned to a window by an application framework.

[`CGDisplayStream`](/documentation/CoreGraphics/CGDisplayStream)

A reference to a display stream object.

[`CGDisplayStreamUpdate`](/documentation/CoreGraphics/CGDisplayStreamUpdate)

A reference to frame update’s metadata.

[`CGDisplayStreamFrameAvailableHandler`](/documentation/CoreGraphics/CGDisplayStreamFrameAvailableHandler)

A block called when a data stream has a new frame event to process.

### Constants

[`CGCaptureOptions`](/documentation/CoreGraphics/CGCaptureOptions)

Configuration parameters that are used when capturing displays.

[`CGDisplayChangeSummaryFlags`](/documentation/CoreGraphics/CGDisplayChangeSummaryFlags)

The configuration parameters that are passed to a display reconfiguration callback function.

[`CGConfigureOption`](/documentation/CoreGraphics/CGConfigureOption)

The scope of the changes in a display configuration transaction.

[Display Fade Blend Fractions](/documentation/CoreGraphics/display-fade-blend-fractions)

The lower and upper bounds for blend color fractions during a display fade operation.

[Display Fade Constants](/documentation/CoreGraphics/display-fade-constants)

Values relating to fade operations.

[Display ID Defaults](/documentation/CoreGraphics/display-id-defaults)

Default values for a display ID.

[Display Mode Standard Properties](/documentation/CoreGraphics/display-mode-standard-properties)

Keys for the standard properties in a display mode dictionary.

[Display Mode Optional Properties](/documentation/CoreGraphics/display-mode-optional-properties)

Keys for optional properties in a display mode dictionary.

[Reserved Window Levels](/documentation/CoreGraphics/reserved-window-levels)

Window level constants.

[`CGScreenUpdateOperation`](/documentation/CoreGraphics/CGScreenUpdateOperation)

Types of screen-update operations.

[`CGWindowLevelKey`](/documentation/CoreGraphics/CGWindowLevelKey)

Keys that represent the standard window levels in macOS. Quartz includes these keys to support application frameworks like Cocoa. Applications do not need to use them directly.

[Window Server Session Properties](/documentation/CoreGraphics/window-server-session-properties)

The keys for the standard properties in a window server session dictionary.

[`CGDisplayStreamUpdateRectType`](/documentation/CoreGraphics/CGDisplayStreamUpdateRectType)

Use these constants to determine which rectangles your app is interested in.

[`CGDisplayStreamFrameStatus`](/documentation/CoreGraphics/CGDisplayStreamFrameStatus)

Describes a frame update event.

[Display Stream Optional Property Keys](/documentation/CoreGraphics/display-stream-optional-property-keys)

These keys are used to populate the `properties` dictionary used when creating a new display stream.

[Display Stream YCbCr to RGB conversion Matrix Options](/documentation/CoreGraphics/display-stream-ycbcr-to-rgb-conversion-matrix-options)

These strings are used to specify a matrix for the `CGDisplayStream/yCbCrMatrix` option.

## See Also

  [Quartz Display Services Programming Topics](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004316)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
