# ArkWeb

|操作|旧版本|新版本|d.ts文件|
|:----|:------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
|函数变更|类名：WebviewController； API声明：setScrollable(enable: boolean): void; 差异内容：NA|类名：WebviewController； API声明：setScrollable(enable: boolean, type?: ScrollType): void; 差异内容：type?: ScrollType|api/@ohos.web.webview.d.ts|
|新增API|NA|类名：webview； API声明： enum ScrollType 差异内容： enum ScrollType|api/@ohos.web.webview.d.ts|
|新增API|NA|类名：ScrollType； API声明：EVENT 差异内容：EVENT|api/@ohos.web.webview.d.ts|
|新增API|NA|类名：WebviewController； API声明：scrollByWithResult(deltaX: number, deltaY: number): boolean; 差异内容：scrollByWithResult(deltaX: number, deltaY: number): boolean;|api/@ohos.web.webview.d.ts|
|新增API|NA|类名：global； API声明：type OnNativeEmbedVisibilityChangeCallback = (nativeEmbedVisibilityInfo: NativeEmbedVisibilityInfo) =\> void; 差异内容：type OnNativeEmbedVisibilityChangeCallback = (nativeEmbedVisibilityInfo: NativeEmbedVisibilityInfo) =\> void;|component/web.d.ts|
|新增API|NA|类名：ProtectedResourceType； API声明：SENSOR = 'TYPE_SENSOR' 差异内容：SENSOR = 'TYPE_SENSOR'|component/web.d.ts|
|新增API|NA|类名：global； API声明： declare interface NativeEmbedVisibilityInfo 差异内容： declare interface NativeEmbedVisibilityInfo|component/web.d.ts|
|新增API|NA|类名：NativeEmbedVisibilityInfo； API声明：visibility: boolean; 差异内容：visibility: boolean;|component/web.d.ts|
|新增API|NA|类名：NativeEmbedVisibilityInfo； API声明：embedId: string; 差异内容：embedId: string;|component/web.d.ts|
|新增API|NA|类名：WebAttribute； API声明：onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback): WebAttribute; 差异内容：onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback): WebAttribute;|component/web.d.ts|
|新增API|NA|类名：WebAttribute； API声明：editMenuOptions(editMenu: EditMenuOptions): WebAttribute; 差异内容：editMenuOptions(editMenu: EditMenuOptions): WebAttribute;|component/web.d.ts|
