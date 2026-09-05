* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/backgroundtasks#app-main)

Framework

# Background Tasks

Support background processing in your app by wrapping your app’s most critical work in framework-provided tasks.

iOS 13.0+iPadOS 13.0+Mac Catalyst 13.1+tvOS 13.0+visionOS 1.0+

## [Overview](https://developer.apple.com/documentation/backgroundtasks\#overview)

Use this framework to keep your app content up to date and run tasks requiring minutes to complete even if your app is in the background. Longer tasks can leverage external power, network connectivity, and the GPU on supported devices.

To launch your app in the background and perform necessary work, register launch handlers for framework-provided tasks and schedule the tasks as needed.

Your app can also use a framework-provided task to execute critical jobs in the foreground and complete them in the background if a person backgrounds your app before the job completes.

## [Topics](https://developer.apple.com/documentation/backgroundtasks\#topics)

### [Essentials](https://developer.apple.com/documentation/backgroundtasks\#Essentials)

[Background Tasks updates](https://developer.apple.com/documentation/updates/backgroundtasks)

Learn about important changes in Background Tasks.

[`class BGTaskScheduler`](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler)

A class for scheduling tasks that add background support to your app’s most critical work.

[`class BGTask`](https://developer.apple.com/documentation/backgroundtasks/bgtask)

An abstract class for the framework’s tasks.

### [Background tasks](https://developer.apple.com/documentation/backgroundtasks\#Background-tasks)

[Using background tasks to update your app](https://developer.apple.com/documentation/uikit/using-background-tasks-to-update-your-app)

Configure your app to perform tasks in the background to make efficient use of processing time and power.

[Refreshing and Maintaining Your App Using Background Tasks](https://developer.apple.com/documentation/backgroundtasks/refreshing-and-maintaining-your-app-using-background-tasks)

Use scheduled background tasks for refreshing your app content and for performing maintenance.

[Choosing Background Strategies for Your App](https://developer.apple.com/documentation/backgroundtasks/choosing-background-strategies-for-your-app)

Select the best method of scheduling background runtime for your app.

[`class BGProcessingTask`](https://developer.apple.com/documentation/backgroundtasks/bgprocessingtask)

A time-consuming processing task that runs while the app is in the background.

[`class BGAppRefreshTask`](https://developer.apple.com/documentation/backgroundtasks/bgapprefreshtask)

An object representing a short task typically used to refresh content that’s run while the app is in the background.

[`class BGHealthResearchTask`](https://developer.apple.com/documentation/backgroundtasks/bghealthresearchtask)

A time-consuming, necessary processing task that runs while the app is in the background to prepare data essential to a health research study.

### [Foreground tasks with background support](https://developer.apple.com/documentation/backgroundtasks\#Foreground-tasks-with-background-support)

[Performing long-running tasks on iOS and iPadOS](https://developer.apple.com/documentation/backgroundtasks/performing-long-running-tasks-on-ios-and-ipados)

Use a continuous background task to do work that can complete as needed.

[`class BGContinuedProcessingTask`](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask)

A task that starts in the foreground and can continue running in the background as needed.

[`Background GPU Access`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.gpu)

The entitlement the system requires for a continuous background task to use the GPU.

### [Task requests](https://developer.apple.com/documentation/backgroundtasks\#Task-requests)

[`class BGProcessingTaskRequest`](https://developer.apple.com/documentation/backgroundtasks/bgprocessingtaskrequest)

A request to launch your app in the background to execute a processing task that can take minutes to complete.

[`class BGAppRefreshTaskRequest`](https://developer.apple.com/documentation/backgroundtasks/bgapprefreshtaskrequest)

A request to launch your app in the background to execute a short refresh task.

[`class BGTaskRequest`](https://developer.apple.com/documentation/backgroundtasks/bgtaskrequest)

An abstract class for representing task requests.

[`class BGHealthResearchTaskRequest`](https://developer.apple.com/documentation/backgroundtasks/bghealthresearchtaskrequest)

A request to launch your app in the background to execute processing for a health research study in which a user participates.

[`class BGContinuedProcessingTaskRequest`](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest)

A request for a workload that the system continues processing even if a person backgrounds the app.

### [Development and testing](https://developer.apple.com/documentation/backgroundtasks\#Development-and-testing)

[Starting and Terminating Tasks During Development](https://developer.apple.com/documentation/backgroundtasks/starting-and-terminating-tasks-during-development)

Use the debugger during development to start tasks and to terminate them before completion.

Current page is Background Tasks