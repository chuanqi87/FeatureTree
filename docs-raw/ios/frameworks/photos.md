* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/photos#app-main)

Framework

# Photos

Work with image and video assets that the Photos app manages, including those from iCloud Photos and Live Photos.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.11+tvOS 10.0+visionOS 1.0+

## [Overview](https://developer.apple.com/documentation/photos\#overview)

Use PhotoKit to access image and video assets that the Photos app manages in iOS, macOS, tvOS, and visionOS. You might use this framework to edit or display a person’s photos, or to manage collections of assets such as albums, Moments, and Shared Albums. The framework provides access to photos on the person’s device and in iCloud.

## [Topics](https://developer.apple.com/documentation/photos\#topics)

### [Shared photo library](https://developer.apple.com/documentation/photos\#Shared-photo-library)

[`class PHPhotoLibrary`](https://developer.apple.com/documentation/photos/phphotolibrary)

An object that manages access and changes to a person’s photo library.

### [Asset retrieval](https://developer.apple.com/documentation/photos\#Asset-retrieval)

[Fetching Objects and Requesting Changes](https://developer.apple.com/documentation/photokit/fetching-objects-and-requesting-changes)

Get assets, asset collections, and collection lists matching a specified query.

[`class PHAsset`](https://developer.apple.com/documentation/photos/phasset)

A representation of an image, video, or Live Photo in the Photos library.

[`class PHAssetCollection`](https://developer.apple.com/documentation/photos/phassetcollection)

A representation of a Photos asset grouping, such as Moments, a user-created album, or a Smart Album.

[`class PHCollection`](https://developer.apple.com/documentation/photos/phcollection)

The abstract superclass for Photos asset collections and collection lists.

[`class PHCollectionList`](https://developer.apple.com/documentation/photos/phcollectionlist)

A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.

[`class PHObject`](https://developer.apple.com/documentation/photos/phobject)

The abstract superclass for Photos model objects, including assets and collections.

[`class PHFetchResult`](https://developer.apple.com/documentation/photos/phfetchresult)

An ordered list of assets or collections returned from a Photos fetch method.

[`class PHFetchOptions`](https://developer.apple.com/documentation/photos/phfetchoptions)

A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.

### [Asset loading](https://developer.apple.com/documentation/photos\#Asset-loading)

[Loading and Caching Assets and Thumbnails](https://developer.apple.com/documentation/photokit/loading-and-caching-assets-and-thumbnails)

Request image, video, or Live Photos content, and cache for quick reuse.

[`class PHImageManager`](https://developer.apple.com/documentation/photos/phimagemanager)

An object that facilitates retrieving or generating preview thumbnails and asset data.

[`class PHCachingImageManager`](https://developer.apple.com/documentation/photos/phcachingimagemanager)

An object that facilitates retrieving or generating preview thumbnails, optimized for batch preloading large numbers of assets.

[`class PHImageRequestOptions`](https://developer.apple.com/documentation/photos/phimagerequestoptions)

A set of options affecting the delivery of still image representations of Photos assets you request from an image manager.

[`class PHVideoRequestOptions`](https://developer.apple.com/documentation/photos/phvideorequestoptions)

A set of options affecting the delivery of video asset data that you request from an image manager.

[`class PHLivePhotoRequestOptions`](https://developer.apple.com/documentation/photos/phlivephotorequestoptions)

A set of options affecting the delivery of Live Photo assets you request from an image manager.

### [Asset metadata](https://developer.apple.com/documentation/photos\#Asset-metadata)

[`class PHAssetExtendedMetadata`](https://developer.apple.com/documentation/photos/phassetextendedmetadata)

Represents other asset attributes that are not included when fetching `PHAsset` directly.

Beta

### [Asset resource management](https://developer.apple.com/documentation/photos\#Asset-resource-management)

[`class PHAssetResource`](https://developer.apple.com/documentation/photos/phassetresource)

An underlying data resource associated with a photo, video, or Live Photo asset in the Photos library.

[`class PHAssetCreationRequest`](https://developer.apple.com/documentation/photos/phassetcreationrequest)

A request to create a new Photos asset from underlying data resources, for use in a photo library change block.

[`class PHAssetResourceCreationOptions`](https://developer.apple.com/documentation/photos/phassetresourcecreationoptions)

A set of options affecting the creation of a new Photos asset from underlying resources.

[`class PHAssetResourceManager`](https://developer.apple.com/documentation/photos/phassetresourcemanager)

A resource manager for the data storage underlying a Photos asset.

[`class PHAssetResourceRequestOptions`](https://developer.apple.com/documentation/photos/phassetresourcerequestoptions)

A set of options affecting the delivery of underlying asset data that you request from the asset-resource manager.

### [Background resource upload extensions](https://developer.apple.com/documentation/photos\#Background-resource-upload-extensions)

[Uploading asset resources in the background](https://developer.apple.com/documentation/photokit/uploading-asset-resources-in-the-background)

Enable reliable cloud backup for photo library assets with background processing.

[`protocol PHBackgroundResourceUploadExtension`](https://developer.apple.com/documentation/photos/phbackgroundresourceuploadextension) Deprecated

[`class PHAssetResourceUploadJob`](https://developer.apple.com/documentation/photos/phassetresourceuploadjob)

An object that represents a request to upload an asset resource.

[`class PHAssetResourceUploadJobChangeRequest`](https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest)

Use within an application’s `com.apple.photos.background-upload` extension to create and change [`PHAssetResourceUploadJob`](https://developer.apple.com/documentation/photos/phassetresourceuploadjob) records.

### [Live Photos](https://developer.apple.com/documentation/photos\#Live-Photos)

[`class PHLivePhoto`](https://developer.apple.com/documentation/photos/phlivephoto)

A displayable representation of a Live Photo.

### [Errors](https://developer.apple.com/documentation/photos\#Errors)

[`struct PHPhotosError`](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct)

A structure that represents a framework error.

[`let PHPhotosErrorDomain: String`](https://developer.apple.com/documentation/photos/phphotoserrordomain)

A string representation of the error domain.

### [Deprecated errors](https://developer.apple.com/documentation/photos\#Deprecated-errors)

[API Reference\\
Deprecated Errors](https://developer.apple.com/documentation/photokit/deprecated-errors)

Review unsupported errors and their replacements.

### [Classes](https://developer.apple.com/documentation/photos\#Classes)

[`class PHProject`](https://developer.apple.com/documentation/photos/phproject)

A representation of a Photos app project extension.

[`class PHProjectChangeRequest`](https://developer.apple.com/documentation/photos/phprojectchangerequest)

A request to change asset data in a Photos project extension.

[`class PHAssetResourceUploadJobOptions`](https://developer.apple.com/documentation/photos/phassetresourceuploadjoboptions)

Options that affect the service behavior when processing Asset Resource Upload Jobs.

Beta

### [Protocols](https://developer.apple.com/documentation/photos\#Protocols)

[`protocol PHBackgroundResourceUploadJobExtension`](https://developer.apple.com/documentation/photos/phbackgroundresourceuploadjobextension) Beta

[`protocol PHPhotoLibraryPersistentChangesObserver`](https://developer.apple.com/documentation/photos/phphotolibrarypersistentchangesobserver) Beta

## [See Also](https://developer.apple.com/documentation/photos\#see-also)

### [Frameworks](https://developer.apple.com/documentation/photos\#Frameworks)

[PhotosUI](https://developer.apple.com/documentation/photosui)

Present a person’s photo library using a picker interface, display Live Photos, or extend the Photos app with custom functionality.

Current page is Photos