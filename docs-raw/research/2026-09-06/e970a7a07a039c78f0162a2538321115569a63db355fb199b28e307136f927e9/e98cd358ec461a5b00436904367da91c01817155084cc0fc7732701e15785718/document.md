# Drag and drop

Bring drag and drop to your app by using interaction APIs with your views.

## Discussion

With drag and drop in iOS, users can drag items from one onscreen location to another using continuous gestures. A drag-and-drop activity can take place in a single app, or it can start in one app and end in another.

![A video that demonstrates dragging an image into Messages app.](videos/com.apple.uikit/drag-and-drop-1.mp4)

> Note:
> Prior to iOS 15, drag-and-drop activities on iPhone can take place in a single app but not between two apps.

The app from which an item is dragged is the *source app*. The app on which an item is dropped is the *destination app*. For drag and drop in a single app, that app plays both roles simultaneously. The complete user action from start to finish — using system-mediated gestures — is a *drag activity*. A *drag session*, by contrast, is an object that’s managed by the system and that manages the items the user is dragging.

When dragging is in progress, the source and destination apps continue to run normally and support user interaction. A user can invoke the Dock, return to the Home screen, open a second app in Split View, and even start another drag activity.

Unlike in macOS, iOS drag and drop supports multiple simultaneous drag activities—as many as the user’s fingers can handle. You can design your app so that the user can sequentially add drag items to an in-progress drag session, and a destination app can accept multiple, simultaneous drops.

Text views and text fields automatically support drag and drop. Collection views and table views offer dedicated, view-specific methods and properties, and text views offer APIs for customizing the views’ drag-and-drop behavior. You can configure any custom view to support drag and drop.

> Note:
> The system handles all security aspects of inter-app drag and drop in iOS. You don’t need to perform additional configuration like setting special entitlements or `Info.plist` keys.

## Topics

### Essentials

[Understanding a drag item as a promise](/documentation/UIKit/understanding-a-drag-item-as-a-promise)

Use drag items to convey data representation promises between a source app and a destination app.

[Making a view into a drag source](/documentation/UIKit/making-a-view-into-a-drag-source)

Adopt drag interaction APIs to provide items for dragging.

[Making a view into a drop destination](/documentation/UIKit/making-a-view-into-a-drop-destination)

Adopt drop interaction APIs to selectively consume dragged content.

[Adopting drag and drop in a custom view](/documentation/UIKit/adopting-drag-and-drop-in-a-custom-view)

Demonstrates how to enable drag and drop for a `UIImageView` instance.

[Adopting drag and drop in a table view](/documentation/UIKit/adopting-drag-and-drop-in-a-table-view)

Demonstrates how to enable and implement drag and drop for a table view.

### Drag and drop interactions

Add interactions to your views to make them drag sources or drop destinations.

[`UIDragInteractionDelegate`](/documentation/UIKit/UIDragInteractionDelegate)

The interface for configuring and controlling a drag interaction.

[`UIDropInteractionDelegate`](/documentation/UIKit/UIDropInteractionDelegate)

The interface for configuring and controlling a drop interaction.

[`UIDragInteraction`](/documentation/UIKit/UIDragInteraction)

An interaction to enable dragging of items from a view, employing a delegate to provide drag items and to respond to calls from the drag session.

[`UIDropInteraction`](/documentation/UIKit/UIDropInteraction)

An interaction to enable dropping of items onto a view, employing a delegate to instantiate objects and respond to calls from the drop session.

### Spring-loaded interactions

Enable spring loading to support drag and drop for your navigable UI.

[`UISpringLoadedInteractionBehavior`](/documentation/UIKit/UISpringLoadedInteractionBehavior)

The interface for specifying the behavior of a spring-loaded interaction.

[`UISpringLoadedInteractionSupporting`](/documentation/UIKit/UISpringLoadedInteractionSupporting)

The interface that determines if an object supports a spring-loaded interaction for drag and drop activities.

[`UISpringLoadedInteraction`](/documentation/UIKit/UISpringLoadedInteraction)

An interaction object for configuring and controlling spring-loaded, user-driven navigation during a drag activity.

[`UISpringLoadedInteractionContext`](/documentation/UIKit/UISpringLoadedInteractionContext)

The interface an object implements to provide information about a spring-loaded interaction.

[`UISpringLoadedInteractionEffect`](/documentation/UIKit/UISpringLoadedInteractionEffect)

The interface for providing visual styling to a spring-loaded interaction based on the interaction state.

### Drag sources

Specify drag items for drag and drop.

[`UIDragItem`](/documentation/UIKit/UIDragItem)

A representation of an underlying data item as a person drags it from one location to another.

[`UIDragDropSession`](/documentation/UIKit/UIDragDropSession)

The common interface for querying the state of both drag sessions and drop sessions.

[`UIDragSession`](/documentation/UIKit/UIDragSession)

The interface for configuring a drag session.

[`UIDragAnimating`](/documentation/UIKit/UIDragAnimating)

The interface for providing custom animation alongside the system’s lift, drop, and cancellation animations.

### Drop destinations

Specify how a destination view consumes drag items.

[`UIDropSession`](/documentation/UIKit/UIDropSession)

The interface for querying a drop session about its state and associated drag items.

[`UIDropProposal`](/documentation/UIKit/UIDropProposal)

A configuration for the behavior of a drop interaction, required if a view accepts drop activities.

[`UIDropOperation`](/documentation/UIKit/UIDropOperation)

Operation types that determine how a drag and drop activity resolves when the user drops a drag item.

[`UIDropSessionProgressIndicatorStyle`](/documentation/UIKit/UIDropSessionProgressIndicatorStyle)

The drop-progress indicator styles for the drop session, used while data is moving from the source to the destination.

### Item providers

Work with data-representation promises for drag and drop.

[Data delivery with drag and drop](/documentation/UIKit/data-delivery-with-drag-and-drop)

Share data between iPad apps during a drag and drop operation using an item provider.

  <doc://com.apple.documentation/documentation/Foundation/NSItemProvider>

  <doc://com.apple.documentation/documentation/Foundation/NSItemProviderReading>

  <doc://com.apple.documentation/documentation/Foundation/NSItemProviderWriting>

[`UIItemProviderPresentationSizeProviding`](/documentation/UIKit/UIItemProviderPresentationSizeProviding)

[`UIItemProviderReadingAugmentationDesignating`](/documentation/UIKit/UIItemProviderReadingAugmentationDesignating)

[`UIItemProviderReadingAugmentationProviding`](/documentation/UIKit/UIItemProviderReadingAugmentationProviding)

### Pasteboard support

Simplify the requesting and consuming of appropriate data representations for pasted and dropped items.

[`UIPasteConfiguration`](/documentation/UIKit/UIPasteConfiguration)

The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.

[`UIPasteConfigurationSupporting`](/documentation/UIKit/UIPasteConfigurationSupporting)

The interface that determines whether a responder object supports paste configuration.

### Custom drag item previews

Apply customizations to make drag item previews more appealing and meaningful to the user.

[`UIDragPreviewParameters`](/documentation/UIKit/UIDragPreviewParameters)

A set of parameters for adjusting the appearance of a drag item preview or a targeted drag item preview.

[`UIDragPreview`](/documentation/UIKit/UIDragPreview)

A graphical preview for a single drag item, used by the system after a drag has started and when no related animation is running.

[`UIDragPreviewTarget`](/documentation/UIKit/UIDragPreviewTarget)

A geometric specification for the source or destination of a drag item preview, used by the system when a user drops items or cancels a drag activity.

[`UITargetedDragPreview`](/documentation/UIKit/UITargetedDragPreview)

A drag item preview used by the system during lift, drop, or cancellation animation.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
