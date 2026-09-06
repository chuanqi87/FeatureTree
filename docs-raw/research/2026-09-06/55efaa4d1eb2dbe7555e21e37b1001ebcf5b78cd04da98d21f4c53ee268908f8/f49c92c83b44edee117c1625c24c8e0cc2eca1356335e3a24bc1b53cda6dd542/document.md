# Select

## Description

Generates new documents, either by referencing a subset of existing fields, or
by assigning a field to the result of a given expression.

## Examples

### Web

```
const result = await execute(db.pipeline()
  .collection("books")
  .select(field("soldBooks").multiply(field("price")).round().as("partialRevenue"))
  .aggregate(field("partialRevenue").sum().as("totalRevenue"))
  );

test.firestore.js
```

##### Swift

```
let result = try await db.pipeline()
  .collection("books")
  .select([Field("soldBooks").multiply(Field("price")).round().as("partialRevenue")])
  .aggregate([Field("partialRevenue").sum().as("totalRevenue")])
  .execute()

PipelineSnippets.swift
```

### Kotlin

```
val result = db.pipeline()
    .collection("books")
    .select(Expression.multiply(field("soldBooks"), field("price")).round().alias("partialRevenue"))
    .aggregate(AggregateFunction.sum("partialRevenue").alias("totalRevenue"))
    .execute()

DocSnippets.kt
```

### Java

```
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(Expression.multiply(field("soldBooks"), field("price")).round().alias("partialRevenue"))
    .aggregate(AggregateFunction.sum("partialRevenue").alias("totalRevenue"))
    .execute();

DocSnippets.java
```

##### Python

```
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("soldBooks")
        .multiply(Field.of("price"))
        .round()
        .as_("partialRevenue")
    )
    .aggregate(Field.of("partialRevenue").sum().as_("totalRevenue"))
    .execute()
)

firestore_pipelines.py
```

##### Java

```
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(round(multiply(field("soldBooks"), field("price"))).as("partialRevenue"))
        .aggregate(sum("partialRevenue").as("totalRevenue"))
        .execute()
        .get();

PipelineSnippets.java
```

##### Go

```
snapshot := client.Pipeline().
	Collection("books").
	Select(firestore.Fields(
		firestore.Round(firestore.Multiply(firestore.FieldOf("soldBooks"), firestore.FieldOf("price"))).As("partialRevenue"),
	)).
	Aggregate(firestore.Accumulators(
		firestore.Sum("partialRevenue").As("totalRevenue"),
	)).
	Execute(ctx)

pipeline_snippets_arithmetic.go
```

## Behavior

### Document Metadata Fields

The `select(...)` stage only emits the fields or expressions explicitly
specified in the stage. This is a divergence from Core operations
where the `select(...)` setting on a query acts as a property mask rather than a
projection and also **always** includes the document's metadata fields of
`__name__`, `__create_time__`, and `__update_time__`.

To get Core operations-style behavior in a `select(...)` the fields
must be explicitly specified like:

### Node.js

```
const results = await db.pipeline()
  .collection("/users")
  .select(
    field("__name__"),
    field("__create_time__"),
    field("__update_time__"),
    field("email"))
  .execute();
```

### Position of a Select Stage

There are no restrictions on when a select stage can be used, but any fields not
included in a select stage won't be accessible to subsequent stages in a
pipeline. For example, to select only the `name` and `location` fields of all
cities in Canada from the following dataset:

### Node.js

```
await db.collection("cities").doc("SF").set({
  name: "San Francisco",
  population: 800000,
  location: {country: "USA", state: "California"}
});

await db.collection("cities").doc("TO").set({
  name: "Toronto",
  population: 3000000,
  location: {country: "Canada", province: "Ontario"}
});
```

The following pipeline can be used:

### Node.js

```
const names = await db.pipeline()
  .collection("/cities")
  .where(equal(field("location.country"), "Canada"))
  .select(stringConcat(field("name"), ", ", field("location.country")).as("name"), "population")
  .execute();
```

Which produces the following documents:

```
{ name: "Toronto, Canada", population: 3000000 },
```

However, if the `select(...)` stage is instead placed before the
[`where(...)`](https://firebase.google.com/docs/firestore/pipelines/stages/transformation/where) stage, like:

### Node.js

```
const names = await db.pipeline()
  .collection("/cities")
  .select(stringConcat(field("name"), ",", field("location.country")).as("name"), "population")
  .where(equal(field("location.country"), "Canada"))
  .execute();
```

No documents will be produced, because `location.country` has been removed from
the document before the execution of the [`where(...)`](https://firebase.google.com/docs/firestore/pipelines/stages/transformation/where)
stage.

### Select Nested Fields

The `select(...)` stage can be used to select nested fields from both maps and
arrays. For example, to select the nested `country` field and first entry of the
`landmarks` array from the following documents:

### Node.js

```
await db.collection("cities").doc("SF").set({
  name: "San Francisco",
  population: 800000,
  location: { country: "USA", state: "California" },
  landmarks: [ "Golden Gate Bridge", "Alcatraz" ]
});

await db.collection("cities").doc("TO").set({
  name: "Toronto",
  population:  3000000,
  province: "ON",
  location: { country: "Canada", province: "Ontario" },
  landmarks: [ "CN Tower", "Casa Loma" ]
});

await db.collection("cities").doc("AT").set({
  name: "Atlantis",
  population: null
});
```

The following pipeline can be used:

### Node.js

```
const locations = await db.pipeline()
  .collection("/cities")
  .select(
    field("name").as("city"),
    field("location.country").as("country"),
    field("landmarks").offset(0).as("topLandmark"))
  .execute();
```

Which produces the following documents:

```
{ city: "San Francisco", country: "USA", topLandmark: "Golden Gate Bridge" },
{ city: "Toronto", country: "Canada", topLandmark: "CN Tower" },
{ city: "Atlantis" }
```

If a nested map value or array value does not exist, it is not included in the
resulting document. Array and map access in the select stage behaves identically
to the [`offset(...)`](https://firebase.google.com/docs/firestore/pipelines/stages/transformation/offset) and `get_field(...)` functions,
respectively.

### Assign Nested Fields

The result of an expression can also be assigned to a nested field, making it
possible to have the `select(...)` stage return a subset of nested fields from
the previous stage. For example the following can be used to ensure only the
`city` & `state` information is returned while still preserving the document's
original shape:

### Node.js

```
const results = await db.pipeline()
  .collection("/users")
  .addFields(
    field("__name__"),
    field("address.city").as("address.city"),
    field("address.state").as("address.state"))
  .execute();
```
