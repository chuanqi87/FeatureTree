#!/usr/bin/env python3
"""Author the ui domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "ui_concern"


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "ui", parent=None, level="L1",
        zh="界面与窗口", en="UI and Windowing",
        definition="应用界面范式、布局、控件、导航、窗口形态、主题、动效与系统壳层 UI 集成；不含无障碍与原生绘图底层。",
        includes=["声明/命令式 UI、布局容器、控件、导航、多窗、主题资源、动画、桌面壳/表盘 UI 入口"],
        excludes=["a11y 无障碍树", "graphics 底层绘制", "app.desktop 小组件宿主生命周期"],
        legacy={"disposition": "kept", "sources": ["ui"]},
    ))

    l2 = [
        ("ui.paradigm", "界面范式与状态", "UI Paradigm and State",
         "声明式/命令式构建模型、状态作用域、自定义组件与原生嵌入。",
         ["声明式 DSL、命令式视图树、本地/共享状态、自定义组件、原生嵌入"],
         ["具体控件见 ui.controls", "布局算法见 ui.layout"],
         ["ui.declarative", "ui.imperative", "ui.declarative.vs_imperative"]),
        ("ui.layout", "布局与滚动", "Layout and Scrolling",
         "线性/弹性/网格/约束布局、滚动容器与响应式分页。",
         ["linear、flex、grid、constraint、scroll、responsive、pagination"],
         ["列表项控件外观见 ui.controls", "导航结构见 ui.navigation"],
         ["ui.controls.list"]),
        ("ui.controls", "控件与交互件", "Controls and Widgets",
         "可复用交互与展示控件类别：选择、文本、弹层、菜单、选择器、进度、图像、图表与高级控件。",
         ["button_selection、text_display、dialog、menu、picker、progress、image、chart、advanced"],
         ["布局容器见 ui.layout", "导航栏见 ui.navigation.app_bar"],
         ["ui.controls"]),
        ("ui.navigation", "导航结构", "Navigation Structure",
         "页面栈、标签、抽屉/侧栏与应用栏导航模式。",
         ["stack、tabs、drawer_sidebar、app_bar"],
         ["窗口分屏见 ui.window", "转场动画见 ui.animation.transition"],
         ["ui.navigation"]),
        ("ui.window", "窗口与系统栏", "Window and System Bars",
         "窗口获取与属性、系统栏、分屏/自由窗、画中画、方向与子窗。",
         ["manage、system_bars、split_free、pip、orientation、subwindow"],
         ["导航栈见 ui.navigation.stack"],
         ["ui.window"]),
        ("ui.theme", "主题与外观", "Theme and Appearance",
         "深色模式、样式复用、动态配色、资源限定符与材质视觉效果。",
         ["dark_mode、styling、customization、resource、visual_effects"],
         ["动效曲线见 ui.animation"],
         ["ui.theme"]),
        ("ui.animation", "动效与动画", "Animation and Motion",
         "属性动画、转场、曲线与共享元素过渡。",
         ["property、transition、curve、shared_element"],
         ["控件内帧动画见 ui.controls.image"],
         []),
        ("ui.system_integration", "系统壳层UI集成", "System Shell UI Integration",
         "状态栏/快捷栏等桌面壳层条目与表盘/复杂功能 UI 扩展入口。",
         ["desktop_shell、watchface"],
         ["桌面小组件见 app.desktop.widget"],
         []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        f.append(feature(
            fid, parent="ui", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy={"disposition": "merged_from" if sources else "new", "sources": sources}
            if sources and fid not in ("ui.controls", "ui.navigation", "ui.window", "ui.theme")
            else {"disposition": "kept" if sources else "new", "sources": sources or []},
        ))
    # Fix L2 legacy: keep ids that match
    for node in f:
        if node["id"] in {"ui.controls", "ui.navigation", "ui.window", "ui.theme"}:
            node["legacy"] = {"disposition": "kept", "sources": [node["id"]]}
        elif node["id"] == "ui.paradigm":
            node["legacy"] = {"disposition": "merged_from", "sources": [
                "ui.declarative", "ui.imperative", "ui.declarative.vs_imperative",
            ]}
        elif node["id"] == "ui.layout":
            node["legacy"] = {"disposition": "merged_from", "sources": ["ui.controls.list"]}

    # --- paradigm ---
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("ui.paradigm.declarative", "声明式UI", "Declarative UI",
         "以状态驱动描述界面树并由框架差分更新的声明式构建模型。",
         ["Composable/@Component/build、状态驱动刷新"],
         ["命令式视图树见 paradigm.imperative"],
         merge_bindings(
             A("Composable", "https://developer.android.com/develop/ui/compose", "api"),
             I("SwiftUI", "https://developer.apple.com/documentation/swiftui", "framework"),
             H("@Component", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components"),
         ),
         {"disposition": "renamed_from", "sources": ["ui.declarative", "ui.declarative.vs_imperative"]}),
        ("ui.paradigm.imperative", "命令式视图树", "Imperative View Tree",
         "通过命令式创建、挂载与变更视图节点构建界面。",
         ["View/ViewGroup、UIView、FrameNode"],
         ["声明式见 paradigm.declarative"],
         merge_bindings(
             A("android.view.View", "https://developer.android.com/reference/android/view/View"),
             I("UIView", "https://developer.apple.com/documentation/uikit/uiview", "class"),
             H("FrameNode", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode"),
         ),
         {"disposition": "renamed_from", "sources": ["ui.imperative"]}),
        ("ui.paradigm.state.local", "本地组件状态", "Local Component State",
         "绑定到单个组件作用域的可变 UI 状态。",
         ["@State/remember、@StateObject 局部"],
         ["跨组件共享见 state.shared"],
         merge_bindings(
             A("mutableStateOf", "https://developer.android.com/develop/ui/compose/state", "api"),
             I("@State", "https://developer.apple.com/documentation/swiftui/state", "property"),
             H("@State", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state"),
         ),
         {"disposition": "new", "sources": []}),
        ("ui.paradigm.state.shared", "共享与提升状态", "Shared and Lifted State",
         "跨组件共享、依赖注入或应用级可观察状态。",
         ["ViewModel/@Provide/@Consume、EnvironmentObject、AppStorage"],
         ["单组件本地状态见 state.local"],
         merge_bindings(
             A("ViewModel", "https://developer.android.com/topic/libraries/architecture/viewmodel", "class"),
             I("EnvironmentObject", "https://developer.apple.com/documentation/swiftui/environmentobject", "property"),
             H("@Provide / @Consume", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-provide-and-consume"),
         ),
         {"disposition": "new", "sources": []}),
        ("ui.paradigm.custom_component", "自定义组件", "Custom Component",
         "封装可复用自定义 UI 组件及其插槽/构建器参数。",
         ["自定义 View/@Component/@Builder、ViewModifier"],
         ["系统控件类别见 ui.controls"],
         merge_bindings(
             A("View 自定义子类", "https://developer.android.com/develop/ui/views/layout/custom-views/create-view", "guide"),
             I("View", "https://developer.apple.com/documentation/swiftui/view", "protocol"),
             H("@Builder / @BuilderParam", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder"),
         ),
         {"disposition": "new", "sources": []}),
        ("ui.paradigm.native_embed", "原生视图嵌入", "Native View Embedding",
         "在声明式树中嵌入命令式原生视图，或反向承载声明式内容。",
         ["AndroidView/UIViewRepresentable、EmbeddedComponent/ContentSlot"],
         ["纯声明式见 paradigm.declarative"],
         merge_bindings(
             A("AndroidView", "https://developer.android.com/jetpack/compose/migrate/interoperability-apis/views-in-compose", "api"),
             I("UIViewRepresentable", "https://developer.apple.com/documentation/swiftui/uiviewrepresentable", "protocol"),
             H("EmbeddedComponent", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-embedded-component"),
         ),
         {"disposition": "new", "sources": []}),
    ]:
        parent = "ui.paradigm.state" if ".state." in fid else "ui.paradigm"
        axis = "state_scope" if parent.endswith(".state") else "paradigm_model"
        f.append(feature(
            fid, parent=parent, level="L4" if parent.endswith(".state") else "L3",
            zh=zh, en=en, definition=definition, includes=includes, excludes=excludes,
            sibling_axis=axis, granularity="atomic", bindings=bindings, legacy=legacy,
        ))
    f.append(feature(
        "ui.paradigm.state", parent="ui.paradigm", level="L3",
        zh="UI状态管理", en="UI State Management",
        definition="本地与共享作用域的界面状态绑定模型。",
        includes=["local、shared"],
        excludes=["持久化存储见 storage"],
        sibling_axis="paradigm_model",
        bindings=merge_bindings(
            A("State in Compose", "https://developer.android.com/develop/ui/compose/state", "guide"),
            I("State and Data Flow", "https://developer.apple.com/documentation/swiftui/state-and-data-flow", "guide"),
            H("@State", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state"),
        ),
    ))

    # --- layout ---
    layout_atomics = [
        ("ui.layout.linear", "线性布局", "Linear Layout",
         "按主轴单向排列子项的线性容器。",
         ["Row/Column、LinearLayout、HStack/VStack"],
         ["弹性权重见 layout.flex"],
         merge_bindings(
             A("LinearLayout", "https://developer.android.com/reference/android/widget/LinearLayout"),
             I("HStack / VStack", "https://developer.apple.com/documentation/swiftui/hstack", "structure"),
             H("Row / Column", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row"),
         )),
        ("ui.layout.flex", "弹性布局", "Flex Layout",
         "基于弹性伸缩与换行的主/交叉轴布局。",
         ["Flex、Modifier.weight、flexible frames"],
         ["固定线性见 layout.linear"],
         merge_bindings(
             A("FlexboxLayout", "https://developer.android.com/reference/com/google/android/flexbox/FlexboxLayout", "class"),
             I("flexible frames", "https://developer.apple.com/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:)", "method"),
             H("Flex", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex"),
         )),
        ("ui.layout.grid", "网格布局", "Grid Layout",
         "行列网格与惰性网格单元布局。",
         ["Grid/LazyVerticalGrid、UICollectionView 网格、GridRow"],
         ["瀑布流见 scroll.waterfall"],
         merge_bindings(
             A("LazyVerticalGrid", "https://developer.android.com/jetpack/compose/lists#grids", "api"),
             I("GridItem", "https://developer.apple.com/documentation/swiftui/griditem", "structure"),
             H("Grid", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid"),
         )),
        ("ui.layout.constraint", "约束布局", "Constraint Layout",
         "以相对约束与锚点定位子项的布局。",
         ["ConstraintLayout、RelativeContainer、Auto Layout 约束"],
         ["线性/弹性见 layout.linear / flex"],
         merge_bindings(
             A("ConstraintLayout", "https://developer.android.com/develop/ui/views/layout/constraint-layout", "guide"),
             I("Auto Layout", "https://developer.apple.com/documentation/uikit/nslayoutconstraint", "class"),
             H("RelativeContainer", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-relativecontainer"),
         )),
        ("ui.layout.responsive", "响应式尺寸布局", "Responsive Size Layout",
         "按窗口尺寸类/断点切换布局形态。",
         ["WindowSizeClass、GridRow 断点、size classes"],
         ["分屏窗口见 ui.window.split_free"],
         merge_bindings(
             A("WindowSizeClass", "https://developer.android.com/develop/ui/compose/layouts/adaptive", "guide"),
             I("horizontalSizeClass", "https://developer.apple.com/documentation/swiftui/environmentvalues/horizontalsizeclass", "property"),
             H("GridRow 断点", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout"),
         )),
        ("ui.layout.pagination", "分页容器", "Pagination Container",
         "可左右翻页的页面容器与指示器。",
         ["ViewPager2/Swiper、TabView 页式、PageControl"],
         ["标签导航见 ui.navigation.tabs"],
         merge_bindings(
             A("ViewPager2", "https://developer.android.com/reference/androidx/viewpager2/widget/ViewPager2"),
             I("TabView", "https://developer.apple.com/documentation/swiftui/tabview", "structure"),
             H("Swiper", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper"),
         )),
    ]
    for fid, zh, en, definition, includes, excludes, bindings in layout_atomics:
        f.append(feature(
            fid, parent="ui.layout", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="layout_model",
            granularity="atomic", bindings=bindings,
        ))

    f.append(feature(
        "ui.layout.scroll", parent="ui.layout", level="L3",
        zh="滚动容器", en="Scroll Containers",
        definition="可滚动内容容器及其回收、刷新与嵌套协调。",
        includes=["container、recycling、refresh、nested、waterfall"],
        excludes=["分页见 layout.pagination"],
        sibling_axis="layout_model",
        legacy={"disposition": "merged_from", "sources": ["ui.controls.list"]},
        bindings=merge_bindings(
            A("RecyclerView", "https://developer.android.com/guide/topics/ui/layout/recyclerview", "guide"),
            I("ScrollView / List", "https://developer.apple.com/documentation/swiftui/scrollview", "structure"),
            H("Scroll / List", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll"),
        ),
    ))
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("ui.layout.scroll.container", "基础滚动容器", "Basic Scroll Container",
         "承载可超出视口内容的基础滚动视图。",
         ["ScrollView、Scroll"], ["列表回收见 scroll.recycling"],
         merge_bindings(
             A("ScrollView", "https://developer.android.com/reference/android/widget/ScrollView"),
             I("ScrollView", "https://developer.apple.com/documentation/swiftui/scrollview", "structure"),
             H("Scroll", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll"),
         ), {"disposition": "new", "sources": []}),
        ("ui.layout.scroll.recycling", "列表回收与惰性", "List Recycling and Laziness",
         "大列表项回收复用或惰性构建。",
         ["RecyclerView/LazyColumn、UITableView、List/LazyForEach"],
         ["下拉刷新见 scroll.refresh"],
         merge_bindings(
             A("RecyclerView", "https://developer.android.com/guide/topics/ui/layout/recyclerview", "guide"),
             I("UITableView", "https://developer.apple.com/documentation/uikit/uitableview", "class"),
             H("List / LazyForEach", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list"),
         ), {"disposition": "renamed_from", "sources": ["ui.controls.list"]}),
        ("ui.layout.scroll.refresh", "下拉刷新", "Pull to Refresh",
         "滚动容器上的下拉刷新手势与指示。",
         ["SwipeRefreshLayout、refreshable、Refresh"],
         ["滚动本身见 scroll.container"],
         merge_bindings(
             A("SwipeRefreshLayout", "https://developer.android.com/reference/androidx/swiperefreshlayout/widget/SwipeRefreshLayout"),
             I("refreshable", "https://developer.apple.com/documentation/swiftui/view/refreshable(action:)", "method"),
             H("Refresh", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh"),
         ), {"disposition": "new", "sources": []}),
        ("ui.layout.scroll.nested", "嵌套滚动协调", "Nested Scroll Coordination",
         "父子滚动区域之间的嵌套滚动与联动。",
         ["NestedScrollConnection、nestedScroll、coordinator"],
         ["单层滚动见 scroll.container"],
         merge_bindings(
             A("NestedScrollView", "https://developer.android.com/reference/androidx/core/widget/NestedScrollView"),
             I("ScrollViewReader", "https://developer.apple.com/documentation/swiftui/scrollviewreader", "structure"),
             H("nestedScroll", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-nested-scrolling"),
         ), {"disposition": "new", "sources": []}),
        ("ui.layout.scroll.waterfall", "瀑布流布局", "Waterfall Layout",
         "不等高多列瀑布流滚动布局。",
         ["StaggeredGrid、WaterFlow"],
         ["规则网格见 layout.grid"],
         merge_bindings(
             A("StaggeredGridLayoutManager", "https://developer.android.com/reference/androidx/recyclerview/widget/StaggeredGridLayoutManager"),
             pending("ios", "可用 UICollectionView 自定义布局实现"),
             H("WaterFlow", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent="ui.layout.scroll", level="L4", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="scroll_capability",
            granularity="atomic", bindings=bindings, legacy=legacy,
        ))

    # --- controls ---
    control_branches = [
        ("ui.controls.button_selection", "按钮与选择", "Buttons and Selection",
         "动作按钮与开关/单选/多选/分段/滑条等选择控件。",
         ["action、toggle、choices、segment、range、rating"],
         ["文本输入见 text_display"],
         ["ui.controls.button"]),
        ("ui.controls.text_display", "文本展示与输入", "Text Display and Input",
         "文本展示、富文本与文本输入编辑。",
         ["plain/rich text、selection、text field"],
         ["按钮文案见 button_selection"],
         ["ui.controls.text_field"]),
        ("ui.controls.dialog", "对话框与弹层", "Dialogs and Sheets",
         "告警、自定义、半屏 sheet 与全屏覆盖弹层。",
         ["alert、sheet、custom、full_cover"],
         ["轻提示见 popup_toast"],
         ["ui.controls.dialog"]),
        ("ui.controls.menu", "菜单", "Menus",
         "上下文菜单与层级菜单。",
         ["context、hierarchy"],
         ["导航抽屉见 ui.navigation.drawer_sidebar"],
         []),
        ("ui.controls.picker", "选择器", "Pickers",
         "日期时间与滚轮/列表选择器。",
         ["date_time、wheel"],
         ["分段选择见 button_selection"],
         []),
        ("ui.controls.progress", "进度指示", "Progress Indicators",
         "确定与不确定进度指示。",
         ["determinate、indeterminate"],
         ["图表见 chart"],
         []),
        ("ui.controls.image", "图像视图", "Image Views",
         "静态图像展示与简单帧动画图像。",
         ["display、frame_animation"],
         ["媒体解码见 media.image"],
         ["ui.controls.image"]),
        ("ui.controls.chart", "图表控件", "Charts",
         "数据图表与仪表盘类可视化控件。",
         ["data_chart、gauge"],
         ["通用图像见 image"],
         []),
        ("ui.controls.advanced", "高级复合控件", "Advanced Controls",
         "树、过滤器、计数器等复合/行业控件。",
         ["tree、filter、counter"],
         ["基础按钮见 button_selection"],
         []),
        ("ui.controls.popup_toast", "弹出提示", "Popups and Toasts",
         "Toast/Snackbar、气泡与引导浮层。",
         ["toast、popover、guidance"],
         ["模态对话框见 dialog"],
         []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in control_branches:
        f.append(feature(
            fid, parent="ui.controls", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="control_category",
            legacy={"disposition": "kept" if sources and sources[0] == fid else (
                "renamed_from" if sources else "new"), "sources": sources},
        ))

    control_leaves = [
        ("ui.controls.button_selection.action", "动作按钮", "Action Button",
         "触发动作的按钮控件。", ["Button"], ["开关见 toggle"],
         merge_bindings(
             A("Button", "https://developer.android.com/reference/android/widget/Button"),
             I("Button", "https://developer.apple.com/documentation/swiftui/button", "structure"),
             H("Button", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button"),
         ), {"disposition": "renamed_from", "sources": ["ui.controls.button"]}),
        ("ui.controls.button_selection.toggle", "开关与勾选", "Toggle and Checkbox",
         "布尔开关、复选与单选控件。", ["Switch/Checkbox/Radio"], ["动作按钮见 action"],
         merge_bindings(
             A("Switch / CheckBox", "https://developer.android.com/guide/topics/ui/controls", "guide"),
             I("Toggle", "https://developer.apple.com/documentation/swiftui/toggle", "structure"),
             H("Toggle / Checkbox", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.button_selection.segment", "分段控件", "Segmented Control",
         "互斥分段选项控件。", ["SegmentedButton/Picker segmented"], ["标签导航见 navigation.tabs"],
         merge_bindings(
             A("MaterialButtonToggleGroup", "https://developer.android.com/reference/com/google/android/material/button/MaterialButtonToggleGroup"),
             I("Picker .segmented", "https://developer.apple.com/documentation/swiftui/pickerstyle/segmented", "type"),
             H("SegmentButton", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-segmentbutton"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.button_selection.range", "范围滑条", "Range Slider",
         "连续或离散数值范围选择。", ["Slider"], ["评分见 rating"],
         merge_bindings(
             A("SeekBar / Slider", "https://developer.android.com/reference/android/widget/SeekBar"),
             I("Slider", "https://developer.apple.com/documentation/swiftui/slider", "structure"),
             H("Slider", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.text_display.plain", "文本展示", "Plain Text Display",
         "静态或样式化文本展示。", ["Text/TextView"], ["输入见 input"],
         merge_bindings(
             A("TextView", "https://developer.android.com/reference/android/widget/TextView"),
             I("Text", "https://developer.apple.com/documentation/swiftui/text", "structure"),
             H("Text", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.text_display.input", "文本输入", "Text Input",
         "单行/多行文本输入与编辑。", ["EditText/TextField"], ["纯展示见 plain"],
         merge_bindings(
             A("EditText", "https://developer.android.com/reference/android/widget/EditText"),
             I("TextField", "https://developer.apple.com/documentation/swiftui/textfield", "structure"),
             H("TextInput", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput"),
         ), {"disposition": "renamed_from", "sources": ["ui.controls.text_field"]}),
        ("ui.controls.text_display.rich", "富文本", "Rich Text",
         "可含多样式/嵌入的富文本展示与编辑。", ["Spannable/AttributedString/StyledString"], ["纯文本见 plain"],
         merge_bindings(
             A("Spannable", "https://developer.android.com/reference/android/text/Spannable", "interface"),
             I("AttributedString", "https://developer.apple.com/documentation/foundation/attributedstring", "structure"),
             H("StyledString", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.dialog.alert", "告警对话框", "Alert Dialog",
         "系统风格确认/告警对话框。", ["AlertDialog"], ["自定义见 custom"],
         merge_bindings(
             A("AlertDialog", "https://developer.android.com/reference/android/app/AlertDialog"),
             I("alert", "https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:actions:message:)", "method"),
             H("AlertDialog", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-alert-dialog-box"),
         ), {"disposition": "split_from", "sources": ["ui.controls.dialog"]}),
        ("ui.controls.dialog.sheet", "半屏面板", "Sheet",
         "自底部或侧向滑出的半屏内容面板。", ["BottomSheet/sheet/bindSheet"], ["全屏覆盖见 full_cover"],
         merge_bindings(
             A("ModalBottomSheet", "https://developer.android.com/reference/com/google/android/material/bottomsheet/BottomSheetDialog"),
             I("sheet", "https://developer.apple.com/documentation/swiftui/view/sheet(ispresented:ondismiss:content:)", "method"),
             H("bindSheet", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition"),
         ), {"disposition": "split_from", "sources": ["ui.controls.dialog"]}),
        ("ui.controls.dialog.custom", "自定义对话框", "Custom Dialog",
         "应用自定义内容的模态对话框。", ["Dialog/CustomDialog"], ["告警见 alert"],
         merge_bindings(
             A("Dialog", "https://developer.android.com/guide/topics/ui/dialogs", "guide"),
             I("confirmationDialog", "https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:)", "method"),
             H("CustomDialog", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box"),
         ), {"disposition": "split_from", "sources": ["ui.controls.dialog"]}),
        ("ui.controls.menu.context", "上下文菜单", "Context Menu",
         "长按或右键触发的上下文菜单。", ["ContextMenu/bindContextMenu"], ["层级菜单见 hierarchy"],
         merge_bindings(
             A("PopupMenu", "https://developer.android.com/reference/android/widget/PopupMenu"),
             I("contextMenu", "https://developer.apple.com/documentation/swiftui/view/contextmenu(menuitems:)", "method"),
             H("bindContextMenu", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.menu.hierarchy", "层级菜单", "Hierarchical Menu",
         "可嵌套的菜单项层级。", ["Menu/MenuItem"], ["上下文菜单见 context"],
         merge_bindings(
             A("android.view.Menu", "https://developer.android.com/guide/topics/ui/menus", "guide"),
             I("Menu", "https://developer.apple.com/documentation/swiftui/menu", "structure"),
             H("Menu / MenuItem", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menu"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.picker.date_time", "日期时间选择", "Date Time Picker",
         "日期与/或时间选择控件。", ["DatePicker/TimePicker"], ["滚轮通用见 wheel"],
         merge_bindings(
             A("DatePicker", "https://developer.android.com/reference/android/widget/DatePicker"),
             I("DatePicker", "https://developer.apple.com/documentation/swiftui/datepicker", "structure"),
             H("DatePicker / TimePicker", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datepicker"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.picker.wheel", "滚轮选择器", "Wheel Picker",
         "通用滚轮或列选择器。", ["NumberPicker/TextPicker/Picker"], ["日期见 date_time"],
         merge_bindings(
             A("NumberPicker", "https://developer.android.com/reference/android/widget/NumberPicker"),
             I("Picker", "https://developer.apple.com/documentation/swiftui/picker", "structure"),
             H("TextPicker", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textpicker"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.progress.determinate", "确定进度", "Determinate Progress",
         "可知完成比例的进度条。", ["ProgressBar determinate"], ["不确定见 indeterminate"],
         merge_bindings(
             A("ProgressBar", "https://developer.android.com/reference/android/widget/ProgressBar"),
             I("ProgressView(value:)", "https://developer.apple.com/documentation/swiftui/progressview", "structure"),
             H("Progress", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.progress.indeterminate", "不确定进度", "Indeterminate Progress",
         "未知时长的加载指示。", ["CircularProgress/LoadingProgress"], ["确定进度见 determinate"],
         merge_bindings(
             A("CircularProgressIndicator", "https://developer.android.com/reference/com/google/android/material/progressindicator/CircularProgressIndicator"),
             I("ProgressView()", "https://developer.apple.com/documentation/swiftui/progressview", "structure"),
             H("LoadingProgress", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-loadingprogress"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.image.display", "图像展示", "Image Display",
         "在界面中展示位图/矢量图像。", ["ImageView/Image"], ["帧动画见 frame_animation"],
         merge_bindings(
             A("ImageView", "https://developer.android.com/reference/android/widget/ImageView"),
             I("Image", "https://developer.apple.com/documentation/swiftui/image", "structure"),
             H("Image", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image"),
         ), {"disposition": "renamed_from", "sources": ["ui.controls.image"]}),
        ("ui.controls.image.frame_animation", "帧动画图像", "Frame Animation Image",
         "基于多帧图像的简单逐帧动画展示。", ["AnimationDrawable、ImageAnimator"], ["属性动画见 ui.animation.property"],
         merge_bindings(
             A("AnimationDrawable", "https://developer.android.com/reference/android/graphics/drawable/AnimationDrawable"),
             I("UIImage.animatedImage", "https://developer.apple.com/documentation/uikit/uiimage/1624991-animatedimage", "type"),
             H("ImageAnimator", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imageanimator"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.chart.data_chart", "数据图表", "Data Charts",
         "折线/柱状等数据系列图表控件。", ["Chart/Swift Charts"], ["仪表见 gauge"],
         merge_bindings(
             pending("android", "可用第三方或 Compose Canvas；系统无统一 Chart API"),
             I("Charts", "https://developer.apple.com/documentation/charts", "framework"),
             H("DataPanel", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datapanel"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.chart.gauge", "仪表盘控件", "Gauge Control",
         "环形/指针类仪表进度可视化控件。", ["Gauge"], ["数据系列图见 data_chart"],
         merge_bindings(
             pending("android"),
             I("Gauge", "https://developer.apple.com/documentation/swiftui/gauge", "structure"),
             H("Gauge", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-gauge"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.popup_toast.toast", "轻提示", "Toast / Snackbar",
         "短暂非模态轻提示。", ["Toast/Snackbar/showToast"], ["对话框见 dialog"],
         merge_bindings(
             A("Snackbar", "https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar"),
             pending("ios", "无系统 Toast；可用临时 overlay"),
             H("promptAction.showToast", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.popup_toast.popover", "气泡弹出层", "Popover",
         "锚定到控件的气泡/弹出层内容。", ["PopupWindow、popover、bindPopup"], ["Toast 见 toast"],
         merge_bindings(
             A("PopupWindow", "https://developer.android.com/reference/android/widget/PopupWindow"),
             I("popover", "https://developer.apple.com/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:)", "method"),
             H("bindPopup", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.advanced.tree", "树形控件", "Tree Control",
         "可展开层级的树形列表控件。", ["TreeView"], ["普通列表见 layout.scroll.recycling"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("TreeView", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-treeview"),
         ), {"disposition": "new", "sources": []}),
        ("ui.controls.advanced.filter", "过滤器控件", "Filter Control",
         "条件过滤芯片/面板类复合控件。", ["Filter"], ["分段选择见 button_selection.segment"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("Filter", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-filter"),
         ), {"disposition": "new", "sources": []}),
    ]
    for fid, zh, en, definition, includes, excludes, bindings, legacy in control_leaves:
        parent = ".".join(fid.split(".")[:3])
        axis = parent.split(".")[-1] + "_variant"
        f.append(feature(
            fid, parent=parent, level="L4", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=axis,
            granularity="atomic", bindings=bindings, legacy=legacy,
        ))

    # --- navigation ---
    f.append(feature(
        "ui.navigation.stack", parent="ui.navigation", level="L3",
        zh="页面导航栈", en="Navigation Stack",
        definition="基于路由/目的地的页面进出栈导航。",
        includes=["back_stack、routes、predictive_back"],
        excludes=["标签见 tabs"],
        sibling_axis="navigation_pattern",
        legacy={"disposition": "kept", "sources": ["ui.navigation.stack"]},
        bindings=merge_bindings(
            A("NavController", "https://developer.android.com/guide/navigation", "guide"),
            I("NavigationStack", "https://developer.apple.com/documentation/swiftui/navigationstack", "structure"),
            H("Navigation", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation"),
        ),
    ))
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("ui.navigation.stack.back_stack", "返回栈管理", "Back Stack Management",
         "压入/弹出目的地并维护返回栈。", ["push/pop、back queue"], ["预测性返回见 predictive_back"],
         merge_bindings(
             A("NavController.navigate", "https://developer.android.com/guide/navigation", "guide"),
             I("NavigationPath", "https://developer.apple.com/documentation/swiftui/navigationpath", "structure"),
             H("NavPathStack", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation"),
         )),
        ("ui.navigation.stack.predictive_back", "预测性返回手势", "Predictive Back Gesture",
         "系统级预测性返回手势与动画协调。", ["OnBackPressedCallback predictive"], ["普通返回栈见 back_stack"],
         merge_bindings(
             A("OnBackPressedCallback", "https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture", "guide"),
             I("interactivePopGestureRecognizer", "https://developer.apple.com/documentation/uikit/uinavigationcontroller", "class"),
             pending("harmonyos"),
         )),
        ("ui.navigation.tabs", "标签导航", "Tab Navigation",
         "底部或顶部标签切换主入口。", ["TabLayout/Tabs/TabView"], ["分页 Swiper 见 layout.pagination"],
         merge_bindings(
             A("BottomNavigationView", "https://developer.android.com/reference/com/google/android/material/bottomnavigation/BottomNavigationView"),
             I("TabView", "https://developer.apple.com/documentation/swiftui/tabview", "structure"),
             H("Tabs", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs"),
         )),
        ("ui.navigation.drawer_sidebar", "抽屉与侧栏", "Drawer and Sidebar",
         "侧滑抽屉或常驻侧栏导航。", ["DrawerLayout/SideBarContainer/NavigationSplitView"], ["应用栏见 app_bar"],
         merge_bindings(
             A("DrawerLayout", "https://developer.android.com/reference/androidx/drawerlayout/widget/DrawerLayout"),
             I("NavigationSplitView", "https://developer.apple.com/documentation/swiftui/navigationsplitview", "structure"),
             H("SideBarContainer", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-sidebarcontainer"),
         )),
        ("ui.navigation.app_bar", "应用栏", "App Bar",
         "顶栏标题、导航图标与动作命令区。", ["AppBarLayout/Toolbar/ToolBar"], ["旧 navigation_bar 控件归此"],
         merge_bindings(
             A("AppBarLayout", "https://developer.android.com/reference/com/google/android/material/appbar/AppBarLayout"),
             I("toolbar / navigationTitle", "https://developer.apple.com/documentation/swiftui/view/navigationtitle(_:)", "method"),
             H("ToolBar", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-toolbar"),
         )),
    ]:
        parent = "ui.navigation.stack" if fid.startswith("ui.navigation.stack.") else "ui.navigation"
        level = "L4" if parent.endswith(".stack") else "L3"
        axis = "stack_capability" if level == "L4" else "navigation_pattern"
        legacy = {"disposition": "renamed_from", "sources": ["ui.controls.navigation_bar"]} if fid.endswith("app_bar") else {"disposition": "new", "sources": []}
        f.append(feature(
            fid, parent=parent, level=level, zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=axis,
            granularity="atomic", bindings=bindings, legacy=legacy,
        ))

    # --- window ---
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("ui.window.manage", "窗口获取与属性", "Window Acquire and Properties",
         "获取主窗/场景并设置尺寸、全屏等窗口属性。",
         ["Window/WindowStage/UIWindow"], ["系统栏见 system_bars"],
         merge_bindings(
             A("WindowManager", "https://developer.android.com/reference/android/view/WindowManager", "interface"),
             I("UIWindow / UIWindowScene", "https://developer.apple.com/documentation/uikit/uiwindow", "class"),
             H("@ohos.window", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-window"),
         ), {"disposition": "new", "sources": []}),
        ("ui.window.system_bars", "系统栏与边到边", "System Bars and Edge-to-Edge",
         "状态栏/导航栏外观与边到边避让。",
         ["WindowInsets、setDecorFitsSystemWindows、systemBarProperties"],
         ["沉浸式内容策略可同属此能力"],
         merge_bindings(
             A("WindowInsetsCompat", "https://developer.android.com/develop/ui/views/layout/edge-to-edge", "guide"),
             I("safeAreaInset", "https://developer.apple.com/documentation/uikit/uiview/safeareainsets", "property"),
             H("setWindowSystemBarProperties", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-window"),
         ), {"disposition": "new", "sources": []}),
        ("ui.window.split_free", "分屏与自由窗", "Split and Freeform Windows",
         "分屏、自由窗口与可调整多窗形态。",
         ["multi-window、freeform、resizeableActivity"],
         ["画中画见 pip"],
         merge_bindings(
             A("Multi-window support", "https://developer.android.com/guide/topics/large-screens/multi-window-support", "guide"),
             I("UIScene / Stage Manager", "https://developer.apple.com/documentation/uikit/uiscene", "class"),
             H("freeWindowMode", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-manager"),
         ), {"disposition": "renamed_from", "sources": ["ui.window.multiwindow"]}),
        ("ui.window.pip", "画中画窗口", "Picture-in-Picture",
         "将界面内容转入系统画中画小窗。",
         ["enterPictureInPictureMode、startPiP、AVPictureInPictureController"],
         ["分屏见 split_free"],
         merge_bindings(
             A("PictureInPictureParams", "https://developer.android.com/reference/android/app/PictureInPictureParams"),
             I("AVPictureInPictureController", "https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller", "class"),
             H("startPiP", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pip-window"),
         ), {"disposition": "kept", "sources": ["ui.window.pip"]}),
        ("ui.window.orientation", "窗口方向策略", "Window Orientation Policy",
         "锁定或跟随的窗口方向策略。",
         ["screenOrientation、setWindowOrientation"],
         ["旋转传感器见 sensors"],
         merge_bindings(
             A("setRequestedOrientation", "https://developer.android.com/reference/android/app/Activity#setRequestedOrientation(int)", "method"),
             I("supportedInterfaceOrientations", "https://developer.apple.com/documentation/uikit/uiviewcontroller/supportedinterfaceorientations", "property"),
             H("setWindowOrientation", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-window"),
         ), {"disposition": "new", "sources": []}),
        ("ui.window.subwindow", "子窗口", "Subwindows",
         "依附于主窗的子窗口/浮层窗口创建与管理。",
         ["createSubWindow、辅助 UIWindow"],
         ["系统对话框见 ui.controls.dialog"],
         merge_bindings(
             A("Dialog / PopupWindow", "https://developer.android.com/reference/android/widget/PopupWindow"),
             I("UIWindow", "https://developer.apple.com/documentation/uikit/uiwindow", "class"),
             H("createSubWindow", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-window"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent="ui.window", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="window_capability",
            granularity="atomic", bindings=bindings, legacy=legacy,
        ))

    # --- theme ---
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("ui.theme.dark_mode", "深色模式", "Dark Mode",
         "跟随系统或应用覆盖的深/浅色外观。",
         ["DayNight、ColorScheme、ColorMode"],
         ["动态取色见 customization"],
         merge_bindings(
             A("UiModeManager / DayNight", "https://developer.android.com/develop/ui/views/theming/darktheme", "guide"),
             I("colorScheme / preferredColorScheme", "https://developer.apple.com/documentation/swiftui/view/preferredcolorscheme(_:)", "method"),
             H("ColorMode", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface"),
         ), {"disposition": "kept", "sources": ["ui.theme.dark_mode"]}),
        ("ui.theme.styling", "样式复用", "Style Reuse",
         "主题样式、状态样式与修饰符复用。",
         ["styles、@Styles、ViewModifier"],
         ["资源限定符见 resource"],
         merge_bindings(
             A("Themes and styles", "https://developer.android.com/guide/topics/ui/themes", "guide"),
             I("ViewModifier", "https://developer.apple.com/documentation/swiftui/viewmodifier", "protocol"),
             H("@Styles / stateStyles", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-style"),
         ), {"disposition": "new", "sources": []}),
        ("ui.theme.customization", "动态配色定制", "Dynamic Color Customization",
         "基于壁纸/品牌色的动态配色与作用域主题。",
         ["Dynamic Color、WithTheme"],
         ["深色模式开关见 dark_mode"],
         merge_bindings(
             A("dynamicLightColorScheme", "https://developer.android.com/develop/ui/compose/designsystems/material3#dynamic_color", "guide"),
             I("Accent Color", "https://developer.apple.com/documentation/appkit/nscolor/controlaccentcolor", "type"),
             H("WithTheme", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-theme"),
         ), {"disposition": "new", "sources": []}),
        ("ui.theme.resource", "主题资源访问", "Theme Resource Access",
         "按限定符解析颜色/尺寸/字符串等 UI 资源。",
         ["Resources/$r、Asset catalog"],
         ["样式语法见 styling"],
         merge_bindings(
             A("Resources", "https://developer.android.com/guide/topics/resources/providing-resources", "guide"),
             I("Asset Catalog", "https://developer.apple.com/documentation/xcode/adding-images-to-your-app", "guide"),
             H("$r / ResourceManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access"),
         ), {"disposition": "new", "sources": []}),
        ("ui.theme.visual_effects", "材质与视觉效果", "Material Visual Effects",
         "模糊、材质、阴影等主题级视觉效果。",
         ["blur、Material、shadow"],
         ["属性动画见 ui.animation.property"],
         merge_bindings(
             A("RenderEffect", "https://developer.android.com/reference/android/graphics/RenderEffect"),
             I("Material", "https://developer.apple.com/documentation/swiftui/material", "structure"),
             H("backdropBlur / backgroundBlurStyle", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent="ui.theme", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="theme_aspect",
            granularity="atomic", bindings=bindings, legacy=legacy,
        ))

    # --- animation ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("ui.animation.property", "属性动画", "Property Animation",
         "对透明度、位移、缩放等属性做插值动画。",
         ["ObjectAnimator/animateTo/withAnimation"],
         ["页面转场见 transition"],
         merge_bindings(
             A("ObjectAnimator", "https://developer.android.com/reference/android/animation/ObjectAnimator"),
             I("withAnimation", "https://developer.apple.com/documentation/swiftui/withanimation(_:_:)", "function"),
             H("animateTo", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation"),
         )),
        ("ui.animation.transition", "转场动画", "Transition Animation",
         "视图出现/消失与页面切换转场。",
         ["Transition/pageTransition"],
         ["共享元素见 shared_element"],
         merge_bindings(
             A("Transition", "https://developer.android.com/reference/android/transition/Transition"),
             I("AnyTransition", "https://developer.apple.com/documentation/swiftui/anytransition", "structure"),
             H("pageTransition", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-page"),
         )),
        ("ui.animation.curve", "动画曲线", "Animation Curves",
         "缓动与弹簧等时间曲线。",
         ["Interpolator/spring/curves"],
         ["属性驱动见 property"],
         merge_bindings(
             A("SpringAnimation", "https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation"),
             I("spring", "https://developer.apple.com/documentation/swiftui/animation/spring(response:dampingfraction:blendduration:)", "type"),
             H("curves / springMotion", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-curve"),
         )),
        ("ui.animation.shared_element", "共享元素过渡", "Shared Element Transition",
         "跨页面/层级的共享元素几何过渡。",
         ["sharedElement/geometryTransition/matchedGeometryEffect"],
         ["普通转场见 transition"],
         merge_bindings(
             A("SharedTransitionScope", "https://developer.android.com/develop/ui/compose/animation/shared-elements", "guide"),
             I("matchedGeometryEffect", "https://developer.apple.com/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:)", "method"),
             H("geometryTransition", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-geometrytransition"),
         )),
    ]:
        f.append(feature(
            fid, parent="ui.animation", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="animation_kind",
            granularity="atomic", bindings=bindings,
        ))

    # --- system_integration ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("ui.system_integration.desktop_shell", "桌面壳层条目", "Desktop Shell Entries",
         "状态栏图标、快捷栏任务等桌面壳层 UI 扩展入口。",
         ["StatusBarManager、quickBar、addToStatusBar"],
         ["小组件见 app.desktop.widget"],
         merge_bindings(
             A("StatusBarManager", "https://developer.android.com/reference/android/app/StatusBarManager"),
             pending("ios"),
             H("addToStatusBar / quickBarManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statusbarmanager"),
         )),
        ("ui.system_integration.watchface", "表盘与复杂功能", "Watch Face and Complications",
         "表盘格式、复杂功能与表盘服务 UI 扩展。",
         ["Watch Face Format、CLKComplication、表盘服务"],
         ["健康数据见 health_home"],
         merge_bindings(
             A("Watch Face Format", "https://developer.android.com/training/wearables/watch-faces", "guide"),
             I("ClockKit", "https://developer.apple.com/documentation/clockkit", "framework"),
             pending("harmonyos"),
         )),
    ]:
        f.append(feature(
            fid, parent="ui.system_integration", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="shell_surface",
            granularity="atomic", bindings=bindings,
            device_forms=["phone", "tablet", "watch"] if "watchface" in fid else ["phone", "tablet"],
        ))

    dedup = {n["id"]: n for n in f}
    return list(dedup.values())


def main():
    nodes = build()
    path = write_domain("ui", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
