* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/photosui#app-main)

Framework

# PhotosUI

Present a person’s photo library using a picker interface, display Live Photos, or extend the Photos app with custom functionality.

iOS 8.0+iPadOS 8.0+Mac Catalyst 13.1+macOS 10.11+tvOS 10.0+visionOS 1.0+watchOS 9.0+

## [Overview](https://developer.apple.com/documentation/photosui\#overview)

PhotosUI offers a photo picker that lets people view their library and choose one or more photos for your app to display or process. The picker renders in a system view and only gives your app access to the photos someone chooses, which facilitates a user experience with enhanced privacy.

The framework also provides a view you can use to display Live Photos.

## [Topics](https://developer.apple.com/documentation/photosui\#topics)

### [Shared photo library](https://developer.apple.com/documentation/photosui\#Shared-photo-library)

[Delivering an Enhanced Privacy Experience in Your Photos App](https://developer.apple.com/documentation/photokit/delivering-an-enhanced-privacy-experience-in-your-photos-app)

Adopt the latest privacy enhancements to deliver advanced user-privacy controls.

[`class PHLivePhotoView`](https://developer.apple.com/documentation/photosui/phlivephotoview)

A view that displays a Live Photo.

### [Photos picker for UIKit, AppKit](https://developer.apple.com/documentation/photosui\#Photos-picker-for-UIKit-AppKit)

[Selecting Photos and Videos in iOS](https://developer.apple.com/documentation/photokit/selecting-photos-and-videos-in-ios)

Improve the user experience of finding and selecting assets by using the Photos picker.

[`class PHPickerViewController`](https://developer.apple.com/documentation/photosui/phpickerviewcontroller)

A view controller that provides the user interface for choosing assets from the photo library.

[`protocol PHPickerViewControllerDelegate`](https://developer.apple.com/documentation/photosui/phpickerviewcontrollerdelegate-5yntc)

A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.

[`struct PHPickerConfiguration`](https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct)

An object that contains information about how to configure a picker view controller.

[`struct PHPickerFilter`](https://developer.apple.com/documentation/photosui/phpickerfilter-swift.struct)

A type that defines the filter to apply to the photo library.

[`struct PHPickerResult`](https://developer.apple.com/documentation/photosui/phpickerresult-swift.struct)

Types that represent a selected asset from a person’s photo library.

### [Photos picker for SwiftUI](https://developer.apple.com/documentation/photosui\#Photos-picker-for-SwiftUI)

[Bringing Photos picker to your SwiftUI app](https://developer.apple.com/documentation/photokit/bringing-photos-picker-to-your-swiftui-app)

Select media assets by using a Photos picker view that SwiftUI provides.

[Implementing an inline Photos picker](https://developer.apple.com/documentation/photokit/implementing-an-inline-photos-picker)

Embed a system-provided, half-height Photos picker into your app’s view.

[`struct PhotosPicker`](https://developer.apple.com/documentation/photosui/photospicker)

A view that displays a Photos picker for choosing assets from the photo library.

[`struct PhotosPickerItem`](https://developer.apple.com/documentation/photosui/photospickeritem)

A type that represents an item you use with a Photos picker.

[`struct PhotosPickerSelectionBehavior`](https://developer.apple.com/documentation/photosui/photospickerselectionbehavior)

A type that describes how the Photos picker handles user selection.

[`struct PhotosPickerStyle`](https://developer.apple.com/documentation/photosui/photospickerstyle)

### [Live Photos](https://developer.apple.com/documentation/photosui\#Live-Photos)

[Displaying Live Photos](https://developer.apple.com/documentation/photokit/displaying-live-photos)

Provide the same interactive playback of Live Photos as in the iOS Photos app.

### [Photo editing extensions](https://developer.apple.com/documentation/photosui\#Photo-editing-extensions)

[Creating Photo Editing Extensions](https://developer.apple.com/documentation/photokit/creating-photo-editing-extensions)

Provide custom functionality in the Photos app by bundling an app extension.

[`protocol PHContentEditingController`](https://developer.apple.com/documentation/photosui/phcontenteditingcontroller)

A protocol your custom view controller class implements to provide a user interface for your Photos extension.

### [macOS Photos project extensions](https://developer.apple.com/documentation/photosui\#macOS-Photos-project-extensions)

[Creating a Slideshow Project Extension for Photos](https://developer.apple.com/documentation/photokit/creating-a-slideshow-project-extension-for-photos)

Augment the macOS Photos app with extensions that support project creation.

[`class PHProject`](https://developer.apple.com/documentation/photos/phproject)

A representation of a Photos app project extension.

[`class PHProjectInfo`](https://developer.apple.com/documentation/photosui/phprojectinfo)

Information about the project extension.

[`class PHProjectExtensionContext`](https://developer.apple.com/documentation/photosui/phprojectextensioncontext)

An object that provides Photos project extensions with access to the underlying project, as well as to the user’s photo library for editing.

[`class PHProjectElement`](https://developer.apple.com/documentation/photosui/phprojectelement)

The superclass for all element objects.

[`class PHProjectSection`](https://developer.apple.com/documentation/photosui/phprojectsection)

A collection of content representing curated asset and text elements.

[`class PHProjectRegionOfInterest`](https://developer.apple.com/documentation/photosui/phprojectregionofinterest)

A representation of a region of interest in a photo asset.

[`class PHProjectChangeRequest`](https://developer.apple.com/documentation/photos/phprojectchangerequest)

A request to change asset data in a Photos project extension.

[`protocol PHProjectExtensionController`](https://developer.apple.com/documentation/photosui/phprojectextensioncontroller)

A protocol defining the life cycle and supported types of project extensions.

[`struct PHProjectCategory`](https://developer.apple.com/documentation/photosui/phprojectcategory)

A representation of Photos project extension categories.

### [Classes](https://developer.apple.com/documentation/photosui\#Classes)

[`class PHSharedAlbumCreationViewController`](https://developer.apple.com/documentation/photosui/phsharedalbumcreationviewcontroller) Beta

[`class PHSharedAlbumCustomizationViewController`](https://developer.apple.com/documentation/photosui/phsharedalbumcustomizationviewcontroller) Beta

[`class PHSharedAlbumPostingViewController`](https://developer.apple.com/documentation/photosui/phsharedalbumpostingviewcontroller) Beta

### [Structures](https://developer.apple.com/documentation/photosui\#Structures)

[`struct PHPickerMetadataOptions`](https://developer.apple.com/documentation/photosui/phpickermetadataoptions)

Constants that specify metadata options for \\c PHPickerViewController.

Beta

[`struct PHPickerSearchText`](https://developer.apple.com/documentation/photosui/phpickersearchtext-swift.struct)

A search text for `PHPickerViewController`.

[`struct PHSharedAlbumCreationConfiguration`](https://developer.apple.com/documentation/photosui/phsharedalbumcreationconfiguration-swift.struct)

An object used to configure a `PHSharedAlbumCreationViewController`.

[`struct PHSharedAlbumCreationResult`](https://developer.apple.com/documentation/photosui/phsharedalbumcreationresult-swift.struct)

The result of a user creating a shared album.

### [Enumerations](https://developer.apple.com/documentation/photosui\#Enumerations)

[`enum PHSharedAlbumCreationSharingPolicy`](https://developer.apple.com/documentation/photosui/phsharedalbumcreationsharingpolicy)

The sharing policy for creating shared albums.

Beta

## [See Also](https://developer.apple.com/documentation/photosui\#see-also)

### [Frameworks](https://developer.apple.com/documentation/photosui\#Frameworks)

[Photos](https://developer.apple.com/documentation/photos)

Work with image and video assets that the Photos app manages, including those from iCloud Photos and Live Photos.

Current page is PhotosUI