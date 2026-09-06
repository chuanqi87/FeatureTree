# Filter which map features to display

Select platform:
[Android](https://developers.google.com/maps/documentation/android-sdk/cloud-customization/viz "View this page for the Android platform docs.")
[Android 3D](https://developers.google.com/maps/documentation/maps-3d/android-sdk/cloud-customization/viz "View this page for the Android 3D platform docs.")
[iOS](https://developers.google.com/maps/documentation/ios-sdk/cloud-customization/viz "View this page for the iOS platform docs.")
[iOS 3D](https://developers.google.com/maps/documentation/maps-3d/ios-sdk/cloud-customization/viz "View this page for the iOS 3D platform docs.")
[JavaScript](https://developers.google.com/maps/documentation/javascript/cloud-customization/viz "View this page for the JavaScript platform docs.")
[Web Service](https://developers.google.com/maps/documentation/maps-static/cloud-customization/viz "View this page for the Web Service platform docs.")

You can filter which specific map features to display by adjusting their
visibility. If you want to control how dense all POIs are on the map, see
[Control the density of Points of interest](https://developers.google.com/maps/documentation/maps-3d/ios-sdk/cloud-customization/poi-behavior-customization).

You customize which points of interest on a map to display by setting the
visibility for a map feature:

1. In the style editor, select the POI map feature you want to display or hide.
   For example, **Points of interest > Lodging**.
2. Under **Visibility**, the visibility is controlled by an eye icon
   visibility toggle.
   Select the eye icon to enable visibility selection, which turns the icon
   blue. The default basemap visibility is shown in gray.

   ![Visibility eye icon toggle displays the default in gray](/static/maps/images/cloud-customization/visibility-default.png)
3. Select the icon again to toggle the visibility between off and on.

   * **On**: Always display this map feature, when the zoom level
     allows.
       
     ![Lodging Visibility is On - hotels are shown](/static/maps/images/cloud-customization/viz-lodging-on.png)
   * **Off**: Never display this map feature.
       
     ![Lodging Visibility is Off - hotels disappear](/static/maps/images/cloud-customization/viz-lodging-off.png)

**Note:** When you hide map features, you may expose boundary inaccuracies. Map
feature boundaries are not always precise, but are adjusted to look correct when
all layers are visible. To learn more about how map layers affect each other,
see [Manage styles that overlap](https://developers.google.com/maps/documentation/maps-3d/ios-sdk/cloud-customization/overlap).
