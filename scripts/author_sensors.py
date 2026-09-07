#!/usr/bin/env python3
"""Author the sensors domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "sensor_capability_family"


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
        "sensors", parent=None, level="L1",
        zh="传感器与运动", en="Sensors and Motion",
        definition="运动/环境传感器访问、触感振动、融合感知；设备亮度/电池见 device，健康体征深度能力见 health_home。",
        includes=["运动、环境、访问订阅、触感、融合感知"],
        excludes=["亮度/电池见 device", "连续心率健康研究见 health_home"],
        legacy={"disposition": "kept", "sources": ["sensors"]},
    ))

    l2 = [
        ("sensors.motion", "运动传感器", "Motion Sensors",
         "加速度、陀螺仪、姿态、方向与线性加速度等运动读数。",
         ["加速度、陀螺、姿态、方向、重力"],
         ["环境光/气压见 sensors.environment"],
         ["sensors.motion"]),
        ("sensors.environment", "环境传感器", "Environment Sensors",
         "环境光、气压、温湿度等环境量测。",
         ["环境光、气压、温湿度"],
         ["运动传感器见 sensors.motion"],
         ["sensors.environment"]),
        ("sensors.access", "传感器访问与订阅", "Sensor Access",
         "传感器枚举、采样配置与订阅/取消。",
         ["列表、采样率、订阅、权限"],
         ["具体传感器类型见 motion/environment"],
         []),
        ("sensors.haptics", "振动与触感", "Haptics",
         "基础振动、预设效果与高级触感引擎。",
         ["振动、Core Haptics、UI 反馈"],
         ["音频路由见 device.audio_route"],
         []),
        ("sensors.fusion", "融合感知", "Sensor Fusion",
         "活动识别、静止、握持与设备姿态融合状态。",
         ["活动识别、静止、握持、姿态融合"],
         ["原始运动读数见 sensors.motion"],
         []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="sensors", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # motion
    f.append(atom(
        "sensors.motion.accel_gyro", "sensors.motion", "motion_sensor_type",
        "加速度与陀螺仪", "Accelerometer and Gyroscope",
        "读取加速度计与陀螺仪原始运动数据。",
        ["TYPE_ACCELEROMETER、TYPE_GYROSCOPE、CMAccelerometerData"],
        ["sensors.motion.attitude"],
        merge_bindings(
            A("Sensor.TYPE_ACCELEROMETER",
              "https://developer.android.com/reference/android/hardware/Sensor#TYPE_ACCELEROMETER"),
            I("CMMotionManager",
              "https://developer.apple.com/documentation/coremotion/cmmotionmanager", "class"),
            H("sensor.accelerometer",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
        ),
        legacy={"disposition": "kept", "sources": ["sensors.motion.accel_gyro"]},
    ))
    for row in [
        ("sensors.motion.attitude", "设备姿态", "Device Attitude",
         "获取设备姿态四元数/旋转矩阵。",
         ["ROTATION_VECTOR、CMDeviceMotion.attitude"],
         ["sensors.motion.accel_gyro"],
         merge_bindings(
             A("Sensor.TYPE_ROTATION_VECTOR",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_ROTATION_VECTOR"),
             I("CMAttitude",
               "https://developer.apple.com/documentation/coremotion/cmattitude", "class"),
             H("ORIENTATION",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.motion.orientation", "屏幕方向传感器", "Orientation Sensor",
         "获取设备相对世界坐标系的方位角。",
         ["TYPE_ORIENTATION / 旋转矢量推导"],
         ["sensors.motion.attitude"],
         merge_bindings(
             A("SensorManager.getOrientation",
               "https://developer.android.com/reference/android/hardware/SensorManager#getOrientation(float[],%20float[])"),
             I("CMAttitude.yaw",
               "https://developer.apple.com/documentation/coremotion/cmattitude/1616038-yaw", "property"),
             H("ORIENTATION",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.motion.gravity", "重力与线性加速度", "Gravity and Linear Acceleration",
         "分离重力分量与线性加速度。",
         ["TYPE_GRAVITY、TYPE_LINEAR_ACCELERATION"],
         ["sensors.motion.accel_gyro"],
         merge_bindings(
             A("Sensor.TYPE_LINEAR_ACCELERATION",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_LINEAR_ACCELERATION"),
             I("userAcceleration",
               "https://developer.apple.com/documentation/coremotion/cmdevicemotion/1616031-useracceleration", "property"),
             H("LINEAR_ACCELEROMETER",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.motion.magnetometer", "磁力计", "Magnetometer",
         "读取地磁场强度。",
         ["TYPE_MAGNETIC_FIELD、CMMagnetometerData"],
         ["sensors.motion.attitude"],
         merge_bindings(
             A("Sensor.TYPE_MAGNETIC_FIELD",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_MAGNETIC_FIELD"),
             I("startMagnetometerUpdates",
               "https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616112-startmagnetometerupdates", "method"),
             H("MAGNETIC_FIELD",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.motion.proximity", "近距传感器", "Proximity Sensor",
         "检测物体靠近屏幕的距离状态。",
         ["TYPE_PROXIMITY"],
         ["sensors.environment.ambient"],
         merge_bindings(
             A("Sensor.TYPE_PROXIMITY",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_PROXIMITY"),
             I("proximityState",
               "https://developer.apple.com/documentation/uikit/uidevice/1620040-proximitystate", "property"),
             H("PROXIMITY",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.motion.pedometer", "计步器", "Pedometer",
         "步数与步行相关事件计数。",
         ["TYPE_STEP_COUNTER、CMPedometer"],
         ["sensors.fusion.activity"],
         merge_bindings(
             A("Sensor.TYPE_STEP_COUNTER",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_STEP_COUNTER"),
             I("CMPedometer",
               "https://developer.apple.com/documentation/coremotion/cmpedometer", "class"),
             H("PEDOMETER",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.motion.step_detector", "步伐检测", "Step Detector",
         "单步事件检测（非累计计数）。",
         ["TYPE_STEP_DETECTOR"],
         ["sensors.motion.pedometer"],
         merge_bindings(
             A("Sensor.TYPE_STEP_DETECTOR",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_STEP_DETECTOR"),
             I("CMPedometerEvent",
               "https://developer.apple.com/documentation/coremotion/cmpedometerevent", "class"),
             pending("harmonyos"),
         )),
        ("sensors.motion.significant_motion", "显著运动触发", "Significant Motion",
         "检测用户显著移动后的一次性触发传感器。",
         ["TYPE_SIGNIFICANT_MOTION"],
         ["sensors.fusion.activity"],
         merge_bindings(
             A("Sensor.TYPE_SIGNIFICANT_MOTION",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_SIGNIFICANT_MOTION"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("sensors.motion.uncalibrated", "未校准运动读数", "Uncalibrated Motion",
         "未校准加速度/陀螺原始读数。",
         ["TYPE_ACCELEROMETER_UNCALIBRATED"],
         ["sensors.motion.accel_gyro"],
         merge_bindings(
             A("Sensor.TYPE_GYROSCOPE_UNCALIBRATED",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_GYROSCOPE_UNCALIBRATED"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("sensors.motion.game_rotation", "游戏旋转矢量", "Game Rotation Vector",
         "不依赖磁力计的旋转矢量。",
         ["TYPE_GAME_ROTATION_VECTOR"],
         ["sensors.motion.attitude"],
         merge_bindings(
             A("Sensor.TYPE_GAME_ROTATION_VECTOR",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_GAME_ROTATION_VECTOR"),
             I("CMDeviceMotion",
               "https://developer.apple.com/documentation/coremotion/cmdevicemotion", "class"),
             pending("harmonyos"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "sensors.motion", "motion_sensor_type",
            zh, en, definition, includes, excludes, bindings,
        ))

    # environment
    f.append(atom(
        "sensors.environment.ambient", "sensors.environment", "environment_sensor_type",
        "环境光", "Ambient Light",
        "读取环境光照度。",
        ["TYPE_LIGHT、ambientLight"],
        ["sensors.environment.pressure"],
        merge_bindings(
            A("Sensor.TYPE_LIGHT",
              "https://developer.android.com/reference/android/hardware/Sensor#TYPE_LIGHT"),
            pending("ios", "无通用环境光公开 API，待核"),
            H("AMBIENT_LIGHT",
              "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
        ),
        legacy={"disposition": "kept", "sources": ["sensors.environment.ambient"]},
    ))
    for row in [
        ("sensors.environment.pressure", "气压计", "Barometer",
         "读取大气压强。",
         ["TYPE_PRESSURE、CMAltimeter"],
         ["sensors.environment.ambient"],
         merge_bindings(
             A("Sensor.TYPE_PRESSURE",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_PRESSURE"),
             I("CMAltimeter",
               "https://developer.apple.com/documentation/coremotion/cmaltimeter", "class"),
             H("BAROMETER",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.environment.temperature", "环境温度", "Ambient Temperature",
         "读取环境温度（若硬件支持）。",
         ["TYPE_AMBIENT_TEMPERATURE"],
         ["sensors.environment.humidity"],
         merge_bindings(
             A("Sensor.TYPE_AMBIENT_TEMPERATURE",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_AMBIENT_TEMPERATURE"),
             pending("ios"),
             H("AMBIENT_TEMPERATURE",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.environment.humidity", "相对湿度", "Relative Humidity",
         "读取相对湿度。",
         ["TYPE_RELATIVE_HUMIDITY"],
         ["sensors.environment.temperature"],
         merge_bindings(
             A("Sensor.TYPE_RELATIVE_HUMIDITY",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_RELATIVE_HUMIDITY"),
             pending("ios"),
             H("HUMIDITY",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.environment.ultraviolet", "紫外线", "Ultraviolet",
         "读取紫外线强度（若支持）。",
         ["紫外传感器"],
         ["sensors.environment.ambient"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("ULTRAVIOLET",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.environment.hall", "霍尔传感器", "Hall Sensor",
         "磁翻盖/霍尔开关状态。",
         ["HALL"],
         ["sensors.motion.magnetometer"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("HALL",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.environment.heart_rate_basic", "基础心率传感", "Basic Heart Rate Sensor",
         "设备侧基础心率传感器读数入口（深度健康研究另域）。",
         ["TYPE_HEART_RATE"],
         ["sensors.fusion.activity"],
         merge_bindings(
             A("Sensor.TYPE_HEART_RATE",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_HEART_RATE"),
             I("HKQuantityTypeIdentifier.heartRate",
               "https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615248-heartrate", "property"),
             H("HEART_RATE",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         ), "sensitive"),
    ]:
        if len(row) == 7:
            fid, zh, en, definition, includes, excludes, bindings = row
            privacy = "none"
        else:
            fid, zh, en, definition, includes, excludes, bindings, privacy = row
        f.append(atom(
            fid, "sensors.environment", "environment_sensor_type",
            zh, en, definition, includes, excludes, bindings, privacy=privacy,
        ))

    # access
    for row in [
        ("sensors.access.list", "传感器列表", "Sensor List",
         "枚举设备可用传感器及其能力参数。",
         ["getSensorList、isAccelerometerAvailable"],
         ["sensors.access.subscribe"],
         merge_bindings(
             A("SensorManager.getSensorList",
               "https://developer.android.com/reference/android/hardware/SensorManager#getSensorList(int)"),
             I("isAccelerometerAvailable",
               "https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616116-isaccelerometeravailable", "property"),
             H("getSensorList",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.access.subscribe", "订阅传感器数据", "Subscribe Sensor",
         "注册监听以持续接收传感器事件。",
         ["registerListener、startDeviceMotionUpdates、sensor.on"],
         ["sensors.access.unsubscribe"],
         merge_bindings(
             A("SensorManager.registerListener",
               "https://developer.android.com/reference/android/hardware/SensorManager#registerListener(android.hardware.SensorEventListener,%20android.hardware.Sensor,%20int)"),
             I("startDeviceMotionUpdates",
               "https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616133-startdevicemotionupdates", "method"),
             H("sensor.on",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.access.unsubscribe", "取消订阅", "Unsubscribe Sensor",
         "注销传感器监听。",
         ["unregisterListener、stopDeviceMotionUpdates"],
         ["sensors.access.subscribe"],
         merge_bindings(
             A("SensorManager.unregisterListener",
               "https://developer.android.com/reference/android/hardware/SensorManager#unregisterListener(android.hardware.SensorEventListener)"),
             I("stopDeviceMotionUpdates",
               "https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616120-stopdevicemotionupdates", "method"),
             H("sensor.off",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.access.sampling", "采样率配置", "Sampling Rate",
         "配置传感器采样周期/延迟。",
         ["SENSOR_DELAY_GAME、deviceMotionUpdateInterval"],
         ["sensors.access.subscribe"],
         merge_bindings(
             A("SensorManager.SENSOR_DELAY_GAME",
               "https://developer.android.com/reference/android/hardware/SensorManager#SENSOR_DELAY_GAME"),
             I("deviceMotionUpdateInterval",
               "https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616114-devicemotionupdateinterval", "property"),
             H("interval",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.access.batching", "批处理与 FIFO", "Sensor Batching",
         "批量递送传感器事件以降低唤醒。",
         ["maxReportLatencyUs、batch"],
         ["sensors.access.sampling"],
         merge_bindings(
             A("SensorManager.registerListener latency",
               "https://developer.android.com/reference/android/hardware/SensorManager#registerListener(android.hardware.SensorEventListener,%20android.hardware.Sensor,%20int,%20int)"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("sensors.access.dynamic", "动态传感器", "Dynamic Sensors",
         "连接/断开动态（外接）传感器设备。",
         ["DynamicSensorCallback"],
         ["sensors.access.list"],
         merge_bindings(
             A("SensorManager.DynamicSensorCallback",
               "https://developer.android.com/reference/android/hardware/SensorManager.DynamicSensorCallback"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("sensors.access.permission", "传感器权限", "Sensor Permission",
         "运动与身体传感器等运行时权限。",
         ["ACTIVITY_RECOGNITION、Motion usage"],
         ["sensors.access.subscribe"],
         merge_bindings(
             A("ACTIVITY_RECOGNITION",
               "https://developer.android.com/guide/topics/sensors/sensors_motion"),
             I("NSMotionUsageDescription",
               "https://developer.apple.com/documentation/bundleresources/information_property_list/nsmotionusagedescription", "guide"),
             H("ohos.permission.ACCELEROMETER",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sensor-guidelines", "guide"),
         ), "runtime_permission"),
        ("sensors.access.wake_up", "唤醒型传感器", "Wake-up Sensor",
         "可唤醒应用处理器的传感器模式。",
         ["isWakeUpSensor"],
         ["sensors.access.subscribe"],
         merge_bindings(
             A("Sensor.isWakeUpSensor",
               "https://developer.android.com/reference/android/hardware/Sensor#isWakeUpSensor()"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("sensors.access.direct_channel", "直接通道", "Sensor Direct Channel",
         "将传感器数据写入共享内存直接通道。",
         ["SensorDirectChannel"],
         ["sensors.access.subscribe"],
         merge_bindings(
             A("SensorDirectChannel",
               "https://developer.android.com/reference/android/hardware/SensorDirectChannel"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("sensors.access.one_shot", "单次触发传感器", "One-shot Sensor",
         "触发即完成的传感器请求模式。",
         ["requestTriggerSensor"],
         ["sensors.access.subscribe"],
         merge_bindings(
             A("SensorManager.requestTriggerSensor",
               "https://developer.android.com/reference/android/hardware/SensorManager#requestTriggerSensor(android.hardware.TriggerEventListener,%20android.hardware.Sensor)"),
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
            fid, "sensors.access", "access_capability",
            zh, en, definition, includes, excludes, bindings, privacy=privacy,
        ))

    # haptics (vibration under sensors, not device)
    for row in [
        ("sensors.haptics.vibrate", "基础振动", "Basic Vibration",
         "按时长或基础模式触发振动。",
         ["Vibrator.vibrate、AudioServicesPlaySystemSound"],
         ["sensors.haptics.effects"],
         merge_bindings(
             A("Vibrator",
               "https://developer.android.com/reference/android/os/Vibrator"),
             I("AudioServicesPlaySystemSound",
               "https://developer.apple.com/documentation/audiotoolbox/1405202-audioservicesplaysystemsound", "function"),
             H("@ohos.vibrator",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vibrator"),
         )),
        ("sensors.haptics.effects", "预设振动效果", "Predefined Haptic Effects",
         "使用系统预设触感/振动效果。",
         ["VibrationEffect.createPredefined、UIImpactFeedbackGenerator"],
         ["sensors.haptics.vibrate"],
         merge_bindings(
             A("VibrationEffect",
               "https://developer.android.com/reference/android/os/VibrationEffect"),
             I("UIImpactFeedbackGenerator",
               "https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator", "class"),
             H("vibrator effect",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vibrator"),
         )),
        ("sensors.haptics.pattern", "自定义振动波形", "Custom Vibration Pattern",
         "自定义振幅/时序振动波形。",
         ["createWaveform、CHHapticPattern"],
         ["sensors.haptics.effects"],
         merge_bindings(
             A("VibrationEffect.createWaveform",
               "https://developer.android.com/reference/android/os/VibrationEffect#createWaveform(long[],%20int)"),
             I("CHHapticPattern",
               "https://developer.apple.com/documentation/corehaptics/chhapticpattern", "class"),
             H("VibrateEffect",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vibrator"),
         )),
        ("sensors.haptics.engine", "高级触感引擎", "Advanced Haptics Engine",
         "可编程触感引擎与玩家/图案播放。",
         ["Core Haptics、VibratorManager"],
         ["sensors.haptics.pattern"],
         merge_bindings(
             A("VibratorManager",
               "https://developer.android.com/reference/android/os/VibratorManager"),
             I("Core Haptics",
               "https://developer.apple.com/documentation/corehaptics", "framework"),
             H("@ohos.vibrator",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vibrator"),
         )),
        ("sensors.haptics.ui_feedback", "控件触感反馈", "UI Haptic Feedback",
         "与 UI 控件交互绑定的轻触反馈。",
         ["performHapticFeedback、UIFeedbackGenerator"],
         ["sensors.haptics.effects"],
         merge_bindings(
             A("View.performHapticFeedback",
               "https://developer.android.com/reference/android/view/View#performHapticFeedback(int)"),
             I("UINotificationFeedbackGenerator",
               "https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator", "class"),
             pending("harmonyos"),
         )),
        ("sensors.haptics.capability", "触感能力查询", "Haptics Capability",
         "查询设备是否支持振幅控制等触感能力。",
         ["hasAmplitudeControl、supportsHaptics"],
         ["sensors.haptics.vibrate"],
         merge_bindings(
             A("Vibrator.hasAmplitudeControl",
               "https://developer.android.com/reference/android/os/Vibrator#hasAmplitudeControl()"),
             I("CHHapticDeviceCapability",
               "https://developer.apple.com/documentation/corehaptics/chhapticdevicecapability", "protocol"),
             H("isSupportEffect",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vibrator"),
         )),
        ("sensors.haptics.cancel", "停止振动", "Cancel Vibration",
         "取消正在进行的振动。",
         ["cancel"],
         ["sensors.haptics.vibrate"],
         merge_bindings(
             A("Vibrator.cancel",
               "https://developer.android.com/reference/android/os/Vibrator#cancel()"),
             I("CHHapticEngine stop",
               "https://developer.apple.com/documentation/corehaptics/chhapticengine", "class"),
             H("stopVibration",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vibrator"),
         )),
        ("sensors.haptics.audio_coupled", "音振协同", "Audio-Haptic Sync",
         "音频与触感同步播放。",
         ["HapticGenerator、CHHapticAdvancedPatternPlayer"],
         ["sensors.haptics.engine"],
         merge_bindings(
             A("HapticGenerator",
               "https://developer.android.com/reference/android/media/audiofx/HapticGenerator"),
             I("CHHapticAdvancedPatternPlayer",
               "https://developer.apple.com/documentation/corehaptics/chhapticadvancedpatternplayer", "protocol"),
             pending("harmonyos"),
         )),
    ]:
        fid, zh, en, definition, includes, excludes, bindings = row
        f.append(atom(
            fid, "sensors.haptics", "haptics_capability",
            zh, en, definition, includes, excludes, bindings,
        ))

    # fusion
    for row in [
        ("sensors.fusion.activity", "活动识别", "Activity Recognition",
         "识别步行/跑步/驾车等身体活动类型。",
         ["ActivityRecognitionClient、CMMotionActivityManager"],
         ["sensors.motion.pedometer"],
         merge_bindings(
             A("ActivityRecognitionClient",
               "https://developers.google.com/android/reference/com/google/android/gms/location/ActivityRecognitionClient"),
             I("CMMotionActivityManager",
               "https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager", "class"),
             pending("harmonyos"),
         ), "sensitive"),
        ("sensors.fusion.stationary", "静止检测", "Stationary Detect",
         "判断设备是否处于静止状态。",
         ["TYPE_STATIONARY_DETECT"],
         ["sensors.fusion.activity"],
         merge_bindings(
             A("Sensor.TYPE_STATIONARY_DETECT",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_STATIONARY_DETECT"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("sensors.fusion.motion_detect", "运动检测", "Motion Detect",
         "判断设备是否处于运动状态。",
         ["TYPE_MOTION_DETECT"],
         ["sensors.fusion.stationary"],
         merge_bindings(
             A("Sensor.TYPE_MOTION_DETECT",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_MOTION_DETECT"),
             pending("ios"),
             pending("harmonyos"),
         )),
        ("sensors.fusion.device_posture", "设备姿态形态", "Device Posture Fusion",
         "折叠/展平/握持等设备形态融合状态。",
         ["FoldState、UIDevice orientation 综合"],
         ["sensors.motion.attitude"],
         merge_bindings(
             A("WindowInfoTracker / FoldingFeature",
               "https://developer.android.com/guide/topics/large-screens/learn-about-foldables"),
             I("UIDevice.orientation",
               "https://developer.apple.com/documentation/uikit/uidevice/1620053-orientation", "property"),
             H("display.getFoldDisplayMode",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display"),
         )),
        ("sensors.fusion.grip", "握持手感知", "Grip / Handedness",
         "感知用户握持手或操作手。",
         ["握持检测 API"],
         ["sensors.fusion.device_posture"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("握持手",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         )),
        ("sensors.fusion.headline", "抬头/朝向场景", "Device Raise / Glance",
         "抬腕/抬头查看等融合手势场景。",
         ["CMMotionActivity / 抬腕"],
         ["sensors.fusion.activity"],
         merge_bindings(
             pending("android"),
             I("CMMotionManager",
               "https://developer.apple.com/documentation/coremotion/cmmotionmanager", "class"),
             pending("harmonyos"),
         )),
        ("sensors.fusion.restricted_research", "受限研究传感器读取", "Restricted Research Sensors",
         "系统研究级传感器套件的受限读取入口。",
         ["SensorKit"],
         ["sensors.access.subscribe"],
         merge_bindings(
             pending("android"),
             I("SensorKit",
               "https://developer.apple.com/documentation/sensorkit", "framework"),
             pending("harmonyos"),
         ), "sensitive"),
        ("sensors.fusion.rotation_matrix", "旋转矩阵合成", "Rotation Matrix Fusion",
         "由加速度与磁场合成旋转矩阵/方向。",
         ["getRotationMatrix"],
         ["sensors.motion.attitude"],
         merge_bindings(
             A("SensorManager.getRotationMatrix",
               "https://developer.android.com/reference/android/hardware/SensorManager#getRotationMatrix(float[],%20float[],%20float[],%20float[])"),
             I("CMAttitude.rotationMatrix",
               "https://developer.apple.com/documentation/coremotion/cmattitude/1616096-rotationmatrix", "property"),
             pending("harmonyos"),
         )),
    ]:
        if len(row) == 7:
            fid, zh, en, definition, includes, excludes, bindings = row
            privacy = "none"
        else:
            fid, zh, en, definition, includes, excludes, bindings, privacy = row
        f.append(atom(
            fid, "sensors.fusion", "fusion_capability",
            zh, en, definition, includes, excludes, bindings, privacy=privacy,
        ))

    for row in [
        ("sensors.motion.accelerometer_only", "加速度计", "Accelerometer",
         "单独读取加速度计三轴数据。",
         ["TYPE_ACCELEROMETER、startAccelerometerUpdates"],
         ["sensors.motion.accel_gyro"],
         merge_bindings(
             A("Sensor.TYPE_ACCELEROMETER",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_ACCELEROMETER"),
             I("startAccelerometerUpdates",
               "https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616135-startaccelerometerupdates", "method"),
             H("sensor.accelerometer",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         ), "sensors.motion", "motion_sensor_type"),
        ("sensors.motion.gyroscope_only", "陀螺仪", "Gyroscope",
         "单独读取陀螺仪角速度。",
         ["TYPE_GYROSCOPE、startGyroUpdates"],
         ["sensors.motion.accel_gyro"],
         merge_bindings(
             A("Sensor.TYPE_GYROSCOPE",
               "https://developer.android.com/reference/android/hardware/Sensor#TYPE_GYROSCOPE"),
             I("startGyroUpdates",
               "https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616119-startgyroupdates", "method"),
             H("GYROSCOPE",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         ), "sensors.motion", "motion_sensor_type"),
        ("sensors.access.max_rate", "最大采样率查询", "Max Sampling Rate",
         "查询传感器支持的最快采样周期。",
         ["getMinDelay"],
         ["sensors.access.sampling"],
         merge_bindings(
             A("Sensor.getMinDelay",
               "https://developer.android.com/reference/android/hardware/Sensor#getMinDelay()"),
             pending("ios"),
             pending("harmonyos"),
         ), "sensors.access", "access_capability"),
        ("sensors.access.reporting_mode", "上报模式", "Reporting Mode",
         "查询连续/变化触发/单次等上报模式。",
         ["getReportingMode"],
         ["sensors.access.subscribe"],
         merge_bindings(
             A("Sensor.getReportingMode",
               "https://developer.android.com/reference/android/hardware/Sensor#getReportingMode()"),
             pending("ios"),
             pending("harmonyos"),
         ), "sensors.access", "access_capability"),
        ("sensors.haptics.intensity", "触感强度", "Haptic Intensity",
         "调节触感/振动强度参数。",
         ["amplitude、UIImpactFeedbackGenerator intensity"],
         ["sensors.haptics.effects"],
         merge_bindings(
             A("VibrationEffect.createOneShot",
               "https://developer.android.com/reference/android/os/VibrationEffect#createOneShot(long,%20int)"),
             I("UIImpactFeedbackGenerator.FeedbackStyle",
               "https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator/feedbackstyle", "enum"),
             H("vibrator intensity",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vibrator"),
         ), "sensors.haptics", "haptics_capability"),
        ("sensors.haptics.primitive", "触感基元组合", "Haptic Primitives",
         "使用系统触感基元组合复杂效果。",
         ["CompositionBuilder、CHHapticEvent"],
         ["sensors.haptics.pattern"],
         merge_bindings(
             A("VibrationEffect.Composition",
               "https://developer.android.com/reference/android/os/VibrationEffect.Composition"),
             I("CHHapticEvent",
               "https://developer.apple.com/documentation/corehaptics/chhapticevent", "class"),
             pending("harmonyos"),
         ), "sensors.haptics", "haptics_capability"),
        ("sensors.fusion.tilt_detect", "倾倒检测", "Tilt Detect",
         "检测设备倾倒/大幅姿态变化事件。",
         ["倾倒/翻转检测"],
         ["sensors.fusion.stationary"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("倾斜检测",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         ), "sensors.fusion", "fusion_capability"),
        ("sensors.fusion.flip", "翻转手势感知", "Flip Gesture",
         "检测设备翻转静音等融合手势。",
         ["翻转手势"],
         ["sensors.fusion.activity"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("翻转",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         ), "sensors.fusion", "fusion_capability"),
        ("sensors.environment.color_temperature", "相关色温", "Color Temperature",
         "读取环境光相关色温（若支持）。",
         ["色温传感器"],
         ["sensors.environment.ambient"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("COLOR_TEMPERATURE",
               "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor"),
         ), "sensors.environment", "environment_sensor_type"),
        ("sensors.access.flush", "刷新传感器事件", "Flush Sensor Events",
         "刷新批处理队列中的挂起传感器事件。",
         ["flush"],
         ["sensors.access.batching"],
         merge_bindings(
             A("SensorManager.flush",
               "https://developer.android.com/reference/android/hardware/SensorManager#flush(android.hardware.SensorEventListener)"),
             pending("ios"),
             pending("harmonyos"),
         ), "sensors.access", "access_capability"),
    ]:
        fid, zh, en, definition, includes, excludes, bindings, parent, axis = row
        f.append(atom(
            fid, parent, axis, zh, en, definition, includes, excludes, bindings,
        ))

    return list({n["id"]: n for n in f}.values())


def main():
    nodes = build()
    path = write_domain("sensors", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
