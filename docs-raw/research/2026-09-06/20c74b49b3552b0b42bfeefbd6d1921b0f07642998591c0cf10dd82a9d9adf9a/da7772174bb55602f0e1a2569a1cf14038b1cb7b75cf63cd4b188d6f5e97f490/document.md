# Policies and attributions for Places SDK for Android

This topic provides attribution requirements for all applications
developed with the Places SDK for Android, including the Place Autocomplete
service that is part of that API. For more Google Maps Platform terms,
see the [Google Maps Platform Terms of Service](https://cloud.google.com/maps-platform/terms/).

## Policies

This section describes policies relevant to Places SDK for Android. Policies provide practical
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

Follow these instructions to retrieve third-party attributions, and to display
the attributions in your app.

**Note:** Reviews and photos provided through the Places SDK for Android are
subject to Google's content and product policies wherever you are in the world.
To report content that you or your users would like removed from Google's
services under Google's policies or applicable laws, see
[Report Content On Google](https://support.google.com/legal/troubleshooter/1114905#ts=9723198%2C7170398).


### Retrieving attributions from a Place

If your app displays information obtained by calling
[get place by ID](https://developers.google.com/maps/documentation/places/android-sdk/place-details#get-place),
the app must also display third-party attributions for the place details
obtained.

The API returns a
[`Place`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/Place)
object. To retrieve attributions from the `Place` object, call
[`Place.getAttributions()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/Place#getAttributions()).
The method returns a `List` of `String` objects, or null
if there are no attributions to display.

```
String placeId = "INSERT_PLACE_ID_HERE";
List<Place.Field> placeFields = Arrays.asList(Place.Field.ID, Place.Field.DISPLAY_NAME);
FetchPlaceRequest request = FetchPlaceRequest.newInstance(placeId, placeFields);

placesClient.fetchPlace(request).addOnSuccessListener((response) -> {
  Place place = response.getPlace();
  textView.append("Place found: " + place.getName());
  List<String> attributions = place.getAttributions();
  if (attributions != null) {
    StringBuilder stringBuilder = new StringBuilder("Attributions: ");
    for (String attribution : attributions) {
      stringBuilder.append(attribution).append("\n");
    }
    textView.append(stringBuilder.toString());
  }}).addOnFailureListener((exception) -> {
    if (exception instanceof ApiException) {
      // Handle the error.
    }
  }
);
```



### Display attributions for a photo

If your app displays place photos, you must
show attributions for each photo that has them.
[`PhotoMetadata`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/PhotoMetadata),
can contain either of two types of attributions:

* **Attributions**, an attribution string accessed by
  [`PhotoMetadata.getAttributions()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/PhotoMetadata#public-abstract-string-getattributions).
* **AuthorAttributions**, an
  [`AuthorAttributions`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/AuthorAttributions)
  object accessed by
  [`PhotoMetadata.getAuthorAttributions()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/PhotoMetadata#public-abstract-authorattributions-getauthorattributions).

To get the string attributions for a photo, call
`PhotoMetadata.getAttributions()`. The method returns an
HTML character sequence, or an empty string if there are no attributions to
display.

```
// Get the photo metadata from the Place object.
PhotoMetadata photoMetadata = place.getPhotoMetadatas().get(0);

// Get the attribution text.
String attributions = photoMetadata.getAttributions();
```

To get the author attributions for a photo, call
`PhotoMetadata.getAuthorAttributions()`. The method returns an
`AuthorAttributions` object. This object contains a `List`
of [`AuthorAttribution`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/AuthorAttribution)
objects, one per author attribution.

```
// Get the photo metadata from the Place object.
PhotoMetadata photoMetadata = place.getPhotoMetadatas().get(0);

// Get the author attributions object.
AuthorAttributions authorAttributions = photoMetadata.getAuthorAttributions();
List<AuthorAttribution> authorAttributionList = authorAttributions.asList();
```



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

### Display a review

A `Place` object can contain up to five reviews, where each review
is represented by a
[`Review`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/Review)
object. You can optionally display these reviews in your app.

When displaying reviews contributed by Google users, you must place the
author's name in close proximity. When available in the author attribution field
of the `Review` object, we recommend you include the author's photo
and link to their profile as well. The following image shows an example of a
review of a park:

![Author attribution display](/static/maps/documentation/places/images/review_attributions.png)

Google also recommends that you display how reviews are being sorted to the
end user.

**Note:** The default is to sort the reviews by
relevance. For the new SDK, sorting by relevance is the only option.

To access the reviews, call
[`Place.getReviews()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/Place#getReviews()):

```
// Specify the fields to return.
final List<Place.Field> placeFields = Arrays.asList(Place.Field.REVIEWS);

// Construct a request object, passing the place ID and fields array.
final FetchPlaceRequest request = FetchPlaceRequest.newInstance("INSERT_PLACE_ID_HERE", placeFields);

placesClient.fetchPlace(request).addOnSuccessListener((response) -> {
    Place place = response.getPlace();
    List<Review> reviews = place.getReviews();
    // For loop for iterating over the List
    for (int i = 0; i < reviews.size(); i++) {
      // For each review, get the Review object.
        Review placeReview = reviews.get(i);

      // Get any attribution and author attribution.
        String reviewAttribution = placeReview.getAttribution();
        AuthorAttribution authorAttribution = placeReview.getAuthorAttribution();

        // Display the review contents and attributions as necessary.
    }
}).addOnFailureListener((exception) -> {
    if (exception instanceof ApiException) {
        // Handle the error.
    }
});
```



### Displaying third-party attributions

Attributions to third-party providers contain content and links in HTML
format that you must preserve and display to the user in the format in which
they are provided. Google recommends displaying this information below the place details.

The API generates attributions for all the places that are used by the app.
The attributions are supplied per API call, not per place.

**Note:** The attributions returned by these methods
do **not** include the Google attribution. You must include
this attribution yourself, as described in
[Displaying the Google logo and attributions](https://developers.google.com/maps/documentation/places/android-sdk/places-ui-kit-attr-req#logo).

One way to display the attributions is with a
[`TextView`](https://developer.android.com/reference/android/widget/TextView.html).
For example:

```
TextView attributionsText = (TextView) findViewById(R.id.attributions);
String thirdPartyAttributions = place.getAttributions();
attributionsText.setText(thirdPartyAttributions);
```



### Example of a third-party attribution

```
Listings by <a href="https://www.example.com/">Example Company</a>
```



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
