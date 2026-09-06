# android.view.accessibility

Added in [API level 4](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# android.view.accessibility

---

[Kotlin](https://developer.android.com/reference/kotlin/android/view/accessibility/package-summary "View this page in Kotlin")
|Java

The classes in this package are used to represent screen content and changes to it
as well as APIs for querying the global accessibility state of the system.

`AccessibilityEvent`s are sent by the system when
something notable happens in the user interface. For example, when a
`Button` is clicked, a `View` is focused, etc.

`AccessibilityRecord` contains information
about state change of its source `View`. When a view fires
an accessibility event it requests from its parent to dispatch the
constructed event. The parent may optionally append a record for itself for
providing more context to `AccessibilityService`s.
Hence, accessibility services can facilitate additional accessibility records
to enhance feedback.

`AccessibilityNodeInfo` represents a node of the
window content as well as actions that can be requested from its source. From the point
of view of an `AccessibilityService` a window content is
presented as tree of accessibility node info which may or may not map one-to-one
to the view hierarchy. In other words, a custom view is free to report itself as
a tree of accessibility node info.

`AccessibilityManager` is a system level service that
serves as an event dispatch for `AccessibilityEvent`s,
and provides facilities for querying the accessibility state of the system. Accessibility
events are generated when something notable happens in the user interface, for example an
`Activity` starts, the focus or selection of a `View`
changes etc. Parties interested in handling accessibility events implement and register an
accessibility service which extends `AccessibilityService`.

### Developer Guides

For more information about making applications accessible, read the
[Accessibility](https://developer.android.com/guide/topics/ui/accessibility)
developer guide.

## Interfaces

|  |  |
| --- | --- |
| [AccessibilityEventSource](https://developer.android.com/reference/android/view/accessibility/AccessibilityEventSource) | This interface is implemented by classes source of `AccessibilityEvent`s. |
| [AccessibilityManager.AccessibilityServicesStateChangeListener](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager.AccessibilityServicesStateChangeListener) | Listener for changes to the state of accessibility services. |
| [AccessibilityManager.AccessibilityStateChangeListener](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager.AccessibilityStateChangeListener) | Listener for the system accessibility state. |
| [AccessibilityManager.AudioDescriptionRequestedChangeListener](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager.AudioDescriptionRequestedChangeListener) | Listener for the audio description by default state. |
| [AccessibilityManager.HighContrastTextStateChangeListener](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager.HighContrastTextStateChangeListener) | Listener for the system high contrast text state. |
| [AccessibilityManager.TouchExplorationStateChangeListener](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager.TouchExplorationStateChangeListener) | Listener for the system touch exploration state. |

## Classes

|  |  |
| --- | --- |
| [AccessibilityEvent](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent) | This class represents accessibility events that are sent by the system when something notable happens in the user interface. |
| [AccessibilityManager](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager) | System level service that serves as an event dispatch for `AccessibilityEvent`s, and provides facilities for querying the accessibility state of the system. |
| [AccessibilityNodeInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo) | This class represents a node of the window content as well as actions that can be requested from its source. |
| [AccessibilityNodeInfo.AccessibilityAction](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.AccessibilityAction) | A class defining an action that can be performed on an `AccessibilityNodeInfo`. |
| [AccessibilityNodeInfo.CollectionInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.CollectionInfo) | Class with information if a node is a collection. |
| [AccessibilityNodeInfo.CollectionInfo.Builder](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.CollectionInfo.Builder) | The builder for CollectionInfo. |
| [AccessibilityNodeInfo.CollectionItemInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.CollectionItemInfo) | Class with information if a node is a collection item. |
| [AccessibilityNodeInfo.CollectionItemInfo.Builder](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.CollectionItemInfo.Builder) | Builder for creating `CollectionItemInfo` objects. |
| [AccessibilityNodeInfo.ExtraRenderingInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.ExtraRenderingInfo) | Class with information of a view useful to evaluate accessibility needs. |
| [AccessibilityNodeInfo.ExtraRenderingInfo.Builder](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.ExtraRenderingInfo.Builder) | The builder for ExtraRenderingInfo. |
| [AccessibilityNodeInfo.MathInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.MathInfo) | A class that holds information about a node that represents a mathematical expression. |
| [AccessibilityNodeInfo.RangeInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.RangeInfo) | Class with information if a node is a range. |
| [AccessibilityNodeInfo.Selection](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.Selection) | Represents a selection of content that may extend across more than one `AccessibilityNodeInfo` instance. |
| [AccessibilityNodeInfo.SelectionPosition](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.SelectionPosition) | A class which defines either the start or end of a selection that can span across multiple AccessibilityNodeInfo objects. |
| [AccessibilityNodeInfo.SelectionPosition.Builder](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.SelectionPosition.Builder) | Builder for creating `SelectionPosition` objects. |
| [AccessibilityNodeInfo.StructuredDataInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.StructuredDataInfo) | An abstract base class for holding structured semantic information about a node. |
| [AccessibilityNodeInfo.TouchDelegateInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.TouchDelegateInfo) | Class with information of touch delegated views and regions from `TouchDelegate` for the `AccessibilityNodeInfo`. |
| [AccessibilityNodeProvider](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeProvider) | This class is the contract a client should implement to enable support of a virtual view hierarchy rooted at a given view for accessibility purposes. |
| [AccessibilityRecord](https://developer.android.com/reference/android/view/accessibility/AccessibilityRecord) | Represents a record in an `AccessibilityEvent` and contains information about state change of its source `View`. |
| [AccessibilityRequestPreparer](https://developer.android.com/reference/android/view/accessibility/AccessibilityRequestPreparer) | Object responsible to ensuring that a `View` is prepared to meet a synchronous request for accessibility data. |
| [AccessibilityWindowInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityWindowInfo) | This class represents a state snapshot of a window for accessibility purposes. |
| [CaptioningManager](https://developer.android.com/reference/android/view/accessibility/CaptioningManager) | Contains methods for accessing and monitoring preferred video captioning state and visual properties. |
| [CaptioningManager.CaptioningChangeListener](https://developer.android.com/reference/android/view/accessibility/CaptioningManager.CaptioningChangeListener) | Listener for changes in captioning properties, including enabled state and user style preferences. |
| [CaptioningManager.CaptionStyle](https://developer.android.com/reference/android/view/accessibility/CaptioningManager.CaptionStyle) | Specifies visual properties for video captions, including foreground and background colors, edge properties, and typeface. |

* ## Interfaces

  + [AccessibilityEventSource](https://developer.android.com/reference/android/view/accessibility/AccessibilityEventSource)
  + [AccessibilityManager.AccessibilityServicesStateChangeListener](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager.AccessibilityServicesStateChangeListener)
  + [AccessibilityManager.AccessibilityStateChangeListener](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager.AccessibilityStateChangeListener)
  + [AccessibilityManager.AudioDescriptionRequestedChangeListener](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager.AudioDescriptionRequestedChangeListener)
  + [AccessibilityManager.HighContrastTextStateChangeListener](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager.HighContrastTextStateChangeListener)
  + [AccessibilityManager.TouchExplorationStateChangeListener](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager.TouchExplorationStateChangeListener)
* ## Classes

  + [AccessibilityEvent](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent)
  + [AccessibilityManager](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager)
  + [AccessibilityNodeInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo)
  + [AccessibilityNodeInfo.AccessibilityAction](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.AccessibilityAction)
  + [AccessibilityNodeInfo.CollectionInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.CollectionInfo)
  + [AccessibilityNodeInfo.CollectionInfo.Builder](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.CollectionInfo.Builder)
  + [AccessibilityNodeInfo.CollectionItemInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.CollectionItemInfo)
  + [AccessibilityNodeInfo.CollectionItemInfo.Builder](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.CollectionItemInfo.Builder)
  + [AccessibilityNodeInfo.ExtraRenderingInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.ExtraRenderingInfo)
  + [AccessibilityNodeInfo.ExtraRenderingInfo.Builder](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.ExtraRenderingInfo.Builder)
  + [AccessibilityNodeInfo.MathInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.MathInfo)
  + [AccessibilityNodeInfo.RangeInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.RangeInfo)
  + [AccessibilityNodeInfo.Selection](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.Selection)
  + [AccessibilityNodeInfo.SelectionPosition](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.SelectionPosition)
  + [AccessibilityNodeInfo.SelectionPosition.Builder](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.SelectionPosition.Builder)
  + [AccessibilityNodeInfo.StructuredDataInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.StructuredDataInfo)
  + [AccessibilityNodeInfo.TouchDelegateInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.TouchDelegateInfo)
  + [AccessibilityNodeProvider](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeProvider)
  + [AccessibilityRecord](https://developer.android.com/reference/android/view/accessibility/AccessibilityRecord)
  + [AccessibilityRequestPreparer](https://developer.android.com/reference/android/view/accessibility/AccessibilityRequestPreparer)
  + [AccessibilityWindowInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityWindowInfo)
  + [CaptioningManager](https://developer.android.com/reference/android/view/accessibility/CaptioningManager)
  + [CaptioningManager.CaptioningChangeListener](https://developer.android.com/reference/android/view/accessibility/CaptioningManager.CaptioningChangeListener)
  + [CaptioningManager.CaptionStyle](https://developer.android.com/reference/android/view/accessibility/CaptioningManager.CaptionStyle)
