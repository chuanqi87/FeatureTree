# 请求

#### has.request

has.request(Object object): RequestTask

发起HTTPS网络请求。

从1.0.4版本开始，调用返回[RequestTask](#requesttask)。  
![](https://media:901788330616742917)  
* 开发者服务器接口地址，必须是https协议，并在AGC完成[服务器域名配置](https://developer.huawei.com/consumer/cn/doc/atomic-guides/agc-help-harmonyos-server-domain)。

* 在ASCF运行时2.0.1版本之前，不支持TLS 1.2加密协议；2.0.1及以后版本，支持TLS 1.2加密协议。

起始版本： 1.0.0

需要权限： 在module.json5中声明ohos.permission.INTERNET。

注意事项：在调用此接口前，需要先完成[配置服务器域名](https://developer.huawei.com/consumer/cn/doc/atomic-guides/agc-help-harmonyos-server-domain)。

参数：

参数为Object对象，包括以下字段。  

|参数|类型|默认值|必填|描述|
|:------------|:--------------------------|:----|:-|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|url|string|-|是|开发者服务器接口地址。|
|data|string\|Object\|ArrayBuffer|-|否|请求的参数。|
|header|Object|-|否|可自定义设置请求的请求头header，header中不能配置Referer。 content-type默认为application/json。 若存在多个content-type字段，在ASCF运行时2.0.1版本之前，以第一个content-type值解析处理data数据；2.0.1及后续版本，按最后一个content-type值解析处理data数据。|
|timeout|number|-|否|超时时间，单位：ms。默认值：60000。|
|method|string|GET|否|HTTP请求方法。|
|dataType|string|json|否|返回的数据格式。|
|responseType|string|text|否|响应的数据类型。|
|enableHttp2|boolean|false|否|开启http2。|
|enableProfile|boolean|true|否|是否开启profile，默认开启。开启后可在接口回调的res.profile中查看性能调试信息。|
|enableCache|boolean|false|否|开启Http缓存。|
|enableChunked|boolean|false|否|开启transfer-encoding chunked。 起始版本： 2.0.2|
|success|function|-|否|接口调用成功的回调函数。|
|fail|function|-|否|接口调用失败的回调函数。|
|complete|function|-|否|接口调用结束的回调函数（调用成功、失败都会执行）。|

method的合法值：  

|值|描述|
|:------|:-------------|
|OPTIONS|HTTP请求OPTIONS。|
|GET|HTTP请求GET。|
|HEAD|HTTP请求HEAD。|
|POST|HTTP请求POST。|
|PUT|HTTP请求PUT。|
|DELETE|HTTP请求DELETE。|
|TRACE|HTTP请求TRACE。|
|CONNECT|HTTP请求CONNECT。|

responseType的合法值：  

|值|描述|
|:----------|:-----------------|
|text|响应的数据为文本。|
|arraybuffer|响应的数据为ArrayBuffer。|

success返回值：  

|参数|类型|描述|
|:---------|:------------------------|:--------------------------|
|data|string/object/arraybuffer|服务器返回的数据。|
|statusCode|number|服务器返回的HTTP状态码。|
|header|object|服务器返回的HTTP Response Header。|
|cookies|Array\<string\>|开发者服务器返回的cookies，格式为字符串数组。|
|profile|Object|网络请求过程中一些调试信息。|

返回值：

返回网络请求对象[RequestTask](#requesttask)。

错误码：  

|错误码|错误信息|
|:-------|:--------------------------------------------------------------------------------------------------------------------------------|
|102|Parameter error. Possible causes: 1.method is invalid. 2.url format is invalid.|
|201|Permission denied.|
|401|Parameter error. Possible causes: 1. Missing mandatory parameters. 2. Incorrect parameter type. 3. Parameter verification failed.|
|40000101|request error. 更多错误信息参考：[HTTP错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-http)。|

示例：

```
has.request({
  url: 'https://www.example.com', // 此处仅为样例，请开发者更换为可用接口地址
  data: {
    x: '',
    y: ''
  },
  header: {
    'content-type': 'application/json'
  },
  success: (res) => {
    console.info(res.data);
  }
});
```

#### RequestTask

网络请求任务对象。

起始版本： 1.0.4  

#### RequestTask.abort

RequestTask.abort()

中断请求任务。

起始版本： 1.0.4

示例：

```
const requestTask = has.request({
  url: 'https://www.example.com', // 此处仅为样例，请开发者更换为可用接口地址
  data: {
    x: '',
    y: ''
  },
  header: {
    'content-type': 'application/json'
  },
  success: (res) => {
    console.info(res.data);
  }
})
requestTask.abort(); // 中断网络请求
```

#### RequestTask.onHeadersReceived

RequestTask.onHeadersReceived(function callback)

监听HTTP Response Header事件，会比请求完成事件更早。

起始版本： 1.0.4

参数：  

|参数|类型|必填|描述|
|:-------|:-------|:-|:---------------------------|
|callback|function|是|HTTP Response Header事件的回调函数。|

callback返回值：  

|参数|类型|描述|
|:-----|:-----|:-----------------------------|
|header|object|开发者服务器返回的HTTP Response Header。|

错误码：  

|错误码|错误信息|
|:--|:---------------------------------------------------------------|
|102|Parameter error. Possible causes: listener should be a function.|

示例：

```
const requestTask = has.request({
  url: 'https://www.example.com', // 此处仅为样例，请开发者更换为可用接口地址
  data: {
    x: '',
    y: ''
  },
  header: {
    'content-type': 'application/json'
  },
  success: (res) => {
    console.info(res.data);
  }
});
const callback = (res) => {
  console.info('Request onHeadersReceived', res);
};
requestTask.onHeadersReceived(callback);
```

#### RequestTask.offHeadersReceived

RequestTask.offHeadersReceived(function callback)

移除HTTP Response Header事件的监听函数，没传则移除所有监听。

起始版本： 1.0.4

参数：  

|参数|类型|必填|描述|
|:-------|:-------|:-|:---------------------------------------|
|callback|function|否|onHeadersReceived传入的回调函数。不传此参数则移除所有回调函数。|

错误码：  

|错误码|错误信息|
|:--|:---------------------------------------------------------------|
|102|Parameter error. Possible causes: listener should be a function.|

示例：

```
const requestTask = has.request({
  url: 'https://www.example.com', // 此处仅为样例，请开发者更换为可用接口地址
  data: {
    x: '',
    y: ''
  },
  header: {
    'content-type': 'application/json'
  },
  success: (res) => {
    console.info(res.data);
  }
});
const callback = (res) => {
  console.info('Request onHeadersReceived', res.header);
};
requestTask.onHeadersReceived(callback);
requestTask.offHeadersReceived(callback);
```

#### RequestTask.onChunkReceived

RequestTask.onChunkReceived(function callback)

监听Transfer-Encoding Chunk Received事件，当接收到新的chunk时触发。

起始版本： 2.0.2

参数：  

|参数|类型|必填|描述|
|:-------|:-------|:-|:---------------------------------------|
|callback|function|是|Transfer-Encoding Chunk Received事件的监听函数。|

callback返回值：  

|参数|类型|描述|
|:---|:----------|:---------------|
|data|ArrayBuffer|返回的chunk buffer。|

错误码：  

|错误码|错误信息|
|:--|:---------------------------------------------------------------|
|102|Parameter error. Possible causes: listener should be a function.|

示例：

```
const requestTask = has.request({
  url: 'https://www.example.com', // 此处仅为样例，请开发者更换为可用接口地址
  enableChunked: true,
  success: (res) => {
    console.info('request success', res);
  },
  fail: (err) => {
    console.error('request fail', err);
  }
});
const onChunkReceivedFn = (res) => {
  console.info('onChunkReceived callback triggered', res.data.byteLength);
};
requestTask.onChunkReceived(onChunkReceivedFn);
```

#### RequestTask.offChunkReceived

RequestTask.offChunkReceived(function callback)

移除Transfer-Encoding Chunk Received事件的监听函数。

起始版本： 2.0.2

参数：  

|参数|类型|必填|描述|
|:-------|:-------|:-|:--------------------------------------------------------------------------------|
|callback|function|否|[RequestTask.onChunkReceived](#requesttaskonchunkreceived)传入的监听函数，不传此参数则移除所有监听函数。|

|错误码|错误信息|
|:--|:---------------------------------------------------------------|
|102|Parameter error. Possible causes: listener should be a function.|

示例：

```
const requestTask = has.request({
  url: 'https://www.example.com', // 此处仅为样例，请开发者更换为可用接口地址
  enableChunked: true,
  success: (res) => {
    console.info('request success', res);
  },
  fail: (err) => {
    console.error('request fail', err);
  }
});
const onChunkReceivedFn = (res) => {
  console.info('onChunkReceived callback triggered', res.data.byteLength);
};
requestTask.onChunkReceived(onChunkReceivedFn);
requestTask.offChunkReceived(onChunkReceivedFn);
```
