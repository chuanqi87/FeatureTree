# Accessibility API

Browse API in the Accessibility framework.

## Overview

While many Apple frameworks provide built-in accessibility support,
the Accessibility framework defines API for supporting additional accessibility features across multiple platforms.
The Accessibility framework includes API that enable you to:

- Respond to changes in Accessibility system settings
- Post accessibility notifications
- Define an accessible representation of your chart to support audio graphs
- Interact with hardware such as braille displays and hearing devices
- Generate a localized description of a color

## Topics

### System settings

[`AccessibilitySettings`](/documentation/Accessibility/AccessibilitySettings)

A structure for working with accessibility system settings.

[`AXOpenSettingsFeature`](/documentation/Accessibility/AXOpenSettingsFeature)

[`AXAnimatedImagesEnabled`](/documentation/Accessibility/AXAnimatedImagesEnabled)

[`AXAnimatedImagesEnabledDidChangeNotification`](/documentation/Accessibility/AXAnimatedImagesEnabledDidChangeNotification)

[`AXPrefersHorizontalTextLayout`](/documentation/Accessibility/AXPrefersHorizontalTextLayout)

[`AXPrefersHorizontalTextLayoutDidChangeNotification`](/documentation/Accessibility/AXPrefersHorizontalTextLayoutDidChangeNotification)

[`AXPrefersHeadAnchorAlternative`](/documentation/Accessibility/AXPrefersHeadAnchorAlternative)

[`AXPrefersHeadAnchorAlternativeDidChangeNotification`](/documentation/Accessibility/AXPrefersHeadAnchorAlternativeDidChangeNotification)

[`AXPrefersNonBlinkingTextInsertionIndicator`](/documentation/Accessibility/AXPrefersNonBlinkingTextInsertionIndicator)

### Notifications

[`AccessibilityNotification`](/documentation/Accessibility/AccessibilityNotification)

Types of accessibility notifications that an app can post.

### Assistive technologies

[`AccessibilityTechnology`](/documentation/Accessibility/AccessibilityTechnology)

[`AXTechnologyAutomation`](/documentation/Accessibility/AccessibilityTechnology/automation)

[`AXTechnologyFullKeyboardAccess`](/documentation/Accessibility/AccessibilityTechnology/fullKeyboardAccess)

[`AXTechnologyHoverText`](/documentation/Accessibility/AccessibilityTechnology/hoverText)

[`AXTechnologySpeakScreen`](/documentation/Accessibility/AccessibilityTechnology/speakScreen)

[`AXTechnologySwitchControl`](/documentation/Accessibility/AccessibilityTechnology/switchControl)

[`AXTechnologyVoiceControl`](/documentation/Accessibility/AccessibilityTechnology/voiceControl)

[`AXTechnologyVoiceOver`](/documentation/Accessibility/AccessibilityTechnology/voiceOver)

[`AXTechnologyZoom`](/documentation/Accessibility/AccessibilityTechnology/zoom)

[`AccessibilityRequest`](/documentation/Accessibility/AccessibilityRequest)

### Features

[Customized accessibility content](/documentation/Accessibility/customized-accessibility-content)

Customize your apps to deliver accessibility information to your users in measured
portions as they need it.

[Audio graphs](/documentation/Accessibility/audio-graphs)

Define an accessible representation of your chart for VoiceOver to generate an audio
graph.

[Hearing device support](/documentation/Accessibility/hearing-device-support)

Access information about paired hearing aid devices and streaming status.

[`AXNameFromColor`](/documentation/Accessibility/AXNameFromColor(_:))

Returns a localized description of the color to use in accessibility attributes.

### Braille

[Braille displays](/documentation/Accessibility/braille-displays)

Display a graphical representation of images, icons, data, and more on a two-dimensional
braille display.

[`AXBrailleTable`](/documentation/Accessibility/AXBrailleTable)

A rule for translating print text to Braille, and back-translating Braille to print text.

[`AXBrailleTranslator`](/documentation/Accessibility/AXBrailleTranslator)

Translates print text to Braille and Braille to print text according to the given Braille table.

[`AXBrailleTranslationResult`](/documentation/Accessibility/AXBrailleTranslationResult)

The result of translation or back-translation.

### Math expressions

[`AXMathExpressionNumber`](/documentation/Accessibility/AXMathExpressionNumber)

[`AXMathExpressionIdentifier`](/documentation/Accessibility/AXMathExpressionIdentifier)

[`AXMathExpressionOperator`](/documentation/Accessibility/AXMathExpressionOperator)

[`AXMathExpressionText`](/documentation/Accessibility/AXMathExpressionText)

[`AXMathExpressionFenced`](/documentation/Accessibility/AXMathExpressionFenced)

[`AXMathExpressionRow`](/documentation/Accessibility/AXMathExpressionRow)

[`AXMathExpressionTable`](/documentation/Accessibility/AXMathExpressionTable)

[`AXMathExpressionTableCell`](/documentation/Accessibility/AXMathExpressionTableCell)

[`AXMathExpressionTableRow`](/documentation/Accessibility/AXMathExpressionTableRow)

[`AXMathExpressionUnderOver`](/documentation/Accessibility/AXMathExpressionUnderOver)

[`AXMathExpressionSubSuperscript`](/documentation/Accessibility/AXMathExpressionSubSuperscript)

[`AXMathExpressionFraction`](/documentation/Accessibility/AXMathExpressionFraction)

[`AXMathExpressionMultiscript`](/documentation/Accessibility/AXMathExpressionMultiscript)

[`AXMathExpressionRoot`](/documentation/Accessibility/AXMathExpressionRoot)

[`AXMathExpression`](/documentation/Accessibility/AXMathExpression)

[`AXMathExpressionProvider`](/documentation/Accessibility/AXMathExpressionProvider)

### Override sessions

[`AXFeatureOverrideSession`](/documentation/Accessibility/AXFeatureOverrideSession)

A token object that represents an override session held by your app.

[`AXFeatureOverrideSessionManager`](/documentation/Accessibility/AXFeatureOverrideSessionManager)

A manager class to begin and end accessibility feature override sessions. Multiple override sessions are reconciled by combining the requests, preferring feature enablement. Ending all sessions restores the prior state of Accessibility feature enablement. Your app must be entitled with com.apple.developer.accessibility.merchant-api-control.

[`Options`](/documentation/Accessibility/AXFeatureOverrideSession/Options)

Options indicating which Accessibility features will be turned on or off when an override session is held by your app.

[`AXFeatureOverrideSessionErrorDomain`](/documentation/Accessibility/AXFeatureOverrideSessionErrorDomain)

[`AXFeatureOverrideSessionError`](/documentation/Accessibility/AXFeatureOverrideSessionError-swift.struct)

[`Code`](/documentation/Accessibility/AXFeatureOverrideSessionError-swift.struct/Code)

  <doc://com.apple.documentation/documentation/BundleResources/Entitlements/com.apple.developer.accessibility.merchant-api-control>

### Deprecated

[`AXAnimatedImagesEnabled()`](/documentation/Accessibility/AXAnimatedImagesEnabled())

Returns a Boolean value that indicates whether the system setting for Animated Images
is on.

[`AXPrefersHeadAnchorAlternative()`](/documentation/Accessibility/AXPrefersHeadAnchorAlternative())

Returns a Boolean value that indicates the person’s preference for content that follows
their head position.

[`AXPrefersHorizontalTextLayout()`](/documentation/Accessibility/AXPrefersHorizontalTextLayout())

Returns a Boolean value that indicates whether the system setting for Prefer Horizontal
Text is on.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
