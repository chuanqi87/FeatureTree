# App intents

Make your app’s custom actions available to the system by using app intent types.

## Overview

An app intent expresses one of your app’s capabilities to the system, and contains
code to perform that action. You express your app intents as types that adopt the
[`AppIntent`](/documentation/AppIntents/AppIntent) protocol and specify the data you need to perform the action. For specific
types of actions, you might also base your intents on other [app intent types](/documentation/AppIntents/app-intent-types).
For example, if your app intent launches your app and displays some content, use the
[`OpenIntent`](/documentation/AppIntents/OpenIntent) protocol instead. If an app intent supports system features, adopt a schema from an
[app schema domain](/documentation/AppIntents/app-schema-domains).

If your app intent requires data to complete its action, specify those data requirements using
parameters. An app intent parameter is a property that you annotate with the `@Parameter`
macro. To improve the experience of specifying parameter values, include parameter summaries.

An intent returns a result to tell the system when it completes its action, and whether the
action was successful or failed. A result can also provide textual or view-based content for
Siri or the Shortcuts app to incorporate into conversations.

## Topics

### App intent definition

[Creating your first app intent](/documentation/AppIntents/Creating-your-first-app-intent)

Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.

[Accelerating app interactions with App Intents](/documentation/AppIntents/AcceleratingAppInteractionsWithAppIntents)

Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts.

  <doc://com.apple.documentation/documentation/SiriKit/soup-chef-with-app-intents-migrating-custom-intents>

[`AppIntent`](/documentation/AppIntents/AppIntent)

An interface you use to express app-specific actions and make them available to
the rest of the system.

[App intent types](/documentation/AppIntents/app-intent-types)

Build your intents from types that define common behaviors such as opening or deleting
items, playing or recording media, and more.

### Add-on behaviors

[`UndoableIntent`](/documentation/AppIntents/UndoableIntent)

An interface you use to register undoable actions in your app intent code.

[`CancellableIntent`](/documentation/AppIntents/CancellableIntent)

An interface to support the graceful cancellation of your app intent’s task.

[`LongRunningIntent`](/documentation/AppIntents/LongRunningIntent)

An interface you use to extend the background execution time of an app intent
that performs a long-running task.

[`PredictableIntent`](/documentation/AppIntents/PredictableIntent)

An interface that indicates the system can suggest the intent as a potential action to run.

[`IntentPrediction`](/documentation/AppIntents/IntentPrediction)

A prediction for an app intent that the system might display to someone when it’s relevant.

### Parameters

[Adding parameters to an app intent](/documentation/AppIntents/Adding-parameters-to-an-app-intent)

Enable people to configure app intents with their custom input values.

[`IntentParameter`](/documentation/AppIntents/IntentParameter)

A property wrapper that indicates the associated property is an input argument of the app intent.

[`IntentParameterDependency`](/documentation/AppIntents/IntentParameterDependency)

A property wrapper that represents an app intent dependency you use to provide dynamic options.

[`IntentParameterContext`](/documentation/AppIntents/IntentParameterContext)

A type that provides information about an associated parameter during value resolution.

[`InputConnectionBehavior`](/documentation/AppIntents/InputConnectionBehavior)

Describes the input behaviors for connecting a parameter to the output of the previous App Intent.

[`DynamicOptionsProvider`](/documentation/AppIntents/DynamicOptionsProvider)

An interface for providing a dynamic list of options for a parameter of your app intent.

[Resolvers](/documentation/AppIntents/resolvers)

Resolve the parameters of your app intents, and extend the standard resolution
types to include your app’s custom types.

### Disambiguation

[`IntentChoiceOption`](/documentation/AppIntents/IntentChoiceOption)

A structure representing an entry in a list of options for a person to choose from before an app intent resumes its action.

[`ConfirmationConditions`](/documentation/AppIntents/ConfirmationConditions)

Conditions for a confirmation request.

### Results

[`IntentResult`](/documentation/AppIntents/IntentResult)

A type that contains the result of performing an action, and includes optional information to deliver back to the initiator.

[`IntentDialog`](/documentation/AppIntents/IntentDialog)

The text you want the system to display, or speak, when requesting a value, asking for
disambiguation, or confirming an action.

[`IntentResultContainer`](/documentation/AppIntents/IntentResultContainer)

An object that represents the output of a completed intent.

[`ProvidesDialog`](/documentation/AppIntents/ProvidesDialog)

The result of performing an action that delivers a dialog back to the initiator of the action.

[`ReturnsValue`](/documentation/AppIntents/ReturnsValue)

The result of performing an action that delivers a value back to the initiator.

[`ShowsSnippetView`](/documentation/AppIntents/ShowsSnippetView)

The result of performing an action that delivers a view back to the initiator of the action.

[`ResultsCollection`](/documentation/AppIntents/ResultsCollection)

A protocol representing a collection of returned items with support for sectioning.

[`OpensIntent`](/documentation/AppIntents/OpensIntent)

A result type that indicates your app intent returns another app intent.

### Dependency management

[`AppDependencyManager`](/documentation/AppIntents/AppDependencyManager)

An object that manages the registration and initialization of an app intent’s
dependencies.

[`AppDependency`](/documentation/AppIntents/AppDependency)

A property wrapper that resolves a registered dependency at runtime.

### Shortcuts support

[`ParameterSummary`](/documentation/AppIntents/ParameterSummary)

An interface for defining the visual representation of an app intent’s parameters.

[`IntentParameterSummary`](/documentation/AppIntents/IntentParameterSummary)

A type that describes the user interface configuration of an app intent’s parameters.

[`ParameterSummaryString`](/documentation/AppIntents/ParameterSummaryString)

A human-readable string that interpolates parameter key paths to provide user-configurable placeholders in the Shortcuts app.

[`ParameterSummaryWhenCondition`](/documentation/AppIntents/ParameterSummaryWhenCondition)

A type that represents a conditional statement in a parameter summary.

[`ParameterSummarySwitchCondition`](/documentation/AppIntents/ParameterSummarySwitchCondition)

A type that represents a switch statement in a parameter summary.

[`ParameterSummaryCaseCondition`](/documentation/AppIntents/ParameterSummaryCaseCondition)

A type that represents an individual case of a switch statement in a parameter summary.

[`ParameterSummaryDefaultCaseCondition`](/documentation/AppIntents/ParameterSummaryDefaultCaseCondition)

A type that represents the default case of a switch statement in a parameter summary.

### Intent-related data

[`IntentModes`](/documentation/AppIntents/IntentModes)

A set of options you use to configure the runtime behavior of an app intent.

[`IntentSystemContext`](/documentation/AppIntents/IntentSystemContext)

Contextual information that the system provides while it performs an app intent.

[`IntentDescription`](/documentation/AppIntents/IntentDescription)

The human-readable description and metadata for an app intent.

[`IntentDialog`](/documentation/AppIntents/IntentDialog)

The text you want the system to display, or speak, when requesting a value, asking for
disambiguation, or confirming an action.

[`IntentDeprecation`](/documentation/AppIntents/IntentDeprecation)

[`IntentProjection`](/documentation/AppIntents/IntentProjection)

Projections for an app intent that returns non-optional values for parameters.

### Type conversions

[`IntentValueConvertible`](/documentation/AppIntents/IntentValueConvertible)

A protocol that allows the system to use types to as app intent parameters or properties.

[`IntentValueConvertibleWrapper`](/documentation/AppIntents/IntentValueConvertibleWrapper)

A protocol for types that wrap another intent value that supports conversion.

[`IntentValueExpressing`](/documentation/AppIntents/IntentValueExpressing)

A protocol for types that can create intent value expressions.

### Intent queries

[`IntentValueQuery`](/documentation/AppIntents/IntentValueQuery)

A query that provides entity values to the system; for example,
for visual intelligence search.

[`IntentValueContainer`](/documentation/AppIntents/IntentValueContainer)

A container that stores a value that supports intent value conversion.

[`IntentValueExpression`](/documentation/AppIntents/IntentValueExpression)

A type that represents a lazily evaluated intent value.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
