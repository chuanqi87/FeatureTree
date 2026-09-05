# androidx.compose.ui

# androidx.compose.ui

Common/AllAndroid/JVM


## Interfaces

|  |  |  |
| --- | --- | --- |
| `Alignment` | An interface to calculate the position of a sized box inside an available space. | Cmn |
| `Alignment.Horizontal` | An interface to calculate the position of box of a certain width inside an available width. | Cmn |
| `Alignment.Vertical` | An interface to calculate the position of a box of a certain height inside an available height. | Cmn |
| `Modifier` | An ordered, immutable collection of `modifier elements` that decorate or add behavior to Compose UI elements. | Cmn |
| `Modifier.Element` | A single element contained within a `Modifier` chain. | Cmn |
| `MotionDurationScale` | Provides a duration scale for motion such as animations. | Cmn |
| `UiMediaScope` | A receiver scope that provides access to the properties of the current media environment. | Cmn |

## Classes

|  |  |  |
| --- | --- | --- |
| `BiasAbsoluteAlignment` | An `Alignment` specified by bias: for example, a bias of -1 represents alignment to the left/top, a bias of 0 will represent centering, and a bias of 1 will represent right/bottom. | Cmn |
| `BiasAbsoluteAlignment.Horizontal` | An `Alignment.Horizontal` specified by bias: for example, a bias of -1 represents alignment to the left, a bias of 0 will represent centering, and a bias of 1 will represent right. | Cmn |
| `BiasAlignment` | An `Alignment` specified by bias: for example, a bias of -1 represents alignment to the start/top, a bias of 0 will represent centering, and a bias of 1 will represent end/bottom. | Cmn |
| `BiasAlignment.Horizontal` | An `Alignment.Horizontal` specified by bias: for example, a bias of -1 represents alignment to the start, a bias of 0 will represent centering, and a bias of 1 will represent end. | Cmn |
| `BiasAlignment.Vertical` | An `Alignment.Vertical` specified by bias: for example, a bias of -1 represents alignment to the top, a bias of 0 will represent centering, and a bias of 1 will represent bottom. | Cmn |
| `CombinedModifier` | A node in a `Modifier` chain. | Cmn |
| `FrameRateCategory` | A type-safe representation of a frame rate category for a display or application. | Cmn |
| `Modifier.Node` | The longer-lived object that is created for each `Modifier.Element` applied to a `androidx.compose.ui.layout.Layout`. | Cmn |
| `R` |  | android |
| `R.id` |  | android |
| `UiMediaScope.KeyboardKind` | Describes the kind of keyboard available. | Cmn |
| `UiMediaScope.PointerPrecision` | Describes the precision of the available pointing devices. | Cmn |
| `UiMediaScope.Posture` | Describes the posture of the window, typically on a foldable device. | Cmn |
| `UiMediaScope.ViewingDistance` | Describes the typical distance between the user and the screen. | Cmn |

## Objects

|  |  |  |
| --- | --- | --- |
| `AbsoluteAlignment` | A collection of common `Alignment`s unaware of the layout direction. | Cmn |
| `AndroidComposeUiFlags` | This is a collection of flags which are used to guard against regressions in some of the "riskier" refactors or new feature support that is added to this module. | android |
| `ComposeUiFlags` | This is a collection of flags which are used to guard against regressions in some of the "riskier" refactors or new feature support that is added to this module. | Cmn |
| `Modifier.Companion` | The companion object `Modifier` is the empty, default, or starter `Modifier` that contains no `elements`. | Cmn |
| `MotionDurationScale.Key` |  | Cmn |

## Annotations

|  |  |  |
| --- | --- | --- |
| `ExperimentalComposeUiApi` |  | Cmn |
| `ExperimentalMediaQueryApi` |  | Cmn |
| `InternalComposeUiApi` | Unstable API for use only between `compose-ui` modules sharing the same exact version, subject to change without notice in major, minor, or patch releases. | Cmn |
| `UiComposable` | An annotation that can be used to mark a composable function as being expected to be use in a composable function that is also marked or inferred to be marked as a `UiComposable`. | Cmn |

## Composables

|  |  |  |
| --- | --- | --- |
| `derivedMediaQuery` | Evaluates a query against the current `UiMediaScope`, wrapped in a `derivedStateOf`. | Cmn |
| `mediaQuery` | Evaluates a query against the current `UiMediaScope`. | Cmn |

## Modifiers

|  |  |  |
| --- | --- | --- |
| `composed` | Declare a just-in-time composition of a `Modifier` that will be composed for each element it modifies. | Cmn |
| `keepScreenOn` | A modifier that keeps the device screen on as long as it is part of the composition on supported platforms. | Cmn |
| `preferredFrameRate` | Set a requested frame rate on Composable | Cmn |
| `sensitiveContent` | This modifier hints that the composable renders sensitive content (i.e. username, password, credit card etc) on the screen, and the content should be protected during screen share in supported environments. | Cmn |
| `zIndex` | Creates a modifier that controls the drawing order for the children of the same layout parent. | Cmn |

## Extension functions summary

|  |  |  |
| --- | --- | --- |
| `Modifier` | `Composer.materialize(modifier: Modifier)`  Materialize any instance-specific `composed modifiers` for applying to a raw tree node. | Cmn |
| `inline T` | `@ExperimentalMediaQueryApi <T : Any?> CompositionLocalAccessorScope.mediaQuery(query: UiMediaScope.() -> T)`  Evaluates a query against the current `UiMediaScope` from a `CompositionLocalAccessorScope`. | Cmn |
| `inline T` | `@ExperimentalMediaQueryApi <T : Any?> CompositionLocalConsumerModifierNode.mediaQuery(query: UiMediaScope.() -> T)`  Evaluates a query against the current `UiMediaScope` from a `Modifier.Node`. | Cmn |

## Top-level properties summary

|  |  |  |
| --- | --- | --- |
| `ProvidableCompositionLocal<UiMediaScope>` | `@ExperimentalMediaQueryApi LocalUiMediaScope`  A `UiMediaScope` provides information about the window environment and input devices, enabling adaptive layouts and behavior. | Cmn |

## Extension functions

### Composer.materialize

Cmn

Artifact: [androidx.compose.ui:ui](https://developer.android.com/jetpack/androidx/releases/compose-ui)

[View Source](https://cs.android.com/search?q=file:androidx/compose/ui/ComposedModifier.kt+function:materialize)

Added in [1.5.0](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.5.0)

```
fun Composer.materialize(modifier: Modifier): Modifier
```

Materialize any instance-specific `composed modifiers` for applying to a raw tree node. Call right before setting the returned modifier on an emitted node. You almost certainly do not need to call this function directly.

### CompositionLocalAccessorScope.mediaQuery

Cmn

Artifact: [androidx.compose.ui:ui](https://developer.android.com/jetpack/androidx/releases/compose-ui)

[View Source](https://cs.android.com/search?q=file:androidx/compose/ui/MediaQuery.kt+function:mediaQuery)

Added in [1.12.0](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.12.0)

```
@ExperimentalMediaQueryApi  
inline fun <T : Any?> CompositionLocalAccessorScope.mediaQuery(query: UiMediaScope.() -> T): T
```

Evaluates a query against the current `UiMediaScope` from a `CompositionLocalAccessorScope`.

If called within a snapshot-aware context, the specific property reads within the query will be tracked, and the scope will be invalidated when any of those properties change.

```
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.style.MutableStyleState
import androidx.compose.foundation.style.Style
import androidx.compose.foundation.style.hovered
import androidx.compose.foundation.style.pressed
import androidx.compose.foundation.style.size
import androidx.compose.foundation.style.styleable
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.UiMediaScope.PointerPrecision
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.mediaQuery
import androidx.compose.ui.unit.dp

// Create a styleable clickable box
@Composable
fun ClickableStyleableBox(
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    style: Style = Style,
) {
    val interactionSource = remember { MutableInteractionSource() }
    val styleState = remember { MutableStyleState(interactionSource) }
    Box(
        modifier =
            modifier
                .clickable(interactionSource = interactionSource, onClick = onClick)
                .styleable(styleState, style)
    )
}

ClickableStyleableBox(
    onClick = {},
    style = {
        background(Color.Green)

        // Dynamic size based on window Size
        if (mediaQuery { windowWidth > 600.dp && windowHeight > 400.dp }) {
            size(200.dp)
        } else {
            size(150.dp)
        }

        // Hover state for fine pointer input
        if (mediaQuery { pointerPrecision == PointerPrecision.Fine }) {
            hovered { background(Color.Yellow) }
        }
        pressed { background(Color.Red) }
    },
)
```

| Parameters |
| --- |
| `query: UiMediaScope.() -> T` | A lambda expression with `UiMediaScope` as its receiver, representing the condition to evaluate. |

| Returns |
| --- |
| `T` | The immediate result of the query. |

### CompositionLocalConsumerModifierNode.mediaQuery

Cmn

Artifact: [androidx.compose.ui:ui](https://developer.android.com/jetpack/androidx/releases/compose-ui)

[View Source](https://cs.android.com/search?q=file:androidx/compose/ui/MediaQuery.kt+function:mediaQuery)

Added in [1.12.0](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.12.0)

```
@ExperimentalMediaQueryApi  
inline fun <T : Any?> CompositionLocalConsumerModifierNode.mediaQuery(query: UiMediaScope.() -> T): T
```

Evaluates a query against the current `UiMediaScope` from a `Modifier.Node`.

This function is designed to be used within a `Modifier.Node` that implements `CompositionLocalConsumerModifierNode`.

If called within a snapshot-aware context like `LayoutModifierNode.measure` or `DrawModifierNode.draw` callbacks, the reads within the query will be tracked, and the scope will be invalidated when the properties change.

```
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.style.size
import androidx.compose.runtime.Stable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.Measurable
import androidx.compose.ui.layout.MeasureResult
import androidx.compose.ui.layout.MeasureScope
import androidx.compose.ui.mediaQuery
import androidx.compose.ui.node.CompositionLocalConsumerModifierNode
import androidx.compose.ui.node.LayoutModifierNode
import androidx.compose.ui.node.ModifierNodeElement
import androidx.compose.ui.unit.Constraints
import androidx.compose.ui.unit.constrainHeight
import androidx.compose.ui.unit.constrainWidth
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.offset

// Example of a custom padding modifier that uses [mediaQuery] within a [Modifier.Node].
class AdaptivePaddingNode :
    Modifier.Node(), LayoutModifierNode, CompositionLocalConsumerModifierNode {
    override fun MeasureScope.measure(
        measurable: Measurable,
        constraints: Constraints,
    ): MeasureResult {
        val isLargeScreen = mediaQuery { windowWidth > 600.dp && windowHeight > 400.dp }

        // Adjust padding or size based on the query result
        val extraPadding = if (isLargeScreen) 80.dp.roundToPx() else 16.dp.roundToPx()
        val totalPaddingOnAxis = 2 * extraPadding

        // Measure the content with added padding
        val placeable =
            measurable.measure(constraints.offset(-totalPaddingOnAxis, -totalPaddingOnAxis))

        val width = constraints.constrainWidth(placeable.width + totalPaddingOnAxis)
        val height = constraints.constrainHeight(placeable.height + totalPaddingOnAxis)

        return layout(width, height) { placeable.place(extraPadding, extraPadding) }
    }
}

class AdaptivePaddingElement : ModifierNodeElement<AdaptivePaddingNode>() {
    override fun create() = AdaptivePaddingNode()

    override fun update(node: AdaptivePaddingNode) {}

    override fun equals(other: Any?) = other === this

    override fun hashCode() = 0
}

@Stable fun Modifier.adaptivePadding(): Modifier = this.then(AdaptivePaddingElement())

Box(Modifier.adaptivePadding().background(Color.Blue).size(400.dp))
```

| Parameters |
| --- |
| `query: UiMediaScope.() -> T` | A lambda expression with `UiMediaScope` as its receiver, representing the condition to evaluate. |

| Returns |
| --- |
| `T` | The immediate result of the query. |

## Top-level properties

### LocalUiMediaScope

Cmn

Artifact: [androidx.compose.ui:ui](https://developer.android.com/jetpack/androidx/releases/compose-ui)

[View Source](https://cs.android.com/search?q=file:androidx/compose/ui/MediaQuery.kt+symbol:LocalUiMediaScope)

Added in [1.11.0](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.11.0)

```
@ExperimentalMediaQueryApi  
val LocalUiMediaScope: ProvidableCompositionLocal<UiMediaScope>
```

A `UiMediaScope` provides information about the window environment and input devices, enabling adaptive layouts and behavior. This `CompositionLocal` is the primary mechanism to access the scope within the composable tree.

It is typically provided at the root of an application. Accessing it without a provider will result in a runtime error.
