[Skip to main content](https://developer.android.com/guide/navigation#main-content)

[![Android Developers](https://www.gstatic.com/devrel-devsite/prod/v5e941f15ff6710591bee254538202655020220785b40a3f4d932e94adb9f6037/android/images/lockup.png)](https://developer.android.com/)

`/`

Language

- [English](https://developer.android.com/guide/navigation)
- [Deutsch](https://developer.android.com/guide/navigation?hl=de)
- [Español – América Latina](https://developer.android.com/guide/navigation?hl=es-419)
- [Français](https://developer.android.com/guide/navigation?hl=fr)
- [Indonesia](https://developer.android.com/guide/navigation?hl=id)
- [Italiano](https://developer.android.com/guide/navigation?hl=it)
- [Polski](https://developer.android.com/guide/navigation?hl=pl)
- [Português – Brasil](https://developer.android.com/guide/navigation?hl=pt-br)
- [Tiếng Việt](https://developer.android.com/guide/navigation?hl=vi)
- [Türkçe](https://developer.android.com/guide/navigation?hl=tr)
- [Русский](https://developer.android.com/guide/navigation?hl=ru)
- [עברית](https://developer.android.com/guide/navigation?hl=he)
- [العربيّة](https://developer.android.com/guide/navigation?hl=ar)
- [فارسی](https://developer.android.com/guide/navigation?hl=fa)
- [हिंदी](https://developer.android.com/guide/navigation?hl=hi)
- [বাংলা](https://developer.android.com/guide/navigation?hl=bn)
- [ภาษาไทย](https://developer.android.com/guide/navigation?hl=th)
- [中文 – 简体](https://developer.android.com/guide/navigation?hl=zh-cn)
- [中文 – 繁體](https://developer.android.com/guide/navigation?hl=zh-tw)
- [日本語](https://developer.android.com/guide/navigation?hl=ja)
- [한국어](https://developer.android.com/guide/navigation?hl=ko)

[Android Studio](https://developer.android.com/studio)

[Sign in](https://developer.android.com/_d/signin?continue=https%3A%2F%2Fdeveloper.android.com%2Fguide%2Fnavigation&prompt=select_account)

- [App architecture](https://developer.android.com/topic/architecture/intro)

- On this page
- [Key concepts](https://developer.android.com/guide/navigation#types)
- [Benefits and features](https://developer.android.com/guide/navigation#benefits)
- [Framework options](https://developer.android.com/guide/navigation#framework-options)
- [Set up your environment](https://developer.android.com/guide/navigation#set-up)
- [Next steps](https://developer.android.com/guide/navigation#next-steps)
  - [Detailed guides](https://developer.android.com/guide/navigation#detail)
  - [Codelabs](https://developer.android.com/guide/navigation#addt-resources-codelabs)
  - [Videos](https://developer.android.com/guide/navigation#addt-resources-videos)
  - [Samples](https://developer.android.com/guide/navigation#addt-resources-samples)

- [Android Developers](https://developer.android.com/)
- [Design & Plan](https://developer.android.com/design)
- [App architecture](https://developer.android.com/topic/architecture/intro)

Was this helpful?

# Navigation    Stay organized with collections      Save and categorize content based on your preferences.

- On this page
- [Key concepts](https://developer.android.com/guide/navigation#types)
- [Benefits and features](https://developer.android.com/guide/navigation#benefits)
- [Framework options](https://developer.android.com/guide/navigation#framework-options)
- [Set up your environment](https://developer.android.com/guide/navigation#set-up)
- [Next steps](https://developer.android.com/guide/navigation#next-steps)
  - [Detailed guides](https://developer.android.com/guide/navigation#detail)
  - [Codelabs](https://developer.android.com/guide/navigation#addt-resources-codelabs)
  - [Videos](https://developer.android.com/guide/navigation#addt-resources-videos)
  - [Samples](https://developer.android.com/guide/navigation#addt-resources-samples)

Android Jetpack: Introducing Navigation component - YouTube

Tap to unmute

[Android Jetpack: Introducing Navigation component](https://www.youtube.com/watch?v=Y0Cs2MQxyIs) [Android Developers](https://www.youtube.com/channel/UCVHFbqXqoYvEWM1Ddxl0QDg)

![thumbnail-image](https://yt3.ggpht.com/oNn1SujiwAbtcRmekf88IPF3JtKJyfxiEgbEDbCmDlozxe-gxbctOD5JExj5ViAuX4woBisLjxQ=s68-c-k-c0x00ffffff-no-rj)

Android Developers1.43M subscribers

[Watch on](https://www.youtube.com/watch?v=Y0Cs2MQxyIs)

Navigation refers to the interactions that let users navigate across, into, and
back out from the different pieces of content within your app.

Android Jetpack's Navigation component includes the [Navigation\\
library](https://developer.android.com/jetpack/androidx/releases/navigation), [Safe Args Gradle plug-in](https://developer.android.com/guide/navigation/navigation-pass-data#Safe-args),
and tooling to help you implement app navigation. The Navigation component
handles diverse navigation use cases, from straightforward button clicks to more
complex patterns, such as app bars and the navigation drawer.

## Key concepts

The following table provides an overview of the key concepts in
navigation and the main types that you use to implement them.

| Concept | Purpose | Type |
| --- | --- | --- |
| Host | A UI element that contains the current navigation destination. That is, when a user navigates through an app, the app essentially swaps destinations in and out of the navigation host. | - **Compose**: [`NavHost`](https://developer.android.com/reference/kotlin/androidx/navigation/compose/package-summary#NavHost(androidx.navigation.NavHostController,androidx.navigation.NavGraph,androidx.compose.ui.Modifier,androidx.compose.ui.Alignment,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1))<br>- **Fragments**: [`NavHostFragment`](https://developer.android.com/reference/androidx/navigation/fragment/NavHostFragment) |
| Graph | A data structure that defines all the navigation destinations within the app and how they connect together. | [`NavGraph`](https://developer.android.com/reference/androidx/navigation/NavGraph) |
| Controller | The central coordinator for managing navigation between destinations. The controller offers methods for navigating between destinations, handling deep links, managing the back stack, and more. | [`NavController`](https://developer.android.com/reference/androidx/navigation/NavController) |
| Destination | A node in the navigation graph. When the user navigates to this node, the host displays its content. | [`NavDestination`](https://developer.android.com/reference/androidx/navigation/NavDestination)<br>Typically created when constructing the navigation graph. |
| Route | Uniquely identifies a destination and any data required by it.<br>You can navigate using routes. Routes take you to destinations. | Any serializable data type. |

## Benefits and features

The Navigation component provides a number of other benefits and features,
including the following:

- **Animations and transitions:** Provides standardized resources for
animations and transitions.
- **Deep linking:** Implements and handles deep links that take the user
directly to a destination.
- **UI patterns:** Supports patterns such as navigation drawers and bottom
navigation with minimal additional work.
- **Type safety:** Includes support for passing data between destinations with
[type safety](https://developer.android.com/guide/navigation/design/type-safety).
- **ViewModel support:** Enables scoping a `ViewModel` to a navigation graph
to share UI-related data between the graph's destinations.
- **Fragment transactions:** Fully supports and handles fragment transactions.
- **Back and up:** Handles back and up actions correctly by default.

## Framework options

The Navigation component supports two primary frameworks for implementing your
navigation graph, depending on your app's UI architecture:

- **Compose**: If your app is built entirely with Jetpack Compose, use
Navigation Compose. Destinations in your graph are composables.
- **Fragments**: If your app uses Views or a mix of Views and Compose, use the
Fragment-based Navigation component. Destinations in your graph are
fragments that can host standard Views, Compose content, or a combination
of both.

For applications migrating from Views to Compose, the recommended strategy is
to continue using the Fragment-based Navigation component while converting
individual screens to Compose. Once all fragments have been replaced with
composables, you can migrate the navigation graph to Navigation Compose.

## Set up your environment

To include navigation support in your project, add the following dependencies to
your app's `build.gradle` file:

[Groovy](https://developer.android.com/guide/navigation#groovy)[Kotlin](https://developer.android.com/guide/navigation#kotlin)More

```
plugins {
  // Kotlin serialization plugin for type safe routes and navigation arguments
  id 'org.jetbrains.kotlin.plugin.serialization' version '2.0.21'
}

dependencies {
  def nav_version = "2.10.0"

  // Jetpack Compose Integration
  implementation "androidx.navigation:navigation-compose:$nav_version"

  // Views/Fragments Integration
  implementation "androidx.navigation:navigation-fragment:$nav_version"
  implementation "androidx.navigation:navigation-ui:$nav_version"

  // Feature module support for Fragments
  implementation "androidx.navigation:navigation-dynamic-features-fragment:$nav_version"

  // Testing Navigation
  androidTestImplementation "androidx.navigation:navigation-testing:$nav_version"

  // JSON serialization library, works with the Kotlin serialization plugin.
  implementation "org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3"
}
```

```
plugins {
  // Kotlin serialization plugin for type safe routes and navigation arguments
  kotlin("plugin.serialization") version "2.0.21"
}

dependencies {
  val nav_version = "2.10.0"

  // Jetpack Compose integration
  implementation("androidx.navigation:navigation-compose:$nav_version")

  // Views/Fragments integration
  implementation("androidx.navigation:navigation-fragment:$nav_version")
  implementation("androidx.navigation:navigation-ui:$nav_version")

  // Feature module support for Fragments
  implementation("androidx.navigation:navigation-dynamic-features-fragment:$nav_version")

  // Testing Navigation
  androidTestImplementation("androidx.navigation:navigation-testing:$nav_version")

  // JSON serialization library, works with the Kotlin serialization plugin
  implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3")
}
```

For information on adding other architecture components to your project, see
[Add components to your project](https://developer.android.com/topic/libraries/architecture/adding-components#navigation).

## Next steps

For more documentation and resources related to the Navigation component, see
the following resources.

### Detailed guides

For more information on how to implement a navigation host and `NavController`,
as well as detail on how they interact with Compose and other UI frameworks, see
the following guides:

- [Create a navigation controller](https://developer.android.com/guide/navigation/navcontroller): Outlines how to create a
`NavController`.
- [Create your navigation graph](https://developer.android.com/guide/navigation/design): Details how to create a navigation host
and a navigation graph.
- [Navigate to a destination](https://developer.android.com/guide/navigation/use-graph/navigate): Demonstrates how to use a `NavController` to
move between the destinations in your graph.

### Codelabs

- [Learn Jetpack Navigation](https://developer.android.com/codelabs/android-navigation)
- [Fragments and the Navigation Component](https://developer.android.com/codelabs/basic-android-kotlin-training-fragments-navigation-component)
- [Build an adaptive app with dynamic navigation](https://developer.android.com/codelabs/basic-android-kotlin-compose-adaptive-navigation-for-large-screens#0)

### Videos

- [Navigating navigation](https://www.youtube.com/watch?v=09qjn706ITA)
- [10 best practices for moving to a single activity](https://www.youtube.com/watch?v=9O1D_Ytk0xg)
- [Single activity: Why, when, and how (Android Dev Summit '18)](https://www.youtube.com/watch?v=2k8x8V77CrU)
- [Android Jetpack: Manage UI navigation with navigation controller (Google\\
I/O '18)](https://www.youtube.com/watch?v=8GCXtCjtg40)

### Samples

[![](https://raw.github.com/android/compose-samples//main/Jetcaster/readme/jetcaster-hero.png)](https://github.com/android/compose-samples/tree/main/Jetcaster)

GitHub

[**Jetcaster sample 🎙️**](https://github.com/android/compose-samples/tree/main/Jetcaster)

Jetcaster is a sample podcast app, built with Jetpack Compose. The goal of the sample is to showcase building with Compose across multiple form factors (mobile, TV, and Wear) and full featured architecture.
To try out this sample app, use the latest

[![](https://raw.github.com/android/compose-samples//main/Jetchat//screenshots/screenshots.png)](https://github.com/android/compose-samples/tree/main/Jetchat)

GitHub

[**Jetchat sample**](https://github.com/android/compose-samples/tree/main/Jetchat)

Jetchat is a sample chat app built with Jetpack Compose.
To try out this sample app, use the latest stable version of Android Studio. You can clone this repository or import the project from Android Studio following the steps here.
This sample

[![](https://raw.github.com/android/compose-samples//main/Jetsnack//screenshots/screenshots.png)](https://github.com/android/compose-samples/tree/main/Jetsnack)

GitHub

[**Jetsnack sample**](https://github.com/android/compose-samples/tree/main/Jetsnack)

Jetsnack is a sample snack ordering app built with Jetpack Compose.
To try out this sample app, use the latest stable version of Android Studio. You can clone this repository or import the project from Android Studio following the steps here.
This

[![](https://raw.github.com/android/architecture-samples//main//screenshots/screenshots.png)](https://github.com/android/architecture-samples/tree/main)

GitHub

[**Architecture**](https://github.com/android/architecture-samples/tree/main)

These samples showcase different architectural approaches to developing Android apps. In its different branches you'll find the same app (a TODO app) implemented with small differences.
In this branch you'll find:
User Interface built with Jetpack

[![](https://raw.github.com/android/compose-samples//main/JetNews//screenshots/screenshots.png)](https://github.com/android/compose-samples/tree/main/JetNews)

GitHub

[**Jetnews sample**](https://github.com/android/compose-samples/tree/main/JetNews)

Jetnews is a sample news reading app, built with Jetpack Compose. The goal of the sample is to showcase the current UI capabilities of Compose.
To try out this sample app, use the latest stable version of Android Studio. You can clone this repository

[![](https://raw.github.com/android/nowinandroid//main//docs/images/screenshots.png)](https://github.com/android/nowinandroid/tree/main)

GitHub

[**Now in Android App**](https://github.com/android/nowinandroid/tree/main)

Learn how this app was designed and built in the design case study, architecture learning journey and modularization learning journey.
This is the repository for the Now in Android app. It is a work in progress 🚧.
Now in Android is a fully functional

expand\_lessLessMoreexpand\_more

Was this helpful?

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.




\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-08-26 UTC."\],\[\],\[\]\]