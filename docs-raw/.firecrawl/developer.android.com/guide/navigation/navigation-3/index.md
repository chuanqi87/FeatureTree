[Skip to main content](https://developer.android.com/guide/navigation/navigation-3#main-content)

[![Android Developers](https://www.gstatic.com/devrel-devsite/prod/v6c08f9bb601564cd99488472d05cdf6fb06f007f31b6552465782b15883ce123/android/images/lockup.png)](https://developer.android.com/)

`/`

Language

- [English](https://developer.android.com/guide/navigation/navigation-3)
- [Deutsch](https://developer.android.com/guide/navigation/navigation-3?hl=de)
- [Español – América Latina](https://developer.android.com/guide/navigation/navigation-3?hl=es-419)
- [Français](https://developer.android.com/guide/navigation/navigation-3?hl=fr)
- [Indonesia](https://developer.android.com/guide/navigation/navigation-3?hl=id)
- [Italiano](https://developer.android.com/guide/navigation/navigation-3?hl=it)
- [Polski](https://developer.android.com/guide/navigation/navigation-3?hl=pl)
- [Português – Brasil](https://developer.android.com/guide/navigation/navigation-3?hl=pt-br)
- [Tiếng Việt](https://developer.android.com/guide/navigation/navigation-3?hl=vi)
- [Türkçe](https://developer.android.com/guide/navigation/navigation-3?hl=tr)
- [Русский](https://developer.android.com/guide/navigation/navigation-3?hl=ru)
- [עברית](https://developer.android.com/guide/navigation/navigation-3?hl=he)
- [العربيّة](https://developer.android.com/guide/navigation/navigation-3?hl=ar)
- [فارسی](https://developer.android.com/guide/navigation/navigation-3?hl=fa)
- [हिंदी](https://developer.android.com/guide/navigation/navigation-3?hl=hi)
- [বাংলা](https://developer.android.com/guide/navigation/navigation-3?hl=bn)
- [ภาษาไทย](https://developer.android.com/guide/navigation/navigation-3?hl=th)
- [中文 – 简体](https://developer.android.com/guide/navigation/navigation-3?hl=zh-cn)
- [中文 – 繁體](https://developer.android.com/guide/navigation/navigation-3?hl=zh-tw)
- [日本語](https://developer.android.com/guide/navigation/navigation-3?hl=ja)
- [한국어](https://developer.android.com/guide/navigation/navigation-3?hl=ko)

[Android Studio](https://developer.android.com/studio)

[Sign in](https://developer.android.com/_d/signin?continue=https%3A%2F%2Fdeveloper.android.com%2Fguide%2Fnavigation%2Fnavigation-3&prompt=select_account)

- [App architecture](https://developer.android.com/topic/architecture/intro)

- On this page
- [Android skills](https://developer.android.com/guide/navigation/navigation-3#android-skills-card__jetpack-navigation-3)
  - [Jetpack Navigation 3](https://developer.android.com/guide/navigation/navigation-3#skill-title_jetpack-navigation-3)
- [Improvements upon Jetpack Navigation](https://developer.android.com/guide/navigation/navigation-3#improvements)
- [Code samples](https://developer.android.com/guide/navigation/navigation-3#code-samples)

- [Android Developers](https://developer.android.com/)
- [Design & Plan](https://developer.android.com/design)
- [App architecture](https://developer.android.com/topic/architecture/intro)

Was this helpful?

# Navigation 3    Stay organized with collections      Save and categorize content based on your preferences.

- On this page
- [Android skills](https://developer.android.com/guide/navigation/navigation-3#android-skills-card__jetpack-navigation-3)
  - [Jetpack Navigation 3](https://developer.android.com/guide/navigation/navigation-3#skill-title_jetpack-navigation-3)
- [Improvements upon Jetpack Navigation](https://developer.android.com/guide/navigation/navigation-3#improvements)
- [Code samples](https://developer.android.com/guide/navigation/navigation-3#code-samples)

Use an Android skill to help you build using Jetpack Navigation 3.

To install the skill from the [Android CLI](https://developer.android.com/tools/agents/android-cli), run:

```
android skills add navigation-3
```

Navigation 3 is a new navigation library designed to work with Compose. With
Navigation 3, you have full control over your back stack, and navigating to and
from destinations is as simple as adding and removing items from a list. It
creates a flexible app navigation system by providing:

- Conventions for modeling a back stack, where each entry on the back stack
represents content that the user has navigated to
- A UI that automatically updates with back stack changes (including animations)
- A scope for items in the back stack, allowing state to be retained while an
item is in the back stack
- An adaptive layout system that allows multiple destinations to be displayed at
the same time, and allowing seamless switching between those layouts
- A mechanism for content to communicate with its parent layout (metadata)

At a high level, you implement Navigation 3 in the following ways:

1. Define the content that users can navigate to in your app, each with a unique
key, and add a function to resolve that key to the content. See [Resolve keys\\
to content](https://developer.android.com/guide/navigation/navigation-3/basics#resolve-keys).
2. Create a back stack that keys are pushed onto and removed as users navigate
your app. See [Create a back stack](https://developer.android.com/guide/navigation/navigation-3/basics#create-back).
3. Use a [`NavDisplay`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/NavDisplay.composable) to display your app's back stack. Whenever the back
stack changes, it updates the UI to display relevant content. See [Display\\
the back stack](https://developer.android.com/guide/navigation/navigation-3/basics#display-back).
4. Modify `NavDisplay`'s [scene strategies](https://developer.android.com/guide/navigation/navigation-3/custom-layouts) as needed to
support adaptive layouts and different platforms.

You can see the [full source code](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:navigation3/) for Navigation 3 on AOSP.

## Improvements upon Jetpack Navigation

Navigation 3 improves upon the original Jetpack Navigation API in the following
ways:

- Provides a simpler integration with Compose
- Offers you full control of the back stack
- Makes it possible to create layouts that can read more than one destination
from the back stack at the same time, allowing them to adapt to changes in
window size and other inputs.

Read more about Navigation 3's principles and API design choices in [this blog\\
post](https://android-developers.googleblog.com/2025/05/announcing-jetpack-navigation-3-for-compose.html).

## Code samples

The [recipes repository](https://github.com/android/nav3-recipes) contains examples of how to use the
Navigation 3 building blocks to solve common navigation challenges.

Was this helpful?

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.




\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-09-01 UTC."\],\[\],\[\]\]