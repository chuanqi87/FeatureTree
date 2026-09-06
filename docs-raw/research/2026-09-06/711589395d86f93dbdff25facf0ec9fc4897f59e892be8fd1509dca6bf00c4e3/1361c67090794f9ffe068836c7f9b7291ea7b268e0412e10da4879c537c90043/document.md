# Drag and Drop

Support the direct manipulation of your app’s content using drag and drop.

## Discussion

With very little programming on your part, custom-view objects can be dragged and dropped anywhere. Objects become part of this dragging mechanism by conforming to dragging protocols: Draggable objects conform to the [`NSDraggingSource`](/documentation/AppKit/NSDraggingSource) protocol, and destination objects (that is, receivers of a drop) conform to the [`NSDraggingDestination`](/documentation/AppKit/NSDraggingDestination) protocol. AppKit hides all the details of tracking the cursor and displaying the dragged image.

> Note:
> To learn how to adopt drag and drop in your iOS app, see <doc://com.apple.documentation/documentation/UIKit/drag-and-drop>.

To learn how to use drag and drop for an image view, see [Supporting Drag and Drop Through File Promises](/documentation/AppKit/supporting-drag-and-drop-through-file-promises). To use drag and drop in a table view, see [Supporting Table View Drag and Drop Through File Promises](/documentation/AppKit/supporting-table-view-drag-and-drop-through-file-promises). For an example of drag and drop in a collection view, see [Supporting Collection View Drag and Drop Through File Promises](/documentation/AppKit/supporting-collection-view-drag-and-drop-through-file-promises), and for an outline view: [Navigating Hierarchical Data Using Outline and Split Views](/documentation/AppKit/navigating-hierarchical-data-using-outline-and-split-views).

## Topics

### Drag Sources

Originate content from a drag source by creating items to represent that content.

[`NSDraggingSource`](/documentation/AppKit/NSDraggingSource)

A set of methods that are implemented by the source object in a dragging session.

[`NSDraggingItem`](/documentation/AppKit/NSDraggingItem)

A single dragged item within a dragging session.

[`NSDraggingSession`](/documentation/AppKit/NSDraggingSession)

An object that encapsulates a drag-and-drop action.

[`NSDraggingImageComponent`](/documentation/AppKit/NSDraggingImageComponent)

A single object in a dragging item.

### Drop Targets

Receive dragged content in your app’s objects.

[`NSDraggingDestination`](/documentation/AppKit/NSDraggingDestination)

A set of methods that the destination object (or recipient) of a dragged image must implement.

[`NSDraggingInfo`](/documentation/AppKit/NSDraggingInfo)

A set of methods that supply information about a dragging session.

[`NSSpringLoadingDestination`](/documentation/AppKit/NSSpringLoadingDestination)

A set of methods that the destination object (or recipient) of a dragged object can implement to support spring-loading.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
