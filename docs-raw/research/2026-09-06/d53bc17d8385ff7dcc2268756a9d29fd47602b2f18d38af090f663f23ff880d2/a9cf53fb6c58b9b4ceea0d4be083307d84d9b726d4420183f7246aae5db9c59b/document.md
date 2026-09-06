# MediaLibrary_RequestId

```
typedef struct MediaLibrary_RequestId {...} MediaLibrary_RequestId
```

#### 概述

定义请求ID。

当请求媒体库资源时，会返回此类型。

请求ID可用于取消对应的媒体库资源请求。

如果请求失败，值将全为零，如 "00000000-0000-0000-0000-000000000000"。

起始版本： 12

相关模块： [MediaAssetManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager)

所在头文件： [media_asset_base_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h)  

#### 汇总

#### 成员变量

|名称|描述|
|:------------------------------------|:-------------------------|
|char requestId\[UUID_STR_MAX_LENGTH\]|请求ID，用于标识媒体库资源请求，可用于取消该请求。|
