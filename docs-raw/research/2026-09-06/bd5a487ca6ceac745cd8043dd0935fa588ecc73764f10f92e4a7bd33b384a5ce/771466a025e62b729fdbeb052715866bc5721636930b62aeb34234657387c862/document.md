# Get Started

## Introduction

Using Maps URLs, you can build a universal, cross-platform URL to launch
[Google Maps](https://www.google.com/maps/@?api=1&map_action=map) and
perform searches, get directions and navigation, and display map views and panoramic images.
The URL syntax is the same regardless of the platform in use.

You don't need a Google API key to use Maps URLs.

## Universal cross-platform syntax

As a developer of an Android app, an iOS app, or a website, you can construct a common URL,
and it will open Google Maps and perform the requested action, no matter the platform in
use when the map is opened.

* On an Android device:
  + If [Google Maps app for Android](https://play.google.com/store/apps/details?id=com.google.android.apps.maps) is installed and active, the URL launches
    Google Maps in the Maps app and performs the requested action.
  + If the Google Maps app is not installed or is disabled, the URL launches
    Google Maps in a browser and performs the requested action.
* On an iOS device:
  + If [Google Maps app for iOS](https://itunes.apple.com/app/id585027354)
    is installed, the URL launches Google Maps in the Maps app and performs
    the requested action.
  + If the Google Maps app is not installed, the URL launches
    Google Maps in a browser and performs the requested action.
* On any other device, the URL launches Google Maps in a browser and
  performs the requested action.

It is recommended that you use a cross-platform URL to launch Google Maps from your app
or website, since these universal URLs allow for broader handling of the maps requests
no matter the platform in use. For features that may only be functional on a mobile
platform (for example, turn-by-turn navigation), you may prefer to use a platform-specific
option for Android or iOS. See the following documentation:

* [Google Maps Intents for Android](https://developer.android.com/guide/components/google-maps-intents) — specifically to launch the
  [Google Maps app for Android](https://play.google.com/store/apps/details?id=com.google.android.apps.maps)
* [Google Maps URL Scheme for iOS](https://developers.google.com/maps/documentation/urls/ios-urlscheme) — specifically to launch the
  [Google Maps app for iOS](https://itunes.apple.com/app/id585027354)

## Launching Google Maps and performing a specific action

To launch Google Maps and optionally perform one of the supported functions,
use a URL scheme of one of the following forms, depending on the action requested:

* [**Search**](https://developers.google.com/maps/documentation/urls/guide#search-action)
  — launch a Google Map that displays a pin for a specific place, or perform
  a general search and launch a map to display the results:  
  `https://www.google.com/maps/search/?api=1&parameters`
* [**Directions**](https://developers.google.com/maps/documentation/urls/guide#directions-action)
  — request directions and launch Google Maps with the results:  
  `https://www.google.com/maps/dir/?api=1&parameters`
* [**Display a map**](https://developers.google.com/maps/documentation/urls/guide#map-action)
  — launch Google Maps with no markers or directions:  
  `https://www.google.com/maps/@?api=1&map_action=map&parameters`
* [**Display a Street View panorama**](https://developers.google.com/maps/documentation/urls/guide#street-view-action)
  — launch an interactive panorama image:  
  `https://www.google.com/maps/@?api=1&map_action=pano&parameters`

**Important**: The parameter `api=1` identifies the version of
Maps URLs this URL is intended for. This parameter is required in every
request. The only valid value is 1. If `api=1` is *NOT* present in the URL,
all parameters are ignored and the default Google Maps app will launch, either
in a browser or the Google Maps mobile app, depending on the platform in use
(for example, <https://www.google.com/maps>).

### Constructing valid URLs

You must [properly encode](https://developers.google.com/maps/url-encoding) URLs.

**Note**: For easier reading, this document uses unencoded URLs.
You should use your platform's standard URL libraries to encode them.

For example, some parameters use a pipe character
(`|`) as a separator, which you must encode as `%7C`
in the final URL. Other parameters use comma-separated values, such as latitude/longitude
coordinates or City, State. You must encode the comma as `%2C`. Encode spaces with
`%20`, or replace them with a plus sign (`+`).

Additionally, URLs are limited to 2,048 characters for each request. Be aware of this limit
when constructing your URLs.

## Map actions

The map actions available are: search, directions, display a map, and display
a Street View panorama. You specify the action in the request URL, along with required
and optional parameters. As is standard in URLs, you separate parameters using the ampersand
(`&`) character. For each action, the list of parameters and their possible
values are enumerated in the [Search Parameters](https://developers.google.com/maps/documentation/urls/guide#search-parameters) section.

### Search

The search action displays results for a search across the visible map region. When searching
for a specific place, the resulting map puts a pin in the specified location and displays
available place details.

#### Forming the Search URL

`https://www.google.com/maps/search/?api=1&parameters`


#### Parameters

* **`query`** (required): Defines the place(s) to highlight
  on the map. The query parameter is required for all search requests.
  + Specify locations as either a place name, address, or comma-separated
    latitude/longitude coordinates. Strings should be
    [URL-encoded](https://developers.google.com/maps/url-encoding), so an address
    such as "City Hall, New York, NY" should be converted to
    `City+Hall%2C+New+York%2C+NY`.
  + Specify general search terms as a
    [URL-encoded](https://developers.google.com/maps/url-encoding) string, such as
    `grocery+stores` or `restaurants+in+seattle+wa`.
* **`query_place_id`** (optional):
  A [place ID](https://developers.google.com/maps/documentation/places/web-service/place-id) is a
  textual identifier that uniquely identifies a place. For the `search` action,
  you must specify a `query`, but you may also specify a
  `query_place_id`. If you specify both parameters, the `query` is only
  used if Google Maps cannot find the place ID. If you are trying to definitively link to a
  specific establishment, the place ID is the best guarantee that you will link to the
  right place. It is also recommended to submit a `query_place_id` when you
  query for a specific location using latitude/longitude coordinates.

#### Search examples

**Location search**

In a location search, you search for a specific location using a place name, address, or
comma-separated latitude/longitude coordinates, and the resulting map displays a pin at
that location. These three examples illustrate searches for the same location using different location values.

Example 1: Searching for the place name "Lumen Field" results in the following map:

`https://www.google.com/maps/search/?api=1&query=lumen+field`

![Map of Lumen Field](/static/maps/documentation/urls/images/search-place-lumenfield.png)

Example 2: Searching for Lumen Field using only
latitude/longitude coordinates results in the following map. Notice that there is a pin in
the map, but no additional place information is provided on the map or in the side panel:

`https://www.google.com/maps/search/?api=1&query=47.5951518%2C-122.3316393`

![](/static/maps/documentation/urls/images/search-latlng-only-lumenfield.png)

Example 3: Searching for Lumen Field using
latitude/longitude coordinates as well as the place ID results in the following map:

`https://www.google.com/maps/search/?api=1&query=47.5951518%2C-122.3316393&query_place_id=ChIJKxjxuaNqkFQR3CK6O1HNNqY`

![](/static/maps/documentation/urls/images/search-place-lumenfield.png)

Example 4: Searching for the place name "Starbucks" results in the following map:

`https://www.google.com/maps/search/?api=1&query=starbucks`

![Search results for Starbucks](/static/maps/documentation/urls/images/search-starbucks.png)

Example 5: Searching for a specific Starbucks using place name and place ID results in the following map:

`https://www.google.com/maps/search/?api=1&query=starbucks&query_place_id=ChIJsU30zM1qkFQRbnOm1_LBoG0`

![](/static/maps/documentation/urls/images/search-starbucks-placeid.png)

When your goal is to display a specific place’s details, construct the Search URLs using one of the following recommended formats:

* `query=PLACE_NAME,ADDRESS`
* `query=PLACE_NAME&query_place_id=PLACE_ID`

To programmatically retrieve Place IDs, you can use the [Places API: Text Search(ID Only)](https://developers.google.com/maps/documentation/places/web-service/usage-and-billing#id-textsearch) features.
This is a non-cost method for obtaining Place IDs. Learn more about [Place ID](https://developers.google.com/maps/documentation/places/web-service/place-id), and [Place API(New) request](https://developers.google.com/maps/documentation/places/web-service/op-overview).

Place IDs can also be retrieved when a user clicks or taps a POI on maps. Find out more details about clickable POI icons
([JavaScript](https://developers.google.com/maps/documentation/javascript/reference/map#MapOptions.clickableIcons),
[Android](https://developers.google.com/android/reference/com/google/android/gms/maps/GoogleMap.OnPoiClickListener),
[iOS](https://developers.google.com/maps/documentation/ios-sdk/reference/objc/Protocols/GMSMapViewDelegate#-mapview:didtappoiwithplaceid:name:location:))

**Categorical search**

In a categorical search, you pass a general search term, and Google Maps
attempts to find listings that match your criteria near the location you specify.
If no location is specified, Google Maps attempts to find listings nearby
your current location. If you prefer to provide a location for a categorical search,
include the location in the general search string
(for example, `pizza+seattle+wa`).

In this example, a search for pizza restaurants in Seattle, WA, results in the following
map:

`https://www.google.com/maps/search/?api=1&query=pizza+seattle+wa`

![](/static/maps/documentation/urls/images/search-pizza-seattle-new.png)

---



### Directions

Directions action displays the path between two or more specified points on the map, as
well as the distance and travel time.

#### Forming the Directions URL

`https://www.google.com/maps/dir/?api=1&parameters`


#### Parameters

* **`origin`**: Defines the starting point from which
  to display directions. Defaults to most relevant starting location, such as device location,
  if available. If none, the resulting map may provide a blank form to allow a user to enter
  the origin. The value can be either a place name, address, or comma-separated
  latitude/longitude coordinates. A string should be
  [URL-encoded](https://developers.google.com/maps/url-encoding), so an address such as
  "City Hall, New York, NY" should be converted to `City+Hall%2C+New+York%2C+NY`.

  **Note**: This parameter is optional, unless you specify an
  `origin_place_id` in your URL. If you choose to specify an
  `origin_place_id`, you must also include an `origin` in the
  URL.
* **`origin_place_id`** (optional):
  A [place ID](https://developers.google.com/maps/documentation/places/web-service/place-id) is a
  textual identifier that uniquely identifies a place. If you are trying
  to definitively specify an establishment, using a place ID is the best guarantee
  that you will link to the right place. URLs that use this parameter must also include an
  `origin`.
* **`destination`**: Defines the endpoint of the directions. If
  none, the resulting map may provide a blank form to allow the user to
  enter the destination. The value can be either a place name, address, or comma-separated
  latitude/longitude coordinates. A string should be
  [URL-encoded](https://developers.google.com/maps/documentation/urls/url-encoding), so an address such as
  "City Hall, New York, NY" should be converted to `City+Hall%2C+New+York%2C+NY`.

  **Note**: This parameter is optional, unless you specify a
  `destination_place_id` in your URL. If you choose to specify a
  `destination_place_id`, you must also include a `destination` in the
  URL.
* **`destination_place_id`** (optional):
  A [place ID](https://developers.google.com/maps/documentation/places/web-service/place-id) is a
  textual identifier that uniquely identifies a place. If you are trying
  to definitively specify an establishment, using a place ID is the best guarantee
  that you will link to the right place. URLs that use this parameter must also include a
  `destination`.
* **`travelmode`** (optional):
  Defines the method of travel. Here's the list of options:

+ `driving`
+ `walking`: Prefers pedestrian paths and sidewalks, where available.
+ `bicycling`: Routes through bike paths, where available. "Bicycling" refers to human-powered
  travel mode.
+ `two-wheeler`: Routes through preferred streets for two-wheelers, where available.
  "Two-wheeler" refers to two-wheeled motorized vehicles, such as motorcycles. For more information, see
  [Two-wheeler coverage](https://developers.google.com/maps/documentation/routes/coverage-two-wheeled).
+ `transit`

If no `travelmode` is specified, the Google Map shows
one or more of the most relevant modes for the specified route and/or user preferences.* **`dir_action=navigate`** (optional): Launches either turn-by-turn
  navigation or route preview to the specified destination, based on whether the origin is
  available. If the user specifies an origin and it is not close to the user's current
  location, or the current device location is unavailable, the map launches a route preview.
  If the user does not specify an origin (in which case the origin defaults to the
  current device location), or the origin is close to the user's current
  location, the map launches turn-by-turn navigation. Note that navigation is not available
  on all Google Maps products and/or between all destinations; in those cases this
  parameter will be ignored.
* **`waypoints`**: Specifies one or more intermediary places to
  route directions through between the `origin` and
  `destination`. Multiple waypoints can be specified by using the pipe
  character (`|`) to separate places (for example,
  `Berlin,Germany|Paris,France`). The number of waypoints allowed varies by
  the platform where the link opens, with up to three waypoints supported on mobile
  browsers, and a maximum of nine waypoints supported otherwise.
  Waypoints are displayed on the map in the same order they are listed in the URL.
  Each waypoint can be either a place name, address, or comma-separated latitude/longitude
  coordinates. Strings should be [URL-encoded](https://developers.google.com/maps/documentation/urls/url-encoding), so waypoints such as "Berlin,Germany|Paris,France" should be converted to
  `Berlin%2CGermany%7CParis%2CFrance`.

  **Notes**:

  + Waypoints are not supported on all Google Maps products; in those cases
    this parameter will be ignored.
  + This parameter is optional, unless you specify `waypoint_place_ids` in
    your URL. If you choose to specify `waypoint_place_ids`, you must also
    include `waypoints` in the URL.
* **`waypoint_place_ids`** (optional):
  A [place ID](https://developers.google.com/maps/documentation/places/web-service/place-id) is a
  textual identifier that uniquely identifies a place. `Waypoint_place_ids`
  allows you to provide a list of place IDs to match the list of `waypoints`.
  Place IDs should be listed in the same order as the waypoints, and separated using the
  pipe character "`|`" ([URL-encoded](https://developers.google.com/maps/documentation/urls/url-encoding) as `%7C`). If you are trying to definitively specify certain
  establishments, place IDs are the best guarantee that you will link to the right places.
  URLs that use this parameter must also include `waypoints`.
* **`avoid`** (optional):
  Sets features that route should try to avoid. It can be set to one or more of these options, separated by a comma character "`,`"
  ( [URL-encoded](https://developers.google.com/maps/documentation/urls/url-encoding) as
  `%2C`):
  + `ferries`
  + `highways`
  + `tolls`

#### Directions examples

The following URL launches a map in directions mode and provides a form to allow the user
to enter the origin and destination.

`https://www.google.com/maps/dir/?api=1`

![Map for origin to destination](/static/maps/documentation/urls/images/dir-no-params.png)

The following example launches a map with bicycling directions
from the Space Needle to Pike Place Market, in Seattle, WA.

`https://www.google.com/maps/dir/?api=1&origin=Space+Needle+Seattle+WA&destination=Pike+Place+Market+Seattle+WA&travelmode=bicycling`

![Map for Seattle destination](/static/maps/documentation/urls/images/dir-bicycling-seattle.png)

The following example launches a map with two-wheeler directions
from Google Mumbai to the Mumbai International Airport.

**Note**: The following example for a two-wheeler link works
only if you're physically located in the country that supports two-wheelers. This link
works in countries where two-wheelers are supported, see [Two-wheeler coverage.](https://developers.google.com/maps/documentation/routes/coverage-two-wheeled).

`https://www.google.com/maps/dir/?api=1&origin=Google+Mumbai+India&destination=Mumbai+Airport&travelmode=two-wheeler`

![Map for Mumbai International Airport destination](/static/maps/documentation/urls/images/dir-two-wheeler.png)

The following example launches a map with walking directions
from Google Sydney, Australia to the Queen Victoria Building.

`https://www.google.com/maps/dir/?api=1&origin=Google+Pyrmont+NSW&destination=QVB&destination_place_id=ChIJISz8NjyuEmsRFTQ9Iw7Ear8&travelmode=walking`

![Map for Queen Victoria Building destination](/static/maps/documentation/urls/images/dir-walking-sydney.png)

### Displaying a map

The map action returns a map with no markers or directions.

#### Forming the map URL

`https://www.google.com/maps/@?api=1&map_action=map&parameters`


#### Parameters

* **`map_action=map`** (required): Specifies the type of map view
  to display. Maps and Street View share the same endpoint. To ensure a map is displayed,
  the `map_action` must be specified as `map`.
* **`center`** (optional): Defines the center of the map window,
  and accepts latitude/longitude coordinates as comma-separated values
  (for example, `-33.8569,151.2152`).
* **`zoom`** (optional): Sets the initial zoom level of the map.
  Accepted values are whole integers ranging from 0 (the whole world) to 21 (individual
  buildings). The upper limit can vary depending on the map data available at the selected
  location. The default is 15.
* **`basemap`** (optional): Defines the type of map to display.
  The value can be either `roadmap` (default), `satellite`, or
  `terrain`.
* **`layer`** (optional): Defines an extra layer to display on
  the map, if any. The value can be one of the following: `none` (default),
  `transit`, `traffic`, or `bicycling`.

#### Map examples

This example URL launches a default Google Map, centered on the user’s current location.

`https://www.google.com/maps/@?api=1&map_action=map`

![](/static/maps/documentation/urls/images/map-no-params.png)

The following example displays a map centered on Katoomba, NSW,
Australia (at `-33.712206,150.311941`), and sets the optional `zoom`
and `basemap` parameters.

`https://www.google.com/maps/@?api=1&map_action=map&center=-33.712206%2C150.311941&zoom=12&basemap=terrain`

![](/static/maps/documentation/urls/images/map-terrain.png)

---



### Displaying a Street View panorama

The pano action lets you launch a viewer to display Street View images as interactive
panoramas. Each Street View panorama provides a full 360-degree view from a single location.
Images contain 360 degrees of horizontal view (a full wrap-around) and 180 degrees
of vertical view (from straight up to straight down). The pano action launches a viewer
that renders the resulting panorama as a sphere with a camera at its center. You can
manipulate the camera to control the zoom and the orientation of the camera.

Google Street View provides panoramic views from designated locations
throughout its
[coverage area](http://maps.google.com/help/maps/streetview/learn/where-is-street-view.html). [User
contributed Photospheres](https://www.google.com/maps/views/home) and
[Street View special collections](https://www.google.com/maps/views/streetview)
are also available.

#### Forming the Street View URL

`https://www.google.com/maps/@?api=1&map_action=pano&parameters`


#### Parameters

* **`map_action=pano`** (required): Specifies the type of view to
  display. Maps and Street View share the same endpoint. To ensure a panorama is displayed,
  the `action` must be specified as `pano`.

One of the following URL parameters is also required:

* **`viewpoint`**: The viewer displays the panorama photographed
  closest to the `viewpoint` location, specified as comma-separated
  latitude/longitude coordinates (for example 46.414382,10.013988). Because Street View imagery
  is periodically refreshed, and photographs may be taken from slightly different positions
  each time, it's possible that your location may snap to a different panorama when imagery
  is updated.
* **`pano`**: The specific [panorama ID](https://developers.google.com/maps/documentation/urls/guide#pano-id)
  of the image to display. If you specify a `pano` you may also specify a
  `viewpoint`. The `viewpoint` is only used if Google Maps
  cannot find the panorama ID. If `pano` is specified but not found, and a
  `viewpoint` is *NOT* specified, no panorama image is displayed. Instead,
  Google Maps opens in default mode, displaying a map centered on the user's current
  location.

The following URL parameters are optional:

* **`heading`**: Indicates the compass heading of the camera
  in degrees clockwise from North. Accepted values are from -180 to 360 degrees. If
  omitted, a default heading is chosen based on the viewpoint (if specified) of the
  query and the actual location of the image.
* **`pitch`**: Specifies the angle, up or down, of the camera.
  The pitch is specified in degrees from -90 to 90. Positive values will angle the camera
  up, while negative values will angle the camera down. The default pitch of 0 is set
  based on on the position of the camera when the image was captured. Because of this,
  a pitch of 0 is often, but not always, horizontal. For example, an image taken on a
  hill will likely exhibit a default pitch that is not horizontal.
* **`fov`**: Determines the horizontal field of view of the image.
  The field of view is expressed in degrees, with a range of 10 - 100. It defaults to 90.
  When dealing with a fixed-size viewport, the field of view is considered the zoom level,
  with smaller numbers indicating a higher level of zoom.

#### Street View examples

The first two examples display a panorama of the Eiffel Tower. Example one
uses only a `viewpoint` for the location, and sets the optional
`heading`, `pitch`, and `fov` parameters. For comparison,
example two uses a `pano` ID as well as the same parameters set in the
first example. The third example displays an indoor panorama image.

Example 1: Uses only a `viewpoint` to specify location.

`https://www.google.com/maps/@?api=1&map_action=pano&viewpoint=48.857832%2C2.295226&heading=-45&pitch=38&fov=80`

![](/static/maps/documentation/urls/images/pano-eiffel-tower-latlng.png)

Example 2: Uses a `pano` ID as well as a `viewpoint` location.
The `pano` ID takes precedence over the `viewpoint`.
In this example, the panorama ID is found, so the `viewpoint` is ignored. Notice
that the panorama image that is displayed for the `pano` ID is slightly different,
and more recent, than the image found using only the `viewpoint`.

`https://www.google.com/maps/@?api=1&map_action=pano&pano=tu510ie_z4ptBZYo2BGEJg&viewpoint=48.857832%2C2.295226&heading=-45&pitch=38&fov=80`

![](/static/maps/documentation/urls/images/pano-eiffel-tower.png)

Example 3: Displays a panorama of the interior of
the Sarastro restaurant in London, UK, specified with a panorama ID.

`https://www.google.com/maps/@?api=1&map_action=pano&pano=4U-oRQCNsC6u7r8gp02sLA`

![](/static/maps/documentation/urls/images/pano-sarastro-restaurant.png)

#### Finding a panorama ID

To find the ID of a specific panorama image, there are multiple methods you can use.

* For JavaScript, use the
  [StreetViewPanorama](https://developers.google.com/maps/documentation/javascript/3.exp/reference#StreetViewPanorama) class.
* For Android, use the public class
  [StreetViewPanoramaLocation](https://developers.google.com/android/reference/com/google/android/gms/maps/model/StreetViewPanoramaLocation).
* For iOS, use the
  [GMSPanorama](https://developers.google.com/maps/documentation/ios-sdk/reference/interface_g_m_s_panorama) class.
* You may also make [metadata requests using the Google Street View Image API](https://developers.google.com/maps/documentation/streetview/metadata).
  Image metadata requests provide data about Street View panoramas, including the
  panorama ID.

## More examples

### Directions examples using waypoints

The following directions examples launch Google Maps and display driving
directions from Paris, France to Cherbourg, France, routing through the following waypoints:

| City, Country | Place Name | Place ID |
| --- | --- | --- |
| 1. Versailles, France | The Palace of Versailles | ChIJdUyx15R95kcRj85ZX8H8OAU |
| 2. Chartres, France | Chartres Cathedral | ChIJKzGHdEgM5EcR\_OBTT3nQoEA |
| 3. Le Mans, France | Cathedral of Saint Julian of Le Mans | ChIJG2LvQNCI4kcRKXNoAsPi1Mc |
| 4. Caen, France | Caen Castle | ChIJ06tnGbxCCkgRsfNjEQMwUsc |

In the example URLs, the waypoints are defined in different ways so you can compare the
differences in the display of the waypoints on the resulting maps.

Example 1: Waypoints defined as City, Country:

`https://www.google.com/maps/dir/?api=1&origin=Paris%2CFrance&destination=Cherbourg%2CFrance&travelmode=driving&waypoints=Versailles%2CFrance%7CChartres%2CFrance%7CLe+Mans%2CFrance%7CCaen%2CFrance`

![](/static/maps/documentation/urls/images/dir-waypoints-city.png)

Example 2: Waypoints defined as specific place names:

`https://www.google.com/maps/dir/?api=1&origin=Paris%2CFrance&destination=Cherbourg%2CFrance&travelmode=driving&waypoints=Palace+of+Versailles%7CChartres+Cathedral%7CCathedral+of+Saint+Julian+of+Le+Mans%7CCaen+Castle`

![](/static/maps/documentation/urls/images/dir-waypoints-placenames.png)

Example 3: Waypoints defined as City, Country, and also provides
`waypoint_place_ids` for a specific establishment in each waypoint:

`https://www.google.com/maps/dir/?api=1&origin=Paris%2CFrance&destination=Cherbourg%2CFrance&travelmode=driving&waypoints=Versailles%2CFrance%7CChartres%2CFrance%7CLe+Mans%2CFrance%7CCaen%2CFrance&waypoint_place_ids=ChIJdUyx15R95kcRj85ZX8H8OAU%7CChIJKzGHdEgM5EcR_OBTT3nQoEA%7CChIJG2LvQNCI4kcRKXNoAsPi1Mc%7CChIJ06tnGbxCCkgRsfNjEQMwUsc`

![](/static/maps/documentation/urls/images/dir-waypoints-city-and-waypoint-place-ids.png)

Example 4: Defines waypoints as City, Country, but lists the waypoints in a different order
compared to the previous examples. Demonstrates that the map displays waypoints in the order
they are listed in the URL.

`https://www.google.com/maps/dir/?api=1&origin=Paris%2CFrance&destination=Cherbourg%2CFrance&travelmode=driving&waypoints=Versailles%2CFrance%7CCaen%2CFrance%7CLe+Mans%2CFrance%7CChartres%2CFrance`

![](/static/maps/documentation/urls/images/dir-waypoints-city-diff-order.png)

### Map examples

Displays a map with a specified `basemap` (satellite) and
`layer` (transit).

`https://www.google.com/maps/@?api=1&map_action=map&center=37.7992940%2C-122.3976113&zoom=15&basemap=satellite&layer=transit`

![](/static/maps/documentation/urls/images/map-satellite-transit.png)

### Street View examples

Displays a Street View panorama using a FIFE image key as the `pano` ID. Note
that the `pano` ID is prefaced with **F:**.

`https://www.google.com/maps/@?api=1&map_action=pano&pano=F:-ud6AZSB-sQg/V0cfCSV3OWI/AAAAAAAAG1U/UQEoc5sXPQEIP7zzD6SWzmKb8Vbug47uQCLIB&heading=22&pitch=-5&fov=55`

![](/static/maps/documentation/urls/images/pano-fife-id.png)

## Improving Maps URLs with UTM parameters

To help Google better understand how developers are integrating Maps URLs and to ensure optimal performance,
we encourage you to include UTM tracking parameters in your URL construction. By adding **`utm_source`** and **`utm_campaign`** parameters,
you provide valuable data that allows us to analyze usage patterns and improve the Maps URLs product.

For the **`utm_source`** parameter, please use the name of your application. The **`utm_campaign`** parameter should reflect
the user's intended action, such as "location\_sharing," "place\_details\_search," or "directions\_request."

For example, a URL with UTM parameters might look like this:

`https://www.google.com/maps/search/?api=1&query=Sydney+Opera+House&query_place_id=ChIJ3S-JXmauEmsRUcIaWtf4MzE&utm_source=YOUR_APP_NAME&utm_campaign=place_details_search`
