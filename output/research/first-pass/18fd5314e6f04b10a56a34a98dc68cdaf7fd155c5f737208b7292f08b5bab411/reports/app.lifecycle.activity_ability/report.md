# 界面组件生命周期 — 首轮初判

低可信、未经逐条独立精审；不是最新正式版支持确认，没有真机实测。

三平台均读到前台界面组件生命周期官方正文：Android Activity定义七回调、四状态与三个生命期，重建后经savedInstanceState/rememberSaveable自动恢复；iOS UIViewController以视图出现/消失回调为主，状态保留为opt-in(restorationIdentifier+恢复归档)；HarmonyOS UIAbility(仅Stage模型,API9+首批)为组件级四状态，页面加载在onWindowStageCreate，onSaveState仅限appRecovery故障场景。初判回调粒度与状态恢复触发条件存在结构性差异；iOS入口组件映射与三平台版本基线是主要缺口。

## 三平台初判

| 平台 | 文档信号 | 证据强弱 | 观察 | 真机需求 |
| --- | --- | --- | --- | --- |
| android | documented_mechanism | direct | Activity为前台界面组件：官方参考定义onCreate/onStart/onRestart/onResume/onPause/onStop/onDestroy回调、active/visible/stopped/destroyed四状态与整段/可见/前台三个生命期循环；onCreate提供先前冻结状态的Bundle；指南称Activity重建后状态自动恢复(Compose rememberSaveable)，并提及后台启动Activity受系统限制。 | recommended |
| ios | documented_mechanism | direct | UIViewController管理视图层级，视图懒加载(loadView/viewDidLoad)；可见性变化触发viewWillAppear/viewIsAppearing/viewDidAppear/viewWillDisappear/viewDidDisappear等回调；状态保留为opt-in：设置restorationIdentifier后系统可在应用转后台时要求编码，恢复按restorationClass→app delegate→既有对象→storyboard顺序重建视图控制器。 | recommended |
| harmonyos | documented_mechanism | direct | UIAbility为含UI应用组件(仅Stage模型,API9+首批)：组件级四状态Create/Foreground/Background/Destroy对应onCreate/onForeground/onBackground/onDestroy，页面加载在onWindowStageCreate；onCreate仅冷启动触发并携带launchParam(含上次退出原因)；onSaveState需配合appRecovery且当前仅APP_RECOVERY故障场景；onPrepareToTerminate(10+)需权限且仅PC/2in1/Tablet执行回调。 | recommended |

## android 条件与证据

适用范围：未固定API Level；所读为developer.android.com当前Activity参考与生命周期指南(Android系统SDK层,非AndroidX)，未核对文档声明的适用版本。
条件：Activity须在AndroidManifest.xml声明<activity>；onCreate必须实现；重写回调须调用superclass；onPause实现须快速返回，否则下一个Activity无法resume；后台启动Activity受系统限制(指南提及,细则未读)
缺口：未核对所读参考/指南适用的API Level与最低系统版本；onSaveInstanceState/onRestoreInstanceState具体契约原文段落未读，仅见指南概述；后台启动Activity限制的豁免条件与targetSDK关系未读；多窗口模式下生命周期回调时序未读
真机分类理由：生命周期回调时序、进程被杀后的实际状态恢复与厂商进程策略相关，静态文档不能验证运行时行为；建议后续真机验证，本轮仅分类不设计用例。

- [Activity](https://developer.android.com/reference/android/app/Activity)，Activity > Activity Lifecycle(状态与回调定义,186-201为回调签名代码块)，正文 115–202 行；获取 2026-09-05T10:15:53.163135+00:00；SHA 4260bd7d809e9944bf8c70f388036a3fc9040991269313a261f8ba2b7917c786。
- [Activity](https://developer.android.com/reference/android/app/Activity)，Activity > Activity Lifecycle 生命周期表(onCreate携带先前冻结状态Bundle;onPause killable性)，正文 207–213 行；获取 2026-09-05T10:15:53.163135+00:00；SHA 4260bd7d809e9944bf8c70f388036a3fc9040991269313a261f8ba2b7917c786。
- [The activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle)，Activity-lifecycle concepts(核心六回调onCreate/onStart/onResume/onPause/onStop/onDestroy)，正文 44–47 行；获取 2026-09-05T10:29:21.696442+00:00；SHA 2f2b84ad5abe5c4a16b1867701c006e534c5854e4f11eb2805c54fa1ad81b975。
- [The activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle)，Restore activity UI state using saved instance state(重建后自动恢复,rememberSaveable)，正文 521–527 行；获取 2026-09-05T10:29:21.696442+00:00；SHA 2f2b84ad5abe5c4a16b1867701c006e534c5854e4f11eb2805c54fa1ad81b975。

## ios 条件与证据

适用范围：Apple平台UIKit官方文档(正文提及iOS 8起旋转方法废弃改用viewWillTransition)；未读取各符号iOS availability元数据；未固定iOS版本。
条件：UIKit目录含多平台内容，iOS适用性需逐符号核对；状态保留为opt-in:需restorationIdentifier且恢复归档可用、app代理shouldRestoreApplicationState返回true；视图懒加载，首次访问view属性才加载或创建视图；界面旋转自iOS 8起经viewWillTransition(to:with:)报告
缺口：未读取各回调符号的iOS availability版本元数据；iOS前台入口组件归属(UISceneDelegate/UIApplicationDelegate与UIViewController分工)未在本包来源核对；SwiftUI场景官方推荐的状态恢复路径未读；状态保留在强制退出/系统回收下的行为未读
真机分类理由：状态保留/恢复归档的实际触发与前后台切换回调时序需真机验证；静态文档仅描述机制，本轮仅分类不设计用例。

- [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller)，UIViewController > Overview(视图控制器职责与管理视图层级)，正文 11–22 行；获取 2026-09-05T10:15:49.375266+00:00；SHA 09b50abbf514548df3ef74c97c2cd8acdca84666e910a2fd6decd541af593b8e。
- [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller)，Subclassing notes > Handle view-related notifications(出现/消失回调与状态转换)，正文 51–57 行；获取 2026-09-05T10:15:49.375266+00:00；SHA 09b50abbf514548df3ef74c97c2cd8acdca84666e910a2fd6decd541af593b8e。
- [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller)，Topics > Managing the view(view/loadView/viewDidLoad)，正文 128–152 行；获取 2026-09-05T10:15:49.375266+00:00；SHA 09b50abbf514548df3ef74c97c2cd8acdca84666e910a2fd6decd541af593b8e。
- [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller)，Support state preservation and restoration(restorationIdentifier转后台时编码)，正文 96–100 行；获取 2026-09-05T10:15:49.375266+00:00；SHA 09b50abbf514548df3ef74c97c2cd8acdca84666e910a2fd6decd541af593b8e。
- [About the UI restoration process](https://developer.apple.com/documentation/uikit/about-the-ui-restoration-process)，Recreate your view controllers(UIKit重建顺序:restorationClass→app delegate→既有对象→storyboard)，正文 15–26 行；获取 2026-09-05T11:22:03.716381+00:00；SHA 44abd4f5146b6ebba91b6563bd44442c1494fbfe2b3c54c668665753e204d90e。

## harmonyos 条件与证据

适用范围：华为HarmonyOS官方参考(developer.huawei.com,非OpenHarmony仓库)；模块首批API 9+，onPrepareToTerminate 10+、onWill/onDid前后台回调20+、isDestroyed 26.0.0；未固定HarmonyOS发行版与最新正式版基线。
条件：仅可在Stage模型下使用；onSaveState需enableAppRecovery(saveOccasion=SAVE_WHEN_ERROR)使能；onPrepareToTerminate需ohos.permission.PREPARE_APP_TERMINATE,仅PC/2in1/Tablet执行回调；onCreate仅冷启动触发,重复拉起走onNewWant(正文未读)；EmbeddedUIExtensionAbility仅多进程配置设备(2in1/Tablet)可用
缺口：未固定HarmonyOS最新正式版与API版本基线(任务version_baseline unresolved)；appRecovery恢复路径与wantParam回传到onCreate Want.parameters的细节未读；手机设备上onPrepareToTerminate不执行时的替代关闭流程未核对；onBackPressed/onContinue/onCollaborate等回调与状态恢复关系未读；ArkUI页面级生命周期不在本包来源范围,未读
真机分类理由：文档明示设备形态行为差异(手机不执行onPrepareToTerminate)与故障恢复触发条件，需真机验证实际执行差异；本轮仅分类不设计用例。

- [@ohos.app.ability.UIAbility (带界面的应用组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)，UIAbility生命周期状态(Create/Foreground/Background/Destroy四状态)，正文 11–20 行；获取 2026-09-05T10:26:49.555101+00:00；SHA 74f440e4185df41bd58e1b2bc35e042159f738daa09ea6380c01233f3c237c8f。
- [@ohos.app.ability.UIAbility (带界面的应用组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)，onCreate(仅冷启动触发;launchParam含启动原因与上次退出原因)，正文 57–74 行；获取 2026-09-05T10:26:49.555101+00:00；SHA 74f440e4185df41bd58e1b2bc35e042159f738daa09ea6380c01233f3c237c8f。
- [@ohos.app.ability.UIAbility (带界面的应用组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)，onWindowStageCreate(WindowStage创建后加载页面)，正文 91–105 行；获取 2026-09-05T10:26:49.555101+00:00；SHA 74f440e4185df41bd58e1b2bc35e042159f738daa09ea6380c01233f3c237c8f。
- [@ohos.app.ability.UIAbility (带界面的应用组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)，onSaveState(需配合appRecovery,当前仅支持APP_RECOVERY故障场景)，正文 636–653 行；获取 2026-09-05T10:26:49.555101+00:00；SHA 74f440e4185df41bd58e1b2bc35e042159f738daa09ea6380c01233f3c237c8f。
- [@ohos.app.ability.UIAbility (带界面的应用组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)，onPrepareToTerminate(需权限;仅PC/2in1和Tablet执行回调)，正文 743–758 行；获取 2026-09-05T10:26:49.555101+00:00；SHA 74f440e4185df41bd58e1b2bc35e042159f738daa09ea6380c01233f3c237c8f。
- [EmbeddedUIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/embeddeduiextensionability)，EmbeddedUIExtensionAbility > 约束限制与生命周期(仅多进程设备;六回调)，正文 17–28 行；获取 2026-09-04T09:35:09+00:00；SHA 2871ac26faaa67251d5b7538dcfe37e6a6d2327165084f78a043934b8e2a06c7。

## 待验证差异假设

- programming_model：假设(can)：三平台前台组件生命周期回调粒度结构性不同——Android Activity提供六/七个组件级可见性回调(onCreate/onStart/onResume/onPause/onStop/onDestroy)；iOS UIViewController为视图出现/消失回调(viewWillAppear等,视图懒加载经loadView/viewDidLoad)；HarmonyOS UIAbility组件级仅Create/Foreground/Background/Destroy四状态，页面加载移至onWindowStageCreate。；待核：iOS前台/后台切换时序实际由UISceneDelegate承担的部分未读，UIViewController作为'前台界面入口组件'对应物待确认；HarmonyOS ArkUI页面级生命周期与UIAbility回调的分工未在本包来源中；Android多窗口/分屏下回调时序与单窗口的差异待核。
- lifecycle_background：假设(can)：状态保存/恢复的触发条件不同——Android Activity重建时自动恢复先前冻结状态(onCreate的Bundle,Compose rememberSaveable免显式恢复逻辑)；iOS需opt-in(恢复归档存在且app代理shouldRestoreApplicationState返回true)才在启动过程中重建视图控制器；HarmonyOS onSaveState须先使能appRecovery且当前仅在APP_RECOVERY故障场景触发，非通用状态保存。；待核：Android onSaveInstanceState/onRestoreInstanceState契约原文段落未读，仅见指南概述；iOS系统因内存回收终止而非归档恢复时其余状态的去向未读；HarmonyOS非故障场景(系统回收/后台清理)是否存在其他状态保存机制未读。
- device_forms：假设(can)：HarmonyOS明示生命周期回调的设备形态条件——onPrepareToTerminate(10+)需权限且仅在PC/2in1/Tablet执行回调、其他设备不执行，EmbeddedUIExtensionAbility仅多进程设备(2in1/Tablet)可用；本轮所读Android Activity与iOS UIViewController生命周期文档未载明设备形态条件，两平台是否存在类似条件未证(不据此断言不存在)。；待核：Android/iOS在折叠屏、分屏等设备形态下的回调差异未检索，不能断言无设备条件；HarmonyOS手机上onPrepareToTerminate不执行时的关闭流程需真机核对；关闭拦截类回调(onPrepareToTerminate)是否属于本节点'生命周期回调与状态恢复'比较范围需精研时界定。

范围缺口：iOS'前台界面入口组件'映射未确认：本包绑定UIViewController,但UIKit前台生命周期由UIScene/UISceneDelegate与UIViewController分工承担，本包来源未覆盖UIScene；Android状态保存契约(onSaveInstanceState/ViewModel/SavedStateHandle)原文未读，仅见指南概述；HarmonyOS appRecovery恢复路径与ArkUI页面级生命周期原文未读；三平台最新正式版基线未固定(任务version_baseline unresolved),所读文档版本适用性待核；HarmonyOS来源为华为官网文档,未与OpenHarmony发行版分开核对

后续优先级：P1；存在高风险映射(iOS前台入口组件归属未确认、HarmonyOS onSaveState仅限故障恢复场景与Android/iOS通用恢复的映射)及未固定版本基线；该节点是app.lifecycle下核心比较叶子，需优先精研补读关键原文。

逐条引用及原文摘录见同目录 normalized.json。
