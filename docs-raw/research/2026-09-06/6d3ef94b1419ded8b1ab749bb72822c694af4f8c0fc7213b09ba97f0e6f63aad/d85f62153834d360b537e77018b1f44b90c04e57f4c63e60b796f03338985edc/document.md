# Coordinating multiple gesture recognizers

Discover how to use multiple gesture recognizers on the same view.

## Discussion

Gesture recognizers track incoming touch events separately, but UIKit normally allows the recognition of only one gesture at a time on a single view. Recognizing only one gesture at a time is usually preferable because it prevents user input from triggering more than one action at a time. However, this default behavior can introduce unintended side effects. For example, in a view that contains both pan and swipe gesture recognizers, swipes are never recognized. Because the pan gesture recognizer is continuous, it always recognizes its gesture before the swipe gesture recognizer, which is discrete.

To prevent the unintended side effects of the default recognition behavior, you can tell UIKit to recognize gestures in a specific order using a delegate object. UIKit uses the methods of your delegate object to determine whether a gesture recognizer must come before or after other gesture recognizers. For example, your delegate can tell UIKit that a swipe gesture recognizer must fail before a pan gesture recognizer is allowed to act. Your delegate can also tell UIKit that two gestures can be recognized simultaneously.

## Topics

### Simultaneous gestures

[Preferring one gesture over another](/documentation/UIKit/preferring-one-gesture-over-another)

Use a gesture recognizer delegate object to determine the order in which gestures are recognized in your views.

[Allowing the simultaneous recognition of multiple gestures](/documentation/UIKit/allowing-the-simultaneous-recognition-of-multiple-gestures)

Learn how to use a delegate object to allow detection of more than one gesture at a time.

[Attaching gesture recognizers to UIKit controls](/documentation/UIKit/attaching-gesture-recognizers-to-uikit-controls)

Learn how gesture recognizers interact with UIKit controls such as buttons, switches, and sliders.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
