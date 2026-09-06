# Modeling data

Configure the data model file to contain your app’s object graph.

## Discussion

A data model holds information about your application’s objects and the graph of how objects relate to each other. You provide this information in your project’s `.xcdatamodeld` file package. To add a data model to your project, see [Creating a Core Data model](/documentation/CoreData/creating-a-core-data-model).

This screenshot shows the data model for an app that displays a feed of earthquake data.

![A screenshot showing an .xcdatamodeld file containing a Quake entity with code, magnitude, place, and time attributes.](images/com.apple.coredata/media-3839155@2x.png)

Model your data by describing your objects as entities, adding their properties as attributes and relationships, and finally generating respective [`NSManagedObject`](/documentation/CoreData/NSManagedObject) subclasses to inherit change tracking and life cycle management.

## Topics

### Configuring a Core Data Model

[Configuring Entities](/documentation/CoreData/configuring-entities)

Model your app’s objects.

[Configuring Attributes](/documentation/CoreData/configuring-attributes)

Describe the properties that compose an entity.

[Configuring Relationships](/documentation/CoreData/configuring-relationships)

Specify how entities relate and how change propagates between them.

[Generating code](/documentation/CoreData/generating-code)

Automatically or manually generate managed object subclasses from entities.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
