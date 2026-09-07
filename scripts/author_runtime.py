#!/usr/bin/env python3
"""Author the runtime domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "runtime_capability_family"


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
        "runtime", parent=None, level="L1",
        zh="运行时与国际化", en="Runtime and Internationalization",
        definition="并发执行、国际化本地化、运行环境、内存管理与运行时打包加载。",
        includes=['并发、i18n、环境、内存、打包运行时'],
        excludes=['应用组件模型见 app', '安全密钥见 security'],
        legacy={'disposition': 'kept', 'sources': ['runtime']},
    ))
    l2 = [
        ('runtime.concurrency', '并发模型', 'Concurrency', '线程、任务池、队列、锁与跨线程通信。', ['worker、taskpool、队列、锁'], ['进程模型见 app.process'], ['runtime.concurrency']),
        ('runtime.i18n', '国际化', 'Internationalization', '区域、格式化、资源与双向文本。', ['locale、格式、资源、RTL'], ['系统语言设置 UI'], ['runtime.i18n']),
        ('runtime.env', '运行环境', 'Runtime Environment', '配置、时间、QoS 与运行时加速服务。', ['configuration、datetime、QoS'], ['设备硬件见 device'], []),
        ('runtime.memory', '内存管理', 'Memory Management', '堆内存、引用与低内存响应。', ['heap、GC提示、低内存'], ['性能采样见 observability.perf'], []),
        ('runtime.packaging_runtime', '打包与加载运行时', 'Packaging and Loading Runtime', '模块/原生库加载与跨语言互操作运行时。', ['模块、JNI/NAPI、动态加载'], ['应用安装见 app.install'], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="runtime", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- runtime.concurrency ---
    leaf(f, "runtime.concurrency.overview", "runtime.concurrency", "concurrency_operation", "并发模型总览入口", "Concurrency Model Overview",
         "查询或选择平台推荐的并发原语入口。", ['Dispatchers / TaskPool overview'], ['具体队列见 queues'],
         B(('Kotlin coroutines', 'https://developer.android.com/kotlin/coroutines', 'guide'), ('Swift Concurrency', 'https://developer.apple.com/documentation/swift/concurrency', 'guide'), ('TaskPool', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction')), {'disposition': 'kept', 'sources': ['runtime.concurrency.overview']}, level="L3", privacy="none")
    leaf(f, "runtime.concurrency.queues", "runtime.concurrency", "concurrency_operation", "调度队列", "Dispatch Queues",
         "串行/并发队列上调度异步工作。", ['GCD / Handler / AsyncRunner'], ['任务池见 taskpool'],
         B(('Handler', 'https://developer.android.com/reference/android/os/Handler'), ('DispatchQueue', 'https://developer.apple.com/documentation/dispatch/dispatchqueue', 'class'), ('AsyncRunner', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asyncrunner')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.concurrency.taskpool", "runtime.concurrency", "concurrency_operation", "任务池", "Task Pool",
         "在任务池中执行可转移任务。", ['TaskPool'], ['常驻线程见 worker'],
         B(('Executor', 'https://developer.android.com/reference/java/util/concurrent/Executor'), ('TaskGroup', 'https://developer.apple.com/documentation/swift/taskgroup', 'struct'), ('taskpool', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.concurrency.worker", "runtime.concurrency", "concurrency_operation", "常驻工作线程", "Persistent Worker Thread",
         "创建常驻 Worker 处理长时间任务。", ['Worker'], ['任务池见 taskpool'],
         B(('Thread', 'https://developer.android.com/reference/java/lang/Thread'), None, ('worker', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-worker')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.concurrency.locks", "runtime.concurrency", "concurrency_operation", "锁与条件同步", "Locks and Conditions",
         "互斥锁、条件变量与异步锁。", ['mutex / NSLock'], ['队列见 queues'],
         B(('ReentrantLock', 'https://developer.android.com/reference/java/util/concurrent/locks/ReentrantLock'), ('NSLock', 'https://developer.apple.com/documentation/foundation/nslock', 'class'), ('AsyncLock', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-lock')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.concurrency.shared_memory", "runtime.concurrency", "concurrency_operation", "共享内存缓冲", "Shared Memory Buffer",
         "跨线程共享内存缓冲区。", ['SharedArrayBuffer / ashmem'], ['消息通信见 messaging'],
         B(('SharedMemory', 'https://developer.android.com/reference/android/os/SharedMemory'), None, ('SendShareable', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.concurrency.messaging", "runtime.concurrency", "concurrency_operation", "线程间消息", "Inter-Thread Messaging",
         "线程间事件与消息传递。", ['Emitter / MessageChannel'], ['共享内存见 shared_memory'],
         B(('Handler messages', 'https://developer.android.com/reference/android/os/Handler'), ('NotificationCenter', 'https://developer.apple.com/documentation/foundation/notificationcenter', 'class'), ('emitter', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.concurrency.futures", "runtime.concurrency", "concurrency_operation", "异步结果对象", "Future Async Result",
         "表示尚未完成的异步计算结果。", ['Future / Promise / Task'], ['队列见 queues'],
         B(('CompletableFuture', 'https://developer.android.com/reference/java/util/concurrent/CompletableFuture'), ('Task', 'https://developer.apple.com/documentation/swift/task', 'struct'), ('Promise', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promise')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.concurrency.sendable", "runtime.concurrency", "concurrency_operation", "可发送共享对象", "Sendable Shared Objects",
         "在并发域间传递可发送对象。", ['Sendable'], ['共享内存见 shared_memory'],
         B(None, ('Sendable', 'https://developer.apple.com/documentation/swift/sendable', 'protocol'), ('Sendable', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- runtime.i18n ---
    leaf(f, "runtime.i18n.locale", "runtime.i18n", "i18n_operation", "区域设置", "Locale Settings",
         "获取与匹配用户/应用区域。", ['Locale / LocaleList'], ['格式化见 formatting'],
         B(('Locale', 'https://developer.android.com/reference/java/util/Locale'), ('Locale', 'https://developer.apple.com/documentation/foundation/locale', 'struct'), ('i18n', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-i18n')), {'disposition': 'kept', 'sources': ['runtime.i18n.locale']}, level="L3", privacy="none")
    leaf(f, "runtime.i18n.formatting", "runtime.i18n", "i18n_operation", "日期数字格式化", "Date Number Formatting",
         "按区域格式化日期、时间与数字。", ['DateFormat / NumberFormat'], ['区域见 locale'],
         B(('DateFormat', 'https://developer.android.com/reference/java/text/DateFormat'), ('DateFormatter', 'https://developer.apple.com/documentation/foundation/dateformatter', 'class'), ('intl', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-intl')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.i18n.resources", "runtime.i18n", "i18n_operation", "本地化资源", "Localized Resources",
         "按区域加载字符串与资源。", ['strings.xml / Localizable'], ['区域见 locale'],
         B(('Resources', 'https://developer.android.com/guide/topics/resources/localization', 'guide'), ('Bundle localization', 'https://developer.apple.com/documentation/foundation/bundle', 'class'), ('resourceManager', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.i18n.rtl", "runtime.i18n", "i18n_operation", "双向文本布局", "Bidirectional Text Layout",
         "RTL/LTR 布局方向与镜像。", ['layoutDirection'], ['资源见 resources'],
         B(('layoutDirection', 'https://developer.android.com/reference/android/view/View', 'class'), ('layoutDirection', 'https://developer.apple.com/documentation/swiftui/environmentvalues/layoutdirection', 'property'), ('Direction', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-i18n')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.i18n.collator", "runtime.i18n", "i18n_operation", "区域排序规则", "Locale Collator",
         "按区域规则比较与排序字符串。", ['Collator'], ['格式化见 formatting'],
         B(('Collator', 'https://developer.android.com/reference/java/text/Collator'), ('String.localizedStandardCompare', 'https://developer.apple.com/documentation/foundation/nsstring', 'class'), ('Collator', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-intl')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.i18n.timezone", "runtime.i18n", "i18n_operation", "时区", "Time Zone",
         "查询与转换时区。", ['TimeZone'], ['日期格式见 formatting'],
         B(('TimeZone', 'https://developer.android.com/reference/java/util/TimeZone'), ('TimeZone', 'https://developer.apple.com/documentation/foundation/timezone', 'struct'), ('i18n', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-i18n')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.i18n.preferred_language", "runtime.i18n", "i18n_operation", "偏好语言列表", "Preferred Languages",
         "读取用户偏好语言列表。", ['LocaleList / preferredLanguages'], ['应用区域见 locale'],
         B(('LocaleList', 'https://developer.android.com/reference/android/os/LocaleList'), ('Locale.preferredLanguages', 'https://developer.apple.com/documentation/foundation/locale', 'struct'), ('System.getSystemLanguage', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-i18n')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.i18n.pseudo", "runtime.i18n", "i18n_operation", "伪本地化", "Pseudo Localization",
         "启用伪本地化以测试布局。", ['pseudo locales'], ['资源见 resources'],
         B(('PseudoLocales', 'https://developer.android.com/guide/topics/resources/pseudolocales', 'guide'), ('Pseudolanguage', 'https://developer.apple.com/documentation/xcode', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- runtime.env ---
    leaf(f, "runtime.env.configuration", "runtime.env", "env_operation", "运行配置变更", "Configuration Changes",
         "监听密度、方向、主题等配置变更。", ['Configuration / traitCollection'], ['区域见 i18n.locale'],
         B(('Configuration', 'https://developer.android.com/reference/android/content/res/Configuration'), ('UITraitCollection', 'https://developer.apple.com/documentation/uikit/uitraitcollection', 'class'), ('EnvironmentCallback', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-environmentcallback')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.env.datetime", "runtime.env", "env_operation", "系统日期时间", "System Date Time",
         "读取系统时间并监听变更。", ['SystemClock / Date'], ['时区见 i18n.timezone'],
         B(('SystemClock', 'https://developer.android.com/reference/android/os/SystemClock'), ('Date', 'https://developer.apple.com/documentation/foundation/date', 'struct'), ('systemDateTime', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-systemdatetime')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.env.qos", "runtime.env", "env_operation", "线程QoS优先级", "Thread QoS Priority",
         "为工作设置服务质量优先级。", ['QoS / Process.setThreadPriority'], ['队列见 concurrency.queues'],
         B(('Process.setThreadPriority', 'https://developer.android.com/reference/android/os/Process'), ('qos_class', 'https://developer.apple.com/documentation/dispatch', 'framework'), ('qos', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-qos')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.env.ffrt", "runtime.env", "env_operation", "函数流并发运行时", "Function Flow Runtime",
         "使用函数流运行时调度并发任务。", ['FFRT'], ['通用任务池见 concurrency.taskpool'],
         B(None, None, ('FFRT', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ffrt-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.env.accel_services", "runtime.env", "env_operation", "运行时加速服务", "Runtime Acceleration Services",
         "算法/热点加速等运行时加速服务入口。", ['FAST / Linx'], ['推理加速见 ai.inference'],
         B(None, None, ('FAST', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.env.build_info", "runtime.env", "env_operation", "构建与设备信息", "Build and Device Info",
         "读取 OS 版本、构建号等运行环境信息。", ['Build.VERSION / ProcessInfo'], ['硬件能力见 device'],
         B(('Build', 'https://developer.android.com/reference/android/os/Build'), ('ProcessInfo', 'https://developer.apple.com/documentation/foundation/processinfo', 'class'), ('deviceInfo', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-device-info')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- runtime.memory ---
    leaf(f, "runtime.memory.heap_stats", "runtime.memory", "memory_operation", "堆内存统计", "Heap Memory Statistics",
         "查询堆已用/可用内存。", ['Runtime.totalMemory / task_info'], ['低内存见 low_memory'],
         B(('Runtime', 'https://developer.android.com/reference/java/lang/Runtime'), ('mach_task_basic_info', 'https://developer.apple.com/documentation/kernel/mach_task_basic_info', 'struct'), ('Hidebug', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.memory.low_memory", "runtime.memory", "memory_operation", "低内存回调", "Low Memory Callback",
         "在系统内存压力时收到回调并释放缓存。", ['onTrimMemory / didReceiveMemoryWarning'], ['堆统计见 heap_stats'],
         B(('ComponentCallbacks2', 'https://developer.android.com/reference/android/content/ComponentCallbacks2'), ('UIApplication memory warning', 'https://developer.apple.com/documentation/uikit/uiapplication', 'class'), ('ApplicationStateChange', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-applicationstatechangecallback')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.memory.gc_hint", "runtime.memory", "memory_operation", "GC与回收提示", "GC and Reclamation Hints",
         "提示运行时进行垃圾回收或资源回收。", ['System.gc / autoreleasepool'], ['堆统计见 heap_stats'],
         B(('Runtime.gc', 'https://developer.android.com/reference/java/lang/Runtime'), ('autoreleasepool', 'https://developer.apple.com/documentation/swift', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.memory.native_alloc", "runtime.memory", "memory_operation", "Native内存分配", "Native Memory Allocation",
         "原生堆分配与对齐分配入口。", ['malloc / ashmem'], ['共享内存见 concurrency.shared_memory'],
         B(('NDK memory', 'https://developer.android.com/ndk/guides', 'guide'), ('malloc', 'https://developer.apple.com/documentation/kernel/1537751-malloc', 'function'), ('native memory', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-memory')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.memory.weak_refs", "runtime.memory", "memory_operation", "弱引用与缓存引用", "Weak and Soft References",
         "使用弱/软引用管理可回收缓存。", ['WeakReference'], ['低内存见 low_memory'],
         B(('WeakReference', 'https://developer.android.com/reference/java/lang/ref/WeakReference'), ('NSPointerArray', 'https://developer.apple.com/documentation/foundation/nspointerarray', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- runtime.packaging_runtime ---
    leaf(f, "runtime.packaging_runtime.module_load", "runtime.packaging_runtime", "packaging_runtime_operation", "模块动态加载", "Dynamic Module Load",
         "运行时动态加载应用模块或包。", ['dynamic import / SplitInstall'], ['原生库见 native_lib'],
         B(('Play Feature Delivery', 'https://developer.android.com/guide/playcore/feature-delivery', 'guide'), ('Bundle.load', 'https://developer.apple.com/documentation/foundation/bundle', 'class'), ('dynamicImport', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dynamic-import')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.packaging_runtime.native_lib", "runtime.packaging_runtime", "packaging_runtime_operation", "原生库加载", "Native Library Load",
         "加载 JNI/NAPI 原生共享库。", ['System.loadLibrary / dlopen'], ['JNI 互操作见 jni'],
         B(('System.loadLibrary', 'https://developer.android.com/reference/java/lang/System'), ('dlopen', 'https://developer.apple.com/documentation/kernel', 'framework'), ('loadNativeModule', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-process')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.packaging_runtime.jni", "runtime.packaging_runtime", "packaging_runtime_operation", "JNI互操作", "JNI Interop",
         "Java/Kotlin 与原生代码互操作。", ['JNI'], ['NAPI 见 napi'],
         B(('JNI tips', 'https://developer.android.com/training/articles/perf-jni', 'guide'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.packaging_runtime.napi", "runtime.packaging_runtime", "packaging_runtime_operation", "NAPI节点互操作", "NAPI Interop",
         "ArkTS/JS 与原生通过 NAPI 互操作。", ['Node-API'], ['JNI 见 jni'],
         B(None, None, ('Node-API', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-process')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.packaging_runtime.jsvm", "runtime.packaging_runtime", "packaging_runtime_operation", "嵌入式脚本引擎", "Embedded Script Engine",
         "嵌入 JS 引擎执行脚本。", ['JSVM / JavaScriptCore'], ['WebView 见 web'],
         B(None, ('JavaScriptCore', 'https://developer.apple.com/documentation/javascriptcore', 'framework'), ('JSVM', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jsvm-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "runtime.packaging_runtime.vm_runtime", "runtime.packaging_runtime", "packaging_runtime_operation", "语言虚拟机运行时", "Language VM Runtime",
         "ART/ArkTS 等语言 VM 运行时配置与查询。", ['ART / ArkTS VM'], ['模块加载见 module_load'],
         B(('ART', 'https://source.android.com/docs/core/runtime', 'guide'), None, ('ArkTS runtime', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("runtime", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
