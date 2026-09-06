# Captions

Coordinate the presentation of closed-captioned data for your app’s media files.

## Discussion

People can create custom styles for caption appearance in Accessibility settings. The Media Accessibility framework provides access to these user-captioning settings.

In macOS, choose System Settings > Accessibility > Captions to access these options.

![Screenshot of the Accessibility settings in macOS with Captions selected.](images/com.apple.mediaaccessibility/media-3709928@2x.png)

When a person creates a custom caption style, the settings affect attributes, such as caption color, font, and language.

![Screenshot of the Captions settings for a custom style in macOS.](images/com.apple.mediaaccessibility/media-3709929@2x.png)

By choosing custom styles for media text, people are requesting improved legibility. The Media Accessibility functions let you to tailor the user experience of your media content. You must be able to influence the caption-rendering process at time of delivery for the following functions to be useful. Retrieving a person’s preferences and dynamically rendering the captions for maximum readability provides the best user experience.

## Topics

### General settings

[`kMACaptionAppearanceSettingsChangedNotification`](/documentation/MediaAccessibility/kMACaptionAppearanceSettingsChangedNotification)

A notification that occurs when any user-defined caption settings change.

[`MACaptionAppearanceDidDisplayCaptions`](/documentation/MediaAccessibility/MACaptionAppearanceDidDisplayCaptions(_:))

Informs accessibility clients when captions display onscreen.

[`MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics`](/documentation/MediaAccessibility/MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(_:))

Returns the preferences for captioning sounds.

[`MACaptionAppearanceGetDisplayType`](/documentation/MediaAccessibility/MACaptionAppearanceGetDisplayType(_:))

Returns the preferred type of captions to display.

[`MACaptionAppearanceSetDisplayType`](/documentation/MediaAccessibility/MACaptionAppearanceSetDisplayType(_:_:))

Sets the preference for the type of caption.

### Language settings

[`MACaptionAppearanceAddSelectedLanguage`](/documentation/MediaAccessibility/MACaptionAppearanceAddSelectedLanguage(_:_:))

Adds a preference for caption language to the stack of languages.

[`MACaptionAppearanceCopySelectedLanguages`](/documentation/MediaAccessibility/MACaptionAppearanceCopySelectedLanguages(_:))

Returns the preferred caption languages.

### Text settings

[`MACaptionAppearanceCopyFontDescriptorForStyle`](/documentation/MediaAccessibility/MACaptionAppearanceCopyFontDescriptorForStyle(_:_:_:))

Returns the preferred font for the specified style of type.

[`MACaptionAppearanceCopyForegroundColor`](/documentation/MediaAccessibility/MACaptionAppearanceCopyForegroundColor(_:_:))

Returns the preference for text color.

[`MACaptionAppearanceGetForegroundOpacity`](/documentation/MediaAccessibility/MACaptionAppearanceGetForegroundOpacity(_:_:))

Returns the preference for text opacity.

[`MACaptionAppearanceGetRelativeCharacterSize`](/documentation/MediaAccessibility/MACaptionAppearanceGetRelativeCharacterSize(_:_:))

Returns the preference for font scaling.

[`MACaptionAppearanceGetTextEdgeStyle`](/documentation/MediaAccessibility/MACaptionAppearanceGetTextEdgeStyle(_:_:))

Returns the preference for text edge style.

### Text highlight settings

[`MACaptionAppearanceCopyBackgroundColor`](/documentation/MediaAccessibility/MACaptionAppearanceCopyBackgroundColor(_:_:))

Returns the preference for the text highlight color.

[`MACaptionAppearanceGetBackgroundOpacity`](/documentation/MediaAccessibility/MACaptionAppearanceGetBackgroundOpacity(_:_:))

Returns the preference for the text highlight opacity.

### Caption window settings

[`MACaptionAppearanceCopyWindowColor`](/documentation/MediaAccessibility/MACaptionAppearanceCopyWindowColor(_:_:))

Returns the preference for the caption window’s color.

[`MACaptionAppearanceGetWindowOpacity`](/documentation/MediaAccessibility/MACaptionAppearanceGetWindowOpacity(_:_:))

Returns the preference for the overlay’s opacity.

[`MACaptionAppearanceGetWindowRoundedCornerRadius`](/documentation/MediaAccessibility/MACaptionAppearanceGetWindowRoundedCornerRadius(_:_:))

Returns the radius of the caption window’s corners.

### Image captioning settings

[`MAImageCaptioningCopyCaption`](/documentation/MediaAccessibility/MAImageCaptioningCopyCaption(_:_:))

Returns an accessibility caption from an image’s metadata.

[`MAImageCaptioningSetCaption`](/documentation/MediaAccessibility/MAImageCaptioningSetCaption(_:_:_:))

Sets the accessibility caption for an image’s metadata.

[`MAImageCaptioningCopyMetadataTagPath`](/documentation/MediaAccessibility/MAImageCaptioningCopyMetadataTagPath())

Returns the metadata tag path.

### Audible media selection settings

[`kMAAudibleMediaSettingsChangedNotification`](/documentation/MediaAccessibility/kMAAudibleMediaSettingsChangedNotification)

A notification that occurs when any user-defined audible media settings change.

[`MAAudibleMediaCopyPreferredCharacteristics`](/documentation/MediaAccessibility/MAAudibleMediaCopyPreferredCharacteristics())

Returns the preference for audible media characteristics.

[`MAMediaCharacteristicDescribesVideoForAccessibility`](/documentation/MediaAccessibility/MAMediaCharacteristicDescribesVideoForAccessibility)

A media characteristic that indicates that a track or media selection option includes audible content that describes a video for accessibility.

[`MAMediaCharacteristicDescribesMusicAndSoundForAccessibility`](/documentation/MediaAccessibility/MAMediaCharacteristicDescribesMusicAndSoundForAccessibility)

A media characteristic that indicates that a track includes legible content in the language of its specified locale that describes music and sound other than spoken dialog.

[`MAMediaCharacteristicTranscribesSpokenDialogForAccessibility`](/documentation/MediaAccessibility/MAMediaCharacteristicTranscribesSpokenDialogForAccessibility)

A media characteristic that indicates that a track includes legible content in the language of its specified locale that transcribes spoken dialog and identifies the speakers.

### Profile settings

[`MACaptionAppearanceCopyProfileIDs`](/documentation/MediaAccessibility/MACaptionAppearanceCopyProfileIDs())

[`MACaptionAppearanceSetActiveProfileID`](/documentation/MediaAccessibility/MACaptionAppearanceSetActiveProfileID(_:))

[`MACaptionAppearanceCopyActiveProfileID`](/documentation/MediaAccessibility/MACaptionAppearanceCopyActiveProfileID())

[`MACaptionAppearanceCopyProfileName`](/documentation/MediaAccessibility/MACaptionAppearanceCopyProfileName(_:))

[`MACaptionAppearanceExecuteBlockForProfileID`](/documentation/MediaAccessibility/MACaptionAppearanceExecuteBlockForProfileID(_:_:))

### Customization status

[`MACaptionAppearanceIsCustomized`](/documentation/MediaAccessibility/MACaptionAppearanceIsCustomized(_:))

### Constants

[`MACaptionAppearanceDomain`](/documentation/MediaAccessibility/MACaptionAppearanceDomain)

A value that specifies which domain to retrieve a preference setting from.

[`MACaptionAppearanceDisplayType`](/documentation/MediaAccessibility/MACaptionAppearanceDisplayType)

A value that specifies the type of captions to display.

[`MACaptionAppearanceBehavior`](/documentation/MediaAccessibility/MACaptionAppearanceBehavior)

A value that indicates the preferred behavior for a preference setting.

[`MACaptionAppearanceFontStyle`](/documentation/MediaAccessibility/MACaptionAppearanceFontStyle)

A value that specifies a font style.

[`MACaptionAppearanceTextEdgeStyle`](/documentation/MediaAccessibility/MACaptionAppearanceTextEdgeStyle)

A value that specifies a style for the outside of the text.

### Macros

[`MA_EXPORT`](/documentation/MediaAccessibility/MA_EXPORT)

[`MA_EXTERN`](/documentation/MediaAccessibility/MA_EXTERN)

[`MA_VISIBLE`](/documentation/MediaAccessibility/MA_VISIBLE)

[`MA_EXTERN_C_BEGIN`](/documentation/MediaAccessibility/MA_EXTERN_C_BEGIN)

[`MA_EXTERN_C_END`](/documentation/MediaAccessibility/MA_EXTERN_C_END)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
