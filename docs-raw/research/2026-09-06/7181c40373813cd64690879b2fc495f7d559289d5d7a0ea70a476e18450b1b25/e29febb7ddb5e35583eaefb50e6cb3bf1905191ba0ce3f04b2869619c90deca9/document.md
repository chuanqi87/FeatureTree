# Get a Media Queue

Provide a playback queue from a successfully processed play media intent.

## Discussion

There isn’t a default path for this endpoint. Specify the URL for this endpoint in your [`ExtensionConfig.Media.Queues.PlayMedia`](/documentation/SiriKitCloudMedia/ExtensionConfig/Media-data.dictionary/Queues-data.dictionary/PlayMedia-data.dictionary) object.

## Topics

### Receiving a Queue Request

[`PlayMediaRequest`](/documentation/SiriKitCloudMedia/PlayMediaRequest)

A request for a media playback queue.

### Creating or Updating a Playback Queue

[`Queue`](/documentation/SiriKitCloudMedia/Queue)

A sequence of media content for playback, with links to the previous and next segments of a full playback queue.

[`QueueIdentifier`](/documentation/SiriKitCloudMedia/QueueIdentifier)

A stable identifier for a playback queue.

[`QueueInsertPointer`](/documentation/SiriKitCloudMedia/QueueInsertPointer)

Instructions for editing the current playback queue.

[`QueuePlayPointer`](/documentation/SiriKitCloudMedia/QueuePlayPointer)

A position within a playback queue.

### Providing Queue Items

[`Content`](/documentation/SiriKitCloudMedia/Content)

A description of a piece of playback content, such as a song, podcast, or advertisement.

[`ContentIdentifier`](/documentation/SiriKitCloudMedia/ContentIdentifier)

An identifier for a song, podcast, ad, or other media content. The identifier must be stable and unique within a queue.

[`ContentAttributes`](/documentation/SiriKitCloudMedia/ContentAttributes)

Metadata for some media content.

### Customizing Playback Controls

[`QueueControlMapping`](/documentation/SiriKitCloudMedia/QueueControlMapping)

A dictionary of configuration names and the media controls they permit.

[`PlayMediaControl`](/documentation/SiriKitCloudMedia/PlayMediaControl)

A configuration for permitted user interactions and other player behaviors during playback.

[`PlayMediaControlScheme`](/documentation/SiriKitCloudMedia/PlayMediaControlScheme)

Default playback controls and settings for common content types.

[`PlayMediaControlCommandSet`](/documentation/SiriKitCloudMedia/PlayMediaControlCommandSet)

A set of modifications to apply to the default set of available playback controls.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
