# Location Kit

|操作|旧版本|新版本|d.ts文件|
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
|API废弃版本变更|类名：geolocation； API声明：function getCurrentLocation(callback: AsyncCallback\<Location\>): void; 差异内容：NA|类名：geolocation； API声明：function getCurrentLocation(callback: AsyncCallback\<Location\>): void; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：geolocation； API声明：function getCurrentLocation(request?: CurrentLocationRequest): Promise\<Location\>; 差异内容：NA|类名：geolocation； API声明：function getCurrentLocation(request?: CurrentLocationRequest): Promise\<Location\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：geolocation； API声明：function getLastLocation(): Promise\<Location\>; 差异内容：NA|类名：geolocation； API声明：function getLastLocation(): Promise\<Location\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：geolocation； API声明：function isLocationEnabled(): Promise\<boolean\>; 差异内容：NA|类名：geolocation； API声明：function isLocationEnabled(): Promise\<boolean\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：geolocation； API声明：function requestEnableLocation(): Promise\<boolean\>; 差异内容：NA|类名：geolocation； API声明：function requestEnableLocation(): Promise\<boolean\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：geolocation； API声明：function getAddressesFromLocation(request: ReverseGeoCodeRequest): Promise\<Array\<GeoAddress\>\>; 差异内容：NA|类名：geolocation； API声明：function getAddressesFromLocation(request: ReverseGeoCodeRequest): Promise\<Array\<GeoAddress\>\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：geolocation； API声明：function getAddressesFromLocationName(request: GeoCodeRequest): Promise\<Array\<GeoAddress\>\>; 差异内容：NA|类名：geolocation； API声明：function getAddressesFromLocationName(request: GeoCodeRequest): Promise\<Array\<GeoAddress\>\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：geolocation； API声明：function isGeoServiceAvailable(): Promise\<boolean\>; 差异内容：NA|类名：geolocation； API声明：function isGeoServiceAvailable(): Promise\<boolean\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：geolocation； API声明：function getCachedGnssLocationsSize(): Promise\<number\>; 差异内容：NA|类名：geolocation； API声明：function getCachedGnssLocationsSize(): Promise\<number\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：geolocation； API声明：function flushCachedGnssLocations(): Promise\<boolean\>; 差异内容：NA|类名：geolocation； API声明：function flushCachedGnssLocations(): Promise\<boolean\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：geolocation； API声明：function sendCommand(command: LocationCommand): Promise\<boolean\>; 差异内容：NA|类名：geolocation； API声明：function sendCommand(command: LocationCommand): Promise\<boolean\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：SatelliteStatusInfo； API声明：satellitesNumber: number; 差异内容：NA|类名：SatelliteStatusInfo； API声明：satellitesNumber: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：SatelliteStatusInfo； API声明：satelliteIds: Array\<number\>; 差异内容：NA|类名：SatelliteStatusInfo； API声明：satelliteIds: Array\<number\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：SatelliteStatusInfo； API声明：carrierToNoiseDensitys: Array\<number\>; 差异内容：NA|类名：SatelliteStatusInfo； API声明：carrierToNoiseDensitys: Array\<number\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：SatelliteStatusInfo； API声明：altitudes: Array\<number\>; 差异内容：NA|类名：SatelliteStatusInfo； API声明：altitudes: Array\<number\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：SatelliteStatusInfo； API声明：azimuths: Array\<number\>; 差异内容：NA|类名：SatelliteStatusInfo； API声明：azimuths: Array\<number\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：SatelliteStatusInfo； API声明：carrierFrequencies: Array\<number\>; 差异内容：NA|类名：SatelliteStatusInfo； API声明：carrierFrequencies: Array\<number\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：CachedGnssLocationsRequest； API声明：reportingPeriodSec: number; 差异内容：NA|类名：CachedGnssLocationsRequest； API声明：reportingPeriodSec: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：CachedGnssLocationsRequest； API声明：wakeUpCacheQueueFull: boolean; 差异内容：NA|类名：CachedGnssLocationsRequest； API声明：wakeUpCacheQueueFull: boolean; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeofenceRequest； API声明：priority: LocationRequestPriority; 差异内容：NA|类名：GeofenceRequest； API声明：priority: LocationRequestPriority; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeofenceRequest； API声明：scenario: LocationRequestScenario; 差异内容：NA|类名：GeofenceRequest； API声明：scenario: LocationRequestScenario; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeofenceRequest； API声明：geofence: Geofence; 差异内容：NA|类名：GeofenceRequest； API声明：geofence: Geofence; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Geofence； API声明：latitude: number; 差异内容：NA|类名：Geofence； API声明：latitude: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Geofence； API声明：longitude: number; 差异内容：NA|类名：Geofence； API声明：longitude: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Geofence； API声明：radius: number; 差异内容：NA|类名：Geofence； API声明：radius: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Geofence； API声明：expiration: number; 差异内容：NA|类名：Geofence； API声明：expiration: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：ReverseGeoCodeRequest； API声明：locale?: string; 差异内容：NA|类名：ReverseGeoCodeRequest； API声明：locale?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：ReverseGeoCodeRequest； API声明：latitude: number; 差异内容：NA|类名：ReverseGeoCodeRequest； API声明：latitude: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：ReverseGeoCodeRequest； API声明：longitude: number; 差异内容：NA|类名：ReverseGeoCodeRequest； API声明：longitude: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：ReverseGeoCodeRequest； API声明：maxItems?: number; 差异内容：NA|类名：ReverseGeoCodeRequest； API声明：maxItems?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoCodeRequest； API声明：locale?: string; 差异内容：NA|类名：GeoCodeRequest； API声明：locale?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoCodeRequest； API声明：description: string; 差异内容：NA|类名：GeoCodeRequest； API声明：description: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoCodeRequest； API声明：maxItems?: number; 差异内容：NA|类名：GeoCodeRequest； API声明：maxItems?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoCodeRequest； API声明：minLatitude?: number; 差异内容：NA|类名：GeoCodeRequest； API声明：minLatitude?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoCodeRequest； API声明：minLongitude?: number; 差异内容：NA|类名：GeoCodeRequest； API声明：minLongitude?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoCodeRequest； API声明：maxLatitude?: number; 差异内容：NA|类名：GeoCodeRequest； API声明：maxLatitude?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoCodeRequest； API声明：maxLongitude?: number; 差异内容：NA|类名：GeoCodeRequest； API声明：maxLongitude?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：latitude?: number; 差异内容：NA|类名：GeoAddress； API声明：latitude?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：longitude?: number; 差异内容：NA|类名：GeoAddress； API声明：longitude?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：locale?: string; 差异内容：NA|类名：GeoAddress； API声明：locale?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：placeName?: string; 差异内容：NA|类名：GeoAddress； API声明：placeName?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：countryCode?: string; 差异内容：NA|类名：GeoAddress； API声明：countryCode?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：countryName?: string; 差异内容：NA|类名：GeoAddress； API声明：countryName?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：administrativeArea?: string; 差异内容：NA|类名：GeoAddress； API声明：administrativeArea?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：subAdministrativeArea?: string; 差异内容：NA|类名：GeoAddress； API声明：subAdministrativeArea?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：locality?: string; 差异内容：NA|类名：GeoAddress； API声明：locality?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：subLocality?: string; 差异内容：NA|类名：GeoAddress； API声明：subLocality?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：roadName?: string; 差异内容：NA|类名：GeoAddress； API声明：roadName?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：subRoadName?: string; 差异内容：NA|类名：GeoAddress； API声明：subRoadName?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：premises?: string; 差异内容：NA|类名：GeoAddress； API声明：premises?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：postalCode?: string; 差异内容：NA|类名：GeoAddress； API声明：postalCode?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：phoneNumber?: string; 差异内容：NA|类名：GeoAddress； API声明：phoneNumber?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：addressUrl?: string; 差异内容：NA|类名：GeoAddress； API声明：addressUrl?: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：descriptions?: Array\<string\>; 差异内容：NA|类名：GeoAddress； API声明：descriptions?: Array\<string\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoAddress； API声明：descriptionsSize?: number; 差异内容：NA|类名：GeoAddress； API声明：descriptionsSize?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequest； API声明：priority?: LocationRequestPriority; 差异内容：NA|类名：LocationRequest； API声明：priority?: LocationRequestPriority; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequest； API声明：scenario?: LocationRequestScenario; 差异内容：NA|类名：LocationRequest； API声明：scenario?: LocationRequestScenario; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequest； API声明：timeInterval?: number; 差异内容：NA|类名：LocationRequest； API声明：timeInterval?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequest； API声明：distanceInterval?: number; 差异内容：NA|类名：LocationRequest； API声明：distanceInterval?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequest； API声明：maxAccuracy?: number; 差异内容：NA|类名：LocationRequest； API声明：maxAccuracy?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：CurrentLocationRequest； API声明：priority?: LocationRequestPriority; 差异内容：NA|类名：CurrentLocationRequest； API声明：priority?: LocationRequestPriority; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：CurrentLocationRequest； API声明：scenario?: LocationRequestScenario; 差异内容：NA|类名：CurrentLocationRequest； API声明：scenario?: LocationRequestScenario; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：CurrentLocationRequest； API声明：maxAccuracy?: number; 差异内容：NA|类名：CurrentLocationRequest； API声明：maxAccuracy?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：CurrentLocationRequest； API声明：timeoutMs?: number; 差异内容：NA|类名：CurrentLocationRequest； API声明：timeoutMs?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Location； API声明：latitude: number; 差异内容：NA|类名：Location； API声明：latitude: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Location； API声明：longitude: number; 差异内容：NA|类名：Location； API声明：longitude: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Location； API声明：altitude: number; 差异内容：NA|类名：Location； API声明：altitude: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Location； API声明：accuracy: number; 差异内容：NA|类名：Location； API声明：accuracy: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Location； API声明：speed: number; 差异内容：NA|类名：Location； API声明：speed: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Location； API声明：timeStamp: number; 差异内容：NA|类名：Location； API声明：timeStamp: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Location； API声明：direction: number; 差异内容：NA|类名：Location； API声明：direction: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Location； API声明：timeSinceBoot: number; 差异内容：NA|类名：Location； API声明：timeSinceBoot: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Location； API声明：additions?: Array\<string\>; 差异内容：NA|类名：Location； API声明：additions?: Array\<string\>; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：Location； API声明：additionSize?: number; 差异内容：NA|类名：Location； API声明：additionSize?: number; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequestPriority； API声明：UNSET = 0x200 差异内容：NA|类名：LocationRequestPriority； API声明：UNSET = 0x200 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequestPriority； API声明：ACCURACY 差异内容：NA|类名：LocationRequestPriority； API声明：ACCURACY 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequestPriority； API声明：LOW_POWER 差异内容：NA|类名：LocationRequestPriority； API声明：LOW_POWER 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequestPriority； API声明：FIRST_FIX 差异内容：NA|类名：LocationRequestPriority； API声明：FIRST_FIX 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequestScenario； API声明：UNSET = 0x300 差异内容：NA|类名：LocationRequestScenario； API声明：UNSET = 0x300 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequestScenario； API声明：NAVIGATION 差异内容：NA|类名：LocationRequestScenario； API声明：NAVIGATION 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequestScenario； API声明：TRAJECTORY_TRACKING 差异内容：NA|类名：LocationRequestScenario； API声明：TRAJECTORY_TRACKING 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequestScenario； API声明：CAR_HAILING 差异内容：NA|类名：LocationRequestScenario； API声明：CAR_HAILING 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequestScenario； API声明：DAILY_LIFE_SERVICE 差异内容：NA|类名：LocationRequestScenario； API声明：DAILY_LIFE_SERVICE 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationRequestScenario； API声明：NO_POWER 差异内容：NA|类名：LocationRequestScenario； API声明：NO_POWER 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoLocationErrorCode； API声明：INPUT_PARAMS_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：INPUT_PARAMS_ERROR 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoLocationErrorCode； API声明：REVERSE_GEOCODE_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：REVERSE_GEOCODE_ERROR 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoLocationErrorCode； API声明：GEOCODE_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：GEOCODE_ERROR 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoLocationErrorCode； API声明：LOCATOR_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：LOCATOR_ERROR 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoLocationErrorCode； API声明：LOCATION_SWITCH_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：LOCATION_SWITCH_ERROR 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoLocationErrorCode； API声明：LAST_KNOWN_LOCATION_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：LAST_KNOWN_LOCATION_ERROR 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：GeoLocationErrorCode； API声明：LOCATION_REQUEST_TIMEOUT_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：LOCATION_REQUEST_TIMEOUT_ERROR 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationPrivacyType； API声明：OTHERS = 0 差异内容：NA|类名：LocationPrivacyType； API声明：OTHERS = 0 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationPrivacyType； API声明：STARTUP 差异内容：NA|类名：LocationPrivacyType； API声明：STARTUP 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationPrivacyType； API声明：CORE_LOCATION 差异内容：NA|类名：LocationPrivacyType； API声明：CORE_LOCATION 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationCommand； API声明：scenario: LocationRequestScenario; 差异内容：NA|类名：LocationCommand； API声明：scenario: LocationRequestScenario; 差异内容：9|api/@ohos.geolocation.d.ts|
|API废弃版本变更|类名：LocationCommand； API声明：command: string; 差异内容：NA|类名：LocationCommand； API声明：command: string; 差异内容：9|api/@ohos.geolocation.d.ts|
|权限变更|类名：geolocation； API声明：function getCurrentLocation(callback: AsyncCallback\<Location\>): void; 差异内容：NA|类名：geolocation； API声明：function getCurrentLocation(callback: AsyncCallback\<Location\>): void; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：geolocation； API声明：function getCurrentLocation(request?: CurrentLocationRequest): Promise\<Location\>; 差异内容：NA|类名：geolocation； API声明：function getCurrentLocation(request?: CurrentLocationRequest): Promise\<Location\>; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：geolocation； API声明：function getLastLocation(): Promise\<Location\>; 差异内容：NA|类名：geolocation； API声明：function getLastLocation(): Promise\<Location\>; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：geolocation； API声明：function isLocationEnabled(): Promise\<boolean\>; 差异内容：NA|类名：geolocation； API声明：function isLocationEnabled(): Promise\<boolean\>; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：geolocation； API声明：function requestEnableLocation(): Promise\<boolean\>; 差异内容：NA|类名：geolocation； API声明：function requestEnableLocation(): Promise\<boolean\>; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：geolocation； API声明：function getAddressesFromLocation(request: ReverseGeoCodeRequest): Promise\<Array\<GeoAddress\>\>; 差异内容：NA|类名：geolocation； API声明：function getAddressesFromLocation(request: ReverseGeoCodeRequest): Promise\<Array\<GeoAddress\>\>; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：geolocation； API声明：function getAddressesFromLocationName(request: GeoCodeRequest): Promise\<Array\<GeoAddress\>\>; 差异内容：NA|类名：geolocation； API声明：function getAddressesFromLocationName(request: GeoCodeRequest): Promise\<Array\<GeoAddress\>\>; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：geolocation； API声明：function isGeoServiceAvailable(): Promise\<boolean\>; 差异内容：NA|类名：geolocation； API声明：function isGeoServiceAvailable(): Promise\<boolean\>; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：geolocation； API声明：function getCachedGnssLocationsSize(): Promise\<number\>; 差异内容：NA|类名：geolocation； API声明：function getCachedGnssLocationsSize(): Promise\<number\>; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：geolocation； API声明：function flushCachedGnssLocations(): Promise\<boolean\>; 差异内容：NA|类名：geolocation； API声明：function flushCachedGnssLocations(): Promise\<boolean\>; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：geolocation； API声明：function sendCommand(command: LocationCommand): Promise\<boolean\>; 差异内容：NA|类名：geolocation； API声明：function sendCommand(command: LocationCommand): Promise\<boolean\>; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：latitude?: number; 差异内容：NA|类名：GeoAddress； API声明：latitude?: number; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：longitude?: number; 差异内容：NA|类名：GeoAddress； API声明：longitude?: number; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：locale?: string; 差异内容：NA|类名：GeoAddress； API声明：locale?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：placeName?: string; 差异内容：NA|类名：GeoAddress； API声明：placeName?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：countryCode?: string; 差异内容：NA|类名：GeoAddress； API声明：countryCode?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：countryName?: string; 差异内容：NA|类名：GeoAddress； API声明：countryName?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：administrativeArea?: string; 差异内容：NA|类名：GeoAddress； API声明：administrativeArea?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：subAdministrativeArea?: string; 差异内容：NA|类名：GeoAddress； API声明：subAdministrativeArea?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：locality?: string; 差异内容：NA|类名：GeoAddress； API声明：locality?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：subLocality?: string; 差异内容：NA|类名：GeoAddress； API声明：subLocality?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：roadName?: string; 差异内容：NA|类名：GeoAddress； API声明：roadName?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：subRoadName?: string; 差异内容：NA|类名：GeoAddress； API声明：subRoadName?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：premises?: string; 差异内容：NA|类名：GeoAddress； API声明：premises?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：postalCode?: string; 差异内容：NA|类名：GeoAddress； API声明：postalCode?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：phoneNumber?: string; 差异内容：NA|类名：GeoAddress； API声明：phoneNumber?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：addressUrl?: string; 差异内容：NA|类名：GeoAddress； API声明：addressUrl?: string; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：descriptions?: Array\<string\>; 差异内容：NA|类名：GeoAddress； API声明：descriptions?: Array\<string\>; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoAddress； API声明：descriptionsSize?: number; 差异内容：NA|类名：GeoAddress； API声明：descriptionsSize?: number; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：Location； API声明：latitude: number; 差异内容：NA|类名：Location； API声明：latitude: number; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：Location； API声明：longitude: number; 差异内容：NA|类名：Location； API声明：longitude: number; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：Location； API声明：altitude: number; 差异内容：NA|类名：Location； API声明：altitude: number; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：Location； API声明：accuracy: number; 差异内容：NA|类名：Location； API声明：accuracy: number; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：Location； API声明：speed: number; 差异内容：NA|类名：Location； API声明：speed: number; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：Location； API声明：timeStamp: number; 差异内容：NA|类名：Location； API声明：timeStamp: number; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：Location； API声明：direction: number; 差异内容：NA|类名：Location； API声明：direction: number; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：Location； API声明：timeSinceBoot: number; 差异内容：NA|类名：Location； API声明：timeSinceBoot: number; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：Location； API声明：additions?: Array\<string\>; 差异内容：NA|类名：Location； API声明：additions?: Array\<string\>; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：Location； API声明：additionSize?: number; 差异内容：NA|类名：Location； API声明：additionSize?: number; 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoLocationErrorCode； API声明：INPUT_PARAMS_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：INPUT_PARAMS_ERROR 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoLocationErrorCode； API声明：REVERSE_GEOCODE_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：REVERSE_GEOCODE_ERROR 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoLocationErrorCode； API声明：GEOCODE_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：GEOCODE_ERROR 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoLocationErrorCode； API声明：LOCATOR_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：LOCATOR_ERROR 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoLocationErrorCode； API声明：LOCATION_SWITCH_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：LOCATION_SWITCH_ERROR 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoLocationErrorCode； API声明：LAST_KNOWN_LOCATION_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：LAST_KNOWN_LOCATION_ERROR 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|权限变更|类名：GeoLocationErrorCode； API声明：LOCATION_REQUEST_TIMEOUT_ERROR 差异内容：NA|类名：GeoLocationErrorCode； API声明：LOCATION_REQUEST_TIMEOUT_ERROR 差异内容：ohos.permission.LOCATION|api/@ohos.geolocation.d.ts|
|函数变更|类名：geoLocationManager； API声明：function on(type: 'locationChange', request: LocationRequest, callback: Callback\<Location\>): void; 差异内容：request: LocationRequest|类名：geoLocationManager； API声明：function on(type: 'locationChange', request: LocationRequest \| ContinuousLocationRequest, callback: Callback\<Location\>): void; 差异内容：request: LocationRequest \| ContinuousLocationRequest|api/@ohos.geoLocationManager.d.ts|
|函数变更|类名：geoLocationManager； API声明：function getCurrentLocation(request: CurrentLocationRequest, callback: AsyncCallback\<Location\>): void; 差异内容：request: CurrentLocationRequest|类名：geoLocationManager； API声明：function getCurrentLocation(request: CurrentLocationRequest \| SingleLocationRequest, callback: AsyncCallback\<Location\>): void; 差异内容：request: CurrentLocationRequest \| SingleLocationRequest|api/@ohos.geoLocationManager.d.ts|
|函数变更|类名：geoLocationManager； API声明：function getCurrentLocation(request?: CurrentLocationRequest): Promise\<Location\>; 差异内容：request?: CurrentLocationRequest|类名：geoLocationManager； API声明：function getCurrentLocation(request?: CurrentLocationRequest \| SingleLocationRequest): Promise\<Location\>; 差异内容：request?: CurrentLocationRequest \| SingleLocationRequest|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明：function on(type: 'locationError', callback: Callback\<LocationError\>): void; 差异内容：function on(type: 'locationError', callback: Callback\<LocationError\>): void;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明：function off(type: 'locationError', callback?: Callback\<LocationError\>): void; 差异内容：function off(type: 'locationError', callback?: Callback\<LocationError\>): void;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明：function addGnssGeofence(fenceRequest: GnssGeofenceRequest): Promise\<number\>; 差异内容：function addGnssGeofence(fenceRequest: GnssGeofenceRequest): Promise\<number\>;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明：function removeGnssGeofence(geofenceId: number): Promise\<void\>; 差异内容：function removeGnssGeofence(geofenceId: number): Promise\<void\>;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明：function getGeofenceSupportedCoordTypes(): Array\<CoordinateSystemType\>; 差异内容：function getGeofenceSupportedCoordTypes(): Array\<CoordinateSystemType\>;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteStatusInfo； API声明：satelliteConstellation: Array\<SatelliteConstellationCategory\>; 差异内容：satelliteConstellation: Array\<SatelliteConstellationCategory\>;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteStatusInfo； API声明：satelliteAdditionalInfo: Array\<number\>; 差异内容：satelliteAdditionalInfo: Array\<number\>;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export interface GnssGeofenceRequest 差异内容： export interface GnssGeofenceRequest|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：GnssGeofenceRequest； API声明：geofence: Geofence; 差异内容：geofence: Geofence;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：GnssGeofenceRequest； API声明：monitorTransitionEvents: Array\<GeofenceTransitionEvent\>; 差异内容：monitorTransitionEvents: Array\<GeofenceTransitionEvent\>;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：GnssGeofenceRequest； API声明：notifications?: Array\<NotificationRequest\>; 差异内容：notifications?: Array\<NotificationRequest\>;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：GnssGeofenceRequest； API声明：geofenceTransitionCallback: AsyncCallback\<GeofenceTransition\>; 差异内容：geofenceTransitionCallback: AsyncCallback\<GeofenceTransition\>;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：Geofence； API声明：coordinateSystemType?: CoordinateSystemType; 差异内容：coordinateSystemType?: CoordinateSystemType;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：ReverseGeoCodeRequest； API声明：country?: string; 差异内容：country?: string;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：GeoCodeRequest； API声明：country?: string; 差异内容：country?: string;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export interface GeofenceTransition 差异内容： export interface GeofenceTransition|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：GeofenceTransition； API声明：geofenceId: number; 差异内容：geofenceId: number;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：GeofenceTransition； API声明：transitionEvent: GeofenceTransitionEvent; 差异内容：transitionEvent: GeofenceTransitionEvent;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export interface ContinuousLocationRequest 差异内容： export interface ContinuousLocationRequest|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：ContinuousLocationRequest； API声明：interval: number; 差异内容：interval: number;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：ContinuousLocationRequest； API声明：locationScenario: UserActivityScenario \| PowerConsumptionScenario; 差异内容：locationScenario: UserActivityScenario \| PowerConsumptionScenario;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export interface SingleLocationRequest 差异内容： export interface SingleLocationRequest|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SingleLocationRequest； API声明：locatingPriority: LocatingPriority; 差异内容：locatingPriority: LocatingPriority;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SingleLocationRequest； API声明：locatingTimeoutMs: number; 差异内容：locatingTimeoutMs: number;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：Location； API声明：additionsMap?: Map\<string, string\>; 差异内容：additionsMap?: Map\<string, string\>;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：Location； API声明：altitudeAccuracy: number; 差异内容：altitudeAccuracy: number;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：Location； API声明：speedAccuracy: number; 差异内容：speedAccuracy: number;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：Location； API声明：directionAccuracy: number; 差异内容：directionAccuracy: number;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：Location； API声明：uncertaintyOfTimeSinceBoot: number; 差异内容：uncertaintyOfTimeSinceBoot: number;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：Location； API声明：sourceType: LocationSourceType; 差异内容：sourceType: LocationSourceType;|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export enum LocationSourceType 差异内容： export enum LocationSourceType|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：LocationSourceType； API声明：GNSS = 1 差异内容：GNSS = 1|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：LocationSourceType； API声明：NETWORK = 2 差异内容：NETWORK = 2|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：LocationSourceType； API声明：INDOOR = 3 差异内容：INDOOR = 3|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：LocationSourceType； API声明：RTK = 4 差异内容：RTK = 4|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export enum CoordinateSystemType 差异内容： export enum CoordinateSystemType|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：CoordinateSystemType； API声明：WGS84 = 1 差异内容：WGS84 = 1|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：CoordinateSystemType； API声明：GCJ02 = 2 差异内容：GCJ02 = 2|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export enum LocationError 差异内容： export enum LocationError|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：LocationError； API声明：LOCATING_FAILED_DEFAULT = -1 差异内容：LOCATING_FAILED_DEFAULT = -1|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：LocationError； API声明：LOCATING_FAILED_LOCATION_PERMISSION_DENIED = -2 差异内容：LOCATING_FAILED_LOCATION_PERMISSION_DENIED = -2|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：LocationError； API声明：LOCATING_FAILED_BACKGROUND_PERMISSION_DENIED = -3 差异内容：LOCATING_FAILED_BACKGROUND_PERMISSION_DENIED = -3|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：LocationError； API声明：LOCATING_FAILED_LOCATION_SWITCH_OFF = -4 差异内容：LOCATING_FAILED_LOCATION_SWITCH_OFF = -4|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：LocationError； API声明：LOCATING_FAILED_INTERNET_ACCESS_FAILURE = -5 差异内容：LOCATING_FAILED_INTERNET_ACCESS_FAILURE = -5|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export enum GeofenceTransitionEvent 差异内容： export enum GeofenceTransitionEvent|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：GeofenceTransitionEvent； API声明：GEOFENCE_TRANSITION_EVENT_ENTER = 1 差异内容：GEOFENCE_TRANSITION_EVENT_ENTER = 1|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：GeofenceTransitionEvent； API声明：GEOFENCE_TRANSITION_EVENT_EXIT = 2 差异内容：GEOFENCE_TRANSITION_EVENT_EXIT = 2|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：GeofenceTransitionEvent； API声明：GEOFENCE_TRANSITION_EVENT_DWELL = 4 差异内容：GEOFENCE_TRANSITION_EVENT_DWELL = 4|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export enum SatelliteConstellationCategory 差异内容： export enum SatelliteConstellationCategory|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteConstellationCategory； API声明：CONSTELLATION_CATEGORY_UNKNOWN = 0 差异内容：CONSTELLATION_CATEGORY_UNKNOWN = 0|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteConstellationCategory； API声明：CONSTELLATION_CATEGORY_GPS = 1 差异内容：CONSTELLATION_CATEGORY_GPS = 1|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteConstellationCategory； API声明：CONSTELLATION_CATEGORY_SBAS = 2 差异内容：CONSTELLATION_CATEGORY_SBAS = 2|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteConstellationCategory； API声明：CONSTELLATION_CATEGORY_GLONASS = 3 差异内容：CONSTELLATION_CATEGORY_GLONASS = 3|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteConstellationCategory； API声明：CONSTELLATION_CATEGORY_QZSS = 4 差异内容：CONSTELLATION_CATEGORY_QZSS = 4|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteConstellationCategory； API声明：CONSTELLATION_CATEGORY_BEIDOU = 5 差异内容：CONSTELLATION_CATEGORY_BEIDOU = 5|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteConstellationCategory； API声明：CONSTELLATION_CATEGORY_GALILEO = 6 差异内容：CONSTELLATION_CATEGORY_GALILEO = 6|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteConstellationCategory； API声明：CONSTELLATION_CATEGORY_IRNSS = 7 差异内容：CONSTELLATION_CATEGORY_IRNSS = 7|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export enum SatelliteAdditionalInfo 差异内容： export enum SatelliteAdditionalInfo|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteAdditionalInfo； API声明：SATELLITES_ADDITIONAL_INFO_NULL = 0 差异内容：SATELLITES_ADDITIONAL_INFO_NULL = 0|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteAdditionalInfo； API声明：SATELLITES_ADDITIONAL_INFO_EPHEMERIS_DATA_EXIST = 1 差异内容：SATELLITES_ADDITIONAL_INFO_EPHEMERIS_DATA_EXIST = 1|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteAdditionalInfo； API声明：SATELLITES_ADDITIONAL_INFO_ALMANAC_DATA_EXIST = 2 差异内容：SATELLITES_ADDITIONAL_INFO_ALMANAC_DATA_EXIST = 2|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteAdditionalInfo； API声明：SATELLITES_ADDITIONAL_INFO_USED_IN_FIX = 4 差异内容：SATELLITES_ADDITIONAL_INFO_USED_IN_FIX = 4|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：SatelliteAdditionalInfo； API声明：SATELLITES_ADDITIONAL_INFO_CARRIER_FREQUENCY_EXIST = 8 差异内容：SATELLITES_ADDITIONAL_INFO_CARRIER_FREQUENCY_EXIST = 8|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export enum UserActivityScenario 差异内容： export enum UserActivityScenario|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：UserActivityScenario； API声明：NAVIGATION = 0x401 差异内容：NAVIGATION = 0x401|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：UserActivityScenario； API声明：SPORT = 0x402 差异内容：SPORT = 0x402|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：UserActivityScenario； API声明：TRANSPORT = 0x403 差异内容：TRANSPORT = 0x403|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：UserActivityScenario； API声明：DAILY_LIFE_SERVICE = 0x404 差异内容：DAILY_LIFE_SERVICE = 0x404|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export enum LocatingPriority 差异内容： export enum LocatingPriority|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：LocatingPriority； API声明：PRIORITY_ACCURACY = 0x501 差异内容：PRIORITY_ACCURACY = 0x501|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：LocatingPriority； API声明：PRIORITY_LOCATING_SPEED = 0x502 差异内容：PRIORITY_LOCATING_SPEED = 0x502|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：geoLocationManager； API声明： export enum PowerConsumptionScenario 差异内容： export enum PowerConsumptionScenario|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：PowerConsumptionScenario； API声明：HIGH_POWER_CONSUMPTION = 0x601 差异内容：HIGH_POWER_CONSUMPTION = 0x601|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：PowerConsumptionScenario； API声明：LOW_POWER_CONSUMPTION = 0x602 差异内容：LOW_POWER_CONSUMPTION = 0x602|api/@ohos.geoLocationManager.d.ts|
|新增API|NA|类名：PowerConsumptionScenario； API声明：NO_POWER_CONSUMPTION = 0x603 差异内容：NO_POWER_CONSUMPTION = 0x603|api/@ohos.geoLocationManager.d.ts|
