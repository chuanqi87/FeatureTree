#!/usr/bin/env python3
"""Author the input domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "input_modality_family"


def atom(fid, parent, axis, zh, en, definition, includes, excludes, bindings, legacy=None, privacy="none"):
    return feature(
        fid, parent=parent, level="L3",
        zh=zh, en=en, definition=definition,
        includes=includes, excludes=excludes, sibling_axis=axis,
        granularity="atomic", bindings=bindings,
        legacy=legacy or {"disposition": "new", "sources": []},
        privacy_class=privacy,
    )


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "input", parent=None, level="L1",
        zh="输入与文本", en="Input and Text",
        definition="触控、按键、输入法、剪贴板、手写笔、手柄、文本编辑与拖放等输入能力。",
        includes=["触控、按键、IME、剪贴板、手写笔、手柄、文本编辑、拖放"],
        excludes=["无障碍开关控制见 a11y", "游戏引擎内输入抽象非系统 API"],
        legacy={"disposition": "kept", "sources": ["input"]},
    ))

    l2 = [
        ("input.touch", "触控与指针", "Touch and Pointer",
         "触摸事件、手势识别与指针样式。",
         ["触摸事件、手势、命中测试、指针"],
         ["按键见 input.key"],
         ["input.touch"]),
        ("input.key", "按键与键盘", "Keys and Keyboard",
         "物理/外接键盘按键事件与导航键。",
         ["按键事件、系统键、键盘导航"],
         ["软键盘 IME 见 input.ime"],
         []),
        ("input.ime", "输入法", "Input Method",
         "软键盘显示、编辑器配置与自定义输入法框架。",
         ["软键盘、编辑器、输入法服务"],
         ["文本选择见 input.text_editing"],
         ["input.ime"]),
        ("input.clipboard", "剪贴板", "Clipboard",
         "系统剪贴板读写与隐私控件。",
         ["读写、延迟粘贴、粘贴按钮"],
         ["拖放见 input.dragdrop"],
         ["input.clipboard"]),
        ("input.stylus", "手写笔", "Stylus",
         "手写笔触点、压感、笔迹与手写转文字。",
         ["笔迹、压感、预测、 scribble"],
         ["普通触控见 input.touch"],
         []),
        ("input.gamepad", "游戏手柄", "Gamepad",
         "手柄发现与按键/轴输入。",
         ["发现、按键轴、触控板手柄"],
         ["普通按键见 input.key"],
         []),
        ("input.text_editing", "文本编辑", "Text Editing",
         "光标选择、自动填充、拼写与富内容插入。",
         ["选择、自动填充、拼写、富内容"],
         ["IME 框架见 input.ime"],
         []),
        ("input.dragdrop", "拖放", "Drag and Drop",
         "应用内与跨应用拖放数据传输。",
         ["拖放会话、跨应用数据"],
         ["剪贴板见 input.clipboard"],
         ["input.dragdrop"]),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="input", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # touch
    f.append(atom(
        "input.touch.gestures", "input.touch", "touch_capability",
        "手势识别", "Gesture Recognition",
        "点击、滑动、捏合等系统/框架手势识别。",
        ["GestureDetector、UIGestureRecognizer"],
        ["input.touch.events"],
        merge_bindings(
            A("GestureDetector",
              "https://developer.android.com/reference/android/view/GestureDetector"),
            I("UIGestureRecognizer",
              "https://developer.apple.com/documentation/uikit/uigesturerecognizer", "class"),
            H("Gesture",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-settings"),
        ),
        legacy={"disposition": "kept", "sources": ["input.touch.gestures"]},
    ))
    for row in [
        ("input.touch.events", "触摸事件", "Touch Events",
         "接收原始触摸/指针事件序列。",
         ["MotionEvent、UITouch、TouchEvent"],
         ["input.touch.gestures"],
         merge_bindings(
             A("MotionEvent",
               "https://developer.android.com/reference/android/view/MotionEvent"),
             I("UITouch",
               "https://developer.apple.com/documentation/uikit/uitouch", "class"),
             H("TouchEvent",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch"),
         )),
        ("input.touch.hit_test", "命中测试", "Hit Testing",
         "控制视图是否参与触摸命中。",
         ["setOnTouchListener / hitTest、pointInside"],
         ["input.touch.events"],
         merge_bindings(
             A("View.onTouchEvent",
               "https://developer.android.com/reference/android/view/View#onTouchEvent(android.view.MotionEvent)"),
             I("hitTest",
               "https://developer.apple.com/documentation/uikit/uiview/1622469-hittest", "method"),
             H("hitTestBehavior",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior"),
         )),
        ("input.touch.pointer_capture", "指针捕获", "Pointer Capture",
         "将后续指针事件捕获到指定目标。",
         ["requestPointerCapture"],
         ["input.touch.events"],
         merge_bindings(
             A("View.requestPointerCapture",
               "https://developer.android.com/reference/android/view/View#requestPointerCapture()"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("input.touch.multi_pointer", "多指触控", "Multi-touch",
         "跟踪多指触点 ID 与坐标。",
         ["getPointerId、UITouch"],
         ["input.touch.events"],
         merge_bindings(
             A("MotionEvent.getPointerId",
               "https://developer.android.com/reference/android/view/MotionEvent#getPointerId(int)"),
             I("UITouch",
               "https://developer.apple.com/documentation/uikit/uitouch", "class"),
             H("TouchType",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch"),
         )),
        ("input.touch.pointer_style", "鼠标指针样式", "Pointer Style",
         "设置鼠标/触控板指针视觉样式。",
         ["PointerIcon、NSCursor"],
         ["input.touch.events"],
         merge_bindings(
             A("PointerIcon",
               "https://developer.android.com/reference/android/view/PointerIcon"),
             I("NSCursor",
               "https://developer.apple.com/documentation/appkit/nscursor", "class"),
             H("pointerStyle",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pointerstyle"),
         )),
        ("input.touch.hover", "悬停事件", "Hover Events",
         "鼠标/触控笔悬停进入离开事件。",
         ["onHoverEvent、UIHoverGestureRecognizer"],
         ["input.touch.events"],
         merge_bindings(
             A("View.onHoverEvent",
               "https://developer.android.com/reference/android/view/View#onHoverEvent(android.view.MotionEvent)"),
             I("UIHoverGestureRecognizer",
               "https://developer.apple.com/documentation/uikit/uihovergesturerecognizer", "class"),
             H("onHover",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-hover"),
         )),
        ("input.touch.edge_gesture", "边缘系统手势", "Edge System Gestures",
         "与系统边缘返回/多任务手势的冲突处理。",
         ["systemGestureExclusionRects、edgesForExtendedLayout"],
         ["input.touch.gestures"],
         merge_bindings(
             A("View.setSystemGestureExclusionRects",
               "https://developer.android.com/reference/android/view/View#setSystemGestureExclusionRects(java.util.List%3Candroid.graphics.Rect%3E)"),
             I("interactivePopGestureRecognizer",
               "https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621876-interactivepopgesturerecognizer", "property"),
             H("gesture优先级",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-settings"),
         )),
        ("input.touch.dispatch", "事件分发控制", "Touch Dispatch",
         "拦截或改写触摸事件分发路径。",
         ["onInterceptTouchEvent、nextResponder"],
         ["input.touch.events"],
         merge_bindings(
             A("ViewGroup.onInterceptTouchEvent",
               "https://developer.android.com/reference/android/view/ViewGroup#onInterceptTouchEvent(android.view.MotionEvent)"),
             I("next",
               "https://developer.apple.com/documentation/uikit/uiresponder/1621104-next", "property"),
             H("hitTestBehavior",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "input.touch", "touch_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # key
    for row in [
        ("input.key.events", "按键事件", "Key Events",
         "接收物理键盘/按键按下抬起事件。",
         ["KeyEvent、pressesBegan"],
         ["input.key.system_keys"],
         merge_bindings(
             A("KeyEvent",
               "https://developer.android.com/reference/android/view/KeyEvent"),
             I("pressesBegan",
               "https://developer.apple.com/documentation/uikit/uiresponder/1621138-pressesbegan", "method"),
             H("KeyEvent",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keyevent"),
         )),
        ("input.key.system_keys", "系统功能键", "System Keys",
         "处理音量、返回等系统功能键的优先响应。",
         ["KEYCODE_VOLUME_*、UIKeyCommand"],
         ["input.key.events"],
         merge_bindings(
             A("KeyEvent.KEYCODE_VOLUME_UP",
               "https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_VOLUME_UP"),
             I("UIKeyCommand",
               "https://developer.apple.com/documentation/uikit/uikeycommand", "class"),
             H("KeyCode",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode"),
         )),
        ("input.key.keyboard_nav", "键盘导航焦点", "Keyboard Focus Navigation",
         "方向键/Tab 在焦点间导航。",
         ["focusSearch、UIFocusSystem"],
         ["input.key.events"],
         merge_bindings(
             A("View.focusSearch",
               "https://developer.android.com/reference/android/view/View#focusSearch(int)"),
             I("UIFocusSystem",
               "https://developer.apple.com/documentation/uikit/uifocussystem", "class"),
             H("focus control",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus"),
         )),
        ("input.key.shortcuts", "键盘快捷键", "Keyboard Shortcuts",
         "注册修饰键组合快捷键。",
         ["Menu shortcut、UIKeyCommand"],
         ["input.key.events"],
         merge_bindings(
             A("MenuItem.setAlphabeticShortcut",
               "https://developer.android.com/reference/android/view/MenuItem#setAlphabeticShortcut(char)"),
             I("UIKeyCommand",
               "https://developer.apple.com/documentation/uikit/uikeycommand", "class"),
             pending("harmonyos"),
         )),
        ("input.key.modifier_state", "修饰键状态", "Modifier State",
         "查询 Shift/Ctrl/Alt/Meta 状态。",
         ["metaState、modifierFlags"],
         ["input.key.events"],
         merge_bindings(
             A("KeyEvent.getMetaState",
               "https://developer.android.com/reference/android/view/KeyEvent#getMetaState()"),
             I("modifierFlags",
               "https://developer.apple.com/documentation/uikit/uikeycommand/1621116-modifierflags", "property"),
             pending("harmonyos"),
         )),
        ("input.key.repeat", "按键重复", "Key Repeat",
         "处理长按产生的按键重复事件。",
         ["getRepeatCount"],
         ["input.key.events"],
         merge_bindings(
             A("KeyEvent.getRepeatCount",
               "https://developer.android.com/reference/android/view/KeyEvent#getRepeatCount()"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("input.key.dpad", "方向垫输入", "D-pad Input",
         "遥控器/方向垫方向与确认键。",
         ["KEYCODE_DPAD_*"],
         ["input.key.keyboard_nav"],
         merge_bindings(
             A("KeyEvent.KEYCODE_DPAD_CENTER",
               "https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_DPAD_CENTER"),
             I("UIPress",
               "https://developer.apple.com/documentation/uikit/uipress", "class"),
             pending("harmonyos"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "input.key", "key_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # ime
    f.append(atom(
        "input.ime.framework", "input.ime", "ime_capability",
        "输入法服务框架", "IME Service Framework",
        "实现系统输入法服务/扩展的框架入口。",
        ["InputMethodService、UIInputViewController"],
        ["input.ime.visibility"],
        merge_bindings(
            A("InputMethodService",
              "https://developer.android.com/reference/android/inputmethodservice/InputMethodService"),
            I("UIInputViewController",
              "https://developer.apple.com/documentation/uikit/uiinputviewcontroller", "class"),
            H("InputMethodExtensionAbility",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod"),
        ),
        legacy={"disposition": "kept", "sources": ["input.ime.framework"]},
    ))
    for row in [
        ("input.ime.visibility", "软键盘显隐", "IME Visibility",
         "弹出或收起软键盘。",
         ["showSoftInput、becomeFirstResponder"],
         ["input.ime.editor_config"],
         merge_bindings(
             A("InputMethodManager.showSoftInput",
               "https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#showSoftInput(android.view.View,%20int)"),
             I("becomeFirstResponder",
               "https://developer.apple.com/documentation/uikit/uiresponder/1621113-becomefirstresponder", "method"),
             H("showTextInput",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethodengine"),
         )),
        ("input.ime.editor_config", "编辑器输入配置", "Editor Input Config",
         "配置键盘类型、回车键动作与输入选项。",
         ["inputType、UIKeyboardType、enterKeyType"],
         ["input.ime.visibility"],
         merge_bindings(
             A("EditorInfo",
               "https://developer.android.com/reference/android/view/inputmethod/EditorInfo"),
             I("UIKeyboardType",
               "https://developer.apple.com/documentation/uikit/uikeyboardtype", "enum"),
             H("InputType",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput"),
         )),
        ("input.ime.keyboard_frame", "键盘高度避让", "Keyboard Frame Avoidance",
         "获取键盘帧并做布局避让。",
         ["WindowInsets.ime、keyboard notifications"],
         ["input.ime.visibility"],
         merge_bindings(
             A("WindowInsetsCompat.Type.ime",
               "https://developer.android.com/reference/androidx/core/view/WindowInsetsCompat.Type#ime()"),
             I("keyboardWillShowNotification",
               "https://developer.apple.com/documentation/uikit/uiresponder/1621578-keyboardwillshownotification", "property"),
             H("onKeyboardHeightChange",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-on-keyboard"),
         )),
        ("input.ime.switch", "输入法切换", "IME Switch",
         "切换当前输入法或语言。",
         ["showInputMethodPicker、UITextInputMode"],
         ["input.ime.framework"],
         merge_bindings(
             A("InputMethodManager.showInputMethodPicker",
               "https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#showInputMethodPicker()"),
             I("UITextInputMode",
               "https://developer.apple.com/documentation/uikit/uitextinputmode", "class"),
             H("switchInputMethod",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod"),
         )),
        ("input.ime.custom_keyboard", "应用内自定义键盘", "Custom In-App Keyboard",
         "使用应用自绘输入视图替代系统键盘。",
         ["inputView、custom keyboard"],
         ["input.ime.framework"],
         merge_bindings(
             A("EditText.setShowSoftInputOnFocus",
               "https://developer.android.com/reference/android/widget/EditText"),
             I("inputView",
               "https://developer.apple.com/documentation/uikit/uiresponder/1621092-inputview", "property"),
             H("custom keyboard",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ime-kit", "guide"),
         )),
        ("input.ime.inline_suggestions", "行内建议", "Inline Suggestions",
         "系统在输入框提供行内自动建议。",
         ["InlineSuggestionsRequest"],
         ["input.text_editing.autofill"],
         merge_bindings(
             A("InlineSuggestionsRequest",
               "https://developer.android.com/reference/android/view/inputmethod/InlineSuggestionsRequest"),
             I("UITextInput / autocorrection",
               "https://developer.apple.com/documentation/uikit/uitextinput", "protocol"),
             pending("harmonyos"),
         )),
        ("input.ime.secure_entry", "安全输入", "Secure Text Entry",
         "密码等安全输入模式。",
         ["inputType password、isSecureTextEntry"],
         ["input.ime.editor_config"],
         merge_bindings(
             A("InputType.TYPE_TEXT_VARIATION_PASSWORD",
               "https://developer.android.com/reference/android/text/InputType#TYPE_TEXT_VARIATION_PASSWORD"),
             I("isSecureTextEntry",
               "https://developer.apple.com/documentation/uikit/uitextinputtraits/1624449-issecuretextentry", "property"),
             H("InputType.Password",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "input.ime", "ime_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # clipboard
    f.append(atom(
        "input.clipboard.read_write", "input.clipboard", "clipboard_capability",
        "剪贴板读写", "Clipboard Read Write",
        "向系统剪贴板写入或读取文本/内容。",
        ["ClipboardManager、UIPasteboard"],
        ["input.clipboard.paste_button"],
        merge_bindings(
            A("ClipboardManager",
              "https://developer.android.com/reference/android/content/ClipboardManager"),
            I("UIPasteboard",
              "https://developer.apple.com/documentation/uikit/uipasteboard", "class"),
            H("@ohos.pasteboard",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pasteboard"),
        ),
        legacy={"disposition": "kept", "sources": ["input.clipboard.read_write"]},
        privacy="sensitive",
    ))
    for row in [
        ("input.clipboard.paste_button", "粘贴控件", "Paste Button",
         "系统粘贴按钮以降低剪贴板读取权限摩擦。",
         ["PasteButton、UIPasteControl"],
         ["input.clipboard.read_write"],
         merge_bindings(
             pending("android"),
             I("UIPasteControl",
               "https://developer.apple.com/documentation/uikit/uipastecontrol", "class"),
             pending("harmonyos"),
         ), "sensitive"),
        ("input.clipboard.delayed", "延迟复制内容", "Delayed Clipboard Content",
         "在真正粘贴时才提供数据的延迟内容项。",
         ["Delayed DataProvider、UIPasteboard detection patterns"],
         ["input.clipboard.read_write"],
         merge_bindings(
             pending("android"),
             I("UIPasteboard",
               "https://developer.apple.com/documentation/uikit/uipasteboard", "class"),
             H("pasteboard delay",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pasteboard"),
         )),
        ("input.clipboard.types", "剪贴板数据类型", "Clipboard Data Types",
         "按 MIME/UTI 类型读写剪贴板。",
         ["ClipData、setData UTI"],
         ["input.clipboard.read_write"],
         merge_bindings(
             A("ClipData",
               "https://developer.android.com/reference/android/content/ClipData"),
             I("UIPasteboard.setData",
               "https://developer.apple.com/documentation/uikit/uipasteboard/1622231-setdata", "method"),
             H("PasteData",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pasteboard"),
         )),
        ("input.clipboard.clear", "清空剪贴板", "Clear Clipboard",
         "清除剪贴板内容。",
         ["clearPrimaryClip、items = []"],
         ["input.clipboard.read_write"],
         merge_bindings(
             A("ClipboardManager.clearPrimaryClip",
               "https://developer.android.com/reference/android/content/ClipboardManager#clearPrimaryClip()"),
             I("UIPasteboard.items",
               "https://developer.apple.com/documentation/uikit/uipasteboard/1622233-items", "property"),
             H("clearData",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pasteboard"),
         )),
        ("input.clipboard.change_listen", "剪贴板变更监听", "Clipboard Change Listen",
         "监听剪贴板内容变化（受隐私限制）。",
         ["OnPrimaryClipChangedListener"],
         ["input.clipboard.read_write"],
         merge_bindings(
             A("ClipboardManager.addPrimaryClipChangedListener",
               "https://developer.android.com/reference/android/content/ClipboardManager#addPrimaryClipChangedListener(android.content.ClipboardManager.OnPrimaryClipChangedListener)"),
             pending("ios", "变更监听受限"),
             H("pasteboard.on",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pasteboard"),
         ), "sensitive"),
        ("input.clipboard.sensitive_flag", "敏感内容标记", "Sensitive Clipboard Flag",
         "标记剪贴板内容为敏感以避免预览泄露。",
         ["EXTRA_IS_SENSITIVE"],
         ["input.clipboard.read_write"],
         merge_bindings(
             A("ClipDescription.EXTRA_IS_SENSITIVE",
               "https://developer.android.com/reference/android/content/ClipDescription#EXTRA_IS_SENSITIVE"),
             pending("ios"),
             pending("harmonyos"),
         )),
    ]:
        if len(row) == 7:
            fid, zh, en, definition, includes, excludes, bindings = row
            privacy = "none"
        else:
            fid, zh, en, definition, includes, excludes, bindings, privacy = row
        f.append(atom(
            fid, "input.clipboard", "clipboard_capability",
            zh, en, definition, includes, excludes, bindings, privacy=privacy,
        ))

    # stylus
    for row in [
        ("input.stylus.ink", "笔迹捕获", "Ink Capture",
         "捕获手写笔轨迹与压感数据。",
         ["MotionEvent.getPressure、PKStroke"],
         ["input.stylus.prediction"],
         merge_bindings(
             A("MotionEvent.getPressure",
               "https://developer.android.com/reference/android/view/MotionEvent#getPressure(int)"),
             I("PencilKit",
               "https://developer.apple.com/documentation/pencilkit", "framework"),
             H("stylus",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch"),
         )),
        ("input.stylus.prediction", "报点预测", "Stroke Prediction",
         "预测后续触点以降低手写延迟。",
         ["MotionEvent.ACTION_MOVE predicted、UIEvent predictedTouches"],
         ["input.stylus.ink"],
         merge_bindings(
             A("MotionEvent.getPredictedEvent",
               "https://developer.android.com/reference/android/view/MotionEvent"),
             I("predictedTouches",
               "https://developer.apple.com/documentation/uikit/uievent/1613805-predictedtouches", "method"),
             H("预测报点",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stylus-kit", "guide"),
         )),
        ("input.stylus.scribble", "手写转文字", "Scribble to Text",
         "在文本框上手写并转为文字。",
         ["UIScribbleInteraction"],
         ["input.stylus.ink"],
         merge_bindings(
             pending("android"),
             I("UIScribbleInteraction",
               "https://developer.apple.com/documentation/uikit/uiscribbleinteraction", "class"),
             H("手写转文字",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stylus-kit", "guide"),
         )),
        ("input.stylus.buttons", "笔身按键", "Stylus Buttons",
         "处理手写笔侧键/双击等笔身事件。",
         ["BUTTON_STYLUS_*、UIPencilInteraction"],
         ["input.stylus.ink"],
         merge_bindings(
             A("MotionEvent.BUTTON_STYLUS_PRIMARY",
               "https://developer.android.com/reference/android/view/MotionEvent#BUTTON_STYLUS_PRIMARY"),
             I("UIPencilInteraction",
               "https://developer.apple.com/documentation/uikit/uipencilinteraction", "class"),
             pending("harmonyos"),
         )),
        ("input.stylus.hover", "笔悬停", "Stylus Hover",
         "手写笔悬停坐标与状态。",
         ["AXIS_DISTANCE、UIHoverGestureRecognizer"],
         ["input.touch.hover"],
         merge_bindings(
             A("MotionEvent.AXIS_DISTANCE",
               "https://developer.android.com/reference/android/view/MotionEvent#AXIS_DISTANCE"),
             I("UIHoverGestureRecognizer",
               "https://developer.apple.com/documentation/uikit/uihovergesturerecognizer", "class"),
             pending("harmonyos"),
         )),
        ("input.stylus.palm_rejection", "掌托抑制", "Palm Rejection",
         "区分手掌误触与笔输入。",
         ["TOOL_TYPE_STYLUS 过滤"],
         ["input.stylus.ink"],
         merge_bindings(
             A("MotionEvent.TOOL_TYPE_STYLUS",
               "https://developer.android.com/reference/android/view/MotionEvent#TOOL_TYPE_STYLUS"),
             I("UITouch.TouchType.pencil",
               "https://developer.apple.com/documentation/uikit/uitouch/touchtype/pencil", "case"),
             pending("harmonyos"),
         )),
        ("input.stylus.tilt", "倾斜与方位角", "Tilt and Orientation",
         "读取笔倾斜角与方位角。",
         ["AXIS_TILT、altitudeAngle"],
         ["input.stylus.ink"],
         merge_bindings(
             A("MotionEvent.AXIS_TILT",
               "https://developer.android.com/reference/android/view/MotionEvent#AXIS_TILT"),
             I("altitudeAngle",
               "https://developer.apple.com/documentation/uikit/uitouch/1618115-altitudeangle", "property"),
             pending("harmonyos"),
         )),
        ("input.stylus.color_picker", "屏幕取色", "Screen Color Picker",
         "用手写笔或系统取色器拾取屏幕颜色。",
         ["UIColorWell / eyedropper"],
         ["input.stylus.ink"],
         merge_bindings(
             pending("android"),
             I("UIColorWell",
               "https://developer.apple.com/documentation/uikit/uicolorwell", "class"),
             H("取色",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stylus-kit", "guide"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "input.stylus", "stylus_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # gamepad
    for row in [
        ("input.gamepad.discovery", "手柄发现", "Gamepad Discovery",
         "发现并监听游戏手柄连接/断开。",
         ["InputDevice、GCController.controllers"],
         ["input.gamepad.input_reading"],
         merge_bindings(
             A("InputDevice",
               "https://developer.android.com/reference/android/view/InputDevice"),
             I("GCController",
               "https://developer.apple.com/documentation/gamecontroller/gccontroller", "class"),
             H("multimodalInput",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputdevice"),
         )),
        ("input.gamepad.input_reading", "手柄输入读取", "Gamepad Input Reading",
         "读取手柄按键、摇杆轴与触发器。",
         ["getAxisValue、GCExtendedGamepad"],
         ["input.gamepad.discovery"],
         merge_bindings(
             A("MotionEvent.getAxisValue",
               "https://developer.android.com/reference/android/view/MotionEvent#getAxisValue(int)"),
             I("GCExtendedGamepad",
               "https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad", "class"),
             H("KeyCode gamepad",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode"),
         )),
        ("input.gamepad.vibration", "手柄振动", "Gamepad Vibration",
         "控制手柄震感反馈。",
         ["createVibrator、haptics"],
         ["input.gamepad.input_reading"],
         merge_bindings(
             A("InputDevice.getVibrator",
               "https://developer.android.com/reference/android/view/InputDevice#getVibrator()"),
             I("GCDeviceHaptics",
               "https://developer.apple.com/documentation/gamecontroller/gcdevicehaptics", "class"),
             pending("harmonyos"),
         )),
        ("input.gamepad.touchpad", "手柄触控板", "Gamepad Touchpad",
         "读取手柄内置触控板输入。",
         ["SOURCE_TOUCHPAD、GCControllerTouchpad"],
         ["input.gamepad.input_reading"],
         merge_bindings(
             A("InputDevice.SOURCE_TOUCHPAD",
               "https://developer.android.com/reference/android/view/InputDevice#SOURCE_TOUCHPAD"),
             I("GCControllerTouchpad",
               "https://developer.apple.com/documentation/gamecontroller/gccontrollertouchpad", "class"),
             pending("harmonyos"),
         )),
        ("input.gamepad.battery", "手柄电量", "Gamepad Battery",
         "查询手柄电池状态。",
         ["GCDeviceBattery"],
         ["input.gamepad.discovery"],
         merge_bindings(
             pending("android"),
             I("GCDeviceBattery",
               "https://developer.apple.com/documentation/gamecontroller/gcdevicebattery", "class"),
             pending("harmonyos"),
         )),
        ("input.gamepad.motion", "手柄运动传感", "Gamepad Motion",
         "读取手柄加速度计/陀螺。",
         ["GCMotion"],
         ["input.gamepad.input_reading"],
         merge_bindings(
             pending("android"),
             I("GCMotion",
               "https://developer.apple.com/documentation/gamecontroller/gcmotion", "class"),
             pending("harmonyos"),
         )),
        ("input.gamepad.virtual", "屏内虚拟按键", "Virtual On-screen Controls",
         "应用内虚拟摇杆/按键控件（非系统手柄）。",
         ["自定义 View 模拟"],
         ["input.gamepad.input_reading"],
         merge_bindings(
             A("View / MotionEvent",
               "https://developer.android.com/reference/android/view/MotionEvent"),
             I("UIControl",
               "https://developer.apple.com/documentation/uikit/uicontrol", "class"),
             H("Button / PanGesture",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "input.gamepad", "gamepad_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # text_editing
    for row in [
        ("input.text_editing.selection", "光标与文本选择", "Cursor and Selection",
         "管理光标位置与选区。",
         ["setSelection、selectedTextRange"],
         ["input.text_editing.autofill"],
         merge_bindings(
             A("EditText.setSelection",
               "https://developer.android.com/reference/android/widget/EditText#setSelection(int,%20int)"),
             I("selectedTextRange",
               "https://developer.apple.com/documentation/uikit/uitextinput/1614505-selectedtextrange", "property"),
             H("TextInputController",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput"),
         )),
        ("input.text_editing.autofill", "自动填充", "Autofill",
         "系统自动填充账号/地址等表单字段。",
         ["AutofillManager、UITextContentType"],
         ["input.text_editing.selection"],
         merge_bindings(
             A("AutofillManager",
               "https://developer.android.com/reference/android/view/autofill/AutofillManager"),
             I("textContentType",
               "https://developer.apple.com/documentation/uikit/uitextinputtraits/1649636-textcontenttype", "property"),
             H("autoFill",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput"),
         ), "sensitive"),
        ("input.text_editing.spellcheck", "拼写检查", "Spell Check",
         "拼写与语法检查标记。",
         ["SpellChecker、UITextChecker"],
         ["input.text_editing.selection"],
         merge_bindings(
             A("SpellChecker",
               "https://developer.android.com/reference/android/view/textservice/SpellChecker"),
             I("UITextChecker",
               "https://developer.apple.com/documentation/uikit/uitextchecker", "class"),
             pending("harmonyos"),
         )),
        ("input.text_editing.rich_content", "富内容插入", "Rich Content Insert",
         "接收图片等富内容插入到输入框。",
         ["OnReceiveContentListener、UITextView insert"],
         ["input.text_editing.selection"],
         merge_bindings(
             A("OnReceiveContentListener",
               "https://developer.android.com/reference/android/view/OnReceiveContentListener"),
             I("insertText / NSAttributedString",
               "https://developer.apple.com/documentation/uikit/uitextview", "class"),
             pending("harmonyos"),
         )),
        ("input.text_editing.data_detector", "文本实体识别", "Data Detectors",
         "识别电话/链接等可交互实体。",
         ["Linkify、UIDataDetectorTypes"],
         ["input.text_editing.selection"],
         merge_bindings(
             A("Linkify",
               "https://developer.android.com/reference/android/text/util/Linkify"),
             I("dataDetectorTypes",
               "https://developer.apple.com/documentation/uikit/uitextview/1615458-datadetectortypes", "property"),
             pending("harmonyos"),
         )),
        ("input.text_editing.undo_redo", "撤销重做", "Undo Redo",
         "文本编辑撤销/重做。",
         ["UndoManager"],
         ["input.text_editing.selection"],
         merge_bindings(
             pending("android", "EditText 无统一 UndoManager，待核"),
             I("UndoManager",
               "https://developer.apple.com/documentation/foundation/undomanager", "class"),
             pending("harmonyos"),
         )),
        ("input.text_editing.menu", "编辑菜单", "Editing Menu",
         "自定义复制/粘贴/查词等编辑菜单项。",
         ["ActionMode、UIMenuController"],
         ["input.text_editing.selection"],
         merge_bindings(
             A("ActionMode",
               "https://developer.android.com/reference/android/view/ActionMode"),
             I("UIMenuController",
               "https://developer.apple.com/documentation/uikit/uimenucontroller", "class"),
             pending("harmonyos"),
         )),
        ("input.text_editing.dictation", "听写输入", "Dictation",
         "语音听写写入文本。",
         ["speech input / dictation"],
         ["input.ime.visibility"],
         merge_bindings(
             pending("android", "SpeechRecognizer 组合，待核"),
             I("UITextInput / dictation",
               "https://developer.apple.com/documentation/uikit/uitextinput", "protocol"),
             pending("harmonyos"),
         )),
    ]:
        if len(row) == 7:
            fid, zh, en, definition, includes, excludes, bindings = row
            privacy = "none"
        else:
            fid, zh, en, definition, includes, excludes, bindings, privacy = row
        f.append(atom(
            fid, "input.text_editing", "text_editing_capability",
            zh, en, definition, includes, excludes, bindings, privacy=privacy,
        ))

    # dragdrop
    f.append(atom(
        "input.dragdrop.cross_app", "input.dragdrop", "dragdrop_capability",
        "跨应用拖放", "Cross-App Drag and Drop",
        "在应用之间拖放传输数据。",
        ["DragAndDrop、UIDragInteraction"],
        ["input.dragdrop.session"],
        merge_bindings(
            A("View.startDragAndDrop",
              "https://developer.android.com/reference/android/view/View#startDragAndDrop(android.content.ClipData,%20android.view.View.DragShadowBuilder,%20java.lang.Object,%20int)"),
            I("UIDragInteraction",
              "https://developer.apple.com/documentation/uikit/uidraginteraction", "class"),
            H("DragController",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-dragcontroller"),
        ),
        legacy={"disposition": "kept", "sources": ["input.dragdrop.cross_app"]},
    ))
    for row in [
        ("input.dragdrop.session", "拖放会话", "Drag Session",
         "启动/结束拖放会话并提供拖影。",
         ["startDragAndDrop、UIDragSession"],
         ["input.dragdrop.cross_app"],
         merge_bindings(
             A("View.startDragAndDrop",
               "https://developer.android.com/reference/android/view/View#startDragAndDrop(android.content.ClipData,%20android.view.View.DragShadowBuilder,%20java.lang.Object,%20int)"),
             I("UIDragSession",
               "https://developer.apple.com/documentation/uikit/uidragsession", "protocol"),
             H("drag start",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-drag-drop"),
         )),
        ("input.dragdrop.drop_target", "放置目标", "Drop Target",
         "声明可接收放置的目标并处理放置数据。",
         ["OnDragListener、UIDropInteraction"],
         ["input.dragdrop.session"],
         merge_bindings(
             A("View.OnDragListener",
               "https://developer.android.com/reference/android/view/View.OnDragListener"),
             I("UIDropInteraction",
               "https://developer.apple.com/documentation/uikit/uidropinteraction", "class"),
             H("onDrop",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-drag-drop"),
         )),
        ("input.dragdrop.shadow", "拖影与预览", "Drag Shadow",
         "自定义拖动预览/拖影外观。",
         ["DragShadowBuilder、UIDragPreview"],
         ["input.dragdrop.session"],
         merge_bindings(
             A("View.DragShadowBuilder",
               "https://developer.android.com/reference/android/view/View.DragShadowBuilder"),
             I("UIDragPreview",
               "https://developer.apple.com/documentation/uikit/uidragpreview", "class"),
             pending("harmonyos"),
         )),
        ("input.dragdrop.types", "拖放数据类型", "Drag Data Types",
         "声明拖放内容类型与建议。",
         ["ClipData、NSItemProvider"],
         ["input.dragdrop.session"],
         merge_bindings(
             A("ClipData",
               "https://developer.android.com/reference/android/content/ClipData"),
             I("NSItemProvider",
               "https://developer.apple.com/documentation/foundation/nsitemprovider", "class"),
             H("unifiedDataChannel",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-udmf"),
         )),
        ("input.dragdrop.local", "应用内拖放", "In-App Drag and Drop",
         "同一应用内视图间拖放重排。",
         ["同一进程 ClipData / local context"],
         ["input.dragdrop.cross_app"],
         merge_bindings(
             A("View.startDragAndDrop",
               "https://developer.android.com/reference/android/view/View#startDragAndDrop(android.content.ClipData,%20android.view.View.DragShadowBuilder,%20java.lang.Object,%20int)"),
             I("UIDragInteraction",
               "https://developer.apple.com/documentation/uikit/uidraginteraction", "class"),
             H("onDrag",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-drag-drop"),
         )),
        ("input.dragdrop.permission", "拖放权限与标志", "Drag Flags",
         "设置全局/跨窗口拖放标志与权限。",
         ["DRAG_FLAG_GLOBAL"],
         ["input.dragdrop.cross_app"],
         merge_bindings(
             A("View.DRAG_FLAG_GLOBAL",
               "https://developer.android.com/reference/android/view/View#DRAG_FLAG_GLOBAL"),
             pending("ios"),
             pending("harmonyos"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "input.dragdrop", "dragdrop_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    return list({n["id"]: n for n in f}.values())


def main():
    nodes = build()
    path = write_domain("input", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
