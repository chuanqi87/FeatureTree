# Place Autocomplete

**European Economic Area (EEA) developers**

If your billing address is in the European Economic Area, effective on 8 July 2025, the
[Google Maps Platform EEA Terms of Service](https://cloud.google.com/terms/maps-platform/eea)
will apply to your use of the Services. Functionality varies by region.
[Learn more](https://developers.google.com/maps/comms/eea/faq).

The autocomplete service in the Places SDK for Android returns place
predictions in response to user search queries. As the user types, the
autocomplete service returns suggestions for places such as businesses,
addresses, [plus codes](https://plus.codes), and
points of interest.

You can add autocomplete to your app in the following ways:

* [Add an autocomplete widget](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#add_an_autocomplete_widget) to save
  development time and ensure a consistent user experience.
* [Get place predictions
  programmatically](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#get_place_predictions_programmatically) to create a
  customized user experience.

**Deprecated:** The Places API (Legacy) autocomplete widget is deprecated. [Migrate to Place Autocomplete (New)](https://developers.google.com/maps/documentation/places/android-sdk/legacy/migrate-autocomplete) to use the [Autocomplete (New) widget](https://developers.google.com/maps/documentation/places/android-sdk/place-autocomplete#autocomplete-widget), or [get place predictions programmatically](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#get_place_predictions). Note that in order to use Place Autocomplete (New) and the Autocomplete (New) widget, you need to enable the Places API (New) on your API key in the Google Cloud console.


## Add an autocomplete widget

![](/static/maps/documentation/places/images/autocomplete-android.png)

The autocomplete widget is a search dialog with built-in autocomplete
functionality. As a user enters search terms, the widget presents a list of
predicted places to choose from. When the user makes a selection, a
[`Place`](https://developers.google.com/android/reference/com/google/android/gms/location/places/Place)
instance is returned, which your app can then use to get details about the
selected place.

There are two options for adding the autocomplete widget to your app:

* [Option 1: Embed an `AutocompleteSupportFragment`](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#option_1_embed_an_autocompletesupportfragment).
* [Option 2: Use an intent to launch the autocomplete activity](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#option_2_use_an_intent_to_launch_the_autocomplete_activity).

### Option 1: Embed an AutocompleteSupportFragment

To add an `AutocompleteSupportFragment` to your app, take the following steps:

1. Add a fragment to your activity's XML layout.
2. Add a listener to your activity or fragment.

#### Add AutocompleteSupportFragment to an activity

To add `AutocompleteSupportFragment` to an activity, add a new fragment to an
XML layout. For example:

```
<fragment android:id="@+id/autocomplete_fragment"
  android:layout_width="match_parent"
  android:layout_height="wrap_content"
  android:name="com.google.android.libraries.places.widget.AutocompleteSupportFragment"
  />
```

* By default, the fragment has no border or background. To provide a
  consistent visual appearance, nest the fragment within another layout
  element such as a
  [CardView](http://developer.android.com/training/material/lists-cards.html).
* If you are using the Autocomplete fragment, and need to override
  `onActivityResult`, you must call `super.onActivityResult`, otherwise the
  fragment will not function properly.

#### Add a PlaceSelectionListener to an activity

The `PlaceSelectionListener` handles returning a place in response to the user's
selection. The following code shows creating a reference to the fragment and
adding a listener to your `AutocompleteSupportFragment`:

### Kotlin

```
    // Initialize the AutocompleteSupportFragment.
    val autocompleteFragment =
        supportFragmentManager.findFragmentById(R.id.autocomplete_fragment)
                as AutocompleteSupportFragment

    // Specify the types of place data to return.
    autocompleteFragment.setPlaceFields(listOf(Place.Field.ID, Place.Field.DISPLAY_NAME))

    // Set up a PlaceSelectionListener to handle the response.
    autocompleteFragment.setOnPlaceSelectedListener(object : PlaceSelectionListener {
        override fun onPlaceSelected(place: Place) {
            binding.autocompleteResult.text = getString(
                R.string.place_selection,
                place.displayName,
                place.id,
                place.formattedAddress
            )
            Log.i(TAG, "Place: ${place.displayName}, ${place.id}")
        }

        override fun onError(status: Status) {
            binding.autocompleteResult.text = getString(R.string.an_error_occurred, status)
            Log.i(TAG, "An error occurred: $status")
        }
    })
```

### Java

```
    // Initialize the AutocompleteSupportFragment.
    AutocompleteSupportFragment autocompleteFragment = (AutocompleteSupportFragment)
            getSupportFragmentManager().findFragmentById(R.id.autocomplete_fragment);

    // Specify the types of place data to return.
    assert autocompleteFragment != null;
    autocompleteFragment.setPlaceFields(Arrays.asList(Place.Field.ID, Place.Field.DISPLAY_NAME, Place.Field.FORMATTED_ADDRESS));

    // Set up a PlaceSelectionListener to handle the response.
    autocompleteFragment.setOnPlaceSelectedListener(new PlaceSelectionListener() {
        @Override
        public void onPlaceSelected(@NonNull Place place) {
            binding.autocompleteResult.setText(
                    getString(
                            R.string.place_selection,
                            place.getDisplayName(),
                            place.getId(),
                            place.getFormattedAddress()
                    )
            );
            Log.i(TAG, "Place: " + place.getDisplayName() + ", " + place.getId());
        }


        @Override
        public void onError(@NonNull Status status) {
            binding.autocompleteResult.setText(getString(R.string.an_error_occurred, status));
            Log.e(TAG, "An error occurred: " + status);
        }
    });
```

### Option 2: Use an intent to launch the autocomplete activity

If you want your app to use a different navigational flow (for example, to
trigger the autocomplete experience from an icon rather than a search field),
your app can launch autocomplete by using an intent.

**Note:** These steps aren't needed if you are [embedding a
fragment](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#option_1_embed_an_autocompletesupportfragment).**Caution:** Do NOT launch the `AutcompleteActivity` directly. Instead, use an
intent to launch `Autocomplete` (`PlaceAutocomplete` in the compatibility
library).

To launch the autocomplete widget using an intent, follow these steps:

1. Use [`Autocomplete.IntentBuilder`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/widget/Autocomplete.IntentBuilder)
   to create an intent, passing the desired `Autocomplete` mode.
2. Define an activity result launcher
   [`registerForActivityResult`](https://developer.android.com/reference/androidx/activity/result/ActivityResultCaller#registerForActivityResult(androidx.activity.result.contract.ActivityResultContract%3CI,O%3E,androidx.activity.result.ActivityResultCallback%3CO%3E))
   that can be used to launch the intent and handle the user's selected place
   prediction in the result.

#### Create an autocomplete intent

The example below uses
[`Autocomplete.IntentBuilder`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/widget/Autocomplete.IntentBuilder)
to create an intent to launch the autocomplete widget as an intent:

### Kotlin

```
    // Set the fields to specify which types of place data to
    // return after the user has made a selection.
    val fields = listOf(Place.Field.ID, Place.Field.DISPLAY_NAME, Place.Field.FORMATTED_ADDRESS)

    val intent = Autocomplete.IntentBuilder(AutocompleteActivityMode.FULLSCREEN, fields)
        .setTypesFilter(listOf(PlaceTypes.ESTABLISHMENT))
        .build(this)

    startAutocomplete.launch(intent)
```

### Java

```
    // Set the fields to specify which types of place data to
    // return after the user has made a selection.
    List<Place.Field> fields = Arrays.asList(Place.Field.ID, Place.Field.DISPLAY_NAME, Place.Field.FORMATTED_ADDRESS);

    // Start the autocomplete intent.
    Intent intent = new Autocomplete.IntentBuilder(AutocompleteActivityMode.FULLSCREEN, fields)
            .setTypesFilter(List.of(PlaceTypes.ESTABLISHMENT))
            .build(this);
    startAutocomplete.launch(intent);
```

When using an intent to launch the autocomplete widget, you can choose from
overlay or full-screen display modes. The following screenshots show each
display mode respectively:

![When displayed in overlay mode, the autocomplete widget appears superimposed over the calling UI.](/static/maps/documentation/places/images/acw_overlay.png)


**Figure 1**: Autocomplete widget in OVERLAY mode

![When displayed in fullscreen mode, the autocomplete widget fills the entire screen.](/static/maps/documentation/places/images/acw_fullscreen.png)


**Figure 2**: Autocomplete widget in FULLSCREEN mode

#### Register a callback for the intent result

To receive a notification when the user has selected a place, define a
`registerForActivityResult()` launcher, which launches the activity and also handles the
result as shown in the following example. If the user selected a prediction, it
will be delivered in the intent contained in the result object. Since the intent
was built by `Autocomplete.IntentBuilder`, the method
`Autocomplete.getPlaceFromIntent()` can extract the Place object from it.

### Kotlin

```
private val startAutocomplete =
    registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result: ActivityResult ->
        if (result.resultCode == RESULT_OK) {
            val intent = result.data
            if (intent != null) {
                val place = Autocomplete.getPlaceFromIntent(intent)
                binding.autocompleteResult.text = getString(
                    R.string.place_selection,
                    place.displayName,
                    place.id,
                    place.formattedAddress)
                Log.i(
                    TAG, "Place: ${place.displayName}, ${place.id}"
                )
            }
        } else if (result.resultCode == RESULT_CANCELED) {
            // The user canceled the operation.
            binding.autocompleteResult.setText(R.string.user_canceled_autocomplete)
            Log.i(TAG, "User canceled autocomplete")
        }
    }
```

### Java

```
private final ActivityResultLauncher<Intent> startAutocomplete = registerForActivityResult(
        new ActivityResultContracts.StartActivityForResult(),
        result -> {
            if (result.getResultCode() == Activity.RESULT_OK) {
                Intent intent = result.getData();
                if (intent != null) {
                    Place place = Autocomplete.getPlaceFromIntent(intent);
                    binding.autocompleteResult.setText(
                            getString(
                                    R.string.place_selection,
                                    place.getDisplayName(),
                                    place.getId(),
                                    place.getFormattedAddress()
                            )
                    );
                    Log.i(TAG, "Place: " + place.getDisplayName() + ", " + place.getId());
                }
            } else if (result.getResultCode() == Activity.RESULT_CANCELED) {
                // The user canceled the operation.
                binding.autocompleteResult.setText(R.string.user_canceled_autocomplete);
                Log.i(TAG, "User canceled autocomplete");
            }
        });
```

## Getting place predictions programmatically

You can create a custom search UI as an alternative to the UI provided by the
autocomplete widget. To do this, your app must get place predictions
programmatically. Your app can get a list of predicted place names and/or
addresses from the autocomplete API by calling
[`PlacesClient.findAutocompletePredictions()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/net/PlacesClient#findAutocompletePredictions(com.google.android.libraries.places.api.net.FindAutocompletePredictionsRequest)),
passing a
[`FindAutocompletePredictionsRequest`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/net/FindAutocompletePredictionsRequest)
object with the following parameters:

* *Required:* A `query` string containing the text typed by the user.
* *Recommended:* A
  [`AutocompleteSessionToken`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/AutocompleteSessionToken),
  which groups the query and selection phases of a user search into a discrete
  session for billing purposes. The session begins when the user starts typing
  a query, and concludes when they select a place.
* *Recommended:* A [`RectangularBounds`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/RectangularBounds)
  object, which specifies latitude and longitude bounds to [constrain results to
  the specified region](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#constrain-AC-results).
* *Optional:* One or more two-letter [country
  code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)s (ISO 3166-1
  Alpha-2), indicating the country or countries to which results should be
  restricted.
* *Optional:* A
  [`TypeFilter`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/TypeFilter),
  which you can use to restrict the results to the specified place type. The
  following place types are supported:

  + `TypeFilter.GEOCODE` – Returns only geocoding results, rather than
    businesses. Use this request to disambiguate results where the specified
    location may be indeterminate.
  + `TypeFilter.ADDRESS` – Returns only autocomplete results with a
    precise address. Use this type when you know the user is looking for a
    fully specified address.
  + `TypeFilter.ESTABLISHMENT` – Returns only places that are
    businesses.
  + `TypeFilter.REGIONS` – Returns only places that match one of the
    following types:
  + `LOCALITY`
  + `SUBLOCALITY`
  + `POSTAL_CODE`
  + `COUNTRY`
  + `ADMINISTRATIVE_AREA_LEVEL_1`
  + `ADMINISTRATIVE_AREA_LEVEL_2`
  + `TypeFilter.CITIES` – Returns only results matching `LOCALITY` or
    `ADMINISTRATIVE_AREA_LEVEL_3`.
* *Optional:* A `LatLng` specifying the location of origin for the request.
  When you call
  [`setOrigin()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/net/FindAutocompletePredictionsRequest.Builder#setOrigin(com.google.android.gms.maps.model.LatLng)),
  the service returns distance in meters (`distanceMeters`) from the specified
  origin, for each autocomplete prediction in the response.

For information about place types, see the guide to [place
types](https://developers.google.com/maps/documentation/places/android-sdk/supported_types#table3).

The example below shows a complete call to
[`PlacesClient.findAutocompletePredictions()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/net/PlacesClient#findAutocompletePredictions(com.google.android.libraries.places.api.net.FindAutocompletePredictionsRequest)).

### Kotlin

```
    // Create a new token for the autocomplete session. Pass this to FindAutocompletePredictionsRequest,
    // and once again when the user makes a selection (for example when calling fetchPlace()).
    val token = AutocompleteSessionToken.newInstance()

    // Create a RectangularBounds object.
    val bounds = RectangularBounds.newInstance(
        LatLng(-33.880490, 151.184363),
        LatLng(-33.858754, 151.229596)
    )
    // Use the builder to create a FindAutocompletePredictionsRequest.
    val request =
        FindAutocompletePredictionsRequest.builder()
            // Call either setLocationBias() OR setLocationRestriction().
            .setLocationBias(bounds)
            //.setLocationRestriction(bounds)
            .setOrigin(LatLng(-33.8749937, 151.2041382))
            .setCountries("AU", "NZ")
            .setTypesFilter(listOf(PlaceTypes.ESTABLISHMENT))
            .setSessionToken(token)
            .setQuery(query)
            .build()
    placesClient.findAutocompletePredictions(request)
        .addOnSuccessListener { response: FindAutocompletePredictionsResponse ->
            val builder = StringBuilder()
            for (prediction in response.autocompletePredictions) {
                builder.append(prediction.getPrimaryText(null).toString()).append("\n")
                Log.i(TAG, prediction.placeId)
                Log.i(TAG, prediction.getPrimaryText(null).toString())
            }
            binding.autocompleteResult.text = builder.toString()
        }.addOnFailureListener { exception: Exception? ->
            if (exception is ApiException) {
                Log.e(TAG, "Place not found: ${exception.statusCode}")
                binding.autocompleteResult.text = getString(R.string.place_not_found, exception.message)
            }
        }
```

### Java

```
    // Create a new token for the autocomplete session. Pass this to FindAutocompletePredictionsRequest,
    // and once again when the user makes a selection (for example when calling fetchPlace()).
    AutocompleteSessionToken token = AutocompleteSessionToken.newInstance();

    // Create a RectangularBounds object.
    RectangularBounds bounds = RectangularBounds.newInstance(
            new LatLng(-33.880490, 151.184363),
            new LatLng(-33.858754, 151.229596));
    // Use the builder to create a FindAutocompletePredictionsRequest.
    FindAutocompletePredictionsRequest request = FindAutocompletePredictionsRequest.builder()
            // Call either setLocationBias() OR setLocationRestriction().
            .setLocationBias(bounds)
            //.setLocationRestriction(bounds)
            .setOrigin(new LatLng(-33.8749937, 151.2041382))
            .setCountries("AU", "NZ")
            .setTypesFilter(List.of(PlaceTypes.ESTABLISHMENT))
            .setSessionToken(token)
            .setQuery(query)
            .build();

    placesClient.findAutocompletePredictions(request).addOnSuccessListener((response) -> {
        StringBuilder builder = new StringBuilder();
        for (AutocompletePrediction prediction : response.getAutocompletePredictions()) {
            builder.append(prediction.getPrimaryText(null).toString()).append("\n");
            Log.i(TAG, prediction.getPlaceId());
            Log.i(TAG, prediction.getPrimaryText(null).toString());
        }
        binding.autocompleteResult.setText(builder.toString());
    }).addOnFailureListener((exception) -> {
        if (exception instanceof ApiException apiException) {
            Log.e(TAG, "Place not found: " + apiException.getStatusCode());
            binding.autocompleteResult.setText(getString(R.string.place_not_found, apiException.getMessage()));
        }
    });
```

The API returns an
[`FindAutocompletePredictionsResponse`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/net/FindAutocompletePredictionsResponse)
in a [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task). The [`FindAutocompletePredictionsResponse`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/net/FindAutocompletePredictionsResponse)
contains a list of
[`AutocompletePrediction`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/AutocompletePrediction)
objects representing predicted places. The list may be empty, if there is no
known place corresponding to the query and the filter criteria.

For each predicted place, you can call the following methods to retrieve place
details:

* [`getFullText(CharacterStyle)`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/AutocompletePrediction#getFullText(android.text.style.CharacterStyle))
  returns the full text of a place description. This is a combination of the
  primary and secondary text. Example: "*Eiffel Tower, Avenue Anatole France,
  Paris, France*". In addition, this method lets you highlight the sections of the
  description that match the search with a style of your choice, using
  [`CharacterStyle`](https://developer.android.com/reference/android/text/style/CharacterStyle.html).
  The `CharacterStyle` parameter is optional. Set it to null if you don't
  need any highlighting.
* [`getPrimaryText(CharacterStyle)`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/AutocompletePrediction#getPrimaryText(android.text.style.CharacterStyle))
  returns the main text describing a place. This is usually the name of the
  place. Examples: "*Eiffel Tower*", and "*123 Pitt Street*".
* [`getSecondaryText(CharacterStyle)`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/AutocompletePrediction#getSecondaryText(android.text.style.CharacterStyle))
  returns the subsidiary text of a place description. This is useful, for
  example, as a second line when showing autocomplete predictions. Examples:
  "*Avenue Anatole France, Paris, France*", and "*Sydney, New South Wales*".
* [`getPlaceId()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/AutocompletePrediction#getPlaceId())
  returns the place ID of the predicted place. A place ID is a textual
  identifier that uniquely identifies a place, which you can use to retrieve
  the
  [`Place`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/Place)
  object again later. For more information about place IDs in
  Places SDK for Android, see the [Place
  Details](https://developers.google.com/maps/documentation/places/android-sdk/place-details). For general
  information about place IDs, see the [Place ID
  overview](https://developers.google.com/maps/documentation/places/android-sdk/place-id).
* [`getPlaceTypes()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/AutocompletePrediction#getPlaceTypes())
  returns the list of place types associated with this place.
* [`getDistanceMeters()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/AutocompletePrediction#getDistanceMeters())
  returns the straight-line distance in meters between this place and the
  origin specified in the request.

**Note:** For more information on initializing `PlacesClient`, see
[Initialize the Places API client](https://developers.google.com/maps/documentation/places/android-sdk/config#connect-client).


You can use a [CancellationToken](https://developers.google.com/android/reference/com/google/android/gms/tasks/CancellationToken)
to attempt to cancel a request to any of the request classes (for example,
`FetchPlaceRequest`). Cancellation is done on a best-effort basis.
Once a cancellation request is issued, no response will be returned.
**Issuing a cancellation token does NOT guarantee that a particular request
will be cancelled, and you may still be charged for the request even if no
response is returned**.



### Session tokens

Session tokens group the query and selection phases of a user autocomplete
search into a discrete session for billing purposes. The session begins when the
user starts typing a query, and concludes when they select a place. Each session
can have multiple queries, followed by one place selection. Once a session has
concluded, the token is no longer valid; your app must generate a fresh token
for each session. We recommend using session tokens for all programmatic
autocomplete sessions (when you embed a fragment, or launch autocomplete using
an intent, the API takes care of this automatically).

The Places SDK for Android uses a
[`AutocompleteSessionToken`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/AutocompleteSessionToken)
to identify each session. Your app should pass a new session token upon
beginning each new session, then pass that same token, along with a Place ID, in
the subsequent call to
[`fetchPlace()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/net/PlacesClient#fetchPlace(com.google.android.libraries.places.api.net.FetchPlaceRequest))
to retrieve Place Details for the place that was selected by the user.

**Tip:** If your app is using the [Autocomplete
widget](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#add_an_autocomplete_widget),
you don't need to implement sessions, as the widget handles sessions
automatically in the background.

[Learn more about session
tokens](https://developers.google.com/maps/documentation/places/android-sdk/session-tokens).

## Constrain autocomplete results

You can constrain autocomplete results to a specific geographic region, and/or
filter the results to one or more place types, or to up to five countries. You
can apply these constraints to the autocomplete activity,
`AutocompleteSupportFragment`, and programmatic autocomplete APIs.

To constrain results, do the following:

* To *prefer* results within the defined region, call `setLocationBias()`
  (some results from outside the defined region may still be returned).
* To *only show* results within the defined region, call
  `setLocationRestriction()` (only results within the defined region will be
  returned).
* To return only results that conform to a particular place type, call
  `setTypesFilter()` (for example, specifying `TypeFilter.ADDRESS` will return
  only results with a precise address).
* To return only results within up to five specified countries, call
  `setCountries()`. Countries must be passed as a two-character, ISO 3166-1
  Alpha-2 compatible [country
  code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

### Bias results to a specific region

To bias autocomplete results to a specific geographic region, call
`setLocationBias()`, passing a
[`RectangularBounds`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/RectangularBounds).
The following code example shows calling `setLocationBias()` on a fragment
instance to bias its autocomplete suggestions to a region of Sydney, Australia.

### Kotlin

```
        autocompleteFragment.setLocationBias(bounds)
```

### Java

```
        autocompleteFragment.setLocationBias(
                RectangularBounds.newInstance(
                        new LatLng(-33.880490, 151.184363),
                        new LatLng(-33.858754, 151.229596)
                )
        );
```

### Restrict results to a specific region

To restrict autocomplete results to a specific geographic region, call
`setLocationRestriction()`, passing a
[`RectangularBounds`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/RectangularBounds).
The following code example shows calling `setLocationRestriction()` on a
fragment instance to bias its autocomplete suggestions to a region of Sydney,
Australia.

### Kotlin

```
        autocompleteFragment.setLocationRestriction(bounds)
```

### Java

```
        autocompleteFragment.setLocationRestriction(
                RectangularBounds.newInstance(
                        new LatLng(-33.880490, 151.184363),
                        new LatLng(-33.858754, 151.229596)
                )
        );
```

**Note:** This restriction is only applied to entire routes, synthetic results
located outside the rectangular bounds may be returned based on a route that
overlaps with the location restrict.

### Filter results by place types or type collection

You can restrict results from an autocomplete request so they only return a
certain place type. Specify a filter using the place types or a type collection
listed in Tables 1, 2, and 3 on [Place Types](https://developers.google.com/maps/documentation/places/android-sdk/legacy/supported_types). If nothing is
specified, all types are returned.

To filter autocomplete results, call
[`setTypesFilter()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/widget/PlaceAutocomplete.IntentBuilder#setTypesFilter(kotlin.collections.List))
to set the filter.

To specify a type or type collection filter:

* Call `setTypesFilter()` and specify up to five *type* values from Table 1
  and Table 2 shown on [Place Types](https://developers.google.com/maps/documentation/places/android-sdk/legacy/supported_types). The type values are
  defined by the constants in
  [`PlaceTypes`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/PlaceTypes).
* Call `setTypesFilter()` and specify a *type collection* from Table 3 shown
  on [Place Types](https://developers.google.com/maps/documentation/places/android-sdk/legacy/supported_types). The collection values are defined by the
  constants in
  [`PlaceTypes`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/api/model/PlaceTypes).

  Only a single type from Table 3 is allowed in the request. If you specify a
  value from Table 3, you cannot specify a value from Table 1 or Table 2. If
  you do, then an error occurs.

The following code example calls `setTypesFilter()` on an
`AutocompleteSupportFragment` and specifies multiple type values.

### Kotlin

```
    autocompleteFragment.setTypesFilter(listOf("landmark", "restaurant", "store"))
```

### Java

```
    autocompleteFragment.setTypesFilter(List.of("landmark", "restaurant", "store"));
```

The following code example shows calling `setTypesFilter()` on an
`AutocompleteSupportFragment` to set a filter returning only results with a
precise address by specifying a type collection.

### Kotlin

```
    autocompleteFragment.setTypesFilter(listOf(PlaceTypes.ADDRESS))
```

### Java

```
    autocompleteFragment.setTypesFilter(List.of(PlaceTypes.ESTABLISHMENT));
```

The following code example shows calling `setTypesFilter()` on an
`IntentBuilder` to set a filter returning only results with a precise address by
specifying a type collection.

### Kotlin

```
    val intent = Autocomplete.IntentBuilder(AutocompleteActivityMode.FULLSCREEN, fields)
        .setTypesFilter(listOf(PlaceTypes.ESTABLISHMENT))
        .build(this)
```

### Java

```
    Intent intent = new Autocomplete.IntentBuilder(AutocompleteActivityMode.FULLSCREEN, fields)
            .setTypesFilter(List.of(PlaceTypes.ESTABLISHMENT))
            .build(this);
```

### Filter results by country

To filter autocomplete results to up to five countries, call
[`setCountries()`](https://developers.google.com/maps/documentation/places/android-sdk/reference/com/google/android/libraries/places/widget/AutocompleteSupportFragment#setCountries(java.lang.String...))
to set the [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
Then, pass the filter to a fragment or intent. Countries must be passed as a
two-character, ISO 3166-1 Alpha-2 compatible [country
code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

The following code example shows calling `setCountries()` on an
`AutocompleteSupportFragment`, to set a filter returning only results within the
specified countries.

### Kotlin

```
    autocompleteFragment.setCountries("AU", "NZ")
```

### Java

```
    autocompleteFragment.setCountries("AU", "NZ");
```

## Usage limits

Your usage of the Places API, including the Places SDK for Android, is
no longer limited to a maximum number of requests per day (QPD). However, the
following usage limits still apply:

* Rate limit is 6,000 QPM (requests per minute). It is
  calculated as the sum of client-side and server-side requests for all
  applications using the credentials of the same project.

## Display attributions in your app

* If your app uses the autocomplete service programmatically, your UI must
  either display a 'Powered by Google' attribution, or appear within a
  Google-branded map.
* If your app uses the autocomplete widget no additional action is required
  (the required attribution is displayed by default).
* If you retrieve and display additional place information after [getting a
  place by
  ID](https://developers.google.com/maps/documentation/places/android-sdk/place-details#get-place), you
  must display third-party attributions too.

For more details, see the documentation on
[attributions](https://developers.google.com/maps/documentation/places/android-sdk/attributions).

## Place Autocomplete (Legacy) optimization

This section describes best practices to help you make the most of the
Place Autocomplete (Legacy) service.

Here are some general guidelines:

* The quickest way to develop a working user interface is to use the
  Maps JavaScript API [Place Autocomplete (Legacy) widget](https://developers.google.com/maps/documentation/javascript/places-autocomplete#add-autocomplete),
  Places SDK for Android [Place Autocomplete (Legacy) widget](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#add_an_autocomplete_widget),
  or Places SDK for iOS [Place Autocomplete (Legacy) UI control](https://developers.google.com/maps/documentation/places/ios-sdk/autocomplete#adding_an_autocomplete_ui_control).
* Understand essential
  Place Autocomplete (Legacy) [data fields](https://developers.google.com/maps/documentation/places/android-sdk/legacy/place-data-fields)
  from the start.
* Location biasing and location restriction fields are optional but can
  have a significant impact on autocomplete performance.
* Use error handling to make sure your app degrades gracefully
  if the API returns an error.
* Make sure your app handles when there is no selection and offers users a way
  to continue.

### Cost optimization best practices

#### Basic cost optimization

To optimize the cost of using the Place Autocomplete (Legacy)
service, use field masks in Place Details (Legacy) and Place Autocomplete (Legacy) widgets to return only the
Place Autocomplete (Legacy) [data fields](https://developers.google.com/maps/documentation/places/android-sdk/legacy/place-data-fields)
you need.

#### Advanced cost optimization

Consider programmatic implementation of Place Autocomplete (Legacy) in order to access
[SKU: Autocomplete - Per Request pricing](https://developers.google.com/maps/billing-and-pricing/sku-details#places_autocomplete-per-request-legacy-ess-sku)
and request [Geocoding API results](https://developers.google.com/maps/documentation/geocoding/overview#results) about the selected place instead of Place Details (Legacy). Per-request pricing paired with Geocoding API is more cost-effective than per-session (session-based) pricing if both of the following conditions are met:

* If you only need the latitude/longitude or address of the user's selected place, the Geocoding API delivers this information for less than a Place Details (Legacy) call.
* If users select an autocomplete prediction within an average of four Place Autocomplete (Legacy) predictions requests or fewer, per-request pricing may be more cost-effective than per-session pricing.

For help selecting the Place Autocomplete (Legacy) implementation that fits your needs, select the tab that corresponds to your answer to the following question.

**Does your application require any information other than the address and latitude/longitude of the selected prediction?**

### Yes, needs more details

**Use session-based Place Autocomplete (Legacy) with Place Details (Legacy).**  
Since your application requires Place Details (Legacy), such as the place name, business status,
or opening hours, your implementation of Place Autocomplete (Legacy) should use a session token
([programmatically](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#sessiontoken) or built into the
[JavaScript](https://developers.google.com/maps/documentation/javascript/places-autocomplete#add-autocomplete),
[Android](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#add_an_autocomplete_widget),
or [iOS](https://developers.google.com/maps/documentation/places/ios-sdk/autocomplete#adding_an_autocomplete_ui_control)
widgets) [per session](https://developers.google.com/maps/billing-and-pricing/sku-details#about-autocomplete-sessions)
plus applicable [Places Data SKUs](https://developers.google.com/maps/billing-and-pricing/sku-details#data-skus),
depending on which place data fields you request.[1](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#fn1)

**Widget implementation**  
Session management is automatically built into the
[JavaScript](https://developers.google.com/maps/documentation/javascript/places-autocomplete#add-autocomplete),
[Android](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#add_an_autocomplete_widget),
or [iOS](https://developers.google.com/maps/documentation/places/ios-sdk/autocomplete#adding_an_autocomplete_ui_control)
widgets. This includes both the Place Autocomplete (Legacy) requests and the Place Details (Legacy) request
on the selected prediction. Be sure to specify the `fields` parameter in order to
ensure you are only requesting the
Place Autocomplete (Legacy) [data fields](https://developers.google.com/maps/documentation/places/android-sdk/legacy/place-data-fields)
you need.

**Programmatic implementation**  
Use a
[session token](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#sessiontoken)
with your Place Autocomplete (Legacy) requests. When requesting Place Details (Legacy) about the selected prediction, include the following parameters:

1. The place ID from [the Place Autocomplete (Legacy) response](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#programmatic-response)
2. The session token used in the Place Autocomplete (Legacy) request
3. The `fields` parameter specifying the
   Place Autocomplete (Legacy) [data fields](https://developers.google.com/maps/documentation/places/android-sdk/legacy/place-data-fields)
   you need

### No, needs only address and location

Geocoding API could be a more cost-effective option than Place Details (Legacy) for your application, depending on the performance of your Place Autocomplete (Legacy) usage. Every application's Place Autocomplete (Legacy) efficiency varies depending on what users are entering, where the application is being used, and whether [performance optimization best practices](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#perf-best-practices) have been implemented.

In order to answer the following question, analyze how many characters a user types on average before selecting a Place Autocomplete (Legacy) prediction in your application.

**Do your users select a Place Autocomplete (Legacy) prediction in four or fewer requests, on average?**

### Yes

**Implement Place Autocomplete (Legacy) programmatically without session tokens and call Geocoding API on the selected place prediction.**  
Geocoding API delivers addresses and latitude/longitude coordinates.
Making four
[Autocomplete - Per Request](https://developers.google.com/maps/billing-and-pricing/sku-details#places_autocomplete-per-request-legacy-ess-sku)
requests plus a [Geocoding API](https://developers.google.com/maps/billing-and-pricing/sku-details#geocoding)
call about the selected place prediction is less than the per-session Place Autocomplete (Legacy)
cost per session.[1](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#fn1)

Consider employing [performance best practices](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#perf-best-practices) to help your users get the prediction they're looking for in even fewer characters.

### No

**Use session-based Place Autocomplete (Legacy) with Place Details (Legacy).**  
Since the average number of requests you expect to make before a user selects a
Place Autocomplete (Legacy) prediction exceeds the cost of per-session pricing, your implementation
of Place Autocomplete (Legacy) should use a session token for both the Place Autocomplete (Legacy) requests
and the associated Place Details (Legacy) request
[per session](https://developers.google.com/maps/billing-and-pricing/sku-details#about-autocomplete-sessions).
[1](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#fn1)

**Widget implementation**  
Session management is automatically built into the
[JavaScript](https://developers.google.com/maps/documentation/javascript/places-autocomplete#add-autocomplete),
[Android](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#add_an_autocomplete_widget),
or [iOS](https://developers.google.com/maps/documentation/places/ios-sdk/autocomplete#adding_an_autocomplete_ui_control)
widgets. This includes both the Place Autocomplete (Legacy) requests and the Place Details (Legacy)
request on the selected prediction. Be sure to specify the `fields` parameter
in order to ensure you are only requesting the fields you need.

**Programmatic implementation**  
Use a
[session token](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#sessiontoken)
with your Place Autocomplete (Legacy) requests.
When requesting Place Details (Legacy) about the selected prediction,
include the following parameters:

1. The place ID from [the Place Autocomplete (Legacy) response](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#programmatic-response)
2. The session token used in the Place Autocomplete (Legacy) request
3. The `fields` parameter specifying
   [Basic Data](https://developers.google.com/maps/billing-and-pricing/sku-details#data-skus) fields
   such as address and geometry

**Consider delaying Place Autocomplete (Legacy) requests**  
You can employ strategies such as delaying a Place Autocomplete (Legacy) request until the user has typed in the first three or four characters so that your application makes fewer requests. For example, making Place Autocomplete (Legacy) requests for each character *after* the user has typed the third character means that if the user types seven characters then selects a prediction for which you make one Geocoding API request, the total cost would be for 4 Place Autocomplete (Legacy) Per Request + Geocoding.[1](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#fn1)

If delaying requests can get your average programmatic request below four, you can follow the guidance for [performant Place Autocomplete (Legacy) with Geocoding API](https://developers.google.com/maps/documentation/places/android-sdk/legacy/autocomplete?tab=Yes#select-location-only) implementation. Note that delaying requests can be perceived as latency by the user who might be expecting to see predictions with every new keystroke.

Consider employing [performance best practices](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#perf-best-practices) to help your users get the prediction they're looking for in fewer characters.

---

1. For costs, see [Google Maps Platform pricing lists](https://developers.google.com/maps/billing-and-pricing/pricing).



### Performance best practices

The following guidelines describe ways to optimize Place Autocomplete (Legacy) performance:

* Add country restrictions,
  [location biasing](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#location_biasing),
  and (for programmatic implementations) language preference to your Place Autocomplete (Legacy)
  implementation. Language preference is not needed
  with widgets since they pick language preferences from the user's browser or mobile device.
* If Place Autocomplete (Legacy) is accompanied by a map, you can bias location by map viewport.
* In situations when a user does not choose one of the Place Autocomplete (Legacy) predictions, generally
  because none of those predictions are the result-address wanted, you can reuse the original
  user input to attempt to get more relevant results:
  + If you expect the user to enter only address information, reuse the original user input
    in a call to the [Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview).
  + If you expect the user to enter queries for a specific place by name or address,
    use a Place Details (Legacy) request. If results are only expected in a specific region, use [location biasing](https://developers.google.com/maps/documentation/places/android-sdk/autocomplete#location_biasing).Other scenarios when it's best to fall back to the Geocoding API include:
  + Users inputting subpremise addresses, such as addresses for specific units or apartments
    within a building. For example, the Czech address "Stroupežnického 3191/17, Praha"
    yields a partial prediction in Place Autocomplete (Legacy).
  + Users inputting addresses with road-segment prefixes like "23-30 29th St, Queens" in
    New York City or "47-380 Kamehameha Hwy, Kaneohe" on the island of Kauai in Hawai'i.

### Location biasing

Bias results to a specified area by passing a `location` parameter and a `radius`
parameter. This instructs Place Autocomplete (Legacy) to *prefer* showing results
within the defined area. Results outside of the defined area may still be
displayed. You can use the `includedRegionCodes` parameter to filter results
to show only those places within a specified country.

**Warning:** If `radius` is not provided, the `location` parameter is ignored.
 Establishment results generally don't rank highly
enough to show in results when the search area is large. If you want
establishments to appear in mixed establishment/geocode results, you can
specify a smaller radius. Alternatively, use `types=establishment`
to restrict results to establishments only.


### Location restricting

Restrict results to a specified area by passing a `locationRestriction` parameter.

You may also restrict results to the region defined by `location`
and a `radius` parameter, by adding the
`strictbounds`
parameter. This instructs Place Autocomplete (Legacy) to return *only*
results within that region.

**Note:** Location restrictions are only applied to entire routes.
Synthetic results located outside the location restriction may be returned based on a route that
overlaps with the location restriction.


## Troubleshooting

Although a wide variety of errors can occur, the majority of the errors your app
is likely to experience are usually caused by configuration errors (for example,
the wrong API key was used, or the API key was configured incorrectly), or quota
errors (your app has exceeded its quota). See [Usage
Limits](https://developers.google.com/maps/documentation/places/android-sdk/usage-and-billing) for more
information about quotas.

Errors that occur in the use of the autocomplete controls are returned in the
`onActivityResult()` callback. Call `Autocomplete.getStatus()` to get the status
message for the result.
