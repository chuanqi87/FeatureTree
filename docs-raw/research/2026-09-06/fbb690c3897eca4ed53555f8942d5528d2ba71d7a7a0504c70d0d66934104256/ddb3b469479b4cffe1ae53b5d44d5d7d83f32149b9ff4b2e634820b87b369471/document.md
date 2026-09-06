# Overview

Select platform:
[Android](https://developers.google.com/maps/documentation/android-sdk/dds-datasets/overview "View this page for the Android platform docs.")
[iOS](https://developers.google.com/maps/documentation/ios-sdk/dds-datasets/overview "View this page for the iOS platform docs.")
[JavaScript](https://developers.google.com/maps/documentation/javascript/dds-datasets/overview "View this page for the JavaScript platform docs.")

Data-driven styling for datasets lets you upload your own geospatial datasets,
apply custom styling to their data features, and display those data features on
maps. With data-driven styling for datasets, you can create data visualizations
based on point, polyline, and polygon geometries, and make data features respond
to tap events. Data-driven styling for datasets is supported on vector maps
only (a map ID is required).

[Get started with data-driven styling for datasets](https://developers.google.com/maps/documentation/ios-sdk/dds-datasets/start)

## Add custom geospatial datasets

Add your custom data using Google Cloud Console or Google Cloud
Shell. Each dataset has a unique ID, which you can associate with a map style.
The following data formats are supported:

* GeoJSON
* Comma-separated (CSV)
* KML

For details about dataset requirements and limitations, see
[Create and manage a dataset](https://developers.google.com/maps/documentation/ios-sdk/dds-datasets/create-dataset#dataset-prerequisites)

### About public datasets

In order to style a dataset you must associate a map style with a map ID, which
also associates the dataset to the map ID. In an app, developers can reference
that map ID, and any map style and geospatial data associated with it. No
additional access control is applied to the geospatial data, making the
geospatial data effectively publicly available to anyone with the app.

## Style data features

Once your custom data has been uploaded and associated to a map
style and map ID, you can style data features for visual impact, and make
features respond to tap events.

Style point data to show specific locations on the map.

![A screenshot showing styled point data.](/static/maps/documentation/javascript/dds-datasets/images/point_data.png)

Style polyline data to highlight geographical features.

![A screenshot showing styled polyline data.](/static/maps/documentation/javascript/dds-datasets/images/polyline_data.png)

Style polygon data to highlight geographical areas.

![A screenshot showing styled polygon data.](/static/maps/documentation/javascript/dds-datasets/images/polygon_data.png)

Make data features respond to tap events by adding an event
listener.

![A screenshot showing a cursor taping a map.](/static/maps/documentation/javascript/dds-datasets/images/feature_click.png)
