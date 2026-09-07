#!/usr/bin/env python3
"""Author the location domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "location_capability_family"


def atom(fid, parent, axis, zh, en, definition, includes, excludes, bindings, legacy=None, privacy="sensitive"):
    return feature(
        fid, parent=parent, level="L3",
        zh=zh, en=en, definition=definition,
        includes=includes, excludes=excludes, sibling_axis=axis,
        granularity="atomic", bindings=bindings,
        legacy=legacy or {"disposition": "new", "sources": []},
        privacy_class=privacy,
    )


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "location", parent=None, level="L1",
        zh="位置与地理", en="Location and Geospatial",
        definition="设备定位、地理围栏、地图展示、地理编码与航向；不含近场 UWB/蓝牙测距（见 connectivity）。",
        includes=["定位、围栏、地图、地理编码、航向"],
        excludes=["UWB/测距见 connectivity.peripherals", "天气业务数据非地理编码"],
        legacy={"disposition": "kept", "sources": ["location"]},
    ))

    l2 = [
        ("location.positioning", "定位", "Positioning",
         "前台/后台获取与监听设备地理位置。",
         ["前台定位、后台定位、最近位置、精度与权限"],
         ["围栏见 location.geofence", "航向见 location.heading"],
         ["location.positioning"]),
        ("location.geofence", "地理围栏", "Geofencing",
         "基于区域进出/停留的地理围栏监控。",
         ["圆形/多边形围栏、进出事件"],
         ["连续定位见 location.positioning"],
         ["location.geofence"]),
        ("location.maps", "地图", "Maps",
         "地图展示、标注、覆盖物与相机控制（能力并集，非品牌并列）。",
         ["地图视图、标记、覆盖物、相机、离线"],
         ["地理编码见 location.geocoding"],
         ["location.maps"]),
        ("location.geocoding", "地理编码", "Geocoding",
         "地址与坐标互转及坐标系辅助。",
         ["正/逆地理编码、坐标换算"],
         ["地图选点见 location.maps"],
         []),
        ("location.heading", "航向与指南针", "Heading",
         "设备航向/指南针朝向。",
         ["真北/磁北航向"],
         ["位置坐标见 location.positioning"],
         []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="location", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # positioning — keep fg/bg legacy ids; add branch groups via L3 atomics only (no L4 needed)
    # User asked positioning (fg/bg) — use L3 groups then? To avoid capability under L1 we already have L2.
    # Structure: L3 branches for modes + related atomics as L3 siblings under positioning.
    f.append(feature(
        "location.positioning.foreground", parent="location.positioning", level="L3",
        zh="前台定位", en="Foreground Location",
        definition="应用可见或前台服务场景下请求/监听位置。",
        includes=["requestLocationUpdates 前台、CLLocationManager 在用"],
        excludes=["location.positioning.background"],
        sibling_axis="positioning_capability",
        legacy={"disposition": "kept", "sources": ["location.positioning.foreground"]},
        bindings=merge_bindings(
            A("FusedLocationProviderClient",
              "https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient"),
            I("CLLocationManager",
              "https://developer.apple.com/documentation/corelocation/cllocationmanager", "class"),
            H("@ohos.geoLocationManager",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
        ),
        privacy_class="sensitive",
    ))
    f.append(feature(
        "location.positioning.background", parent="location.positioning", level="L3",
        zh="后台定位", en="Background Location",
        definition="应用不在前台时持续或显著位置变更监听。",
        includes=["ACCESS_BACKGROUND_LOCATION、allowsBackgroundLocationUpdates"],
        excludes=["location.positioning.foreground"],
        sibling_axis="positioning_capability",
        legacy={"disposition": "kept", "sources": ["location.positioning.background"]},
        bindings=merge_bindings(
            A("ACCESS_BACKGROUND_LOCATION",
              "https://developer.android.com/develop/sensors-and-location/location/permissions#background"),
            I("allowsBackgroundLocationUpdates",
              "https://developer.apple.com/documentation/corelocation/cllocationmanager/1423568-allowsbackgroundlocationupdates", "property"),
            H("geoLocationManager",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-background"),
        ),
        privacy_class="sensitive",
    ))

    # Make fg/bg branches with children — currently they're rollup without granularity atomic.
    # Expand each into L4 atomics, and add sibling L3 modes.
    for row in [
        ("location.positioning.foreground.once", "location.positioning.foreground", "fg_positioning_op",
         "单次前台定位", "One-shot Foreground Location",
         "在前台获取一次当前位置。",
         ["getCurrentLocation、requestLocation"],
         ["location.positioning.foreground.watch"],
         merge_bindings(
             A("FusedLocationProviderClient.getCurrentLocation",
               "https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#getCurrentLocation(int,%20com.google.android.gms.tasks.CancellationToken)"),
             I("requestLocation",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1620548-requestlocation", "method"),
             H("getCurrentLocation",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         )),
        ("location.positioning.foreground.watch", "location.positioning.foreground", "fg_positioning_op",
         "前台连续定位", "Foreground Location Updates",
         "前台持续接收位置更新。",
         ["requestLocationUpdates、startUpdatingLocation"],
         ["location.positioning.foreground.once"],
         merge_bindings(
             A("requestLocationUpdates",
               "https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#requestLocationUpdates(com.google.android.gms.location.LocationRequest,%20com.google.android.gms.location.LocationCallback,%20android.os.Looper)"),
             I("startUpdatingLocation",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1424056-startupdatinglocation", "method"),
             H("onLocationChange",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         )),
        ("location.positioning.background.significant", "location.positioning.background", "bg_positioning_op",
         "显著位置变更", "Significant Location Change",
         "低功耗显著位置变化监控。",
         ["startMonitoringSignificantLocationChanges"],
         ["location.positioning.background.continuous"],
         merge_bindings(
             A("PRIORITY_BALANCED_POWER_ACCURACY",
               "https://developers.google.com/android/reference/com/google/android/gms/location/Priority#PRIORITY_BALANCED_POWER_ACCURACY"),
             I("startMonitoringSignificantLocationChanges",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1423531-startmonitoringsignificantlocati", "method"),
             pending("harmonyos"),
         )),
        ("location.positioning.background.continuous", "location.positioning.background", "bg_positioning_op",
         "后台连续定位", "Background Continuous Location",
         "后台持续位置更新（需相应授权与前台服务/后台模式）。",
         ["foreground service location、UIBackgroundModes location"],
         ["location.positioning.background.significant"],
         merge_bindings(
             A("foregroundServiceType location",
               "https://developer.android.com/develop/sensors-and-location/location/background"),
             I("UIBackgroundModes location",
               "https://developer.apple.com/documentation/bundleresources/information_property_list/uibackgroundmodes", "guide"),
             H("后台定位",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-background", "guide"),
         )),
    ]:
        fid, parent, axis, zh, en, definition, includes, excludes, bindings = row
        f.append(feature(
            fid, parent=parent, level="L4", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=axis,
            granularity="atomic", bindings=bindings, privacy_class="sensitive",
        ))

    for row in [
        ("location.positioning.last_known", "最近历史位置", "Last Known Location",
         "读取系统缓存的最近一次已知位置。",
         ["getLastLocation、location"],
         ["location.positioning.foreground"],
         merge_bindings(
             A("FusedLocationProviderClient.getLastLocation",
               "https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#getLastLocation()"),
             I("location",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1423660-location", "property"),
             H("getLastLocation",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         )),
        ("location.positioning.accuracy", "定位精度与优先级", "Location Accuracy",
         "配置精度、功耗优先级与更新间隔。",
         ["Priority、desiredAccuracy、LocationRequest"],
         ["location.positioning.foreground"],
         merge_bindings(
             A("LocationRequest",
               "https://developers.google.com/android/reference/com/google/android/gms/location/LocationRequest"),
             I("desiredAccuracy",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1423830-desiredaccuracy", "property"),
             H("LocationRequest",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         )),
        ("location.positioning.permission", "定位权限分级", "Location Permission",
         "请求/查询精确与大致、前台与后台定位授权。",
         ["ACCESS_FINE_LOCATION、requestWhenInUseAuthorization"],
         ["location.positioning.foreground"],
         merge_bindings(
             A("ACCESS_FINE_LOCATION",
               "https://developer.android.com/develop/sensors-and-location/location/permissions"),
             I("requestWhenInUseAuthorization",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1620562-requestwheninuseauthorization", "method"),
             H("ohos.permission.LOCATION",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-permission", "guide"),
         )),
        ("location.positioning.gnss_status", "GNSS状态与原始测量", "GNSS Status",
         "卫星状态与可选原始 GNSS 测量。",
         ["GnssStatus、GnssMeasurement"],
         ["location.positioning.foreground"],
         merge_bindings(
             A("GnssStatus",
               "https://developer.android.com/reference/android/location/GnssStatus"),
             pending("ios"),
             H("gnssStatus",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         )),
        ("location.positioning.activity", "活动类型辅助", "Activity Recognition Assist",
         "结合活动识别优化定位策略（步行/驾车等）。",
         ["ActivityRecognitionClient"],
         ["location.positioning.accuracy"],
         merge_bindings(
             A("ActivityRecognitionClient",
               "https://developers.google.com/android/reference/com/google/android/gms/location/ActivityRecognitionClient"),
             I("CMMotionActivityManager",
               "https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager", "class"),
             pending("harmonyos"),
         )),
        ("location.positioning.indoor", "室内定位增强", "Indoor Positioning",
         "室内/高精度定位增强入口。",
         ["indoor / Wi-Fi RTT 辅助待核"],
         ["location.positioning.foreground"],
         merge_bindings(
             A("WifiRttManager",
               "https://developer.android.com/guide/topics/connectivity/wifi-rtt"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("location.positioning.services_check", "定位服务可用性", "Location Services Check",
         "检查系统定位开关与提供者可用性。",
         ["isLocationEnabled、locationServicesEnabled"],
         ["location.positioning.permission"],
         merge_bindings(
             A("LocationManager.isLocationEnabled",
               "https://developer.android.com/reference/android/location/LocationManager#isLocationEnabled()"),
             I("locationServicesEnabled",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1423567-locationservicesenabled", "method"),
             H("isLocationEnabled",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "location.positioning", "positioning_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # Mark fg/bg as branch (they have children)
    for node in f:
        if node["id"] in ("location.positioning.foreground", "location.positioning.background"):
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            node["knowledge_path"] = "knowledge/" + "/".join(node["id"].split(".")) + "/_rollup.yaml"

    # geofence
    f.append(feature(
        "location.geofence.region", parent="location.geofence", level="L3",
        zh="区域围栏监控", en="Region Geofence",
        definition="注册圆形/多边形区域并接收进出事件。",
        includes=["GeofencingClient、CLCircularRegion"],
        excludes=["location.geofence.dwell"],
        sibling_axis="geofence_capability",
        granularity="atomic",
        legacy={"disposition": "kept", "sources": ["location.geofence.region"]},
        bindings=merge_bindings(
            A("GeofencingClient",
              "https://developers.google.com/android/reference/com/google/android/gms/location/GeofencingClient"),
            I("CLCircularRegion",
              "https://developer.apple.com/documentation/corelocation/clcircularregion", "class"),
            H("GeoFence",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
        ),
        privacy_class="sensitive",
    ))
    for row in [
        ("location.geofence.dwell", "停留围栏", "Dwell Geofence",
         "在区域内停留达到阈值时触发。",
         ["GEOFENCE_TRANSITION_DWELL"],
         ["location.geofence.region"],
         merge_bindings(
             A("Geofence.GEOFENCE_TRANSITION_DWELL",
               "https://developers.google.com/android/reference/com/google/android/gms/location/Geofence#GEOFENCE_TRANSITION_DWELL"),
             pending("ios", "可用区域监控+停留逻辑自实现"),
             pending("harmonyos"),
         )),
        ("location.geofence.add_remove", "围栏增删", "Add Remove Geofence",
         "添加、移除单个或批量地理围栏。",
         ["addGeofences、stopMonitoring"],
         ["location.geofence.region"],
         merge_bindings(
             A("GeofencingClient.addGeofences",
               "https://developers.google.com/android/reference/com/google/android/gms/location/GeofencingClient#addGeofences(com.google.android.gms.location.GeofencingRequest,%20android.app.PendingIntent)"),
             I("startMonitoring",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1423656-startmonitoring", "method"),
             H("addGnssGeofence",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         )),
        ("location.geofence.event", "围栏事件回调", "Geofence Events",
         "接收进入/离开/停留围栏事件。",
         ["GeofencingEvent、didEnterRegion"],
         ["location.geofence.region"],
         merge_bindings(
             A("GeofencingEvent",
               "https://developers.google.com/android/reference/com/google/android/gms/location/GeofencingEvent"),
             I("didEnterRegion",
               "https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423560-locationmanager", "method"),
             H("GeoFence 回调",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         )),
        ("location.geofence.limit", "围栏数量与限制", "Geofence Limits",
         "查询平台围栏数量上限与限制条件。",
         ["max geofences"],
         ["location.geofence.add_remove"],
         merge_bindings(
             A("Geofence Limits",
               "https://developer.android.com/develop/sensors-and-location/location/geofencing#add-geofences", "guide"),
             I("maximumRegionMonitoringDistance",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1423652-maximumregionmonitoringdistance", "property"),
             pending("harmonyos"),
         )),
        ("location.geofence.permission", "围栏权限要求", "Geofence Permission",
         "围栏所需的定位/后台权限组合。",
         ["后台定位 + 精确位置"],
         ["location.positioning.permission"],
         merge_bindings(
             A("Geofencing permissions",
               "https://developer.android.com/develop/sensors-and-location/location/geofencing", "guide"),
             I("Always authorization",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1620551-requestalwaysauthorization", "method"),
             H("location permission",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-permission", "guide"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "location.geofence", "geofence_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # maps — keep maps.sdk as atomic
    f.append(feature(
        "location.maps.sdk", parent="location.maps", level="L3",
        zh="地图 SDK 视图", en="Map SDK View",
        definition="嵌入应用内的地图视图与基础渲染能力（跨厂商能力并集）。",
        includes=["MapView、MKMapView、MapComponent"],
        excludes=["location.maps.launch_external"],
        sibling_axis="maps_capability",
        granularity="atomic",
        legacy={"disposition": "kept", "sources": ["location.maps.sdk"]},
        bindings=merge_bindings(
            A("MapView",
              "https://developers.google.com/maps/documentation/android-sdk/map"),
            I("MKMapView",
              "https://developer.apple.com/documentation/mapkit/mkmapview", "class"),
            H("MapComponent",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-mapcomponent"),
        ),
    ))
    for row in [
        ("location.maps.camera", "地图相机视点", "Map Camera",
         "控制地图中心、缩放、倾斜与动画相机。",
         ["CameraUpdate、region、setCamera"],
         ["location.maps.sdk"],
         merge_bindings(
             A("CameraUpdateFactory",
               "https://developers.google.com/maps/documentation/android-sdk/views"),
             I("setRegion",
               "https://developer.apple.com/documentation/mapkit/mkmapview/1452463-setregion", "method"),
             H("map camera",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-camera", "guide"),
         )),
        ("location.maps.marker", "标记与点注释", "Map Markers",
         "添加/更新/移除地图标记与标注。",
         ["Marker、MKPointAnnotation"],
         ["location.maps.overlay"],
         merge_bindings(
             A("Marker",
               "https://developers.google.com/maps/documentation/android-sdk/marker"),
             I("MKPointAnnotation",
               "https://developer.apple.com/documentation/mapkit/mkpointannotation", "class"),
             H("map marker",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-marker", "guide"),
         )),
        ("location.maps.overlay", "覆盖物绘制", "Map Overlays",
         "折线、多边形、圆等矢量覆盖物。",
         ["Polyline、MKOverlay"],
         ["location.maps.marker"],
         merge_bindings(
             A("Polyline",
               "https://developers.google.com/maps/documentation/android-sdk/shapes"),
             I("MKOverlay",
               "https://developer.apple.com/documentation/mapkit/mkoverlay", "protocol"),
             H("map shape",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-drawing", "guide"),
         )),
        ("location.maps.gesture", "地图手势与控件", "Map Gestures",
         "缩放/旋转手势开关与指南针等控件。",
         ["uiSettings、isZoomEnabled"],
         ["location.maps.camera"],
         merge_bindings(
             A("UiSettings",
               "https://developers.google.com/android/reference/com/google/android/gms/maps/UiSettings"),
             I("isZoomEnabled",
               "https://developer.apple.com/documentation/mapkit/mkmapview/1452501-iszoomenabled", "property"),
             H("map gesture",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-gesture", "guide"),
         )),
        ("location.maps.my_location", "我的位置图层", "My Location Layer",
         "在地图上显示用户当前位置蓝点。",
         ["isMyLocationEnabled、showsUserLocation"],
         ["location.positioning.foreground"],
         merge_bindings(
             A("GoogleMap.setMyLocationEnabled",
               "https://developers.google.com/android/reference/com/google/android/gms/maps/GoogleMap#setMyLocationEnabled(boolean)"),
             I("showsUserLocation",
               "https://developer.apple.com/documentation/mapkit/mkmapview/1452115-showsuserlocation", "property"),
             H("my location",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location", "guide"),
         )),
        ("location.maps.type", "地图类型", "Map Type",
         "标准/卫星/混合等底图类型切换。",
         ["mapType、MKMapType"],
         ["location.maps.sdk"],
         merge_bindings(
             A("GoogleMap.setMapType",
               "https://developers.google.com/android/reference/com/google/android/gms/maps/GoogleMap#setMapType(int)"),
             I("mapType",
               "https://developer.apple.com/documentation/mapkit/mkmapview/1452445-maptype", "property"),
             H("map type",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-display", "guide"),
         )),
        ("location.maps.offline", "离线地图", "Offline Maps",
         "下载或使用离线地图瓦片/数据包。",
         ["offline map region"],
         ["location.maps.sdk"],
         merge_bindings(
             pending("android", "厂商 SDK 离线能力并集，待核"),
             I("MKMapSnapshotter / 缓存",
               "https://developer.apple.com/documentation/mapkit/mkmapsnapshotter", "class"),
             H("离线地图",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-offline", "guide"),
         )),
        ("location.maps.snapshot", "地图截图", "Map Snapshot",
         "将当前地图视图导出为静态图片。",
         ["SnapshotReadyCallback、MKMapSnapshotter"],
         ["location.maps.sdk"],
         merge_bindings(
             A("SnapshotReadyCallback",
               "https://developers.google.com/android/reference/com/google/android/gms/maps/GoogleMap.SnapshotReadyCallback"),
             I("MKMapSnapshotter",
               "https://developer.apple.com/documentation/mapkit/mkmapsnapshotter", "class"),
             pending("harmonyos"),
         )),
        ("location.maps.launch_external", "拉起系统地图", "Launch System Maps",
         "通过 URL/Intent 拉起系统或已装地图应用。",
         ["geo: Intent、mapItem openInMaps"],
         ["location.maps.sdk"],
         merge_bindings(
             A("geo: URI",
               "https://developer.android.com/guide/components/intents-common#Maps", "guide"),
             I("openInMaps",
               "https://developer.apple.com/documentation/mapkit/mkmapitem/1453911-openinmaps", "method"),
             H("startAbility 地图",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-launch", "guide"),
         )),
        ("location.maps.cluster", "点聚合", "Marker Clustering",
         "大量标记的聚合展示。",
         ["ClusterManager、MKClusterAnnotation"],
         ["location.maps.marker"],
         merge_bindings(
             A("ClusterManager",
               "https://developers.google.com/maps/documentation/android-sdk/utility/marker-clustering"),
             I("MKClusterAnnotation",
               "https://developer.apple.com/documentation/mapkit/mkclusterannotation", "class"),
             pending("harmonyos"),
         )),
        ("location.maps.heatmap", "热力图层", "Heatmap Layer",
         "密度热力图层渲染。",
         ["HeatmapTileProvider"],
         ["location.maps.overlay"],
         merge_bindings(
             A("HeatmapTileProvider",
               "https://developers.google.com/maps/documentation/android-sdk/utility/heatmap"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("location.maps.route_display", "路线叠加展示", "Route Overlay Display",
         "在地图上展示路径规划结果折线（规划本身可后端）。",
         ["Polyline route、MKRoute.polyline"],
         ["location.maps.overlay"],
         merge_bindings(
             A("Polyline",
               "https://developers.google.com/maps/documentation/android-sdk/shapes"),
             I("MKRoute",
               "https://developer.apple.com/documentation/mapkit/mkroute", "class"),
             H("route",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-route", "guide"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "location.maps", "maps_capability",
            zh, en, definition, includes, excludes, bindings, privacy="none",
        ))

    # geocoding
    for row in [
        ("location.geocoding.forward", "正地理编码", "Forward Geocoding",
         "将地址字符串解析为坐标。",
         ["Geocoder.getFromLocationName、CLGeocoder"],
         ["location.geocoding.reverse"],
         merge_bindings(
             A("Geocoder.getFromLocationName",
               "https://developer.android.com/reference/android/location/Geocoder#getFromLocationName(java.lang.String,%20int)"),
             I("CLGeocoder",
               "https://developer.apple.com/documentation/corelocation/clgeocoder", "class"),
             H("geoLocationManager.getAddressesFromLocationName",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         )),
        ("location.geocoding.reverse", "逆地理编码", "Reverse Geocoding",
         "将坐标解析为地址描述。",
         ["Geocoder.getFromLocation、reverseGeocodeLocation"],
         ["location.geocoding.forward"],
         merge_bindings(
             A("Geocoder.getFromLocation",
               "https://developer.android.com/reference/android/location/Geocoder#getFromLocation(double,%20double,%20int)"),
             I("reverseGeocodeLocation",
               "https://developer.apple.com/documentation/corelocation/clgeocoder/1423626-reversegeocodelocation", "method"),
             H("getAddressesFromLocation",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         )),
        ("location.geocoding.coordinate_convert", "坐标系转换", "Coordinate Convert",
         "不同地理坐标系之间的转换。",
         ["坐标纠偏/转换 API"],
         ["location.geocoding.forward"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("坐标转换",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         )),
        ("location.geocoding.distance", "球面距离计算", "Geodesic Distance",
         "计算两点间大地线距离。",
         ["distanceBetween、distanceFrom"],
         ["location.geocoding.forward"],
         merge_bindings(
             A("Location.distanceBetween",
               "https://developer.android.com/reference/android/location/Location#distanceBetween(double,%20double,%20double,%20double,%20float[])"),
             I("distance(from:)",
               "https://developer.apple.com/documentation/corelocation/cllocation/1423680-distance", "method"),
             pending("harmonyos"),
         )),
        ("location.geocoding.timezone", "时区查询", "Time Zone Lookup",
         "根据坐标查询时区信息。",
         ["TimeZone API / place timezone"],
         ["location.geocoding.reverse"],
         merge_bindings(
             pending("android"),
             I("CLLocation / NSTimeZone",
               "https://developer.apple.com/documentation/foundation/nstimezone", "class"),
             pending("harmonyos"),
         )),
        ("location.geocoding.autocomplete", "地点自动补全", "Place Autocomplete",
         "输入时提示候选地点。",
         ["Places Autocomplete、MKLocalSearchCompleter"],
         ["location.geocoding.forward"],
         merge_bindings(
             A("Places Autocomplete",
               "https://developers.google.com/maps/documentation/places/android-sdk/autocomplete"),
             I("MKLocalSearchCompleter",
               "https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter", "class"),
             H("地点搜索",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-site", "guide"),
         )),
        ("location.geocoding.poi_search", "地点与POI搜索", "POI Search",
         "按关键字/类别搜索周边地点。",
         ["Places search、MKLocalSearch"],
         ["location.geocoding.autocomplete"],
         merge_bindings(
             A("Places Search",
               "https://developers.google.com/maps/documentation/places/android-sdk/search"),
             I("MKLocalSearch",
               "https://developer.apple.com/documentation/mapkit/mklocalsearch", "class"),
             H("site search",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-site", "guide"),
         )),
        ("location.geocoding.place_details", "地点详情", "Place Details",
         "获取地点详细属性与联系信息。",
         ["Place Details"],
         ["location.geocoding.poi_search"],
         merge_bindings(
             A("Place Details",
               "https://developers.google.com/maps/documentation/places/android-sdk/details"),
             I("MKMapItem",
               "https://developer.apple.com/documentation/mapkit/mkmapitem", "class"),
             H("site detail",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-site", "guide"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "location.geocoding", "geocoding_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # heading
    for row in [
        ("location.heading.true_north", "真北航向", "True North Heading",
         "获取相对真北的设备航向。",
         ["heading、trueHeading"],
         ["location.heading.magnetic"],
         merge_bindings(
             A("Sensor.TYPE_ROTATION_VECTOR",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_ROTATION_VECTOR"),
             I("trueHeading",
               "https://developer.apple.com/documentation/corelocation/clheading/1423755-trueheading", "property"),
             H("sensor orientation",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("location.heading.magnetic", "磁北航向", "Magnetic Heading",
         "获取相对磁北的设备航向。",
         ["magneticHeading、TYPE_MAGNETIC_FIELD"],
         ["location.heading.true_north"],
         merge_bindings(
             A("Sensor.TYPE_MAGNETIC_FIELD",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_MAGNETIC_FIELD"),
             I("magneticHeading",
               "https://developer.apple.com/documentation/corelocation/clheading/1423763-magneticheading", "property"),
             H("MAGNETIC_FIELD",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("location.heading.start", "开始航向更新", "Start Heading Updates",
         "启动航向/罗盘更新回调。",
         ["startUpdatingHeading"],
         ["location.heading.stop"],
         merge_bindings(
             A("SensorManager.registerListener",
               "https://developer.android.com/reference/android/hardware/SensorManager#registerListener(android.hardware.SensorEventListener,%20android.hardware.Sensor,%20int)"),
             I("startUpdatingHeading",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1423709-startupdatingheading", "method"),
             H("on",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("location.heading.stop", "停止航向更新", "Stop Heading Updates",
         "停止航向更新以省电。",
         ["stopUpdatingHeading"],
         ["location.heading.start"],
         merge_bindings(
             A("SensorManager.unregisterListener",
               "https://developer.android.com/reference/android/hardware/SensorManager#unregisterListener(android.hardware.SensorEventListener)"),
             I("stopUpdatingHeading",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1423561-stopupdatingheading", "method"),
             H("off",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("location.heading.calibration", "罗盘校准提示", "Heading Calibration",
         "罗盘精度不足时的校准提示回调。",
         ["locationManagerShouldDisplayHeadingCalibration"],
         ["location.heading.true_north"],
         merge_bindings(
             pending("android"),
             I("locationManagerShouldDisplayHeadingCalibration",
               "https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423707-locationmanagershoulddisplayhead", "method"),
             pending("harmonyos"),
         )),
        ("location.heading.accuracy", "航向精度", "Heading Accuracy",
         "查询当前航向精度估计。",
         ["headingAccuracy"],
         ["location.heading.true_north"],
         merge_bindings(
             pending("android"),
             I("headingAccuracy",
               "https://developer.apple.com/documentation/corelocation/clheading/1423739-headingaccuracy", "property"),
             pending("harmonyos"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "location.heading", "heading_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # Extra nodes under thinner branches to reach 60+
    for row in [
        ("location.geofence.polygon", "多边形围栏", "Polygon Geofence",
         "注册多边形区域围栏。",
         ["多边形坐标点围栏"],
         ["location.geofence.region"],
         merge_bindings(
             pending("android", "Geofence 主要为圆形；多边形待核生态 API"),
             pending("ios"),
             H("GeoFence polygon",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         ), "location.geofence", "geofence_capability"),
        ("location.geofence.expiration", "围栏过期", "Geofence Expiration",
         "设置围栏自动过期时间。",
         ["setExpirationDuration"],
         ["location.geofence.add_remove"],
         merge_bindings(
             A("Geofence.Builder.setExpirationDuration",
               "https://developers.google.com/android/reference/com/google/android/gms/location/Geofence.Builder#setExpirationDuration(long)"),
             pending("ios"),
             pending("harmonyos"),
         ), "location.geofence", "geofence_capability"),
        ("location.geocoding.batch", "批量地理编码", "Batch Geocoding",
         "批量地址/坐标互转。",
         ["批量 geocode"],
         ["location.geocoding.forward"],
         merge_bindings(
             A("Geocoder",
               "https://developer.android.com/reference/android/location/Geocoder"),
             I("CLGeocoder",
               "https://developer.apple.com/documentation/corelocation/clgeocoder", "class"),
             pending("harmonyos"),
         ), "location.geocoding", "geocoding_capability"),
        ("location.geocoding.locale", "地理编码区域设置", "Geocoding Locale",
         "按语言/地区偏好返回地址描述。",
         ["Geocoder Locale、CLGeocoder preferredLocale"],
         ["location.geocoding.reverse"],
         merge_bindings(
             A("Geocoder",
               "https://developer.android.com/reference/android/location/Geocoder"),
             I("CLGeocoder",
               "https://developer.apple.com/documentation/corelocation/clgeocoder", "class"),
             pending("harmonyos"),
         ), "location.geocoding", "geocoding_capability"),
        ("location.heading.filter", "航向滤波", "Heading Filter",
         "设置航向更新最小角度变化阈值。",
         ["headingFilter"],
         ["location.heading.start"],
         merge_bindings(
             pending("android"),
             I("headingFilter",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1423537-headingfilter", "property"),
             pending("harmonyos"),
         ), "location.heading", "heading_capability"),
        ("location.heading.orientation_ref", "航向朝向参考", "Heading Orientation Ref",
         "设置航向相对设备朝向的参考系。",
         ["headingOrientation"],
         ["location.heading.true_north"],
         merge_bindings(
             pending("android"),
             I("headingOrientation",
               "https://developer.apple.com/documentation/corelocation/cllocationmanager/1423700-headingorientation", "property"),
             pending("harmonyos"),
         ), "location.heading", "heading_capability"),
        ("location.positioning.mock", "模拟位置测试", "Mock Location Test",
         "开发/测试场景注入模拟位置。",
         ["setMockMode / Xcode simulated location"],
         ["location.positioning.foreground"],
         merge_bindings(
             A("FusedLocationProviderClient.setMockLocation",
               "https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#setMockLocation(android.location.Location)"),
             pending("ios", "Xcode / 模拟器注入，非应用 API"),
             pending("harmonyos"),
         ), "location.positioning", "positioning_capability"),
        ("location.positioning.provider_status", "定位提供者状态", "Provider Status",
         "监听 GPS/网络提供者启用状态变化。",
         ["GnssStatus / ProvidersChanged"],
         ["location.positioning.services_check"],
         merge_bindings(
             A("LocationManager.PROVIDERS_CHANGED_ACTION",
               "https://developer.android.com/reference/android/location/LocationManager#PROVIDERS_CHANGED_ACTION"),
             I("locationManagerDidChangeAuthorization",
               "https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/3563956-locationmanagerdidchangeauthoriz", "method"),
             H("locationEnabledChange",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager"),
         ), "location.positioning", "positioning_capability"),
        ("location.maps.traffic", "路况图层", "Traffic Layer",
         "在地图上显示实时路况。",
         ["isTrafficEnabled"],
         ["location.maps.sdk"],
         merge_bindings(
             A("GoogleMap.setTrafficEnabled",
               "https://developers.google.com/android/reference/com/google/android/gms/maps/GoogleMap#setTrafficEnabled(boolean)"),
             I("MKMapView showsTraffic 类能力",
               "https://developer.apple.com/documentation/mapkit/mkmapview", "class"),
             pending("harmonyos"),
         ), "location.maps", "maps_capability"),
        ("location.maps.building", "建筑物图层", "Building Layer",
         "显示 3D 建筑物或室内图入口。",
         ["isBuildingsEnabled、MKMapFeatureOptions"],
         ["location.maps.sdk"],
         merge_bindings(
             A("GoogleMap.setBuildingsEnabled",
               "https://developers.google.com/android/reference/com/google/android/gms/maps/GoogleMap#setBuildingsEnabled(boolean)"),
             I("MKMapConfiguration",
               "https://developer.apple.com/documentation/mapkit/mkmapconfiguration", "class"),
             pending("harmonyos"),
         ), "location.maps", "maps_capability"),
    ]:
        fid, zh, en, definition, includes, excludes, bindings, parent, axis = row
        f.append(atom(
            fid, parent, axis, zh, en, definition, includes, excludes, bindings,
            privacy="sensitive" if parent.startswith("location.positioning") or parent.startswith("location.geofence") else "none",
        ))

    return list({n["id"]: n for n in f}.values())


def main():
    nodes = build()
    path = write_domain("location", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
