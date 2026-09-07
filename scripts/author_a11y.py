#!/usr/bin/env python3
"""Author the a11y domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "a11y_capability_family"


def B(a=None, i=None, h=None):
    parts = []
    if a:
        parts.append(A(a[0], a[1], a[2] if len(a) > 2 else "class"))
    else:
        parts.append(pending("android"))
    if i:
        parts.append(I(i[0], i[1], i[2] if len(i) > 2 else "framework"))
    else:
        parts.append(pending("ios"))
    if h:
        parts.append(H(h[0], h[1], h[2] if len(h) > 2 else "module"))
    else:
        parts.append(pending("harmonyos"))
    return merge_bindings(*parts)


def leaf(f, fid, parent, axis, zh, en, definition, includes, excludes, bindings, legacy=None, level="L3", privacy="none"):
    f.append(feature(
        fid, parent=parent, level=level, zh=zh, en=en, definition=definition,
        includes=includes, excludes=excludes, sibling_axis=axis,
        granularity="atomic", bindings=bindings,
        legacy=legacy or {"disposition": "new", "sources": []},
        privacy_class=privacy,
    ))


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "a11y", parent=None, level="L1",
        zh="无障碍", en="Accessibility",
        definition="无障碍树与语义、辅助服务、视觉/运动/听觉适配及无障碍测试。",
        includes=['框架、服务、视觉、运动、听觉、测试'],
        excludes=['TTS 引擎通用合成见 ai.speech.tts', '普通 UI 布局见 ui'],
        legacy={'disposition': 'kept', 'sources': ['a11y']},
    ))
    l2 = [
        ('a11y.framework', '无障碍框架', 'Accessibility Framework', '无障碍节点树、语义标注与焦点走焦。', ['树、标注、焦点、播报'], ['辅助服务实现见 service'], ['a11y.framework']),
        ('a11y.service', '辅助功能服务', 'Accessibility Service', '实现系统辅助服务扩展与手势放大。', ['service extension、手势、放大'], ['应用侧语义见 framework'], ['a11y.service']),
        ('a11y.vision', '视觉无障碍', 'Vision Accessibility', '字号、对比度、动效与加粗等视觉适配。', ['字号、对比、动效'], ['读屏服务见 service'], []),
        ('a11y.motor', '运动无障碍', 'Motor Accessibility', '触控目标、开关控制等运动障碍适配。', ['触控目标、开关控制'], ['视觉见 vision'], []),
        ('a11y.hearing', '听觉无障碍', 'Hearing Accessibility', '字幕、闪光提示与音乐触感等。', ['字幕、闪光、触感'], ['媒体播放见 media'], []),
        ('a11y.testing', '无障碍测试', 'Accessibility Testing', '无障碍扫描与读屏测试工具入口。', ['scanner、读屏测试'], ['框架语义见 framework'], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="a11y", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- a11y.framework ---
    leaf(f, "a11y.framework.tree", "a11y.framework", "framework_operation", "无障碍节点树", "Accessibility Node Tree",
         "构建与查询无障碍节点树。", ['AccessibilityNodeInfo / UIAccessibility'], ['标注见 labeling'],
         B(('AccessibilityNodeInfo', 'https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo'), ('UIAccessibility', 'https://developer.apple.com/documentation/uikit/accessibility', 'guide'), ('accessibility', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility')), {'disposition': 'kept', 'sources': ['a11y.framework.tree']}, level="L3", privacy="none")
    leaf(f, "a11y.framework.labeling", "a11y.framework", "framework_operation", "语义标注", "Semantic Labeling",
         "为控件提供可访问名称、提示与角色。", ['contentDescription / accessibilityLabel'], ['节点树见 tree'],
         B(('ViewCompat.setAccessibilityDelegate', 'https://developer.android.com/reference/androidx/core/view/ViewCompat'), ('accessibilityLabel', 'https://developer.apple.com/documentation/swiftui/view/accessibilitylabel(_:)', 'method'), ('accessibilityText', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.framework.focus", "a11y.framework", "framework_operation", "无障碍焦点", "Accessibility Focus",
         "管理无障碍焦点顺序与主动聚焦。", ['focus order / accessibilityFocus'], ['播报见 announce'],
         B(('focusable / nextFocus', 'https://developer.android.com/guide/topics/ui/accessibility', 'guide'), ('accessibilityFocus', 'https://developer.apple.com/documentation/uikit/uiaccessibility', 'guide'), ('accessibilityFocus', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-accessibility')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.framework.announce", "a11y.framework", "framework_operation", "动态播报", "Live Announcements",
         "主动播报内容或状态变化。", ['announceForAccessibility / live region'], ['焦点见 focus'],
         B(('announceForAccessibility', 'https://developer.android.com/reference/android/view/View'), ('UIAccessibility.post', 'https://developer.apple.com/documentation/uikit/uiaccessibility', 'guide'), ('sendAccessibilityEvent', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-accessibility')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.framework.grouping", "a11y.framework", "framework_operation", "分组朗读", "Grouped Reading",
         "将组合控件作为整体朗读。", ['shouldGroupAccessibilityChildren'], ['标注见 labeling'],
         B(('AccessibilityNodeInfo', 'https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo'), ('accessibilityElement(children:)', 'https://developer.apple.com/documentation/swiftui/view/accessibilityelement(children:)', 'method'), ('accessibilityGroup', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-accessibility')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.framework.custom_provider", "a11y.framework", "framework_operation", "自绘无障碍提供方", "Custom Draw Accessibility Provider",
         "为自绘/自定义渲染内容提供无障碍节点。", ['AccessibilityNodeProvider'], ['标准控件见 tree'],
         B(('AccessibilityNodeProvider', 'https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeProvider'), ('UIAccessibilityContainer', 'https://developer.apple.com/documentation/uikit/uiaccessibilitycontainer', 'protocol'), ('accessibility custom', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-accessibility')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.framework.actions", "a11y.framework", "framework_operation", "自定义无障碍动作", "Custom Accessibility Actions",
         "向辅助技术暴露自定义动作。", ['custom actions'], ['标注见 labeling'],
         B(('AccessibilityAction', 'https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat.AccessibilityActionCompat'), ('AccessibilityAction', 'https://developer.apple.com/documentation/swiftui/accessibilityactionkind', 'struct'), ('accessibilityAction', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-accessibility')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- a11y.service ---
    leaf(f, "a11y.service.extension", "a11y.service", "service_operation", "辅助服务扩展", "Accessibility Service Extension",
         "实现系统辅助功能服务。", ['AccessibilityService'], ['节点查询见 node_query'],
         B(('AccessibilityService', 'https://developer.android.com/reference/android/accessibilityservice/AccessibilityService'), None, ('AccessibilityExtensionAbility', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-accessibilityextensionability')), {'disposition': 'kept', 'sources': ['a11y.service.extension']}, level="L3", privacy="none")
    leaf(f, "a11y.service.event", "a11y.service", "service_operation", "辅助事件监听", "Accessibility Event Listen",
         "接收窗口与内容变化等辅助事件。", ['onAccessibilityEvent'], ['服务见 extension'],
         B(('AccessibilityEvent', 'https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent'), None, ('accessibility event', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/accessibilitykit-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.service.gesture", "a11y.service", "service_operation", "辅助手势派发", "Accessibility Gesture Dispatch",
         "由辅助服务派发手势操作。", ['dispatchGesture'], ['服务见 extension'],
         B(('GestureDescription', 'https://developer.android.com/reference/android/accessibilityservice/GestureDescription'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.service.magnification", "a11y.service", "service_operation", "放大镜控制", "Magnification Control",
         "控制系统放大镜能力。", ['MagnificationController'], ['视觉字号见 vision'],
         B(('MagnificationController', 'https://developer.android.com/reference/android/accessibilityservice/AccessibilityService.MagnificationController'), ('Zoom', 'https://developer.apple.com/accessibility/', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.service.node_query", "a11y.service", "service_operation", "节点查询遍历", "Node Query Traversal",
         "从辅助服务侧查询与遍历节点。", ['findAccessibilityNodeInfos'], ['应用侧树见 framework.tree'],
         B(('AccessibilityService', 'https://developer.android.com/reference/android/accessibilityservice/AccessibilityService'), None, ('accessibility', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/accessibilitykit-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.service.button", "a11y.service", "service_operation", "辅助功能按钮", "Accessibility Button",
         "响应系统辅助功能按钮回调。", ['accessibilityButton'], ['服务见 extension'],
         B(('AccessibilityButtonController', 'https://developer.android.com/reference/android/accessibilityservice/AccessibilityService.AccessibilityButtonController'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- a11y.vision ---
    leaf(f, "a11y.vision.font_scale", "a11y.vision", "vision_a11y_operation", "系统字号缩放", "Font Scale",
         "适配系统字体缩放偏好。", ['fontScale'], ['加粗见 bold_text'],
         B(('Configuration.fontScale', 'https://developer.android.com/reference/android/content/res/Configuration'), ('Dynamic Type', 'https://developer.apple.com/documentation/uikit/uifont/scaling_fonts_automatically', 'guide'), ('fontSizeScale', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-config')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.vision.bold_text", "a11y.vision", "vision_a11y_operation", "粗体文本", "Bold Text",
         "适配系统粗体文本偏好。", ['boldText'], ['字号见 font_scale'],
         B(None, ('boldTextEnabled', 'https://developer.apple.com/documentation/uikit/uiaccessibility', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.vision.contrast", "a11y.vision", "vision_a11y_operation", "增强对比度", "Increase Contrast",
         "适配高对比度/区分无障碍色。", ['highContrast / Increase Contrast'], ['色反转见 invert'],
         B(('highTextContrast', 'https://developer.android.com/reference/android/provider/Settings.Secure', 'class'), ('UIAccessibility.isDarkerSystemColorsEnabled', 'https://developer.apple.com/documentation/uikit/uiaccessibility', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.vision.reduce_motion", "a11y.vision", "vision_a11y_operation", "减弱动态效果", "Reduce Motion",
         "在减弱动态效果开启时降低动画。", ['reduceMotion'], ['对比度见 contrast'],
         B(('Animator duration scale', 'https://developer.android.com/reference/android/provider/Settings.Global', 'class'), ('UIAccessibility.isReduceMotionEnabled', 'https://developer.apple.com/documentation/uikit/uiaccessibility', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.vision.invert", "a11y.vision", "vision_a11y_operation", "智能反色", "Smart Invert Colors",
         "适配智能反色，避免图片被反转。", ['accessibilityIgnoresInvertColors'], ['对比度见 contrast'],
         B(None, ('accessibilityIgnoresInvertColors', 'https://developer.apple.com/documentation/uikit/uiview', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.vision.elder_mode", "a11y.vision", "vision_a11y_operation", "适老关怀模式", "Elder Care Mode",
         "声明并同步适老化/关怀模式状态。", ['senior mode'], ['字号见 font_scale'],
         B(None, None, ('elderlyFriendly', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-accessibility')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- a11y.motor ---
    leaf(f, "a11y.motor.touch_target", "a11y.motor", "motor_operation", "触控目标尺寸", "Touch Target Size",
         "保证可交互控件满足最小触控目标。", ['min touch target'], ['开关控制见 switch_control'],
         B(('Material touch target', 'https://developer.android.com/guide/topics/ui/accessibility/apps', 'guide'), ('Apple HIG touch target', 'https://developer.apple.com/design/human-interface-guidelines/accessibility', 'guide'), ('touch target', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-accessibility')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.motor.switch_control", "a11y.motor", "motor_operation", "开关控制适配", "Switch Control Adaptation",
         "适配开关控制扫描与选择。", ['Switch Control'], ['触控目标见 touch_target'],
         B(None, ('Switch Control', 'https://developer.apple.com/accessibility/', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.motor.sticky_keys", "a11y.motor", "motor_operation", "粘滞键与慢速键", "Sticky and Slow Keys",
         "适配键盘粘滞键/慢速键偏好。", ['sticky keys'], ['开关控制见 switch_control'],
         B(None, ('Keyboard accessibility', 'https://developer.apple.com/accessibility/', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.motor.assistive_touch", "a11y.motor", "motor_operation", "辅助触控", "Assistive Touch",
         "适配辅助触控手势与指针。", ['AssistiveTouch'], ['触控目标见 touch_target'],
         B(None, ('AssistiveTouch', 'https://developer.apple.com/accessibility/', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.motor.timing_controls", "a11y.motor", "motor_operation", "时限操作可延长", "Extendable Time Limits",
         "为限时交互提供延长或关闭时限。", ['extend time limits'], ['触控目标见 touch_target'],
         B(None, ('Accessibility Timeout', 'https://developer.apple.com/design/human-interface-guidelines/accessibility', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- a11y.hearing ---
    leaf(f, "a11y.hearing.caption", "a11y.hearing", "hearing_operation", "字幕与转写", "Captions and Transcription",
         "提供或遵循系统字幕偏好。", ['closed captions'], ['媒体播放见 media'],
         B(('CaptioningManager', 'https://developer.android.com/reference/android/view/accessibility/CaptioningManager'), ('AVTextStyleRule / Media accessibility', 'https://developer.apple.com/documentation/avfoundation', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.hearing.audio_description", "a11y.hearing", "hearing_operation", "音频描述", "Audio Description",
         "为视频提供音频描述轨道支持。", ['audio description'], ['字幕见 caption'],
         B(None, ('Media Accessibility', 'https://developer.apple.com/documentation/mediaaccessibility', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.hearing.flashing", "a11y.hearing", "hearing_operation", "闪光与视觉告警", "Flash and Visual Alerts",
         "用闪光/视觉方式提示告警。", ['LED/flash alerts'], ['字幕见 caption'],
         B(None, ('LED Flash for Alerts', 'https://developer.apple.com/accessibility/', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.hearing.mono_audio", "a11y.hearing", "hearing_operation", "单声道音频", "Mono Audio",
         "适配单声道音频偏好。", ['mono audio'], ['媒体路由见 device'],
         B(None, ('UIAccessibility.isMonoAudioEnabled', 'https://developer.apple.com/documentation/uikit/uiaccessibility', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.hearing.music_haptics", "a11y.hearing", "hearing_operation", "音乐触感反馈", "Music Haptics",
         "将音乐节奏转为触感反馈。", ['music haptics'], ['通用触感见 device'],
         B(None, ('Music Haptics', 'https://developer.apple.com/accessibility/', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- a11y.testing ---
    leaf(f, "a11y.testing.scanner", "a11y.testing", "testing_operation", "无障碍扫描器", "Accessibility Scanner",
         "运行无障碍问题自动扫描。", ['Accessibility Scanner / Accessibility Inspector'], ['读屏测试见 screen_reader_test'],
         B(('Accessibility Scanner', 'https://support.google.com/accessibility/android/answer/6376570', 'guide'), ('Accessibility Inspector', 'https://developer.apple.com/documentation/accessibility/accessibility-inspector', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.testing.screen_reader_test", "a11y.testing", "testing_operation", "读屏测试", "Screen Reader Testing",
         "用读屏进行端到端无障碍测试。", ['TalkBack / VoiceOver tests'], ['扫描器见 scanner'],
         B(('Espresso a11y checks', 'https://developer.android.com/guide/topics/ui/accessibility/testing', 'guide'), ('XCTest accessibility', 'https://developer.apple.com/documentation/xctest', 'framework'), ('Hypium a11y', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.testing.unit_checks", "a11y.testing", "testing_operation", "无障碍单元断言", "Accessibility Unit Assertions",
         "在单元/UI 测试中断言无障碍属性。", ['accessibility assertions'], ['扫描器见 scanner'],
         B(('AccessibilityChecks', 'https://developer.android.com/guide/topics/ui/accessibility/testing', 'guide'), ('XCUIElement accessibility', 'https://developer.apple.com/documentation/xctest', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "a11y.testing.automation", "a11y.testing", "testing_operation", "无障碍自动化驱动", "Accessibility Automation Driving",
         "通过无障碍树驱动 UI 自动化。", ['UIAutomator a11y tree'], ['单元断言见 unit_checks'],
         B(('UiAutomator', 'https://developer.android.com/training/testing/other-components/ui-automator', 'guide'), ('XCUITest', 'https://developer.apple.com/documentation/xctest', 'framework'), ('Hypium', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("a11y", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
