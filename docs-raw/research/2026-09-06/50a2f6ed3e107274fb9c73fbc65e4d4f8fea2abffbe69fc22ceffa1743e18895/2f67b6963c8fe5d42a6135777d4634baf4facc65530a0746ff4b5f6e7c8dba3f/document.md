# Current Place

Using the Places SDK for iOS, you can discover the place where the
device is currently located. That is, the place at the device's
currently-reported location. Examples of places include local businesses,
points of interest, and geographic locations.

1. [Request location authorization](https://developers.google.com/maps/documentation/places/ios-sdk/current-place#permissions)
2. [Usage limits](https://developers.google.com/maps/documentation/places/ios-sdk/current-place#quota)
3. [Get the current location](https://developers.google.com/maps/documentation/places/ios-sdk/current-place#get-current)
4. [Display attributions in your app](https://developers.google.com/maps/documentation/places/ios-sdk/current-place#attributions)

## Requesting location authorization

If your app uses
[`GMSPlacesClient findPlaceLikelihoodsFromCurrentLocationWithPlaceFields:`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacesClient#-findplacelikelihoodsfromcurrentlocationwithplacefields:callback:),
your app must request permission to use location services. Add the
`NSLocationWhenInUseUsageDescription` key to your `Info.plist`
file, to define the string informing the user why you need the location
services. For example:

```
<key>NSLocationWhenInUseUsageDescription</key>
<string>Show your location on the map</string>
```

If you want to call
[`findPlaceLikelihoodsFromCurrentLocationWithPlaceFields:`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacesClient#-findplacelikelihoodsfromcurrentlocationwithplacefields:callback:) when
the app is in the background, without triggering a confirmation dialog, take
the following steps prior to making the call:

1. Add the `NSLocationAlwaysUsageDescription` key to your `Info.plist`file.
2. Call `requestAlwaysAuthorization` on any instance of `CLLocationManager`
   before calling the method.

Request authorization from `CLLocationManager` as follows:

### Swift

```
    locationManager.requestAlwaysAuthorization()
```

### Objective-C

```
    [self.locationManager requestAlwaysAuthorization];
```

## Getting the current location

**Note:** iOS 14 introduced a new privacy feature where users can
choose to share their approximate, rather than precise, location. Check your app's value of
`accuracyAuthorization`
in `CLLocationManager` so your app behaves appropriately.
[See this video for more information.](https://developer.apple.com/videos/play/wwdc2020/10162/)

To find the local business or other place where the device is currently
located, call
[`GMSPlacesClient
findPlaceLikelihoodsFromCurrentLocationWithPlaceFields:`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacesClient#-findplacelikelihoodsfromcurrentlocationwithplacefields:callback:). Include
the following parameters:

* One or more `GMSPlaceField`s, specifying which data types
  to return. If you omit this parameter, ALL possible fields will be returned, and
  you will be billed accordingly. This applies only to Place Details requests.
* A callback method to handle the results.

**IMPORTANT!**
`findPlaceLikelihoodsFromCurrentLocationWithPlaceFields:`
does not support the following fields: `GMSPlaceFieldAddressComponents`,
`GMSPlaceFieldOpeningHours`, `GMSPlaceFieldPhoneNumber`,
and `GMSPlaceFieldWebsite`. Read more about
[place data fields](https://developers.google.com/maps/documentation/places/ios-sdk/place-data-fields)

Fields correspond to Place Search results, and are divided into three billing categories:
Basic, Contact, and Atmosphere. Basic fields are billed at base rate, and incur no additional
charges. Contact and Atmosphere fields are billed at a higher rate. For more information
about how Place data requests are billed, see
[Usage and Billing](https://developers.google.com/maps/documentation/places/ios-sdk/usage-and-billing).

The API invokes the specified callback method, returning an array of
[`GMSPlaceLikelihood`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlaceLikelihood)
objects.

Each
[`GMSPlaceLikelihood`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlaceLikelihood)
object represents a place. For each place, the result includes an
indication of the likelihood that the place is the right one. A higher value
means a greater probability that the place is the best match. The buffer may
be empty, if there is no known place corresponding to the device location.

The following code sample retrieves the list of places where the device is
most likely to be located, and logs the name and likelihood for each place.

### Swift

```
// Specify the place data types to return.
let fields: GMSPlaceField = GMSPlaceField(rawValue: UInt(GMSPlaceField.name.rawValue) |
                                          UInt(GMSPlaceField.placeID.rawValue))!
placesClient?.findPlaceLikelihoodsFromCurrentLocation(withPlaceFields: fields, callback: {
  (placeLikelihoodList: Array<GMSPlaceLikelihood>?, error: Error?) in
  if let error = error {
    print("An error occurred: \(error.localizedDescription)")
    return
  }

  if let placeLikelihoodList = placeLikelihoodList {
    for likelihood in placeLikelihoodList {
      let place = likelihood.place
      print("Current Place name \(String(describing: place.name)) at likelihood \(likelihood.likelihood)")
      print("Current PlaceID \(String(describing: place.placeID))")
    }
  }
})
```

### Objective-C

```
// Specify the place data types to return.
GMSPlaceField fields = (GMSPlaceFieldName | GMSPlaceFieldPlaceID);
[_placesClient findPlaceLikelihoodsFromCurrentLocationWithPlaceFields:fields callback:^(NSArray<GMSPlaceLikelihood *> * _Nullable likelihoods, NSError * _Nullable error) {
  if (error != nil) {
    NSLog(@"An error occurred %@", [error localizedDescription]);
    return;
  }
  if (likelihoods != nil) {
    for (GMSPlaceLikelihood *likelihood in likelihoods) {
      GMSPlace *place = likelihood.place;
      NSLog(@"Current place name: %@", place.name);
      NSLog(@"Place ID: %@", place.placeID);
    }
  }
}];
```

Notes about the likelihood values:

* The likelihood provides a relative probability
  of the place being the best match within the list of returned places for a
  single request. You can't compare likelihoods across different requests.
* The value of the likelihood will be between 0 and 1.0.
* The sum of the likelihoods in a returned array of
  [`GMSPlaceLikelihood`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlaceLikelihood)
  objects is always less than or equal to 1.0. Note that the sum isn't
  necessarily 1.0.

For example, to represent a 55% likelihood that the correct place is Place A,
and a 35% likelihood that it's Place B, the likelihood array has two members:
Place A with a likelihood of 0.55 and
Place B with a likelihood of 0.35.

## Displaying attributions in your app

When your app displays information obtained from
[`GMSPlacesClient
findPlaceLikelihoodsFromCurrentLocationWithPlaceFields:`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacesClient#-findplacelikelihoodsfromcurrentlocationwithplacefields:callback:), the app
must also display attributions. Read more about
[attributions](https://developers.google.com/maps/documentation/places/ios-sdk/attributions).
