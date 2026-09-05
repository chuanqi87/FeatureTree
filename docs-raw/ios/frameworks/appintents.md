* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/appintents#app-main)

Framework

# App Intents

Make content and actions discoverable by Apple Intelligence and support system experiences like Siri, Spotlight, Shortcuts, and widgets.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

## [Overview](https://developer.apple.com/documentation/appintents\#Overview)

Make your app’s actions and data available outside your app using the App Intents framework. Every app has code to perform specific actions, such as playing music or displaying photos. Apps also have data, such as songs or photos, that people might want to use outside your app.

![A hero image of an App Intents framework icon.](https://developer.apple.com/tutorials/images/com.apple.AppIntents/app-intents-hero@2x.png)

With App Intents, you express your app’s actions and data in a structured way that makes them discoverable by Apple Intelligence and provides deeper integration with system features people use frequently. For example:

- People can interact with your app’s content through Siri.

- Spotlight helps people navigate to your data directly from search results.

- The Shortcuts app helps people configure workflows that include your app’s actions.

- People can configure Apple Pencil or the Action button on iPhone to perform your app’s actions when pressed.

- [Widgets](https://developer.apple.com/documentation/widgetkit), [controls](https://developer.apple.com/documentation/widgetkit/controls-collection), and [Live Activities](https://developer.apple.com/documentation/activitykit) can use your app’s actions to perform relevant tasks.

- You can define custom Focus modes, and respond to Focus changes.


Use this framework to declare the actions your app performs as one or more _app intents_. You can also create _app entities_ and _app enums_ to make your app’s key data types available to the system. For example, a music app might define entities for the songs and albums it manages, and define an app intent to play them. During compilation, the compiler generates information that Apple Intelligence, Siri, and other system features need to discover and use your intents, entities, and app enum types.

For design guidance on how to implement features that involve [Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets), [Controls](https://developer.apple.com/design/human-interface-guidelines/controls), [App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts), [Siri](https://developer.apple.com/design/human-interface-guidelines/siri), or the [Action button](https://developer.apple.com/design/human-interface-guidelines/action-button), see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines).

## [Topics](https://developer.apple.com/documentation/appintents\#topics)

### [Essentials](https://developer.apple.com/documentation/appintents\#Essentials)

Learn the fundamentals of the App Intents framework.

[Getting started with the App Intents framework](https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework)

Make your app’s actions and content available to the rest of the system using the App Intents framework.

[App Intents updates](https://developer.apple.com/documentation/updates/appintents)

Learn about important changes in App Intents.

### [App-specific content](https://developer.apple.com/documentation/appintents\#App-specific-content)

Define the actions, data, and types that represent your app’s capabilities to the system.

[API Reference\\
App intents](https://developer.apple.com/documentation/appintents/app-intents)

Make your app’s custom actions available to the system by using app intent types.

[API Reference\\
App entities](https://developer.apple.com/documentation/appintents/app-entities)

Make your app’s core types and data concepts available to the system using app entity types.

[API Reference\\
App enums](https://developer.apple.com/documentation/appintents/app-enums)

Make your app’s enumerations and predefined values available to the system by using app enum types.

[API Reference\\
Common data types](https://developer.apple.com/documentation/appintents/common-data-types)

Use framework-defined types for common parameter and result data types such as contacts, files, currencies, and more.

[API Reference\\
App extension](https://developer.apple.com/documentation/appintents/app-extension)

Deliver app intents in an app extension or other package that lives outside your app’s code.

### [System integration](https://developer.apple.com/documentation/appintents\#System-integration)

Adopt schemas for well-known actions, display visual results, and donate behavioral signals to Apple Intelligence.

[API Reference\\
App schema domains](https://developer.apple.com/documentation/appintents/app-schema-domains)

Declare support for well-known actions and content by applying system-defined schemas to your app intents, app entities, and app enumerations.

[API Reference\\
Visual presentation](https://developer.apple.com/documentation/appintents/visual-presentation)

Display app intents and app entities visually using snippets, and associate intents and entities with your app’s scenes and views.

[API Reference\\
Donations and discovery](https://developer.apple.com/documentation/appintents/donations-and-discovery)

Donate your app’s intents and entities to the system to help it identify trends and predict future behaviors.

### [Feature integration](https://developer.apple.com/documentation/appintents\#Feature-integration)

Make your app intents and entities available to Siri, Spotlight, Shortcuts, widgets, and other system features.

[Adopting App Intents to support system experiences](https://developer.apple.com/documentation/appintents/adopting-app-intents-to-support-system-experiences)

Create app intents and entities so people can use your app’s content and actions across system experiences.

[API Reference\\
Apple Intelligence and Siri AI](https://developer.apple.com/documentation/appintents/apple-intelligence-and-siri-ai)

Integrate your app with Apple Intelligence and bring it to Siri AI.

[API Reference\\
Spotlight integration](https://developer.apple.com/documentation/appintents/spotlight)

Add your entities to your app’s Spotlight index, and automate the indexing of your content.

[API Reference\\
App Shortcuts](https://developer.apple.com/documentation/appintents/app-shortcuts)

Improve the experience of using your app intents and entities in system experiences like Siri, Spotlight, and the Shortcuts app.

[API Reference\\
Widgets, Live Activities, and Controls](https://developer.apple.com/documentation/appintents/widgets-live-activities-and-controls)

Implement interactive widgets, controls, watch complications, and Live Activities using app intents.

[API Reference\\
Hardware interactions](https://developer.apple.com/documentation/appintents/hardware-interactions)

Run your App Shortcuts from the Action button on iPhone or Apple Watch, or launch your own conversational app from the side button on iPhone.

[API Reference\\
Focus](https://developer.apple.com/documentation/appintents/focus)

Adjust your app’s behavior and filter incoming notifications when the current Focus changes.

[API Reference\\
Visual intelligence](https://developer.apple.com/documentation/appintents/visual-intelligence)

Match images to your app’s content and report the results to the Visual Intelligence framework using an app intent.

### [Testing](https://developer.apple.com/documentation/appintents\#Testing)

Verify that your intent, entity, query, and enum types work correctly.

[Verifying your App Intents implementation](https://developer.apple.com/documentation/appintents/verifying-your-app-intents-implementation)

Confirm that your app intents work correctly, the system can understand your content, and that it can run your app’s actions.

[Testing your App Intents code](https://developer.apple.com/documentation/appintentstesting/testing-your-app-intents-code)

Evaluate intents, entities, and queries, and verify your integration with system features like Spotlight and Siri.

[App Intents Testing](https://developer.apple.com/documentation/appintentstesting)

Test your app intents, entities, queries, and integration with system features like Siri or Spotlight.

Beta

### [Errors](https://developer.apple.com/documentation/appintents\#Errors)

Handle errors that occur when running your app intents.

[`struct AppIntentError`](https://developer.apple.com/documentation/appintents/appintenterror)

An error that indicates a problem occurred while performing an app intent.

[`protocol CustomAppIntentErrorConvertible`](https://developer.apple.com/documentation/appintents/customappintenterrorconvertible)

A type that the system automatically converts to an app intent error.

### [Deprecated](https://developer.apple.com/documentation/appintents\#Deprecated)

Avoid deprecated classes and protocols in your apps.

[API Reference\\
Deprecated symbols](https://developer.apple.com/documentation/appintents/deprecated-symbols)

Review unsupported symbols and their replacements.

### [Structures](https://developer.apple.com/documentation/appintents\#Structures)

[`struct EmptySnippetIntent`](https://developer.apple.com/documentation/appintents/emptysnippetintent)

A snippet intent that renders an empty view.

Current page is App Intents