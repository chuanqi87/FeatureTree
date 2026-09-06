# Use geospatial queries

**Preview**

This product or feature is
subject to the "Pre-GA Offerings Terms" in the General Service Terms section
of the [Service Specific
Terms](https://firebase.google.com/terms/service-terms#1).
Pre-GA products and features are available "as is" and might have limited support.
For more information, see the
[launch stage descriptions](https://cloud.google.com/products/#product-launch-stages).

You can perform geospatial queries in Cloud Firestore to build
location aware services. For example, you can find the distance between a user
and nearby points of interest, sorting them from nearest to farthest.

## Edition requirements

The geospatial query feature requires a Firestore Enterprise edition database.

## Before you begin

To perform a geospatial query, you must first
[create geospatial indexes](https://firebase.google.com/docs/firestore/enterprise/indexing-native#create-geospatial-index) for the fields you need to
search through.

## Run a geospatial query

To perform a geospatial query, use the `geoDistance` expression within the
`query` parameter of the `search(...)` stage.

Only the less than or equals (`<=`) operator is supported. The distance is
measured in meters.

For example, the following query
finds all restaurants within 1,000 meters of the listed geopoint.

### Web

```
firestore.pipeline().collection('restaurants')
  .search({
    query: field('location')
      .geoDistance(new GeoPoint(38.989177, -107.065076))
      .lessThan(1000 /* m */)
  });
```

##### iOS

```
firestore.pipeline().collection("restaurants")
    .search(
        query: Field("location")
            .geoDistance(GeoPoint(latitude: 38.989177, longitude: -107.065076))
            .lessThan(1000)
    )
```

##### Android

```
firestore.pipeline()
        .collection("restaurants")
        .search(new SearchOptions()
                .withQuery(field("location")
                        .geoDistance(new GeoPoint(38.989177, -107.065076))
                        .lessThan(1000 /* meters */)));
```

##### Node.js

```
firestore.pipeline().collection('restaurants')
  .search({
    query: field('location')
      .geoDistance(new GeoPoint(38.989177, -107.065076))
      .lessThan(1000 /* m */)
  });
```
