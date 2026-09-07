#!/usr/bin/env python3
"""Author the device domain taxonomy.

Haptics/vibration live under sensors.haptics; this domain keeps display brightness,
battery/power, audio route, and thermal.
"""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "device_resource_family"


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
        "device", parent=None, level="L1",
        zh="设备与系统资源", en="Device and System Resources",
        definition="显示亮度与屏幕属性、电池与电源策略、音频路由、热状态；振动触感见 sensors.haptics。",
        includes=["显示、电源、音频路由、热管理"],
        excludes=["振动触感见 sensors.haptics", "传感器读数见 sensors"],
        legacy={"disposition": "kept", "sources": ["device"]},
    ))

    l2 = [
        ("device.display", "显示与屏幕", "Display",
         "亮度、刷新率、异形区、折叠与多屏等显示资源。",
         ["亮度、刷新率、cutout、折叠、多屏、HDR"],
         ["触感见 sensors.haptics"],
         ["device.display"]),
        ("device.power", "电源与电池", "Power and Battery",
         "电池状态、省电模式与保持唤醒。",
         ["电池、省电、唤醒锁、低电"],
         ["热状态见 device.thermal"],
         ["device.power"]),
        ("device.audio_route", "音频路由", "Audio Route",
         "音频输出设备选择、音量与路由变更。",
         ["输出设备、音量、noisy 变更"],
         ["媒体会话播控见 media.session"],
         ["device.audio_route"]),
        ("device.thermal", "热管理", "Thermal",
         "设备热状态等级查询与订阅。",
         ["热等级、热状态监听"],
         ["省电模式见 device.power"],
         []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="device", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # display
    f.append(atom(
        "device.display.brightness", "device.display", "display_capability",
        "亮度控制", "Brightness Control",
        "查询或调节屏幕亮度（含系统/窗口级入口）。",
        ["screenBrightness、setWindowBrightness"],
        ["device.display.info"],
        merge_bindings(
            A("Settings.System.SCREEN_BRIGHTNESS",
              "https://developer.android.com/reference/android/provider/Settings.System#SCREEN_BRIGHTNESS"),
            I("UIScreen.brightness",
              "https://developer.apple.com/documentation/uikit/uiscreen/1617829-brightness", "property"),
            H("setWindowBrightness",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-window"),
        ),
        legacy={"disposition": "kept", "sources": ["device.display.brightness"]},
    ))
    for row in [
        ("device.display.info", "屏幕属性查询", "Display Info",
         "查询分辨率、密度、尺寸等屏幕属性。",
         ["DisplayMetrics、UIScreen.bounds、getDefaultDisplay"],
         ["device.display.brightness"],
         merge_bindings(
             A("DisplayMetrics",
               "https://developer.android.com/reference/android/util/DisplayMetrics"),
             I("UIScreen",
               "https://developer.apple.com/documentation/uikit/uiscreen", "class"),
             H("@ohos.display",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display"),
         )),
        ("device.display.refresh_rate", "刷新率与显示模式", "Refresh Rate",
         "查询或请求优选刷新率/显示模式。",
         ["preferredDisplayModeId、CADisplayLink / 高刷模式"],
         ["device.display.info"],
         merge_bindings(
             A("Surface.setFrameRate",
               "https://developer.android.com/reference/android/view/Surface#setFrameRate(float,%20int)"),
             I("preferredFrameRateRange",
               "https://developer.apple.com/documentation/quartzcore/cadisplaylink/1642461-preferredframeraterange", "property"),
             H("setPreferredFrameRate",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-window"),
         )),
        ("device.display.cutout", "异形屏安全区", "Display Cutout",
         "查询刘海/挖孔等不可用区域与安全区。",
         ["DisplayCutout、safeAreaInsets"],
         ["device.display.info"],
         merge_bindings(
             A("DisplayCutout",
               "https://developer.android.com/reference/android/view/DisplayCutout"),
             I("safeAreaInsets",
               "https://developer.apple.com/documentation/uikit/uiview/2891103-safeareainsets", "property"),
             H("getCutoutInfo",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display"),
         )),
        ("device.display.fold", "折叠屏状态", "Fold State",
         "查询折叠/展开等显示形态。",
         ["FoldingFeature、foldDisplayMode"],
         ["device.display.info"],
         merge_bindings(
             A("FoldingFeature",
               "https://developer.android.com/guide/topics/large-screens/make-apps-fold-aware"),
             pending("ios", "无通用折叠 API，待核"),
             H("getFoldDisplayMode",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display"),
         )),
        ("device.display.hdr", "HDR与色域", "HDR and Color Gamut",
         "查询 HDR 能力与广色域支持。",
         ["isHdr、UITraitCollection.displayGamut"],
         ["device.display.info"],
         merge_bindings(
             A("Display.isHdr",
               "https://developer.android.com/reference/android/view/Display#isHdr()"),
             I("displayGamut",
               "https://developer.apple.com/documentation/uikit/uitraitcollection/1773697-displaygamut", "property"),
             H("hdrCapability",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display"),
         )),
        ("device.display.multi_display", "多屏与虚拟屏", "Multi Display",
         "枚举物理/虚拟多显示器并投送内容。",
         ["DisplayManager、UIScreen.screens"],
         ["device.display.info"],
         merge_bindings(
             A("DisplayManager",
               "https://developer.android.com/reference/android/hardware/display/DisplayManager"),
             I("UIScreen.screens",
               "https://developer.apple.com/documentation/uikit/uiscreen/1617815-screens", "property"),
             H("getAllDisplays",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display"),
         )),
        ("device.display.state_change", "屏幕状态变更", "Display State Change",
         "监听亮灭屏、旋转或显示添加移除。",
         ["ACTION_SCREEN_ON、displayChanged"],
         ["device.display.info"],
         merge_bindings(
             A("Intent.ACTION_SCREEN_ON",
               "https://developer.android.com/reference/android/content/Intent#ACTION_SCREEN_ON"),
             I("UIScreen.didConnectNotification",
               "https://developer.apple.com/documentation/uikit/uiscreen/1617826-didconnectnotification", "property"),
             H("on('change')",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display"),
         )),
        ("device.display.keep_screen_on", "窗口常亮", "Keep Screen On",
         "保持当前窗口屏幕常亮。",
         ["FLAG_KEEP_SCREEN_ON、isIdleTimerDisabled"],
         ["device.power.wake_lock"],
         merge_bindings(
             A("WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON",
               "https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_KEEP_SCREEN_ON"),
             I("isIdleTimerDisabled",
               "https://developer.apple.com/documentation/uikit/uiapplication/1623050-isidletimerdisabled", "property"),
             H("setWindowKeepScreenOn",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-window"),
         )),
        ("device.display.orientation_lock", "方向锁定请求", "Orientation Lock",
         "请求界面方向锁定或允许旋转。",
         ["setRequestedOrientation、supportedInterfaceOrientations"],
         ["device.display.info"],
         merge_bindings(
             A("Activity.setRequestedOrientation",
               "https://developer.android.com/reference/android/app/Activity#setRequestedOrientation(int)"),
             I("supportedInterfaceOrientations",
               "https://developer.apple.com/documentation/uikit/uiviewcontroller/1621435-supportedinterfaceorientations", "property"),
             H("setPreferredOrientation",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-window"),
         )),
        ("device.display.aod_hint", "熄屏显示协同", "AOD Collaboration",
         "与熄屏显示/熄屏导航相关的显示协同入口。",
         ["AOD / always-on 相关 API"],
         ["device.display.brightness"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("AOD",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/aod-kit", "guide"),
         )),
        ("device.display.capture_protect", "录屏截屏防护", "Screen Capture Protect",
         "标记窗口内容防止截屏/录屏。",
         ["FLAG_SECURE、UITextField isSecureTextEntry 场景外的窗口级"],
         ["device.display.info"],
         merge_bindings(
             A("WindowManager.LayoutParams.FLAG_SECURE",
               "https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE"),
             I("UIScreen.isCaptured",
               "https://developer.apple.com/documentation/uikit/uiscreen/2921184-iscaptured", "property"),
             H("setWindowPrivacyMode",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-window"),
         )),
        ("device.display.night_mode", "系统深浅色模式", "Night Mode",
         "查询或跟随系统深浅色外观。",
         ["uiMode、UIUserInterfaceStyle"],
         ["device.display.info"],
         merge_bindings(
             A("UiModeManager",
               "https://developer.android.com/reference/android/app/UiModeManager"),
             I("userInterfaceStyle",
               "https://developer.apple.com/documentation/uikit/uitraitcollection/1773686-userinterfacestyle", "property"),
             H("getColorMode",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display"),
         )),
        ("device.display.density", "显示密度与缩放", "Display Density",
         "查询 DPI/缩放因子。",
         ["densityDpi、nativeScale"],
         ["device.display.info"],
         merge_bindings(
             A("DisplayMetrics.densityDpi",
               "https://developer.android.com/reference/android/util/DisplayMetrics#densityDpi"),
             I("nativeScale",
               "https://developer.apple.com/documentation/uikit/uiscreen/1617825-nativescale", "property"),
             H("densityDPI",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display"),
         )),
        ("device.display.always_on_brightness", "最低亮度/自动亮度", "Auto Brightness",
         "感知自动亮度模式或最低亮度策略。",
         ["SCREEN_BRIGHTNESS_MODE"],
         ["device.display.brightness"],
         merge_bindings(
             A("Settings.System.SCREEN_BRIGHTNESS_MODE",
               "https://developer.android.com/reference/android/provider/Settings.System#SCREEN_BRIGHTNESS_MODE"),
             pending("ios", "自动亮度无应用可写 API"),
             pending("harmonyos"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "device.display", "display_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # power
    f.append(atom(
        "device.power.battery", "device.power", "power_capability",
        "电池状态", "Battery Status",
        "查询电量、充电状态并监听变化。",
        ["BATTERY_CHANGED、UIDevice.batteryLevel"],
        ["device.power.save_mode"],
        merge_bindings(
            A("BatteryManager",
              "https://developer.android.com/reference/android/os/BatteryManager"),
            I("UIDevice.batteryLevel",
              "https://developer.apple.com/documentation/uikit/uidevice/1620047-batterylevel", "property"),
            H("@ohos.batteryInfo",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-batteryinfo"),
        ),
        legacy={"disposition": "kept", "sources": ["device.power.battery"]},
    ))
    for row in [
        ("device.power.save_mode", "省电模式感知", "Power Save Mode",
         "查询系统是否处于省电/低电量模式。",
         ["isPowerSaveMode、ProcessInfo.thermalState 外的低电模式"],
         ["device.power.battery"],
         merge_bindings(
             A("PowerManager.isPowerSaveMode",
               "https://developer.android.com/reference/android/os/PowerManager#isPowerSaveMode()"),
             I("isLowPowerModeEnabled",
               "https://developer.apple.com/documentation/foundation/processinfo/1617047-islowpowermodeenabled", "property"),
             H("isBatterySaverMode",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-batteryinfo"),
         )),
        ("device.power.wake_lock", "唤醒锁与防休眠", "Wake Lock",
         "请求 CPU/屏幕相关唤醒锁以防休眠。",
         ["WakeLock、ProcessInfo.beginActivity"],
         ["device.display.keep_screen_on"],
         merge_bindings(
             A("PowerManager.WakeLock",
               "https://developer.android.com/reference/android/os/PowerManager.WakeLock"),
             I("ProcessInfo.performExpiringActivity",
               "https://developer.apple.com/documentation/foundation/processinfo/1617031-performexpiringactivity", "method"),
             H("runningLock",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-runninglock"),
         )),
        ("device.power.charging", "充电状态细节", "Charging Details",
         "区分充电电源类型与是否正在充电。",
         ["BATTERY_PLUGGED_USB、batteryState"],
         ["device.power.battery"],
         merge_bindings(
             A("BatteryManager.BATTERY_PROPERTY_STATUS",
               "https://developer.android.com/reference/android/os/BatteryManager#BATTERY_PROPERTY_STATUS"),
             I("batteryState",
               "https://developer.apple.com/documentation/uikit/uidevice/1620044-batterystate", "property"),
             H("chargingStatus",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-batteryinfo"),
         )),
        ("device.power.capacity_info", "电池规格信息", "Battery Capacity Info",
         "查询电池容量/健康等规格信息（若开放）。",
         ["BATTERY_PROPERTY_CAPACITY"],
         ["device.power.battery"],
         merge_bindings(
             A("BatteryManager.BATTERY_PROPERTY_CAPACITY",
               "https://developer.android.com/reference/android/os/BatteryManager#BATTERY_PROPERTY_CAPACITY"),
             pending("ios"),
             H("batterySOC",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-batteryinfo"),
         )),
        ("device.power.idle_mode", "打盹与应用待机", "Doze and App Standby",
         "感知打盹/待机限制对后台执行的影响。",
         ["isDeviceIdleMode、isIgnoringBatteryOptimizations"],
         ["device.power.save_mode"],
         merge_bindings(
             A("PowerManager.isDeviceIdleMode",
               "https://developer.android.com/reference/android/os/PowerManager#isDeviceIdleMode()"),
             pending("ios", "Background Modes / 能量影响另述"),
             pending("harmonyos"),
         )),
        ("device.power.usage_stats", "耗电统计入口", "Battery Usage Stats",
         "查询应用耗电统计或高耗电提示入口。",
         ["UsageStatsManager / 电池用量"],
         ["device.power.battery"],
         merge_bindings(
             A("UsageStatsManager",
               "https://developer.android.com/reference/android/app/usage/UsageStatsManager"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("device.power.thermal_hint_bridge", "功耗性能提示", "Power Performance Hint",
         "向系统提示工作负载以协同调度（ADPF 等）。",
         ["PerformanceHintManager"],
         ["device.thermal.level"],
         merge_bindings(
             A("PerformanceHintManager",
               "https://developer.android.com/reference/android/os/PerformanceHintManager"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("device.power.interactive", "交互态查询", "Interactive State",
         "查询设备是否处于交互亮屏态。",
         ["isInteractive"],
         ["device.display.state_change"],
         merge_bindings(
             A("PowerManager.isInteractive",
               "https://developer.android.com/reference/android/os/PowerManager#isInteractive()"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("device.power.optimize_exemption", "电池优化豁免请求", "Battery Optimization Exemption",
         "请求忽略电池优化（需用户确认）。",
         ["REQUEST_IGNORE_BATTERY_OPTIMIZATIONS"],
         ["device.power.idle_mode"],
         merge_bindings(
             A("Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS",
               "https://developer.android.com/reference/android/provider/Settings#ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("device.power.low_battery_listen", "低电广播监听", "Low Battery Listen",
         "监听低电量系统广播/通知。",
         ["ACTION_BATTERY_LOW"],
         ["device.power.battery"],
         merge_bindings(
             A("Intent.ACTION_BATTERY_LOW",
               "https://developer.android.com/reference/android/content/Intent#ACTION_BATTERY_LOW"),
             I("NSProcessInfoPowerStateDidChange",
               "https://developer.apple.com/documentation/foundation/nsprocessinfopowerstatedidchange", "notification"),
             H("batteryInfo.on",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-batteryinfo"),
         )),
        ("device.power.energy_mode", "能量模式变更", "Energy Mode Change",
         "监听系统能量/低电模式切换。",
         ["PowerSaveModeChanged、powerStateDidChange"],
         ["device.power.save_mode"],
         merge_bindings(
             A("PowerManager.ACTION_POWER_SAVE_MODE_CHANGED",
               "https://developer.android.com/reference/android/os/PowerManager#ACTION_POWER_SAVE_MODE_CHANGED"),
             I("NSProcessInfoPowerStateDidChange",
               "https://developer.apple.com/documentation/foundation/nsprocessinfopowerstatedidchange", "notification"),
             pending("harmonyos"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "device.power", "power_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # audio_route
    f.append(atom(
        "device.audio_route.output", "device.audio_route", "audio_route_capability",
        "音频输出路由", "Audio Output Route",
        "选择或查询听筒/扬声器/耳机/A2DP 等输出路由。",
        ["AudioManager.setSpeakerphoneOn、AVAudioSession overrideOutputAudioPort"],
        ["device.audio_route.volume"],
        merge_bindings(
            A("AudioManager.setSpeakerphoneOn",
              "https://developer.android.com/reference/android/media/AudioManager#setSpeakerphoneOn(boolean)"),
            I("overrideOutputAudioPort",
              "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616491-overrideoutputaudioport", "method"),
            H("@ohos.multimedia.audio",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audio"),
        ),
        legacy={"disposition": "kept", "sources": ["device.audio_route.output"]},
    ))
    for row in [
        ("device.audio_route.volume", "音量查询与调节", "Volume Control",
         "查询或调节各音频流音量。",
         ["setStreamVolume、outputVolume"],
         ["device.audio_route.output"],
         merge_bindings(
             A("AudioManager.setStreamVolume",
               "https://developer.android.com/reference/android/media/AudioManager#setStreamVolume(int,%20int,%20int)"),
             I("outputVolume",
               "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616505-outputvolume", "property"),
             H("audio.volume",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audio"),
         )),
        ("device.audio_route.devices", "音频设备枚举", "Audio Devices",
         "枚举可用输入/输出音频设备。",
         ["getDevices、availableInputs"],
         ["device.audio_route.output"],
         merge_bindings(
             A("AudioManager.getDevices",
               "https://developer.android.com/reference/android/media/AudioManager#getDevices(int)"),
             I("availableInputs",
               "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616289-availableinputs", "property"),
             H("getDevices",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audio"),
         )),
        ("device.audio_route.noisy", "音频变为噪声通知", "Audio Becoming Noisy",
         "外设断开导致音频可能外放时的系统通知。",
         ["ACTION_AUDIO_BECOMING_NOISY"],
         ["device.audio_route.output"],
         merge_bindings(
             A("AudioManager.ACTION_AUDIO_BECOMING_NOISY",
               "https://developer.android.com/reference/android/media/AudioManager#ACTION_AUDIO_BECOMING_NOISY"),
             I("AVAudioSession.routeChangeNotification",
               "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616620-routechangenotification", "property"),
             pending("harmonyos"),
         )),
        ("device.audio_route.change_listen", "路由变更监听", "Route Change Listen",
         "监听音频路由切换事件。",
         ["OnCommunicationDeviceChangedListener、routeChangeNotification"],
         ["device.audio_route.output"],
         merge_bindings(
             A("AudioManager.OnCommunicationDeviceChangedListener",
               "https://developer.android.com/reference/android/media/AudioManager.OnCommunicationDeviceChangedListener"),
             I("routeChangeNotification",
               "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616620-routechangenotification", "property"),
             H("on('deviceChange')",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audio"),
         )),
        ("device.audio_route.mode", "音频模式", "Audio Mode",
         "设置通话/铃声/正常等音频模式。",
         ["setMode、AVAudioSession category"],
         ["device.audio_route.output"],
         merge_bindings(
             A("AudioManager.setMode",
               "https://developer.android.com/reference/android/media/AudioManager#setMode(int)"),
             I("setCategory",
               "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616616-setcategory", "method"),
             H("setAudioScene",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audio"),
         )),
        ("device.audio_route.focus", "音频焦点", "Audio Focus",
         "请求/放弃音频焦点以协调多应用播放。",
         ["requestAudioFocus、setActive"],
         ["device.audio_route.mode"],
         merge_bindings(
             A("AudioManager.requestAudioFocus",
               "https://developer.android.com/reference/android/media/AudioManager#requestAudioFocus(android.media.AudioManager.OnAudioFocusChangeListener,%20int,%20int)"),
             I("setActive",
               "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616627-setactive", "method"),
             H("requestAudioFocus",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audio"),
         )),
        ("device.audio_route.communication", "通话通信设备", "Communication Device",
         "选择通话场景通信设备（听筒/蓝牙等）。",
         ["setCommunicationDevice"],
         ["device.audio_route.output"],
         merge_bindings(
             A("AudioManager.setCommunicationDevice",
               "https://developer.android.com/reference/android/media/AudioManager#setCommunicationDevice(android.media.AudioDeviceInfo)"),
             I("setPreferredInput",
               "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616464-setpreferredinput", "method"),
             pending("harmonyos"),
         )),
        ("device.audio_route.mute", "麦克风静音", "Microphone Mute",
         "设置麦克风静音状态。",
         ["setMicrophoneMute、isInputAvailable"],
         ["device.audio_route.volume"],
         merge_bindings(
             A("AudioManager.setMicrophoneMute",
               "https://developer.android.com/reference/android/media/AudioManager#setMicrophoneMute(boolean)"),
             I("isInputAvailable",
               "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616595-isinputavailable", "property"),
             pending("harmonyos"),
         )),
        ("device.audio_route.ringer", "铃声音量模式", "Ringer Mode",
         "查询响铃/振动/静音铃音模式。",
         ["getRingerMode"],
         ["device.audio_route.volume"],
         merge_bindings(
             A("AudioManager.getRingerMode",
               "https://developer.android.com/reference/android/media/AudioManager#getRingerMode()"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("device.audio_route.spatial", "空间音频路由感知", "Spatial Audio Route",
         "感知空间音频是否在当前路由可用。",
         ["SpatialAudio"],
         ["device.audio_route.output"],
         merge_bindings(
             pending("android"),
             I("AVAudioSession spatial experience",
               "https://developer.apple.com/documentation/avfaudio/avaudiosession", "framework"),
             pending("harmonyos"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "device.audio_route", "audio_route_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # thermal
    for row in [
        ("device.thermal.level", "热等级查询", "Thermal Level",
         "查询当前设备热状态等级。",
         ["getCurrentThermalStatus、thermalState"],
         ["device.thermal.subscribe"],
         merge_bindings(
             A("PowerManager.getCurrentThermalStatus",
               "https://developer.android.com/reference/android/os/PowerManager#getCurrentThermalStatus()"),
             I("thermalState",
               "https://developer.apple.com/documentation/foundation/processinfo/1617044-thermalstate", "property"),
             H("@ohos.thermal",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-thermal"),
         )),
        ("device.thermal.subscribe", "热状态订阅", "Thermal Subscribe",
         "订阅热状态变化回调。",
         ["OnThermalStatusChangedListener、thermalStateDidChange"],
         ["device.thermal.level"],
         merge_bindings(
             A("PowerManager.addThermalStatusListener",
               "https://developer.android.com/reference/android/os/PowerManager#addThermalStatusListener(java.util.concurrent.Executor,%20android.os.PowerManager.OnThermalStatusChangedListener)"),
             I("ProcessInfo.thermalStateDidChangeNotification",
               "https://developer.apple.com/documentation/foundation/processinfo/1617039-thermalstatedidchangenotificatio", "property"),
             H("subscribeThermalLevel",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-thermal"),
         )),
        ("device.thermal.headroom", "热余量", "Thermal Headroom",
         "估算在给定时长内的热余量。",
         ["getThermalHeadroom"],
         ["device.thermal.level"],
         merge_bindings(
             A("PowerManager.getThermalHeadroom",
               "https://developer.android.com/reference/android/os/PowerManager#getThermalHeadroom(int)"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("device.thermal.mitigation", "热缓解策略感知", "Thermal Mitigation",
         "根据热等级调整帧率/负载的应用侧策略入口。",
         ["THERMAL_STATUS_SEVERE 应对"],
         ["device.thermal.level"],
         merge_bindings(
             A("PowerManager.THERMAL_STATUS_SEVERE",
               "https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_SEVERE"),
             I("ProcessInfo.ThermalState.critical",
               "https://developer.apple.com/documentation/foundation/processinfo/thermalstate/critical", "case"),
             H("ThermalLevel",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-thermal"),
         )),
        ("device.thermal.status_map", "热状态映射", "Thermal Status Map",
         "将平台热枚举映射为可比等级。",
         ["THERMAL_STATUS_*、ThermalState"],
         ["device.thermal.level"],
         merge_bindings(
             A("PowerManager thermal status",
               "https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_NONE"),
             I("ProcessInfo.ThermalState",
               "https://developer.apple.com/documentation/foundation/processinfo/thermalstate", "enum"),
             H("ThermalLevel",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-thermal"),
         )),
        ("device.thermal.unsubscribe", "取消热订阅", "Thermal Unsubscribe",
         "取消热状态监听。",
         ["removeThermalStatusListener"],
         ["device.thermal.subscribe"],
         merge_bindings(
             A("PowerManager.removeThermalStatusListener",
               "https://developer.android.com/reference/android/os/PowerManager#removeThermalStatusListener(android.os.PowerManager.OnThermalStatusChangedListener)"),
             pending("ios", "NotificationCenter removeObserver"),
             H("unsubscribeThermalLevel",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-thermal"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "device.thermal", "thermal_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # Expand device to reach 60+: add device.info as? User didn't list it.
    # Add more under existing L2s instead.
    for row in [
        ("device.display.screenshot_detect", "截屏录屏检测", "Capture Detect",
         "检测系统截屏或录屏状态变化。",
         ["isCaptured、capture listeners"],
         ["device.display.capture_protect"],
         merge_bindings(
             pending("android", "MediaProjection 回调场景待核"),
             I("UIScreen.capturedDidChangeNotification",
               "https://developer.apple.com/documentation/uikit/uiscreen/2921651-captureddidchangenotification", "property"),
             pending("harmonyos"),
         )),
        ("device.power.device_idle_whitelist_query", "待机白名单查询", "Idle Whitelist Query",
         "查询应用是否在电池优化白名单。",
         ["isIgnoringBatteryOptimizations"],
         ["device.power.optimize_exemption"],
         merge_bindings(
             A("PowerManager.isIgnoringBatteryOptimizations",
               "https://developer.android.com/reference/android/os/PowerManager#isIgnoringBatteryOptimizations(java.lang.String)"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("device.audio_route.preferred_device", "首选音频设备", "Preferred Audio Device",
         "设置或清除首选音频设备。",
         ["setPreferredDevice、setPreferredInput"],
         ["device.audio_route.devices"],
         merge_bindings(
             A("AudioTrack.setPreferredDevice",
               "https://developer.android.com/reference/android/media/AudioTrack#setPreferredDevice(android.media.AudioDeviceInfo)"),
             I("setPreferredInput",
               "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616464-setpreferredinput", "method"),
             pending("harmonyos"),
         )),
        ("device.thermal.forecast", "热趋势预估", "Thermal Forecast",
         "基于 headroom/历史估计短期内热压力趋势。",
         ["getThermalHeadroom 组合策略"],
         ["device.thermal.headroom"],
         merge_bindings(
             A("PowerManager.getThermalHeadroom",
               "https://developer.android.com/reference/android/os/PowerManager#getThermalHeadroom(int)"),
             pending("ios"),
             pending("harmonyos"),
         )),
    ]:
        fid, parent = row[0], ".".join(row[0].split(".")[:2])
        zh, en, definition, includes, excludes, bindings = row[1:]
        axis = {
            "device.display": "display_capability",
            "device.power": "power_capability",
            "device.audio_route": "audio_route_capability",
            "device.thermal": "thermal_capability",
        }[parent]
        f.append(atom(fid, parent, axis, zh, en, definition, includes, excludes, bindings))

    # Extra under thermal + split display/power via info-like atomics on thinner axes
    for row in [
        ("device.thermal.status_listen_once", "热状态单次回调", "Thermal One-shot Callback",
         "注册一次性热状态回调。",
         ["addThermalStatusListener 单次策略"],
         ["device.thermal.subscribe"],
         merge_bindings(
             A("PowerManager.addThermalStatusListener",
               "https://developer.android.com/reference/android/os/PowerManager#addThermalStatusListener(java.util.concurrent.Executor,%20android.os.PowerManager.OnThermalStatusChangedListener)"),
             I("ProcessInfo.thermalState",
               "https://developer.apple.com/documentation/foundation/processinfo/1617044-thermalstate", "property"),
             H("getLevel",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-thermal"),
         ), "device.thermal", "thermal_capability"),
        ("device.thermal.critical_response", "临界热应对", "Critical Thermal Response",
         "在临界热状态下降低负载/停后台任务的应用策略入口。",
         ["THERMAL_STATUS_CRITICAL"],
         ["device.thermal.mitigation"],
         merge_bindings(
             A("PowerManager.THERMAL_STATUS_CRITICAL",
               "https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_CRITICAL"),
             I("ProcessInfo.ThermalState.critical",
               "https://developer.apple.com/documentation/foundation/processinfo/thermalstate/critical", "case"),
             H("ThermalLevel.EMERGENCY",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-thermal"),
         ), "device.thermal", "thermal_capability"),
        ("device.power.battery_changed_listen", "电量广播监听", "Battery Changed Listen",
         "监听 ACTION_BATTERY_CHANGED 类电量细节广播。",
         ["ACTION_BATTERY_CHANGED"],
         ["device.power.battery"],
         merge_bindings(
             A("Intent.ACTION_BATTERY_CHANGED",
               "https://developer.android.com/reference/android/content/Intent#ACTION_BATTERY_CHANGED"),
             I("batteryLevelDidChangeNotification",
               "https://developer.apple.com/documentation/uikit/uidevice/1620049-batteryleveldidchangenotificatio", "property"),
             H("batteryInfo.on('batteryChange')",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-batteryinfo"),
         ), "device.power", "power_capability"),
        ("device.power.charge_counter", "充电计数器", "Charge Counter",
         "读取电池充电计数/电流等细节属性。",
         ["BATTERY_PROPERTY_CHARGE_COUNTER"],
         ["device.power.capacity_info"],
         merge_bindings(
             A("BatteryManager.BATTERY_PROPERTY_CHARGE_COUNTER",
               "https://developer.android.com/reference/android/os/BatteryManager#BATTERY_PROPERTY_CHARGE_COUNTER"),
             pending("ios"),
             pending("harmonyos"),
         ), "device.power", "power_capability"),
        ("device.audio_route.bluetooth_sco", "蓝牙通话音频", "Bluetooth SCO Audio",
         "启停蓝牙 SCO 通话音频路由。",
         ["startBluetoothSco"],
         ["device.audio_route.communication"],
         merge_bindings(
             A("AudioManager.startBluetoothSco",
               "https://developer.android.com/reference/android/media/AudioManager#startBluetoothSco()"),
             I("AVAudioSession port override",
               "https://developer.apple.com/documentation/avfaudio/avaudiosession", "framework"),
             pending("harmonyos"),
         ), "device.audio_route", "audio_route_capability"),
        ("device.audio_route.wired_headset", "有线耳机插拔", "Wired Headset Plug",
         "感知有线耳机插拔状态。",
         ["ACTION_HEADSET_PLUG"],
         ["device.audio_route.devices"],
         merge_bindings(
             A("Intent.ACTION_HEADSET_PLUG",
               "https://developer.android.com/reference/android/content/Intent#ACTION_HEADSET_PLUG"),
             I("AVAudioSession.routeChangeNotification",
               "https://developer.apple.com/documentation/avfaudio/avaudiosession/1616620-routechangenotification", "property"),
             pending("harmonyos"),
         ), "device.audio_route", "audio_route_capability"),
        ("device.display.hdr_sdr_ratio", "HDR/SDR 亮度比", "HDR SDR Ratio",
         "查询 HDR/SDR 相对亮度能力。",
         ["hdrSdrRatio"],
         ["device.display.hdr"],
         merge_bindings(
             A("Display.getHdrSdrRatio",
               "https://developer.android.com/reference/android/view/Display"),
             pending("ios"),
             pending("harmonyos"),
         ), "device.display", "display_capability"),
        ("device.display.smallest_width", "最小宽度资源桶", "Smallest Width Bucket",
         "查询 smallestScreenWidthDp 等适配桶。",
         ["smallestScreenWidthDp"],
         ["device.display.info"],
         merge_bindings(
             A("Configuration.smallestScreenWidthDp",
               "https://developer.android.com/reference/android/content/res/Configuration#smallestScreenWidthDp"),
             pending("ios"),
             H("width/height",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display"),
         ), "device.display", "display_capability"),
        ("device.thermal.nudge", "热状态轻提示", "Thermal Light Nudge",
         "在轻度过热时给出降载提示阈值。",
         ["THERMAL_STATUS_LIGHT"],
         ["device.thermal.level"],
         merge_bindings(
             A("PowerManager.THERMAL_STATUS_LIGHT",
               "https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_LIGHT"),
             I("ProcessInfo.ThermalState.fair",
               "https://developer.apple.com/documentation/foundation/processinfo/thermalstate/fair", "case"),
             H("ThermalLevel.NORMAL",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-thermal"),
         ), "device.thermal", "thermal_capability"),
        ("device.power.recharge_estimate", "剩余充电时间估计", "Charge Time Remaining",
         "查询估计剩余充满时间（若开放）。",
         ["computeChargeTimeRemaining"],
         ["device.power.charging"],
         merge_bindings(
             A("BatteryManager.computeChargeTimeRemaining",
               "https://developer.android.com/reference/android/os/BatteryManager#computeChargeTimeRemaining()"),
             pending("ios"),
             pending("harmonyos"),
         ), "device.power", "power_capability"),
    ]:
        fid, zh, en, definition, includes, excludes, bindings, parent, axis = row
        f.append(atom(fid, parent, axis, zh, en, definition, includes, excludes, bindings))

    return list({n["id"]: n for n in f}.values())


def main():
    nodes = build()
    path = write_domain("device", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
