# ArkTS API错误码

![](https://media:201787906178302809)  
以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。  

#### 1008301002 路由跳转失败

错误信息

Route switching failed.

错误描述

路由跳转失败。

可能原因

输入参数不符合要求，或路由跳转异常。

处理步骤

检查输入参数是否符合[InteractiveLivenessConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness#interactivelivenessconfig)要求，过一段时间重试，并做好相关的逻辑判断。  

#### 1008302000 检测算法初始化

错误信息

Detection algorithm initialization.

错误描述

检测算法初始化未完成，无检测数据返回。

可能原因

获取结果时还未进行活体检测。

处理步骤

活体检测完成之后再获取结果。  

#### 1008302001 检测超时

错误信息

Detection timeout.

错误描述

检测超时，跳转失败页面。如果配置了失败页面或者back路由跳转，建议有重新检测的场景。

可能原因

1. 未按照提示完成指定动作，如提示向左摇头，实际上却向右摇头。

2. 环境不满足检测要求。

处理步骤

1. 检测时请按提示缓慢完成指定动作。

2. 避免在暗光或者阳光直射的环境下进行活体检测。

#### 1008302002 动作错误

错误信息

Action mutual exclusion error.

错误描述

动作错误，跳转失败页面。如果配置了失败页面或者back路由跳转，建议有重新检测的场景。

可能原因

1. 检测时，没有按照提示完成相关动作，导致检测失败了。

2. 在运动中进行检测，导致动作互斥检测失败。

处理步骤

1. 请避免在运动中进行检测。

2. 请按照提示缓慢完成指定动作。

#### 1008302003 连续性检测失败

错误信息

Continuity Check Failure.

错误描述

连续性检测失败，跳转失败页面。如果配置了失败页面或者back路由跳转，建议有重新检测的场景。

可能原因

检测多个动作时，没有按照提示完成相关动作，导致连续性检测失败了。

处理步骤

检测时请按提示完成相关动作。  

#### 1008302004 检测未完成

错误信息

The test is not complete.

错误描述

检测未完成。如果配置了失败页面或者back路由跳转，建议有重新检测的场景。

可能原因

1. 用户主动退出检测。

2. 检测流程被打断，息屏、退到后台等。

处理步骤

请重新完成活体检测流程，并确保活体检测过程中设备停留在活体检测页面。  

#### 1013700002 服务异常

错误信息

The service is abnormal.

错误描述

使用功能时，底层服务异常。

可能原因

1. 底层能力绑定失败。

处理步骤

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)方式获取技术支持。
