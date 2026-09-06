# App Shortcuts

Improve the experience of using your app intents and entities in system experiences like Siri, Spotlight, and the Shortcuts app.

## Overview

App Shortcuts provide a polished experience for your app intents and entities in the
Shortcuts app and other system experiences. An App Shortcut combines the action from your
app intent with other data, such as a title, image, and spoken phrases that someone might
use to run the shortcut. A shortcut can also contain preconfigured parameters, so someone
can run the action quickly, and without having to specify additional information. For example,
a hiking app might offer an app intent to start a hike, but require you to select a trail
before starting the action. Without a shortcut, someone must provide the trail information
each time they run the intent. However, a shortcut can simplify this flow by offering to
start a hike on the person’s favorite trail.

You create App Shortcuts programmatically in your code, and the compiler generates the information
the rest of the system needs to use it. This approach means that the shortcuts you create
are available as soon as someone installs your app, and you don’t have to register them yourself.
Specify your shortcuts in your code by defining a custom type that adopts the [`AppShortcutsProvider`](/documentation/AppIntents/AppShortcutsProvider)
protocol. Include this type in your app, app extension, Swift package, or library that you
use to manage your intents-related code. Inside this type, construct one or more [`AppShortcut`](/documentation/AppIntents/AppShortcut)
types using static data. Define your shortcuts in the same place you define the app intents
that those shortcuts use.

> Note: Apple may extract anonymized App Shortcuts data such as localized phrases, display
> representation values, and the title and description of related intents. Machine learning
> models use this data when training to help improve the App Shortcuts experience.

Although the Shortcuts app and other system features find your shortcuts automatically, you can
also make them available from your app using tip views. The [`SiriTipView`](/documentation/AppIntents/SiriTipView) and [`SiriTipUIView`](/documentation/AppIntents/SiriTipUIView)
types display the relevant shortcuts for the app intent you specify. You can also use a
[`ShortcutsLink`](/documentation/AppIntents/ShortcutsLink) or [`ShortcutsUIButton`](/documentation/AppIntents/ShortcutsUIButton) to open your app’s page in the Shortcuts app.

## Topics

### App Shortcut management

[`AppShortcutsProvider`](/documentation/AppIntents/AppShortcutsProvider)

A type alias for the type that provides an app’s preconfigured shortcuts.

### App Shortcut definition

[`AppShortcut`](/documentation/AppIntents/AppShortcut)

A type that defines a preconfigured shortcut for a specific app intent.

[`AppShortcutPhrase`](/documentation/AppIntents/AppShortcutPhrase)

A spoken phrase that causes the system to run the corresponding App Shortcut.

[`AppShortcutPhraseToken`](/documentation/AppIntents/AppShortcutPhraseToken)

Dynamic values you can include in the spoken phrases that run your shortcut.

[`NegativeAppShortcutPhrase`](/documentation/AppIntents/NegativeAppShortcutPhrase)

An object that represents a negative phrase.

[`NegativeAppShortcutPhrases`](/documentation/AppIntents/NegativeAppShortcutPhrases)

This is a set of negative phrases, which will all be added to the app-level negative
training set. All the training data specified here, will be used to completely bypass your app

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/CFBundleIcons/CFBundlePrimaryIcon/NSAppIconActionTintColorName>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/CFBundleIcons/CFBundlePrimaryIcon/NSAppIconComplementingColorNames>

[`AppShortcutsBuilder`](/documentation/AppIntents/AppShortcutsBuilder)

A result builder that allows you to declaratively describe the App Shortcuts that your app provides.

[`ShortcutTileColor`](/documentation/AppIntents/ShortcutTileColor)

Describes the colors a shortcut tile in the Shortcuts app.

[`AppShortcutsContent`](/documentation/AppIntents/AppShortcutsContent)

### App Shortcut options

[`AppShortcutOptionsCollection`](/documentation/AppIntents/AppShortcutOptionsCollection)

Represents a collection of options for parameters of an App Shortcut.

[`AppShortcutOptionsCollectionProtocol`](/documentation/AppIntents/AppShortcutOptionsCollectionProtocol)

[`AppShortcutOptionsCollectionSpecification`](/documentation/AppIntents/AppShortcutOptionsCollectionSpecification)

[`AppShortcutOptionsCollectionSpecificationBuilder`](/documentation/AppIntents/AppShortcutOptionsCollectionSpecificationBuilder)

### App Shortcut parameter presentation

[`AppShortcutParameterPresentation`](/documentation/AppIntents/AppShortcutParameterPresentation)

Describes the presentation of an App Shortcut  for the provided parameter.

[`AppShortcutParameterPresentationSummary`](/documentation/AppIntents/AppShortcutParameterPresentationSummary)

The summary of the presentation of an App Shortcut parameter.

[`AppShortcutParameterPresentationSummaryString`](/documentation/AppIntents/AppShortcutParameterPresentationSummaryString)

[`AppShortcutParameterPresentationTitle`](/documentation/AppIntents/AppShortcutParameterPresentationTitle)

A struct that represents the title of the presentation of an App Shortcut.

[`AppShortcutParameterPresentationTitleString`](/documentation/AppIntents/AppShortcutParameterPresentationTitleString)

### Buttons

[`ShortcutsUIButton`](/documentation/AppIntents/ShortcutsUIButton)

A button that opens the current app’s page in the Shortcuts app.

[`ShortcutsLink`](/documentation/AppIntents/ShortcutsLink)

A button that brings users to the current app’s App Shortcuts page in the Shortcuts app.

[`ShortcutsLinkStyle`](/documentation/AppIntents/ShortcutsLinkStyle)

The styles to apply to buttons you use to open your app’s page in the Shortcuts app.

### Tip views

[`SiriTipUIView`](/documentation/AppIntents/SiriTipUIView)

A view that displays the phrase a person uses to invoke an App Shortcut.

[`SiriTipView`](/documentation/AppIntents/SiriTipView)

A SwiftUI view that displays the phrase someone uses to invoke an App Shortcut.

[`SiriTipViewStyle`](/documentation/AppIntents/SiriTipViewStyle)

The styles to apply to the tip views you use to display spoken phrases.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
