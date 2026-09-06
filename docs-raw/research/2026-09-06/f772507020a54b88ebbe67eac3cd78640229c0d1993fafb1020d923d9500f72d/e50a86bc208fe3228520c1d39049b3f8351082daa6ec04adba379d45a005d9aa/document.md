# Policies and attributions for Places SDK for iOS

This document lists requirements that are specific to all applications
developed with the Places SDK for iOS, including the Place Autocomplete
service that is part of that API. More general information for Google Maps
developers may be found in the
[Google Maps Platform Terms of Service](https://cloud.google.com/maps-platform/terms/).

## Policies

This section describes policies relevant to Places SDK for iOS. Policies provide practical
implementation guidelines and requirements to help you use the Service
correctly and in line with Google Maps Platform's expectations.

### Exceptions from caching restrictions

Note that the **place ID**, used to uniquely identify a place, is
**exempt from** the [caching restrictions](https://cloud.google.com/maps-platform/terms/maps-service-terms).
You can therefore store place ID values indefinitely.
The place ID is returned in the `place_id` field in
API responses. Learn how to save, refresh, and manage place IDs in the [Place IDs guide](https://developers.google.com/maps/documentation/places/web-service/place-id#save-id).

### European Economic Area countries and territories

This product has different Terms of Service for customers with a billing address in the
European Economic Area (EEA), and it may also have different functionality.
Before building with Google Maps Platform, review the following EEA-specific
terms and information:

* [Google Maps Platform EEA Terms of Service](https://cloud.google.com/terms/maps-platform/eea)
* [Google Maps Platform EEA Service Specific Terms](https://cloud.google.com/terms/maps-platform/eea/maps-service-terms)
* [EEA frequently asked questions (FAQ)](https://developers.google.com/maps/comms/eea/faq)
* [Google Maps Platform Road Safety Requirements](https://cloud.google.com/terms/maps-platform/eea-safety-requirements)

If your billing address is not in the EEA, the following terms of service apply to you:

* [Google Maps Platform Terms of Service](https://cloud.google.com/maps-platform/terms)
* [Google Maps Platform Service Specific Terms](https://cloud.google.com/maps-platform/terms/maps-service-terms)

## Google Maps attribution requirements

This section provides attribution requirements and guidelines for displaying Google
Maps and Content through your applications.

**Note:** The following updated attribution requirements now use "Google Maps"
instead of only "Google." We acknowledge that your existing implementations may use the
attribution of "Google,"
in alignment with prior guidance, and you may continue using "Google" as an attribution for now.
For new implementations, use "Google Maps" as described in this section. In the future,
we will provide timelines and instructions to help you transition existing "Google" attributions
to "Google Maps" attributions.


### Attribution example

Following is an attribution example for Places UI Kit.

![Places UI Kit
attribution example on a non-Google map](/static/maps/images/non-google-map-places-ui-kit-attribution.png)


Required attribution applied to the Place Details compact component.
On this non-Google map, the Google Maps attribution is clearly visible, and Google Maps Platform
content is visually differentiated from other content.

### Display Google Maps attribution

You must follow Google Maps attribution requirements when displaying Content from
Google Maps Platform APIs in your app or website. You don't need to add extra attribution
if the Content is shown on a Google Map where the attribution is already visible.

### Included Google Maps attribution

For Google Maps attribution that is already provided by Google Maps Platform in
the user interface, such as in Places UI Kit:

* Don't remove included attribution regardless of where it is displayed. Don't alter, hide,
  or obscure the attribution and make sure it is clearly visible against the background.
* Always visually distinguish Google Maps Platform Content from other content by using UI
  cues such as a border, background color, shadow, or sufficient whitespace.
* When making visual modifications, you must adhere to all Google Maps attribution
  requirements.

### Google Maps logo and text attribution

Attribution should take the form of the Google Maps logo whenever possible.
In cases where space is limited, the text **Google Maps** is acceptable.
It must always be clear to end users which content is provided by Google Maps.

![Left: Google Maps logo attribution, Right: Google Maps text attribution](/static/maps/images/01_GMP_Logo_Text.png)


Left: Example of Google Maps logo attribution, Right: Example of Google Maps text attribution



### Logo attribution

Follow these requirements for using the Google Maps logo in your app or website.
![Acceptable variations for Google Maps logo attribution](/static/maps/images/02_GMP_Logo_Alternates.svg)


Examples of acceptable variations for Google Maps logo attribution



#### Download Google Maps logos

Use the official Google Maps logo files. Download the logos below, and follow the guidelines in this section.

[Download the Google Maps attribution assets](https://developers.google.com/static/maps/documentation/images/Google_Maps_Attribution_Assets.zip)

When using the Google Maps logo, follow these guidelines.

* Don't modify the logo in any way.
* Maintain the aspect ratio of the logo to prevent distortion.
* Use the outlined logo on a busy background, like a map or image.
* Use the non-outlined logo on a plain background, like a solid color or subtle gradient.

#### Logo size specification

Follow these size specifications for the Google Maps logo:

* **Minimum logo height:** 16dp
* **Maximum logo height:** 19dp
* **Minimum logo clear space:** 10dp on left, right and top, 5dp on the bottom

To learn about dp, see [Pixel density](https://m2.material.io/design/layout/pixel-density.html#pixel-density) on the Material Design website.

![Google Maps logo showing minimum clear space and acceptable size range](/static/maps/images/03_GMP_Logo_Clear.svg)


Example of Google Maps logo showing minimum clear space and acceptable size range



#### Logo accessibility

Follow these accessibility requirements for the Google Maps logo:

* Maintain an [accessible contrast](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html) between the logo and the background.
* Include an accessibility label with the text **Google Maps**.

![Unacceptable variations and accessibility issues for Google Maps logo attribution](/static/maps/images/04_GMP_Logo_Accessibility.svg)


Examples of unacceptable variations and accessibility issues for Google Maps logo attribution



### Text attribution

If the size of your interface does not support using the Google Maps logo, you can spell out **Google Maps** in text. Follow these guidelines:

![Acceptable variations of the Google Maps text attribution](/static/maps/images/05_GMP_Text_Attribution.svg)


Examples of acceptable variations of the Google Maps text attribution

* Don't modify the text **Google Maps** in any way:  
  + Don't change the capitalization of **Google Maps**
  + Don't wrap **Google Maps** onto multiple lines
  + Don't localize **Google Maps** into another language.
  + Prevent browsers from translating **Google Maps** by using the HTML attribute `translate="no"`.

![Unacceptable variations of the Google Maps text attribution](/static/maps/images/06_GMP_Text_Donts.svg)


Examples of unacceptable variations of the Google Maps text attribution

* Style Google Maps text as described in the following table:

  | Google Maps text-styling requirements | |
  | --- | --- |
  | **Property** | **Style** |
  | Font family | [Roboto](https://fonts.google.com/specimen/Roboto?preview.text_type=custom). Loading the font is optional. |
  | Fallback font family | Any sans serif body font already used in your product or "Sans-Serif" to invoke the default system font |
  | Font style | Normal |
  | Font weight | 400 |
  | Font color | White, black (#1F1F1F), or gray (#5E5E5E). Maintain accessible [(4.5:1)](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html) contrast against the background. |
  | Font size | Minimum font size: 12sp  Maximum font size: 16sp  To learn about sp, see [Font size units](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc) on the Material Design website. |
  | Letter spacing | Normal |

#### Example CSS

The following CSS renders Google Maps with the appropriate typographic style and color on a white or light background.

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {
font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### Visual requirements

Follow these requirements for the visual treatment of Google Maps attribution.

* Position attribution near the top or bottom of the content, and within the same visual container. For a single line of content, attribution can be positioned to the right or left.
* Visually distinguish Google Maps Platform Content from other content by using UI cues such as a border, background color, shadow, or sufficient whitespace.
* Don't misrepresent Google Maps by attributing it with non-Google Maps Platform content.
* Verify that the attribution is always visible and legible. Never remove, hide, obscure, or modify it.

The following figures show examples of these visual requirements.

![Example of Google Maps attribution positioned at the top, at the bottom, and to the side of the content](/static/maps/images/07_GMP_Attribution_Placement.png)


Example of Google Maps attribution positioned at the top, at the bottom, and to the side of the content

  

![Example of two approaches to differentiating Google Maps Content (the place rating) from other content](/static/maps/images/08_GMP_Attribution_Separation.svg)


Example of two approaches to differentiating Google Maps Content (the place rating) from other content

  

![Don't obscure the Google Maps attribution or mix it with content from other sources](/static/maps/images/09_GMP_Attribution_position_donts.png)


Don't obscure the Google Maps attribution or mix it with content from other sources



### Third-party data providers

Some of the data and images on our mapping products come from providers other than Google.
For some products, such as Map Tiles API, we may provide you with the required attribution
to the third-party data provider. When we do, the text of your
attribution must say the name "Google Maps" and the relevant
data provider(s), such as "Map data: Google, Maxar Technologies." When Google provides
third-party attribution, only including "Google Maps" or the Google logo is not
proper attribution.

## Other attribution requirements

Attributions to third-party providers contain content and links that you
must display to the user in the format in which they are provided. Google
recommends that your app shows this information below the place details.

The third-party attributions returned by
the API do **not** include the Google attribution. You must
include this attribution yourself, as described in
[Displaying the Google logo and attributions](https://developers.google.com/maps/documentation/places/ios-sdk/places-ui-kit-attr-req#logo).

**Tip:** You might find it convenient to use
a third-party library to render `NSAttributedString` data.

Follow these instructions to retrieve third-party attributions for a single
place or a collection of places.

### Retrieve attributions for a single place

When you retrieve a place by [getting a
place by ID](https://developers.google.com/maps/documentation/places/ios-sdk/place-details#get-place), you
can retrieve the attributions for that place from the
`attributions` property on
[`GMSPlace`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlace).

The `attributions` are provided as an
`NSAttributedString` object.

### Retrieve attributions for a collection of places

If your app displays information obtained by requesting the device's
[current place](https://developers.google.com/maps/documentation/places/ios-sdk/current-place), the app must display
third-party attributions for the place details displayed. You can retrieve the
attributions for all the places retrieved in the request, from the
`attributions` property on
[`GMSPlaceLikelihoodList`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlaceLikelihoodList).

The `attributions` are provided as a
`NSAttributedString` object, which you can access and display in
the same way as the `attributions` on a single place, as described
[above](https://developers.google.com/maps/documentation/places/ios-sdk/places-ui-kit-attr-req#attributions-place).

### Search results attributions

In Europe, when using Google's unadulterated ranking, search products must have explainer text no
more than 1 click away that describes the main factors and the weighting of the main factors that
determine search results ranking. Explainer text:

> *Header:* About these results  
>   
> *Body:* When you search for businesses or places near a location, Google Maps will show you
> local results. Several factors — primarily relevance, distance and prominence — are combined to
> help find the best results for your search.  
>   
> *Button 1:* Learn more  
> *"Learn more" text should link to a [Help Center article](https://support.google.com/maps/answer/3092445?&ref_topic=3092444#zippy=%2Cwithin-google-maps%2Cother-google-products).*  
>   
> *Button 2:* OK

### Display attributions for a photo

If your app displays
[photos](https://developers.google.com/maps/documentation/places/ios-sdk/photos), you must
show any `attributions` and `authorAttributions` for each
photo that has them.

* To access any attributions, use
  [`GMSPlacePhotoMetadata.attributions`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacePhotoMetadata).
  This property is a `NSAttributedString`, or `nil` if
  there are no attributions to display.
* To access any author attributions, use
  [`GMSPlacePhotoMetadata.authorAttributions`](https://developers.google.com/maps/documentation/places/ios-sdk/reference/objc/Classes/GMSPlacePhotoMetadata).
  This property contains an array of `GMSPlaceAuthorAttribution`
  objects.

### Swift

```
GMSPlacesClient.sharedClient().lookUpPhotosForPlaceID(placeID) { (photos, error) -> Void in
  if let error = error {
    // TODO: handle the error.
    print("Error: \(error.description)")
  } else {
    // Get attribution for the first photo in the list.
    if let photo = photos?.results.first {
      let attributions = photo.attributions
    }
  }
}
```

### Objective-C

```
[[GMSPlacesClient sharedClient]
    lookUpPhotosForPlaceID:placeID
      callback:^(GMSPlacePhotoMetadataList *_Nullable photos,
                  NSError *_Nullable error) {
        if (error) {
          // TODO: handle the error.
          NSLog(@"Error: %@", [error description]);
        } else {
          // Get attribution for the first photo in the list.
          if (photos.results.count > 0) {
            GMSPlacePhotoMetadata *photo = photos.results.firstObject;
            NSAttributedString *attributions = photo.attributions;
          }
        }
      }];
```

### Display a review

A `GMSPlace` object can contain up to five reviews, where each
review is represented by a `GMSPlaceReview` object. You can
optionally display these reviews in your app.

When displaying reviews contributed by Google users, you must place the
author's name in close proximity. When available in the author attribution field
of the `GMSPlaceReview` object, we recommend you include the author's
photo and link to their profile as well. The following image shows an example
of a review of a park:

![Author attribution display](/static/maps/documentation/places/images/review_attributions.png)

Google also recommends that you display how reviews are being sorted to the
end user.

**Note:** The default is to sort the reviews by
relevance. For the new SDK, sorting by relevance is the only option.

To access the reviews:

### Swift

```
// Define a Place ID.
let placeID = "ChIJV4k8_9UodTERU5KXbkYpSYs"

// Specify the place data types to return.
let myProperties: [GMSPlaceProperty] = [.name, .website, .reviews]

// Create the GMSFetchPlaceRequest object.
let fetchPlaceRequest = GMSFetchPlaceRequest(placeID: placeID, placeProperties: myProperties)

client.fetchPlaceWithRequest(fetchPlaceRequest: fetchPlaceRequest, callback: {
  (place: GMSPlace?, error: Error?) in
  if let error = error {
    print("An error occurred: \(error.localizedDescription)")
    return
  }
  if let place = place {
    let firstReview: GMSPlaceReview = place.reviews![0]

    // Use firstReview to access review text, authorAttribution, and other fields.

  }
})
```

### Objective-C

```
// Define a Place ID.
NSString *placeID = @"ChIJV4k8_9UodTERU5KXbkYpSYs";

// Specify the place data types to return, including reviews.
NSArray<GMSPlaceProperty *> *myProperties = @[GMSPlacePropertyName, GMSPlacePropertyWebsite,GMSPlacePropertyReviews];

GMSFetchPlaceRequest *fetchPlaceRequest = [[GMSFetchPlaceRequest alloc] initWithPlaceID:placeID placeProperties: myProperties];

[placesClient fetchPlaceWithRequest: fetchPlaceRequest, callback: ^(GMSPlace *_Nullable place, NSError *_Nullable error) {
  if (error) {
    // TODO: handle the error.
    NSLog(@"Error: %@", [error description]);
  } else {
    // Get first review.
    GMSPlaceReview *firstReview = [place reviews][0];

    // Use firstReview to access review text, authorAttribution, and other fields.

  }
}];
```

### Display third-party attributions

Attributions to third-party providers are provided as `NSAttributedString` objects that
contain content and links that you must preserve and display to the user.

The recommended way to display the attributions is with a `UITextView`, because links in the attributions must work.
To ensure links work, set a delegate on the `UITextView` and set the `shouldInteractWithURL`
method of your `UITextViewDelegate` to return `YES`.

### Swift

```
...
  self.attributionTextView.delegate = self
...

// MARK: - UITextViewDelegate

func textView(textView: UITextView, shouldInteractWithURL URL: NSURL,
  inRange characterRange: NSRange) -> Bool {
  // Make links clickable.
  return true
}
```

### Objective-C

```
...
  self.attributionTextView.delegate = self;
...

#pragma mark - UITextViewDelegate

- (BOOL)textView:(UITextView *)textView
    shouldInteractWithURL:(NSURL *)url
                  inRange:(NSRange)characterRange {
  // Make links clickable.
  return YES;
}
```

### Example of a third-party attribution

A third-party attribution typically consists of text with a link. For
example:

*Listings by [Example Company](https://www.example.com/)*

In the above example, the *Example Company* text range is covered by
an `NSLink` attribute.

### Autocomplete for end user addresses

When an end user uses Autocomplete functionality within your Customer Application to type
ahead a street address and that street address would have been completely and accurately provided
by that end user without Autocomplete, the end user's selected address is then
not subject to the Google Maps Content restrictions in your Google Maps Platform Agreement.
This exception applies only to the street address selected by the end user and solely for
that end user's specific transaction; it does not apply to the list of suggested addresses
provided by the Autocomplete functionality or to other Google Maps Content. This exception does
not apply to any POI or address lookup functionality offered by other Google Maps Platform
Services.

![Autocomplete end user address](/static/maps/documentation/places/images/autocomplete-end-user-address.png)

*In the previous image, the address list on the left is still subject to the restrictions on
Google Maps Content. Once the end user selects their chosen address, that address is not subject
to the restrictions on Google Maps Content solely for the purpose of that end user's
applicable transaction.*
