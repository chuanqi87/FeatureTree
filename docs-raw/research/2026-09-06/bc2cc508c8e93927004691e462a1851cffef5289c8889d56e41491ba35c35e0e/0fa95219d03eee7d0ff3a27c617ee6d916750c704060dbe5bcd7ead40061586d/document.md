# Handling pan gestures

Trace the movement of fingers around the screen, and apply that movement to your content.

## Discussion

A pan gesture occurs any time a person moves one or more fingers around the screen. A screen-edge pan gesture is a specialized pan gesture that originates from the edge of the screen. Use the [`UIPanGestureRecognizer`](/documentation/UIKit/UIPanGestureRecognizer) class for pan gestures and the [`UIScreenEdgePanGestureRecognizer`](/documentation/UIKit/UIScreenEdgePanGestureRecognizer) class for screen-edge pan gestures.

You can attach a gesture recognizer in one of these ways:

- Programmatically. Call the [`addGestureRecognizer(_:)`](/documentation/UIKit/UIView/addGestureRecognizer(_:)) method of your view.
- In Interface Builder. Drag the appropriate object from the library and drop it onto your view.

![A diagram demonstrating a single-finger pan gesture.](images/com.apple.uikit/handling-pan-gestures-1@2x.png)

Use pan gesture recognizers for tasks that require you to track the movement of the person’s fingers onscreen. You might use a pan gesture recognizer to drag objects around in your interface or update their appearance based on the position of the person’s finger. Pan gestures are continuous, so your action method is called whenever the touch information changes, giving you a chance to update your content.

A pan gesture recognizer enters the [`UIGestureRecognizer.State.began`](/documentation/UIKit/UIGestureRecognizer/State-swift.enum/began) state as soon as the required amount of initial movement is achieved. After that initial change, subsequent changes cause the gesture recognizer to enter the [`UIGestureRecognizer.State.changed`](/documentation/UIKit/UIGestureRecognizer/State-swift.enum/changed) state. When the person’s fingers lift from the screen, the gesture recognizer enters the [`UIGestureRecognizer.State.ended`](/documentation/UIKit/UIGestureRecognizer/State-swift.enum/ended) state.

To simplify tracking, use the pan gesture recognizer’s [`translation(in:)`](/documentation/UIKit/UIPanGestureRecognizer/translation(in:)) method to get the distance that the person’s finger has moved from the original touch location. At the beginning of the gesture, a pan gesture recognizer stores the initial point of contact for the person’s fingers. (If the gesture involves multiple fingers, the gesture recognizer uses the center point of the set of touches.) Each time the fingers move, the [`translation(in:)`](/documentation/UIKit/UIPanGestureRecognizer/translation(in:)) method reports the distance from the original location.

The following code shows an action method used to drag a view around the screen. When the gesture begins, this method saves the initial position of the view. It then updates the position of the view based on the movement of a person’s fingers.

```swift
var initialCenter = CGPoint()  // The initial center point of the view.
@IBAction func panPiece(_ gestureRecognizer: UIPanGestureRecognizer) {   
   guard gestureRecognizer.view != nil else { return }
   let piece = gestureRecognizer.view!
   // Get the changes in the X and Y directions relative to
   // the superview's coordinate space.
   let translation = gestureRecognizer.translation(in: piece.superview)
   if gestureRecognizer.state == .began {
      // Save the view's original position. 
      self.initialCenter = piece.center
   }
      // Update the position for the .began, .changed, and .ended states
   if gestureRecognizer.state != .cancelled {
      // Add the X and Y translation to the view's original position.
      let newCenter = CGPoint(x: initialCenter.x + translation.x, y: initialCenter.y + translation.y)
      piece.center = newCenter
   }
   else {
      // On cancellation, return the piece to its original location.
      piece.center = initialCenter
   }
}
```

If the code for your pan gesture recognizer isn’t called, check to see if the following conditions are true, and make corrections as needed:

- The [`isUserInteractionEnabled`](/documentation/UIKit/UIView/isUserInteractionEnabled) property of the view is set to <doc://com.apple.documentation/documentation/Swift/true>. Image views and labels set this property to <doc://com.apple.documentation/documentation/Swift/false> by default.
- The number of touches is between the values specified in the [`minimumNumberOfTouches`](/documentation/UIKit/UIPanGestureRecognizer/minimumNumberOfTouches) and [`maximumNumberOfTouches`](/documentation/UIKit/UIPanGestureRecognizer/maximumNumberOfTouches) properties.
- For a [`UIScreenEdgePanGestureRecognizer`](/documentation/UIKit/UIScreenEdgePanGestureRecognizer) object, the [`edges`](/documentation/UIKit/UIScreenEdgePanGestureRecognizer/edges) property is configured and touches start at the appropriate edge.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
