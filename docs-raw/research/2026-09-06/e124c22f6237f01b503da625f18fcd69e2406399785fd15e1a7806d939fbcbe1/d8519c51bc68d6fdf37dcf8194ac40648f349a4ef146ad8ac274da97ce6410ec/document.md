# 命令行执行测试

#### 环境准备

硬件环境操作系统：

Windows操作系统、MacOS操作系统要求：

内存：推荐使用16GB及以上

硬盘：100GB 及以上

分辨率：1600\*900 像素及以上

Command客户端使用准备

1、准备工作：安装 Windows 或 Mac 版本的 DevEco Testing 客户端，建议提前手动下载所需要的测试服务卡片。

2、使用命令行进行测试任务时，每个json文件对应一个测试服务，同时执行的任务数不能超过4个，执行新的任务需要打开一个新的命令行窗口。  
![](https://media:901787900072766762)  
同一台PC限制只能执行一个上架预检/场景化性能/性能基础质量测试任务（性能测试），即如果一台PC已经在执行性能测试，则此台电脑不允许再执行性能测试。

PS：性能测试对内存消耗比较大，为了避免出现任务执行失败或异常的情况，限制一台PC只能同时执行一个性能测试任务。

<br />

#### Command客户端使用指南

#### 用户信息登录认证

客户端鉴权

安装DevEco Testing客户端后，登录进入首页-\>点击设置，在基本设置页面开启登录状态保活。

![](https://media:901787900072801763 "点击放大")  

#### 命令行启动测试任务

Win 环境命令行启动

1、右键DevEco Testing工具图标，选择打开文件所在目录即 DevEco Testing 安装目录，进入bin文件目录，即 DevEcoTestingConsole.bat 文件所在目录。

2、在当前文件路径中输入cmd后点击回车进入cmd命令窗口。

![](https://media:901787900072838764 "点击放大")

3、进入cmd窗口后，输入：DevEcoTestingConsole.bat -params 参数json文件路径。

![](https://media:901787900072882765 "点击放大")  
![](https://media:901787900072910766)  
json文件路径中不要含有特殊字符、中文、空格，可以直接拖动json文件到cmd命令窗口内自动填充文件路径。

4、参数json文件选择以UTF-8无BOM格式编码，具体文件参数可参考 [json文件说明文档](#section94357421134) 中各测试服务参数示例构建json文件。

<br />

Mac 环境命令行启动

1、安装完客户端后，在应用程序中找到DevEco_Testing_for_App.app，选中后control+右键，选择显示包内容进入 DevEco_Testing_for_App.app/Contents/PlugIns/java.jdk/Contents/Home 目录，在该目录下选中bin目录后control + 右键，选择新建位于文件夹位置的终端窗口。

![](https://media:901787900072962767 "点击放大")

2、执行 ./DevEcoTestingConsole.sh 脚本

在终端窗口中执行 ./DevEcoTestingConsole.sh -params 参数json文件路径（建议：路径中不要含有特殊字符、中文、空格，可以直接拖动json文件到命令窗口内自动填充文件路径）。

初次执行可能会有permission denied权限问题，需给./DevEcoTestingConsole.sh脚本添加可执行权限，在终端窗口执行 chmod +x ./DevEcoTestingConsole.sh 。

![](https://media:901787900072993768 "点击放大")

权限添加完成即可通过命令行方式执行 "./DevEcoTestingConsole.sh -params json文件路径 "命令启动测试服务。

![](https://media:901787900073024769 "点击放大")

<br />

#### 配置 json 文件

使用命令行启动测试任务前，需要配置 json 文件，可前往 [json文件说明文档](#section94357421134) 进行查看

<br />

#### 命令行接口查看任务状态

查看任务状态前需要获取任务的taskId，在任务创建成功后可以在对应的打印日志中获取：

![](https://media:901787900073054770 "点击放大")

Mac查看任务状态 终端窗口执行命令：./DevEcoTestingConsole.sh -taskIds "f3\*\*\*469eca"

Win查看任务状态 cmd窗口执行命令：DevEcoTestingConsole.bat -taskIds "f3\*\*\*469eca"

查询结果如下：

![](https://media:901787900073086771 "点击放大")  

#### 命令行停止任务

Mac停止任务 终端窗口执行命令：./DevEcoTestingConsole.sh -stopTask "f3\*\*\*469eca"

Win停止任务 cmd窗口执行命令：DevEcoTestingConsole.bat -stopTask "f3\*\*\*469eca"

结果如下：

![](https://media:901787900073122772 "点击放大")  
![](https://media:901787900073151773)  
上文查看任务状态、停止任务 "xxx" 中的字符是任务ID，工具可支持批量查询/停止多个任务，多个任务ID通过" , "分割。

例如：DevEcoTestingConsole.bat -taskIds "f3a9b27c-439c-40cd-8c21-84bbda469eca,e44c8800-76ed-43f5-9717-021aef15a956,589de9bf-357d-4577-a9c3-c27723e48175"

<br />

版本客户端更新测试服务

Windows 和 Mac 命令行启动任务参数，拼接-update 参数；本地测试服务未下载时，不设置参数（即-update false）也会进行服务下载；本地测试服务已下载时，设置 -update true 更新测试服务；设置 -update false 不更新测试服务。

<br />

#### 通过命令执行测试服务

#### 场景化性能测试

![](https://media:901787900073221774 "点击放大")

<br />

参数说明：  

|----------------|----|------------------------------------------|---------------------------------------------------------------------------------------------------|
|参数|是否必填|取值范围|说明|
|solutionName|是|场景化性能测试|测试服务名|
|executeRounds|是|1-10的整数|执行轮数|
|manualScriptPath|是|用例工程路径|用例工程路径示例参考： Window路径参考：D:\\\\ProgramData\\\\用例工程文件（目录以\\\\分割）； Mac路径参考：/Applications/testing/用例工程文件|
|caseList|是|用例工程中用例名称，至少选一条|用例名称集合|
|perf|是|"响应时延", "完成时延", "丢帧卡顿", "音视频", "黑白块"|固定值，必填项|
|system|是|"CPU", "内存", "温度", "网络", "GPU", "存储", "电量"|指标监控（CPU与内存必选）|
|std|是|"极优体验" "较好体验" "一般体验"|检测标准(较好体验和一般体验建议必选)|
|saveAllImages|是|true/false|是否保留全部数据，选择"是"会保存测试过程中的所有截图，占用较大磁盘空间|
|generateIdeFile|是|true/false|是否生成IDE分析文件|
|sn|是|-|设备sn号|
|taskName|是|-|任务名称|

<br />

示例：场景化性能测试

```
{
    "taskParams": {
        "solutionName": "场景化性能测试",
        "executeRounds": 1,
        "manualScriptPath": "D:\\test\\testcase",
        "caseList": [
            "OH_PerfDemoTest01",
            "OH_PerfDemoTest02"
        ],
        "std": [
            "较好体验", 
            "一般体验", 
            "极优体验"
        ],
        "watchingKpi": {
            "perf": [
                "响应时延",
                "完成时延",
                "丢帧卡顿",
                "音视频",
                "黑白块"
            ],
            "system": [
                "CPU",
                "内存",
                "温度",
                "网络",
                "电量" 
            ]
        },
        "extraTaskParam": {
            "saveAllImages": true,
            "generateIdeFile": true
        },
        "sn": [
            "3AP0*****302"
        ],
        "taskName": "Task-0312-184049"
    }
}
```

<br />

<br />

#### 性能基础质量测试

![](https://media:901787900073295775 "点击放大")

<br />

参数说明：  

|--------------------|---------------------|--------------------------------------------------|--------------------------------------------------------------------------------|
|参数|是否必填|取值范围|说明|
|sn|是|-|设备sn号|
|taskName|是|-|任务名称|
|solutionName|是|性能基础质量测试|测试服务名|
|package.name|是|应用包名|待测应用包名 com.hmos.\*\*\*|
|startTimes|是|1-10之间整数|应用冷启动测试次数|
|traversalTimes|是|10-120之间整数|测试时长，单位：分钟|
|std|是|"极优体验","较好体验", "一般体验"|检测标准选项|
|system|是|"CPU", "内存", "温度", "网络", "GPU", "存储", "电量"|指标监控（CPU与内存必选）|
|perf|是|"响应时延", "完成时延", "丢帧卡顿", "音视频", "黑白块"|固定值，必填项|
|traversalSceneType|是|<br /> scene <br />|遍历方式，需要加上当前参数任务才能正常创建|
|extraTaskParam|是|enableBackgroundTest saveAllImages generateIdeFile|其他配置|
|enableBackgroundTest|是|true/false|是否开启后台负载测试|
|saveAllImages|是|true/false|是否保存全部数据，选择"是"会保存测试过程中的所有截图，占用较大磁盘空间|
|generateIdeFile|是|true/false|是否生成IDE分析文件|
|traversalAction|是|basic|遍历方式 basic-随机遍历|
|installAppPath|否（安装新的应用必传，已安装应用无需填写）|安装包路径，支持hap，zip格式|待安装应用包路径，仅使用新安装应用时填写，路径中不要含有空格和中文，目录以\\\\分割，例： D:\\\\test\\\\com.hmos.\*\*\*.hap|

<br />

示例：性能基础质量测试随机遍历

```
{
    "taskParams": {
        "sn": [
            "3AP0*****302"
        ],
        "traversalSceneType": "scene",
        "taskName": "Task-0804-171639",
        "std": [
            "较好体验",
            "一般体验"
        ],
        "watchingKpi": {
            "perf": [
                "响应时延",
                "完成时延",
                "丢帧卡顿",
                "音视频",
                "黑白块"
            ],
            "system": [
                "CPU",
                "内存",
                "温度",
                "网络",
                "电量"
            ]
        },
        "extraTaskParam": {
            "enableBackgroundTest": true,
            "saveAllImages": false,
            "generateIdeFile": false
        },
        "traversalAction": "basic",
        "startTimes": "1",
        "traversalTimes": "10",
        "solutionName": "性能基础质量测试",
        "package.name": "com.hmos.***", // 选择已安装的应用时传此参数，不传installAppPath
        "installAppPath": "D:\\test\\com.hmos.***" // 选择安装新应用时传此参数，不传package.name
    }
}
```

<br />

<br />

#### 稳定性基础质量测试

![](https://media:901787900073364776 "点击放大")

<br />

参数说明：  

|---------------------------|---------------------|-----------------------|-------------------------------------------------------------------------------|
|参数|是否必填|取值范围|说明|
|solutionName|是|稳定性基础质量测试|测试服务名|
|package.name|是|应用包名|待测应用包名 如：com.hmos.\*\*\*|
|testDuration|是|取值范围：10-60000整数|测试时长，单位：分钟|
|uninstallApp|否|"true": 卸载 "false": 不卸载|是否卸载应用： 使用已安装应用时，需要手动选择false 安装新应用测试场景下按需求填写|
|installAppPath|否（安装新的应用必传，已安装应用无需填写）|安装包路径，支持hap，zip格式|待安装应用包路径，仅使用新安装应用时填写，路径中不要含有空格和中文，目录以\\\\分割 例：D:\\\\test\\\\com.hmos.\*\*\*.hap|
|threadDetect|否|true/false|是否开启多线程检测|
|asanEnable|否|true/false|asan检测开关|
|sn|是|-|设备sn号|
|taskName|是|-|任务名称|
|blackSelected|否|-|应用图谱工具生成的黑名单数据|
|deeplinkRollbackProbability|否|0-60(百分比)|deeplink切换概率|
|deeplinkRollbackPeriodMin|否|1-10080(分钟)|deeplink切换周期|
|deeplink|否|-|deeplink切换链接|
|appFeaturePath|否|-|应用图谱生成的文件路径|

示例1：稳定性基础质量测试-是否安装新应用

```
{ 
     "taskParams": { 
         "solutionName": "稳定性基础质量测试", 
         "package.name": "com.hmos.***", // 选择已安装的应用时传此参数，不传installAppPath
         "installAppPath": "D:\\test\\com.hmos.***.hap",   // 选择安装新应用时传此参数，不传package.name
         "testDuration": "10", 
         "uninstallApp": "false", 
         "threadDetect": "true", 
         "asanEnable": "true", 
         "sn": [ 
             "3AP0*****302" 
         ], 
         "taskName": "Task-***-184050" 
     } 
 }
```

<br />

示例2：稳定性基础质量测试-通用

```
{
    "taskParams": {
        "sn": [
            "LNGxxxxxx03" 
        ],
        "uninstallApp": "false", 
        "taskName": "稳定性测试", 
        "threadDetect": "true", 
        "testDuration": "10", 
        "deeplink": [ 
            "snssdk1128://camera",
            "snssdk1128://search"
        ],
        "deeplinkRollbackProbability": "60", 
        "deeplinkRollbackPeriodMin": "30", 
        "graphPath": "/root/.testing/graphTool/dy", 
        "appFeaturePath": "/root/.testing/graphTool/graph/appfeature.json", 
        "blackSelected": [
            {
                "feature": "文本测试",  
                "blackName": "新建黑名单1" 
            }
        ],
        "solutionName": "稳定性基础质量测试", 
        "package.name": "com.hm.xxx" 
    }
}
```

<br />

#### 内存泄漏测试

![](https://media:901787900073420777 "点击放大")

<br />

参数说明：  

|---------------------------|---------------------|------------------------------|--------------------------------------------------------------------------------|
|参数|是否必填|取值范围|说明|
|sn|是|-|设备sn号|
|taskName|是|-|任务名称|
|solutionName|是|内存泄漏测试|测试服务名|
|package.name|是|应用包名|待测应用包名 如：com.hmos.\*\*\*|
|testDuration|是|10-10080之间整数|测试时长，单位：分钟|
|deeplinkRollbackProbability|否|0-60(百分比)|deeplink切换概率|
|deeplinkRollbackPeriodMin|否|1-10080(分钟)|deeplink切换周期|
|deeplink|否|-|deeplink切换链接|
|appFeaturePath|否|合法路径|图谱特性路径|
|blackSelected|否|选中的图谱特性和黑名单，校验对应关系，所有关键字不超过30个|图谱配置|
|installAppPath|否（安装新的应用必传，已安装应用无需填写）|安装包路径，支持hap，zip格式|待安装应用包路径，仅使用新安装应用时填写，路径中不要含有空格和中文，目录以\\\\分割，例： D:\\\\test\\\\com.hmos.\*\*\*.hap|

示例1：内存泄漏测试随机遍历

```
{
   "taskParams": {
        "sn": [
            "3AP0124816000023"
        ],
        "taskName": "内存泄漏测试0",
        "testDuration": "60",
        "solutionName": "内存泄漏测试",
        "package.name": "com.ss.****",    //应用包名
        "installAppPath": "D:\\test\\com.hmos.***"  //安装新应用时需添加，已安装则不需要
    }
}
```

<br />

示例2：内存泄漏测试随机遍历-黑名单和Deeplink

```
{
    "taskParams": {
        "sn": [
            "23*****180"
        ],
        "taskName": "内存泄漏测试",
        "testDuration": "10",
        "solutionName": "内存泄漏测试",
        "package.name": "com.****w.com",
        "deeplink": [
            "snssdk1128://search/trending",
            "snssdk1128://mainPage?tabid=homepage_tablive"
        ],
        "deeplinkRollbackProbability": "20",
        "deeplinkRollbackPeriodMin": "",
        "appFeaturePath": "E://DevEco Testing//graphTool//appfeature.json",
        "blackSelected": [
            {
                "feature": "黑名单1",
                "blackName": "消息"
            },
            {
                "feature": "黑名单1",
                "blackName": "个人中心"
            }
        ]
    }
}
```

<br />

#### 应用上架预检（本地）

![](https://media:901787900073493778 "点击放大")

<br />

参数说明：  

|------------------------|-------|-----------------------------|----------------------------------------------------------------------------|
|参数|是否必填|取值范围|说明|
|sn|是|-|设备sn号|
|isExecute|自定义测试必须|true false|自定义测试是否选择执行对应的任务|
|uninstall.app|否|true false|是否测试安装卸载应用场景|
|startTimes|自定义测试必须|1-10之间整数|启动测试次数（性能）|
|traversalTimes|自定义测试必须|10-120之间整数|性能测试执行时长，单位：分钟|
|uxTestDuration|自定义测试必须|10-240之间整数|ux测试执行时长，单位：分钟|
|stabilityTestDuration|自定义测试必须|10-10080之间整数|稳定性测试执行时长，单位：分钟|
|taskName|是|-|任务名称|
|packageName|是|-|应用包名|
|isUploadApp|是|true false|是否为综合预检模式|
|app.history.package.path|否|历史应用包路径|历史上架应用包安装路径，路径中不要含有空格和中文，目录以\\\\分割 如： D:\\\\test\\\\com.hmos.\*\*\*.hap|
|levelFirst|是|见 softwareCatagory参数取值说明|一级应用类别|
|levelSecond|是|见 softwareCatagory参数取值说明|二级应用类别|
|levelThird|是|见 softwareCatagory参数取值说明|三级应用类别|
|app_path|是|自定义测试选择hap和zip包，综合自检选择hap格式的包|应用包路径，需要与待测应用为同版本，路径中不要含有空格和中文，目录以\\\\分割 例： D:\\\\hap\\\\com.hmos.\*\*\*.hap|
|solutionName|是|应用上架预检（本地）|测试服务名|

softwareCatagory参数取值说明：  

|--------------|---------------|-------------------------------------|
|一类（levelFirst）|二类（levelSecond）|三类（levelThird）|
|游戏|休闲益智|休闲，IO，音乐节奏，消除，解密，益智|
|游戏|经营策略|古代谋略，现代战略，养成，塔防，经营，MOBA|
|游戏|游戏|游戏|
|游戏|动作设计|跑酷，射击，格斗|
|游戏|角色扮演|多人在线，卡牌，冒险，回合制，生存，动作，放置挂机，仙侠，武侠，传奇，魔幻|
|游戏|棋牌游戏|斗地主，麻将，桌游与棋类，纸牌，捕鱼|
|游戏|体育竞技|赛车，运动，篮球，足球|
|应用|影音娱乐|电视，视频，音乐，K歌，直播，电台|
|应用|实用工具|输入，浏览器，安全性能，工具，闹钟，wifi|
|应用|金融理财|股票基金，银行，贷款，理财，记账，彩票|
|应用|社交通讯|社区，聊天，婚恋，通讯|
|应用|便携生活|家政，本地生活，租房买房，家居装修，电影票，天气日历|
|应用|出行导航|导航，地图，用车，交通票务，公交地铁|
|应用|主题个性|壁纸，铃声，锁屏，桌面|
|应用|教育|英文，学习，翻译，备考|
|应用|运动健康|养生，运动，医疗，健康|
|应用|拍摄美化|拍照，图像美化，相册图库，短视频，影音编辑|
|应用|新闻阅读|电子书，新闻，动漫，有声读物，杂志，幽默，体育，分类信息|
|应用|购物比价|优惠，商城，团购，导购，快递，海淘|
|应用|美食|菜谱，生鲜，买卖，餐饮|
|应用|汽车|养车，违章查询，汽车资讯，驾考|
|应用|旅游住宿|住宿，旅游，行程助手|
|应用|商务|办公软件，效率，笔记，邮箱，招聘|
|应用|儿童|儿童教育，儿歌，母婴|

<br />

示例1：应用上架预检（本地）------自定义测试

```
{
    "taskParams": {
        "sn": [
            "2MM0*****380"
        ],
        "devecoProviderOptions": {},
        "isUploadApp": "false",
        "customTest": {
            "compatibility": {
                "isExecute": true,
                "executeData": {
                    "uninstall.app": false
                }
            },
            "power": {
                "isExecute": true,
                "executeData": {}
            },
            "performance": {
                "isExecute": true,
                "executeData": {
                    "startTimes": 10,
                    "traversalTimes": 90
                }
            },
            "ux": {
                "isExecute": true,
                "executeData": {
                    "uxTestDuration": 60
                }
            },
            "stability": {
                "isExecute": true,
                "executeData": {
                    "stabilityTestDuration": 240
                }
            }
        },
        "taskName": "Task-0801-174411",
        "packageName": "com.hmos.***",
        "app.history.package.path": "",
        "softwareCatagory": {
            "levelFirst": "应用",
            "levelSecond": "影音娱乐",
            "levelThird": "视频"
        },
        "app_path": "D:\\hap\\com.hmos.***.hap",
        "solutionName": "应用上架预检（本地）"
    }   
}
```

<br />

示例2：应用上架预检（本地）------综合自检

```
{
    "taskParams": {
        "sn": [
            "2MM0*****380"
        ],
        "devecoProviderOptions": {},
        "isUploadApp": "true",
        "taskName": "Task-0801-174411",
        "packageName": "com.hmos.***",
        "app.history.package.path": "",
        "softwareCatagory": {
            "levelFirst": "应用",
            "levelSecond": "影音娱乐",
            "levelThird": "视频"
        },
        "app_path": "D:\\hap\\com.hmos.***.hap",
        "solutionName": "应用上架预检（本地）"
    }   
}
```

<br />

#### 测试服务任务产物

在任务结束信息打印日志中\[command task status\] taskPath: ......(即为任务数据存储路径)

打开任务数据存储目录，任务报告html和任务产物（2d_report_data.json）可在 taskPath目录下export文件夹下找到，例如：

![](https://media:901787900073532779 "点击放大")

任务产物（2d_report_data.json）说明如下。  

#### json文件说明文档

#### 场景化性能测试

```
{
      "isTaskPass" : false,
      "generalData" : {
      "taskInfo": { } // 任务基础信息
      "appInfo" : { } // 应用信息 
   },
      "expandData" : [ {
      "serviceType" : "performanceScript",
      "resultSummary" : { } // 整体情况，包含总共操作次数、执行轮次、用例个数、较好体验、一般体验、极优体验等
      "resultDetails": [ ] // 用例详细数据，包含用例id、用例名称、用例执行结果状态、用例步骤详情、用例的资源数据统计等
    }
  ]
}
```

<br />

|-----------|----------|-------------------|
|参数|数据类型|说明|
|isTaskPass|Boolean|任务是否通过|
|generalData|JsonObject|整体信息，包含任务基础信息、应用信息等|
|expandData|Jsonarray|结果详情，包含整体情况、用例详细数据等|

更多参数详情及完整 json文件示例请点击下载：[场景化性能json配置参数查询](https://media:901787900073655782)

<br />

<br />

#### 性能基础质量测试

```
{
       "isTaskPass": false, //任务所有指标是否都达到标准
        "generalData": { //任务参数
        "taskInfo": { }, // 任务参数
        "appInfo": { }//应用信息
    },
    "expandData": [ //结果详情
        {
            "serviceType": "performance",//性能详情
            "resultSummary": {}, // 专项结果总览
            "resultDetails": [] // 用例详细数据，包含用例id、用例名称、用例执行结果状态、用例步骤详情、用例的资源数据统计等
        }
    ]
}
```

<br />

|-----------|----------|-------------------|
|参数|数据类型|说明|
|isTaskPass|Boolean|任务所有指标是否都达到标准|
|generalData|JsonObject|整体信息，包含任务基础信息、应用信息等|
|expandData|Jsonarray|结果详情，包含整体情况、用例详细数据等|

更多参数详情及完整 json文件示例请点击下载：[性能基础json配置参数查询](https://media:901787900073706783)

<br />

<br />

#### 稳定性基础质量测试

```
{
       "isTaskPass": false, //任务所有指标是否都达到标准
        "generalData": { //任务参数
        "taskInfo": { }, // 任务参数
        "appInfo": { }//应用信息
    },
    "expandData": [ //结果详情
        {
            "serviceType": "stability",//稳定性详情
            "resultSummary": {}, // 专项结果总览
            "resultDetails": [] 
        }
    ]
}
```

<br />

|----------|----------|----|
|参数|数据类型|说明|
|taskId|string|任务id|
|taskName|string|任务名称|
|taskPath|string|报告路径|
|taskParams|JsonObject|执行参数|

更多详细参数查询可参考以下文档：[稳定性基础质量json配置参数查询](https://media:901787900073764784)

<br />

<br />

#### 内存泄漏测试

```
{
       "isTaskPass": false, //任务所有指标是否都达到标准
        "generalData": { //任务参数
        "taskInfo": { }, // 任务参数
        "appInfo": { }//应用信息
    },
    "expandData": [ //结果详情
        {
            "serviceType": "performance",//性能详情
            "resultSummary": {}, // 专项结果总览
            "resultDetails": [] 
        }
    ]
}
```

<br />

|----------|------|----------------------|
|参数|数据类型|说明|
|taskId|String|客户端中该任务的id。|
|taskName|String|创建任务时，填写的任务名称。|
|taskType|String|任务类型，固定为内存泄漏测试|
|taskPath|String|测试任务存储数据的文件夹路径。|
|taskParams|Object|在创建任务选择的一些执行参数，详见下方文档。|

更多详细参数查询可参考以下文档：[内存泄漏json配置参数查询](https://media:901787900073807785)

<br />

#### 应用上架预检（本地）

```
{ 
     "isTaskPass": false, //任务所有指标是否都达到标准 
     "generalData": { //任务参数 
         "taskInfo": { 
             "taskId": "0019d332-d92b-457d-8f2d-3e2a30d7c650", //任务id 
             "taskName": "Task-1120-175437", //任务名称 
             "taskPath": "D:\\ProgramData\\DevEco Testing\\xxx\\tasks\\0019d332-d92b-457d-8f2d-3e2a30d7c650", //报告路径 
             "taskParams": {}//执行参数 
         }, 
         "appInfo": {} //应用信息 
     }, 
     "expandData": [ //结果详情 
         { 
             "serviceType": "compatibility",//专项类型 
             "resultSummary": {},//子项结果总览 
             "resultDetails": []//每条规则详情 
         }, 
     ]
 }
```

<br />

|----------|----------|----|
|参数|数据类型|说明|
|taskId|string|任务id|
|taskName|string|任务名称|
|taskPath|string|报告路径|
|taskParams|JsonObject|执行参数|

更多参数详情及完整 json文件示例请点击下载：[上架预检json配置参数查询](https://media:901787900073860786)

<br />

<br />

#### 支持自动清理报告数据

参数示例：

# 不清理（默认）

-cleanupPolicy none # 不清理

<br />

# 按时间保留

-cleanupPolicy 7d # 保留7天

-cleanupPolicy 30d # 保留30天

-cleanupPolicy 90d # 保留90天

<br />

# 按数量保留

-cleanupPolicy 10t # 保留10个任务

-cleanupPolicy 50t # 保留50个任务

-cleanupPolicy 100t # 保留100个任务

<br />

策略一：默认不清理

当传入-cleanupPolicy none参数时，默认不清理。当不传-cleanupPolicy参数时，也是默认不清理。

<br />

策略二：按照天数保留报告数据

当传入-cleanupPolicy 10d参数时，则保留近10天的报告数据，其他报告做清理处理。

天数范围1-100000。

<br />

策略三：按照数量保留报告数据

当传入-cleanupPolicy 10t参数时，则保留近10个的报告数据，其他报告做清理处理。

个数范围1-100000。

<br />

清理数据范围：

清理是为了腾出空间，所以会清理掉报告目录下的大文件资源，例如日志、图片、视频等。

测试数据还是会保留，保留report.json和task.db任务记录、2d_report_data.json、report.html。

<br />

#### 常见报错

#### 系统报错

No value present please check device sn：设备sn号对应的手机没连接

Connection refused: connect ： DevEcoTesting客户端未启动/重启客户端

Error: Could not create the Java Virtual Machine ：命令启动窗口目录错误，需在客户端安装目录下启动，详见[命令行启动测试任务](#section151421712547)  

#### 自定义报错

设备类错误：DT.1001xx  

|---------|----------------------------------------------------|--------|
|错误码|错误信息|错误详情|
|DT.100101|not find device sn, please check device sn!|传入参数sn为空|
|DT.100102|device sn is invalid, please check device sn!|sn正则检测非法|
|DT.100103|device is running task, please check running device!|设备正在执行任务|
|DT.100104|app is not exist|app不存在|

任务类错误:DT.1002xx  

|---------|------------------------------------------|------------|
|错误码|错误信息|错误详情|
|DT.100201|running task has reached the upper limit 4|正在执行任务已达4个上限|
|DT.100202|performance testing only create task once|已存在性能测试任务|
|DT.100203|task dry run failed|任务预执行失败|

公共参数类错误:DT.100301-DT.100306  

|---------|------------------------------------------|------------------|
|错误码|错误信息|错误详情|
|DT.100301|packageName is invalid|packageName正则检测非法|
|DT.100302|solution name is empty! system exit.|传入参数solutionName为空|
|DT.100303|install app path is not exist|installAppPath不存在|
|DT.100304|the param is invalid, please check params!|部分要求检测任务参数非法（时间类）|
|DT.100305|the path is invalid, please check path!|路径参数检测不存在|
|DT.100306|this json file has exception|json文件解析异常|

测试服务参数类错误:DT.100320-DT.100399  

|---------|--------|----------------------------------------------------------------|
|错误码|服务类型|错误信息|
|DT.100320|上架预检参数校验|已安装应用与安装包应用包名不一致|
|DT.100321|上架预检参数校验|输入的设备数超过3台|
|DT.100322|上架预检参数校验|输入的专项执行参数不在可执行范围内|
|DT.100323|上架预检参数校验|选择了兼容性专项但是没有传入安装包路径|
|DT.100324|上架预检参数校验|测试服务无法解析应用包|
|DT.100340|稳定性参数校验|黑名单关键字数量不能超过30个|
|DT.100341|稳定性参数校验|deeplink输入参数不合规：应用没有对应的deeplink链接或者切换概率应该是0-60、切换周期应该为1-10080的整数|
|DT.100342|稳定性参数校验|设备目录权限异常，手动删除设备kingkongDir目录，重启设备|
|DT.100343|稳定性参数校验|appFeaturePath校验失败，文件不存在或者特性名称对应不上|
|DT.100344|稳定性参数校验|测试时长必须是10-60000之间的整数|
|DT.100345|稳定性参数校验|稳定性环境初始化失败|
|DT.100350|性能参数校验|输入参数不能为空|
|DT.100351|性能参数校验|参数 traversalAction 不能为空或者不合法，请检查|
|DT.100352|性能参数校验|参数测试时长为10 - 120之间的整数|
|DT.100353|性能参数校验|参数 startTimes 必须在1-10之间的整数|
|DT.100354|性能参数校验|参数 std 不合法，请检查|
|DT.100355|性能参数校验|参数 watchingKpi 不合法，请检查|
|DT.100356|性能参数校验|参数 executeRounds 必须在1-10之间|
|DT.100357|性能参数校验|参数 caseList 不能为空或者不合法，请检查|
|DT.100358|性能参数校验|文件路径过长，请检查|
|DT.100359|性能参数校验|当前系统剩余运行内存不足|
|DT.100360|性能参数校验|设备存在root目录，请root设备后删除所有临时文件及目录之后，再刷回对外最新系统版本|

测试服务类错误:DT.1004xx  

|---------|--------------------------|-----------------|
|错误码|错误信息|错误详情|
|DT.100401|test service is not exist|测试服务不存在|
|DT.100402|test service update failed|测试服务更新失败|
|DT.100403|query atomic service error|查询原子服务错误（如关联公共资源）|

鉴权证书类错误:DT.1005xx  

|---------|-------------------------------|-----------|
|错误码|错误信息|错误详情|
|DT.100501|cert file is not exist|鉴权证书文件不存在|
|DT.100502|cert file is null|鉴权证书文件为空|
|DT.100503|cert file authentication failed|鉴权证书文件鉴权失败|
|DT.100504|cert file has expired|鉴权证书文件过期|
|DT.100505|cert refresh token failed|证书获取token失败|

环境类错误：DT.1006xx  

|---------|--------------------------------------------------|---------|
|错误码|错误信息|错误详情|
|DT.100601|disk space is less than 10GB, please free up space|磁盘空间小于10G|

网络异常错误码：DT.1007xx  

|---------|-----------------|----|
|错误码|错误信息|错误详情|
|DT.100701|network exception|网络异常|

未知异常错误码：DT.100801  

|---------|-----------------|----|
|错误码|错误信息|错误详情|
|DT.100801|unknown exception|未知异常|

用户未完成登录：DT.100901  

|---------|--------------|-------|
|错误码|错误信息|错误详情|
|DT.100901|user not login|用户未完成登录|

#### 任务结束信息

\[command task status\] taskPath: ......(任务数据存储路径)

\[command task status\]（taskName）...... task state is finish/failed/stop/timeout

\[command task status\] task completed or task stop

任务报告html可在 taskPath目录下export文件下找到，例如：

![](https://media:901787900073569780 "点击放大")

![](https://media:901787900073601781 "点击放大")

<br />

#### 常见问题

（1）如何获取 DevEco Testing 的hdc

客户端解压路径：/DevEco Testing/app/resources/bin目录下

<br />

（2）无法执行file send/recv操作，导致任务执行失败

造成原因：环境中存在多个hdc版本，造成hdc端口有冲突。

解决方案：确保环境中只有一个hdc进程，若docker镜像中有hdc执行，需要进入docker镜像中将hdc进程杀掉（命令：hdc kill）。

保证hdc只有一个server端，即可解决该问题。

<br />
