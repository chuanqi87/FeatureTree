# Control Positioning

This example demonstrates custom positioning of the map controls. The zoom
control options are placed on the left of the map and the map type controls are
placed along the top of the map.

Read the
[documentation](https://developers.google.com/maps/documentation/javascript/controls#ControlPositioning).




### TypeScript

```
const mapElement = document.querySelector('gmp-map')!;
let innerMap: google.maps.Map;

async function init() {
    // Request needed libraries.
    const [{ MapTypeControlStyle }, { ControlPosition }] = await Promise.all([
        google.maps.importLibrary('maps'),
        google.maps.importLibrary('core'),
    ]);

    // Get the inner map.
    innerMap = mapElement.innerMap;

    // Set the map's controls options.
    innerMap.setOptions({
        mapTypeControl: true,
        mapTypeControlOptions: {
            style: MapTypeControlStyle.HORIZONTAL_BAR,
            position: ControlPosition.BLOCK_START_INLINE_CENTER,
        },
        zoomControl: true,
        zoomControlOptions: {
            position: ControlPosition.INLINE_START_BLOCK_CENTER,
        },
        scaleControl: true,
        streetViewControl: true,
        streetViewControlOptions: {
            position: ControlPosition.INLINE_START_BLOCK_START,
        },
        fullscreenControl: true,
    });
}

void init();

index.ts
```


**Note:** Read the [guide](https://developers.google.com/maps/documentation/javascript/using-typescript) on using TypeScript and Google Maps.

### JavaScript

```
const mapElement = document.querySelector('gmp-map');
let innerMap;

async function init() {
    // Request needed libraries.
    const [{ MapTypeControlStyle }, { ControlPosition }] = await Promise.all([
        google.maps.importLibrary('maps'),
        google.maps.importLibrary('core'),
    ]);

    // Get the inner map.
    innerMap = mapElement.innerMap;

    // Set the map's controls options.
    innerMap.setOptions({
        mapTypeControl: true,
        mapTypeControlOptions: {
            style: MapTypeControlStyle.HORIZONTAL_BAR,
            position: ControlPosition.BLOCK_START_INLINE_CENTER,
        },
        zoomControl: true,
        zoomControlOptions: {
            position: ControlPosition.INLINE_START_BLOCK_CENTER,
        },
        scaleControl: true,
        streetViewControl: true,
        streetViewControlOptions: {
            position: ControlPosition.INLINE_START_BLOCK_START,
        },
        fullscreenControl: true,
    });
}

void init();

index.js
```

### CSS

```
/* 
 * Optional: Makes the sample page fill the window. 
 */
html,
body {
    height: 100%;
    margin: 0;
    padding: 0;
}

style.css
```

### HTML

```
<html>
    <head>
        <title>Control Positioning</title>

        <link rel="stylesheet" type="text/css" href="./style.css" />
        <script type="module" src="./index.js"></script>
        <script>
            // prettier-ignore
            (g=>{var h,a,k,p="The Google Maps JavaScript API",c="google",l="importLibrary",q="__ib__",m=document,b=window;b=b[c]||(b[c]={});var d=b.maps||(b.maps={}),r=new Set,e=new URLSearchParams,u=()=>h||(h=new Promise(async(f,n)=>{await (a=m.createElement("script"));e.set("libraries",[...r]+"");for(k in g)e.set(k.replace(/[A-Z]/g,t=>"_"+t[0].toLowerCase()),g[k]);e.set("callback",c+".maps."+q);a.src=`https://maps.${c}apis.com/maps/api/js?`+e;d[q]=f;a.onerror=()=>h=n(Error(p+" could not load."));a.nonce=m.querySelector("script[nonce]")?.nonce||"";m.head.append(a)}));d[l]?console.warn(p+" only loads once. Ignoring:",g):d[l]=(f,...n)=>r.add(f)&&u().then(()=>d[l](f,...n))})({
                key: "GOOGLE_MAPS_API_KEY"
            });
        </script>
    </head>
    <body>
        <gmp-map center="-28.643387, 153.612224" zoom="12"></gmp-map>
    </body>
</html>

index.html
```

### Clone Sample

Git and Node.js are required to run this sample locally. Follow these [instructions](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
to install Node.js and NPM. The following commands clone, install dependencies and start the sample application.

```
  git clone https://github.com/googlemaps-samples/js-api-samples.git
  cd samples/control-positioning
  npm i
  npm start
```
