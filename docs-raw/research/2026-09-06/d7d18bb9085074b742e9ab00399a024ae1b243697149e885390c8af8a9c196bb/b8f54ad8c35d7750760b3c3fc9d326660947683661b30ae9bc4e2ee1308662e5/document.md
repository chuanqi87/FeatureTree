# Background Tasks Kit

|操作|旧版本|新版本|d.ts文件|
|:----|:--|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|
|新增API|NA|类名：ContinuousTaskNotification； API声明：continuousTaskId?: number; 差异内容：continuousTaskId?: number;|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：backgroundTaskManager； API声明： interface ContinuousTaskCancelInfo 差异内容： interface ContinuousTaskCancelInfo|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelInfo； API声明：reason: ContinuousTaskCancelReason; 差异内容：reason: ContinuousTaskCancelReason;|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelInfo； API声明：id: number; 差异内容：id: number;|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：backgroundTaskManager； API声明：function on(type: 'continuousTaskCancel', callback: Callback\<ContinuousTaskCancelInfo\>): void; 差异内容：function on(type: 'continuousTaskCancel', callback: Callback\<ContinuousTaskCancelInfo\>): void;|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：backgroundTaskManager； API声明：function off(type: 'continuousTaskCancel', callback?: Callback\<ContinuousTaskCancelInfo\>): void; 差异内容：function off(type: 'continuousTaskCancel', callback?: Callback\<ContinuousTaskCancelInfo\>): void;|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：backgroundTaskManager； API声明： export enum ContinuousTaskCancelReason 差异内容： export enum ContinuousTaskCancelReason|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelReason； API声明：USER_CANCEL = 1 差异内容：USER_CANCEL = 1|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelReason； API声明：SYSTEM_CANCEL = 2 差异内容：SYSTEM_CANCEL = 2|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelReason； API声明：USER_CANCEL_REMOVE_NOTIFICATION = 3 差异内容：USER_CANCEL_REMOVE_NOTIFICATION = 3|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelReason； API声明：SYSTEM_CANCEL_DATA_TRANSFER_LOW_SPEED = 4 差异内容：SYSTEM_CANCEL_DATA_TRANSFER_LOW_SPEED = 4|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelReason； API声明：SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_USE_AVSESSION = 5 差异内容：SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_USE_AVSESSION = 5|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelReason； API声明：SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_RUNNING = 6 差异内容：SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_RUNNING = 6|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelReason； API声明：SYSTEM_CANCEL_AUDIO_RECORDING_NOT_RUNNING = 7 差异内容：SYSTEM_CANCEL_AUDIO_RECORDING_NOT_RUNNING = 7|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelReason； API声明：SYSTEM_CANCEL_NOT_USE_LOCATION = 8 差异内容：SYSTEM_CANCEL_NOT_USE_LOCATION = 8|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelReason； API声明：SYSTEM_CANCEL_NOT_USE_BLUETOOTH = 9 差异内容：SYSTEM_CANCEL_NOT_USE_BLUETOOTH = 9|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelReason； API声明：SYSTEM_CANCEL_NOT_USE_MULTI_DEVICE = 10 差异内容：SYSTEM_CANCEL_NOT_USE_MULTI_DEVICE = 10|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
|新增API|NA|类名：ContinuousTaskCancelReason； API声明：SYSTEM_CANCEL_USE_ILLEGALLY = 11 差异内容：SYSTEM_CANCEL_USE_ILLEGALLY = 11|api/@ohos.resourceschedule.backgroundTaskManager.d.ts|
