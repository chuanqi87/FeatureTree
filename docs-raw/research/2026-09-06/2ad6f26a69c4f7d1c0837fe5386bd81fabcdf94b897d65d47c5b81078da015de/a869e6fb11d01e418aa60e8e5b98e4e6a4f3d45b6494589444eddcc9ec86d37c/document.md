# Notification Kit

|操作|旧版本|新版本|d.ts文件|
|:-------|:-------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|
|新增错误码|类名：notificationManager； API声明：function setBadgeNumber(badgeNumber: number, callback: AsyncCallback\<void\>): void; 差异内容：NA|类名：notificationManager； API声明：function setBadgeNumber(badgeNumber: number, callback: AsyncCallback\<void\>): void; 差异内容：801|api/@ohos.notificationManager.d.ts|
|新增错误码|类名：notificationManager； API声明：function setBadgeNumber(badgeNumber: number): Promise\<void\>; 差异内容：NA|类名：notificationManager； API声明：function setBadgeNumber(badgeNumber: number): Promise\<void\>; 差异内容：801|api/@ohos.notificationManager.d.ts|
|新增错误码|类名：notificationManager； API声明：function openNotificationSettings(context: UIAbilityContext): Promise\<void\>; 差异内容：NA|类名：notificationManager； API声明：function openNotificationSettings(context: UIAbilityContext): Promise\<void\>; 差异内容：801|api/@ohos.notificationManager.d.ts|
|删除错误码|类名：notificationManager； API声明：function cancelAll(): Promise\<void\>; 差异内容：401|类名：notificationManager； API声明：function cancelAll(): Promise\<void\>; 差异内容：NA|api/@ohos.notificationManager.d.ts|
|删除错误码|类名：notificationManager； API声明：function getSlots(): Promise\<Array\<NotificationSlot\>\>; 差异内容：401|类名：notificationManager； API声明：function getSlots(): Promise\<Array\<NotificationSlot\>\>; 差异内容：NA|api/@ohos.notificationManager.d.ts|
|删除错误码|类名：notificationManager； API声明：function removeAllSlots(): Promise\<void\>; 差异内容：401|类名：notificationManager； API声明：function removeAllSlots(): Promise\<void\>; 差异内容：NA|api/@ohos.notificationManager.d.ts|
|删除错误码|类名：notificationManager； API声明：function isNotificationEnabled(): Promise\<boolean\>; 差异内容：401|类名：notificationManager； API声明：function isNotificationEnabled(): Promise\<boolean\>; 差异内容：NA|api/@ohos.notificationManager.d.ts|
|删除错误码|类名：notificationManager； API声明：function getActiveNotificationCount(): Promise\<number\>; 差异内容：401|类名：notificationManager； API声明：function getActiveNotificationCount(): Promise\<number\>; 差异内容：NA|api/@ohos.notificationManager.d.ts|
|删除错误码|类名：notificationManager； API声明：function getActiveNotifications(): Promise\<Array\<NotificationRequest\>\>; 差异内容：401|类名：notificationManager； API声明：function getActiveNotifications(): Promise\<Array\<NotificationRequest\>\>; 差异内容：NA|api/@ohos.notificationManager.d.ts|
|删除错误码|类名：notificationManager； API声明：function requestEnableNotification(): Promise\<void\>; 差异内容：401|类名：notificationManager； API声明：function requestEnableNotification(): Promise\<void\>; 差异内容：NA|api/@ohos.notificationManager.d.ts|
|删除错误码|类名：notificationManager； API声明：function isDistributedEnabled(): Promise\<boolean\>; 差异内容：401|类名：notificationManager； API声明：function isDistributedEnabled(): Promise\<boolean\>; 差异内容：NA|api/@ohos.notificationManager.d.ts|
|新增API|NA|类名：global； API声明：export interface NotificationIconButton 差异内容：export interface NotificationIconButton|api/notification/notificationContent.d.ts|
|起始版本有变化|类名：notificationManager； API声明：function isNotificationEnabled(callback: AsyncCallback\<boolean\>): void; 差异内容：9|类名：notificationManager； API声明：function isNotificationEnabled(callback: AsyncCallback\<boolean\>): void; 差异内容：11|api/@ohos.notificationManager.d.ts|
|起始版本有变化|类名：notificationManager； API声明：function isNotificationEnabled(): Promise\<boolean\>; 差异内容：9|类名：notificationManager； API声明：function isNotificationEnabled(): Promise\<boolean\>; 差异内容：11|api/@ohos.notificationManager.d.ts|
|起始版本有变化|类名：global； API声明：export enum NotificationFlagStatus 差异内容：8|类名：global； API声明：export enum NotificationFlagStatus 差异内容：11|api/notification/notificationFlags.d.ts|
|起始版本有变化|类名：NotificationFlagStatus； API声明：TYPE_NONE = 0 差异内容：8|类名：NotificationFlagStatus； API声明：TYPE_NONE = 0 差异内容：11|api/notification/notificationFlags.d.ts|
|起始版本有变化|类名：NotificationFlagStatus； API声明：TYPE_OPEN = 1 差异内容：8|类名：NotificationFlagStatus； API声明：TYPE_OPEN = 1 差异内容：11|api/notification/notificationFlags.d.ts|
|起始版本有变化|类名：NotificationFlagStatus； API声明：TYPE_CLOSE = 2 差异内容：8|类名：NotificationFlagStatus； API声明：TYPE_CLOSE = 2 差异内容：11|api/notification/notificationFlags.d.ts|
|接口新增可选属性|类名：global； API声明： 差异内容：NA|类名：NotificationRequest； API声明：updateOnly?: boolean; 差异内容：updateOnly?: boolean;|api/notification/notificationRequest.d.ts|
|新增导出符号|类名：global； API声明：export interface NotificationIconButton 差异内容：NA|类名：global； API声明： 差异内容：export interface NotificationIconButton|api/notification/notificationContent.d.ts|
