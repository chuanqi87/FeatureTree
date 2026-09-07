#!/usr/bin/env python3
"""Author the observability domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "observability_capability_family"


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
        "observability", parent=None, level="L1",
        zh="可观测与质量", en="Observability and Quality",
        definition="应用日志、崩溃卡死、性能剖析、指标与分布式追踪。",
        includes=['日志、崩溃、性能、指标、追踪'],
        excludes=['无障碍测试扫描见 a11y.testing', '游戏专用质量见 games'],
        legacy={'disposition': 'kept', 'sources': ['observability']},
    ))
    l2 = [
        ('observability.logging', '日志', 'Logging', '应用与系统日志写入、检索与监听。', ['app log、system log、watcher'], ['崩溃转储见 crash'], ['observability.logging']),
        ('observability.crash', '崩溃与卡死', 'Crash and Hang', '崩溃捕获、卡死检测与错误上报。', ['native/js crash、ANR/freeze、report'], ['性能追踪见 tracing'], ['observability.crash']),
        ('observability.perf', '性能剖析', 'Performance Profiling', '启动、帧率、CPU/内存等性能采集与检测。', ['启动、帧、CPU/内存、检测'], ['分布式追踪见 tracing'], ['observability.perf']),
        ('observability.metrics', '运行指标', 'Runtime Metrics', '应用运行指标采集与上报。', ['metrics kit、性能指标'], ['日志见 logging'], []),
        ('observability.tracing', '分布式追踪', 'Distributed Tracing', '跨组件调用链与系统 trace 采集。', ['trace section、hitrace'], ['宏观性能见 perf'], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="observability", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- observability.logging ---
    leaf(f, "observability.logging.app", "observability.logging", "logging_operation", "应用日志", "Application Logging",
         "写入应用级日志并控制级别。", ['Log / Logger / hilog'], ['系统日志见 system'],
         B(('Log', 'https://developer.android.com/reference/android/util/Log'), ('Logger / OSLog', 'https://developer.apple.com/documentation/os/logging', 'framework'), ('hilog', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hilog')), {'disposition': 'kept', 'sources': ['observability.logging.app']}, level="L3", privacy="none")
    leaf(f, "observability.logging.system", "observability.logging", "logging_operation", "系统日志读取", "System Log Read",
         "读取或订阅系统日志缓冲。", ['logcat read'], ['应用写入见 app'],
         B(('logcat', 'https://developer.android.com/tools/logcat', 'guide'), None, ('hilog', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hilog')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.logging.structured", "observability.logging", "logging_operation", "结构化事件日志", "Structured Event Logging",
         "写入结构化诊断或分析事件。", ['structured events'], ['普通日志见 app'],
         B(('EventLog', 'https://developer.android.com/reference/android/util/EventLog'), ('Logger', 'https://developer.apple.com/documentation/os/logger', 'struct'), ('hilog', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hilog')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.logging.native", "observability.logging", "logging_operation", "Native日志", "Native Logging",
         "在原生代码中写入日志。", ['__android_log / os_log'], ['应用层见 app'],
         B(('NDK logging', 'https://developer.android.com/ndk/reference/group/logging', 'guide'), ('os_log', 'https://developer.apple.com/documentation/os/logging', 'framework'), ('HiLog C', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hilog')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.logging.watcher", "observability.logging", "logging_operation", "日志监听", "Log Watcher",
         "监听日志流并回调处理。", ['log watcher'], ['写入见 app'],
         B(None, None, ('hilog', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hilog')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.logging.viewer", "observability.logging", "logging_operation", "日志查看器接入", "Log Viewer Integration",
         "接入系统或 IDE 日志查看能力。", ['log viewer'], ['读取见 system'],
         B(('Logcat', 'https://developer.android.com/tools/logcat', 'guide'), ('Console', 'https://developer.apple.com/documentation/xcode', 'guide'), ('HiLog', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- observability.crash ---
    leaf(f, "observability.crash.report", "observability.crash", "crash_operation", "崩溃报告生成", "Crash Report Generation",
         "生成并上报应用崩溃报告。", ['crash report'], ['卡死见 freeze'],
         B(('ApplicationExitInfo', 'https://developer.android.com/reference/android/app/ApplicationExitInfo'), ('MetricKit crash diagnostics', 'https://developer.apple.com/documentation/metrickit', 'framework'), ('ErrorManager', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-errormanager')), {'disposition': 'kept', 'sources': ['observability.crash.report']}, level="L3", privacy="none")
    leaf(f, "observability.crash.native", "observability.crash", "crash_operation", "Native崩溃分析", "Native Crash Analysis",
         "捕获并解析 native 崩溃堆栈。", ['tombstone / crashlytics native'], ['JS 崩溃见 js'],
         B(('Tombstone', 'https://source.android.com/docs/core/tests/debug', 'guide'), ('Crash Reports', 'https://developer.apple.com/documentation/xcode/examining-the-fields-in-a-crash-report', 'guide'), ('Faultlogger', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/faultlogger')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.crash.js", "observability.crash", "crash_operation", "脚本崩溃分析", "Script Crash Analysis",
         "捕获 JS/ArkTS 未处理异常。", ['JS exception'], ['native 见 native'],
         B(None, None, ('ErrorManager', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-errormanager')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.crash.freeze", "observability.crash", "crash_operation", "应用卡死检测", "App Freeze Detection",
         "检测 ANR/应用冻结并生成报告。", ['ANR / freeze'], ['崩溃见 report'],
         B(('ANR', 'https://developer.android.com/topic/performance/vitals/anr', 'guide'), ('Watchdog', 'https://developer.apple.com/documentation/xcode', 'guide'), ('HiCollie', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hicollie-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.crash.event_subscribe", "observability.crash", "crash_operation", "崩溃事件订阅", "Crash Event Subscribe",
         "订阅进程退出或崩溃事件。", ['exit/crash subscribe'], ['报告见 report'],
         B(('ActivityManager.AppExit', 'https://developer.android.com/reference/android/app/ApplicationExitInfo'), ('MetricKit', 'https://developer.apple.com/documentation/metrickit', 'framework'), ('ErrorManager', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-errormanager')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.crash.fault_rules", "observability.crash", "crash_operation", "故障检测规则", "Fault Detection Rules",
         "配置故障检测规则与阈值。", ['fault rules'], ['卡死见 freeze'],
         B(None, None, ('Faultlogger', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/faultlogger')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.crash.third_party", "observability.crash", "crash_operation", "第三方崩溃上报接入", "Third-Party Crash Reporting",
         "接入第三方崩溃采集 SDK 的系统侧约束入口。", ['third-party crash SDK hooks'], ['系统报告见 report'],
         B(('Firebase Crashlytics hooks', 'https://firebase.google.com/docs/crashlytics', 'guide'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- observability.perf ---
    leaf(f, "observability.perf.app_launch", "observability.perf", "perf_operation", "启动性能", "App Launch Performance",
         "测量冷/热启动耗时与阶段。", ['startup tracing'], ['帧率见 frame'],
         B(('App Startup', 'https://developer.android.com/topic/performance/vitals/launch-time', 'guide'), ('os_signpost launch', 'https://developer.apple.com/documentation/os/logging', 'framework'), ('AppStartup', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.perf.frame", "observability.perf", "perf_operation", "帧率与卡顿", "Frame Rate and Jank",
         "采集帧时长与卡顿指标。", ['jank / frame metrics'], ['启动见 app_launch'],
         B(('FrameMetrics', 'https://developer.android.com/reference/android/view/FrameMetrics'), ('MetricKit hang diagnostics', 'https://developer.apple.com/documentation/metrickit', 'framework'), ('HiPerf', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiperf')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.perf.cpu_memory", "observability.perf", "perf_operation", "CPU与内存采样", "CPU and Memory Sampling",
         "采样 CPU、内存占用与泄漏线索。", ['cpu/mem sample'], ['追踪见 tracing'],
         B(('Debug.MemoryInfo', 'https://developer.android.com/reference/android/os/Debug.MemoryInfo'), ('MetricKit', 'https://developer.apple.com/documentation/metrickit', 'framework'), ('Hidebug', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.perf.detection", "observability.perf", "perf_operation", "性能问题检测", "Performance Issue Detection",
         "自动检测主线程阻塞等性能问题。", ['StrictMode / performance detector'], ['帧率见 frame'],
         B(('StrictMode', 'https://developer.android.com/reference/android/os/StrictMode'), ('Main Thread Checker', 'https://developer.apple.com/documentation/xcode', 'guide'), ('HiChecker', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hichecker-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.perf.baseline_profile", "observability.perf", "perf_operation", "基线配置文件", "Baseline Profiles",
         "生成与应用启动/热点基线配置。", ['Baseline Profiles'], ['启动测量见 app_launch'],
         B(('Baseline Profiles', 'https://developer.android.com/topic/performance/baselineprofiles/overview', 'guide'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.perf.benchmark", "observability.perf", "perf_operation", "微宏观基准测试", "Micro Macro Benchmark",
         "运行微基准与宏观基准测试。", ['Benchmark'], ['线上指标见 metrics'],
         B(('Benchmark', 'https://developer.android.com/topic/performance/benchmarking/benchmarking-overview', 'guide'), ('XCTest measure', 'https://developer.apple.com/documentation/xctest', 'framework'), ('Hypium perf', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.perf.mem_leak", "observability.perf", "perf_operation", "内存泄漏分析", "Memory Leak Analysis",
         "检测与分析内存泄漏。", ['leak detection'], ['内存采样见 cpu_memory'],
         B(('LeakCanary hooks / MAT', 'https://developer.android.com/topic/performance/memory', 'guide'), ('Memgraph / Instruments', 'https://developer.apple.com/documentation/xcode', 'guide'), ('Hidebug', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- observability.metrics ---
    leaf(f, "observability.metrics.runtime", "observability.metrics", "metrics_operation", "运行时指标套件", "Runtime Metrics Suite",
         "采集能耗、挂起、磁盘等运行时指标。", ['MetricKit / Jetpack Metrics'], ['崩溃诊断见 crash'],
         B(('JankStats / metrics', 'https://developer.android.com/topic/performance/jankstats', 'guide'), ('MetricKit', 'https://developer.apple.com/documentation/metrickit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.metrics.custom", "observability.metrics", "metrics_operation", "自定义业务指标", "Custom Business Metrics",
         "上报自定义计数/计时指标。", ['custom metrics'], ['系统指标见 runtime'],
         B(('Firebase Performance API', 'https://firebase.google.com/docs/perf-mon', 'guide'), ('MetricKit MXMetricPayload', 'https://developer.apple.com/documentation/metrickit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.metrics.payload_subscribe", "observability.metrics", "metrics_operation", "指标载荷订阅", "Metrics Payload Subscribe",
         "订阅系统定期投递的指标载荷。", ['MXMetricManager'], ['自定义见 custom'],
         B(None, ('MXMetricManager', 'https://developer.apple.com/documentation/metrickit/mxmetricmanager', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.metrics.energy", "observability.metrics", "metrics_operation", "能耗指标", "Energy Metrics",
         "采集应用能耗相关指标。", ['energy metrics'], ['CPU 采样见 perf'],
         B(('BatteryHistorian hooks', 'https://developer.android.com/topic/performance/power', 'guide'), ('MXCPUMetric', 'https://developer.apple.com/documentation/metrickit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.metrics.state_report", "observability.metrics", "metrics_operation", "指标状态上报", "Metrics Status Reporting",
         "向系统或服务上报指标采集状态。", ['metrics status'], ['载荷订阅见 payload_subscribe'],
         B(None, ('MetricKit', 'https://developer.apple.com/documentation/metrickit', 'framework'), ('HiSysEvent', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hisysevent')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- observability.tracing ---
    leaf(f, "observability.tracing.sections", "observability.tracing", "tracing_operation", "代码段追踪", "Code Section Tracing",
         "在关键代码段打点生成调用链。", ['Trace.beginSection / os_signpost'], ['系统 trace 见 system_trace'],
         B(('android.os.Trace', 'https://developer.android.com/reference/android/os/Trace'), ('os_signpost', 'https://developer.apple.com/documentation/os/logging', 'framework'), ('HiTraceMeter', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracemeter')), {'disposition': 'renamed_from', 'sources': ['observability.perf.trace']}, level="L3", privacy="none")
    leaf(f, "observability.tracing.system_trace", "observability.tracing", "tracing_operation", "系统Trace采集", "System Trace Capture",
         "采集系统级 systrace/hitrace 数据。", ['Perfetto / hitrace'], ['应用打点见 sections'],
         B(('Perfetto', 'https://developer.android.com/topic/performance/tracing', 'guide'), ('Instruments', 'https://developer.apple.com/documentation/xcode', 'guide'), ('HiTrace', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitrace')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.tracing.distributed", "observability.tracing", "tracing_operation", "跨设备追踪关联", "Cross-Device Trace Correlation",
         "关联跨设备或跨进程的追踪上下文。", ['distributed trace id'], ['本机段见 sections'],
         B(None, None, ('HiTraceId', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracechain')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.tracing.async_spans", "observability.tracing", "tracing_operation", "异步跨度追踪", "Async Span Tracing",
         "追踪异步任务起止跨度。", ['async sections'], ['同步段见 sections'],
         B(('Trace.asyncTraceBegin', 'https://developer.android.com/reference/android/os/Trace'), ('os_signpost event', 'https://developer.apple.com/documentation/os/logging', 'framework'), ('HiTraceMeter', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracemeter')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "observability.tracing.deep_recording", "observability.tracing", "tracing_operation", "深度录制诊断", "Deep Recording Diagnostics",
         "启动深度录制以捕获难复现性能问题。", ['deep recording'], ['常规 trace 见 system_trace'],
         B(None, ('os_signpost', 'https://developer.apple.com/documentation/os/logging', 'framework'), ('Deep recording', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitrace')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")


    leaf(f, "observability.logging.redaction", "observability.logging", "logging_operation", "日志脱敏", "Log Redaction",
         "对敏感字段进行日志脱敏处理入口。", ["redaction"], ["结构化见 structured"],
         B(("Log", "https://developer.android.com/reference/android/util/Log"),
           ("Logger privacy", "https://developer.apple.com/documentation/os/logging", "framework"),
           ("hilog", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hilog")))
    leaf(f, "observability.crash.breadcrumb", "observability.crash", "crash_operation", "崩溃面包屑", "Crash Breadcrumbs",
         "在崩溃前记录用户操作面包屑。", ["breadcrumbs"], ["报告见 report"],
         B(("ApplicationExitInfo", "https://developer.android.com/reference/android/app/ApplicationExitInfo"),
           ("MetricKit", "https://developer.apple.com/documentation/metrickit", "framework"), None))
    leaf(f, "observability.perf.network_timing", "observability.perf", "perf_operation", "网络耗时剖析", "Network Timing Profiling",
         "采集请求阶段耗时用于性能分析。", ["network timing"], ["追踪见 tracing"],
         B(("Network Insight", "https://developer.android.com/topic/performance/networkinsight", "guide"),
           ("URLSessionTaskMetrics", "https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics", "class"), None))
    leaf(f, "observability.perf.rendering", "observability.perf", "perf_operation", "渲染性能采样", "Rendering Performance Sampling",
         "采样 GPU/渲染管线性能。", ["GPU rendering"], ["帧率见 frame"],
           B(("Profile GPU Rendering", "https://developer.android.com/topic/performance/rendering", "guide"),
             ("Metal System Trace", "https://developer.apple.com/documentation/xcode", "guide"),
             ("HiPerf", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiperf")))
    leaf(f, "observability.metrics.disk_io", "observability.metrics", "metrics_operation", "磁盘IO指标", "Disk IO Metrics",
         "采集磁盘读写相关运行指标。", ["disk IO metrics"], ["运行时指标见 runtime"],
         B(None, ("MetricKit", "https://developer.apple.com/documentation/metrickit", "framework"),
           ("HiSysEvent", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hisysevent")))
    leaf(f, "observability.metrics.hang_diagnostic", "observability.metrics", "metrics_operation", "挂起诊断指标", "Hang Diagnostic Metrics",
         "采集主线程挂起诊断指标载荷。", ["hang diagnostics"], ["卡死见 crash.freeze"],
         B(None, ("MXHangDiagnostic", "https://developer.apple.com/documentation/metrickit", "framework"), None))
    leaf(f, "observability.tracing.flow_events", "observability.tracing", "tracing_operation", "流式事件追踪", "Flow Event Tracing",
         "关联生产者-消费者流式事件。", ["flow events"], ["代码段见 sections"],
         B(("Trace", "https://developer.android.com/reference/android/os/Trace"),
           ("os_signpost", "https://developer.apple.com/documentation/os/logging", "framework"),
           ("HiTrace", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitrace")))
    leaf(f, "observability.tracing.export", "observability.tracing", "tracing_operation", "追踪导出", "Trace Export",
         "导出 trace 文件供外部分析。", ["trace export"], ["系统采集见 system_trace"],
         B(("Perfetto", "https://developer.android.com/topic/performance/tracing", "guide"),
           ("Instruments", "https://developer.apple.com/documentation/xcode", "guide"),
           ("HiTrace", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitrace")))

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("observability", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
