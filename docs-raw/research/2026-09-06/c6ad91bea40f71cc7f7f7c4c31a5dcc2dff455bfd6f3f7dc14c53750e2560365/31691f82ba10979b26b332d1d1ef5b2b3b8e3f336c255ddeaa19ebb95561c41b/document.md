# Place Photos

You can use the Places SDK for iOS to request place photos to display in
your application. Photos returned by the photos service come from a variety of
sources, including business owners and user-contributed photos. To retrieve
photos for a place, you must take the following steps:

1. Call [`[GMSPlacesClient
   fetchPlaceFromPlaceId]`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacesClient#-fetchplacefromplaceid:placefields:sessiontoken:callback:),
   passing a string with a place ID and a callback. This will call the callback
   with a
   [`GMSPlacePhotoMetadataList`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacePhotoMetadataList)
   object.
2. On the [`GMSPlacePhotoMetadataList`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacePhotoMetadataList)
   object access the
   [`results`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacePhotoMetadataList#results)
   property and select the photos to load from the array.
3. For each [`GMSPlacePhotoMetadata`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacePhotoMetadata)
   to load from this list call [`[GMSPlacesClient
   loadPlacePhoto:callback:]`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacesClient#-loadplacephoto:callback:)
   or [`[GMSPlacesClient
   loadPlacePhoto:constrainedToSize:scale:callback:]`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacesClient#-loadplacephoto:constrainedtosize:scale:callback:).
   These will call the callback with a usable UIImage. Photos can have a
   maximum width or height of 1600 pixels.

**Note:** Whenever you display a place photo, make sure to follow the attribution
guidelines. See [Attributions](https://developers.google.com/maps/documentation/places/ios-sdk/photos#attributions) for more information.


## Sample code

The following example method takes a place ID and gets the first photo in the
returned list. You can use this method as a template for the method you will
create in your own app.

### Swift

```
// Specify the place data types to return (in this case, just photos).
let fields: GMSPlaceField = GMSPlaceField(rawValue: UInt(GMSPlaceField.photos.rawValue))!

placesClient?.fetchPlace(fromPlaceID: "INSERT_PLACE_ID_HERE",
                         placeFields: fields,
                         sessionToken: nil, callback: {
  (place: GMSPlace?, error: Error?) in
  if let error = error {
    print("An error occurred: \(error.localizedDescription)")
    return
  }
  if let place = place {
    // Get the metadata for the first photo in the place photo metadata list.
    let photoMetadata: GMSPlacePhotoMetadata = place.photos![0]

    // Call loadPlacePhoto to display the bitmap and attribution.
    self.placesClient?.loadPlacePhoto(photoMetadata, callback: { (photo, error) -> Void in
      if let error = error {
        // TODO: Handle the error.
        print("Error loading photo metadata: \(error.localizedDescription)")
        return
      } else {
        // Display the first image and its attributions.
        self.imageView?.image = photo;
        self.lblText?.attributedText = photoMetadata.attributions;
      }
    })
  }
})
```

### Objective-C

```
// Specify the place data types to return (in this case, just photos).
GMSPlaceField fields = (GMSPlaceFieldPhotos);

NSString *placeId = @"INSERT_PLACE_ID_HERE";

[_placesClient fetchPlaceFromPlaceID:placeId placeFields:fields sessionToken:nil callback:^(GMSPlace * _Nullable place, NSError * _Nullable error) {
  if (error != nil) {
    NSLog(@"An error occurred %@", [error localizedDescription]);
    return;
  }
  if (place != nil) {
    GMSPlacePhotoMetadata *photoMetadata = [place photos][0];
    [self->_placesClient loadPlacePhoto:photoMetadata callback:^(UIImage * _Nullable photo, NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Error loading photo metadata: %@", [error localizedDescription]);
        return;
      } else {
        // Display the first image and its attributions.
        self->imageView.image = photo;
        self->lblText.attributedText = photoMetadata.attributions;
      }
    }];
  }
}];
```

## Caching

Photos loaded using [`[GMSPlacesClient loadPlacePhoto:callback:]`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacesClient#-loadplacephoto:callback:)
or [`[GMSPlacesClient loadPlacePhoto:constrainedToSize:scale:callback:]`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacesClient#-loadplacephoto:constrainedtosize:scale:callback:)
are cached both on disk and in-memory by the [Foundation URL loading system](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/URLLoadingSystem/URLLoadingSystem.html)
in the shared [`NSURLCache`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSURLCache_Class/index.html).

To configure the caching behavior you can change the shared URL cache using
[`[NSURLCache setSharedURLCache:]`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSURLCache_Class/index.html#//apple_ref/occ/clm/NSURLCache/setSharedURLCache:)
in your application delegate's `application:didFinishLaunchingWithOptions:`
method.

If you don't want your application to share a `NSURLCache` with the
Places SDK for iOS you can create a new `NSURLCache` and use this
exclusively within your app without setting it as the shared cache.

## Attributions

In most cases, place photos can be used without attribution, or will have the
required attribution included as part of the image. However, if the returned
[`GMSPlacePhotoMetadata`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacePhotoMetadata)
instance includes an attribution, you must include the additional attribution
in your application wherever you display the image. Note that links in the
attribution must be tappable. See the documentation on [attributions](https://developers.google.com/maps/documentation/places/ios-sdk/attributions).

## Usage limits

Retrieving an image costs one unit of quota; there are no usage limits for
retrieving photo metadata. Read more about
[usage and billing](https://developers.google.com/maps/documentation/places/ios-sdk/usage-and-billing).
