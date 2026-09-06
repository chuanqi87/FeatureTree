# PHPickerConfiguration

An object that contains information about how to configure a picker view controller.

```
@interface PHPickerConfiguration : NSObject
```

## Topics

### Creating a configuration

[`-  init`](/documentation/PhotosUI/PHPickerConfiguration-c.class/init)

Creates a new configuration object.

[`-  initWithPhotoLibrary:`](/documentation/PhotosUI/PHPickerConfiguration-c.class/initWithPhotoLibrary:)

Creates a new configuration object for a photo library.

### Filtering asset types

[`filter`](/documentation/PhotosUI/PHPickerConfiguration-c.class/filter)

The filter you apply to restrict the asset types the picker displays.

[`PHPickerFilter`](/documentation/PhotosUI/PHPickerFilter-c.class)

A type that defines the filter to apply to the photo library.

### Selecting the preferred asset representation

[`preferredAssetRepresentationMode`](/documentation/PhotosUI/PHPickerConfiguration-c.class/preferredAssetRepresentationMode)

A mode that determines which representation to use if an asset contains more than one.

[`PHPickerConfigurationAssetRepresentationMode`](/documentation/PhotosUI/PHPickerConfigurationAssetRepresentationMode)

Constants identifying the mode the system uses when many representations exist for an asset.

### Preselecting assets

[`preselectedAssetIdentifiers`](/documentation/PhotosUI/PHPickerConfiguration-c.class/preselectedAssetIdentifiers)

An array of asset identifiers to preselect in the picker.

### Setting the selection limit

[`selectionLimit`](/documentation/PhotosUI/PHPickerConfiguration-c.class/selectionLimit)

The maximum number of selections the user can make.

[`selection`](/documentation/PhotosUI/PHPickerConfiguration-c.class/selection)

The selection behavior for the picker.

[`PHPickerConfigurationSelection`](/documentation/PhotosUI/PHPickerConfigurationSelection)

Options that represent differing selection behavior.

### Customizing picker appearance and behavior

[`mode`](/documentation/PhotosUI/PHPickerConfiguration-c.class/mode)

A layout type for the photos in the picker’s view.

[`PHPickerMode`](/documentation/PhotosUI/PHPickerMode-c.enum)

Layout options that determine how the picker orders photos visually.

[`disabledCapabilities`](/documentation/PhotosUI/PHPickerConfiguration-c.class/disabledCapabilities)

The aspects of a photo picker’s default appearance that your app can disable.

[`PHPickerCapabilities`](/documentation/PhotosUI/PHPickerCapabilities)

Options that customize the look and behavior of the photos picker.

[`edgesWithoutContentMargins`](/documentation/PhotosUI/PHPickerConfiguration-c.class/edgesWithoutContentMargins)

The portions of a photo picker’s perimeter that are borderless.

[`PHPickerUpdateConfiguration`](/documentation/PhotosUI/PHPickerUpdateConfiguration)

An object that defines the aspects of a photo picker’s appearance that can change while it’s presented.

## Relationships

### Inherits From

[`NSObject-swift.class`](/documentation/ObjectiveC/NSObject-swift.class)

### Conforms To

[`NSCopying`](/documentation/Foundation/NSCopying)

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
