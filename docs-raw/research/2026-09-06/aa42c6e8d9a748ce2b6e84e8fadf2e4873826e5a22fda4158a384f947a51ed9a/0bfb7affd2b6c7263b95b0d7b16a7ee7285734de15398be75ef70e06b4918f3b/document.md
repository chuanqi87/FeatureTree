# Third-party casting support

Provide custom playback controls for third-party casting services and other media sources.

## Overview

Use the [`AVPlaybackUserInterfaceControllable`](/documentation/AVKit/AVPlaybackUserInterfaceControllable-92fri) protocol suite to build custom transport controls that work with third-party casting services. The [`AVPlaybackUserInterfaceControllable`](/documentation/AVKit/AVPlaybackUserInterfaceControllable-92fri) composite protocol combines playback, timeline, media selection, volume, and metadata capabilities into a single interface.

## Topics

### Playback

[`AVPlaybackUserInterfacePlaybackControllable`](/documentation/AVKit/AVPlaybackUserInterfacePlaybackControllable-9he54)

Provides playback control and state management for media content.

[`AVPlaybackUserInterfacePlaybackControllable`](/documentation/AVKit/AVPlaybackUserInterfacePlaybackControllable-81n66)

Provides playback control and state management for media content.

[`AVPlaybackUserInterfacePlaybackState`](/documentation/AVKit/AVPlaybackUserInterfacePlaybackState)

Describes possible transport states of the playback source.

[`AVPlaybackUserInterfaceSeekCapabilities`](/documentation/AVKit/AVPlaybackUserInterfaceSeekCapabilities)

Describes navigation capabilities of the media source.

### Timeline

[`AVPlaybackUserInterfaceTimeControllable`](/documentation/AVKit/AVPlaybackUserInterfaceTimeControllable-50vcy)

Provides time control and navigation capabilities for media content.

[`AVPlaybackUserInterfaceTimeControllable`](/documentation/AVKit/AVPlaybackUserInterfaceTimeControllable-62fq2)

Provides time control and navigation capabilities for media content.

[`AVPlaybackUserInterfacePlaybackPosition`](/documentation/AVKit/AVPlaybackUserInterfacePlaybackPosition)

A snapshot comprising a playback position recorded at a known host time and the rate of position
advancement.

[`AVPlaybackUserInterfaceTimelineSegment`](/documentation/AVKit/AVPlaybackUserInterfaceTimelineSegment)

Represents a contiguous segment of timeline content with specific playback characteristics.

[`AVPlaybackUserInterfaceTimelineSegmentType`](/documentation/AVKit/AVPlaybackUserInterfaceTimelineSegmentType)

Describes the type of content within a timeline segment.

### Media selection

[`AVPlaybackUserInterfaceMediaSelectionControllable`](/documentation/AVKit/AVPlaybackUserInterfaceMediaSelectionControllable-8ee5z)

Provides audio and subtitle selection capabilities for media content.

[`AVPlaybackUserInterfaceMediaSelectionControllable`](/documentation/AVKit/AVPlaybackUserInterfaceMediaSelectionControllable-2fftn)

Provides audio and subtitle selection capabilities for media content.

[`AVPlaybackUserInterfaceMediaSelectionOption`](/documentation/AVKit/AVPlaybackUserInterfaceMediaSelectionOption)

Represents a media selection option for audio tracks or subtitle tracks.

### Volume

[`AVPlaybackUserInterfaceVolumeControllable`](/documentation/AVKit/AVPlaybackUserInterfaceVolumeControllable-4vgi1)

Provides volume and audio muting control for media content.

[`AVPlaybackUserInterfaceVolumeControllable`](/documentation/AVKit/AVPlaybackUserInterfaceVolumeControllable-5ystg)

Provides volume and audio muting control for media content.

### Metadata

[`AVPlaybackUserInterfaceMetadataProviding`](/documentation/AVKit/AVPlaybackUserInterfaceMetadataProviding-814y4)

Provides metadata information about media content including title, artwork, and content type.

[`AVPlaybackUserInterfaceMetadataProviding`](/documentation/AVKit/AVPlaybackUserInterfaceMetadataProviding-1w04z)

Provides metadata information about media content including title, artwork, and content type.

[`AVPlaybackUserInterfaceContentMetadata`](/documentation/AVKit/AVPlaybackUserInterfaceContentMetadata-swift.struct)

A Swift-friendly structure representing media metadata.

[`AVPlaybackUserInterfaceContentMetadata`](/documentation/AVKit/AVPlaybackUserInterfaceContentMetadata-c.class)

Provides metadata information about media content including title, artwork, and content type.

[`AVPlaybackUserInterfaceContentMetadataTemplate`](/documentation/AVKit/AVPlaybackUserInterfaceContentMetadataTemplate)

A mutable template for configuring media metadata before creating immutable metadata objects.

[`AVPlaybackUserInterfaceContentArtwork`](/documentation/AVKit/AVPlaybackUserInterfaceContentArtwork)

Base class representing artwork or cover art for media content.

[`AVPlaybackUserInterfaceContentURLArtwork`](/documentation/AVKit/AVPlaybackUserInterfaceContentURLArtwork)

An artwork subclass that references artwork via a URL and content type.

[`AVPlaybackUserInterfaceContentVideoProperties`](/documentation/AVKit/AVPlaybackUserInterfaceContentVideoProperties)

Properties specific to video content.

### Complete interface

[`AVPlaybackUserInterfaceControllable`](/documentation/AVKit/AVPlaybackUserInterfaceControllable-92fri)

A comprehensive protocol that provides complete media control and information for playback, timeline navigation, audio/subtitle selection, volume control, and metadata access.

[`AVPlaybackUserInterfaceControllable`](/documentation/AVKit/AVPlaybackUserInterfaceControllable-7ti30)

A comprehensive protocol that provides complete media control and information for playback, timeline navigation, audio/subtitle selection, volume control, and metadata access.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
