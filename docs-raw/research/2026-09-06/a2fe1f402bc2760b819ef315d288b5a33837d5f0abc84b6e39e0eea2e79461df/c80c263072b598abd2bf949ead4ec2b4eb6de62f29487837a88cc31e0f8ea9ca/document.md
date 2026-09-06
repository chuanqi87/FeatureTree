# General media item property keys

System-defined properties for obtaining the metadata for a media item.

## Discussion

Obtain metadata for a media item by calling the [`value(forProperty:)`](/documentation/MediaPlayer/MPMediaEntity/value(forProperty:)) method with these property keys. You can use the filterable property keys to build media property predicates, which [`MPMediaPropertyPredicate`](/documentation/MediaPlayer/MPMediaPropertyPredicate) describes.

## Topics

### Property keys

[`MPMediaItemPropertyPlaybackDuration`](/documentation/MediaPlayer/MPMediaItemPropertyPlaybackDuration)

The playback duration of the media item.

[`MPMediaItemPropertyAlbumTrackNumber`](/documentation/MediaPlayer/MPMediaItemPropertyAlbumTrackNumber)

The track number of the media item, for a media item that is part of an album.

[`MPMediaItemPropertyAlbumTrackCount`](/documentation/MediaPlayer/MPMediaItemPropertyAlbumTrackCount)

The number of tracks for the album that contains the media item.

[`MPMediaItemPropertyDiscNumber`](/documentation/MediaPlayer/MPMediaItemPropertyDiscNumber)

The disc number of the media item, for a media item that is part of a multidisc album.

[`MPMediaItemPropertyDiscCount`](/documentation/MediaPlayer/MPMediaItemPropertyDiscCount)

The number of discs for the album that contains the media item.

[`MPMediaItemPropertyArtwork`](/documentation/MediaPlayer/MPMediaItemPropertyArtwork)

The artwork image for the media item.

[`MPMediaItemPropertyLyrics`](/documentation/MediaPlayer/MPMediaItemPropertyLyrics)

The lyrics for the media item.

[`MPMediaItemPropertyReleaseDate`](/documentation/MediaPlayer/MPMediaItemPropertyReleaseDate)

The date of the media item’s first public release.

[`MPMediaItemPropertyBeatsPerMinute`](/documentation/MediaPlayer/MPMediaItemPropertyBeatsPerMinute)

The number of musical beats per minute for the media item.

[`MPMediaItemPropertyComments`](/documentation/MediaPlayer/MPMediaItemPropertyComments)

Textual information about the media item.

[`MPMediaItemPropertyAssetURL`](/documentation/MediaPlayer/MPMediaItemPropertyAssetURL)

A URL that points to the media item.

[`MPMediaItemPropertyIsExplicit`](/documentation/MediaPlayer/MPMediaItemPropertyIsExplicit)

A Boolean value that indicates whether the media item contains explicit (adult) lyrics or language.

[`MPMediaItemPropertyIsPreorder`](/documentation/MediaPlayer/MPMediaItemPropertyIsPreorder)

A Boolean value that indicates whether the media item is a preorder.

[`MPMediaItemPropertyPlaybackStoreID`](/documentation/MediaPlayer/MPMediaItemPropertyPlaybackStoreID)

The identifier for enqueueing store tracks.

### Filterable property keys

[`MPMediaItemPropertyAlbumArtist`](/documentation/MediaPlayer/MPMediaItemPropertyAlbumArtist)

The primary performing artist for an album.

[`MPMediaItemPropertyAlbumArtistPersistentID`](/documentation/MediaPlayer/MPMediaItemPropertyAlbumArtistPersistentID)

The persistent identifier for an album artist.

[`MPMediaItemPropertyAlbumPersistentID`](/documentation/MediaPlayer/MPMediaItemPropertyAlbumPersistentID)

The key for the persistent identifier for an album.

[`MPMediaItemPropertyAlbumTitle`](/documentation/MediaPlayer/MPMediaItemPropertyAlbumTitle)

The title of an album.

[`MPMediaItemPropertyArtist`](/documentation/MediaPlayer/MPMediaItemPropertyArtist)

The performing artists for a media item — which may vary from the primary artist for the album that a media item belongs to.

[`MPMediaItemPropertyArtistPersistentID`](/documentation/MediaPlayer/MPMediaItemPropertyArtistPersistentID)

The key for the persistent identifier for an artist.

[`MPMediaItemPropertyComposer`](/documentation/MediaPlayer/MPMediaItemPropertyComposer)

The musical composer for the media item.

[`MPMediaItemPropertyComposerPersistentID`](/documentation/MediaPlayer/MPMediaItemPropertyComposerPersistentID)

The persistent identifier for a composer.

[`MPMediaItemPropertyGenre`](/documentation/MediaPlayer/MPMediaItemPropertyGenre)

The music or film genre of the media item.

[`MPMediaItemPropertyGenrePersistentID`](/documentation/MediaPlayer/MPMediaItemPropertyGenrePersistentID)

The persistent identifier for a genre.

[`MPMediaItemPropertyHasProtectedAsset`](/documentation/MediaPlayer/MPMediaItemPropertyHasProtectedAsset)

A Boolean value that indicates the media item has DRM protection so it can’t play through a standard playback API.

[`MPMediaItemPropertyIsCompilation`](/documentation/MediaPlayer/MPMediaItemPropertyIsCompilation)

A Boolean value that indicates whether the media item is part of a compilation.

[`MPMediaItemPropertyIsCloudItem`](/documentation/MediaPlayer/MPMediaItemPropertyIsCloudItem)

A Boolean value that indicates whether the media item is an iCloud item.

[`MPMediaItemPropertyMediaType`](/documentation/MediaPlayer/MPMediaItemPropertyMediaType)

The media type of the media item.

[`MPMediaItemPropertyPersistentID`](/documentation/MediaPlayer/MPMediaItemPropertyPersistentID)

The key for the persistent identifier for the media item.

[`MPMediaItemPropertyPlayCount`](/documentation/MediaPlayer/MPMediaItemPropertyPlayCount)

The number of times the user plays the media item.

[`MPMediaItemPropertyPodcastPersistentID`](/documentation/MediaPlayer/MPMediaItemPropertyPodcastPersistentID)

The persistent identifier for an audio podcast.

[`MPMediaItemPropertyPodcastTitle`](/documentation/MediaPlayer/MPMediaItemPropertyPodcastTitle)

The title of a podcast.

[`MPMediaItemPropertyTitle`](/documentation/MediaPlayer/MPMediaItemPropertyTitle)

The title or name of the media item.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
