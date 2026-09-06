# Core Media

Represent time-based audio-visual assets with essential data types.

## Overview

The Core Media framework defines the media pipeline used by AVFoundation and other high-level media frameworks found on Apple platforms. Use Core Media’s low-level data types and interfaces to efficiently process media samples and manage queues of media data.

## Topics

### Sample Processing

[CMSampleBuffer](/documentation/CoreMedia/cmsamplebuffer-api)

An object that contains zero or more media samples of a uniform media type.

[CMBlockBuffer](/documentation/CoreMedia/cmblockbuffer-api)

An object the system uses to move blocks of memory through a processing system.

[CMTaggedBufferGroup](/documentation/CoreMedia/cmtaggedbuffergroup)

Objective-C types and interfaces for working with Core Media tagged buffer groups.

[CMFormatDescription](/documentation/CoreMedia/cmformatdescription-api)

A media format descriptor that describes the samples in a sample buffer.

[CMAttachment](/documentation/CoreMedia/cmattachment-api)

Add supporting metadata to sample buffers.

[`CMTaggedBuffer`](/documentation/CoreMedia/CMTaggedBuffer)

An instance of a media buffer containing metadata tags.

[`CMMutableDataBlockBuffer`](/documentation/CoreMedia/CMMutableDataBlockBuffer)

A block buffer that provides read-write access to a range of bytes.

[`CMReadOnlyDataBlockBuffer`](/documentation/CoreMedia/CMReadOnlyDataBlockBuffer)

A block buffer that provides read-only access to the a range of bytes.

[`CMReadySampleBuffer`](/documentation/CoreMedia/CMReadySampleBuffer)

Buffer carrying readily available samples of media data.

[`CMSampleDataReference`](/documentation/CoreMedia/CMSampleDataReference)

References sample data in at a URL.

[`CMTaggedDynamicBuffer`](/documentation/CoreMedia/CMTaggedDynamicBuffer)

Contains a collection of tags associated with a read-only media buffer.

### Time Representation

[CMTime](/documentation/CoreMedia/cmtime-api)

A structure that represents time.

[CMTimeRange](/documentation/CoreMedia/cmtimerange-api)

A structure that represents a range of time.

[CMTimeMapping](/documentation/CoreMedia/cmtimemapping-api)

A structure that maps a segment of a source time range to a target time range.

### Media Synchronization

[CMClock](/documentation/CoreMedia/cmclock-api)

A reference clock you use to synchronize applications and devices.

[CMAudioClock](/documentation/CoreMedia/cmaudioclock-api)

A specialized reference clock that synchronizes with audio sources.

[CMTimebase](/documentation/CoreMedia/cmtimebase-api)

A model of a timeline under application control.

### Text Markup

[CMTextMarkup](/documentation/CoreMedia/cmtextmarkup)

Attributes that specify text markup in legible media.

### Metadata

[CMMetadata](/documentation/CoreMedia/cmmetadata)

The APIs for working with the framework’s Metadata Identifier Services and Metadata Data Type Registry.

[CMTag](/documentation/CoreMedia/cmtag-api)

Types and interfaces for working with Core Media tags.

[`CMTag`](/documentation/CoreMedia/CMTag-swift.class)

A tag to set additional metadata on media buffers.

[`CMTypedTag`](/documentation/CoreMedia/CMTypedTag)

A tag to set additional metadata on media buffers, with an associated Swift type for its value.

[CMTagCollection](/documentation/CoreMedia/cmtagcollection)

Objective-C types and interfaces for working with Core Media tag collections.

[`CMProjectionType`](/documentation/CoreMedia/CMProjectionType)

Constants describing the projection surface information in a 3D video buffer or channel.

[`CMStereoViewComponents`](/documentation/CoreMedia/CMStereoViewComponents)

Constants describing the stereo views contained within a buffer or channel.

[`CMStereoViewInterpretationOptions`](/documentation/CoreMedia/CMStereoViewInterpretationOptions)

Create a set of stereo view interpretation options from a constant.

[`CMPackingType`](/documentation/CoreMedia/CMPackingType)

The type of packing within each video frame, if any.

### Queues

[CMSimpleQueue](/documentation/CoreMedia/cmsimplequeue-api)

A simple, lockless FIFO queue of elements.

[CMBufferQueue](/documentation/CoreMedia/cmbufferqueue-api)

A queue of timed buffers.

[CMMemoryPool](/documentation/CoreMedia/cmmemorypool-api)

An object that optimizes memory allocation when working with large blocks of memory.

### Reference

[Core Media Constants](/documentation/CoreMedia/core-media-constants)

[Core Media Functions](/documentation/CoreMedia/core-media-functions)

[Core Media Type Aliases](/documentation/CoreMedia/core-media-type-aliases)

[Core Media Macros](/documentation/CoreMedia/core-media-macros)

### Reference

[Core Media Constants](/documentation/CoreMedia/core-media-constants)

[Core Media Functions](/documentation/CoreMedia/core-media-functions)

[Core Media Type Aliases](/documentation/CoreMedia/core-media-type-aliases)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
