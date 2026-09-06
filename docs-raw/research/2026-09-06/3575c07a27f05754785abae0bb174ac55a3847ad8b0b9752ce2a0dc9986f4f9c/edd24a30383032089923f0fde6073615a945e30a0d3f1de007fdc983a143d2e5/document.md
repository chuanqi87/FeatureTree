# FusedLocationProviderClient

public interface **FusedLocationProviderClient** implements [HasApiKey](https://developers.google.com/android/reference/com/google/android/gms/common/api/HasApiKey)<[Api.ApiOptions.NoOptions](https://developers.google.com/android/reference/com/google/android/gms/common/api/Api.ApiOptions.NoOptions)>



The main entry point for interacting with the Fused Location Provider (FLP). In order to
obtain an instance of this class, see `LocationServices`.

In order to use most location APIs, clients are required to hold either the `Manifest.permission.ACCESS_COARSE_LOCATION`
permission or the `Manifest.permission.ACCESS_FINE_LOCATION`.
Clients holding only the [coarse permission](https://developer.android.com/training/location/permissions#accuracy) will
receive locations that have been obfuscated to hide the device's exact location, and only
reveal the approximate area of the device. In addition, clients with only the coarse
permission will receive location updates at a throttled rate to avoid wasting power to derive
approximate locations. Applications which do not require exact location to work properly
(such as a weather app potentially) are encouraged to request only the coarse location
permission. From Android 12 onwards, the user may force any app to use coarse location even
if it has requested fine location, so apps should carefully test their behavior with only the
coarse location permission to ensure their functionality works as expected.

If clients have only the coarse or fine location permission, they will not receive
locations while they are in the background. Whether an app is in the background or foreground
is normally determined by whether it is currently showing any UI to the user. Apps may also
use a [foreground
location service](https://developer.android.com/guide/components/foreground-services) to maintain their foreground status when they would normally be in the
background.

If clients also hold the `Manifest.permission.ACCESS_BACKGROUND_LOCATION` permission, they may receive
locations while in the background even if the above conditions are not met.

There are several types of use cases for location. One of the most common is simply
obtaining a single location in order to determine where the device is now, and continue from
there. The `getCurrentLocation(CurrentLocationRequest, CancellationToken)` API is designed with
exactly this use case in mind. On the other hand, if repeated location updates are required,
such as when tracking the user's location over time, `requestLocationUpdates(LocationRequest, Executor, LocationListener)` or one of its
variants is better suited. Clients are encourage to familiarize themselves with the full
range of APIs available in this class to understand which is best suited for their needs.

### Constant Summary

|  |  |  |
| --- | --- | --- |
| [String](https://developer.android.com/reference/java/lang/String.html) | [KEY\_MOCK\_LOCATION](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#KEY_MOCK_LOCATION) | *This constant is deprecated. Use `Location.isMock()` on Android S and above, otherwise use [LocationCompat.isMock()](https://developer.android.com/reference/androidx/core/location/LocationCompat#isMock(android.location.Location)) from the compat libraries instead.* |
| [String](https://developer.android.com/reference/java/lang/String.html) | [KEY\_VERTICAL\_ACCURACY](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#KEY_VERTICAL_ACCURACY) | *This constant is deprecated. Use `Location.getVerticalAccuracyMeters()` on Android O and above, otherwise use [LocationCompat.getVerticalAccuracyMeters()](https://developer.android.com/reference/androidx/core/location/LocationCompat#getVerticalAccuracyMeters(android.location.Location)) from the compat libraries instead.* |

### Public Method Summary

|  |  |
| --- | --- |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [flushLocations](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#flushLocations())() Flushes any locations currently being batched and sends them to all registered `LocationListener`s, `LocationCallback`s, and `PendingIntent`s. |
| abstract Task<[Location](https://developer.android.com/reference/android/location/Location.html)> | [getCurrentLocation](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#getCurrentLocation(int,%20com.google.android.gms.tasks.CancellationToken))(int priority, CancellationToken cancellationToken) Returns a single location fix representing the best estimate of the current location of the device. |
| abstract Task<[Location](https://developer.android.com/reference/android/location/Location.html)> | [getCurrentLocation](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#getCurrentLocation(com.google.android.gms.location.CurrentLocationRequest,%20com.google.android.gms.tasks.CancellationToken))([CurrentLocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/CurrentLocationRequest) request, CancellationToken cancellationToken) Returns a single location fix representing the best estimate of the current location of the device. |
| abstract Task<[Location](https://developer.android.com/reference/android/location/Location.html)> | [getLastLocation](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#getLastLocation(com.google.android.gms.location.LastLocationRequest))([LastLocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/LastLocationRequest) request) Returns the most recent cached location from the past currently available. |
| abstract Task<[Location](https://developer.android.com/reference/android/location/Location.html)> | [getLastLocation](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#getLastLocation())() Returns the most recent cached location from the past currently available. |
| abstract Task<[LocationAvailability](https://developers.google.com/android/reference/com/google/android/gms/location/LocationAvailability)> | [getLocationAvailability](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#getLocationAvailability())() Returns the estimated availability of location data. |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [removeDeviceOrientationUpdates](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#removeDeviceOrientationUpdates(com.google.android.gms.location.DeviceOrientationListener))([DeviceOrientationListener](https://developers.google.com/android/reference/com/google/android/gms/location/DeviceOrientationListener) listener) *This method is deprecated. Use `FusedOrientationProviderClient.removeOrientationUpdates(DeviceOrientationListener)` instead.* |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [removeLocationUpdates](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#removeLocationUpdates(com.google.android.gms.location.LocationListener))([LocationListener](https://developers.google.com/android/reference/com/google/android/gms/location/LocationListener) listener) Removes all location updates for the given listener. |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [removeLocationUpdates](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#removeLocationUpdates(com.google.android.gms.location.LocationCallback))([LocationCallback](https://developers.google.com/android/reference/com/google/android/gms/location/LocationCallback) callback) Removes all location updates for the given callback. |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [removeLocationUpdates](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#removeLocationUpdates(android.app.PendingIntent))([PendingIntent](https://developer.android.com/reference/android/app/PendingIntent.html) pendingIntent) Removes all location updates for the given pending intent. |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [requestDeviceOrientationUpdates](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#requestDeviceOrientationUpdates(com.google.android.gms.location.DeviceOrientationRequest,%20java.util.concurrent.Executor,%20com.google.android.gms.location.DeviceOrientationListener))([DeviceOrientationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/DeviceOrientationRequest) request, [Executor](https://developer.android.com/reference/java/util/concurrent/Executor.html) executor, [DeviceOrientationListener](https://developers.google.com/android/reference/com/google/android/gms/location/DeviceOrientationListener) listener) *This method is deprecated. Use `FusedOrientationProviderClient.requestOrientationUpdates(DeviceOrientationRequest, Executor, DeviceOrientationListener)` instead.* |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [requestDeviceOrientationUpdates](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#requestDeviceOrientationUpdates(com.google.android.gms.location.DeviceOrientationRequest,%20com.google.android.gms.location.DeviceOrientationListener,%20android.os.Looper))([DeviceOrientationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/DeviceOrientationRequest) request, [DeviceOrientationListener](https://developers.google.com/android/reference/com/google/android/gms/location/DeviceOrientationListener) listener, [Looper](https://developer.android.com/reference/android/os/Looper.html) looper) *This method is deprecated. Use `FusedOrientationProviderClient.requestOrientationUpdates(DeviceOrientationRequest, Executor, DeviceOrientationListener)` instead.* |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [requestLocationUpdates](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#requestLocationUpdates(com.google.android.gms.location.LocationRequest,%20com.google.android.gms.location.LocationListener,%20android.os.Looper))([LocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest) request, [LocationListener](https://developers.google.com/android/reference/com/google/android/gms/location/LocationListener) listener, [Looper](https://developer.android.com/reference/android/os/Looper.html) looper) Requests location updates with the given request and results delivered to the given listener on the specified `Looper`. |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [requestLocationUpdates](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#requestLocationUpdates(com.google.android.gms.location.LocationRequest,%20java.util.concurrent.Executor,%20com.google.android.gms.location.LocationCallback))([LocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest) request, [Executor](https://developer.android.com/reference/java/util/concurrent/Executor.html) executor, [LocationCallback](https://developers.google.com/android/reference/com/google/android/gms/location/LocationCallback) callback) Requests location updates with the given request and results delivered to the given callback on the specified `Executor`. |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [requestLocationUpdates](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#requestLocationUpdates(com.google.android.gms.location.LocationRequest,%20java.util.concurrent.Executor,%20com.google.android.gms.location.LocationListener))([LocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest) request, [Executor](https://developer.android.com/reference/java/util/concurrent/Executor.html) executor, [LocationListener](https://developers.google.com/android/reference/com/google/android/gms/location/LocationListener) listener) Requests location updates with the given request and results delivered to the given listener on the specified `Executor`. |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [requestLocationUpdates](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#requestLocationUpdates(com.google.android.gms.location.LocationRequest,%20com.google.android.gms.location.LocationCallback,%20android.os.Looper))([LocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest) request, [LocationCallback](https://developers.google.com/android/reference/com/google/android/gms/location/LocationCallback) callback, [Looper](https://developer.android.com/reference/android/os/Looper.html) looper) Requests location updates with the given request and results delivered to the given callback on the specified `Looper`. |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [requestLocationUpdates](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#requestLocationUpdates(com.google.android.gms.location.LocationRequest,%20android.app.PendingIntent))([LocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest) request, [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent.html) pendingIntent) Requests location updates with the given request and results delivered via the specified `PendingIntent`. |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [setMockLocation](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#setMockLocation(android.location.Location))([Location](https://developer.android.com/reference/android/location/Location.html) location) Sets the mock location of the Fused Location Provider. |
| abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> | [setMockMode](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#setMockMode(boolean))(boolean mockMode) Sets whether or not the Fused Location Provider is in mock mode. |








## Constants

#### public static final [String](https://developer.android.com/reference/java/lang/String.html) **KEY\_MOCK\_LOCATION**

**This constant is deprecated.**  
Use `Location.isMock()`
on Android S and above, otherwise use [LocationCompat.isMock()](https://developer.android.com/reference/androidx/core/location/LocationCompat#isMock(android.location.Location)) from the compat libraries instead.

Key used for the Bundle extra in `Location`
object indicating whether this is a mock location.

Constant Value:
"mockLocation"

#### public static final [String](https://developer.android.com/reference/java/lang/String.html) **KEY\_VERTICAL\_ACCURACY**

**This constant is deprecated.**  
Use `Location.getVerticalAccuracyMeters()` on Android O and above, otherwise use
[LocationCompat.getVerticalAccuracyMeters()](https://developer.android.com/reference/androidx/core/location/LocationCompat#getVerticalAccuracyMeters(android.location.Location)) from the compat libraries instead.

Key used for the Bundle extra in `Location`
object holding a float indicating the estimated vertical accuracy of the location, in
meters.

Constant Value:
"verticalAccuracy"








## Public Methods

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **flushLocations** ()

Flushes any locations currently being batched and sends them to all registered
`LocationListener`s,
`LocationCallback`s,
and `PendingIntent`s.
This call is only useful when batching is specified using `LocationRequest.setMaxWaitTime(long)`, otherwise locations are already
delivered immediately when available.

#### public abstract Task<[Location](https://developer.android.com/reference/android/location/Location.html)> **getCurrentLocation** (int priority, CancellationToken cancellationToken)

Returns a single location fix representing the best estimate of the current location
of the device. This may return a cached location if a recent enough location fix
exists, or may compute a fresh location. If unable to retrieve a current location fix
before timing out, null will be returned.

The behavior of this method can be modified in important ways through various
parameters of `CurrentLocationRequest`,
and clients are encouraged to familiarize themselves with `CurrentLocationRequest`
and the `getCurrentLocation(CurrentLocationRequest, CancellationToken)` overload.

See `getCurrentLocation(CurrentLocationRequest, CancellationToken)` for more
documentation.

#### public abstract Task<[Location](https://developer.android.com/reference/android/location/Location.html)> **getCurrentLocation** ([CurrentLocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/CurrentLocationRequest) request, CancellationToken cancellationToken)

Returns a single location fix representing the best estimate of the current location
of the device. This may return a cached location if a recent enough location fix
exists, or may compute a fresh location. If unable to retrieve a current location fix
before timing out, null will be returned.

Clients may supply an optional `CancellationToken`
which may be used to cancel the request.

This API has the same [background
location limits](https://developer.android.com/about/versions/oreo/background-location-limits) that apply to `requestLocationUpdates(LocationRequest, PendingIntent)` and all location
APIs, so clients may note that this API fails to return a location more often when
invoked from the background. Clients that need reliable background access to location
can use the techniques mentioned in the above link, such as using a foreground location
service to call this API.

There are many parameters of `CurrentLocationRequest`
that can substantially affect the latency and behavior of this API - in particular,
clients are encouraged to select a `CurrentLocationRequest.getMaxUpdateAgeMillis()` that best suits their needs,
and to review all parameters of the request to familiarize themselves with the
options.

#### public abstract Task<[Location](https://developer.android.com/reference/android/location/Location.html)> **getLastLocation** ([LastLocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/LastLocationRequest) request)

Returns the most recent cached location from the past currently available. Will
return null if no such cached location is available. The returned location may be of an
arbitrary age, so clients should check how old the location is to see if it suits their
purposes.

See `getLastLocation()` for more documentation.

#### public abstract Task<[Location](https://developer.android.com/reference/android/location/Location.html)> **getLastLocation** ()

Returns the most recent cached location from the past currently available. Will
return null if no such cached location is available. The returned location may be of an
arbitrary age, so clients should check how old the location is to see if it suits their
purposes.

Since this method simply checks caches for pre-computed locations it is generally
cheap and quick to return.

However, clients should still avoid calling this method in a tight loop or otherwise
wasting system resources. If a client wishes to be informed of new locations passively,
registering a location request with `Priority.PRIORITY_PASSIVE`
through `requestLocationUpdates(LocationRequest, Executor, LocationListener)` or
similar APIs is far more efficient than calling this method over and over
indefinitely.

If a client needs the current location of the device and is checking to see if a
cached location is recent enough to be useful, but will need to calculate a new
location otherwise, clients are recommended to use `getCurrentLocation(CurrentLocationRequest, CancellationToken)` which can take
advantage of a cached location or calculate a new location if necessary in a single
method call.

#### public abstract Task<[LocationAvailability](https://developers.google.com/android/reference/com/google/android/gms/location/LocationAvailability)> **getLocationAvailability** ()

Returns the estimated availability of location data. If `LocationAvailability.isLocationAvailable()` returns true then it is likely
(but not guaranteed) that Fused Location Provider APIs will be able to derive and
return fresh location updates. If `LocationAvailability.isLocationAvailable()` returns false, then it is likely
(but not guaranteed) that Fused Location Provider APIs will be unable to derive and
return fresh location updates, though there may be cached locations available.

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **removeDeviceOrientationUpdates** ([DeviceOrientationListener](https://developers.google.com/android/reference/com/google/android/gms/location/DeviceOrientationListener) listener)

**This method is deprecated.**  
Use `FusedOrientationProviderClient.removeOrientationUpdates(DeviceOrientationListener)`
instead.

Removes all device orientation updates for the given listener.

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **removeLocationUpdates** ([LocationListener](https://developers.google.com/android/reference/com/google/android/gms/location/LocationListener) listener)

Removes all location updates for the given listener.

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **removeLocationUpdates** ([LocationCallback](https://developers.google.com/android/reference/com/google/android/gms/location/LocationCallback) callback)

Removes all location updates for the given callback.

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **removeLocationUpdates** ([PendingIntent](https://developer.android.com/reference/android/app/PendingIntent.html) pendingIntent)

Removes all location updates for the given pending intent.

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **requestDeviceOrientationUpdates** ([DeviceOrientationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/DeviceOrientationRequest) request, [Executor](https://developer.android.com/reference/java/util/concurrent/Executor.html) executor, [DeviceOrientationListener](https://developers.google.com/android/reference/com/google/android/gms/location/DeviceOrientationListener) listener)

**This method is deprecated.**  
Use `FusedOrientationProviderClient.requestOrientationUpdates(DeviceOrientationRequest,
Executor, DeviceOrientationListener)` instead.

Requests device orientation updates with the given request and delivers results to
the given listener on the specified `Executor`.

A previous request for device orientation for the same listener will be replaced by
this request.

Device orientation updates will only be served if the requesting app is in
foreground.

Use `removeDeviceOrientationUpdates(DeviceOrientationListener)` to stop device
orientation updates once no longer needed.

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **requestDeviceOrientationUpdates** ([DeviceOrientationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/DeviceOrientationRequest) request, [DeviceOrientationListener](https://developers.google.com/android/reference/com/google/android/gms/location/DeviceOrientationListener) listener, [Looper](https://developer.android.com/reference/android/os/Looper.html) looper)

**This method is deprecated.**  
Use `FusedOrientationProviderClient.requestOrientationUpdates(DeviceOrientationRequest,
Executor, DeviceOrientationListener)` instead.

Requests device orientation updates with the given request and delivers results to
the given listener on the specified `Looper`.

A previous device orientation request for the same listener will be replaced by this
request.

Device orientation updates will only be served if the requesting app is in
foreground.

##### Throws

|  |  |
| --- | --- |
| [IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html) | if `looper` is null and the calling thread has not called `Looper.prepare()`. |

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **requestLocationUpdates** ([LocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest) request, [LocationListener](https://developers.google.com/android/reference/com/google/android/gms/location/LocationListener) listener, [Looper](https://developer.android.com/reference/android/os/Looper.html) looper)

Requests location updates with the given request and results delivered to the given
listener on the specified `Looper`.

See `requestLocationUpdates(LocationRequest, Executor, LocationListener)` for more
documentation.

##### Throws

|  |  |
| --- | --- |
| [IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html) | if `looper` is null and the calling thread has not called `Looper.prepare()` |

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **requestLocationUpdates** ([LocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest) request, [Executor](https://developer.android.com/reference/java/util/concurrent/Executor.html) executor, [LocationCallback](https://developers.google.com/android/reference/com/google/android/gms/location/LocationCallback) callback)

Requests location updates with the given request and results delivered to the given
callback on the specified `Executor`.

If the given `Looper` is null,
the Looper associated with the calling thread will be used instead.

See `requestLocationUpdates(LocationRequest, Executor, LocationListener)` for more
documentation.

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **requestLocationUpdates** ([LocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest) request, [Executor](https://developer.android.com/reference/java/util/concurrent/Executor.html) executor, [LocationListener](https://developers.google.com/android/reference/com/google/android/gms/location/LocationListener) listener)

Requests location updates with the given request and results delivered to the given
listener on the specified `Executor`.
A previous request for location updates for the same listener will be replaced by this
request. If the location request has a priority higher than `Priority.PRIORITY_PASSIVE`,
a wakelock may be held on the client's behalf while delivering locations.

Use `removeLocationUpdates(LocationListener)` to stop location updates once no
longer needed.

Depending on the arguments passed in through the `LocationRequest`,
cached locations from the past may be delivered when the listener is first registered.
Clients should ensure they are checking location timestamps appropriately if
necessary.

Location requests that do not specify batching (see `LocationRequest.isBatched()`)
are guaranteed to receive locations that are monotonically increasing in time (they
will never receive a location that appears to travel backwards in time compared to the
prior location). Location requests that allow for batching (or are passive) may receive
batches of locations, and batches may be out-of-order with respect to other received
batches (within a single batch locations are still guaranteed to be in order).

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **requestLocationUpdates** ([LocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest) request, [LocationCallback](https://developers.google.com/android/reference/com/google/android/gms/location/LocationCallback) callback, [Looper](https://developer.android.com/reference/android/os/Looper.html) looper)

Requests location updates with the given request and results delivered to the given
callback on the specified `Looper`.

If the given `Looper` is null,
the Looper associated with the calling thread will be used instead.

See `requestLocationUpdates(LocationRequest, Executor, LocationListener)` for more
documentation.

##### Throws

|  |  |
| --- | --- |
| [IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html) | if `looper` is null and the calling thread has not called `Looper.prepare()` |

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **requestLocationUpdates** ([LocationRequest](https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest) request, [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent.html) pendingIntent)

Requests location updates with the given request and results delivered via the
specified `PendingIntent`.
A previous request for location updates for the same pending intent will be replaced by
this request. If the location request has a priority higher than `Priority.PRIORITY_PASSIVE`,
a wakelock may be held on the client's behalf while delivering locations. A wakelock
will not be held while delivering availability updates.

Location updates should be extracted from the received `Intent` via
`LocationResult.hasResult(Intent)` and `LocationResult.extractResult(Intent)`. Availability updates should be
extracted from the `Intent` via
`LocationAvailability.hasLocationAvailability(Intent)` and `LocationAvailability.extractLocationAvailability(Intent)`.

This method is suited for receiving location updates in the background, even when
the receiving app may have been killed by the system. Using a `PendingIntent`
allows the target component to be started and receive location updates. For foreground
use cases prefer to listen for location updates via a listener or callback instead of a
pending intent.

`PendingIntent`
location requests are automatically removed when the client application is reset (when
the client application is upgraded or removed, or the user force-restarts or
force-quits it), or if the pending intent is canceled.

Use `removeLocationUpdates(PendingIntent)` to stop location updates once no longer
needed.

Depending on the arguments passed in through the `LocationRequest`,
locations from the past may be delivered when the callback is first registered. Clients
should ensure they are checking location timestamps appropriately if necessary.

Location requests that do not specify batching (see `LocationRequest.isBatched()`)
are guaranteed to receive locations that are monotonically increasing in time (they
will never receive a location that appears to travel backwards in time compared to the
prior location). Location requests that allow for batching (or are passive) may receive
batches of locations, and batches may be out-of-order with respect to other received
batches (within a single batch locations are still guaranteed to be in order).

This API will not work for [instant apps](https://developer.android.com/topic/google-play-instant), since they are
intended to run only in the foreground and will be disconnected otherwise. Instant apps
should prefer to use any of the overloads that accept `LocationListener`
or `LocationCallback`
instead.

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **setMockLocation** ([Location](https://developer.android.com/reference/android/location/Location.html) location)

Sets the mock location of the Fused Location Provider.

Delivers the given location to the FLP as if it was coming from an underlying
location source. Normal FLP logic around receiving and delivering location will
generally apply. For this reason the timestamps of the location should be set
appropriately, as the FLP may expect monotonically increasing timestamps. When this
location is reported to FLP clients it will be marked as a mock location (see
`Location.isMock()`
or [LocationCompat.isMock()](https://developer.android.com/reference/androidx/core/location/LocationCompat#isMock(android.location.Location)) from the compat libraries).

This API can only be successfully used while the FLP is in mock mode. Clients must
fulfill the same security requirements as for `setMockMode(boolean)` as well.

#### public abstract Task<[Void](https://developer.android.com/reference/java/lang/Void.html)> **setMockMode** (boolean mockMode)

Sets whether or not the Fused Location Provider is in mock mode.

Entering mock mode clears the FLP's cached locations, and ensures that the FLP will
only report locations set through `setMockLocation(Location)`. Exiting mock mode will clear any mock locations
set from the FLP's cache as well. Mock mode affects all location clients using the FLP,
including location clients in other processes and derivative APIs such as geofencing
and so forth. Because this affects all FLP usage, clients should always ensure they
properly set the mock mode to false when finished.

Successfully using this API on devices running Android M+ requires the client to
request the `android.permission.ACCESS_MOCK_LOCATION` permission and to be
selected as the mock location app within the device developer settings. Using this API
on pre-M devices requires the `Settings.Secure.ALLOW_MOCK_LOCATION` setting
to be enabled.
