#!/usr/bin/env python3
"""Author the app domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "app_runtime_concern"


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
        "app", parent=None, level="L1",
        zh="应用模型", en="Application Model",
        definition="应用组件模型、生命周期、进程、后台执行、启动、桌面呈现、安装更新与系统扩展点。",
        includes=["model、lifecycle、process、background、launch、desktop、install、extensions"],
        excludes=["ui 窗口与控件", "runtime 语言/包管理底层", "enterprise 设备策略"],
        legacy={"disposition": "kept", "sources": ["app"]},
    ))

    l2 = [
        ("app.model", "应用组件模型", "App Component Model",
         "应用入口、上下文、界面组件与后台服务组件模型。",
         ["app_entry、context、ui_entry、service_component"],
         ["生命周期回调细节见 app.lifecycle"],
         []),
        ("app.lifecycle", "组件生命周期", "Component Lifecycle",
         "界面组件生命周期、进程死亡恢复与退出。",
         ["activity_ability、callbacks、process_death、recovery、app_exit"],
         ["进程优先级见 app.process", "后台任务见 app.background"],
         ["app.lifecycle"]),
        ("app.process", "进程与隔离", "Process and Isolation",
         "多进程模型、优先级、隔离与 IPC。",
         ["model、priority、isolation、ipc"],
         ["组件生命周期见 app.lifecycle"],
         ["app.lifecycle.process"]),
        ("app.background", "后台执行", "Background Execution",
         "前台长时任务、延迟条件任务与短暂延缓挂起。",
         ["foreground_task、deferred_work、transient"],
         ["播放后台续播见 media.playback", "推送见 notifications"],
         ["app.background"]),
        ("app.launch", "启动与初始化", "Launch and Startup",
         "启动初始化、启动窗与启动加速。",
         ["startup_init、splash、acceleration"],
         ["安装见 app.install"],
         []),
        ("app.desktop", "桌面呈现", "Desktop Presence",
         "桌面小组件、快捷方式与动态图标。",
         ["widget、shortcuts、dynamic_icon"],
         ["壳层状态栏条目见 ui.system_integration"],
         ["app.desktop"]),
        ("app.install", "安装与更新", "Install and Update",
         "包安装更新、应用内更新、即用安装、按需模块与包查询。",
         ["package_update、inapp_update、instant、on_demand、query"],
         ["签名安全见 security"],
         ["app.install"]),
        ("app.extensions", "系统扩展点", "System Extensions",
         "分享、照片编辑、UI 嵌入、驱动与智能体等扩展能力。",
         ["share、photo_editor、ui_embed、driver、agent"],
         ["桌面小组件见 app.desktop.widget"],
         ["app.extensions"]),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        disp = "kept" if sources and sources[0] == fid else ("renamed_from" if sources else "new")
        if fid == "app.process":
            disp = "renamed_from"
        f.append(feature(
            fid, parent="app", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy={"disposition": disp, "sources": sources},
        ))

    # model
    leaf(f, "app.model.app_entry", "app.model", "model_role",
         "应用进程入口", "Application Process Entry",
         "应用进程级入口与全局创建回调。",
         ["Application/AbilityStage、UIApplicationMain"],
         ["界面组件入口见 ui_entry"],
         merge_bindings(
             A("Application", "https://developer.android.com/reference/android/app/Application"),
             I("UIApplicationMain", "https://developer.apple.com/documentation/uikit/uiapplicationmain(_:_:_:_:)", "function"),
             H("AbilityStage", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage"),
         ))
    leaf(f, "app.model.context", "app.model", "model_role",
         "应用与组件上下文", "App and Component Context",
         "获取应用/组件上下文以访问系统服务与资源。",
         ["Context/UIAbilityContext、UIApplication"],
         ["入口组件见 ui_entry"],
         merge_bindings(
             A("Context", "https://developer.android.com/reference/android/content/Context"),
             I("UIApplication", "https://developer.apple.com/documentation/uikit/uiapplication", "class"),
             H("ApplicationContext / UIAbilityContext", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext"),
         ))
    leaf(f, "app.model.ui_entry", "app.model", "model_role",
         "界面入口组件", "UI Entry Component",
         "可作为界面入口被启动的 Activity/UIAbility/Scene。",
         ["Activity/UIAbility exported 入口"],
         ["生命周期回调见 lifecycle.activity_ability"],
         merge_bindings(
             A("Activity", "https://developer.android.com/reference/android/app/Activity"),
             I("UIScene / App lifecycle", "https://developer.apple.com/documentation/uikit/uiscene", "class"),
             H("UIAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability"),
         ))
    leaf(f, "app.model.service_component", "app.model", "model_role",
         "服务组件", "Service Component",
         "无界面后台服务组件的声明与启动模型。",
         ["Service、AppServiceExtensionAbility"],
         ["前台服务长时任务见 background.foreground_task"],
         merge_bindings(
             A("Service", "https://developer.android.com/reference/android/app/Service"),
             pending("ios", "无对等 Service 组件；用后台任务 API"),
             H("AppServiceExtensionAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appserviceextensionability"),
         ))

    # lifecycle
    leaf(f, "app.lifecycle.activity_ability", "app.lifecycle", "lifecycle_aspect",
         "界面组件生命周期", "UI Component Lifecycle",
         "前台界面入口组件的创建、可见、销毁与状态保存回调。",
         ["Activity/UIAbility/UIViewController 生命周期"],
         ["进程回收见 process / process_death"],
         merge_bindings(
             A("Activity lifecycle", "https://developer.android.com/guide/components/activities/activity-lifecycle", "guide"),
             I("UIViewController", "https://developer.apple.com/documentation/uikit/uiviewcontroller", "class"),
             H("UIAbility 生命周期", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-lifecycle"),
         ),
         {"disposition": "kept", "sources": ["app.lifecycle.activity_ability"]})
    leaf(f, "app.lifecycle.callbacks", "app.lifecycle", "lifecycle_aspect",
         "应用级生命周期回调", "App-level Lifecycle Callbacks",
         "进程/应用前后台切换等全局生命周期监听。",
         ["ProcessLifecycleOwner、scene phase、ApplicationStateChange"],
         ["单页面组件见 activity_ability"],
         merge_bindings(
             A("ProcessLifecycleOwner", "https://developer.android.com/reference/androidx/lifecycle/ProcessLifecycleOwner"),
             I("scenePhase", "https://developer.apple.com/documentation/swiftui/scenephase", "enumeration"),
             H("ApplicationStateChangeCallback", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-application"),
         ))
    leaf(f, "app.lifecycle.process_death", "app.lifecycle", "lifecycle_aspect",
         "进程死亡状态保存", "Process Death State Saving",
         "在进程可能被杀死前保存可恢复状态。",
         ["onSaveInstanceState、onSaveState、scene restoration"],
         ["崩溃恢复见 recovery"],
         merge_bindings(
             A("onSaveInstanceState", "https://developer.android.com/guide/components/activities/activity-lifecycle#onSaveInstanceState", "guide"),
             I("UISceneSession state restoration", "https://developer.apple.com/documentation/uikit/uiscenesession", "class"),
             H("UIAbility.onSaveState", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-persist-data"),
         ))
    leaf(f, "app.lifecycle.recovery", "app.lifecycle", "lifecycle_aspect",
         "异常恢复重启", "Abnormal Recovery Restart",
         "应用异常后的状态保存与拉起恢复。",
         ["appRecovery、exception handler restart"],
         ["常规状态保存见 process_death"],
         merge_bindings(
             pending("android", "可用自定义异常处理；无统一 appRecovery API"),
             pending("ios"),
             H("appRecovery", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-apprecovery"),
         ))
    leaf(f, "app.lifecycle.app_exit", "app.lifecycle", "lifecycle_aspect",
         "应用退出与自终止", "App Exit and Self Termination",
         "主动终止自身 Ability/任务或重启应用。",
         ["finishAffinity/terminateSelf/exit"],
         ["系统杀进程见 process.priority"],
         merge_bindings(
             A("Activity.finish", "https://developer.android.com/reference/android/app/Activity#finish()", "method"),
             I("exit(0) / UIApplication", "https://developer.apple.com/documentation/uikit/uiapplication", "class"),
             H("terminateSelf / restartApp", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext"),
         ))

    # process
    leaf(f, "app.process.model", "app.process", "process_aspect",
         "多进程模型", "Multi-process Model",
         "为组件指定独立进程与进程划分模型。",
         ["android:process、module process 字段"],
         ["IPC 通道见 ipc"],
         merge_bindings(
             A("android:process", "https://developer.android.com/guide/components/processes-and-threads", "guide"),
             pending("ios", "App Extensions 另进程；主应用通常单进程"),
             H("process 配置", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/process-model"),
         ),
         {"disposition": "merged_from", "sources": ["app.lifecycle.process"]})
    leaf(f, "app.process.priority", "app.process", "process_aspect",
         "进程优先级", "Process Priority",
         "前后台与服务状态下的进程重要性/优先级。",
         ["oom_adj / importance levels"],
         ["后台任务配额见 background"],
         merge_bindings(
             A("Processes and application life cycle", "https://developer.android.com/guide/components/activities/process-lifecycle", "guide"),
             I("App lifecycle memory", "https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle", "guide"),
             H("进程优先级", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/process-model"),
         ))
    leaf(f, "app.process.isolation", "app.process", "process_aspect",
         "进程与子进程隔离", "Process Isolation",
         "子进程/隔离进程创建与安全边界。",
         ["isolatedProcess、native child process"],
         ["同应用多进程见 model"],
         merge_bindings(
             A("android:isolatedProcess", "https://developer.android.com/guide/topics/manifest/service-element#isolated", "guide"),
             pending("ios"),
             H("Native child process", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess"),
         ))
    leaf(f, "app.process.ipc", "app.process", "process_aspect",
         "进程间通信", "Inter-process Communication",
         "跨进程调用通道与序列化。",
         ["Binder/AIDL、XPC、RPC/MessageSequence"],
         ["组件启动模型见 app.model"],
         merge_bindings(
             A("AIDL", "https://developer.android.com/guide/components/aidl", "guide"),
             I("XPC", "https://developer.apple.com/documentation/xpc", "framework"),
             H("rpc.IRemoteObject", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rpc"),
         ))
    leaf(f, "app.process.ipc.channel", "app.process.ipc", "ipc_detail",
         "IPC通道", "IPC Channel",
         "建立并维护跨进程通信连接与死亡通知。",
         ["IBinder/Messenger、xpc_connection、connectServiceExtensionAbility"],
         ["序列化见 serialization"],
         merge_bindings(
             A("IBinder", "https://developer.android.com/reference/android/os/IBinder"),
             I("xpc_connection_t", "https://developer.apple.com/documentation/xpc/xpc_connection_t", "type"),
             H("connectServiceExtensionAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext"),
         ), level="L4")
    leaf(f, "app.process.ipc.serialization", "app.process.ipc", "ipc_detail",
         "IPC序列化", "IPC Serialization",
         "跨进程传递的数据打包与反序列化。",
         ["Parcel/Parcelable、XPC dictionary、MessageSequence"],
         ["通道建立见 channel"],
         merge_bindings(
             A("Parcel", "https://developer.android.com/reference/android/os/Parcel"),
             I("XPC dictionaries", "https://developer.apple.com/documentation/xpc", "framework"),
             H("MessageSequence", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rpc"),
         ), level="L4")
    for node in f:
        if node["id"] == "app.process.ipc":
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            node["knowledge_path"] = "knowledge/app/process/ipc/_rollup.yaml"

    # background
    leaf(f, "app.background.foreground_task", "app.background", "background_kind",
         "前台长时任务", "Foreground Long-running Task",
         "用户可感知的长时后台执行（前台服务/连续任务）。",
         ["startForeground、BGContinuedProcessingTask、startContinuousTask"],
         ["延迟任务见 deferred_work"],
         merge_bindings(
             A("Foreground services", "https://developer.android.com/develop/background-work/services/foreground-services", "guide"),
             I("BGContinuedProcessingTask", "https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask", "class"),
             H("startContinuousTask", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager"),
         ),
         {"disposition": "kept", "sources": ["app.background.foreground_task"]})
    leaf(f, "app.background.deferred_work", "app.background", "background_kind",
         "延迟与条件任务", "Deferred and Conditional Work",
         "按网络/充电等约束调度的延迟或周期性后台工作。",
         ["WorkManager、BGTaskScheduler、workScheduler"],
         ["前台服务见 foreground_task"],
         merge_bindings(
             A("WorkManager", "https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started", "guide"),
             I("BGTaskScheduler", "https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler", "class"),
             H("workScheduler", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workscheduler"),
         ),
         {"disposition": "kept", "sources": ["app.background.deferred_work"]})
    leaf(f, "app.background.transient", "app.background", "background_kind",
         "短暂延缓挂起", "Transient Suspend Delay",
         "短时间申请延迟进入挂起以完成收尾工作。",
         ["requestSuspendDelay、beginBackgroundTask"],
         ["长时任务见 foreground_task"],
         merge_bindings(
             pending("android", "可用 Wakeful 模式有限替代；无同名 API"),
             I("beginBackgroundTask", "https://developer.apple.com/documentation/uikit/uiapplication/1623031-beginbackgroundtask", "method"),
             H("requestSuspendDelay", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager"),
         ))
    leaf(f, "app.background.foreground_task.types", "app.background.foreground_task", "foreground_detail",
         "前台任务类型声明", "Foreground Task Type Declaration",
         "声明长时任务的系统类型与权限约束。",
         ["foregroundServiceType、continuous task types"],
         ["启动见父节点"],
         merge_bindings(
             A("foregroundServiceType", "https://developer.android.com/develop/background-work/services/foreground-services#types", "guide"),
             pending("ios"),
             H("BackgroundMode", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/continuous-task"),
         ), level="L4")
    leaf(f, "app.background.deferred_work.constraints", "app.background.deferred_work", "deferred_detail",
         "延迟任务约束", "Deferred Work Constraints",
         "网络、电量、空闲等执行约束条件。",
         ["Constraints、BGAppRefresh、WorkInfo constraints"],
         ["调度入口见父节点"],
         merge_bindings(
             A("Constraints.Builder", "https://developer.android.com/reference/androidx/work/Constraints.Builder"),
             I("BGAppRefreshTaskRequest", "https://developer.apple.com/documentation/backgroundtasks/bgapprefreshtaskrequest", "class"),
             H("WorkInfo 约束", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workscheduler"),
         ), level="L4")
    for node in f:
        if node["id"] in {"app.background.foreground_task", "app.background.deferred_work"}:
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            parts = node["id"].split(".")
            node["knowledge_path"] = "knowledge/" + "/".join(parts) + "/_rollup.yaml"

    # launch
    leaf(f, "app.launch.startup_init", "app.launch", "launch_aspect",
         "启动初始化器", "Startup Initializers",
         "进程启动阶段的组件初始化编排。",
         ["App Startup Initializer、startupManager"],
         ["启动窗见 splash"],
         merge_bindings(
             A("App Startup", "https://developer.android.com/topic/libraries/app-startup", "guide"),
             pending("ios"),
             H("startupManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-startupmanager"),
         ))
    leaf(f, "app.launch.splash", "app.launch", "launch_aspect",
         "启动窗与闪屏", "Splash / Starting Window",
         "系统启动窗或首屏占位资源配置。",
         ["SplashScreen API、Launch Screen、Starting Window"],
         ["初始化器见 startup_init"],
         merge_bindings(
             A("SplashScreen", "https://developer.android.com/reference/androidx/core/splashscreen/SplashScreen"),
             I("Launch Screen", "https://developer.apple.com/documentation/uikit/uistoryboard/storyboard_launch_screen", "guide"),
             H("Starting Window", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-window"),
         ))
    leaf(f, "app.launch.acceleration", "app.launch", "launch_aspect",
         "启动加速", "Launch Acceleration",
         "启动剖析配置与系统预加载加速。",
         ["Baseline Profiles、app preload"],
         ["闪屏见 splash"],
         merge_bindings(
             A("Baseline Profiles", "https://developer.android.com/topic/performance/baselineprofiles/overview", "guide"),
             pending("ios"),
             H("应用预加载", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-preload"),
         ))
    leaf(f, "app.launch.acceleration.aot_profile", "app.launch.acceleration", "acceleration_detail",
         "AOT剖析配置", "AOT Profile Installation",
         "安装/使用基线剖析文件加速启动与运行。",
         ["ProfileInstaller / baseline-prof.txt"],
         ["系统预加载见 system_preload"],
         merge_bindings(
             A("ProfileInstaller", "https://developer.android.com/reference/androidx/profileinstaller/ProfileInstaller"),
             pending("ios"),
             pending("harmonyos"),
         ), level="L4")
    leaf(f, "app.launch.acceleration.system_preload", "app.launch.acceleration", "acceleration_detail",
         "系统预加载", "System Preload",
         "系统在启动前预创建进程/阶段以加速冷启动。",
         ["appPreloadPhase / getAppPreloadType"],
         ["AOT 剖析见 aot_profile"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("appPreloadPhase", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-preload"),
         ), level="L4")
    for node in f:
        if node["id"] == "app.launch.acceleration":
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            node["knowledge_path"] = "knowledge/app/launch/acceleration/_rollup.yaml"

    # desktop
    leaf(f, "app.desktop.widget", "app.desktop", "desktop_surface",
         "桌面小组件", "Home Screen Widgets",
         "桌面/负一屏小组件的提供与刷新。",
         ["AppWidget、WidgetKit、FormExtensionAbility"],
         ["快捷方式见 shortcuts"],
         merge_bindings(
             A("AppWidgetProvider", "https://developer.android.com/reference/android/appwidget/AppWidgetProvider"),
             I("WidgetKit", "https://developer.apple.com/documentation/widgetkit", "framework"),
             H("FormExtensionAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability"),
         ),
         {"disposition": "kept", "sources": ["app.desktop.widget"]})
    leaf(f, "app.desktop.shortcuts", "app.desktop", "desktop_surface",
         "桌面快捷方式", "App Shortcuts",
         "静态/动态应用快捷方式发布与更新。",
         ["ShortcutManager、UIApplicationShortcutItem、shortcutManager"],
         ["小组件见 widget"],
         merge_bindings(
             A("ShortcutManager", "https://developer.android.com/reference/android/content/pm/ShortcutManager"),
             I("UIApplicationShortcutItem", "https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem", "class"),
             H("桌面快捷方式", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/shortcuts"),
         ),
         {"disposition": "kept", "sources": ["app.desktop.shortcuts"]})
    leaf(f, "app.desktop.dynamic_icon", "app.desktop", "desktop_surface",
         "动态图标", "Dynamic App Icon",
         "运行时切换桌面应用图标/角标相关入口。",
         ["activity-alias icon、alternate icons、动态图标"],
         ["快捷方式见 shortcuts"],
         merge_bindings(
             A("activity-alias icons", "https://developer.android.com/guide/topics/manifest/activity-alias-element", "guide"),
             I("setAlternateIconName", "https://developer.apple.com/documentation/uikit/uiapplication/2806818-setalternateiconname", "method"),
             H("动态图标", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-icon-management"),
         ))
    leaf(f, "app.desktop.widget.timeline", "app.desktop.widget", "widget_detail",
         "小组件时间线刷新", "Widget Timeline Refresh",
         "按时间线或周期性策略刷新小组件内容。",
         ["TimelineProvider、AppWidget update、formProvider update"],
         ["小组件声明见父节点"],
         merge_bindings(
             A("AppWidgetManager.updateAppWidget", "https://developer.android.com/reference/android/appwidget/AppWidgetManager"),
             I("TimelineProvider", "https://developer.apple.com/documentation/widgetkit/timelineprovider", "protocol"),
             H("formProvider", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formprovider"),
         ), level="L4")
    for node in f:
        if node["id"] == "app.desktop.widget":
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            node["knowledge_path"] = "knowledge/app/desktop/widget/_rollup.yaml"

    # install
    leaf(f, "app.install.package_update", "app.install", "install_aspect",
         "应用安装更新", "Package Install and Update",
         "应用包安装、更新与包格式分发模型。",
         ["PackageInstaller、HAP/AAB 安装更新"],
         ["应用内更新 API 见 inapp_update"],
         merge_bindings(
             A("PackageInstaller", "https://developer.android.com/reference/android/content/pm/PackageInstaller"),
             I("NSExtension / App install (系统)", "https://developer.apple.com/documentation/storekit", "framework"),
             H("bundleManager / HAP", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-package-overview"),
         ),
         {"disposition": "kept", "sources": ["app.install.package_update"]})
    leaf(f, "app.install.inapp_update", "app.install", "install_aspect",
         "应用内更新", "In-app Update",
         "应用内检查并触发更新流程。",
         ["AppUpdateManager、updateManager"],
         ["商店外安装见 package_update"],
         merge_bindings(
             A("AppUpdateManager", "https://developer.android.com/guide/playcore/in-app-updates", "guide"),
             I("AppStore / SKStoreProductViewController", "https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller", "class"),
             H("updateManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-updatemanager"),
         ))
    leaf(f, "app.install.instant", "app.install", "install_aspect",
         "轻量即用安装", "Instant / Lightweight Install",
         "免安装或轻量即用的应用分发与拉起。",
         ["App Clip、AtomicService/元服务、Instant（历史）"],
         ["完整包安装见 package_update"],
         merge_bindings(
             A("Google Play Instant", "https://developer.android.com/topic/google-play-instant", "guide"),
             I("App Clip", "https://developer.apple.com/documentation/appclip", "framework"),
             H("AtomicService", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/atomic-service-overview"),
         ),
         {"disposition": "kept", "sources": ["app.install.instant"]})
    leaf(f, "app.install.on_demand", "app.install", "install_aspect",
         "按需模块交付", "On-demand Module Delivery",
         "按需下载功能模块/资产包。",
         ["Play Feature Delivery、moduleInstallManager"],
         ["完整更新见 package_update"],
         merge_bindings(
             A("SplitInstallManager", "https://developer.android.com/guide/playcore/feature-delivery", "guide"),
             pending("ios", "On-Demand Resources"),
             H("moduleInstallManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-moduleinstallmanager"),
         ))
    leaf(f, "app.install.query", "app.install", "install_aspect",
         "已安装包查询", "Installed Package Query",
         "查询本机已安装应用/包信息（受可见性约束）。",
         ["PackageManager、bundleManager.getBundleInfo、canOpenURL 限制"],
         ["安装动作见 package_update"],
         merge_bindings(
             A("PackageManager", "https://developer.android.com/reference/android/content/pm/PackageManager"),
             I("canOpenURL / LSApplicationQueriesSchemes", "https://developer.apple.com/documentation/uikit/uiapplication/1622952-canopenurl", "method"),
             H("bundleManager.getBundleInfo", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager"),
         ))
    leaf(f, "app.install.twin", "app.install", "install_aspect",
         "应用分身", "App Twin / Clone",
         "同一应用多实例/分身安装与管理入口。",
         ["应用分身"],
         ["普通安装见 package_update"],
         merge_bindings(
             pending("android", "OEM 分身能力，非统一公开 API"),
             pending("ios"),
             H("应用分身", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone"),
         ))

    # extensions
    leaf(f, "app.extensions.share", "app.extensions", "extension_kind",
         "分享扩展", "Share Extension",
         "作为系统分享目标接收并处理外来内容。",
         ["ShareCompat / Share Extension / ShareExtensionAbility"],
         ["通用 UI 嵌入见 ui_embed"],
         merge_bindings(
             A("ShareSheet / Intent.ACTION_SEND", "https://developer.android.com/training/sharing/receive", "guide"),
             I("Share Extension", "https://developer.apple.com/documentation/foundation/app_extension_support", "guide"),
             H("ShareExtensionAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-shareextensionability"),
         ),
         {"disposition": "kept", "sources": ["app.extensions.share"]})
    leaf(f, "app.extensions.photo_editor", "app.extensions", "extension_kind",
         "照片编辑扩展", "Photo Editor Extension",
         "向系统相册提供就地照片编辑扩展。",
         ["Photo Editing Extension、PhotoEditorExtensionAbility"],
         ["媒体库管理见 media.library.manage"],
         merge_bindings(
             pending("android"),
             I("Photo Editing Extension", "https://developer.apple.com/documentation/photokit/photo_editing_extension", "guide"),
             H("PhotoEditorExtensionAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-photoeditorextensionability"),
         ))
    leaf(f, "app.extensions.ui_embed", "app.extensions", "extension_kind",
         "嵌入式UI扩展", "Embedded UI Extension",
         "在宿主中嵌入扩展提供的界面内容。",
         ["EmbeddedUIExtensionAbility、App Extensions UI"],
         ["分享扩展见 share"],
         merge_bindings(
             pending("android", "可用 Activity 嵌入 / SDK 视图"),
             I("App Extensions", "https://developer.apple.com/documentation/foundation/app_extension_support", "guide"),
             H("EmbeddedUIExtensionAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddeduiextensionability"),
         ))
    leaf(f, "app.extensions.driver", "app.extensions", "extension_kind",
         "驱动扩展", "Driver Extension",
         "外设/驱动类扩展能力入口。",
         ["DriverExtensionAbility"],
         ["USB 主机见 connectivity.usb"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("DriverExtensionAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-driverextensionability"),
         ))
    leaf(f, "app.extensions.agent", "app.extensions", "extension_kind",
         "智能体扩展", "Agent Extension",
         "系统智能体/代理宿主扩展入口。",
         ["AgentExtensionAbility"],
         ["通用 AI 运行时见 ai"],
         merge_bindings(
             pending("android"),
             pending("ios", "App Intents / Siri 另域"),
             H("AgentExtensionAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-agentextensionability"),
         ))

    # a few more atomics to enrich without padding
    leaf(f, "app.model.ui_entry.launch_mode", "app.model.ui_entry", "ui_entry_detail",
         "界面入口启动模式", "UI Entry Launch Mode",
         "单例/标准等界面入口启动模式与任务亲和。",
         ["launchMode、launchType"],
         ["生命周期回调见 lifecycle.activity_ability"],
         merge_bindings(
             A("launchMode", "https://developer.android.com/guide/components/activities/tasks-and-back-stack", "guide"),
             pending("ios"),
             H("launchType", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-launch-type"),
         ), level="L4")
    leaf(f, "app.lifecycle.activity_ability.state_restore", "app.lifecycle.activity_ability", "lifecycle_ui_detail",
         "界面状态恢复", "UI State Restoration",
         "界面组件在重建后恢复视图状态。",
         ["restoreState、setSupportRestore"],
         ["进程死亡保存见 process_death"],
         merge_bindings(
             A("ViewModel SavedState", "https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate", "guide"),
             I("Restoring Your App's State", "https://developer.apple.com/documentation/uikit/view_controllers/preserving_your_app_s_ui_across_launches", "guide"),
             H("setSupportRestore", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-persist-data"),
         ), level="L4")
    for node in f:
        if node["id"] in {"app.model.ui_entry", "app.lifecycle.activity_ability"}:
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            parts = node["id"].split(".")
            node["knowledge_path"] = "knowledge/" + "/".join(parts) + "/_rollup.yaml"

    leaf(f, "app.install.on_demand.status", "app.install.on_demand", "ondemand_detail",
         "按需模块状态监听", "On-demand Module Status",
         "监听按需模块下载/安装会话状态。",
         ["SplitInstallStateUpdatedListener、module install session"],
         ["发起安装见父节点"],
         merge_bindings(
             A("SplitInstallStateUpdatedListener", "https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallStateUpdatedListener"),
             I("NSBundleResourceRequest", "https://developer.apple.com/documentation/foundation/nsbundleresourcerequest", "class"),
             H("moduleInstallManager 会话", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-moduleinstallmanager"),
         ), level="L4")
    leaf(f, "app.install.on_demand.deferred", "app.install.on_demand", "ondemand_detail",
         "延后按需安装", "Deferred On-demand Install",
         "在空闲时延后下载按需模块。",
         ["deferred install / wifi-only install"],
         ["状态监听见 status"],
         merge_bindings(
             A("SplitInstallManager.deferredInstall", "https://developer.android.com/guide/playcore/feature-delivery/on-demand", "guide"),
             I("NSBundleResourceRequest loadingPriority", "https://developer.apple.com/documentation/foundation/nsbundleresourcerequest", "class"),
             pending("harmonyos"),
         ), level="L4")
    for node in f:
        if node["id"] == "app.install.on_demand":
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            node["knowledge_path"] = "knowledge/app/install/on_demand/_rollup.yaml"

    # Enrich single-child branches + additional atomics toward ~70-120
    leaf(f, "app.lifecycle.activity_ability.multi_instance", "app.lifecycle.activity_ability", "lifecycle_ui_detail",
         "多实例与任务", "Multi-instance and Tasks",
         "同一界面组件多任务/多实例呈现。",
         ["documentLaunchMode、UIScene sessions、UIAbility 多实例"],
         ["状态恢复见 state_restore"],
         merge_bindings(
             A("documentLaunchMode", "https://developer.android.com/guide/components/activities/multi-window#multi-instance", "guide"),
             I("UISceneSession", "https://developer.apple.com/documentation/uikit/uiscenesession", "class"),
             H("UIAbility 多实例", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-multi-instance"),
         ), level="L4")
    leaf(f, "app.model.ui_entry.exported", "app.model.ui_entry", "ui_entry_detail",
         "入口导出与可见性", "Entry Export Visibility",
         "声明界面入口是否可被外部拉起。",
         ["exported / skills"],
         ["启动模式见 launch_mode"],
         merge_bindings(
             A("android:exported", "https://developer.android.com/guide/topics/manifest/activity-element#exported", "guide"),
             I("LSApplicationQueriesSchemes / URL types", "https://developer.apple.com/documentation/bundleresources/information-property-list/lsapplicationqueriesschemes", "guide"),
             H("exported / skills", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file"),
         ), level="L4")
    leaf(f, "app.background.foreground_task.notification", "app.background.foreground_task", "foreground_detail",
         "前台任务通知", "Foreground Task Notification",
         "长时任务必须展示的用户可感知通知/状态。",
         ["startForeground notification、continuous task notification"],
         ["类型声明见 types"],
         merge_bindings(
             A("startForeground", "https://developer.android.com/reference/android/app/Service#startForeground(int,%20android.app.Notification)", "method"),
             pending("ios"),
             H("连续任务通知", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/continuous-task"),
         ), level="L4")
    leaf(f, "app.background.deferred_work.periodic", "app.background.deferred_work", "deferred_detail",
         "周期性延迟任务", "Periodic Deferred Work",
         "按间隔重复执行的延迟后台任务。",
         ["PeriodicWorkRequest、BGProcessingTask periodic"],
         ["约束见 constraints"],
         merge_bindings(
             A("PeriodicWorkRequest", "https://developer.android.com/reference/androidx/work/PeriodicWorkRequest"),
             I("BGProcessingTaskRequest", "https://developer.apple.com/documentation/backgroundtasks/bgprocessingtaskrequest", "class"),
             H("workScheduler 周期任务", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workscheduler"),
         ), level="L4")
    leaf(f, "app.desktop.widget.configuration", "app.desktop.widget", "widget_detail",
         "小组件配置界面", "Widget Configuration UI",
         "用户添加小组件时的配置 Activity/界面。",
         ["AppWidget config activity、IntentConfiguration、form config"],
         ["时间线刷新见 timeline"],
         merge_bindings(
             A("AppWidget configuration", "https://developer.android.com/develop/ui/views/appwidgets#setting-up-configuration-activity", "guide"),
             I("IntentConfiguration", "https://developer.apple.com/documentation/widgetkit/intentconfiguration", "structure"),
             H("卡片配置", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/formextensionability"),
         ), level="L4")
    leaf(f, "app.extensions.share.receive", "app.extensions.share", "share_detail",
         "接收分享内容", "Receive Shared Content",
         "解析并接收系统分享传入的文本/文件等内容。",
         ["Intent extras / extension context input items"],
         ["作为分享目标注册见父节点"],
         merge_bindings(
             A("Intent.EXTRA_STREAM", "https://developer.android.com/training/sharing/receive", "guide"),
             I("NSExtensionContext.inputItems", "https://developer.apple.com/documentation/foundation/nsextensioncontext/1416593-inputitems", "property"),
             H("ShareExtensionAbility.onShareSelect", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-shareextensionability"),
         ), level="L4")
    leaf(f, "app.extensions.share.send", "app.extensions.share", "share_detail",
         "发起系统分享", "Send via System Share",
         "将内容交给系统分享面板分发。",
         ["ACTION_SEND / UIActivityViewController / share sheet"],
         ["接收扩展见 receive"],
         merge_bindings(
             A("Intent.ACTION_SEND", "https://developer.android.com/training/sharing/send", "guide"),
             I("UIActivityViewController", "https://developer.apple.com/documentation/uikit/uiactivityviewcontroller", "class"),
             H("系统分享", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-overview"),
         ), level="L4")
    leaf(f, "app.launch.startup_init.dependencies", "app.launch.startup_init", "startup_detail",
         "初始化依赖图", "Initializer Dependency Graph",
         "声明启动初始化器之间的依赖顺序。",
         ["Initializer dependencies、startup config dependencies"],
         ["运行初始化见父节点"],
         merge_bindings(
             A("Initializer.dependencies", "https://developer.android.com/topic/libraries/app-startup", "guide"),
             pending("ios"),
             H("StartupConfig 依赖", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-startupmanager"),
         ), level="L4")
    leaf(f, "app.process.priority.memory_trim", "app.process.priority", "priority_detail",
         "内存裁剪回调", "Memory Trim Callbacks",
         "在系统内存压力下接收裁剪级别回调。",
         ["onTrimMemory、didReceiveMemoryWarning"],
         ["优先级层级见父节点"],
         merge_bindings(
             A("ComponentCallbacks2.onTrimMemory", "https://developer.android.com/reference/android/content/ComponentCallbacks2#onTrimMemory(int)", "method"),
             I("didReceiveMemoryWarning", "https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623063-applicationdidreceivememorywarni", "method"),
             H("Application.onMemoryLevel", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-application"),
         ), level="L4")
    leaf(f, "app.model.service_component.bind", "app.model.service_component", "service_detail",
         "绑定服务连接", "Bound Service Connection",
         "客户端绑定服务组件并获取通信接口。",
         ["bindService、connectServiceExtensionAbility"],
         ["服务声明见父节点"],
         merge_bindings(
             A("bindService", "https://developer.android.com/guide/components/bound-services", "guide"),
             pending("ios"),
             H("connectServiceExtensionAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext"),
         ), level="L4")
    leaf(f, "app.desktop.shortcuts.pin", "app.desktop.shortcuts", "shortcut_detail",
         "固定快捷方式", "Pinned Shortcuts",
         "请求将快捷方式固定到桌面。",
         ["requestPinShortcut、ShortcutItem"],
         ["动态快捷方式发布见父节点"],
         merge_bindings(
             A("ShortcutManager.requestPinShortcut", "https://developer.android.com/reference/android/content/pm/ShortcutManager#requestPinShortcut(android.content.pm.ShortcutInfo,%20android.content.IntentSender)", "method"),
             pending("ios"),
             H("固定快捷方式", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/shortcuts"),
         ), level="L4")
    leaf(f, "app.install.package_update.session", "app.install.package_update", "package_detail",
         "安装会话", "Install Session",
         "创建包安装/更新会话并提交。",
         ["PackageInstaller.Session、bundle install session"],
         ["包格式见父节点"],
         merge_bindings(
             A("PackageInstaller.Session", "https://developer.android.com/reference/android/content/pm/PackageInstaller.Session"),
             pending("ios", "系统安装，无对等第三方会话 API"),
             H("bundleInstaller", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-installer"),
         ), level="L4")
    for node in f:
        if node["id"] in {
            "app.extensions.share", "app.launch.startup_init", "app.process.priority",
            "app.model.service_component", "app.desktop.shortcuts", "app.install.package_update",
        }:
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            parts = node["id"].split(".")
            node["knowledge_path"] = "knowledge/" + "/".join(parts) + "/_rollup.yaml"

    leaf(f, "app.process.priority.lmr", "app.process.priority", "priority_detail",
         "后台限制与待机桶", "Background Restrictions and Standby",
         "应用待机桶与后台限制对执行机会的影响查询。",
         ["AppStandby / UsageStats、Background App Refresh"],
         ["内存裁剪见 memory_trim"],
         merge_bindings(
             A("UsageStatsManager", "https://developer.android.com/reference/android/app/usage/UsageStatsManager"),
             I("Background App Refresh", "https://developer.apple.com/documentation/backgroundtasks", "framework"),
             H("应用休眠/管控", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/background-task-overview"),
         ), level="L4")
    leaf(f, "app.launch.startup_init.timeout", "app.launch.startup_init", "startup_detail",
         "启动初始化超时", "Startup Initializer Timeout",
         "启动任务超时与失败处理策略。",
         ["startup timeout config"],
         ["依赖图见 dependencies"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("StartupTask 超时", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-startupmanager"),
         ), level="L4")
    leaf(f, "app.desktop.shortcuts.dynamic", "app.desktop.shortcuts", "shortcut_detail",
         "动态快捷方式发布", "Dynamic Shortcut Publishing",
         "运行时发布/更新动态快捷方式集合。",
         ["setDynamicShortcuts、shortcutItems"],
         ["固定快捷方式见 pin"],
         merge_bindings(
             A("ShortcutManager.setDynamicShortcuts", "https://developer.android.com/reference/android/content/pm/ShortcutManager#setDynamicShortcuts(java.util.List%3Candroid.content.pm.ShortcutInfo%3E)", "method"),
             I("UIApplication.shortcutItems", "https://developer.apple.com/documentation/uikit/uiapplication/1622937-shortcutitems", "property"),
             H("动态快捷方式", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/shortcuts"),
         ), level="L4")
    leaf(f, "app.model.service_component.start", "app.model.service_component", "service_detail",
         "启动服务组件", "Start Service Component",
         "显式启动服务组件（非绑定）。",
         ["startService / startForegroundService、startAbility service"],
         ["绑定见 bind"],
         merge_bindings(
             A("startService", "https://developer.android.com/guide/components/services", "guide"),
             pending("ios"),
             H("startAbility (service)", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appserviceextensionability"),
         ), level="L4")
    leaf(f, "app.install.package_update.uninstall", "app.install.package_update", "package_detail",
         "卸载应用包", "Uninstall Package",
         "请求卸载本应用或其他可见包（受权限约束）。",
         ["deletePackage / uninstall"],
         ["安装会话见 session"],
         merge_bindings(
             A("PackageInstaller.uninstall", "https://developer.android.com/reference/android/content/pm/PackageInstaller#uninstall(java.lang.String,%20android.content.IntentSender)", "method"),
             pending("ios"),
             H("bundleManager.uninstall", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-installer"),
         ), level="L4")
    leaf(f, "app.model.app_entry.multi_module", "app.model.app_entry", "app_entry_detail",
         "多模块应用入口", "Multi-module App Entry",
         "多 module/App Extension 共存时的入口与 AbilityStage 划分。",
         ["multiple modules / App Extensions hosts"],
         ["进程入口见父节点"],
         merge_bindings(
             A("App modules", "https://developer.android.com/guide/app-bundle", "guide"),
             I("App Extensions", "https://developer.apple.com/documentation/foundation/app_extension_support", "guide"),
             H("AbilityStage 多模块", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-structure-stage"),
         ), level="L4")
    leaf(f, "app.model.app_entry.attach_base", "app.model.app_entry", "app_entry_detail",
         "进程附加与基础上下文", "Attach Base Context",
         "进程创建早期附加基础上下文/资源覆写入口。",
         ["attachBaseContext"],
         ["多模块见 multi_module"],
         merge_bindings(
             A("Application.attachBaseContext", "https://developer.android.com/reference/android/app/Application#attachBaseContext(android.content.Context)", "method"),
             pending("ios"),
             H("AbilityStage.onCreate", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage"),
         ), level="L4")
    leaf(f, "app.lifecycle.callbacks.foreground", "app.lifecycle.callbacks", "lifecycle_cb_detail",
         "前后台切换监听", "Foreground Background Observation",
         "观察应用进入前台/后台。",
         ["ON_START/ON_STOP、scenePhase、onApplicationForeground"],
         ["页面级生命周期见 activity_ability"],
         merge_bindings(
             A("Lifecycle.Event", "https://developer.android.com/reference/androidx/lifecycle/Lifecycle.Event"),
             I("scenePhase", "https://developer.apple.com/documentation/swiftui/scenephase", "enumeration"),
             H("onApplicationForeground/Background", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-application"),
         ), level="L4")
    leaf(f, "app.lifecycle.callbacks.environment", "app.lifecycle.callbacks", "lifecycle_cb_detail",
         "配置环境变更", "Configuration Environment Changes",
         "监听语言、暗色、密度等配置变更。",
         ["onConfigurationChanged、traitCollection"],
         ["前后台见 foreground"],
         merge_bindings(
             A("onConfigurationChanged", "https://developer.android.com/reference/android/app/Application#onConfigurationChanged(android.content.res.Configuration)", "method"),
             I("traitCollectionDidChange", "https://developer.apple.com/documentation/uikit/uitraitenvironment/1623516-traitcollectiondidchange", "method"),
             H("EnvironmentCallback", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-environmentcallback"),
         ), level="L4")
    leaf(f, "app.background.transient.expire", "app.background.transient", "transient_detail",
         "延缓挂起到期", "Suspend Delay Expiration",
         "短暂延缓挂起到期回调与收尾。",
         ["expiration handler / suspend delay callback"],
         ["申请延缓见 request"],
         merge_bindings(
             pending("android"),
             I("UIBackgroundTask expirationHandler", "https://developer.apple.com/documentation/uikit/uiapplication/1623031-beginbackgroundtask", "method"),
             H("SuspendDelay 回调", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager"),
         ), level="L4")
    leaf(f, "app.background.transient.request", "app.background.transient", "transient_detail",
         "申请短暂延缓", "Request Transient Delay",
         "申请短时间延迟进入挂起。",
         ["beginBackgroundTask、requestSuspendDelay"],
         ["到期见 expire"],
         merge_bindings(
             pending("android"),
             I("beginBackgroundTask", "https://developer.apple.com/documentation/uikit/uiapplication/1623031-beginbackgroundtask", "method"),
             H("requestSuspendDelay", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager"),
         ), level="L4")
    leaf(f, "app.extensions.ui_embed.host", "app.extensions.ui_embed", "embed_detail",
         "嵌入扩展宿主", "Embedded Extension Host",
         "宿主侧加载并展示嵌入式扩展 UI。",
         ["EmbeddedComponent host / extension host"],
         ["扩展实现见 provider"],
         merge_bindings(
             pending("android"),
             I("NSExtensionHost", "https://developer.apple.com/documentation/foundation/app_extension_support", "guide"),
             H("EmbeddedComponent", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-embedded-component"),
         ), level="L4")
    leaf(f, "app.extensions.ui_embed.provider", "app.extensions.ui_embed", "embed_detail",
         "嵌入扩展提供方", "Embedded Extension Provider",
         "作为嵌入式 UI 扩展提供可被宿主加载的界面。",
         ["EmbeddedUIExtensionAbility provider"],
         ["宿主加载见 host"],
         merge_bindings(
             pending("android"),
             I("App Extension principal class", "https://developer.apple.com/documentation/foundation/app_extension_support", "guide"),
             H("EmbeddedUIExtensionAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddeduiextensionability"),
         ), level="L4")
    for node in f:
        if node["id"] in {
            "app.model.app_entry", "app.lifecycle.callbacks", "app.background.transient",
            "app.extensions.ui_embed",
        }:
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            parts = node["id"].split(".")
            node["knowledge_path"] = "knowledge/" + "/".join(parts) + "/_rollup.yaml"

    dedup = {n["id"]: n for n in f}
    return list(dedup.values())


def main():
    nodes = build()
    path = write_domain("app", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
