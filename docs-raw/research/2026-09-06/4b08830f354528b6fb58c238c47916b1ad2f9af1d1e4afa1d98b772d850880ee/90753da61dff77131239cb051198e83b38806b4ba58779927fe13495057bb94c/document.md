# Drawing Layer (Library)

Drawing library functionality in the Maps JavaScript API is
[deprecated](https://developers.google.com/maps/launch-stages#deprecated). This API was deprecated
in August 2025 and will be made unavailable in a later version of the Maps JavaScript API,
releasing in May 2026. For more information, see
[Deprecations](https://developers.google.com/maps/deprecations).

1. [Overview](https://developers.google.com/maps/documentation/javascript/drawinglayer#overview)
2. [Use the Library](https://developers.google.com/maps/documentation/javascript/drawinglayer#using_the_library)
3. [DrawingManager Options](https://developers.google.com/maps/documentation/javascript/drawinglayer#drawingmanager_options)
4. [Update the Drawing Tools Control](https://developers.google.com/maps/documentation/javascript/drawinglayer#updating_the_drawing_tools_control)
5. [Drawing Events](https://developers.google.com/maps/documentation/javascript/drawinglayer#drawing_events)

## Overview

The `DrawingManager` class provides a graphical interface for users to draw
polygons, rectangles, polylines, circles, and markers on the map.

## Use the Library

The Drawing Tools are a self-contained library, separate from the main Maps
API JavaScript code. To use the functionality contained within this library,
you must first load it using the [`libraries`](https://developers.google.com/maps/documentation/javascript/libraries) parameter in the
Maps API bootstrap URL:

```
<script async
    src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&loading=async&libraries=drawing&callback=initMap">
</script>
```

Once you’ve added the libraries parameter, you can create a `DrawingManager`
object as follows:

```
var drawingManager = new google.maps.drawing.DrawingManager();
drawingManager.setMap(map);
```



## DrawingManager Options

The `DrawingManager` constructor takes a set of options that define the set of
controls to display, the position of the control, and the initial drawing
state.

* The `drawingMode` property of the `DrawingManager` defines the initial
  drawing state of the DrawingManager. It accepts a
  [`google.maps.drawing.OverlayType`](https://developers.google.com/maps/documentation/javascript/reference#OverlayType)
  constant. Default is `null`, in which case the cursor is in a non-drawing
  mode when the DrawingManager is initialized.
* The `drawingControl` property of the `DrawingManager` defines the
  visibility of the drawing tools selection interface on the map. It accepts a
  boolean value.
* You can also define the position of the control, and the types of
  overlays that should be represented in the control, using the
  `drawingControlOptions` property of the `DrawingManager`.
  + `position` defines the position of the drawing control on the map, and
    accepts a [`google.maps.ControlPosition`](https://developers.google.com/maps/documentation/javascript/reference#ControlPosition)
    constant.
  + `drawingModes` is an array of
    [`google.maps.drawing.OverlayType`](https://developers.google.com/maps/documentation/javascript/reference#OverlayType) constants, and
    defines the overlay types to include in the drawing control shape
    picker. The hand icon will always be present, allowing the user to
    interact with the map without drawing. The order of the tools in the
    control will match the order in which they are declared in the array.
* Each type of overlay can be assigned a set of default properties, that
  define the appearance of the overlay when first created. These are defined
  in that overlay’s `{overlay}Options` property (where `{overlay}` represents
  the overlay type). For example, a circle’s fill properties, stroke
  properties, zIndex, and clickability can be defined with the `circleOptions`
  property. If any size, location, or map values are passed, they are ignored.
  For full details of which properties can be set, refer to the
  [API Reference documentation](https://developers.google.com/maps/documentation/javascript/reference#DrawingManagerOptions).

**Note:** To make a shape [user-editable](https://developers.google.com/maps/documentation/javascript/shapes#editable) after it has
been created, set its `editable` property to `true`.

### TypeScript

```
// This example requires the Drawing library. Include the libraries=drawing
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=drawing">

function initMap(): void {
  const map = new google.maps.Map(
    document.getElementById("map") as HTMLElement,
    {
      center: { lat: -34.397, lng: 150.644 },
      zoom: 8,
    }
  );

  const drawingManager = new google.maps.drawing.DrawingManager({
    drawingMode: google.maps.drawing.OverlayType.MARKER,
    drawingControl: true,
    drawingControlOptions: {
      position: google.maps.ControlPosition.TOP_CENTER,
      drawingModes: [
        google.maps.drawing.OverlayType.MARKER,
        google.maps.drawing.OverlayType.CIRCLE,
        google.maps.drawing.OverlayType.POLYGON,
        google.maps.drawing.OverlayType.POLYLINE,
        google.maps.drawing.OverlayType.RECTANGLE,
      ],
    },
    markerOptions: {
      icon: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png",
    },
    circleOptions: {
      fillColor: "#ffff00",
      fillOpacity: 1,
      strokeWeight: 5,
      clickable: false,
      editable: true,
      zIndex: 1,
    },
  });

  drawingManager.setMap(map);
}

declare global {
  interface Window {
    initMap: () => void;
  }
}
window.initMap = initMap;

index.ts
```


**Note:** Read the [guide](https://developers.google.com/maps/documentation/javascript/using-typescript) on using TypeScript and Google Maps.

### JavaScript

```
// This example requires the Drawing library. Include the libraries=drawing
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=drawing">
function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
  const drawingManager = new google.maps.drawing.DrawingManager({
    drawingMode: google.maps.drawing.OverlayType.MARKER,
    drawingControl: true,
    drawingControlOptions: {
      position: google.maps.ControlPosition.TOP_CENTER,
      drawingModes: [
        google.maps.drawing.OverlayType.MARKER,
        google.maps.drawing.OverlayType.CIRCLE,
        google.maps.drawing.OverlayType.POLYGON,
        google.maps.drawing.OverlayType.POLYLINE,
        google.maps.drawing.OverlayType.RECTANGLE,
      ],
    },
    markerOptions: {
      icon: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png",
    },
    circleOptions: {
      fillColor: "#ffff00",
      fillOpacity: 1,
      strokeWeight: 5,
      clickable: false,
      editable: true,
      zIndex: 1,
    },
  });

  drawingManager.setMap(map);
}

window.initMap = initMap;

index.js
```


**Note:** The JavaScript is compiled from the TypeScript snippet.

[View example](https://developers.google.com/maps/documentation/javascript/examples/drawing-tools)

## Update the Drawing Tools Control

Once the `DrawingManager` object has been created, you can update it by
calling `setOptions()` and passing new values.

```
drawingManager.setOptions({
  drawingControlOptions: {
    position: google.maps.ControlPosition.BOTTOM_LEFT,
    drawingModes: ['marker']
  }
});
```

To hide or show the drawing tools control:

```
// To hide:
drawingManager.setOptions({
  drawingControl: false
});

// To show:
drawingManager.setOptions({
  drawingControl: true
});
```

To remove the drawing tools control from the `map` object:

```
drawingManager.setMap(null);
```

*Hiding* the drawing control causes the drawing tools control to not display,
but all of the functionality of the `DrawingManager` class is still available.
In this way, you can implement your own control. *Removing* the
`DrawingManager` from the `map` object disables all drawing functionality; it
must be reattached to the map with `drawingManager.setMap(map)`, or a new
`DrawingManager` object constructed, if drawing features are to be restored.

## Drawing Events

When a shape overlay is created, two events are fired:

* An `{overlay}complete` event (where `{overlay}` represents
  the overlay type, such as `circlecomplete`, `polygoncomplete`, etc). A
  reference to the overlay is passed as an argument.
* An `overlaycomplete` event. An object literal, containing the
  `OverlayType` and a reference to the overlay, is passed as an argument.

```
google.maps.event.addListener(drawingManager, 'circlecomplete', function(circle) {
  var radius = circle.getRadius();
});

google.maps.event.addListener(drawingManager, 'overlaycomplete', function(event) {
  if (event.type == 'circle') {
    var radius = event.overlay.getRadius();
  }
});
```

Note that [`google.maps.Map`](https://developers.google.com/maps/documentation/javascript/reference#Map)
events, such as `click` and `mousemove` are disabled while drawing on the map.
