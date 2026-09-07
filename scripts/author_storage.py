#!/usr/bin/env python3
"""Author the storage domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "storage_capability_family"


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "storage", parent=None, level="L1",
        zh="数据与存储", en="Data and Storage",
        definition="应用沙箱与用户文件访问、本地库/键值、端云同步、备份归档、共享与静态加密等数据持久化能力。",
        includes=["文件访问、数据库、键值、云同步、备份、归档、共享、加密、索引、文档、类型标识"],
        excludes=["网络传输见 network", "安全密钥原语见 security.crypto", "分布式跨端 Continuity 见 distributed"],
        legacy={"disposition": "kept", "sources": ["storage"]},
    ))

    l2 = [
        ("storage.file_access", "文件访问", "File Access",
         "应用沙箱、系统选择器/SAF 与用户可见文件的受控读写。",
         ["沙箱、选择器、持久授权、媒体库、容量查询"], ["加密见 storage.encryption"], []),
        ("storage.db", "关系数据库", "Relational Database",
         "本地关系型结构化存储与 ORM/迁移。",
         ["SQLite、ORM、事务迁移"], ["键值见 storage.kv"], ["storage.db"]),
        ("storage.kv", "键值存储", "Key-Value Storage",
         "轻量偏好、异步键值与可复制键值持久化。",
         ["Preferences、DataStore、复制键值"], ["关系库见 storage.db"], ["storage.kv"]),
        ("storage.cloud", "云端同步存储", "Cloud Sync Storage",
         "与账号绑定的端云记录/对象同步（能力并集，非平台品牌并列）。",
         ["记录同步、对象存储、离线缓存"], ["本地备份见 storage.backup"], ["storage.cloud"]),
        ("storage.backup", "备份与迁移", "Backup and Migration",
         "应用数据自动备份、恢复与设备迁移。",
         ["自动备份、恢复、迁移"], ["端云实时同步见 storage.cloud.sync"], []),
        ("storage.archive", "归档与压缩", "Archive and Compression",
         "流式压缩解压与归档打包。",
         ["压缩、归档流"], ["文档渲染见 storage.document"], []),
        ("storage.sharing", "跨应用数据共享", "Cross-App Data Sharing",
         "向其他应用暴露或消费结构化数据与文件入口。",
         ["内容提供者、文件提供者、数据共享扩展"], ["系统分享面板见 interop"], []),
        ("storage.encryption", "静态数据加密", "At-Rest Encryption",
         "文件/库静态加密与密钥库支持的加密文件容器。",
         ["文件保护、库加密、密钥库加密文件"], ["密钥生成见 security.crypto.keystore"], []),
        ("storage.search_index", "内容搜索索引", "Search Index",
         "将应用内容编入系统或本地可检索索引。",
         ["应用搜索索引、系统索引贡献"], ["全文关系查询见 storage.db"], []),
        ("storage.document", "文档处理", "Document Processing",
         "PDF 等文档的预览、渲染与基础编辑。",
         ["PDF 预览/表单、系统文件预览"], ["纯文件读写见 storage.file_access"], []),
        ("storage.type_id", "数据类型标识", "Type Identification",
         "统一类型标识与 MIME/扩展名识别。",
         ["UTI/UTType、MIME"], ["文件打开见 storage.file_access"], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="storage", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- file_access ---
    f.append(feature(
        "storage.sandbox", parent="storage.file_access", level="L3",
        zh="应用沙箱文件", en="App Sandbox Files",
        definition="仅本应用可访问的私有、缓存与临时文件空间。",
        includes=["私有目录、缓存、临时"],
        excludes=["用户可见文件见 picker/media_store"],
        sibling_axis="file_access_scope",
        legacy={"disposition": "kept", "sources": ["storage.sandbox"]},
    ))
    f.append(feature(
        "storage.user_files", parent="storage.file_access", level="L3",
        zh="用户文件受控访问", en="User File Access",
        definition="通过选择器、SAF/媒体库访问用户可见文档与媒体。",
        includes=["选择器、持久授权、媒体库"],
        excludes=["沙箱私有目录见 storage.sandbox"],
        sibling_axis="file_access_scope",
        legacy={"disposition": "kept", "sources": ["storage.user_files"]},
    ))
    f.append(feature(
        "storage.file_access.stats", parent="storage.file_access", level="L3",
        zh="存储容量与文件系统统计", en="Storage Volume Statistics",
        definition="查询可用空间、用量与文件系统统计信息。",
        includes=["StatFs/statvfs、用量"],
        excludes=["文件读写本身"],
        sibling_axis="file_access_scope",
        granularity="atomic",
        bindings=merge_bindings(
            A("StatFs", "https://developer.android.com/reference/android/os/StatFs"),
            I("URL.resourceValues", "https://developer.apple.com/documentation/foundation/url/resourcevalues(forkeys:)", "method"),
            H("@ohos.file.statvfs", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-statvfs"),
        ),
    ))
    f.append(feature(
        "storage.file_access.native_io", parent="storage.file_access", level="L3",
        zh="Native文件IO", en="Native File I/O",
        definition="原生层打开/读写文件及 URI 与路径转换。",
        includes=["C/Native FileIO、URI 转换"],
        excludes=["ArkTS/Java 高层文件 API"],
        sibling_axis="file_access_scope",
        granularity="atomic",
        bindings=merge_bindings(
            pending("android", "通常经 NDK/标准 POSIX，待核统一入口"),
            I("open", "https://developer.apple.com/documentation/kernel/3383352-open", "function"),
            H("OH_FileIO", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileio"),
        ),
    ))
    f.append(feature(
        "storage.file_access.watch", parent="storage.file_access", level="L3",
        zh="目录变更监视", en="Directory Change Watching",
        definition="监视目录或文件树变更事件。",
        includes=["FileObserver、DispatchSource、file watcher"],
        excludes=["数据库变更见 storage.db.observe"],
        sibling_axis="file_access_scope",
        granularity="atomic",
        bindings=merge_bindings(
            A("FileObserver", "https://developer.android.com/reference/android/os/FileObserver"),
            I("DispatchSource.FileSystemObject",
              "https://developer.apple.com/documentation/dispatch/dispatchsource/3333204-makesource", "method"),
            pending("harmonyos"),
        ),
    ))
    f.append(feature(
        "storage.file_access.scoped_storage", parent="storage.file_access", level="L3",
        zh="分区存储合规访问", en="Scoped Storage Access",
        definition="在分区存储策略下访问应用可见的共享集合与媒体。",
        includes=["scoped storage、应用专属外部目录"],
        excludes=["选择器授权见 user_files.picker"],
        sibling_axis="file_access_scope",
        granularity="atomic",
        bindings=merge_bindings(
            A("Scoped storage", "https://developer.android.com/about/versions/11/privacy/storage", "guide"),
            pending("ios", "沙箱模型本身即隔离"),
            H("user file access", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-overview"),
        ),
    ))

    for fid, parent, axis, zh, en, definition, includes, excludes, bindings, legacy in [
        ("storage.sandbox.private_files", "storage.sandbox", "sandbox_area",
         "私有文件读写", "Private File I/O",
         "在应用私有目录创建、读写与枚举文件。",
         ["filesDir/documentDirectory、读写"], ["缓存目录见 sandbox.cache"],
         merge_bindings(
             A("Context.getFilesDir", "https://developer.android.com/reference/android/content/Context#getFilesDir()"),
             I("FileManager", "https://developer.apple.com/documentation/foundation/filemanager", "class"),
             H("@ohos.file.fs", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs"),
         ), {"disposition": "kept", "sources": ["storage.sandbox.private_files"]}),
        ("storage.sandbox.cache", "storage.sandbox", "sandbox_area",
         "缓存目录", "Cache Directory",
         "写入可被系统回收的应用缓存目录。",
         ["cacheDir、cachesDirectory"], ["私有持久文件见 private_files"],
         merge_bindings(
             A("Context.getCacheDir", "https://developer.android.com/reference/android/content/Context#getCacheDir()"),
             I("cachesDirectory", "https://developer.apple.com/documentation/foundation/filemanager/1411145-urls", "property"),
             H("cacheDir", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory"),
         ), {"disposition": "new", "sources": []}),
        ("storage.sandbox.temp", "storage.sandbox", "sandbox_area",
         "临时目录", "Temporary Directory",
         "短期临时文件目录，进程或系统可清理。",
         ["temporaryDirectory"], ["缓存见 sandbox.cache"],
         merge_bindings(
             A("File.createTempFile", "https://developer.android.com/reference/java/io/File#createTempFile(java.lang.String,%20java.lang.String)"),
             I("temporaryDirectory", "https://developer.apple.com/documentation/foundation/filemanager/1411145-urls", "property"),
             H("tempDir", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory"),
         ), {"disposition": "new", "sources": []}),
        ("storage.user_files.picker", "storage.user_files", "user_file_channel",
         "文档与媒体选择器", "Document and Media Picker",
         "通过系统选择器选取或保存文档/照片/视频（含 SAF 入口）。",
         ["ACTION_OPEN_DOCUMENT、UIDocumentPicker、documentViewPicker"], ["持久授权见 persist_permission"],
         merge_bindings(
             A("ACTION_OPEN_DOCUMENT", "https://developer.android.com/guide/topics/providers/document-provider"),
             I("UIDocumentPickerViewController", "https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller", "class"),
             H("documentViewPicker", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker"),
         ), {"disposition": "kept", "sources": ["storage.user_files.picker"]}),
        ("storage.user_files.persist_permission", "storage.user_files", "user_file_channel",
         "目录持久访问授权", "Persistable Access Grant",
         "将用户授予的目录/URI 访问权持久化以便后续访问。",
         ["takePersistableUriPermission、persistPermission"], ["单次选择见 picker"],
         merge_bindings(
             A("ContentResolver.takePersistableUriPermission",
               "https://developer.android.com/reference/android/content/ContentResolver#takePersistableUriPermission(android.net.Uri,%20int)"),
             I("startAccessingSecurityScopedResource",
               "https://developer.apple.com/documentation/foundation/nsurl/1417051-startaccessingsecurityscopedreso", "method"),
             H("persistPermission", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-persistpermission"),
         ), {"disposition": "new", "sources": []}),
        ("storage.user_files.media_store", "storage.user_files", "user_file_channel",
         "媒体库与公共集合", "Media Store Collections",
         "读写系统媒体库/公共下载等集合中的条目。",
         ["MediaStore、PhotoKit 相册写入边界"], ["选择器面板见 picker"],
         merge_bindings(
             A("MediaStore", "https://developer.android.com/reference/android/provider/MediaStore"),
             I("PHAsset", "https://developer.apple.com/documentation/photokit/phasset", "class"),
             H("userFileManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-overview"),
         ), {"disposition": "new", "sources": []}),
        ("storage.user_files.save_panel", "storage.user_files", "user_file_channel",
         "系统保存面板", "System Save Panel",
         "拉起系统保存位置选择并写入用户指定位置。",
         ["CREATE_DOCUMENT、UIDocumentPicker 导出、SaveButton"], ["打开选择见 picker"],
         merge_bindings(
             A("ACTION_CREATE_DOCUMENT", "https://developer.android.com/reference/android/content/Intent#ACTION_CREATE_DOCUMENT"),
             I("UIDocumentPickerViewController", "https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller", "class"),
             H("SaveButton", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-savebutton"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent=parent, level="L4", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=axis, granularity="atomic",
            bindings=bindings, legacy=legacy,
        ))

    # --- database ---
    f.append(feature(
        "storage.db.relational", parent="storage.db", level="L3",
        zh="SQLite关系库", en="SQLite Relational Store",
        definition="基于 SQLite 的本地关系表创建、查询与事务。",
        includes=["SQLiteDatabase、RDB"],
        excludes=["ORM 映射见 storage.db.orm"],
        sibling_axis="db_model",
        bindings=merge_bindings(
            A("SQLiteDatabase", "https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase"),
            I("SQLite3", "https://developer.apple.com/documentation/sqlite3", "framework"),
            H("@ohos.data.relationalStore", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-relationalstore"),
        ),
        legacy={"disposition": "kept", "sources": ["storage.db.relational"]},
        granularity="atomic",
    ))
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("storage.db.orm", "对象关系映射", "Object-Relational Mapping",
         "以对象/模型声明方式映射关系表并持久化。",
         ["Room、Core Data/SwiftData、RDB 对象接口"], ["直接 SQL 见 relational"],
         merge_bindings(
             A("Room", "https://developer.android.com/training/data-storage/room", "library"),
             I("NSPersistentContainer", "https://developer.apple.com/documentation/coredata/nspersistentcontainer", "class"),
             H("relationalStore", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-rdb-store"),
         ), {"disposition": "new", "sources": []}),
        ("storage.db.transaction", "事务与批处理", "Transactions and Batch",
         "在事务边界内执行批量读写以保证一致性。",
         ["beginTransaction、batch"], ["单条 CRUD 见 relational"],
         merge_bindings(
             A("SQLiteDatabase.beginTransaction",
               "https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#beginTransaction()"),
             I("NSManagedObjectContext.perform",
               "https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506672-perform", "method"),
             H("executeBatch", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-batch-operations"),
         ), {"disposition": "new", "sources": []}),
        ("storage.db.migration", "模式迁移", "Schema Migration",
         "关系库版本升级时迁移表结构与数据。",
         ["Migration、轻量迁移"], ["首次建表见 relational"],
         merge_bindings(
             A("Migration", "https://developer.android.com/reference/androidx/room/migration/Migration", "class"),
             I("NSPersistentStoreDescription", "https://developer.apple.com/documentation/coredata/nspersistentstoredescription", "class"),
             H("RDB store version", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-rdb-store"),
         ), {"disposition": "new", "sources": []}),
        ("storage.db.observe", "变更观察", "Change Observation",
         "订阅查询结果或表数据变更通知。",
         ["InvalidationTracker、NSFetchedResultsController、结果集监听"], ["一次性查询见 relational"],
         merge_bindings(
             A("InvalidationTracker", "https://developer.android.com/reference/androidx/room/InvalidationTracker", "class"),
             I("NSFetchedResultsController", "https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller", "class"),
             H("on('dataChange')", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-relationalstore"),
         ), {"disposition": "new", "sources": []}),
        ("storage.db.fts", "全文检索表", "Full-Text Search Tables",
         "在关系库内建立全文索引并检索。",
         ["FTS 虚拟表"], ["系统内容索引见 storage.search_index"],
         merge_bindings(
             A("FTS", "https://developer.android.com/training/data-storage/room/defining-data#fts", "guide"),
             pending("ios", "SQLite FTS 扩展待核公开封装"),
             H("fullTextSearch", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-rdb-store"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent="storage.db", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="db_model",
            granularity="atomic", bindings=bindings, legacy=legacy,
        ))

    # --- kv ---
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("storage.kv.preferences", "偏好键值", "Preferences Key-Value",
         "小型配置类同步/轻量键值持久化。",
         ["SharedPreferences、UserDefaults、preferences"], ["异步 DataStore 见 datastore"],
         merge_bindings(
             A("SharedPreferences", "https://developer.android.com/reference/android/content/SharedPreferences"),
             I("UserDefaults", "https://developer.apple.com/documentation/foundation/userdefaults", "class"),
             H("@ohos.data.preferences", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-preferences"),
         ), {"disposition": "kept", "sources": ["storage.kv.preferences"]}),
        ("storage.kv.datastore", "异步事务键值", "Async Transactional Key-Value",
         "协程/流式事务性键值或小型 proto 偏好存储。",
         ["DataStore Preferences/Proto"], ["同步 Preferences 见 preferences"],
         merge_bindings(
             A("DataStore", "https://developer.android.com/topic/libraries/architecture/datastore", "library"),
             pending("ios", "无直接等价；UserDefaults/SwiftData 边界待核"),
             pending("harmonyos", "与 preferences 差异待核"),
         ), {"disposition": "new", "sources": []}),
        ("storage.kv.replicated", "可复制键值库", "Replicated Key-Value Store",
         "支持跨设备复制同步的键值数据库。",
         ["distributed KV、NSUbiquitousKeyValueStore 边界"], ["端云记录同步见 cloud.sync"],
         merge_bindings(
             pending("android"),
             I("NSUbiquitousKeyValueStore", "https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore", "class"),
             H("@ohos.data.distributedKVStore", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributedkvstore"),
         ), {"disposition": "new", "sources": []}),
        ("storage.kv.encrypted", "加密键值存储", "Encrypted Key-Value Store",
         "系统或库提供的加密键值容器。",
         ["EncryptedSharedPreferences、加密 preferences"], ["文件级加密见 storage.encryption"],
         merge_bindings(
             A("EncryptedSharedPreferences",
               "https://developer.android.com/reference/androidx/security/crypto/EncryptedSharedPreferences", "class"),
             pending("ios", "Keychain 见 security.secure_storage"),
             H("encrypted preferences", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences-store"),
         ), {"disposition": "new", "sources": []}),
        ("storage.kv.observe", "键值变更观察", "Key-Value Change Observation",
         "监听键值变更并响应更新。",
         ["OnSharedPreferenceChangeListener、KVO、preferences 监听"], ["写入见 preferences"],
         merge_bindings(
             A("OnSharedPreferenceChangeListener",
               "https://developer.android.com/reference/android/content/SharedPreferences.OnSharedPreferenceChangeListener"),
             I("UserDefaults.didChangeNotification",
               "https://developer.apple.com/documentation/foundation/userdefaults/1411087-didchangenotification", "property"),
             H("on('change')", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-preferences"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent="storage.kv", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="kv_model",
            granularity="atomic", bindings=bindings, legacy=legacy,
        ))

    # --- cloud (one sync capability, not brand-parallel) ---
    for fid, zh, en, definition, includes, excludes, bindings, legacy, related in [
        ("storage.cloud.sync", "端云记录同步", "Cloud Record Sync",
         "结构化记录在设备与账号云端之间的同步（含私有库/端云数据同步等实现路径的能力并集）。",
         ["记录 CRUD 同步、冲突处理入口"], ["对象文件见 cloud.object_store", "本地备份见 backup"],
         merge_bindings(
             A("Firebase Firestore", "https://firebase.google.com/docs/firestore", "guide"),
             I("CKContainer", "https://developer.apple.com/documentation/cloudkit/ckcontainer", "class"),
             H("data-sync", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-sync-of-cloud-db"),
         ), {"disposition": "merged_from", "sources": ["storage.cloud.records"]}, None),
        ("storage.cloud.object_store", "云对象存储", "Cloud Object Storage",
         "向账号云端上传/下载文件对象。",
         ["对象上传下载、元数据"], ["结构化记录见 cloud.sync"],
         merge_bindings(
             A("Firebase Storage", "https://firebase.google.com/docs/storage", "guide"),
             I("CKAsset", "https://developer.apple.com/documentation/cloudkit/ckasset", "class"),
             H("Cloud Disk Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/clouddisk-kit-overview", "guide"),
         ), {"disposition": "new", "sources": []}, None),
        ("storage.cloud.offline", "离线缓存与同步队列", "Offline Cache and Sync Queue",
         "在离线时缓存本地写入并在恢复网络后同步。",
         ["离线持久、同步队列"], ["在线同步见 cloud.sync"],
         merge_bindings(
             A("Firestore persistence", "https://firebase.google.com/docs/firestore/manage-data/enable-offline", "guide"),
             I("CKDatabase", "https://developer.apple.com/documentation/cloudkit/ckdatabase", "class"),
             H("cloud DB offline", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-sync-of-cloud-db"),
         ), {"disposition": "new", "sources": []}, None),
        ("storage.cloud.share", "云记录共享", "Cloud Record Sharing",
         "将云端记录共享给其他用户并管理共享权限。",
         ["共享根记录、参与者"], ["本机跨应用共享见 storage.sharing"],
         merge_bindings(
             pending("android"),
             I("CKShare", "https://developer.apple.com/documentation/cloudkit/ckshare", "class"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}, ["storage.sharing"]),
        ("storage.cloud.push_subscription", "云变更推送订阅", "Cloud Change Push Subscription",
         "订阅云端数据变更推送以触发本地刷新。",
         ["silent push / database subscription"], ["同步写入见 cloud.sync"],
         merge_bindings(
             pending("android"),
             I("CKDatabaseSubscription", "https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription", "class"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}, None),
    ]:
        f.append(feature(
            fid, parent="storage.cloud", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="cloud_capability",
            granularity="atomic", bindings=bindings, legacy=legacy, related=related,
        ))

    # --- backup ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("storage.backup.auto", "自动备份规则", "Automatic Backup Rules",
         "声明应用数据参与系统自动备份/排除规则。",
         ["Auto Backup、dataExtractionRules、备份扩展"], ["实时云同步见 cloud.sync"],
         merge_bindings(
             A("Auto Backup", "https://developer.android.com/guide/topics/data/autobackup", "guide"),
             I("Exclude from Backup", "https://developer.apple.com/documentation/foundation/file_system/excluding_files_from_backups", "guide"),
             H("backup restore", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore"),
         )),
        ("storage.backup.restore", "备份恢复", "Backup Restore",
         "从系统备份恢复应用数据。",
         ["restore 流程、BackupAgent"], ["自动纳入规则见 backup.auto"],
         merge_bindings(
             A("BackupAgent", "https://developer.android.com/reference/android/app/backup/BackupAgent"),
             pending("ios", "系统恢复流程，应用侧 API 有限"),
             H("restore", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore"),
         )),
        ("storage.backup.transfer", "设备迁移传输", "Device Transfer Migration",
         "在设备迁移场景传输应用数据。",
         ["device transfer、迁移通道"], ["日常备份见 backup.auto"],
         merge_bindings(
             A("Android Backup", "https://developer.android.com/identity/sign-in/device-accounts", "guide"),
             I("NSItemProvider transfer", "https://developer.apple.com/documentation/foundation/nsitemprovider", "class"),
             H("native backup", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-backup-and-restore"),
         )),
        ("storage.backup.key_value_backup", "键值备份代理", "Key-Value Backup Agent",
         "以键值助手形式向备份传输注册小型数据。",
         ["BackupAgentHelper、SharedPreferencesBackupHelper"], ["全量文件备份见 backup.auto"],
         merge_bindings(
             A("BackupAgentHelper", "https://developer.android.com/reference/android/app/backup/BackupAgentHelper"),
             pending("ios"), pending("harmonyos"),
         )),
    ]:
        f.append(feature(
            fid, parent="storage.backup", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="backup_role",
            granularity="atomic", bindings=bindings,
        ))

    # --- archive ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("storage.archive.compress", "流压缩解压", "Stream Compression",
         "对字节流执行通用压缩与解压。",
         ["zlib、Compression framework"], ["归档打包见 archive.pack"],
         merge_bindings(
             A("Deflater", "https://developer.android.com/reference/java/util/zip/Deflater"),
             I("Compression", "https://developer.apple.com/documentation/compression", "framework"),
             H("zlib", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-zlib"),
         )),
        ("storage.archive.pack", "归档打包解包", "Archive Pack and Unpack",
         "将多文件打包为归档或从归档解包。",
         ["zip/tar 归档流、Archive Kit"], ["单流压缩见 compress"],
         merge_bindings(
             A("ZipOutputStream", "https://developer.android.com/reference/java/util/zip/ZipOutputStream"),
             I("AppleArchive", "https://developer.apple.com/documentation/applearchive", "framework"),
             H("Archive Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/archive-buffer-compression-guidelines", "guide"),
         )),
        ("storage.archive.checksum", "归档完整性校验", "Archive Integrity Check",
         "计算或校验归档/文件校验和。",
         ["CRC、checksum"], ["密码学摘要见 security.crypto"],
         merge_bindings(
             A("CheckedInputStream", "https://developer.android.com/reference/java/util/zip/CheckedInputStream"),
             I("CRC32", "https://developer.apple.com/documentation/accelerate/crc32_t", "type"),
             pending("harmonyos"),
         )),
    ]:
        f.append(feature(
            fid, parent="storage.archive", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="archive_operation",
            granularity="atomic", bindings=bindings,
        ))

    # --- sharing ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("storage.sharing.content_provider", "内容提供者导出", "Content Provider Export",
         "通过内容提供者向其他应用暴露结构化数据或文件 URI。",
         ["ContentProvider、FileProvider"], ["系统分享 UI 见 interop"],
         merge_bindings(
             A("ContentProvider", "https://developer.android.com/guide/topics/providers/content-providers", "guide"),
             pending("ios", "App Group/File Provider 见 file_provider"),
             H("DataShareExtensionAbility", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-datashareextensionability"),
         )),
        ("storage.sharing.file_provider", "文件提供者扩展", "File Provider Extension",
         "向系统文件界面提供可浏览的虚拟文件系统入口。",
         ["DocumentTree、FileProvider extension"], ["一次性选择器见 user_files.picker"],
         merge_bindings(
             A("DocumentsProvider", "https://developer.android.com/reference/android/provider/DocumentsProvider"),
             I("NSFileProviderExtension", "https://developer.apple.com/documentation/fileprovider/nsfileproviderextension", "class"),
             pending("harmonyos"),
         )),
        ("storage.sharing.query", "跨应用数据查询", "Cross-App Data Query",
         "查询其他应用通过共享机制暴露的数据。",
         ["ContentResolver.query、DataShareHelper"], ["导出侧见 content_provider"],
         merge_bindings(
             A("ContentResolver.query", "https://developer.android.com/reference/android/content/ContentResolver#query(android.net.Uri,%20java.lang.String[],%20java.lang.String,%20java.lang.String[],%20java.lang.String)"),
             pending("ios"),
             H("DataShareHelper", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-dataShare"),
         )),
        ("storage.sharing.app_group", "应用组共享容器", "App Group Shared Container",
         "同一开发者应用组之间共享容器文件。",
         ["App Group container"], ["跨开发者共享见 content_provider"],
         merge_bindings(
             pending("android", "通常无 UID/共享用户 ID，待核"),
             I("containerURLForSecurityApplicationGroupIdentifier",
               "https://developer.apple.com/documentation/foundation/filemanager/1412643-containerurlforsecurityapplicati", "method"),
             pending("harmonyos"),
         )),
    ]:
        f.append(feature(
            fid, parent="storage.sharing", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="sharing_channel",
            granularity="atomic", bindings=bindings,
        ))

    # --- encryption ---
    for fid, zh, en, definition, includes, excludes, bindings, legacy in [
        ("storage.encryption.file_protection", "文件数据保护等级", "File Data Protection Class",
         "为文件指定随锁屏状态生效的数据保护等级。",
         ["NSFileProtection、文件级保护策略"], ["加密文件容器见 keystore_file"],
         merge_bindings(
             pending("android", "直接文件保护 API 有限，待核"),
             I("NSFileProtectionComplete", "https://developer.apple.com/documentation/foundation/nsfileprotectioncomplete", "constant"),
             H("数据加密", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-protection"),
         ), {"disposition": "new", "sources": []}),
        ("storage.encryption.keystore_file", "密钥库支持的加密文件", "Keystore-Backed Encrypted File",
         "使用系统密钥库密钥对文件流进行加解密读写。",
         ["EncryptedFile、密钥绑定文件流"], ["凭据条目见 security.secure_storage"],
         merge_bindings(
             A("EncryptedFile", "https://developer.android.com/reference/androidx/security/crypto/EncryptedFile", "class"),
             I("CryptoKit + FileHandle", "https://developer.apple.com/documentation/cryptokit", "framework"),
             H("文件加密", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-protection"),
         ), {"disposition": "new", "sources": []}),
        ("storage.encryption.db", "数据库加密", "Database Encryption",
         "对关系库文件启用静态加密。",
         ["SQLCipher/加密 RDB 入口"], ["表级权限非本节点"],
         merge_bindings(
             A("SupportFactory", "https://developer.android.com/reference/net/sqlcipher/database/SupportFactory", "class"),
             pending("ios", "SQLCipher/NSFileProtection 组合待核"),
             H("encrypt RDB", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-rdb-store"),
         ), {"disposition": "new", "sources": []}),
        ("storage.encryption.asset_store", "安全资产小数据存储", "Secure Asset Store",
         "口令/令牌等小块敏感资产的系统级加密存储。",
         ["Asset Store、钥匙串式小数据"], ["通用 Keystore 密钥见 security.crypto.keystore"],
         merge_bindings(
             A("EncryptedSharedPreferences",
               "https://developer.android.com/reference/androidx/security/crypto/EncryptedSharedPreferences", "class"),
             I("SecItemAdd", "https://developer.apple.com/documentation/security/1396431-secitemadd", "function"),
             H("@ohos.security.asset", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-security-asset"),
         ), {"disposition": "new", "sources": []}),
    ]:
        f.append(feature(
            fid, parent="storage.encryption", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="encryption_target",
            granularity="atomic", bindings=bindings, legacy=legacy,
            related=["security.crypto.keystore"] if "keystore" in fid or "asset" in fid else None,
        ))

    # --- search_index ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("storage.search_index.app_local", "应用本地搜索索引", "App-Local Search Index",
         "在应用内建立可查询的本地搜索索引。",
         ["AppSearch、Core Spotlight 应用内"], ["关系库 FTS 见 storage.db.fts"],
         merge_bindings(
             A("AppSearch", "https://developer.android.com/reference/androidx/appsearch/app/GlobalSearchSession", "class"),
             I("CSSearchableIndex", "https://developer.apple.com/documentation/corespotlight/cssearchableindex", "class"),
             pending("harmonyos"),
         )),
        ("storage.search_index.system_contribute", "向系统搜索贡献", "System Search Contribution",
         "将内容条目贡献给系统全局搜索。",
         ["AppSearch 全局、Core Spotlight"], ["应用内索引见 app_local"],
         merge_bindings(
             A("GlobalSearchSession", "https://developer.android.com/reference/androidx/appsearch/app/GlobalSearchSession", "class"),
             I("CSSearchableItem", "https://developer.apple.com/documentation/corespotlight/cssearchableitem", "class"),
             pending("harmonyos"),
         )),
        ("storage.search_index.query", "索引查询", "Index Query",
         "对已建立的搜索索引执行查询。",
         ["search、query"], ["建立索引见 app_local"],
         merge_bindings(
             A("SearchSpec", "https://developer.android.com/reference/androidx/appsearch/app/SearchSpec", "class"),
             I("CSSearchQuery", "https://developer.apple.com/documentation/corespotlight/cssearchquery", "class"),
             pending("harmonyos"),
         )),
    ]:
        f.append(feature(
            fid, parent="storage.search_index", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="search_index_role",
            granularity="atomic", bindings=bindings,
        ))

    # --- document ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("storage.document.pdf_view", "PDF渲染与表单", "PDF View and Forms",
         "渲染 PDF 页面并处理基础表单填写。",
         ["PDFView、PdfView"], ["PDF 生成转换见 pdf_mutate"],
         merge_bindings(
             A("PdfRenderer", "https://developer.android.com/reference/android/graphics/pdf/PdfRenderer"),
             I("PDFView", "https://developer.apple.com/documentation/pdfkit/pdfview", "class"),
             H("PdfView", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pdf-view"),
         )),
        ("storage.document.pdf_mutate", "PDF生成与编辑", "PDF Generate and Edit",
         "生成、合并、拆分或标注 PDF 文档。",
         ["PDF 生成、合并拆分、水印"], ["只读渲染见 pdf_view"],
         merge_bindings(
             A("PdfDocument", "https://developer.android.com/reference/android/graphics/pdf/PdfDocument"),
             I("PDFDocument", "https://developer.apple.com/documentation/pdfkit/pdfdocument", "class"),
             H("PDF Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-kit-overview", "guide"),
         )),
        ("storage.document.preview", "系统文件预览", "System File Preview",
         "调用系统预览能力展示常见文件类型。",
         ["Quick Look、Preview Kit"], ["PDF 专用渲染见 pdf_view"],
         merge_bindings(
             pending("android", "Intent VIEW / Print 边界待核"),
             I("QLPreviewController", "https://developer.apple.com/documentation/quicklook/qlpreviewcontroller", "class"),
             H("Preview Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-kit-overview", "guide"),
         )),
        ("storage.document.thumbnail", "文档缩略图", "Document Thumbnail",
         "为文档生成系统可用的缩略图。",
         ["QLThumbnailGenerator、文档缩略图"], ["完整预览见 preview"],
         merge_bindings(
             pending("android"),
             I("QLThumbnailGenerator", "https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator", "class"),
             pending("harmonyos"),
         )),
    ]:
        f.append(feature(
            fid, parent="storage.document", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="document_operation",
            granularity="atomic", bindings=bindings,
        ))

    # --- type_id ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("storage.type_id.uniform_type", "统一类型标识", "Uniform Type Identifier",
         "声明与识别统一类型标识（UTI/UTType）。",
         ["UTType、类型符合性"], ["MIME 映射见 mime"],
         merge_bindings(
             pending("android", "MIME/扩展名为主，UTI 无直接等价"),
             I("UTType", "https://developer.apple.com/documentation/uniformtypeidentifiers/uttype", "struct"),
             pending("harmonyos"),
         )),
        ("storage.type_id.mime", "MIME与扩展名识别", "MIME and Extension Mapping",
         "在 MIME 类型与文件扩展名之间映射识别。",
         ["MimeTypeMap、内容类型"], ["UTI 见 uniform_type"],
         merge_bindings(
             A("MimeTypeMap", "https://developer.android.com/reference/android/webkit/MimeTypeMap"),
             I("UTType.preferredMIMEType", "https://developer.apple.com/documentation/uniformtypeidentifiers/uttype/preferredmimetype", "property"),
             H("file mime", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs"),
         )),
        ("storage.type_id.declare", "类型声明导出", "Type Declaration Export",
         "向系统声明应用可打开或导出的文档类型。",
         ["intent-filter/CFBundleDocumentTypes、类型注册"], ["运行时识别见 uniform_type"],
         merge_bindings(
             A("intent-filter data", "https://developer.android.com/guide/components/intents-filters", "guide"),
             I("CFBundleDocumentTypes", "https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundledocumenttypes", "key"),
             H("skills file type", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file"),
         )),
    ]:
        f.append(feature(
            fid, parent="storage.type_id", level="L3", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis="type_id_role",
            granularity="atomic", bindings=bindings,
        ))

    # Mark L3 file_access branches that need bindings
    for node in f:
        if node["id"] in {"storage.sandbox", "storage.user_files"} and not node.get("bindings"):
            if node["id"] == "storage.sandbox":
                node["bindings"] = merge_bindings(
                    A("Context.getFilesDir", "https://developer.android.com/reference/android/content/Context#getFilesDir()"),
                    I("FileManager", "https://developer.apple.com/documentation/foundation/filemanager", "class"),
                    H("@ohos.file.fs", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs"),
                )
            else:
                node["bindings"] = merge_bindings(
                    A("Storage Access Framework", "https://developer.android.com/guide/topics/providers/document-provider", "guide"),
                    I("UIDocumentPickerViewController", "https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller", "class"),
                    H("documentViewPicker", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker"),
                )

    dedup = {}
    for node in f:
        dedup[node["id"]] = node
    return list(dedup.values())


def main():
    nodes = build()
    path = write_domain("storage", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
