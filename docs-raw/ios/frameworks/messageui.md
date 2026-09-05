* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/messageui#app-main)

Framework

# Message UI

Create a user interface for composing email and text messages, so users can edit and send messages without leaving your app.

iOS 3.0+iPadOS 3.0+Mac Catalyst 13.0+visionOS 1.0+

## [Overview](https://developer.apple.com/documentation/messageui\#overview)

The Message UI framework provides specialized view controllers for presenting standard composition interfaces for email and SMS (Short Messaging Service) text messages. Use these interfaces to add message delivery capabilities, without requiring the user to leave your app.

To display a composition interface, present the corresponding view controller modally from your app. Once presented, the user has the option to customize the contents before sending or canceling the message. Your custom delegate object then handles the dismissal of the view controller based on the user’s action. For information on how to present and dismiss view controllers, see [View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457).

## [Topics](https://developer.apple.com/documentation/messageui\#topics)

### [Email composition interface](https://developer.apple.com/documentation/messageui\#Email-composition-interface)

[`class MFMailComposeViewController`](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller)

A standard view controller, whose interface lets the user manage, edit, and send email messages.

### [Message composition interface](https://developer.apple.com/documentation/messageui\#Message-composition-interface)

[`class MFMessageComposeViewController`](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller)

A standard view controller whose interface lets the user compose and send SMS or MMS messages.

### [Classes](https://developer.apple.com/documentation/messageui\#Classes)

[`class MFComposeAssistantViewController`](https://developer.apple.com/documentation/messageui/mfcomposeassistantviewcontroller)

[`class MFMailDraft`](https://developer.apple.com/documentation/messageui/mfmaildraft)

[`class WritingAssistant`](https://developer.apple.com/documentation/messageui/writingassistant)

### [Protocols](https://developer.apple.com/documentation/messageui\#Protocols)

[`protocol MFComposeAssistantViewControllerDelegate`](https://developer.apple.com/documentation/messageui/mfcomposeassistantviewcontrollerdelegate)

### [Enumerations](https://developer.apple.com/documentation/messageui\#Enumerations)

[`enum MFMailComposeControllerDeferredAction`](https://developer.apple.com/documentation/messageui/mfmailcomposecontrollerdeferredaction)

Current page is Message UI