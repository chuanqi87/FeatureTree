# UIViewController

An object that manages a view hierarchy for your UIKit app.

```
@MainActor class UIViewController
```

## Overview

The [`UIViewController`](/documentation/UIKit/UIViewController) class defines the shared behavior that’s common to all view controllers. You rarely create instances of the [`UIViewController`](/documentation/UIKit/UIViewController) class directly. Instead, you subclass [`UIViewController`](/documentation/UIKit/UIViewController) and add the methods and properties needed to manage the view controller’s view hierarchy.

A view controller’s main responsibilities include the following:

- Updating the contents of the views, usually in response to changes to the underlying data
- Responding to user interactions with views
- Resizing views and managing the layout of the overall interface
- Coordinating with other objects — including other view controllers — in your app

A view controller is tightly bound to the views it manages and takes part in handling events in its view hierarchy. Specifically, view controllers are [`UIResponder`](/documentation/UIKit/UIResponder) objects and are inserted into the responder chain between the view controller’s root view and that view’s superview, which typically belongs to a different view controller. If none of the view controller’s views handle an event, the view controller has the option of handling the event or passing it along to the superview.

View controllers are rarely used in isolation. Instead, you often use multiple view controllers, each of which owns a portion of your app’s user interface. For example, one view controller might display a table of items while a different view controller displays the selected item from that table. Usually, only the views from one view controller are visible at a time. A view controller may present a different view controller to display a new set of views, or it may act as a container for other view controllers’ content and animate views however it wants.

### Subclassing notes

Every app contains at least one custom subclass of [`UIViewController`](/documentation/UIKit/UIViewController). More often, apps contain many custom view controllers. Custom view controllers define the overall behaviors of your app, including the app’s appearance and how it responds to user interactions. The following sections provide a brief overview of some of the tasks your custom subclass performs. For detailed information about using and implementing view controllers, see [View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457).

#### Manage views

Each view controller manages a view hierarchy, the root view of which is stored in the [`view`](/documentation/UIKit/UIViewController/view) property of this class. The root view acts primarily as a container for the rest of the view hierarchy. The size and position of the root view is determined by the object that owns it, which is either a parent view controller or the app’s window. The view controller that’s owned by the window is the app’s root view controller and its view is sized to fill the window.

View controllers load their views lazily. Accessing the [`view`](/documentation/UIKit/UIViewController/view) property for the first time loads or creates the view controller’s views. There are several ways to specify the views for a view controller:

- Specify the view controller and its views in your app’s storyboard. Storyboards are the preferred way to specify your views. With a storyboard, you specify the views and their connections to the view controller. You also specify the relationships and segues between your view controllers, which makes it easier to see and modify your app’s behavior.

To load a view controller from a storyboard, call the [`instantiateViewController(withIdentifier:)`](/documentation/UIKit/UIStoryboard/instantiateViewController(withIdentifier:)) method of the appropriate [`UIStoryboard`](/documentation/UIKit/UIStoryboard) object. The storyboard object creates the view controller and returns it to your code.

- Specify the views for a view controller using a nib file. A nib file lets you specify the views of a single view controller but doesn’t let you define segues or relationships between view controllers. The nib file also stores only minimal information about the view controller itself.

To initialize a view controller object using a nib file, create your view controller class programmatically and initialize it using the [`init(nibName:bundle:)`](/documentation/UIKit/UIViewController/init(nibName:bundle:)) method. When its views are requested, the view controller loads them from the nib file.

- Specify the views for a view controller using the [`loadView()`](/documentation/UIKit/UIViewController/loadView()) method. In that method, create your view hierarchy programmatically and assign the root view of that hierarchy to the view controller’s [`view`](/documentation/UIKit/UIViewController/view) property.

All of these techniques have the same end result, which is to create the appropriate set of views and expose them through the [`view`](/documentation/UIKit/UIViewController/view) property.

> Important:
> A view controller is the sole owner of its view and any subviews it creates. It’s responsible for creating those views and for relinquishing ownership of them at the appropriate times such as when the view controller itself is released. If you use a storyboard or a nib file to store your view objects, each view controller object automatically gets its own copy of these views when the view controller asks for them. However, if you create your views manually, each view controller must have its own unique set of views. You can’t share views between view controllers.

A view controller’s root view is always sized to fit its assigned space. For other views in your view hierarchy, use Interface Builder to specify the Auto Layout constraints that govern how each view is positioned and sized within its superview’s bounds. You can also create constraints programmatically and add them to your views at appropriate times. For more information about how to create constraints, see [Auto Layout Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853).

##### Handle view-related notifications

When the visibility of its views changes, a view controller automatically calls its own methods so that subclasses can respond to the change. Use a method like [`viewIsAppearing(_:)`](/documentation/UIKit/UIViewController/viewIsAppearing(_:)) to prepare your views to appear onscreen, and use [`viewWillDisappear(_:)`](/documentation/UIKit/UIViewController/viewWillDisappear(_:)) to save changes or other state information. Use other methods to make appropriate changes.

The following image shows the possible visible states for a view controller’s views and the state transitions that can occur. Not all `will` callback methods are paired with only a `did` callback method. You need to ensure that if you start a process in a `will` callback method, you end the process in both the corresponding `did` and the opposite `will` callback method.

![A diagram of four spheres arranged in a circle. The sphere on the right is labeled Appearing and has a clockwise arrow leading to the bottom sphere, which is labeled Appeared. A small dot on the arrow is labeled viewDidAppear. A clockwise arrow leads from the bottom sphere to the left sphere, which is labeled Disappearing. A small dot along the arrow is labeled viewWillDisappear. A clockwise arrow leads from the left sphere to the top sphere, which is labeled Disappeared. Two small dots along the arrow are labeled viewDidDisappear and View removed. A clockwise arrow leads from the top sphere to the right sphere. Three small dots along the arrow are labeled viewWillAppear, View added, and viewIsAppearing.](images/com.apple.uikit/media-1965800@2x.png)

##### Handle view rotations

As of iOS 8, all rotation-related methods are deprecated. Instead, rotations are treated as a change in the size of the view controller’s view and are therefore reported using the [`viewWillTransition(to:with:)`](/documentation/UIKit/UIContentContainer/viewWillTransition(to:with:)) method. When the interface orientation changes, UIKit calls this method on the window’s root view controller. That view controller then notifies its child view controllers, propagating the message throughout the view controller hierarchy.

In iOS 6 and iOS 7, your app supports the interface orientations defined in your app’s `Info.plist` file. A view controller can override the [`supportedInterfaceOrientations`](/documentation/UIKit/UIViewController/supportedInterfaceOrientations) method to limit the list of supported orientations. Typically, the system calls this method only on the root view controller of the window or a view controller presented to fill the entire screen; child view controllers use the portion of the window provided for them by their parent view controller and no longer participate directly in decisions about what rotations are supported. The intersection of the app’s orientation mask and the view controller’s orientation mask is used to determine which orientations a view controller can be rotated into.

You can override the [`preferredInterfaceOrientationForPresentation`](/documentation/UIKit/UIViewController/preferredInterfaceOrientationForPresentation) for a view controller that’s intended to be presented full screen in a specific orientation.

When a rotation occurs for a visible view controller, the [`willRotate(to:duration:)`](/documentation/UIKit/UIViewController/willRotate(to:duration:)), [`willAnimateRotation(to:duration:)`](/documentation/UIKit/UIViewController/willAnimateRotation(to:duration:)), and [`didRotate(from:)`](/documentation/UIKit/UIViewController/didRotate(from:)) methods are called during the rotation. The [`viewWillLayoutSubviews()`](/documentation/UIKit/UIViewController/viewWillLayoutSubviews()) method is also called after the view is resized and positioned by its parent. If a view controller isn’t visible when an orientation change occurs, then the rotation methods are never called. However, the [`viewWillLayoutSubviews()`](/documentation/UIKit/UIViewController/viewWillLayoutSubviews()) method is called when the view becomes visible.

> Note:
> At launch time, apps should always set up their interface in a portrait orientation. After the ``doc://com.apple.uikit/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)`` method returns, the app uses the view controller rotation mechanism described above to rotate the views to the appropriate orientation prior to showing the window.

#### Implement a container view controller

A custom [`UIViewController`](/documentation/UIKit/UIViewController) subclass can also act as a container view controller. A container view controller manages the presentation of content of other view controllers it owns, also known as its child view controllers. A child’s view can be presented as-is or in conjunction with views owned by the container view controller.

Your container view controller subclass should declare a public interface to associate its children. The nature of these methods is up to you and depends on the semantics of the container you’re creating. You need to decide how many children can be displayed by your view controller at once, when those children are displayed, and where they appear in your view controller’s view hierarchy. Your view controller class defines what relationships, if any, are shared by the children. By establishing a clean public interface for your container, you ensure that children use its capabilities logically, without accessing too many private details about how your container implements the behavior.

Your container view controller must associate a child view controller with itself before adding the child’s root view to the view hierarchy. This allows iOS to properly route events to child view controllers and the views those controllers manage. Likewise, after it removes a child’s root view from its view hierarchy, it should disconnect that child view controller from itself. To make or break these associations, your container calls specific methods defined by the base class. These methods aren’t intended to be called by clients of your container class; they are to be used only by your container’s implementation to provide the expected containment behavior.

Here are the essential methods you might need to call:

- [`addChild(_:)`](/documentation/UIKit/UIViewController/addChild(_:))
- [`removeFromParent()`](/documentation/UIKit/UIViewController/removeFromParent())
- [`willMove(toParent:)`](/documentation/UIKit/UIViewController/willMove(toParent:))
- [`didMove(toParent:)`](/documentation/UIKit/UIViewController/didMove(toParent:))

> Note:
> You’re not required to override any methods when creating a container view controller.
> 
> By default, rotation and appearance callbacks are automatically forwarded to children. You may optionally override the ``doc://com.apple.uikit/documentation/UIKit/UIViewController/shouldAutomaticallyForwardRotationMethods()`` and ``doc://com.apple.uikit/documentation/UIKit/UIViewController/shouldAutomaticallyForwardAppearanceMethods`` methods to take control of this behavior yourself.

#### Manage memory

Memory is a critical resource in iOS, and view controllers provide built-in support for reducing their memory footprint at critical times. The [`UIViewController`](/documentation/UIKit/UIViewController) class provides some automatic handling of low-memory conditions through its [`didReceiveMemoryWarning()`](/documentation/UIKit/UIViewController/didReceiveMemoryWarning()) method, which releases unneeded memory.

#### Support state preservation and restoration

If you assign a value to the view controller’s [`restorationIdentifier`](/documentation/UIKit/UIViewController/restorationIdentifier) property, the system may ask the view controller to encode itself when the app transitions to the background. When preserved, a view controller preserves the state of any views in its view hierarchy that also have restoration identifiers. View controllers don’t automatically save any other state. If you’re implementing a custom container view controller, you must encode any child view controllers yourself. Each child you encode must have a unique restoration identifier.

For more information about how the system determines which view controllers to preserve and restore, see [App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072). To see an example of state preservation and restoration, see [Restoring your app’s state](/documentation/UIKit/restoring-your-app-s-state).

## Topics

### Creating a view controller

[`-  initWithNibName:bundle:`](/documentation/UIKit/UIViewController/init(nibName:bundle:))

Creates a view controller with the nib file in the specified bundle.

[`-  initWithCoder:`](/documentation/UIKit/UIViewController/init(coder:))

Creates a view controller with data in an unarchiver.

### Getting the storyboard and nib information

[`storyboard`](/documentation/UIKit/UIViewController/storyboard)

The storyboard from which the view controller originated.

[`nibName`](/documentation/UIKit/UIViewController/nibName)

The name of the view controller’s nib file, if one was specified.

[`nibBundle`](/documentation/UIKit/UIViewController/nibBundle)

The view controller’s nib bundle if it exists.

### Managing the view

[`view`](/documentation/UIKit/UIViewController/view)

The view that the controller manages.

[`viewIfLoaded`](/documentation/UIKit/UIViewController/viewIfLoaded)

The view controller’s view, or `nil` if the view isn’t yet loaded.

[`viewLoaded`](/documentation/UIKit/UIViewController/isViewLoaded)

A Boolean value indicating whether the view is currently loaded into memory.

[`-  loadView`](/documentation/UIKit/UIViewController/loadView())

Creates the view that the controller manages.

[`-  viewDidLoad`](/documentation/UIKit/UIViewController/viewDidLoad())

Called after the controller’s view is loaded into memory.

[`-  loadViewIfNeeded`](/documentation/UIKit/UIViewController/loadViewIfNeeded())

Loads the view controller’s view if it’s not loaded yet.

[`title`](/documentation/UIKit/UIViewController/title)

A localized string that represents the view this controller manages.

[`preferredContentSize`](/documentation/UIKit/UIViewController/preferredContentSize)

The preferred size for the view controller’s view.

[`ornaments`](/documentation/UIKit/UIViewController/ornaments)

SwiftUI ornaments to display adjacent to the view controller.

### Responding to view-related events

[`-  viewWillAppear:`](/documentation/UIKit/UIViewController/viewWillAppear(_:))

Notifies the view controller that its view is about to be added to a view hierarchy.

[`-  viewIsAppearing:`](/documentation/UIKit/UIViewController/viewIsAppearing(_:))

Notifies the view controller that the system is adding the view controller’s view to a view hierarchy.

[`-  viewDidAppear:`](/documentation/UIKit/UIViewController/viewDidAppear(_:))

Notifies the view controller that its view was added to a view hierarchy.

[`-  viewWillDisappear:`](/documentation/UIKit/UIViewController/viewWillDisappear(_:))

Notifies the view controller that its view is about to be removed from a view hierarchy.

[`-  viewDidDisappear:`](/documentation/UIKit/UIViewController/viewDidDisappear(_:))

Notifies the view controller that its view was removed from a view hierarchy.

[`beingDismissed`](/documentation/UIKit/UIViewController/isBeingDismissed)

A Boolean value indicating whether the view controller is in the process of being dismissed by one of its ancestors.

[`beingPresented`](/documentation/UIKit/UIViewController/isBeingPresented)

A Boolean value indicating whether the view controller in the process of being presented by one of its ancestors.

[`movingFromParentViewController`](/documentation/UIKit/UIViewController/isMovingFromParent)

A Boolean value indicating whether the view controller is moving from a parent view controller.

[`movingToParentViewController`](/documentation/UIKit/UIViewController/isMovingToParent)

A Boolean value indicating whether the view controller is moving to a parent view controller.

### Managing the view’s properties

[`ViewLoading`](/documentation/UIKit/UIViewController/ViewLoading)

A property wrapper that loads the view controller’s view before accessing the property.

[`-  updateProperties`](/documentation/UIKit/UIViewController/updateProperties())

Configures the view controller’s content and styling properties.

[`-  updatePropertiesIfNeeded`](/documentation/UIKit/UIViewController/updatePropertiesIfNeeded())

Forces an immediate properties update for this view controller and its view,
including any view controllers and views in this subtree.

[`-  setNeedsUpdateProperties`](/documentation/UIKit/UIViewController/setNeedsUpdateProperties())

Call to manually request a properties update for the view controller.
Multiple requests may be coalesced into a single update alongside the next layout pass.

### Extending the view’s safe area

[Positioning content relative to the safe area](/documentation/UIKit/positioning-content-relative-to-the-safe-area)

Position views so that they aren’t obstructed by other content.

[`additionalSafeAreaInsets`](/documentation/UIKit/UIViewController/additionalSafeAreaInsets)

Custom insets that you specify to modify the view controller’s safe area.

[`-  viewSafeAreaInsetsDidChange`](/documentation/UIKit/UIViewController/viewSafeAreaInsetsDidChange())

Called to notify the view controller that the safe area insets of its root view changed.

### Managing the view’s margins

[Positioning content within layout margins](/documentation/UIKit/positioning-content-within-layout-margins)

Position views so that they aren’t crowded by other content.

[`viewRespectsSystemMinimumLayoutMargins`](/documentation/UIKit/UIViewController/viewRespectsSystemMinimumLayoutMargins)

A Boolean value indicating whether the view controller’s view uses the system-defined minimum layout margins.

[`systemMinimumLayoutMargins`](/documentation/UIKit/UIViewController/systemMinimumLayoutMargins)

The minimum layout margins for the view controller’s root view.

[`-  viewLayoutMarginsDidChange`](/documentation/UIKit/UIViewController/viewLayoutMarginsDidChange())

Called to notify the view controller that the layout margins of its root view changed.

### Configuring the view’s layout behavior

[`edgesForExtendedLayout`](/documentation/UIKit/UIViewController/edgesForExtendedLayout)

The edges that you extend for your view controller.

[`UIRectEdge`](/documentation/UIKit/UIRectEdge)

Constants that specify the edges of a rectangle.

[`extendedLayoutIncludesOpaqueBars`](/documentation/UIKit/UIViewController/extendedLayoutIncludesOpaqueBars)

A Boolean value indicating whether or not the extended layout includes opaque bars.

[`-  viewWillLayoutSubviews`](/documentation/UIKit/UIViewController/viewWillLayoutSubviews())

Notifies the view controller that its view is about to lay out its subviews.

[`-  viewDidLayoutSubviews`](/documentation/UIKit/UIViewController/viewDidLayoutSubviews())

Notifies the view controller when its view finishes laying out its subviews.

[`-  updateViewConstraints`](/documentation/UIKit/UIViewController/updateViewConstraints())

Notifies the view controller when its view needs to update its constraints.

### Configuring the view rotation settings

[`supportedInterfaceOrientations`](/documentation/UIKit/UIViewController/supportedInterfaceOrientations)

The interface orientations that the view controller supports.

[`preferredInterfaceOrientationForPresentation`](/documentation/UIKit/UIViewController/preferredInterfaceOrientationForPresentation)

The interface orientation to use when presenting the view controller.

[`-  setNeedsUpdateOfSupportedInterfaceOrientations`](/documentation/UIKit/UIViewController/setNeedsUpdateOfSupportedInterfaceOrientations())

Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.

[`prefersInterfaceOrientationLocked`](/documentation/UIKit/UIViewController/prefersInterfaceOrientationLocked)

A Boolean value that indicates whether the view controller prefers to lock the scene’s interface orientation when the scene is visible.

[`-  setNeedsUpdateOfPrefersInterfaceOrientationLocked`](/documentation/UIKit/UIViewController/setNeedsUpdateOfPrefersInterfaceOrientationLocked())

Indicates that the view controller changed the interface orientation lock preference.

[`childViewControllerForInterfaceOrientationLock`](/documentation/UIKit/UIViewController/childForInterfaceOrientationLock)

A child view controller to query for the interface orientation lock preference.

### Performing segues

[`-  shouldPerformSegueWithIdentifier:sender:`](/documentation/UIKit/UIViewController/shouldPerformSegue(withIdentifier:sender:))

Determines whether the segue with the specified identifier should be performed.

[`-  prepareForSegue:sender:`](/documentation/UIKit/UIViewController/prepare(for:sender:))

Notifies the view controller that a segue is about to be performed.

[`-  performSegueWithIdentifier:sender:`](/documentation/UIKit/UIViewController/performSegue(withIdentifier:sender:))

Initiates the segue with the specified identifier from the current view controller’s storyboard file.

[`-  allowedChildViewControllersForUnwindingFromSource:`](/documentation/UIKit/UIViewController/allowedChildrenForUnwinding(from:))

Returns an array of child view controllers to search for an unwind segue destination.

[`-  childViewControllerContainingSegueSource:`](/documentation/UIKit/UIViewController/childContaining(_:))

Returns the child view controller that contains the source of the unwind segue.

[`-  canPerformUnwindSegueAction:fromViewController:sender:`](/documentation/UIKit/UIViewController/canPerformUnwindSegueAction(_:from:sender:))

Called on a view controller to determine whether it responds to an unwind action.

[`-  unwindForSegue:towardsViewController:`](/documentation/UIKit/UIViewController/unwind(for:towards:))

Called when an unwind segue transitions to a new view controller.

### Presenting a view controller

[`-  showViewController:sender:`](/documentation/UIKit/UIViewController/show(_:sender:))

Presents a view controller in a primary context.

[`-  showDetailViewController:sender:`](/documentation/UIKit/UIViewController/showDetailViewController(_:sender:))

Presents a view controller in a secondary (or detail) context.

[`ShowDetailTargetDidChangeMessage`](/documentation/UIKit/UIViewController/ShowDetailTargetDidChangeMessage)

[`-  presentViewController:animated:completion:`](/documentation/UIKit/UIViewController/present(_:animated:completion:))

Presents a view controller modally.

[`-  dismissViewControllerAnimated:completion:`](/documentation/UIKit/UIViewController/dismiss(animated:completion:))

Dismisses the view controller that was presented modally by the view controller.

[`modalPresentationStyle`](/documentation/UIKit/UIViewController/modalPresentationStyle)

The presentation style for modal view controllers.

[`UIModalPresentationStyle`](/documentation/UIKit/UIModalPresentationStyle)

Modal presentation styles available when presenting view controllers.

[`modalTransitionStyle`](/documentation/UIKit/UIViewController/modalTransitionStyle)

The transition style to use when presenting the view controller.

[`UIModalTransitionStyle`](/documentation/UIKit/UIModalTransitionStyle)

Transition styles available when presenting view controllers.

[`modalInPresentation`](/documentation/UIKit/UIViewController/isModalInPresentation)

A Boolean value indicating whether the view controller enforces a modal behavior.

[`definesPresentationContext`](/documentation/UIKit/UIViewController/definesPresentationContext)

A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.

[`providesPresentationContextTransitionStyle`](/documentation/UIKit/UIViewController/providesPresentationContextTransitionStyle)

A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.

[`disablesAutomaticKeyboardDismissal`](/documentation/UIKit/UIViewController/disablesAutomaticKeyboardDismissal)

Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.

[`UIViewControllerShowDetailTargetDidChangeNotification`](/documentation/UIKit/UIViewController/showDetailTargetDidChangeNotification)

Posted when a split view controller is expanded or collapsed.

### Adding a custom transition or presentation

[`transitioningDelegate`](/documentation/UIKit/UIViewController/transitioningDelegate)

The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.

[`transitionCoordinator`](/documentation/UIKit/UIViewController/transitionCoordinator)

Returns the active transition coordinator object.

[`-  targetViewControllerForAction:sender:`](/documentation/UIKit/UIViewController/targetViewController(forAction:sender:))

Returns the view controller that responds to the action.

[`presentationController`](/documentation/UIKit/UIViewController/presentationController)

The presentation controller that’s managing the current view controller.

[`popoverPresentationController`](/documentation/UIKit/UIViewController/popoverPresentationController)

The nearest popover presentation controller that is managing the current view controller.

[`sheetPresentationController`](/documentation/UIKit/UIViewController/sheetPresentationController)

The sheet presentation controller for the view controller.

[`activePresentationController`](/documentation/UIKit/UIViewController/activePresentationController)

The presentation controller that’s managing the view controller.

[`restoresFocusAfterTransition`](/documentation/UIKit/UIViewController/restoresFocusAfterTransition)

A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.

[Customizing and resizing sheets in UIKit](/documentation/UIKit/customizing-and-resizing-sheets-in-uikit)

Discover how to create a layered and customized sheet experience in UIKit.

### Adapting to environment changes

[`-  collapseSecondaryViewController:forSplitViewController:`](/documentation/UIKit/UIViewController/collapseSecondaryViewController(_:for:))

Called when a split view controller transitions to a compact-width size class.

[`-  separateSecondaryViewControllerForSplitViewController:`](/documentation/UIKit/UIViewController/separateSecondaryViewController(for:))

Called when a split view controller transitions to a regular-width size class.

### Adjusting the interface style

[`overrideUserInterfaceStyle`](/documentation/UIKit/UIViewController/overrideUserInterfaceStyle)

The user interface style adopted by the view controller and all of its children.

[`preferredUserInterfaceStyle`](/documentation/UIKit/UIViewController/preferredUserInterfaceStyle)

The preferred interface style for this view controller.

[`childViewControllerForUserInterfaceStyle`](/documentation/UIKit/UIViewController/childViewControllerForUserInterfaceStyle)

The child view controller that supports the preferred user interface style.

[`-  setNeedsUserInterfaceAppearanceUpdate`](/documentation/UIKit/UIViewController/setNeedsUserInterfaceAppearanceUpdate())

Notifies the view controller that a change occurred that might affect the preferred interface style.

[`UIUserInterfaceStyle`](/documentation/UIKit/UIUserInterfaceStyle)

Constants that indicate the interface style for the app.

### Adjusting the container background style

[`preferredContainerBackgroundStyle`](/documentation/UIKit/UIViewController/preferredContainerBackgroundStyle)

[`childViewControllerForPreferredContainerBackgroundStyle`](/documentation/UIKit/UIViewController/childViewControllerForPreferredContainerBackgroundStyle)

[`-  setNeedsUpdateOfPreferredContainerBackgroundStyle`](/documentation/UIKit/UIViewController/setNeedsUpdateOfPreferredContainerBackgroundStyle())

[`UIContainerBackgroundStyle`](/documentation/UIKit/UIContainerBackgroundStyle)

### Observing trait changes

[`UITraitChangeObservable`](/documentation/UIKit/UITraitChangeObservable-67e94)

A type that calls your code in reaction to changes in the trait environment.

[`UITraitChangeObservable`](/documentation/UIKit/UITraitChangeObservable-7qoet)

A type that calls your code in reaction to changes in the trait environment.

### Overriding trait values

[`traitOverrides`](/documentation/UIKit/UIViewController/traitOverrides-1z1cc)

A mutable container of traits you use to set trait changes for this view controller and its views.

[`UITraitOverrides`](/documentation/UIKit/UITraitOverrides-swift.struct)

A mutable container of traits you use to set trait changes for an object and its descendants.

[`traitOverrides`](/documentation/UIKit/UIViewController/traitOverrides-8u19n)

A mutable container of traits you use to set trait changes for this view controller and its views.

[`UITraitOverrides`](/documentation/UIKit/UITraitOverrides-c.protocol)

A mutable container of traits you use to set trait changes for an object and its descendants.

[`-  updateTraitsIfNeeded`](/documentation/UIKit/UIViewController/updateTraitsIfNeeded())

Updates traits immediately for this view controller and its view, including any view controllers and views in this subtree.

### Managing child view controllers in a custom container

[`childViewControllers`](/documentation/UIKit/UIViewController/children)

An array of view controllers that are children of the current view controller.

[`-  addChildViewController:`](/documentation/UIKit/UIViewController/addChild(_:))

Adds the specified view controller as a child of the current view controller.

[`-  removeFromParentViewController`](/documentation/UIKit/UIViewController/removeFromParent())

Removes the view controller from its parent.

[`-  transitionFromViewController:toViewController:duration:options:animations:completion:`](/documentation/UIKit/UIViewController/transition(from:to:duration:options:animations:completion:))

Transitions between two of the view controller’s child view controllers.

[`shouldAutomaticallyForwardAppearanceMethods`](/documentation/UIKit/UIViewController/shouldAutomaticallyForwardAppearanceMethods)

Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.

[`-  beginAppearanceTransition:animated:`](/documentation/UIKit/UIViewController/beginAppearanceTransition(_:animated:))

Tells a child controller its appearance is about to change.

[`-  endAppearanceTransition`](/documentation/UIKit/UIViewController/endAppearanceTransition())

Tells a child controller its appearance has changed.

[`UIViewControllerHierarchyInconsistencyException`](/documentation/UIKit/UIViewController/hierarchyInconsistencyException)

Raised if the view controller hierarchy is inconsistent with the view hierarchy.

### Responding to containment events

[`-  willMoveToParentViewController:`](/documentation/UIKit/UIViewController/willMove(toParent:))

Called just before the view controller is added or removed from a container view controller.

[`-  didMoveToParentViewController:`](/documentation/UIKit/UIViewController/didMove(toParent:))

Called after the view controller is added or removed from a container view controller.

### Getting other related view controllers

[`presentingViewController`](/documentation/UIKit/UIViewController/presentingViewController)

The view controller that presented this view controller.

[`presentedViewController`](/documentation/UIKit/UIViewController/presentedViewController)

The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.

[`parentViewController`](/documentation/UIKit/UIViewController/parent)

The parent view controller of the recipient.

[`splitViewController`](/documentation/UIKit/UIViewController/splitViewController)

The nearest ancestor in the view controller hierarchy that is a split view controller.

[`navigationController`](/documentation/UIKit/UIViewController/navigationController)

The nearest ancestor in the view controller hierarchy that is a navigation controller.

[`tabBarController`](/documentation/UIKit/UIViewController/tabBarController)

The nearest ancestor in the view controller hierarchy that is a tab bar controller.

### Configuring a navigation interface

[`navigationItem`](/documentation/UIKit/UIViewController/navigationItem)

The navigation item used to represent the view controller in a parent’s navigation bar.

[`hidesBottomBarWhenPushed`](/documentation/UIKit/UIViewController/hidesBottomBarWhenPushed)

A Boolean value indicating whether the toolbar at the bottom of the screen is hidden when the view controller is pushed on to a navigation controller.

[`-  setToolbarItems:animated:`](/documentation/UIKit/UIViewController/setToolbarItems(_:animated:))

Sets the toolbar items to be displayed along with the view controller.

[`toolbarItems`](/documentation/UIKit/UIViewController/toolbarItems)

The toolbar items associated with the view controller.

### Configuring tab bar content

[`tab`](/documentation/UIKit/UIViewController/tab)

The `UITab` instance that was used to create the receiver, and represents the view controller. Default is nil.

[`tabBarItem`](/documentation/UIKit/UIViewController/tabBarItem)

The tab bar item that represents the view controller when added to a tab bar controller.

[`tabBarObservedScrollView`](/documentation/UIKit/UIViewController/tabBarObservedScrollView)

The full-screen scroll view to synchronize with a scrolling tab bar.

### Working with scrolling content

[`-  setContentScrollView:forEdge:`](/documentation/UIKit/UIViewController/setContentScrollView(_:for:))

Sets the scroll view that bars observe for the specified edge.

[`setContentScrollView(_:)`](/documentation/UIKit/UIViewController/setContentScrollView(_:))

Sets the scroll view that bars observe for all edges of the view.

[`-  contentScrollViewForEdge:`](/documentation/UIKit/UIViewController/contentScrollView(for:))

Returns the scroll view the view controller observes for the specified edge.

### Indicating missing content

[`contentUnavailableConfiguration`](/documentation/UIKit/UIViewController/contentUnavailableConfiguration-4b95e)

The current content-unavailable configuration of the view controller.

[`contentUnavailableConfigurationState`](/documentation/UIKit/UIViewController/contentUnavailableConfigurationState-7sczw)

The current configuration state of the content-unavailable view.

[`contentUnavailableConfiguration`](/documentation/UIKit/UIViewController/contentUnavailableConfiguration-6kqfk)

Setting a content unavailable configuration replaces the existing content unavailable view of the view controller with a new content unavailable view instance from the configuration,
or directly applies the configuration to the existing content unavailable view if the configuration is compatible with the existing content unavailable view type.
The default value is nil.

[`contentUnavailableConfigurationState`](/documentation/UIKit/UIViewController/contentUnavailableConfigurationState-9bvga)

Returns the current content unavailable configuration state for the view.
To add your own custom state(s), override the getter and call super to obtain an instance with the
system properties set, then set your own custom states as desired.

[`-  setNeedsUpdateContentUnavailableConfiguration`](/documentation/UIKit/UIViewController/setNeedsUpdateContentUnavailableConfiguration())

Requests that the system update the content-unavailable configuration for the latest state.

[`updateContentUnavailableConfiguration(using:)`](/documentation/UIKit/UIViewController/updateContentUnavailableConfiguration(using:))

Updates the content-unavailable configuration for the provided state.

[`UIContentUnavailableConfiguration`](/documentation/UIKit/UIContentUnavailableConfiguration-swift.struct)

A content configuration for a content-unavailable view.

[`-  updateContentUnavailableConfigurationUsingState:`](/documentation/UIKit/UIViewController/updateContentUnavailableConfigurationUsingState:)

Updates the content-unavailable configuration for the provided state.

[`UIContentUnavailableConfiguration`](/documentation/UIKit/UIContentUnavailableConfiguration-c.class)

A content configuration for a content-unavailable view.

### Supporting app extensions

[`extensionContext`](/documentation/UIKit/UIViewController/extensionContext)

Returns the extension context of the view controller.

### Coordinating with system gestures

[`preferredScreenEdgesDeferringSystemGestures`](/documentation/UIKit/UIViewController/preferredScreenEdgesDeferringSystemGestures)

The screen edges for which you want your gestures to take precedence over the system gestures.

[`childViewControllerForScreenEdgesDeferringSystemGestures`](/documentation/UIKit/UIViewController/childForScreenEdgesDeferringSystemGestures)

Returns the child view controller that should be queried to see if its gestures should take precedence.

[`-  setNeedsUpdateOfScreenEdgesDeferringSystemGestures`](/documentation/UIKit/UIViewController/setNeedsUpdateOfScreenEdgesDeferringSystemGestures())

Notifies the system of changes to the screen edges that defer system gestures.

[`prefersHomeIndicatorAutoHidden`](/documentation/UIKit/UIViewController/prefersHomeIndicatorAutoHidden)

A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.

[`childViewControllerForHomeIndicatorAutoHidden`](/documentation/UIKit/UIViewController/childForHomeIndicatorAutoHidden)

Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.

[`-  setNeedsUpdateOfHomeIndicatorAutoHidden`](/documentation/UIKit/UIViewController/setNeedsUpdateOfHomeIndicatorAutoHidden())

Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.

### Working with transitions

[`preferredTransition`](/documentation/UIKit/UIViewController/preferredTransition)

An object that defines the transition animation when switching to the view controller.

[`Transition`](/documentation/UIKit/UIViewController/Transition)

An object that defines the transition animation when switching to a new view controller.

### Working with focus

[`focusGroupIdentifier`](/documentation/UIKit/UIViewController/focusGroupIdentifier)

The identifier of the focus group that the view controller belongs to.

### Managing pointer lock state

[`prefersPointerLocked`](/documentation/UIKit/UIViewController/prefersPointerLocked)

A Boolean value that indicates whether the view controller prefers to lock the pointer to a specific scene.

[`-  setNeedsUpdateOfPrefersPointerLocked`](/documentation/UIKit/UIViewController/setNeedsUpdateOfPrefersPointerLocked())

Indicates that the view controller changed the pointer lock preference.

[`childViewControllerForPointerLock`](/documentation/UIKit/UIViewController/childViewControllerForPointerLock)

A child view controller to query for the pointer lock preference.

### Managing the status bar

[`prefersStatusBarHidden`](/documentation/UIKit/UIViewController/prefersStatusBarHidden)

Specifies whether the view controller prefers the status bar to be hidden or shown.

[`childViewControllerForStatusBarHidden`](/documentation/UIKit/UIViewController/childForStatusBarHidden)

The view controller to use for determining the hidden state of the status bar.

[`childViewControllerForStatusBarStyle`](/documentation/UIKit/UIViewController/childForStatusBarStyle)

Called when the system needs the view controller to use for determining status bar style.

[`preferredStatusBarStyle`](/documentation/UIKit/UIViewController/preferredStatusBarStyle)

The preferred status bar style for the view controller.

[`UIStatusBarStyle`](/documentation/UIKit/UIStatusBarStyle)

Constants that describe the style of the device’s status bar.

[`modalPresentationCapturesStatusBarAppearance`](/documentation/UIKit/UIViewController/modalPresentationCapturesStatusBarAppearance)

Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.

[`preferredStatusBarUpdateAnimation`](/documentation/UIKit/UIViewController/preferredStatusBarUpdateAnimation)

Specifies the animation style to use for hiding and showing the status bar for the view controller.

[`-  setNeedsStatusBarAppearanceUpdate`](/documentation/UIKit/UIViewController/setNeedsStatusBarAppearanceUpdate())

Indicates to the system that the view controller status bar attributes have changed.

### Managing the Touch Bar

[`childViewControllerForTouchBar`](/documentation/UIKit/UIViewController/childViewControllerForTouchBar)

The child view controller that the system uses to display content in the Touch Bar.

[`-  setNeedsTouchBarUpdate`](/documentation/UIKit/UIViewController/setNeedsTouchBarUpdate())

Tells the system to update the Touch Bar.

### Accessing the available key commands

[`performsActionsWhilePresentingModally`](/documentation/UIKit/UIViewController/performsActionsWhilePresentingModally)

A Boolean value indicating whether the view controller performs menu-related actions.

[`-  addKeyCommand:`](/documentation/UIKit/UIViewController/addKeyCommand(_:))

Associates the specified keyboard shortcut with the view controller.

[`-  removeKeyCommand:`](/documentation/UIKit/UIViewController/removeKeyCommand(_:))

Removes the key command from the view controller.

### Adding editing behaviors to your view controller

[`editing`](/documentation/UIKit/UIViewController/isEditing)

A Boolean value indicating whether the view controller currently allows the user to edit the view contents.

[`-  setEditing:animated:`](/documentation/UIKit/UIViewController/setEditing(_:animated:))

Sets whether the view controller shows an editable view.

[`editButtonItem`](/documentation/UIKit/UIViewController/editButtonItem)

Returns a bar button item that toggles its title and associated state between Edit and Done.

### Handling memory warnings

[`-  didReceiveMemoryWarning`](/documentation/UIKit/UIViewController/didReceiveMemoryWarning())

Sent to the view controller when the app receives a memory warning.

### Managing state restoration

[Restoring your app’s state](/documentation/UIKit/restoring-your-app-s-state)

Provide continuity for the user by preserving current activities.

[`restorationIdentifier`](/documentation/UIKit/UIViewController/restorationIdentifier)

The identifier that determines whether the view controller supports state restoration.

[`restorationClass`](/documentation/UIKit/UIViewController/restorationClass)

The class responsible for recreating this view controller when restoring the app’s state.

[`-  encodeRestorableStateWithCoder:`](/documentation/UIKit/UIViewController/encodeRestorableState(with:))

Encodes state-related information for the view controller.

[`-  decodeRestorableStateWithCoder:`](/documentation/UIKit/UIViewController/decodeRestorableState(with:))

Decodes and restores state-related information for the view controller.

[`-  applicationFinishedRestoringState`](/documentation/UIKit/UIViewController/applicationFinishedRestoringState())

Called on restored view controllers after other object decoding is complete.

### Logging user interaction intervals

[`interactionActivityTrackingBaseName`](/documentation/UIKit/UIViewController/interactionActivityTrackingBaseName)

The base name the view controller uses for logging signposts that annotate user interactions.

### Registering scene accessories

[`-  registerSceneAccessory:`](/documentation/UIKit/UIViewController/registerSceneAccessory(_:))

Registers a new scene accessory configuration associated with this view controller.

[`-  unregisterSceneAccessory:`](/documentation/UIKit/UIViewController/unregisterSceneAccessory(_:))

Unregisters a scene accessory with the specified registration.

### Deprecated

[Deprecated symbols](/documentation/UIKit/uiviewcontroller-deprecated-symbols)

Symbols that view controllers no longer support.

## Relationships

### Inherited By

[`UIReferenceLibraryViewController`](/documentation/UIKit/UIReferenceLibraryViewController)

[`UITableViewController`](/documentation/UIKit/UITableViewController)

[`UIDocumentViewController`](/documentation/UIKit/UIDocumentViewController)

[`UINavigationController`](/documentation/UIKit/UINavigationController)

[`UIFontPickerViewController`](/documentation/UIKit/UIFontPickerViewController)

[`UIAlertController`](/documentation/UIKit/UIAlertController)

[`UIInputViewController`](/documentation/UIKit/UIInputViewController)

[`UIPageViewController`](/documentation/UIKit/UIPageViewController)

[`UICloudSharingController`](/documentation/UIKit/UICloudSharingController)

[`UIDocumentPickerExtensionViewController`](/documentation/UIKit/UIDocumentPickerExtensionViewController)

[`UISplitViewController`](/documentation/UIKit/UISplitViewController)

[`UITabBarController`](/documentation/UIKit/UITabBarController)

[`UISearchContainerViewController`](/documentation/UIKit/UISearchContainerViewController)

[`UIActivityViewController`](/documentation/UIKit/UIActivityViewController)

[`UITextFormattingViewController`](/documentation/UIKit/UITextFormattingViewController)

[`UICollectionViewController`](/documentation/UIKit/UICollectionViewController)

[`UIDocumentPickerViewController`](/documentation/UIKit/UIDocumentPickerViewController)

[`UIColorPickerViewController`](/documentation/UIKit/UIColorPickerViewController)

[`UISearchController`](/documentation/UIKit/UISearchController)

[`UIDocumentMenuViewController`](/documentation/UIKit/UIDocumentMenuViewController)

[`UIDocumentBrowserViewController`](/documentation/UIKit/UIDocumentBrowserViewController)

### Conforms To

[`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)

[`CVarArg`](/documentation/Swift/CVarArg)

[`Sendable`](/documentation/Swift/Sendable)

[`Equatable`](/documentation/Swift/Equatable)

[`UIResponderStandardEditActions`](/documentation/UIKit/UIResponderStandardEditActions)

[`UITraitChangeObservable-67e94`](/documentation/UIKit/UITraitChangeObservable-67e94)

[`Copyable`](/documentation/Swift/Copyable)

[`UIAppearanceContainer`](/documentation/UIKit/UIAppearanceContainer)

[`Hashable`](/documentation/Swift/Hashable)

[`NSExtensionRequestHandling`](/documentation/Foundation/NSExtensionRequestHandling)

[`NSObjectProtocol`](/documentation/ObjectiveC/NSObjectProtocol)

[`UIActivityItemsConfigurationProviding`](/documentation/UIKit/UIActivityItemsConfigurationProviding)

[`Escapable`](/documentation/Swift/Escapable)

[`NSTouchBarProvider`](/documentation/AppKit/NSTouchBarProvider)

[`SendableMetatype`](/documentation/Swift/SendableMetatype)

[`UIContentContainer`](/documentation/UIKit/UIContentContainer)

[`UIPasteConfigurationSupporting`](/documentation/UIKit/UIPasteConfigurationSupporting)

[`UIFocusEnvironment`](/documentation/UIKit/UIFocusEnvironment)

[`UIStateRestoring`](/documentation/UIKit/UIStateRestoring)

[`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)

[`UIUserActivityRestoring`](/documentation/UIKit/UIUserActivityRestoring)

[`UITraitEnvironment`](/documentation/UIKit/UITraitEnvironment)

[`NSCoding`](/documentation/Foundation/NSCoding)

### Inherits From

[`UIResponder`](/documentation/UIKit/UIResponder)

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
