# UIImageView

A view that displays a single image or a sequence of animated images in your interface.

```
@MainActor class UIImageView
```

## Overview

Image views let you efficiently draw any image that can be specified using a [`UIImage`](/documentation/UIKit/UIImage) object. For example, you can use the [`UIImageView`](/documentation/UIKit/UIImageView) class to display the contents of many standard image files, such as JPEG and PNG files. You can configure image views programmatically or in your storyboard file and change the images they display at runtime. For animated images, you can also use the methods of this class to start and stop the animation and specify other animation parameters.

![An image view](images/com.apple.uikit/media-2923882@2x.png)

### Understand how images are scaled

An image view uses its [`contentMode`](/documentation/UIKit/UIView/contentMode-swift.property) property and the configuration of the image itself to determine how to display the image. It’s best to specify images whose dimensions match the dimensions of the image view exactly, but image views can scale your images to fit all or some of the available space. If the size of the image view itself changes, it automatically scales the image as needed.

For an image without cap insets, the presentation of the image is determined solely by the image view’s [`contentMode`](/documentation/UIKit/UIView/contentMode-swift.property) property. The [`UIView.ContentMode.scaleAspectFit`](/documentation/UIKit/UIView/ContentMode-swift.enum/scaleAspectFit) and [`UIView.ContentMode.scaleAspectFill`](/documentation/UIKit/UIView/ContentMode-swift.enum/scaleAspectFill) modes scale the image to fit or fill the space while maintaining the image’s original aspect ratio. The [`UIView.ContentMode.scaleToFill`](/documentation/UIKit/UIView/ContentMode-swift.enum/scaleToFill) value scales the image without regard to the original aspect ratio, which can cause the image to appear distorted. Other content modes place the image at the appropriate location in the image view’s bounds without scaling it.

For a resizable image with cap insets, those insets affect the final appearance of the image. Specifically, cap insets define which parts of the image may be scaled and in which directions. You can create a resizable image that stretches using the [`resizableImage(withCapInsets:resizingMode:)`](/documentation/UIKit/UIImage/resizableImage(withCapInsets:resizingMode:)) method of [`UIImage`](/documentation/UIKit/UIImage). When using an image of this type, you typically set the image view’s content mode to [`UIView.ContentMode.scaleToFill`](/documentation/UIKit/UIView/ContentMode-swift.enum/scaleToFill) so that the image stretches in the appropriate places and fills the image view’s bounds.

For tips on how to prepare images, see [`Debug issues with your image view`](/documentation/UIKit/UIImageView#Debug-issues-with-your-image-view). For more information on creating resizable images with cap insets, see [`UIImage`](/documentation/UIKit/UIImage).

### Determine the final transparency of the image

Images are composited onto the image view’s background and are then composited into the rest of the window. Any transparency in the image allows the image view’s background to show through. Similarly, any further transparency in the background of the image is dependent on the transparency of the image view and the transparency of the [`UIImage`](/documentation/UIKit/UIImage) object it displays. When the image view and its image both have transparency, the image view uses alpha blending to combine the two.

- The image is composited onto the image view’s background.
- If the image view’s [`isOpaque`](/documentation/UIKit/UIView/isOpaque) property is <doc://com.apple.documentation/documentation/Swift/true>, the image’s pixels are composited on top of the image view’s background color and the [`alpha`](/documentation/UIKit/UIView/alpha) property of the image view is ignored.
- If the image view’s [`isOpaque`](/documentation/UIKit/UIView/isOpaque) property is <doc://com.apple.documentation/documentation/Swift/false>, the alpha value of each pixel is multiplied by the image view’s [`alpha`](/documentation/UIKit/UIView/alpha) value, with the resulting value becoming the actual transparency value for that pixel. If the image doesn’t have an alpha channel, the alpha value of each pixel is assumed to be `1.0`.

> Important:
> It’s computationally expensive to composite the alpha channel of an image with the alpha channel of a non-opaque image view. The performance impact is further magnified if you use Core Animation shadows, because the shape of the shadow is then based on the contents of the view and must be dynamically computed. If you aren’t intentionally using the alpha channel of the image or the alpha channel of the image view, set the ``doc://com.apple.uikit/documentation/UIKit/UIView/isOpaque`` property to <doc://com.apple.documentation/documentation/Swift/true> to improve performance. For additional optimization tips, see <doc://com.apple.uikit/documentation/UIKit/UIImageView#Improve-performance>.

### Animate a sequence of images

An image view can store an animated image sequence and play all or part of that sequence. You specify an image sequence as an array of [`UIImage`](/documentation/UIKit/UIImage) objects and assign them to the [`animationImages`](/documentation/UIKit/UIImageView/animationImages) property. Once assigned, you can use the methods and properties of this class to configure the animation timing and to start and stop the animation.

> Note:
> You can also construct a single ``doc://com.apple.uikit/documentation/UIKit/UIImage`` object from a sequence of individual images using the ``doc://com.apple.uikit/documentation/UIKit/UIImage/animatedImage(with:duration:)`` method. Doing so yields the same results as assigning the individual images to the ``doc://com.apple.uikit/documentation/UIKit/UIImageView/animationImages`` property.

Consider the following tips when displaying a sequence of animated images:

- **All images in the sequence should have the same size.** When scaling is required, the image view scales each image in the sequence separately. If the images are different sizes, scaling may not yield the results you want.
- **All images in the sequence should use the same content scale factor.** Make sure the [`scale`](/documentation/UIKit/UIImage/scale) property of each image contains the same value.

### Respond to touch events

Image views ignore user events by default. Normally, you use image views only to present visual content in your interface. If you want an image view to handle user interactions as well, change the value of its [`isUserInteractionEnabled`](/documentation/UIKit/UIImageView/isUserInteractionEnabled) property to <doc://com.apple.documentation/documentation/Swift/true>. After doing that, you can attach gesture recognizers or use any other event handling techniques to respond to touch events or other user-initiated events.

For more information about handling events, see [Event Handling Guide for UIKit Apps](https://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html#//apple_ref/doc/uid/TP40009541).

### Improve performance

Image scaling and alpha blending are two relatively expensive operations that can impact your app’s performance. To maximize performance of your image view code, consider the following tips:

- **Cache scaled versions of frequently used images.** If you expect certain large images to be displayed frequently in a scaled-down thumbnail view, consider creating the scaled-down images in advance and storing them in a thumbnail cache. Doing so alleviates the need for each image view to scale them separately.
- **Use images whose size is close to the size of the image view.** Rather than assigning a large image to an image view, created a scaled version that matches the current size of the image view. You can also create a resizable image object using the [`UIImage.ResizingMode.tile`](/documentation/UIKit/UIImage/ResizingMode-swift.enum/tile) option, which tiles the image instead of scaling it.
- **Make your image view opaque whenever possible.** Unless you’re intentionally working with images that contain transparency (drawing UI elements, for example), make sure the [`isOpaque`](/documentation/UIKit/UIView/isOpaque) property of your image view is set to <doc://com.apple.documentation/documentation/Swift/true>. For more information about how transparency is determined, see [`Determine the final transparency of the image`](/documentation/UIKit/UIImageView#Determine-the-final-transparency-of-the-image).

### Debug issues with your image view

If your image view isn’t displaying what you expected, use the following tips to help diagnose the problem:

- **Load images using the correct method.** Use the [`init(named:in:compatibleWith:)`](/documentation/UIKit/UIImage/init(named:in:compatibleWith:)) method of [`UIImage`](/documentation/UIKit/UIImage) to load images from asset catalogs or your app’s bundle. For images outside of your app’s bundle, use the [`imageWithContentsOfFile:`](/documentation/UIKit/UIImage/imageWithContentsOfFile:) method.
- **Don’t use image views for custom drawing.** The [`UIImageView`](/documentation/UIKit/UIImageView) class doesn’t draw its content using the [`draw(_:)`](/documentation/UIKit/UIView/draw(_:)) method. Use image views only to present images. To do custom drawing involving images, subclass [`UIView`](/documentation/UIKit/UIView) directly and draw your image there.

### Interface Builder attributes

The following table lists the attributes that you configure for image views in Interface Builder.

|Attribute  |Discussion                                                                                                                                                                                                                                                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Image      |The image to display. You can specify any image in your Xcode project, including standalone images and those in image assets. To set this attribute programmatically, use the ``doc://com.apple.uikit/documentation/UIKit/UIImageView/image`` or ``doc://com.apple.uikit/documentation/UIKit/UIImageView/animationImages`` property.|
|Highlighted|The image to display when the image view is highlighted. To set this attribute programmatically, use the ``doc://com.apple.uikit/documentation/UIKit/UIImageView/highlightedImage`` or ``doc://com.apple.uikit/documentation/UIKit/UIImageView/highlightedAnimationImages`` property.                                               |
|State      |The initial state of the image. Use this attribute to mark the image as highlighted. To set this attribute programmatically, use the ``doc://com.apple.uikit/documentation/UIKit/UIImageView/isHighlighted`` property.                                                                                                              |

### Internationalization

Internationalization of image views is automatic if your view displays only static images loaded from your app bundle. If you’re loading images programmatically, you’re at least partially responsible for loading the correct image.

- For resources in your app bundle, you do this by specifying the name in the attributes inspector or by calling the [`init(named:)`](/documentation/UIKit/UIImage/init(named:)) class method on [`UIImage`](/documentation/UIKit/UIImage) to obtain the localized version of each image.
- For images that aren’t in your app bundle, your code must do the following:

1. Determine which image to load in a manner specific to your app, such as providing a localized string that contains the URL.
2. Load that image by passing the URL or data for the correct image to an appropriate [`UIImage`](/documentation/UIKit/UIImage) class method, such as [`imageWithData:`](/documentation/UIKit/UIImage/imageWithData:) or [`imageWithContentsOfFile:`](/documentation/UIKit/UIImage/imageWithContentsOfFile:).

> Note:
> Screen metrics and layout may also change depending on the language and locale, particularly if the internationalized versions of your images have different dimensions. Where possible, you should try to make minimize dimension differences in internationalized versions of image resources.

For more information, see <doc://com.apple.documentation/documentation/Xcode/localization>.

### Accessibility

Image views are accessible by default. The default accessibility traits for an image view are Image and User Interaction Enabled.

For more information about making iOS controls accessible, see the accessibility information in [`UIControl`](/documentation/UIKit/UIControl). For general information about making your interface accessible, see [Accessibility for UIKit](/documentation/UIKit/accessibility-for-uikit).

### State preservation

When you assign a value to an image view’s [`restorationIdentifier`](/documentation/UIKit/UIViewController/restorationIdentifier) property, it attempts to preserve the frame of the displayed image. Specifically, the class preserves the values of the [`bounds`](/documentation/UIKit/UIView/bounds), [`center`](/documentation/UIKit/UIView/center), and [`transform`](/documentation/UIKit/UIView/transform) properties of the view and the <doc://com.apple.documentation/documentation/QuartzCore/CALayer/anchorPoint> property of the underlying layer. During restoration, the image view restores these values so that the image appears exactly as before. For more information about how state preservation and restoration works, see [Restoring your app’s state](/documentation/UIKit/restoring-your-app-s-state).

## Topics

### Creating an image view

[`-  initWithImage:`](/documentation/UIKit/UIImageView/init(image:))

Returns an image view initialized with the specified image.

[`-  initWithImage:highlightedImage:`](/documentation/UIKit/UIImageView/init(image:highlightedImage:))

Returns an image view initialized with the specified regular and highlighted images.

### Accessing the displayed images

[`image`](/documentation/UIKit/UIImageView/image)

The image displayed in the image view.

[`highlightedImage`](/documentation/UIKit/UIImageView/highlightedImage)

The highlighted image displayed in the image view.

### Animating a sequence of images

[`animationImages`](/documentation/UIKit/UIImageView/animationImages)

An array of [`UIImage`](/documentation/UIKit/UIImage) objects to use for an animation.

[`highlightedAnimationImages`](/documentation/UIKit/UIImageView/highlightedAnimationImages)

An array of [`UIImage`](/documentation/UIKit/UIImage) objects to use for an animation when the view is highlighted.

[`animationDuration`](/documentation/UIKit/UIImageView/animationDuration)

The amount of time it takes to go through one cycle of the images.

[`animationRepeatCount`](/documentation/UIKit/UIImageView/animationRepeatCount)

Specifies the number of times to repeat the animation.

[`-  startAnimating`](/documentation/UIKit/UIImageView/startAnimating())

Starts animating the images in the receiver.

[`-  stopAnimating`](/documentation/UIKit/UIImageView/stopAnimating())

Stops animating the images in the receiver.

[`animating`](/documentation/UIKit/UIImageView/isAnimating)

Returns a Boolean value indicating whether the animation is running.

### Configuring the image view

[`userInteractionEnabled`](/documentation/UIKit/UIImageView/isUserInteractionEnabled)

A Boolean value that determines whether user events are ignored and removed from the event queue.

[`highlighted`](/documentation/UIKit/UIImageView/isHighlighted)

A Boolean value that determines whether the image is highlighted.

[`tintColor`](/documentation/UIKit/UIImageView/tintColor)

A color used to tint template images in the view hierarchy.

### Configuring the appearance of symbol images

[Configuring and displaying symbol images in your UI](/documentation/UIKit/configuring-and-displaying-symbol-images-in-your-ui)

Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.

[`preferredSymbolConfiguration`](/documentation/UIKit/UIImageView/preferredSymbolConfiguration)

The configuration values to use when rendering the image.

### Configuring symbol effects

[`addSymbolEffect(_:options:animated:completion:)`](/documentation/UIKit/UIImageView/addSymbolEffect(_:options:animated:completion:)-18jqj)

Adds a discrete symbol effect to the image view with the specified options and animation.

[`addSymbolEffect(_:options:animated:completion:)`](/documentation/UIKit/UIImageView/addSymbolEffect(_:options:animated:completion:)-2ixnm)

Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.

[`addSymbolEffect(_:options:animated:completion:)`](/documentation/UIKit/UIImageView/addSymbolEffect(_:options:animated:completion:)-896qd)

Adds an indefinite symbol effect to the image view with the specified options and animation.

[`setSymbolImage(_:contentTransition:options:completion:)`](/documentation/UIKit/UIImageView/setSymbolImage(_:contentTransition:options:completion:))

Sets a symbol image using the specified content-transition effect, options, and completion handler.

[`removeSymbolEffect(ofType:options:animated:completion:)`](/documentation/UIKit/UIImageView/removeSymbolEffect(ofType:options:animated:completion:)-218lh)

Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.

[`removeSymbolEffect(ofType:options:animated:completion:)`](/documentation/UIKit/UIImageView/removeSymbolEffect(ofType:options:animated:completion:)-31zec)

Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.

[`removeSymbolEffect(ofType:options:animated:completion:)`](/documentation/UIKit/UIImageView/removeSymbolEffect(ofType:options:animated:completion:)-2boi2)

Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.

[`removeAllSymbolEffects(options:animated:)`](/documentation/UIKit/UIImageView/removeAllSymbolEffects(options:animated:))

Removes all symbol effects from the image view, using the specified options and animation setting.

[`UISymbolEffectCompletion`](/documentation/UIKit/UISymbolEffectCompletion-7qt7g)

A completion handler for adding and removing symbol effects and transitions.

[`UISymbolEffectCompletionContext`](/documentation/UIKit/UISymbolEffectCompletionContext-swift.struct)

Information about a symbol effect’s addition or removal.

[`-  addSymbolEffect:`](/documentation/UIKit/UIImageView/addSymbolEffect:)

Adds a symbol effect to the image view with default options and animation.

[`-  addSymbolEffect:options:`](/documentation/UIKit/UIImageView/addSymbolEffect:options:)

Adds a symbol effect to the image view with the specified options and default animation.

[`-  addSymbolEffect:options:animated:`](/documentation/UIKit/UIImageView/addSymbolEffect:options:animated:)

Adds a symbol effect to the image view with the specified options and animation.

[`-  addSymbolEffect:options:animated:completion:`](/documentation/UIKit/UIImageView/addSymbolEffect:options:animated:completion:)

Adds a symbol effect to the image view with the specified options, animation, and completion handler.

[`-  setSymbolImage:withContentTransition:`](/documentation/UIKit/UIImageView/setSymbolImage:withContentTransition:)

Sets a symbol image using the specified content-transition effect.

[`-  setSymbolImage:withContentTransition:options:`](/documentation/UIKit/UIImageView/setSymbolImage:withContentTransition:options:)

Sets a symbol image using the specified content-transition effect and options.

[`-  setSymbolImage:withContentTransition:options:completion:`](/documentation/UIKit/UIImageView/setSymbolImage:withContentTransition:options:completion:)

Sets a symbol image using the specified content-transition effect, options, and completion handler.

[`-  removeSymbolEffectOfType:`](/documentation/UIKit/UIImageView/removeSymbolEffectOfType:)

Removes the symbol effect that matches the specified effect type.

[`-  removeSymbolEffectOfType:options:`](/documentation/UIKit/UIImageView/removeSymbolEffectOfType:options:)

Removes the symbol effect that matches the specified effect type, using the specified options.

[`-  removeSymbolEffectOfType:options:animated:`](/documentation/UIKit/UIImageView/removeSymbolEffectOfType:options:animated:)

Removes the symbol effect that matches the specified effect type, using the specified options and animation setting.

[`-  removeSymbolEffectOfType:options:animated:completion:`](/documentation/UIKit/UIImageView/removeSymbolEffectOfType:options:animated:completion:)

Removes the symbol effect that matches the specified effect type, using the specified options, animation setting, and completion handler.

[`-  removeAllSymbolEffects`](/documentation/UIKit/UIImageView/removeAllSymbolEffects)

Removes all symbol effects from the image view.

[`-  removeAllSymbolEffectsWithOptions:`](/documentation/UIKit/UIImageView/removeAllSymbolEffectsWithOptions:)

Removes all symbol effects from the image view, using the specified options.

[`-  removeAllSymbolEffectsWithOptions:animated:`](/documentation/UIKit/UIImageView/removeAllSymbolEffectsWithOptions:animated:)

Removes all symbol effects from the image view, using the specified options and animation setting.

[`UISymbolEffectCompletion`](/documentation/UIKit/UISymbolEffectCompletion-6rxwa)

A completion handler for adding and removing symbol effects and transitions.

[`UISymbolEffectCompletionContext`](/documentation/UIKit/UISymbolEffectCompletionContext-c.class)

Information about a symbol effect’s addition or removal.

### Transitioning between symbol effects

[`UISymbolContentTransition`](/documentation/UIKit/UISymbolContentTransition)

Represents a symbol content transition and options.

### Managing focus-related behaviors

[`adjustsImageWhenAncestorFocused`](/documentation/UIKit/UIImageView/adjustsImageWhenAncestorFocused)

A Boolean value that determines whether the image view responds when an ancestor gains focus.

[`focusedFrameGuide`](/documentation/UIKit/UIImageView/focusedFrameGuide)

The layout guide to use when the image view is focused.

[`masksFocusEffectToContents`](/documentation/UIKit/UIImageView/masksFocusEffectToContents)

A Boolean value indicating whether the floating focused appearance uses the image’s alpha channel.

### Layering content on top of the image view

[`overlayContentView`](/documentation/UIKit/UIImageView/overlayContentView)

A view for hosting layered content on top of the image view.

### Specifying the dynamic range

[`imageDynamicRange`](/documentation/UIKit/UIImageView/imageDynamicRange)

The resolved treatment to use for HDR images.

[`preferredImageDynamicRange`](/documentation/UIKit/UIImageView/preferredImageDynamicRange)

The preferred treatment to use for HDR images. By default the image view will defer to the value from its traitCollection.

[`DynamicRange`](/documentation/UIKit/UIImage/DynamicRange)

## Relationships

### Conforms To

[`UIPasteConfigurationSupporting`](/documentation/UIKit/UIPasteConfigurationSupporting)

[`UIAccessibilityContentSizeCategoryImageAdjusting`](/documentation/UIKit/UIAccessibilityContentSizeCategoryImageAdjusting)

[`UIActivityItemsConfigurationProviding`](/documentation/UIKit/UIActivityItemsConfigurationProviding)

[`Hashable`](/documentation/Swift/Hashable)

[`UITraitChangeObservable-67e94`](/documentation/UIKit/UITraitChangeObservable-67e94)

[`Escapable`](/documentation/Swift/Escapable)

[`UIFocusItemContainer`](/documentation/UIKit/UIFocusItemContainer)

[`UIAccessibilityIdentification`](/documentation/UIKit/UIAccessibilityIdentification)

[`Copyable`](/documentation/Swift/Copyable)

[`CMBodyIdentifiable`](/documentation/CoreMotion/CMBodyIdentifiable)

[`CALayerDelegate`](/documentation/QuartzCore/CALayerDelegate)

[`NSObjectProtocol`](/documentation/ObjectiveC/NSObjectProtocol)

[`UIAppearance`](/documentation/UIKit/UIAppearance)

[`NSCoding`](/documentation/Foundation/NSCoding)

[`UIFocusItem`](/documentation/UIKit/UIFocusItem)

[`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)

[`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)

[`SendableMetatype`](/documentation/Swift/SendableMetatype)

[`UIResponderStandardEditActions`](/documentation/UIKit/UIResponderStandardEditActions)

[`Sendable`](/documentation/Swift/Sendable)

[`UICoordinateSpace`](/documentation/UIKit/UICoordinateSpace)

[`UIPopoverPresentationControllerSourceItem`](/documentation/UIKit/UIPopoverPresentationControllerSourceItem)

[`Equatable`](/documentation/Swift/Equatable)

[`CVarArg`](/documentation/Swift/CVarArg)

[`UITraitEnvironment`](/documentation/UIKit/UITraitEnvironment)

[`NSTouchBarProvider`](/documentation/AppKit/NSTouchBarProvider)

[`UILargeContentViewerItem`](/documentation/UIKit/UILargeContentViewerItem)

[`UIUserActivityRestoring`](/documentation/UIKit/UIUserActivityRestoring)

[`UIDynamicItem`](/documentation/UIKit/UIDynamicItem)

[`CLBodyIdentifiable`](/documentation/CoreLocation/CLBodyIdentifiable)

[`UIFocusEnvironment`](/documentation/UIKit/UIFocusEnvironment)

[`UIAppearanceContainer`](/documentation/UIKit/UIAppearanceContainer)

### Inherits From

[`UIView`](/documentation/UIKit/UIView)

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
