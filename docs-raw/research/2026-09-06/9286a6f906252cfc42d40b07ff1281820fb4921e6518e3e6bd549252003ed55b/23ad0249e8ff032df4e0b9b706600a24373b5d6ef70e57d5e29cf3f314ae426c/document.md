# Basic Services Kit

|操作|旧版本|新版本|d.ts文件|
|:----|:-----------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|:------------------------|
|错误码变更|类名：SystemPasteboard； API声明：clear(callback: AsyncCallback\<void\>): void; 差异内容：NA|类名：SystemPasteboard； API声明：clear(callback: AsyncCallback\<void\>): void; 差异内容：401|api/@ohos.pasteboard.d.ts|
|错误码变更|类名：SystemPasteboard； API声明：getPasteData(callback: AsyncCallback\<PasteData\>): void; 差异内容：NA|类名：SystemPasteboard； API声明：getPasteData(callback: AsyncCallback\<PasteData\>): void; 差异内容：401|api/@ohos.pasteboard.d.ts|
|错误码变更|类名：request； API声明：function download(config: DownloadConfig, callback: AsyncCallback\<DownloadTask\>): void; 差异内容：NA|类名：request； API声明：function download(config: DownloadConfig, callback: AsyncCallback\<DownloadTask\>): void; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：request； API声明：function download(config: DownloadConfig): Promise\<DownloadTask\>; 差异内容：NA|类名：request； API声明：function download(config: DownloadConfig): Promise\<DownloadTask\>; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：request； API声明：function upload(config: UploadConfig, callback: AsyncCallback\<UploadTask\>): void; 差异内容：NA|类名：request； API声明：function upload(config: UploadConfig, callback: AsyncCallback\<UploadTask\>): void; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：request； API声明：function upload(config: UploadConfig): Promise\<UploadTask\>; 差异内容：NA|类名：request； API声明：function upload(config: UploadConfig): Promise\<UploadTask\>; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：DownloadTask； API声明：remove(callback: AsyncCallback\<boolean\>): void; 差异内容：NA|类名：DownloadTask； API声明：remove(callback: AsyncCallback\<boolean\>): void; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：DownloadTask； API声明：remove(): Promise\<boolean\>; 差异内容：NA|类名：DownloadTask； API声明：remove(): Promise\<boolean\>; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：DownloadTask； API声明：pause(callback: AsyncCallback\<void\>): void; 差异内容：NA|类名：DownloadTask； API声明：pause(callback: AsyncCallback\<void\>): void; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：DownloadTask； API声明：pause(): Promise\<void\>; 差异内容：NA|类名：DownloadTask； API声明：pause(): Promise\<void\>; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：DownloadTask； API声明：resume(callback: AsyncCallback\<void\>): void; 差异内容：NA|类名：DownloadTask； API声明：resume(callback: AsyncCallback\<void\>): void; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：DownloadTask； API声明：resume(): Promise\<void\>; 差异内容：NA|类名：DownloadTask； API声明：resume(): Promise\<void\>; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：DownloadTask； API声明：query(callback: AsyncCallback\<DownloadInfo\>): void; 差异内容：NA|类名：DownloadTask； API声明：query(callback: AsyncCallback\<DownloadInfo\>): void; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：DownloadTask； API声明：query(): Promise\<DownloadInfo\>; 差异内容：NA|类名：DownloadTask； API声明：query(): Promise\<DownloadInfo\>; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：DownloadTask； API声明：queryMimeType(callback: AsyncCallback\<string\>): void; 差异内容：NA|类名：DownloadTask； API声明：queryMimeType(callback: AsyncCallback\<string\>): void; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：DownloadTask； API声明：queryMimeType(): Promise\<string\>; 差异内容：NA|类名：DownloadTask； API声明：queryMimeType(): Promise\<string\>; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：UploadTask； API声明：remove(callback: AsyncCallback\<boolean\>): void; 差异内容：NA|类名：UploadTask； API声明：remove(callback: AsyncCallback\<boolean\>): void; 差异内容：201|api/@ohos.request.d.ts|
|错误码变更|类名：UploadTask； API声明：remove(): Promise\<boolean\>; 差异内容：NA|类名：UploadTask； API声明：remove(): Promise\<boolean\>; 差异内容：201|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const EXCEPTION_PERMISSION: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const EXCEPTION_PERMISSION: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const EXCEPTION_PARAMCHECK: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const EXCEPTION_PARAMCHECK: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const EXCEPTION_UNSUPPORTED: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const EXCEPTION_UNSUPPORTED: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const EXCEPTION_FILEIO: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const EXCEPTION_FILEIO: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const EXCEPTION_FILEPATH: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const EXCEPTION_FILEPATH: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const EXCEPTION_SERVICE: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const EXCEPTION_SERVICE: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const EXCEPTION_OTHERS: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const EXCEPTION_OTHERS: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const NETWORK_MOBILE: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const NETWORK_MOBILE: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const NETWORK_WIFI: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const NETWORK_WIFI: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const ERROR_CANNOT_RESUME: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const ERROR_CANNOT_RESUME: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const ERROR_DEVICE_NOT_FOUND: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const ERROR_DEVICE_NOT_FOUND: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const ERROR_FILE_ALREADY_EXISTS: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const ERROR_FILE_ALREADY_EXISTS: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const ERROR_FILE_ERROR: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const ERROR_FILE_ERROR: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const ERROR_HTTP_DATA_ERROR: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const ERROR_HTTP_DATA_ERROR: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const ERROR_INSUFFICIENT_SPACE: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const ERROR_INSUFFICIENT_SPACE: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const ERROR_TOO_MANY_REDIRECTS: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const ERROR_TOO_MANY_REDIRECTS: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const ERROR_UNHANDLED_HTTP_CODE: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const ERROR_UNHANDLED_HTTP_CODE: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const ERROR_UNKNOWN: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const ERROR_UNKNOWN: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const ERROR_OFFLINE: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const ERROR_OFFLINE: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const ERROR_UNSUPPORTED_NETWORK_TYPE: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const ERROR_UNSUPPORTED_NETWORK_TYPE: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const PAUSED_QUEUED_FOR_WIFI: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const PAUSED_QUEUED_FOR_WIFI: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const PAUSED_WAITING_FOR_NETWORK: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const PAUSED_WAITING_FOR_NETWORK: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const PAUSED_WAITING_TO_RETRY: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const PAUSED_WAITING_TO_RETRY: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const PAUSED_BY_USER: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const PAUSED_BY_USER: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const PAUSED_UNKNOWN: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const PAUSED_UNKNOWN: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const SESSION_SUCCESSFUL: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const SESSION_SUCCESSFUL: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const SESSION_RUNNING: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const SESSION_RUNNING: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const SESSION_PENDING: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const SESSION_PENDING: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const SESSION_PAUSED: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const SESSION_PAUSED: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：request； API声明：const SESSION_FAILED: number; 差异内容：ohos.permission.INTERNET|类名：request； API声明：const SESSION_FAILED: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadConfig； API声明：url: string; 差异内容：ohos.permission.INTERNET|类名：DownloadConfig； API声明：url: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadConfig； API声明：header?: Object; 差异内容：ohos.permission.INTERNET|类名：DownloadConfig； API声明：header?: Object; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadConfig； API声明：enableMetered?: boolean; 差异内容：ohos.permission.INTERNET|类名：DownloadConfig； API声明：enableMetered?: boolean; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadConfig； API声明：enableRoaming?: boolean; 差异内容：ohos.permission.INTERNET|类名：DownloadConfig； API声明：enableRoaming?: boolean; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadConfig； API声明：description?: string; 差异内容：ohos.permission.INTERNET|类名：DownloadConfig； API声明：description?: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadConfig； API声明：networkType?: number; 差异内容：ohos.permission.INTERNET|类名：DownloadConfig； API声明：networkType?: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadConfig； API声明：filePath?: string; 差异内容：ohos.permission.INTERNET|类名：DownloadConfig； API声明：filePath?: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadConfig； API声明：title?: string; 差异内容：ohos.permission.INTERNET|类名：DownloadConfig； API声明：title?: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadConfig； API声明：background?: boolean; 差异内容：ohos.permission.INTERNET|类名：DownloadConfig； API声明：background?: boolean; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadInfo； API声明：description: string; 差异内容：ohos.permission.INTERNET|类名：DownloadInfo； API声明：description: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadInfo； API声明：downloadedBytes: number; 差异内容：ohos.permission.INTERNET|类名：DownloadInfo； API声明：downloadedBytes: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadInfo； API声明：downloadId: number; 差异内容：ohos.permission.INTERNET|类名：DownloadInfo； API声明：downloadId: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadInfo； API声明：failedReason: number; 差异内容：ohos.permission.INTERNET|类名：DownloadInfo； API声明：failedReason: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadInfo； API声明：fileName: string; 差异内容：ohos.permission.INTERNET|类名：DownloadInfo； API声明：fileName: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadInfo； API声明：filePath: string; 差异内容：ohos.permission.INTERNET|类名：DownloadInfo； API声明：filePath: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadInfo； API声明：pausedReason: number; 差异内容：ohos.permission.INTERNET|类名：DownloadInfo； API声明：pausedReason: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadInfo； API声明：status: number; 差异内容：ohos.permission.INTERNET|类名：DownloadInfo； API声明：status: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadInfo； API声明：targetURI: string; 差异内容：ohos.permission.INTERNET|类名：DownloadInfo； API声明：targetURI: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadInfo； API声明：downloadTitle: string; 差异内容：ohos.permission.INTERNET|类名：DownloadInfo； API声明：downloadTitle: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadInfo； API声明：downloadTotalBytes: number; 差异内容：ohos.permission.INTERNET|类名：DownloadInfo； API声明：downloadTotalBytes: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadTask； API声明：on(type: 'progress', callback: (receivedSize: number, totalSize: number) =\> void): void; 差异内容：ohos.permission.INTERNET|类名：DownloadTask； API声明：on(type: 'progress', callback: (receivedSize: number, totalSize: number) =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadTask； API声明：off(type: 'progress', callback?: (receivedSize: number, totalSize: number) =\> void): void; 差异内容：ohos.permission.INTERNET|类名：DownloadTask； API声明：off(type: 'progress', callback?: (receivedSize: number, totalSize: number) =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadTask； API声明：on(type: 'complete' \| 'pause' \| 'remove', callback: () =\> void): void; 差异内容：ohos.permission.INTERNET|类名：DownloadTask； API声明：on(type: 'complete' \| 'pause' \| 'remove', callback: () =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadTask； API声明：on(type: 'complete' \| 'pause' \| 'remove', callback: () =\> void): void; 差异内容：ohos.permission.INTERNET|类名：DownloadTask； API声明：on(type: 'complete' \| 'pause' \| 'remove', callback: () =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadTask； API声明：on(type: 'complete' \| 'pause' \| 'remove', callback: () =\> void): void; 差异内容：ohos.permission.INTERNET|类名：DownloadTask； API声明：on(type: 'complete' \| 'pause' \| 'remove', callback: () =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadTask； API声明：off(type: 'complete' \| 'pause' \| 'remove', callback?: () =\> void): void; 差异内容：ohos.permission.INTERNET|类名：DownloadTask； API声明：off(type: 'complete' \| 'pause' \| 'remove', callback?: () =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadTask； API声明：off(type: 'complete' \| 'pause' \| 'remove', callback?: () =\> void): void; 差异内容：ohos.permission.INTERNET|类名：DownloadTask； API声明：off(type: 'complete' \| 'pause' \| 'remove', callback?: () =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadTask； API声明：off(type: 'complete' \| 'pause' \| 'remove', callback?: () =\> void): void; 差异内容：ohos.permission.INTERNET|类名：DownloadTask； API声明：off(type: 'complete' \| 'pause' \| 'remove', callback?: () =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadTask； API声明：on(type: 'fail', callback: (err: number) =\> void): void; 差异内容：ohos.permission.INTERNET|类名：DownloadTask； API声明：on(type: 'fail', callback: (err: number) =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：DownloadTask； API声明：off(type: 'fail', callback?: (err: number) =\> void): void; 差异内容：ohos.permission.INTERNET|类名：DownloadTask； API声明：off(type: 'fail', callback?: (err: number) =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：File； API声明：filename: string; 差异内容：ohos.permission.INTERNET|类名：File； API声明：filename: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：File； API声明：name: string; 差异内容：ohos.permission.INTERNET|类名：File； API声明：name: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：File； API声明：uri: string; 差异内容：ohos.permission.INTERNET|类名：File； API声明：uri: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：File； API声明：type: string; 差异内容：ohos.permission.INTERNET|类名：File； API声明：type: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：RequestData； API声明：name: string; 差异内容：ohos.permission.INTERNET|类名：RequestData； API声明：name: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：RequestData； API声明：value: string; 差异内容：ohos.permission.INTERNET|类名：RequestData； API声明：value: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadConfig； API声明：url: string; 差异内容：ohos.permission.INTERNET|类名：UploadConfig； API声明：url: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadConfig； API声明：header: Object; 差异内容：ohos.permission.INTERNET|类名：UploadConfig； API声明：header: Object; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadConfig； API声明：method: string; 差异内容：ohos.permission.INTERNET|类名：UploadConfig； API声明：method: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadConfig； API声明：files: Array\<File\>; 差异内容：ohos.permission.INTERNET|类名：UploadConfig； API声明：files: Array\<File\>; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadConfig； API声明：data: Array\<RequestData\>; 差异内容：ohos.permission.INTERNET|类名：UploadConfig； API声明：data: Array\<RequestData\>; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：TaskState； API声明：path: string; 差异内容：ohos.permission.INTERNET|类名：TaskState； API声明：path: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：TaskState； API声明：responseCode: number; 差异内容：ohos.permission.INTERNET|类名：TaskState； API声明：responseCode: number; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：TaskState； API声明：message: string; 差异内容：ohos.permission.INTERNET|类名：TaskState； API声明：message: string; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadTask； API声明：on(type: 'progress', callback: (uploadedSize: number, totalSize: number) =\> void): void; 差异内容：ohos.permission.INTERNET|类名：UploadTask； API声明：on(type: 'progress', callback: (uploadedSize: number, totalSize: number) =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadTask； API声明：off(type: 'progress', callback?: (uploadedSize: number, totalSize: number) =\> void): void; 差异内容：ohos.permission.INTERNET|类名：UploadTask； API声明：off(type: 'progress', callback?: (uploadedSize: number, totalSize: number) =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadTask； API声明：on(type: 'headerReceive', callback: (header: object) =\> void): void; 差异内容：ohos.permission.INTERNET|类名：UploadTask； API声明：on(type: 'headerReceive', callback: (header: object) =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadTask； API声明：off(type: 'headerReceive', callback?: (header: object) =\> void): void; 差异内容：ohos.permission.INTERNET|类名：UploadTask； API声明：off(type: 'headerReceive', callback?: (header: object) =\> void): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadTask； API声明：on(type: 'complete' \| 'fail', callback: Callback\<Array\<TaskState\>\>): void; 差异内容：ohos.permission.INTERNET|类名：UploadTask； API声明：on(type: 'complete' \| 'fail', callback: Callback\<Array\<TaskState\>\>): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadTask； API声明：on(type: 'complete' \| 'fail', callback: Callback\<Array\<TaskState\>\>): void; 差异内容：ohos.permission.INTERNET|类名：UploadTask； API声明：on(type: 'complete' \| 'fail', callback: Callback\<Array\<TaskState\>\>): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadTask； API声明：off(type: 'complete' \| 'fail', callback?: Callback\<Array\<TaskState\>\>): void; 差异内容：ohos.permission.INTERNET|类名：UploadTask； API声明：off(type: 'complete' \| 'fail', callback?: Callback\<Array\<TaskState\>\>): void; 差异内容：NA|api/@ohos.request.d.ts|
|权限变更|类名：UploadTask； API声明：off(type: 'complete' \| 'fail', callback?: Callback\<Array\<TaskState\>\>): void; 差异内容：ohos.permission.INTERNET|类名：UploadTask； API声明：off(type: 'complete' \| 'fail', callback?: Callback\<Array\<TaskState\>\>): void; 差异内容：NA|api/@ohos.request.d.ts|
|新增API|NA|类名：Faults； API声明：PARAM = 0x30 差异内容：PARAM = 0x30|api/@ohos.request.d.ts|
|新增API|NA|类名：Faults； API声明：DNS = 0x50 差异内容：DNS = 0x50|api/@ohos.request.d.ts|
|新增API|NA|类名：Faults； API声明：TCP = 0x60 差异内容：TCP = 0x60|api/@ohos.request.d.ts|
|新增API|NA|类名：Faults； API声明：SSL = 0x70 差异内容：SSL = 0x70|api/@ohos.request.d.ts|
|新增API|NA|类名：Faults； API声明：REDIRECT = 0x80 差异内容：REDIRECT = 0x80|api/@ohos.request.d.ts|
