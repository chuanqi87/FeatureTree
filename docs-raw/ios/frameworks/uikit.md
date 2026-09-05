* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/uikit#app-main)

Framework

# UIKit

Construct and manage a graphical, event-driven user interface for your iOS, iPadOS, or tvOS app.

iOS 2.0+iPadOS 2.0+Mac Catalyst 13.0+tvOS 9.0+visionOS 1.0+watchOS 2.0+

## [Overview](https://developer.apple.com/documentation/uikit\#overview)

UIKit provides a variety of features for building apps, including components you can use to construct the core infrastructure of your iOS, iPadOS, or tvOS apps. The framework provides the window and view architecture for implementing your UI, the event-handling infrastructure for delivering Multi-Touch and other types of input to your app, and the main run loop for managing interactions between the user, the system, and your app.

![An image of the Landmarks sample app on iPad and iPhone showing the Mount Fuji landmark.](https://developer.apple.com/tutorials/images/com.apple.uikit/Landmarks-Building-an-app-with-Liquid-Glass-1@2x.png)

UIKit also includes support for animations, documents, drawing and printing, text management and display, search, app extensions, resource management, and getting information about the current device. You can also customize accessibility support, and localize your app’s interface for different languages, countries, or cultural regions.

UIKit works seamlessly with the [SwiftUI](https://developer.apple.com/documentation/swiftui) framework, so you can implement parts of your UIKit app in SwiftUI or mix interface elements between the two frameworks. For example, you can place UIKit views and view controllers inside SwiftUI views, and vice versa.

To build a macOS app, you can use [SwiftUI](https://developer.apple.com/documentation/swiftui) to create an app that works across all of Apple’s platforms, or use [AppKit](https://developer.apple.com/documentation/appkit) to create an app for Mac only. Alternatively, you can bring your UIKit iPad app to the Mac with [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac-catalyst).

## [Topics](https://developer.apple.com/documentation/uikit\#topics)

### [Essentials](https://developer.apple.com/documentation/uikit\#Essentials)

[Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)

Find out how to bring the new material to your app.

[UIKit updates](https://developer.apple.com/documentation/updates/uikit)

Learn about important changes to UIKit.

[About app development with UIKit](https://developer.apple.com/documentation/uikit/about-app-development-with-uikit)

Learn about the basic support that UIKit and Xcode provide for your iOS and tvOS apps.

[API Reference\\
Protecting the User’s Privacy](https://developer.apple.com/documentation/uikit/protecting-the-user-s-privacy)

Secure personal data, and respect user preferences for how data is used.

### [App structure](https://developer.apple.com/documentation/uikit\#App-structure)

UIKit manages your app’s interactions with the system and provides classes for you to manage your app’s data and resources.

[API Reference\\
App and environment](https://developer.apple.com/documentation/uikit/app-and-environment)

Manage life-cycle events and your app’s UI scenes, and get information about traits and the environment in which your app runs.

[API Reference\\
Documents, data, and pasteboard](https://developer.apple.com/documentation/uikit/documents-data-and-pasteboard)

Organize your app’s data and share that data on the pasteboard.

[API Reference\\
Resource management](https://developer.apple.com/documentation/uikit/resource-management)

Manage the images, strings, storyboards, and nib files that you use to implement your app’s interface.

[API Reference\\
App extensions](https://developer.apple.com/documentation/uikit/app-extensions)

Extend your app’s basic functionality to other parts of the system.

[API Reference\\
Interprocess communication](https://developer.apple.com/documentation/uikit/interprocess-communication)

Display activity-based services to people.

[API Reference\\
Mac Catalyst](https://developer.apple.com/documentation/uikit/mac-catalyst)

Create a version of your iPad app that users can run on a Mac device.

### [User interface](https://developer.apple.com/documentation/uikit\#User-interface)

Views help you display content onscreen and facilitate user interactions; view controllers help you manage views and the structure of your interface.

[API Reference\\
Views and controls](https://developer.apple.com/documentation/uikit/views-and-controls)

Present your content onscreen and define the interactions allowed with that content.

[API Reference\\
View controllers](https://developer.apple.com/documentation/uikit/view-controllers)

Manage your interface using view controllers and facilitate navigation around your app’s content.

[API Reference\\
View layout](https://developer.apple.com/documentation/uikit/view-layout)

Use stack views to lay out the views of your interface automatically. Use Auto Layout when you require precise placement of your views.

[API Reference\\
Appearance customization](https://developer.apple.com/documentation/uikit/appearance-customization)

Apply Liquid Glass to views, support Dark Mode in your app, customize the appearance of bars, and use appearance proxies to modify your UI.

[API Reference\\
Animation and haptics](https://developer.apple.com/documentation/uikit/animation-and-haptics)

Provide feedback to users using view-based animations and haptics.

[API Reference\\
Windows and screens](https://developer.apple.com/documentation/uikit/windows-and-screens)

Provide a container for your view hierarchies and other content.

### [User interactions](https://developer.apple.com/documentation/uikit\#User-interactions)

Responders and gesture recognizers help you handle touches and other events. Drag and drop, focus, peek and pop, and accessibility handle other user interactions.

[API Reference\\
Touches, presses, and gestures](https://developer.apple.com/documentation/uikit/touches-presses-and-gestures)

Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.

[API Reference\\
Menus and shortcuts](https://developer.apple.com/documentation/uikit/menus-and-shortcuts)

Simplify interactions with your app using menu systems, contextual menus, Home Screen quick actions, and keyboard shortcuts.

[API Reference\\
Drag and drop](https://developer.apple.com/documentation/uikit/drag-and-drop)

Bring drag and drop to your app by using interaction APIs with your views.

[API Reference\\
Pointer interactions](https://developer.apple.com/documentation/uikit/pointer-interactions)

Support pointer interactions in your custom controls and views.

[API Reference\\
Apple Pencil interactions](https://developer.apple.com/documentation/uikit/apple-pencil-interactions)

Handle user interactions like double tap and squeeze on Apple Pencil.

[API Reference\\
Focus-based navigation](https://developer.apple.com/documentation/uikit/focus-based-navigation)

Navigate the interface of your UIKit app using a remote, game controller, or keyboard.

[API Reference\\
Accessibility for UIKit](https://developer.apple.com/documentation/uikit/accessibility-for-uikit)

Make your UIKit apps accessible to everyone who uses iOS and tvOS.

### [Graphics, drawing, and printing](https://developer.apple.com/documentation/uikit\#Graphics-drawing-and-printing)

UIKit provides classes and protocols that help you configure your drawing environment and render your content.

[API Reference\\
Images and PDF](https://developer.apple.com/documentation/uikit/images-and-pdf)

Create and manage images, including those that use bitmap and PDF formats.

[API Reference\\
Drawing](https://developer.apple.com/documentation/uikit/drawing)

Configure your app’s drawing environment using colors, renderers, draw paths, strings, and shadows.

[API Reference\\
Printing](https://developer.apple.com/documentation/uikit/printing)

Display the system print panels and manage the printing process.

### [Text](https://developer.apple.com/documentation/uikit\#Text)

In addition to text views that simplify displaying text in your app, UIKit provides custom text management and rendering that supports the system keyboards.

[API Reference\\
Text display and fonts](https://developer.apple.com/documentation/uikit/text-display-and-fonts)

Display text, manage fonts, and check spelling.

[API Reference\\
TextKit](https://developer.apple.com/documentation/uikit/textkit)

Manage text storage and perform custom layout of text-based content in your app’s views.

[API Reference\\
Keyboards and input](https://developer.apple.com/documentation/uikit/keyboards-and-input)

Configure the system keyboard, create your own keyboards to handle input, or detect key presses on a physical keyboard.

[API Reference\\
Writing Tools](https://developer.apple.com/documentation/uikit/writing-tools)

Add support for Writing Tools to your app’s text views.

[API Reference\\
Handwriting recognition](https://developer.apple.com/documentation/uikit/handwriting-recognition)

Configure text fields and custom views that accept text to handle input from Apple Pencil.

### [Deprecated](https://developer.apple.com/documentation/uikit\#Deprecated)

Avoid using deprecated classes and protocols in your apps.

[API Reference\\
Deprecated symbols](https://developer.apple.com/documentation/uikit/deprecated-symbols)

Review unsupported symbols and their replacements.

### [Reference](https://developer.apple.com/documentation/uikit\#Reference)

[API Reference\\
UIKit Enumerations](https://developer.apple.com/documentation/uikit/uikit-enumerations)

[API Reference\\
UIKit Constants](https://developer.apple.com/documentation/uikit/uikit-constants)

This document describes constants that are used throughout the UIKit framework.

[API Reference\\
UIKit Data Types](https://developer.apple.com/documentation/uikit/uikit-data-types)

The UIKit framework defines data types that are used in multiple places throughout the framework.

[API Reference\\
UIKit Functions](https://developer.apple.com/documentation/uikit/uikit-functions)

The UIKit framework defines a number of functions, many of them used in graphics and drawing operations.

### [Protocols](https://developer.apple.com/documentation/uikit\#Protocols)

[`protocol UITraitBridgedEnvironmentKey`](https://developer.apple.com/documentation/uikit/uitraitbridgedenvironmentkey)

### [Structures](https://developer.apple.com/documentation/uikit\#Structures)

[`struct UIConfigurationTextAttributesTransformer`](https://developer.apple.com/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct)

Defines a text transformation that can affect the visual appearance of a string.

[`struct UITraitSystemPrefersReducedResourceUsage`](https://developer.apple.com/documentation/uikit/uitraitsystemprefersreducedresourceusage-swift.struct)

### [Macros](https://developer.apple.com/documentation/uikit\#Macros)

[`macro Preview<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> UIView)`](https://developer.apple.com/documentation/uikit/preview(_:traits:arguments:body:)-6gm4c)

[`macro Preview<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> UIViewController)`](https://developer.apple.com/documentation/uikit/preview(_:traits:arguments:body:)-7cbjv)

### [Enumerations](https://developer.apple.com/documentation/uikit\#Enumerations)

[`enum UITextGrammarCheckingType`](https://developer.apple.com/documentation/uikit/uitextgrammarcheckingtype) Beta

Current page is UIKit