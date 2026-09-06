# MediaLibrary Constants

## Topics

### Constants

[Aperture Media Group Type Identifiers](/documentation/MediaLibrary/aperture-media-group-type-identifiers)

Identifiers for media group types in the Aperture media source. These constants are used to specify a media group’s [`typeIdentifier`](/documentation/MediaLibrary/MLMediaGroup/typeIdentifier) attribute.

[Final Cut Pro Media Group Type Identifiers](/documentation/MediaLibrary/final-cut-pro-media-group-type-identifiers)

Identifiers for media group types in the Final Cut Pro media source. These constants are used to specify a media group’s [`typeIdentifier`](/documentation/MediaLibrary/MLMediaGroup/typeIdentifier) attribute.

[Folders Media Group Type Identifiers](/documentation/MediaLibrary/folders-media-group-type-identifiers)

Identifiers for media group types in folder-based media sources. These constants are used to specify a media group’s [`typeIdentifier`](/documentation/MediaLibrary/MLMediaGroup/typeIdentifier) attribute.

[GarageBand Media Group Type Identifiers](/documentation/MediaLibrary/garageband-media-group-type-identifiers)

Identifiers for media group types in the GarageBand media source. These constants are used to specify a media group’s [`typeIdentifier`](/documentation/MediaLibrary/MLMediaGroup/typeIdentifier) attribute.

[Logic Media Group Type Identifiers](/documentation/MediaLibrary/logic-media-group-type-identifiers)

Identifiers for media group types in the Logic media source. These constants are used to specify a media group’s [`typeIdentifier`](/documentation/MediaLibrary/MLMediaGroup/typeIdentifier) attribute.

[`MLMediaLoadAppFoldersKey`](/documentation/MediaLibrary/MLMediaLoadAppFoldersKey)

Specifies one or more relative paths inside the caller’s app bundle in which to search for media files. The value for this key is an array of strings (relative paths inside the caller’s app bundle).

[`MLMediaLoadAppleLoops`](/documentation/MediaLibrary/MLMediaLoadAppleLoops)

Identifies the folder containing audio loops from Apple.

[`MLMediaLoadExcludeSourcesKey`](/documentation/MediaLibrary/MLMediaLoadExcludeSourcesKey)

Defines which media sources to exclude when loading. This option is processed after [`MLMediaLoadIncludeSourcesKey`](/documentation/MediaLibrary/MLMediaLoadIncludeSourcesKey). The value for this key is an array of strings (media source identifiers). For a list of valid media source identifiers, see [Media Source Identifiers](/documentation/MediaLibrary/media-source-identifiers).

[`MLMediaLoadFoldersKey`](/documentation/MediaLibrary/MLMediaLoadFoldersKey)

Specifies the well-known folders that should be searched for media files. If this key is not present, none of the well-known folders will be provided. The value for this key is an array of strings (identifiers that correspond to well-known folder locations). For a list of well-known folder identifiers, see [Well-Known Folder Identifiers](/documentation/MediaLibrary/well-known-folder-identifiers).

[`MLMediaLoadIncludeSourcesKey`](/documentation/MediaLibrary/MLMediaLoadIncludeSourcesKey)

Defines which media sources to include when loading. If not present, load all available media sources. This option is processed after [`MLMediaLoadSourceTypesKey`](/documentation/MediaLibrary/MLMediaLoadSourceTypesKey). If [`MLMediaLoadIncludeSourcesKey`](/documentation/MediaLibrary/MLMediaLoadIncludeSourcesKey) is present but [`MLMediaLoadSourceTypesKey`](/documentation/MediaLibrary/MLMediaLoadSourceTypesKey) is not, then only those sources specified here will be loaded. This is useful for loading a single media source. When both keys are present, this is useful for adding one or more media sources that normally would not appear for the requested library type. The value for this key is an array of strings (media source identifiers). For a list of valid media source identifiers, see [Media Source Identifiers](/documentation/MediaLibrary/media-source-identifiers).

[`MLMediaLoadMoviesFolder`](/documentation/MediaLibrary/MLMediaLoadMoviesFolder)

Identifies the user’s Movies folder.

[`MLMediaLoadSourceTypesKey`](/documentation/MediaLibrary/MLMediaLoadSourceTypesKey)

Defines which sources to load based on library type. If not present, this will load all sources. The value for this key is a media source type. For a list of valid media source types, see [`MLMediaSourceType`](/documentation/MediaLibrary/MLMediaSourceType).

[`MLMediaSourceApertureIdentifier`](/documentation/MediaLibrary/MLMediaSourceApertureIdentifier)

The media source providing content from Aperture.

[`MLMediaSourceAppDefinedFoldersIdentifier`](/documentation/MediaLibrary/MLMediaSourceAppDefinedFoldersIdentifier)

The media source for app-defined folders. This identifies a media source created from a relative path inside the caller’s app bundle. This source provides data when [`MLMediaLoadAppFoldersKey`](/documentation/MediaLibrary/MLMediaLoadAppFoldersKey) is provided in the options.

[`MLMediaSourceCustomFoldersIdentifier`](/documentation/MediaLibrary/MLMediaSourceCustomFoldersIdentifier)

The media source for custom folders. Currently, the only custom folder is the folder containing audio loops from Apple. This source provides data when [`MLMediaLoadFoldersKey`](/documentation/MediaLibrary/MLMediaLoadFoldersKey) is provided with the [`MLMediaLoadAppleLoops`](/documentation/MediaLibrary/MLMediaLoadAppleLoops) value.

[`MLMediaSourceFinalCutIdentifier`](/documentation/MediaLibrary/MLMediaSourceFinalCutIdentifier)

The media source providing content from Final Cut Pro.

[`MLMediaSourceGarageBandIdentifier`](/documentation/MediaLibrary/MLMediaSourceGarageBandIdentifier)

The media source providing content from GarageBand.

[`MLMediaSourceLogicIdentifier`](/documentation/MediaLibrary/MLMediaSourceLogicIdentifier)

The media source providing content from Logic.

[`MLMediaSourceMoviesFolderIdentifier`](/documentation/MediaLibrary/MLMediaSourceMoviesFolderIdentifier)

The media source for the user’s Movies folder. This source provides data when [`MLMediaLoadFoldersKey`](/documentation/MediaLibrary/MLMediaLoadFoldersKey) is provided with the [`MLMediaLoadMoviesFolder`](/documentation/MediaLibrary/MLMediaLoadMoviesFolder) value.

[`MLMediaSourcePhotoBoothIdentifier`](/documentation/MediaLibrary/MLMediaSourcePhotoBoothIdentifier)

The media source providing content from Photo Booth.

[`MLMediaSourcePhotosIdentifier`](/documentation/MediaLibrary/MLMediaSourcePhotosIdentifier)

[`MLMediaSourceType`](/documentation/MediaLibrary/MLMediaSourceType)

Specifies the source type associated with a particular media source. Source type reflects the primary type of media within the source. These constants are used to specify values for [`MLMediaLoadSourceTypesKey`](/documentation/MediaLibrary/MLMediaLoadSourceTypesKey) in the [`init(options:)`](/documentation/MediaLibrary/MLMediaLibrary/init(options:)) method of [`MLMediaLibrary`](/documentation/MediaLibrary/MLMediaLibrary).

[`MLMediaSourceiMovieIdentifier`](/documentation/MediaLibrary/MLMediaSourceiMovieIdentifier)

The media source providing content from iMovie.

[`MLMediaSourceiPhotoIdentifier`](/documentation/MediaLibrary/MLMediaSourceiPhotoIdentifier)

The media source providing content from iPhoto.

[`MLMediaSourceiTunesIdentifier`](/documentation/MediaLibrary/MLMediaSourceiTunesIdentifier)

The media source providing content from iTunes.

[`MLMediaType`](/documentation/MediaLibrary/MLMediaType)

Specifies the media type associated with a particular media object. These constants are used to specify a media object’s [`mediaType`](/documentation/MediaLibrary/MLMediaObject/mediaType) attribute.

[`MLPhotosAlbumTypeIdentifier`](/documentation/MediaLibrary/MLPhotosAlbumTypeIdentifier)

[`MLPhotosAlbumsGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosAlbumsGroupTypeIdentifier)

[`MLPhotosAllCollectionsGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosAllCollectionsGroupTypeIdentifier)

[`MLPhotosAllMomentsGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosAllMomentsGroupTypeIdentifier)

[`MLPhotosAllPhotosAlbumTypeIdentifier`](/documentation/MediaLibrary/MLPhotosAllPhotosAlbumTypeIdentifier)

[`MLPhotosAllYearsGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosAllYearsGroupTypeIdentifier)

[`MLPhotosBurstGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosBurstGroupTypeIdentifier)

[`MLPhotosCollectionGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosCollectionGroupTypeIdentifier)

[`MLPhotosDepthEffectGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosDepthEffectGroupTypeIdentifier)

[`MLPhotosFacesAlbumTypeIdentifier`](/documentation/MediaLibrary/MLPhotosFacesAlbumTypeIdentifier)

[`MLPhotosFavoritesGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosFavoritesGroupTypeIdentifier)

[`MLPhotosFolderTypeIdentifier`](/documentation/MediaLibrary/MLPhotosFolderTypeIdentifier)

[`MLPhotosFrontCameraGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosFrontCameraGroupTypeIdentifier)

[`MLPhotosLastImportGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosLastImportGroupTypeIdentifier)

[`MLPhotosMomentGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosMomentGroupTypeIdentifier)

[`MLPhotosMyPhotoStreamTypeIdentifier`](/documentation/MediaLibrary/MLPhotosMyPhotoStreamTypeIdentifier)

[`MLPhotosPanoramasGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosPanoramasGroupTypeIdentifier)

[`MLPhotosPublishedAlbumTypeIdentifier`](/documentation/MediaLibrary/MLPhotosPublishedAlbumTypeIdentifier)

[`MLPhotosRootGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosRootGroupTypeIdentifier)

[`MLPhotosScreenshotGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosScreenshotGroupTypeIdentifier)

[`MLPhotosSharedGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosSharedGroupTypeIdentifier)

[`MLPhotosSharedPhotoStreamTypeIdentifier`](/documentation/MediaLibrary/MLPhotosSharedPhotoStreamTypeIdentifier)

[`MLPhotosSloMoGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosSloMoGroupTypeIdentifier)

[`MLPhotosSmartAlbumTypeIdentifier`](/documentation/MediaLibrary/MLPhotosSmartAlbumTypeIdentifier)

[`MLPhotosTimelapseGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosTimelapseGroupTypeIdentifier)

[`MLPhotosVideosGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosVideosGroupTypeIdentifier)

[`MLPhotosYearGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosYearGroupTypeIdentifier)

[`MLiTunesMusicVideosPlaylistTypeIdentifier`](/documentation/MediaLibrary/MLiTunesMusicVideosPlaylistTypeIdentifier)

[`MLiTunesVideoPlaylistTypeIdentifier`](/documentation/MediaLibrary/MLiTunesVideoPlaylistTypeIdentifier)

[Media Object Attribute Keys](/documentation/MediaLibrary/media-object-attribute-keys)

Attribute keys for a media object. These constants are used to specify keys within a media object’s [`attributes`](/documentation/MediaLibrary/MLMediaObject/attributes) dictionary.

[iMovie Media Group Type Identifiers](/documentation/MediaLibrary/imovie-media-group-type-identifiers)

Identifiers for media group types in the iMovie media source. These constants are used to specify a media group’s [`typeIdentifier`](/documentation/MediaLibrary/MLMediaGroup/typeIdentifier) attribute.

[iPhoto Media Group Type Identifiers](/documentation/MediaLibrary/iphoto-media-group-type-identifiers)

Identifiers for media group types in the iPhoto media source. These constants are used to specify a media group’s [`typeIdentifier`](/documentation/MediaLibrary/MLMediaGroup/typeIdentifier) attribute.

[iTunes Media Group Type Identifiers](/documentation/MediaLibrary/itunes-media-group-type-identifiers)

Identifiers for media group types in the iTunes media source. These constants are used to specify a media group’s [`typeIdentifier`](/documentation/MediaLibrary/MLMediaGroup/typeIdentifier) attribute.

[`MLPhotosAnimatedGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosAnimatedGroupTypeIdentifier)

[`MLPhotosLivePhotosGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosLivePhotosGroupTypeIdentifier)

[`MLPhotosLongExposureGroupTypeIdentifier`](/documentation/MediaLibrary/MLPhotosLongExposureGroupTypeIdentifier)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
