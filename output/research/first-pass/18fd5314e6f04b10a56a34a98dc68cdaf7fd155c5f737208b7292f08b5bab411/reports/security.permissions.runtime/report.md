# 运行时权限请求 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到运行时向用户请求敏感权限的机制。Android 指南明示 API 23+ 设备上运行时权限须应用自行请求且先在 manifest 声明；iOS 由系统在首次访问受保护资源时弹窗，需 Info.plist 用途字符串，各框架提供 requestAuthorization 类 API；HarmonyOS 经 AtManager.requestPermissionsFromUser(API 9+，Stage 模型)拉起动态授权弹窗，拒绝后不可再弹。Android 实际请求 API 未在冻结来源中，iOS 版本适用性、HarmonyOS API 与发行版映射未核实，全部 low。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | 指南明示：运行时/特殊权限在 Android 6.0(API 23)+ 设备须应用自行请求；权限须先以 <uses-permission> 在 manifest 声明，可用 <uses-permission-sdk-23> 限定 API 23+ 设备。PackageManager 参考正文仅含 checkPermission、PERMISSION_GRANTED/DENIED 等查询接口，未见 requestPermissions 方法。 | recommended |
| ios | documented_mechanism | direct | 系统默认限制受保护资源，首次访问时自动弹系统提示并展示应用提供的用途字符串；缺失时访问失败甚至崩溃并被 App Review 拒绝。各框架提供专用授权 API（如 SFSpeechRecognizer.requestAuthorization），系统记录用户选择后不再弹窗。 | recommended |
| harmonyos | documented_mechanism | direct | @ohos.abilityAccessCtrl 提供 AtManager.requestPermissionsFromUser（API 9+）在运行时拉起动态授权弹窗申请 user_grant 权限并返回 PermissionRequestResult；用户拒绝后无法再次弹窗，可引导设置页或 requestPermissionOnSetting(API 12+)。仅限 Stage 模型，弹窗不可被遮挡。 | recommended |

## android 条件与证据

适用范围：文档条件：设备 Android 6.0 (API level 23) 或更高；未核实 targetSdk 影响及最新正式版 API Level 对应关系
条件：设备运行 Android 6.0 (API level 23) 或更高；权限须先在 manifest 以 <uses-permission> 声明；适用于运行时(危险)权限与特殊权限；normal/signature 安装时权限自动授予；请求流程指向 training/permissions/requesting（该正文未包含于冻结来源）
缺口：实际请求 API（Activity.requestPermissions/ActivityCompat.requestPermissions 及回调）正文未包含于冻结来源；绑定注记 PackageManager.requestPermissions 未在该参考正文出现，正文仅 checkPermission 等查询接口；拒绝后再请求与 rationale 机制未读到；targetSdk<23 等兼容行为与特殊权限流程未核实
真机分类理由：机制与 API 23+ 条件已有文档说明，但授权弹窗展示、拒绝后再请求路径等属系统运行时 UI 行为，确认最新手机正式版实际表现时建议真机验证；本轮为文档初判，未执行实测

- [Declare app permissions](https://developer.android.com/training/permissions/declaring)，Declare app permissions - 权限类型决定请求方式，API 23+ 须自行请求运行时权限，正文 9–21 行；获取 2026-09-05T10:38:29.447702+00:00；SHA 4a631a9a43f469928ac55d713444e4300950d028f777f87f04dd51991259ffd9。
- [Declare app permissions](https://developer.android.com/training/permissions/declaring)，Declare permissions by API level - <uses-permission-sdk-23> 限定支持运行时权限的设备，正文 111–117 行；获取 2026-09-05T10:38:29.447702+00:00；SHA 4a631a9a43f469928ac55d713444e4300950d028f777f87f04dd51991259ffd9。
- [Declare app permissions](https://developer.android.com/training/permissions/declaring)，Add declaration to app manifest - <uses-permission> 示例，正文 29–43 行；获取 2026-09-05T10:38:29.447702+00:00；SHA 4a631a9a43f469928ac55d713444e4300950d028f777f87f04dd51991259ffd9。
- [PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager)，PackageManager.checkPermission(String,String) 方法摘要行，正文 318–318 行；获取 2026-09-05T14:47:50.985988+00:00；SHA 344f24712bf349d9208150d3c5dde1f8800340c559cc83a5810f1e618aa61a7c。
- [PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager)，PERMISSION_DENIED/PERMISSION_GRANTED 常量摘要行，正文 272–273 行；获取 2026-09-05T14:47:50.985988+00:00；SHA 344f24712bf349d9208150d3c5dde1f8800340c559cc83a5810f1e618aa61a7c。

## ios 条件与证据

适用范围：已读 Apple 文章未标注具体 iOS 最低版本；符号级 availability 与最新 iOS 正式版适用性未核对
条件：Info.plist 须含对应用途字符串，缺失时访问可能失败/崩溃并被 App Review 拒绝；系统提示在应用首次访问受保护资源时自动触发；用户可随时在设置中更改授权，访问前应检查授权状态；部分资源还需另行声明 entitlement（文档提示，未展开）
缺口：是否存在统一权限请求入口未核实（本轮仅读到按框架分散的授权 API）；各受保护资源最低 iOS 版本与符号 availability 未核对；受保护资源完整清单未读取；已读文章未逐项区分 iOS 与其他 Apple 平台适用性
真机分类理由：提示触发时机、选择记忆与设置更改后的行为属系统运行时表现，文档已描述但确认最新 iOS 手机版本实际行为建议真机验证；本轮为文档初判，未执行实测

- [Requesting access to protected resources](https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources)，Provide a purpose string - 首次访问触发系统提示、purpose string 作用，正文 14–22 行；获取 2026-09-05T11:19:56.909063+00:00；SHA 4503d673a7fe8d82f74fd68baaa45adea4f78b95acadf676e6d2e2046682ba2d。
- [Requesting access to protected resources](https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources)，Check for authorization - 各框架提供专用授权检查/请求 API，正文 78–82 行；获取 2026-09-05T11:19:56.909063+00:00；SHA 4503d673a7fe8d82f74fd68baaa45adea4f78b95acadf676e6d2e2046682ba2d。
- [Requesting access to protected resources](https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources)，Reset authorization access - 系统记住选择不再提示，需重置才会再询问，正文 84–88 行；获取 2026-09-05T11:19:56.909063+00:00；SHA 4503d673a7fe8d82f74fd68baaa45adea4f78b95acadf676e6d2e2046682ba2d。
- [Asking Permission to Use Speech Recognition](https://developer.apple.com/documentation/speech/asking-permission-to-use-speech-recognition)，Request Authorization at First Use - requestAuthorization 异步请求并记录结果，正文 26–33 行；获取 2026-09-05T11:18:47.726445+00:00；SHA 52f53f447075b9f1afec19c07f87ca2ba04ad1460f64d60c27e1e96e075c5f74。
- [Asking Permission to Use Speech Recognition](https://developer.apple.com/documentation/speech/asking-permission-to-use-speech-recognition)，Add the Privacy Key to Your Info.plist File - 缺 NSSpeechRecognitionUsageDescription 将崩溃，正文 13–24 行；获取 2026-09-05T11:18:47.726445+00:00；SHA 52f53f447075b9f1afec19c07f87ca2ba04ad1460f64d60c27e1e96e075c5f74。

## harmonyos 条件与证据

适用范围：模块首批接口 API 8 起；requestPermissionsFromUser API 9+，元服务 API 12+，requestPermissionOnSetting API 12+；API version 与 HarmonyOS 手机发行版映射未核实
条件：权限须先在配置文件声明且属 user_grant 类；仅 Stage 模型，需 UIAbility/UIExtensionAbility 的 Context；onWindowStageCreate 中须待 loadContent/setUIContent 完成后再调用；每次访问受保护接口前须检查权限并调用 requestPermissionsFromUser，不持久化授权状态；系统权限弹窗不可被其他组件遮挡
缺口：API version 与 HarmonyOS 手机/平板发行版映射未核实，OpenHarmony 与 HarmonyOS 差异未核对；system_grant/manual_settings 等其余授权类型完整细节未读全；requestPermissionOnSetting/openPermissionOnSetting 正文仅部分读取；平板等设备形态条件未读取
真机分类理由：弹窗拉起、拒绝后再请求限制与设置引导属系统运行时行为，文档已描述但确认最新 HarmonyOS 手机版本表现建议真机验证；本轮为文档初判，未执行实测

- [@ohos.abilityAccessCtrl (程序访问控制管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl)，模块说明 - 权限三类划分与首批接口 API 8 起，正文 1–12 行；获取 2026-09-05T10:26:36.525665+00:00；SHA 4e29a359c4344a756e6a9468537d261788af4503521692e91638c2a67290edbe。
- [@ohos.abilityAccessCtrl (程序访问控制管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl)，AtManager.requestPermissionsFromUser^9+ - 拉起弹窗请求用户授权及拒绝后行为，正文 375–383 行；获取 2026-09-05T10:26:36.525665+00:00；SHA 4e29a359c4344a756e6a9468537d261788af4503521692e91638c2a67290edbe。
- [@ohos.abilityAccessCtrl (程序访问控制管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl)，requestPermissionsFromUser 模型约束 - 元服务 API 12、仅 Stage 模型、SystemCapability，正文 387–391 行；获取 2026-09-05T10:26:36.525665+00:00；SHA 4e29a359c4344a756e6a9468537d261788af4503521692e91638c2a67290edbe。
- [向用户申请授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)，约束与限制 - 拒绝后无法再弹窗、每次先检查、onWindowStageCreate 时序，正文 18–35 行；获取 2026-09-04T09:35:09+00:00；SHA e2db978cce7037f2ea078e550fc79e650db3085391c7fe439e0e2f156c9c38a3。
- [向用户申请授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)，开发步骤 - 运行时动态申请授权流程，正文 101–109 行；获取 2026-09-04T09:35:09+00:00；SHA e2db978cce7037f2ea078e550fc79e650db3085391c7fe439e0e2f156c9c38a3。

## 待验证差异假设

- programming_model：请求发起模型差异（假设）：iOS 文档描述系统在首次访问受保护资源时自动弹窗、授权 API 按框架分散（如 SFSpeechRecognizer.requestAuthorization）；Android 与 HarmonyOS 文档描述应用主动调用运行时请求接口（Android 指向运行时权限请求流程，HarmonyOS 为 requestPermissionsFromUser 传权限列表）。；待核：Android 实际请求 API 形态与回调模型未在冻结来源中读到，无法确认接口细节；iOS 是否存在统一权限请求入口未核实，需逐框架清点。
- permissions_privacy：拒绝后再请求路径差异（假设，iOS vs HarmonyOS）：HarmonyOS 明示拒绝后 requestPermissionsFromUser 无法再次拉起弹窗，须引导用户去系统设置或 requestPermissionOnSetting(API 12+)；iOS 系统记录选择后不再提示，重新询问需用户在设置更改或重置隐私设置。Android 侧冻结资料未记载该行为，暂不纳入本假设比较。；待核：Android 拒绝后再请求行为（rationale、设置引导）未在冻结来源核实；iOS 各框架再次调用请求 API 的实际表现（如定位的再询问选项）未逐框架核实。
- api_surface：请求前声明面差异（假设）：三平台均要求先静态声明再运行时请求——Android 在 manifest 用 <uses-permission>；HarmonyOS 在配置文件声明并关联目标对象；iOS 在 Info.plist 提供用户可读用途字符串，缺失时访问失败/崩溃且被 App Review 拒绝。已读文档范围内仅 iOS 明示强制用户可见说明文案。；待核：Android/HarmonyOS 是否有对应用户可见说明义务（商店审核等）未在冻结资料核实；iOS 用途字符串细则（长度、本地化）对三平台比较的影响未展开。

范围缺口：Android 实际运行时请求 API（Activity.requestPermissions/ActivityCompat/onRequestPermissionsResult）未包含于冻结来源；绑定注记 PackageManager.requestPermissions 未在该参考正文出现（正文仅 checkPermission 等查询接口）；Android targetSdk 对运行时权限行为的影响与特殊权限请求流程未读到；iOS 各受保护资源最低 iOS 版本与符号 availability 未核对，已读文章未标注具体 iOS 版本；HarmonyOS API version 与手机发行版映射未核实，OpenHarmony 与 HarmonyOS 差异未核对；特殊权限/仅设置页授权完整清单与平板设备形态条件未读取

后续优先级：P1；Android 绑定与正文不一致（PackageManager 无 requestPermissions），实际请求 API 与 targetSdk 条件未核实属高风险映射；iOS 版本适用性与 HarmonyOS API-发行版映射未固定，需优先精研

逐条引用及原文摘录见同目录 normalized.json。
