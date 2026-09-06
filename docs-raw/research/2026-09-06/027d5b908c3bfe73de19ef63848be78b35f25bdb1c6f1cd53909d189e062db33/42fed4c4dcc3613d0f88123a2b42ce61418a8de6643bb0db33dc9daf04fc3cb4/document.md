# Intents

Empower people to customize interactions for your app on their device.

## Overview> Note: SiriKit, Intents, and IntentsUI frameworks continue to provide legacy support for Shortcuts actions, widget configuration, and most existing Siri interactions. To implement modern support for these features and integrate your app with Apple Intelligence and Siri AI, use the <doc://com.apple.documentation/documentation/AppIntents> framework.

Intents is a [SiriKit](/documentation/SiriKit) framework you use to support interactions with Siri, Shortcuts, and widgets. Define custom intents for specific actions that someone can trigger with Siri or Shortcuts, and donate intents to help Siri learn someone’s habits and suggest relevant shortcuts over time. You can also provide shortcut suggestions that appear in the Shortcuts app or in Siri’s recommendations to help boost discoverability.

## Topics

### Intents

  <doc://com.apple.sirikit/documentation/SiriKit/dispatching-intents-to-handlers>

  <doc://com.apple.sirikit/documentation/SiriKit/resolving-and-handling-intents>

[`INIntent`](/documentation/Intents/INIntent)

A request to fulfill in your app or Intents extension.

[`INIntentResponse`](/documentation/Intents/INIntentResponse)

Your response to an intent object.

  <doc://com.apple.sirikit/documentation/SiriKit/intent-handling-infrastructure>

  <doc://com.apple.sirikit/documentation/SiriKit/providing-hands-free-app-control-with-intents>

  <doc://com.apple.sirikit/documentation/SiriKit/resolution-results>

  <doc://com.apple.sirikit/documentation/SiriKit/common-data-types>

### Standard Intents

SiriKit groups intents into domains based on the type of app that’s likely to support them.

  <doc://com.apple.sirikit/documentation/SiriKit/car-commands>

  <doc://com.apple.sirikit/documentation/SiriKit/lists-and-notes>

  <doc://com.apple.sirikit/documentation/SiriKit/media>

  <doc://com.apple.sirikit/documentation/SiriKit/messaging>

  <doc://com.apple.sirikit/documentation/SiriKit/payments>

  <doc://com.apple.sirikit/documentation/SiriKit/restaurant-reservations>

  <doc://com.apple.sirikit/documentation/SiriKit/ride-booking>

  <doc://com.apple.sirikit/documentation/SiriKit/voip-calling>

  <doc://com.apple.sirikit/documentation/SiriKit/workouts>

  <doc://com.apple.sirikit/documentation/SiriKit/intent-class-identifiers>

### Shortcuts and Donations

  <doc://com.apple.sirikit/documentation/SiriKit/offering-actions-in-the-shortcuts-app>

  <doc://com.apple.sirikit/documentation/SiriKit/adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app>

  <doc://com.apple.sirikit/documentation/SiriKit/donating-shortcuts>

  <doc://com.apple.sirikit/documentation/SiriKit/deleting-donated-shortcuts>

  <doc://com.apple.sirikit/documentation/SiriKit/soup-chef-accelerating-app-interactions-with-shortcuts>

  <doc://com.apple.sirikit/documentation/SiriKit/soup-chef-with-app-intents-migrating-custom-intents>

  <doc://com.apple.sirikit/documentation/SiriKit/adding-shortcuts-for-wind-down>

[`INShortcutReference`](/documentation/Intents/INShortcutReference)

An object representing an action available in your app that the system may suggest to a user or a user may add to Siri.

[`INInteraction`](/documentation/Intents/INInteraction)

An interaction between the user and your app involving an intent object.

[`INShortcut`](/documentation/Intents/INShortcut-swift.enum)

An action available in your app that the system may suggest to a user or a user may add to Siri.

[`INVoiceShortcutCenter`](/documentation/Intents/INVoiceShortcutCenter)

Retrieve the user’s shortcuts and make shortcut suggestions.

[`INVoiceShortcut`](/documentation/Intents/INVoiceShortcut)

A shortcut the user added to Siri.

[`INShortcutAvailabilityOptions`](/documentation/Intents/INShortcutAvailabilityOptions)

Defined contexts in which an intent or activity might be relevant to a user.

[`INShortcutReference`](/documentation/Intents/INShortcutReference)

An object representing an action available in your app that the system may suggest to a user or a user may add to Siri.

[`INIntentDonationMetadata`](/documentation/Intents/INIntentDonationMetadata)

  <doc://com.apple.sirikit/documentation/SiriKit/watch-and-widget-support>

  <doc://com.apple.sirikit/documentation/SiriKit/siri-event-suggestions>

### Vocabulary

  <doc://com.apple.sirikit/documentation/SiriKit/registering-custom-vocabulary-with-sirikit>

[`INVocabulary`](/documentation/Intents/INVocabulary)

An object for registering user-specific vocabulary that Siri requests might include.

### Deprecated Symbols

  <doc://com.apple.sirikit/documentation/SiriKit/deprecated-symbols>

### Macros

  <doc://com.apple.sirikit/documentation/SiriKit/macros>



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
