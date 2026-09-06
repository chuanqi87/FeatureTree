# Unnest

## Description

Generates a new document for each element in an array.

The new documents contain all the fields from the input along with a different
element from the array. The array element is stored to the `alias` given,
potentially overwriting any pre-existing value with the same field name.

Optionally, the `index_field` argument can be specified. When present,
it includes the element's zero-based index from the source array in the output
documents.

This stage behaves similar to `CROSS JOIN UNNEST(...)` in many SQL systems.

## Examples

### Node.js

```
const userScore = await db.pipeline()
    .collection("/users")
    .unnest(field("scores").as("userScore"), /* index_field= */ "attempt")
    .execute();
```

## Behavior

### Alias and Index Field

The `alias` and optional `index_field` will overwrite the
original fields if the fields already exist in the input document. If the
`index_field` is not provided, the output documents won't contain this
field.

For example, for the following collection:

### Node.js

```
await db.collection("users").add({name: "foo", scores: [5, 4], userScore: 0});
await db.collection("users").add({name: "bar", scores: [1, 3], attempt: 5});
```

The `unnest` stage can be used to extract each individual score per user.

### Node.js

```
const userScore = await db.pipeline()
    .collection("/users")
    .unnest(field("scores").as("userScore"), /* index_field= */ "attempt")
    .execute();
```

In this case, `userScore` and `attempt` are both overwritten.

```
  {name: "foo", scores: [5, 4], userScore: 5, attempt: 0}
  {name: "foo", scores: [5, 4], userScore: 4, attempt: 1}
  {name: "bar", scores: [1, 3], userScore: 1, attempt: 0}
  {name: "bar", scores: [1, 3], userScore: 3, attempt: 1}
```



#### Additional examples

##### Swift

```
let results = try await db.pipeline()
  .database()
  .unnest(Field("arrayField").as("unnestedArrayField"), indexField: "index")
  .execute()

PipelineSnippets.swift
```

### Kotlin

```
val results = db.pipeline()
    .database()
    .unnest(field("arrayField").alias("unnestedArrayField"), UnnestOptions().withIndexField("index"))
    .execute()

DocSnippets.kt
```

### Java

```
Task<Pipeline.Snapshot> results = db.pipeline()
    .database()
    .unnest(field("arrayField").alias("unnestedArrayField"), new UnnestOptions().withIndexField("index"))
    .execute();

DocSnippets.java
```

##### Python

```
from google.cloud.firestore_v1.pipeline_expressions import Field
from google.cloud.firestore_v1.pipeline_stages import UnnestOptions

results = (
    client.pipeline()
    .database()
    .unnest(
        Field.of("arrayField").as_("unnestedArrayField"),
        options=UnnestOptions(index_field="index"),
    )
    .execute()
)

firestore_pipelines.py
```

##### Java

```
Pipeline.Snapshot results =
    firestore
        .pipeline()
        .database()
        .unnest("arrayField", "unnestedArrayField", new UnnestOptions().withIndexField("index"))
        .execute()
        .get();

PipelineSnippets.java
```

##### Go

```
snapshot := client.Pipeline().
	Database().
	UnnestWithAlias("arrayField", "unnestedArrayField", firestore.WithUnnestIndexField("index")).
	Execute(ctx)

pipeline_snippets_general.go
```

### Non Array Values

If the input expression evaluates to a non-array value, then this stage will
return the input document as is with the `index_field` set to `NULL`,
if specified.

For example, for the following collection:

### Node.js

```
await db.collection("users").add({name: "foo", scores: 1});
await db.collection("users").add({name: "bar", scores: null});
await db.collection("users").add({name: "qux", scores: {backupScores: 1}});
```

The `unnest` stage can be used to extract each individual score per user.

### Node.js

```
const userScore = await db.pipeline()
    .collection("/users")
    .unnest(field("scores").as("userScore"), /* index_field= */ "attempt")
    .execute();
```

This produces the following documents with `attempt` set to `NULL`.

```
  { name: "foo", scores: 1, attempt: null }
  { name: "bar", scores: null, attempt: null }
  { name: "qux", scores: { backupScores: 1 }, attempt: null }
```



### Empty Array Values

If the input expression evaluates to an empty array, then no document will be
returned for that input document.

For example, for the following collection:

### Node.js

```
await db.collection("users").add({name: "foo", scores: [5, 4]});
await db.collection("users").add({name: "bar", scores: []});
```

The `unnest` stage can be used to extract each individual score per user.

### Node.js

```
const userScore = await db.pipeline()
    .collection("/users")
    .unnest(field("scores").as("userScore"), /* index_field= */ "attempt")
    .execute();
```

This produces the following documents with user `bar` missing from the
output.

```
  {name: "foo", scores: [5, 4], userScore: 5, attempt: 0}
  {name: "foo", scores: [5, 4], userScore: 4, attempt: 1}
```

In order to return documents with empty arrays as well, you can wrap the
unnested value in an array. For example:

### Node.js

```
const userScore = await db.pipeline()
    .collection("/users")
    .unnest(
      conditional(
        equal(field("scores"), []),
        array([field("scores")]),
        field("scores")
      ).as("userScore"),
    /* index_field= */ "attempt")
    .execute();
```

This will now return document with user `bar`.

```
  {name: "foo", scores: [5, 4], userScore: 5, attempt: 0}
  {name: "foo", scores: [5, 4], userScore: 4, attempt: 1}
  {name: "bar", scores: [], userScore: [], attempt: 0}
```



#### Additional examples

##### Node.js

```
    // Input
    // { identifier : 1, neighbors: [ "Alice", "Cathy" ] }
    // { identifier : 2, neighbors: []                   }
    // { identifier : 3, neighbors: "Bob"                }

    const results = await db.pipeline()
      .database()
      .unnest(Field.of("neighbors"), "unnestedNeighbors", "index")
      .execute();

    // Output
    // { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Alice", index: 0 }
    // { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Cathy", index: 1 }
    // { identifier: 3, neighbors: "Bob", index: null}
```

##### Swift

```
// Input
// { identifier : 1, neighbors: [ "Alice", "Cathy" ] }
// { identifier : 2, neighbors: []                   }
// { identifier : 3, neighbors: "Bob"                }

let results = try await db.pipeline()
  .database()
  .unnest(Field("neighbors").as("unnestedNeighbors"), indexField: "index")
  .execute()

// Output
// { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Alice", index: 0 }
// { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Cathy", index: 1 }
// { identifier: 3, neighbors: "Bob", index: null}

PipelineSnippets.swift
```

### Kotlin

```
// Input
// { identifier : 1, neighbors: [ "Alice", "Cathy" ] }
// { identifier : 2, neighbors: []                   }
// { identifier : 3, neighbors: "Bob"                }

val results = db.pipeline()
    .database()
    .unnest(field("neighbors").alias("unnestedNeighbors"), UnnestOptions().withIndexField("index"))
    .execute()

// Output
// { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Alice", index: 0 }
// { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Cathy", index: 1 }
// { identifier: 3, neighbors: "Bob", index: null}

DocSnippets.kt
```

### Java

```
// Input
// { identifier : 1, neighbors: [ "Alice", "Cathy" ] }
// { identifier : 2, neighbors: []                   }
// { identifier : 3, neighbors: "Bob"                }

Task<Pipeline.Snapshot> results = db.pipeline()
    .database()
    .unnest(field("neighbors").alias("unnestedNeighbors"), new UnnestOptions().withIndexField("index"))
    .execute();

// Output
// { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Alice", index: 0 }
// { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Cathy", index: 1 }
// { identifier: 3, neighbors: "Bob", index: null}

DocSnippets.java
```

##### Python

```
from google.cloud.firestore_v1.pipeline_expressions import Field
from google.cloud.firestore_v1.pipeline_stages import UnnestOptions

# Input
# { "identifier" : 1, "neighbors": [ "Alice", "Cathy" ] }
# { "identifier" : 2, "neighbors": []                   }
# { "identifier" : 3, "neighbors": "Bob"                }

results = (
    client.pipeline()
    .database()
    .unnest(
        Field.of("neighbors").as_("unnestedNeighbors"),
        options=UnnestOptions(index_field="index"),
    )
    .execute()
)

# Output
# { "identifier": 1, "neighbors": [ "Alice", "Cathy" ],
#   "unnestedNeighbors": "Alice", "index": 0 }
# { "identifier": 1, "neighbors": [ "Alice", "Cathy" ],
#   "unnestedNeighbors": "Cathy", "index": 1 }
# { "identifier": 3, "neighbors": "Bob", "index": null}

firestore_pipelines.py
```

##### Java

```
// Input
// { "identifier" : 1, "neighbors": [ "Alice", "Cathy" ] }
// { "identifier" : 2, "neighbors": []                   }
// { "identifier" : 3, "neighbors": "Bob"                }

Pipeline.Snapshot results =
    firestore
        .pipeline()
        .database()
        .unnest("neighbors", "unnestedNeighbors", new UnnestOptions().withIndexField("index"))
        .execute()
        .get();

// Output
// { "identifier": 1, "neighbors": [ "Alice", "Cathy" ],
//   "unnestedNeighbors": "Alice", "index": 0 }
// { "identifier": 1, "neighbors": [ "Alice", "Cathy" ],
//   "unnestedNeighbors": "Cathy", "index": 1 }
// { "identifier": 3, "neighbors": "Bob", "index": null}

PipelineSnippets.java
```

##### Go

```
// Input
// { "identifier" : 1, "neighbors": [ "Alice", "Cathy" ] }
// { "identifier" : 2, "neighbors": []                   }
// { "identifier" : 3, "neighbors": "Bob"                }

results, err := client.Pipeline().
	Database().
	UnnestWithAlias("neighbors", "unnestedNeighbors", firestore.WithUnnestIndexField("index")).
	Execute(ctx).Results().GetAll()
if err != nil {
	fmt.Fprintf(w, "GetAll failed: %v", err)
	return err
}

// Output
// { "identifier": 1, "neighbors": [ "Alice", "Cathy" ],
//   "unnestedNeighbors": "Alice", "index": 0 }
// { "identifier": 1, "neighbors": [ "Alice", "Cathy" ],
//   "unnestedNeighbors": "Cathy", "index": 1 }
// { "identifier": 3, "neighbors": "Bob", "index": nil}

pipeline_snippets_general.go
```

### Nested Unnest

In the case the expression evaluates to a nested array, multiple `unnest(...)`
stages must be used to flatten each nested level.

For example, for the following collection:

### Node.js

```
await db.collection("users").add({name: "foo", record: [{scores: [5, 4], avg: 4.5}, {scores: [1, 3], old_avg: 2}]});
```

The `unnest(...)` stage can be used sequentially to extract the innermost array.

### Node.js

```
const userScore = await db.pipeline()
    .collection("/users")
    .unnest(field("record").as("record"))
    .unnest(field("record.scores").as("userScore"), /* index_field= */ "attempt")
    .execute();
```

This produces the following documents:

```
  { name: "foo", record: [{ scores: [5, 4], avg: 4.5 }], userScore: 5, attempt: 0 }
  { name: "foo", record: [{ scores: [5, 4], avg: 4.5 }], userScore: 4, attempt: 1 }
  { name: "foo", record: [{ scores: [1, 3], avg: 2 }], userScore: 1, attempt: 0 }
  { name: "foo", record: [{ scores: [1, 3], avg: 2 }], userScore: 3, attempt: 1 }
```
