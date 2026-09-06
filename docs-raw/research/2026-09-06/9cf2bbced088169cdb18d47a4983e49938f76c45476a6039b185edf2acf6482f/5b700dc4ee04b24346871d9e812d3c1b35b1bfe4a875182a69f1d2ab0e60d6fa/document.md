# 端插件配置

#### 工具基本信息

新建工具后填写工具名称：

![](https://media:301785143829651564 "点击放大")

添加版本-填写工具版本号、工具描述、执行方式、选择涉及端侧app页面操控开或关

工具描述：填写该工具的功能，用于大模型更好地理解，精准匹配与之对应的业务场景下调用该工具。

执行方式：前台执行、后台执行、卡片执行。

1、前台执行：拉起端侧应用到前台页面；

选择前台执行时，配置工具选择实现方式有三种：标准实现、Applink实现、Deeplink实现。

① 标准实现：标准实现需要进行意图声明和意图调用相关代码开发。意图声明开发者需要编辑对应的意图配置insight_intent.json文件实现意图注册。具体实现参考[插件工具的对应代码实现](https://developer.huawei.com/consumer/cn/doc/service/corresponding-code-implementation-of-plug-in-tools-0000002437625938)，

![](https://media:301785143829737565 "点击放大")

② Applink实现：[可以通过](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startupapp)[App Linking](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startupapp)[应用链接拉起指定应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startupapp)，实现应用间跳转。当应用已安装时，优先通过应用展示内容；若应用未安装，则通过系统浏览器展示网页版内容。已经实现了Applink的应用可以直接配置成端插件使用，Applink携带的参数要以端插件入参的形式呈现，需要配置支持app的最小版本号，长短链接最少填一个。

实现参照：[参考文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startup)

![](https://media:301785143829828566 "点击放大")

③ Deeplink实现：采用Deeplink进行跳转时，系统会根据接口中传入的uri信息，在本地已安装的应用中寻找到符合条件的应用并进行拉起。已经实现了Deeplink的应用可以直接配置成端插件使用，Deeplink携带的参数要以端插件入参的形式呈现，需要配置支持的app最小版本号，跳转链接必填。

实现参照：[参考文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-linking-startup)

![](https://media:301785143829921567 "点击放大")

2、后台执行：后台执行该工具，后续使用该工具的时候，可以绑定卡片把返回的数据以卡片形式呈现出来；

3、卡片执行：调用端侧应用渲染卡片。

![](https://media:301785143829987568 "点击放大")

涉及端侧app页面操控：

![](https://media:301785143830028569 "点击放大")

样例效果：

![](https://media:301785143830290570)  

#### 输入输出参数配置

输入参数：大模型会根据用户输入的词和参数描述进行匹配，在调用插件时传入参数；

输出参数：返回数据必须包含 code 和 result 字段，code 用于表示业务状态码， result 用于承载具体业务数据。

![](https://media:301785143830364571 "点击放大")

<br />

某些插件参数值较为稳定，不需要动态传入参数值，建议为参数设置默认值，并关闭开启开关（参数对模型不可见），减少智能体中的大模型调用插件时的流程，提高调用效率。

![](https://media:301785143830597572 "点击放大")

但对于必填的输入参数，如果想关闭开启开关，则需要填写缺省值。

![](https://media:301785143830673573 "点击放大")
