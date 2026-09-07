#!/usr/bin/env python3
"""Author the health_home domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "health_home_capability_family"


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
        "health_home", parent=None, level="L1",
        zh="健康运动家居车", en="Health Fitness Home Auto",
        definition="健康数据存取、运动锻炼会话、智能家居配件与车载投屏扩展。",
        includes=['健康数据、运动、家居、车载'],
        excludes=['数字健康屏幕时间见 digital_wellbeing', '穿戴消息链路见 distributed.wear_link'],
        legacy={'disposition': 'kept', 'sources': ['health_home']},
    ))
    l2 = [
        ('health_home.health_data', '健康数据', 'Health Data', '健康样本读写、授权、统计与临床记录。', ['授权、样本、统计、记录'], ['运动会话编排见 workout'], {'disposition': 'renamed_from', 'sources': ['health_home.health']}),
        ('health_home.workout', '运动锻炼', 'Workout and Fitness', '锻炼会话、路线与穿戴运动服务。', ['会话、路线、穿戴运动'], ['健康样本存取见 health_data'], []),
        ('health_home.home', '智能家居', 'Smart Home', '家居配件发现、配网、控制与状态。', ['配件、配网、控制'], ['通用蓝牙见 connectivity'], ['health_home.home']),
        ('health_home.auto', '车载扩展', 'Automotive Extension', '车机投屏、导航流转与车载应用模板。', ['投屏、导航流转、车载媒体'], ['通用投屏协议细节见 media/graphics'], ['health_home.auto']),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="health_home", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- health_home.health_data ---
    leaf(f, "health_home.health_data.auth", "health_home.health_data", "health_data_operation", "健康数据授权", "Health Data Authorization",
         "请求并管理健康数据读写授权。", ['requestAuthorization'], ['样本读写见 store'],
         B(('Health Connect', 'https://developer.android.com/health-and-fitness/guides/health-connect', 'guide'), ('HKHealthStore.requestAuthorization', 'https://developer.apple.com/documentation/healthkit/hkhealthstore', 'class'), ('healthStore', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-healthstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.health_data.store", "health_home.health_data", "health_data_operation", "健康样本存取", "Health Sample Store",
         "写入与查询健康样本数据。", ['save/query samples'], ['授权见 auth'],
         B(('Health Connect', 'https://developer.android.com/health-and-fitness/guides/health-connect', 'guide'), ('HKHealthStore', 'https://developer.apple.com/documentation/healthkit/hkhealthstore', 'class'), ('healthStore', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-healthstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.health_data.observer", "health_home.health_data", "health_data_operation", "健康数据变化订阅", "Health Data Observer",
         "订阅健康数据变更事件。", ['observerQuery'], ['存取见 store'],
         B(('Health Connect changes', 'https://developer.android.com/health-and-fitness/guides/health-connect', 'guide'), ('HKObserverQuery', 'https://developer.apple.com/documentation/healthkit/hkobserverquery', 'class'), ('healthStore', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-healthstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "health_home.health_data.stats", "health_home.health_data", "health_data_operation", "健康数据聚合统计", "Health Data Statistics",
         "按时间窗聚合步数、热量等统计。", ['statistics query'], ['原始样本见 store'],
         B(('Aggregate API', 'https://developer.android.com/health-and-fitness/guides/health-connect', 'guide'), ('HKStatisticsQuery', 'https://developer.apple.com/documentation/healthkit/hkstatisticsquery', 'class'), ('healthStore', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-healthstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "health_home.health_data.realtime", "health_home.health_data", "health_data_operation", "实时健康读数", "Realtime Health Reading",
         "读取心率等实时最新读数。", ['realtime HR'], ['历史样本见 store'],
         B(('Health Services', 'https://developer.android.com/health-and-fitness/guides/health-services', 'guide'), ('HKAnchoredObjectQuery', 'https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery', 'class'), ('healthStore', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-healthstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.health_data.records", "health_home.health_data", "health_data_operation", "临床健康记录", "Clinical Health Records",
         "访问病历等临床健康记录。", ['clinical records'], ['日常样本见 store'],
         B(None, ('HKClinicalRecord', 'https://developer.apple.com/documentation/healthkit/hkclinicalrecord', 'class'), None), {'disposition': 'kept', 'sources': ['health_home.health.records']}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.health_data.types_vitals", "health_home.health_data", "health_data_operation", "生命体征类型", "Vitals Data Types",
         "心率、血压、血氧、体温等生命体征类型读写。", ['HR/BP/SpO2/temp'], ['运动度量见 types_activity'],
         B(('Health Connect vitals', 'https://developer.android.com/health-and-fitness/guides/health-connect', 'guide'), ('HKQuantityType', 'https://developer.apple.com/documentation/healthkit/hkquantitytype', 'class'), ('healthStore', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-healthstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.health_data.types_activity", "health_home.health_data", "health_data_operation", "日常活动度量类型", "Activity Metrics Types",
         "步数、距离、活动能量等日常度量。", ['steps/distance/energy'], ['锻炼会话见 workout'],
         B(('Health Connect activity', 'https://developer.android.com/health-and-fitness/guides/health-connect', 'guide'), ('HKQuantityTypeIdentifier.stepCount', 'https://developer.apple.com/documentation/healthkit', 'framework'), ('healthStore', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-healthstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.health_data.types_sleep", "health_home.health_data", "health_data_operation", "睡眠与周期类型", "Sleep and Cycle Types",
         "睡眠分析与生理周期相关类型。", ['sleep / menstrual'], ['生命体征见 types_vitals'],
         B(('Health Connect sleep', 'https://developer.android.com/health-and-fitness/guides/health-connect', 'guide'), ('HKCategoryTypeIdentifier.sleepAnalysis', 'https://developer.apple.com/documentation/healthkit', 'framework'), ('healthStore', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-healthstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.health_data.types_nutrition", "health_home.health_data", "health_data_operation", "营养与体重类型", "Nutrition and Body Types",
         "营养摄入、体重与体成分类型。", ['nutrition/weight'], ['活动度量见 types_activity'],
         B(('Health Connect nutrition', 'https://developer.android.com/health-and-fitness/guides/health-connect', 'guide'), ('HKQuantityTypeIdentifier.bodyMass', 'https://developer.apple.com/documentation/healthkit', 'framework'), ('healthStore', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-healthstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.health_data.ui", "health_home.health_data", "health_data_operation", "健康数据系统界面", "Health Data System UI",
         "跳转系统健康授权或数据界面。", ['health settings UI'], ['授权 API 见 auth'],
         B(('Health Connect UI', 'https://developer.android.com/health-and-fitness/guides/health-connect', 'guide'), ('Health app', 'https://developer.apple.com/documentation/healthkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "health_home.health_data.wear_access", "health_home.health_data", "health_data_operation", "穿戴健康数据访问", "Wear Health Data Access",
         "从穿戴侧读写健康数据入口。", ['wear health access'], ['穿戴消息见 distributed.wear_link'],
         B(('Health Services Wear', 'https://developer.android.com/health-and-fitness/guides/health-services', 'guide'), ('HealthKit', 'https://developer.apple.com/documentation/healthkit', 'framework'), ('healthStore', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-healthstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")

    # --- health_home.workout ---
    leaf(f, "health_home.workout.session", "health_home.workout", "workout_operation", "锻炼会话", "Workout Session",
         "开始、暂停与结束锻炼会话并记录指标。", ['HKWorkoutSession / ExerciseSession'], ['样本存档见 health_data.store'],
         B(('ExerciseSession', 'https://developer.android.com/health-and-fitness/guides/health-connect/develop/write-exercise-records', 'guide'), ('HKWorkoutSession', 'https://developer.apple.com/documentation/healthkit/hkworkoutsession', 'class'), ('healthStore workout', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-healthstore')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.workout.route", "health_home.workout", "workout_operation", "运动轨迹路线", "Workout Route",
         "记录与查询运动 GPS 轨迹。", ['workout route'], ['定位见 location'],
         B(('ExerciseRoute', 'https://developer.android.com/health-and-fitness/guides/health-connect', 'guide'), ('HKWorkoutRoute', 'https://developer.apple.com/documentation/healthkit/hkworkoutroute', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.workout.live_metrics", "health_home.workout", "workout_operation", "运动实时指标", "Live Workout Metrics",
         "会话中订阅心率、配速等实时指标。", ['live metrics'], ['会话控制见 session'],
         B(('Health Services', 'https://developer.android.com/health-and-fitness/guides/health-services', 'guide'), ('HKLiveWorkoutBuilder', 'https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilder', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.workout.wear_services", "health_home.workout", "workout_operation", "穿戴运动服务", "Wear Fitness Services",
         "穿戴侧运动跟踪与目标服务。", ['wear workout services'], ['会话见 session'],
         B(('Health Services', 'https://developer.android.com/health-and-fitness/guides/health-services', 'guide'), ('WorkoutKit', 'https://developer.apple.com/documentation/workoutkit', 'framework'), ('wearEngine', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wearengine')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "health_home.workout.goals", "health_home.workout", "workout_operation", "运动目标与计划", "Fitness Goals and Plans",
         "设置活动环/目标与训练计划。", ['activity rings / goals'], ['会话见 session'],
         B(None, ('HKActivitySummary', 'https://developer.apple.com/documentation/healthkit/hkactivitysummary', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "health_home.workout.builder", "health_home.workout", "workout_operation", "锻炼记录构建", "Workout Record Builder",
         "构建并保存完整锻炼记录元数据。", ['workout builder'], ['会话见 session'],
         B(('ExerciseSessionRecord', 'https://developer.android.com/health-and-fitness/guides/health-connect', 'guide'), ('HKWorkoutBuilder', 'https://developer.apple.com/documentation/healthkit/hkworkoutbuilder', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- health_home.home ---
    leaf(f, "health_home.home.accessories", "health_home.home", "home_operation", "家居配件发现", "Home Accessory Discovery",
         "发现并列出智能家居配件。", ['HMHome / Matter'], ['控制见 control'],
         B(('Home Graph / Matter', 'https://developer.android.com/guide/topics/connectivity/matter', 'guide'), ('HomeKit', 'https://developer.apple.com/documentation/homekit', 'framework'), ('homeDevice', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/connectivity-kit-intro')), {'disposition': 'kept', 'sources': ['health_home.home.accessories']}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.home.commissioning", "health_home.home", "home_operation", "配件配网入网", "Accessory Commissioning",
         "将配件配网并加入家庭网络。", ['commissioning'], ['发现见 accessories'],
         B(('Matter commissioning', 'https://developer.android.com/guide/topics/connectivity/matter', 'guide'), ('HMAccessoryBrowser', 'https://developer.apple.com/documentation/homekit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.home.control", "health_home.home", "home_operation", "家居设备控制", "Home Device Control",
         "读写配件特性并执行控制指令。", ['characteristic write'], ['发现见 accessories'],
         B(('Device controls', 'https://developer.android.com/guide/topics/connectivity/device-controls', 'guide'), ('HMCharacteristic', 'https://developer.apple.com/documentation/homekit/hmcharacteristic', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.home.scenes", "health_home.home", "home_operation", "家庭场景自动化", "Home Scenes Automation",
         "定义并触发家庭场景与自动化。", ['scenes / automations'], ['单设备控制见 control'],
         B(None, ('HMActionSet', 'https://developer.apple.com/documentation/homekit/hmactionset', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "health_home.home.device_controls", "health_home.home", "home_operation", "系统设备控制中心", "System Device Controls",
         "向系统控制中心贡献设备磁贴。", ['ControlsProviderService'], ['应用内控制见 control'],
         B(('ControlsProviderService', 'https://developer.android.com/guide/topics/connectivity/device-controls', 'guide'), ('Control Center', 'https://developer.apple.com/documentation/homekit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "health_home.home.structure", "health_home.home", "home_operation", "家庭与房间结构", "Home Structure",
         "管理家庭、房间与分区结构。", ['homes/rooms'], ['配件见 accessories'],
         B(None, ('HMHome', 'https://developer.apple.com/documentation/homekit/hmhome', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- health_home.auto ---
    leaf(f, "health_home.auto.projection", "health_home.auto", "auto_operation", "车机投屏连接", "Car Projection Connection",
         "建立手机与车机投屏/桌面连接。", ['Android Auto / CarPlay / HiCar'], ['导航流转见 navi_transfer'],
         B(('Android for Cars', 'https://developer.android.com/training/cars', 'guide'), ('CarPlay', 'https://developer.apple.com/carplay/', 'guide'), ('Phone Cast / HiCar', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-guide')), {'disposition': 'kept', 'sources': ['health_home.auto.projection']}, level="L3", privacy="none")
    leaf(f, "health_home.auto.navi_transfer", "health_home.auto", "auto_operation", "导航流转上车", "Navigation Transfer to Car",
         "将导航任务流转到车机继续。", ['navi transfer'], ['投屏连接见 projection'],
         B(('Car App Library Nav', 'https://developer.android.com/training/cars/navigation', 'guide'), ('CarPlay Navigation', 'https://developer.apple.com/carplay/', 'guide'), ('navi transfer', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "health_home.auto.address_transfer", "health_home.auto", "auto_operation", "地址流转下车", "Address Transfer from Car",
         "将车机地址流转回手机步行导航。", ['address transfer'], ['导航上车见 navi_transfer'],
         B(None, None, ('address transfer', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "health_home.auto.media", "health_home.auto", "auto_operation", "车载媒体应用", "Automotive Media App",
         "在车载模板中提供媒体浏览与播控。", ['media template'], ['本机播控见 media.session'],
         B(('Car media apps', 'https://developer.android.com/training/cars/media', 'guide'), ('CarPlay Audio', 'https://developer.apple.com/carplay/', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "health_home.auto.app_templates", "health_home.auto", "auto_operation", "车载应用模板", "Automotive App Templates",
         "使用车载应用模板构建列表/地图等界面。", ['car app templates'], ['投屏见 projection'],
         B(('Car App Library', 'https://developer.android.com/training/cars', 'guide'), ('CarPlay templates', 'https://developer.apple.com/carplay/', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "health_home.auto.hardware", "health_home.auto", "auto_operation", "车载硬件信号", "Automotive Hardware Signals",
         "读取车速、档位等车载硬件信号（受权限约束）。", ['car hardware'], ['投屏见 projection'],
         B(('CarPropertyManager', 'https://developer.android.com/reference/android/car/hardware/property/CarPropertyManager'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "health_home.auto.connection_state", "health_home.auto", "auto_operation", "车机连接状态", "Car Connection State",
         "监听车机连接与会话状态。", ['connection state'], ['投屏见 projection'],
         B(('CarConnection', 'https://developer.android.com/training/cars', 'guide'), ('CarPlay', 'https://developer.apple.com/carplay/', 'guide'), ('HiCar status', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")


    leaf(f, "health_home.health_data.types_hearing", "health_home.health_data", "health_data_operation", "听力健康类型", "Hearing Health Types",
         "听力暴露与听力图等相关健康类型。", ["hearing types"], ["生命体征见 types_vitals"],
         B(("Health Connect hearing", "https://developer.android.com/health-and-fitness/guides/health-connect", "guide"),
           ("HKAudiogramSample", "https://developer.apple.com/documentation/healthkit", "framework"), None), privacy="runtime_permission")
    leaf(f, "health_home.health_data.types_lab", "health_home.health_data", "health_data_operation", "实验室指标类型", "Lab Result Types",
         "血糖等实验室/检验类指标类型。", ["blood glucose / lab"], ["临床记录见 records"],
         B(("BloodGlucoseRecord", "https://developer.android.com/health-and-fitness/guides/health-connect", "guide"),
           ("HKQuantityTypeIdentifier.bloodGlucose", "https://developer.apple.com/documentation/healthkit", "framework"),
           ("healthStore", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-healthstore")), privacy="runtime_permission")
    leaf(f, "health_home.health_data.delete", "health_home.health_data", "health_data_operation", "健康数据删除", "Health Data Delete",
         "按条件删除应用写入的健康样本。", ["delete records"], ["存取见 store"],
         B(("Health Connect delete", "https://developer.android.com/health-and-fitness/guides/health-connect", "guide"),
           ("HKHealthStore.delete", "https://developer.apple.com/documentation/healthkit/hkhealthstore", "class"), None), privacy="runtime_permission")
    leaf(f, "health_home.workout.indoor", "health_home.workout", "workout_operation", "室内运动模式", "Indoor Workout Mode",
         "标记或适配室内运动会话模式。", ["indoor workout"], ["会话见 session"],
         B(("ExerciseSessionRecord", "https://developer.android.com/health-and-fitness/guides/health-connect", "guide"),
           ("HKWorkoutActivityType", "https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype", "enum"), None))
    leaf(f, "health_home.workout.segments", "health_home.workout", "workout_operation", "运动分段", "Workout Segments",
         "记录间歇/分段运动结构。", ["workout segments"], ["会话见 session"],
         B(None, ("HKWorkoutEvent", "https://developer.apple.com/documentation/healthkit/hkworkoutevent", "class"), None))
    leaf(f, "health_home.home.rooms_zones", "health_home.home", "home_operation", "房间与分区", "Rooms and Zones",
         "管理房间与分区以组织配件。", ["rooms/zones"], ["家庭结构见 structure"],
         B(None, ("HMRoom", "https://developer.apple.com/documentation/homekit/hmroom", "class"), None))
    leaf(f, "health_home.home.matter_fabric", "health_home.home", "home_operation", "Matter织物管理", "Matter Fabric Management",
         "管理 Matter 织物与多管理器共享。", ["Matter fabric"], ["配网见 commissioning"],
         B(("Matter", "https://developer.android.com/guide/topics/connectivity/matter", "guide"),
           ("MatterSupport", "https://developer.apple.com/documentation/mattersupport", "framework"), None), privacy="runtime_permission")
    leaf(f, "health_home.auto.poi_search", "health_home.auto", "auto_operation", "车载兴趣点搜索", "Automotive POI Search",
         "在车载模板中提供兴趣点搜索。", ["POI template"], ["应用模板见 app_templates"],
         B(("Car App Library Place", "https://developer.android.com/training/cars", "guide"),
           ("CarPlay", "https://developer.apple.com/carplay/", "guide"), None))
    leaf(f, "health_home.auto.voice_assist", "health_home.auto", "auto_operation", "车载语音助手接入", "Automotive Voice Assist",
         "车载场景下接入语音助手意图。", ["car voice assist"], ["系统意图见 ai.intents"],
         B(("Car App voice", "https://developer.android.com/training/cars", "guide"),
           ("CarPlay / Siri", "https://developer.apple.com/carplay/", "guide"), None))

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("health_home", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
