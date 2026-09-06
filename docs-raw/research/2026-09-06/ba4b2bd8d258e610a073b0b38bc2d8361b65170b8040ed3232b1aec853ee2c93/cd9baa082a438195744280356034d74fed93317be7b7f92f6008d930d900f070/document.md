# MDM Kit

|操作|旧版本|新版本|d.ts文件|
|:----|:--|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|
|新增API|NA|类名：securityManager； API声明：function setAppClipboardPolicy(admin: Want, tokenId: number, policy: ClipboardPolicy): void; 差异内容：function setAppClipboardPolicy(admin: Want, tokenId: number, policy: ClipboardPolicy): void;|api/@ohos.enterprise.securityManager.d.ts|
|新增API|NA|类名：securityManager； API声明：function getAppClipboardPolicy(admin: Want, tokenId?: number): string; 差异内容：function getAppClipboardPolicy(admin: Want, tokenId?: number): string;|api/@ohos.enterprise.securityManager.d.ts|
|新增API|NA|类名：securityManager； API声明： export enum ClipboardPolicy 差异内容： export enum ClipboardPolicy|api/@ohos.enterprise.securityManager.d.ts|
|新增API|NA|类名：ClipboardPolicy； API声明：DEFAULT = 0 差异内容：DEFAULT = 0|api/@ohos.enterprise.securityManager.d.ts|
|新增API|NA|类名：ClipboardPolicy； API声明：IN_APP = 1 差异内容：IN_APP = 1|api/@ohos.enterprise.securityManager.d.ts|
|新增API|NA|类名：ClipboardPolicy； API声明：LOCAL_DEVICE = 2 差异内容：LOCAL_DEVICE = 2|api/@ohos.enterprise.securityManager.d.ts|
|新增API|NA|类名：ClipboardPolicy； API声明：CROSS_DEVICE = 3 差异内容：CROSS_DEVICE = 3|api/@ohos.enterprise.securityManager.d.ts|
|新增API|NA|类名：systemManager； API声明： enum PolicyType 差异内容： enum PolicyType|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：PolicyType； API声明：DEFAULT = 0 差异内容：DEFAULT = 0|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：PolicyType； API声明：PROHIBIT = 1 差异内容：PROHIBIT = 1|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：PolicyType； API声明：UPDATE_TO_SPECIFIC_VERSION = 2 差异内容：UPDATE_TO_SPECIFIC_VERSION = 2|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：PolicyType； API声明：WINDOWS = 3 差异内容：WINDOWS = 3|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：PolicyType； API声明：POSTPONE = 4 差异内容：POSTPONE = 4|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明： export interface OtaUpdatePolicy 差异内容： export interface OtaUpdatePolicy|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：OtaUpdatePolicy； API声明：policyType: PolicyType; 差异内容：policyType: PolicyType;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：OtaUpdatePolicy； API声明：version: string; 差异内容：version: string;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：OtaUpdatePolicy； API声明：latestUpdateTime?: number; 差异内容：latestUpdateTime?: number;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：OtaUpdatePolicy； API声明：delayUpdateTime?: number; 差异内容：delayUpdateTime?: number;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：OtaUpdatePolicy； API声明：installStartTime?: number; 差异内容：installStartTime?: number;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：OtaUpdatePolicy； API声明：installEndTime?: number; 差异内容：installEndTime?: number;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明： export interface UpdatePackageInfo 差异内容： export interface UpdatePackageInfo|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：UpdatePackageInfo； API声明：version: string; 差异内容：version: string;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：UpdatePackageInfo； API声明：packages: Array\<Package\>; 差异内容：packages: Array\<Package\>;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：UpdatePackageInfo； API声明：description?: PackageDescription; 差异内容：description?: PackageDescription;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明： interface Package 差异内容： interface Package|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：Package； API声明：type: PackageType; 差异内容：type: PackageType;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：Package； API声明：path: string; 差异内容：path: string;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：Package； API声明：fd?: number; 差异内容：fd?: number;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明： enum PackageType 差异内容： enum PackageType|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：PackageType； API声明：FIRMWARE = 1 差异内容：FIRMWARE = 1|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明： interface PackageDescription 差异内容： interface PackageDescription|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：PackageDescription； API声明：notify?: NotifyDescription; 差异内容：notify?: NotifyDescription;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明： interface NotifyDescription 差异内容： interface NotifyDescription|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：NotifyDescription； API声明：installTips?: string; 差异内容：installTips?: string;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：NotifyDescription； API声明：installTipsDetail?: string; 差异内容：installTipsDetail?: string;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明： interface UpdateResult 差异内容： interface UpdateResult|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：UpdateResult； API声明：version: string; 差异内容：version: string;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：UpdateResult； API声明：status: UpdateStatus; 差异内容：status: UpdateStatus;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：UpdateResult； API声明：errorInfo: ErrorInfo; 差异内容：errorInfo: ErrorInfo;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明： enum UpdateStatus 差异内容： enum UpdateStatus|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：UpdateStatus； API声明：NO_UPDATE_PACKAGE = -4 差异内容：NO_UPDATE_PACKAGE = -4|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：UpdateStatus； API声明：UPDATE_WAITING = -3 差异内容：UPDATE_WAITING = -3|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：UpdateStatus； API声明：UPDATING = -2 差异内容：UPDATING = -2|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：UpdateStatus； API声明：UPDATE_FAILURE = -1 差异内容：UPDATE_FAILURE = -1|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：UpdateStatus； API声明：UPDATE_SUCCESS = 0 差异内容：UPDATE_SUCCESS = 0|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明： interface ErrorInfo 差异内容： interface ErrorInfo|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：ErrorInfo； API声明：code: number; 差异内容：code: number;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：ErrorInfo； API声明：message: string; 差异内容：message: string;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明：function setOtaUpdatePolicy(admin: Want, policy: OtaUpdatePolicy): void; 差异内容：function setOtaUpdatePolicy(admin: Want, policy: OtaUpdatePolicy): void;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明：function getOtaUpdatePolicy(admin: Want): OtaUpdatePolicy; 差异内容：function getOtaUpdatePolicy(admin: Want): OtaUpdatePolicy;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明：function notifyUpdatePackages(admin: Want, packageInfo: UpdatePackageInfo): Promise\<void\>; 差异内容：function notifyUpdatePackages(admin: Want, packageInfo: UpdatePackageInfo): Promise\<void\>;|api/@ohos.enterprise.systemManager.d.ts|
|新增API|NA|类名：systemManager； API声明：function getUpdateResult(admin: Want, version: string): Promise\<UpdateResult\>; 差异内容：function getUpdateResult(admin: Want, version: string): Promise\<UpdateResult\>;|api/@ohos.enterprise.systemManager.d.ts|
