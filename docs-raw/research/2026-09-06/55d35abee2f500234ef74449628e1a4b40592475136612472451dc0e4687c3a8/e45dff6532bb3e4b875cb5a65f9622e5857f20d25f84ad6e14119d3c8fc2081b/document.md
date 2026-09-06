# Pricing examples

This page includes examples of how billing units are calculated in
some of the most common scenarios. Note that each query might differ in data
processed based on factors such as the query plan, the shape of the data,
and the indexes available.

We recommend using the [Query Explain](https://firebase.google.com/docs/firestore/enterprise/query-explain) feature to better
understand the cost and performance of your specific queries.

## Read operations

Most read operations entail either performing a point read of a specific
document or scanning a range of data based on an identifier. Read operations
consume read units. See the following examples.

### Full-text Search

Charges for full-text search queries are distinguished between the cost to
perform a search on a text index and the cost to retrieve the documents. The
cost to perform a search on a text index is determined by the complexity of the
query and the amount of data scanned in the index to find the results. Factors
influencing this cost include the number and nature of search terms (e.g. terms,
phrases), whether relevance scoring is applied, and the number of index entries
that need to be examined. The cost for retrieving relevant documents is based on
the number and size of documents fetched after the search phase is complete.

The following table delineates the charges associated with executing full-text
search queries for an ecommerce product catalog for a plant nursery. This
example assumes a collection of 200,000 product listings in a collection, with
each product listing document being 2KiB, and a corresponding text search index
size of approximately 100MiB.

| Query | Code Example | Estimated Read Units Consumed Per Query | Estimated Costs (region: us-central1 in USD) |
| --- | --- | --- | --- |
| Search for a rare "dry water" stack flat tray product, resulting in the retrieval of 3 documents. | ``` db.products.find(   {$text: {$search: '"dry water" stack flat'}} ); ``` | 10 total read units  Based on 7 units for full-text search and 3 additional units for the returned documents. | $0.50 per million queries |
| Search for all indoor citrus trees, resulting in the retrieval of 36 documents. | ``` db.products.find(   {$text: {$search: '"indoor" "citrus" "tree"'}} ); ``` | 42 total read units  Based on 6 units for full-text search and 36 additional units for the returned documents. | $2.10 per million queries |
| Search for balcony planters where there are lots of product matches. Sort results by relevance, and limit to the top 50 search results. | ``` db.products.find(   {$text: {$search: 'balcony planter'}} ).sort({score: {$meta: "textScore"}}).limit(50); ``` | 75 total read units  Based on 25 units for full-text search and 50 additional units for the returned documents. | $3.75 per million queries |

These examples illustrate how different query patterns impact costs:

* The **"dry water" query** involves a phrase (`"dry water"`) and additional
  terms. Phrase searches are more complex as the query engine needs to check
  token proximity and order, contributing to the 7 read units for the search
  phase. Since very few documents match, document retrieval cost is low.
* The **"indoor" "citrus" "tree" query** searches for three separate terms.
  While slightly less complex per term than a phrase search, it still requires
  looking up multiple tokens. It has a slightly lower search index scan cost
  of 6 read units, than the "dry water" example, but 36 documents are
  returned, increasing the total cost.
* The **balcony planter query** has the highest full-text search cost of 25
  units by a significant margin. This is primarily because it requests results
  to be sorted by relevance (`.sort({score: {$meta: "textScore"}})` ) on terms
  that match many documents. To determine the top 50 most relevant results,
  the query engine must find *all* potential matches for "balcony" or
  "planter", calculate a relevance score for each, and then sort them. This
  scoring and sorting process across a large number of candidates within the
  index is computationally intensive, even though only 50 documents are
  ultimately retrieved. The broadness of the terms combined with the overhead
  of relevance scoring makes the search phase more expensive.

### Geospatial Queries

Charges for geospatial queries are determined by the complexity of the query
and the specific conditions and sorting utilized, as well as the resources
required to scan all the data in the relevant geospatial index.

The following table delineates the charges associated with executing geospatial
queries for a maps application. This example assumes a collection of 1,000,000
documents representing points of interest, with each point of interest document
being 1KiB, and a corresponding geospatial index size of approximately 60MiB.

| Query | Code Example | Estimated Read Units Consumed Per Query | Estimated Costs (region: us-central1 in USD) |
| --- | --- | --- | --- |
| Find all points of interest within a maximum of 10km, returning 10 matches. | ``` db.pois.find(   {location: {     $near: {       $geometry: <point>,       $maxDistance: 10000     }}}) ``` | 16 total read units.  Based on 6 read units for geospatial query and 10 additional units for the returned documents. | $0.80 per million queries |
| Find all points of interests with a maximum distance of 100km, and return the top 10 closest points of interest out of 1,000 matches | ``` db.pois.find(   {location: {     $near: {       $geometry: <point>,       $maxDistance: 100000     }}}).limit(10) ``` | 19 total read units.  Based on 9 read units for geospatial query and 10 additional units for the returned documents. | $0.95 per million queries |

These examples illustrate how different query patterns impact costs:

* **10km Radius Query**: This query scans a smaller geographic area. Since it
  finds only 10 matches within this 10km radius, the query engine has to do
  less work to identify and order these points by distance (as `$near`
  implicitly does). This results in a lower index scan cost of 6 read units.
* **100km Radius Query**: This query covers a much larger area. The query
  finds 1,000 potential matches within the 100km radius. To fulfill the
  request for the top 10 closest points, the query engine needs to calculate
  distances and sort a much larger set of candidates (up to 1,000 points)
  within the index. This additional computational work of sifting through and
  ranking many more points is why the geospatial query cost is higher at 9
  read units, compared to the 10km query, despite also returning only 10
  documents.

### Point reads

Example billing for point reads:

* Point read of a single 1 KiB document. Consumes: 1 read unit
* Point read of a single 4 KiB document. Consumes: 1 read unit
* Point read of a single 1 MiB document. Consumes: 256 read units
* Point read of 100 documents, 1 KiB each. Consumes: 100 read units

### Scanning

The following examples include scenarios that scan documents or index entries.

#### Scanning Documents

* Query which scans 100 documents, 1 KiB each. Consumes: 25 read units

#### Scanning indexes

The scanning cost, in terms of bytes, is the same regardless of whether it is a
document or index being scanned. However, index entries are often smaller
in size. As a result, they can often provide a more cost effective way of scanning data.

* Query which scans 100 index entries, 1 KiB each. Consumes: 25 read units.
* Query which scans 100 index entries, 128 bytes each. Consumes: 4 read units.

### Minimum document or index entry size

In certain situations it may not be necessary to read the contents of a
document or index entry to satisfy a query. This includes simple count queries
like counting the total number of documents in a collection.
In these situations, a minimum cost of 32 bytes applies per item scanned.

* Count the number of documents in a collection. The query scans 1000
  items in the collection. Consumes: 8 read units.

### Combination of scanning and point reads

Many queries perform a combination of scanning and point reads to satisfy an
operation.

* Query which scans 128 index entries, 256 bytes each and performs a
  point read of 128 documents, 4 KiB each. Consumes: 136 read units, comprised of:
  + 128 read units for point reads
  + 8 read units for index scans

### Query Explain

[Query Explain](https://firebase.google.com/docs/firestore/enterprise/query-explain) helps you understand how the database
executes your queries. The details provided can help you optimize your
queries.

The following costs apply when using Query Explain:

* Query Explain which executes the query: Query cost applies.
* Query Explain using plan only option. Consumes: 1 read unit (minimum cost of a query)

## Write operations

Write operations (creates, updates and deletes) are charged based on the
size of the documents and indexes being created, modified, or deleted during the
operation. Write operations consume write units. Write units are calculated in 1
KiB tranches.

Simple write operations, like update by document ID, only incur the cost of the writes.
Write operations which require querying to satisfy the operation will
additionally incur the read costs associated with the query.

See the following examples.

### Creates

* Create a new 10 KiB document with no indexes. Consumes: 10 write units
* Create a 1 KiB document with 1 index entry of 256 bytes on the collection. Consumes: 2
  write units

### Updates

* Find a 10 KiB document by document ID and update with no indexes on the
  collection. Consumes: 10 write units
* Find a 1 KiB document by document ID and update 1 field with 1 index entry of 256 bytes. Consumes: 3 write units. Note: Updating an index entry in this
  situation consumes 2 write units – one to delete and one to recreate the
  index entry.
* Find a 1 KiB document by document ID and update nothing (no changes). Consumes: 1
  write units (the minimum write costs)
* Query all 1 KiB documents in a collection, which scans 1,000 documents, and
  insert a new 256 bytes field with no indexes on the collection: 1000 read
  units and 1000 writes units.

### Deletes

* Delete a 1 KiB document, which has 1 index on the collection. Consumes: 2 write units
* Delete a 1 KiB document, which has no indexes on the collection. Consumes: 1 write unit

## Index builds

Index builds charge for the index entries created or modified during the build
operation. These costs are incurred anytime an index definition is added or
removed. The index entries are billed identically to writes incurring 1 write
unit per 1KiB.

* Create a new index for a collection containing 500 documents, index
  entries created are 1 KiB each. Consumes 500 write units.
* Delete an existing index for a collection containing 500 documents,
  index entries deleted are 1KiB each. Consumes 500 write units.
