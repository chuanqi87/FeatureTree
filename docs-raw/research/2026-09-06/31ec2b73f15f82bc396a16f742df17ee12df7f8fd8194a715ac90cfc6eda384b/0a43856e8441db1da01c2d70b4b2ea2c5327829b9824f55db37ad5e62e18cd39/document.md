# UITraitDefinition

A type representing a trait in a trait collection.

```
protocol UITraitDefinition
```

## Overview

All traits contained in a [`UITraitCollection`](/documentation/UIKit/UITraitCollection) conform to this protocol. You can create custom traits by defining your own conforming type.

The example below defines a new trait that holds the value of an integer-based enumeration named `Theme`:

```swift
enum Theme: Int {
    case standard
    case monochrome
}

struct ThemeTrait: UITraitDefinition {
    static let defaultValue = Theme.standard
}
```

The protocol defines default implementations for [`name`](/documentation/UIKit/UITraitDefinition-64c15/name) and [`identifier`](/documentation/UIKit/UITraitDefinition-64c15/identifier) properties. Defining [`defaultValue`](/documentation/UIKit/UITraitDefinition-64c15/defaultValue) is the minimum requirement to conform to this protocol. All properties you implement must be constant. `UITraitDefinition` defines the associated type [`Value`](/documentation/UIKit/UITraitDefinition-64c15/Value) which is the type of [`defaultValue`](/documentation/UIKit/UITraitDefinition-64c15/defaultValue).

The best candidates for trait values are simple value types, such as <doc://com.apple.documentation/documentation/Swift/Bool>, <doc://com.apple.documentation/documentation/Swift/Int>, <doc://com.apple.documentation/documentation/Swift/Double>, and enumerations with an <doc://com.apple.documentation/documentation/Swift/Int> raw value. You can also use lightweight structures as trait values. The system frequently tests trait values for equality, so structures need an efficient implementation of `Equatable`. Avoid using Swift classes as trait values.

If you use your custom trait to implement custom dynamic colors, implement [`affectsColorAppearance`](/documentation/UIKit/UITraitDefinition-64c15/affectsColorAppearance) and return `true`. Returning `true` tells the system to update and redraw views automatically when the trait changes. The system responds to changes to your trait similar to changes in system traits contained in [`systemTraitsAffectingColorAppearance`](/documentation/UIKit/UITraitCollection/systemTraitsAffectingColorAppearance-64z7q). Changes to traits that affect color appearance are more expensive, so opt in to this behavior only when necessary, and change such traits infrequently.

For each custom trait, define extensions on [`UIMutableTraits`](/documentation/UIKit/UIMutableTraits-13ja5) and [`UITraitCollection`](/documentation/UIKit/UITraitCollection) to enable reading and modifying your custom traits with standard property syntax. The example below shows extensions for the example `Theme` trait.

```swift
extension UITraitCollection {
    var theme: Theme { self[ThemeTrait.self] }
}

extension UIMutableTraits {
    var theme: Theme {
        get { self[ThemeTrait.self] }
        set { self[ThemeTrait.self] = newValue }
    }
}
```

A trait type serves as a unique key, identifying a trait within a trait collection. Methods such as [`subscript(_:)`](/documentation/UIKit/UITraitCollection/subscript(_:)-6cdgq) take a trait type to identify the trait in a collection.

Traits defined in Swift aren’t automatically bridged to Objective-C. If you need to access your custom trait from both Swift and Objective-C code, define the trait in both languages. For details, see the Objective-C documentation for [`UITraitDefinition`](/documentation/UIKit/UITraitDefinition-3572h).

## Topics

### Associated Types

[`Value`](/documentation/UIKit/UITraitDefinition-64c15/Value)

### Type Properties

[`affectsColorAppearance`](/documentation/UIKit/UITraitDefinition-64c15/affectsColorAppearance)

[`defaultValue`](/documentation/UIKit/UITraitDefinition-64c15/defaultValue)

[`identifier`](/documentation/UIKit/UITraitDefinition-64c15/identifier)

[`name`](/documentation/UIKit/UITraitDefinition-64c15/name)

## Relationships

### Conforming Types

[`UITraitActiveAppearance-swift.struct`](/documentation/UIKit/UITraitActiveAppearance-swift.struct)

[`UITraitPreferredContentSizeCategory-swift.struct`](/documentation/UIKit/UITraitPreferredContentSizeCategory-swift.struct)

[`UITraitUserInterfaceLevel-swift.struct`](/documentation/UIKit/UITraitUserInterfaceLevel-swift.struct)

[`UITraitImageDynamicRange-swift.struct`](/documentation/UIKit/UITraitImageDynamicRange-swift.struct)

[`UITraitDisplayScale-swift.struct`](/documentation/UIKit/UITraitDisplayScale-swift.struct)

[`UITraitListEnvironment-swift.struct`](/documentation/UIKit/UITraitListEnvironment-swift.struct)

[`UITraitLegibilityWeight-swift.struct`](/documentation/UIKit/UITraitLegibilityWeight-swift.struct)

[`UITraitUserInterfaceStyle-swift.struct`](/documentation/UIKit/UITraitUserInterfaceStyle-swift.struct)

[`UITraitLayoutDirection-swift.struct`](/documentation/UIKit/UITraitLayoutDirection-swift.struct)

[`UITraitSplitViewControllerLayoutEnvironment-swift.struct`](/documentation/UIKit/UITraitSplitViewControllerLayoutEnvironment-swift.struct)

[`UITraitSceneCaptureState-swift.struct`](/documentation/UIKit/UITraitSceneCaptureState-swift.struct)

[`UITraitSystemPrefersReducedResourceUsage-swift.struct`](/documentation/UIKit/UITraitSystemPrefersReducedResourceUsage-swift.struct)

[`UITraitHDRHeadroomUsageLimit-swift.struct`](/documentation/UIKit/UITraitHDRHeadroomUsageLimit-swift.struct)

[`UITraitHorizontalSizeClass-swift.struct`](/documentation/UIKit/UITraitHorizontalSizeClass-swift.struct)

[`UITraitVerticalSizeClass-swift.struct`](/documentation/UIKit/UITraitVerticalSizeClass-swift.struct)

[`UITraitUserInterfaceIdiom-swift.struct`](/documentation/UIKit/UITraitUserInterfaceIdiom-swift.struct)

[`UITraitToolbarItemPresentationSize-swift.struct`](/documentation/UIKit/UITraitToolbarItemPresentationSize-swift.struct)

[`UITraitTabAccessoryEnvironment-swift.struct`](/documentation/UIKit/UITraitTabAccessoryEnvironment-swift.struct)

[`UITraitResolvesNaturalAlignmentWithBaseWritingDirection-swift.struct`](/documentation/UIKit/UITraitResolvesNaturalAlignmentWithBaseWritingDirection-swift.struct)

[`UITraitTypesettingLanguage-swift.struct`](/documentation/UIKit/UITraitTypesettingLanguage-swift.struct)

[`UITraitDisplayGamut-swift.struct`](/documentation/UIKit/UITraitDisplayGamut-swift.struct)

[`UITraitForceTouchCapability-swift.struct`](/documentation/UIKit/UITraitForceTouchCapability-swift.struct)

[`UITraitAccessibilityContrast-swift.struct`](/documentation/UIKit/UITraitAccessibilityContrast-swift.struct)

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
