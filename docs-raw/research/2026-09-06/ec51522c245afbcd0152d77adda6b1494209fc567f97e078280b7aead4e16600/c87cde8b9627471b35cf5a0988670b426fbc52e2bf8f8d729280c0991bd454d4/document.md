# Events

Respond to things happening in your RealityKit scene by subscribing to specific event types.

## Overview

You can receive notifications to specific RealityKit events
— all of which conform to the Event protocol —
by subscribing to specific events.
The kinds of events you can subscribe to include the following:

- Two entities colliding
- An entity receiving a new component
- Audio playback reaching the end of its content

For example, you can receive a notification:

- When two objects begin colliding by subscribing to [`CollisionEvents.Began`](/documentation/RealityKit/CollisionEvents/Began) event
- When the scene redraws by subscribing to the [`SceneEvents.Update`](/documentation/RealityKit/SceneEvents/Update) event

## Topics

### Core event types

[`Event`](/documentation/RealityKit/Event)

A type that can be sent as an event.

[`EventSource`](/documentation/RealityKit/EventSource)

A type on which events can be published and subscribed.

[`EventSubscription`](/documentation/RealityKit/EventSubscription)

A subscription to an event.

### Scene and entity lifecycle events

[`SceneEvents`](/documentation/RealityKit/SceneEvents)

Events the scene invokes.

[`AnchorStateEvents`](/documentation/RealityKit/AnchorStateEvents)

Events that trigger on an entity to indicate a change in anchor state.

[`ComponentEvents`](/documentation/RealityKit/ComponentEvents)

Provides the events related to components.

### Input and interaction events

[`AccessibilityEvents`](/documentation/RealityKit/AccessibilityEvents)

[`ManipulationEvents`](/documentation/RealityKit/ManipulationEvents)

Events that occur while a person manipulates an entity.

### Physics and motion events

[`AnimationEvents`](/documentation/RealityKit/AnimationEvents)

Notable milestones that the framework signals during animation playback.

[`CollisionEvents`](/documentation/RealityKit/CollisionEvents)

[`PhysicsSimulationEvents`](/documentation/RealityKit/PhysicsSimulationEvents)

Types of events that fire during physics simulations

### Media events

[`AudioEvents`](/documentation/RealityKit/AudioEvents)

Events associated with audio playback.

[`VideoPlayerEvents`](/documentation/RealityKit/VideoPlayerEvents)

Events associated with video playback for VideoPlayerComponent.

[`ImagePresentationEvents`](/documentation/RealityKit/ImagePresentationEvents)

Events associated with viewing mode transitions for image presentation components.

### Network synchronization events

[`SynchronizationEvents`](/documentation/RealityKit/SynchronizationEvents)

Events associated with network synchronization of scene information.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
