# 查询和监听音频输出设备

应用可通过以下两种方式管理全局音频输出设备：

* 通常情况下，可以[通过AudioRoutingManager查询和监听音频输出设备](#通过audioroutingmanager查询和监听音频输出设备)。
* 从API version 20开始，AudioSessionManager提供了部分输出设备管理的接口，支持[通过AudioSession查询和监听音频输出设备](#通过audiosession查询和监听音频输出设备)，方便在使用AudioSession管理音频焦点的同时管理音频输出。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioRoutingAndVolumeSample)。  

#### 通过AudioRoutingManager查询和监听音频输出设备

本模块提供音频输出设备管理能力，包括查询设备信息和监听连接状态变化。具体API说明请参考文档[AudioRoutingManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioroutingmanager)。  

#### 创建AudioRoutingManager实例

在使用AudioRoutingManager管理音频设备前，需要先导入模块并创建实例。

```
import { audio } from '@kit.AudioKit';
// ...

let audioManager = audio.getAudioManager();
let audioRoutingManager = audioManager.getRoutingManager();
```

#### 支持的音频输出设备类型

目前支持的输出设备如下表所示：  

|名称|值|说明|
|:---------------|:-|:-----------------------------------------------|
|EARPIECE|1|听筒。|
|SPEAKER|2|扬声器。|
|WIRED_HEADSET|3|有线耳机，带麦克风。|
|WIRED_HEADPHONES|4|有线耳机，无麦克风。|
|BLUETOOTH_SCO|7|蓝牙设备SCO（Synchronous Connection Oriented）连接。|
|BLUETOOTH_A2DP|8|蓝牙设备A2DP（Advanced Audio Distribution Profile）连接。|
|USB_HEADSET|22|USB耳机，带麦克风。|
|NEARLINK|31|星闪设备。|

#### 获取输出设备信息

使用[getDevices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioroutingmanager#getdevices9)方法可以获取当前所有输出设备的信息。

```
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

  audioRoutingManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG).then((audioDeviceDescriptors: audio.
    AudioDeviceDescriptors) => {
    console.info(`Succeeded in getting devices. AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to get devices. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
```

#### 监听设备连接状态变化

设置监听事件以监控设备连接状态的变化，设备连接或断开时触发回调。  
![](https://media:201787905726778292)  
监听设备连接状态变化可以监听到全部的设备连接状态变化，不建议作为应用处理自动暂停的依据。应用如需处理自动暂停相关业务，可参考[音频流输出设备变更原因](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-change#音频流输出设备变更原因)。

```
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

  try {
    // 监听音频输出设备状态变化。
    audioRoutingManager.on('deviceChange', audio.DeviceFlag.OUTPUT_DEVICES_FLAG, (deviceChanged: audio.DeviceChangeAction) => {
      console.info(`Succeeded in using on function. DeviceChangeAction: ${JSON.stringify(deviceChanged)}`);
      // ...
    });
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to use on function. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
```

#### 获取最高优先级输出设备信息

使用[getPreferOutputDeviceForRendererInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioroutingmanager#getpreferoutputdeviceforrendererinfo10)方法，可以获取当前最高优先级的输出设备。  
![](https://media:201787905726805293)  
最高优先级输出设备表示声音将在此设备输出的设备。

```
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, // 音频流使用类型：语音通话。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};
// ...

  audioRoutingManager.getPreferOutputDeviceForRendererInfo(audioRendererInfo).
    then((audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
    console.info(`Succeeded in getting prefer output device for renderer info. AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to get prefer output device for renderer info. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
```

#### 监听最高优先级输出设备变化

```
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, // 音频流使用类型：语音通话。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};
// ...

  try {
    audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', audioRendererInfo, (audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
      console.info(`Succeeded in using on function. DeviceChangeAction: ${JSON.stringify(audioDeviceDescriptors)}`);
      // ...
    });
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to use on function. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
```

#### 通过AudioSession查询和监听音频输出设备

应用使用播放器的SDK播放音频流，不持有[AudioRenderer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiorenderer)对象，因此无法灵活控制播放设备的选择和状态监听。从API version 20开始，AudioSession不仅增加了焦点管理功能，还提供了音频输出设备管理功能，包括设置默认输出设备和监听设备变化。请参考以下文档获取更多信息：

* ArkTS API：[AudioSessionManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager)
* C API：[native_audio_session_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-session-manager-h)  

#### 创建AudioSession实例

在使用AudioSessionManager管理音频设备前，需要先导入模块并创建实例。

```
import { audio } from '@kit.AudioKit';
// ...

let audioManager = audio.getAudioManager();
// ...
let audioSessionManager = audioManager.getSessionManager();
```

#### 设置本机默认音频输出设备

[setDefaultOutputDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#setdefaultoutputdevice20)可以用于设置本机默认输出设备。  
![](https://media:201787905726860294)  
* 由于AudioSession是应用级设置，调用本接口设置默认音频输出设备会覆盖AudioRenderer的setDefaultOutputDevice接口设置的音频输出设备信息。
* 调用setDefaultOutputDevice设置音频输出设备后，如需取消，可将参数设为audio.DeviceType.DEFAULT，将音频设备选择权交还给系统。否则，每次调用activateAudioSession时，应用选择的默认输出设备将生效。

```
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

  // 应用根据业务场景设置适合自己的音频会话场景，激活AudioSession时，系统会根据应用选择的音频会话场景申请对应的音频焦点。
  audioSessionManager.setAudioSessionScene(audio.AudioSessionScene.AUDIO_SESSION_SCENE_VOICE_COMMUNICATION);

  // 设置音频会话策略。
  let strategy: audio.AudioSessionStrategy = {
    concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_MIX_WITH_OTHERS
  };

  // 激活AudioSession。
  audioSessionManager.activateAudioSession(strategy).then(() => {
    console.info('Succeeded in activating audio session.');
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to activate audio session. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
  // ...

  // 设置默认输出设备为扬声器。
  audioSessionManager.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
    console.info('Succeeded in setting default output device.');
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to set default output device. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
  // ...

  // 设置默认输出设备为听筒。
  audioSessionManager.setDefaultOutputDevice(audio.DeviceType.EARPIECE).then(() => {
    console.info('Succeeded in setting default output device.');
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to set default output device. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
```

#### 查询本机默认音频输出设备

应用可以通过[getDefaultOutputDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#getdefaultoutputdevice20)查询本机默认输出设备类型。  
![](https://media:201787905726893295)  
本接口用于查询通过[setDefaultOutputDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#setdefaultoutputdevice20)接口设置的输出设备。

```
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

  try {
    let deviceType = audioSessionManager.getDefaultOutputDevice();
    console.info(`Succeeded in getting default output device. DeviceType: ${deviceType}`);
    // ...
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to get default output device. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
```

#### 监听输出设备变化

应用可以通过注册[CurrentOutputDeviceChangedEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#currentoutputdevicechangedevent20)监听输出设备的连接状态变化。  
![](https://media:201787905726920296)  
currentOutputDeviceChangedCallback包含设备变更的原因及推荐的后续操作。应用应根据不同的变更原因进行处理，并按系统推荐的操作继续或停止当前播放。

```
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

let currentOutputDeviceChangedCallback = (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
  console.info(`Succeeded in using on or off function. CurrentOutputDeviceChangedEvent: ${JSON.stringify(currentOutputDeviceChangedEvent)}`);
  // ...

  switch (currentOutputDeviceChangedEvent.changeReason) {
    case audio.AudioStreamDeviceChangeReason.REASON_OLD_DEVICE_UNAVAILABLE:
      // 响应设备不可用事件，如果应用处于播放状态，应暂停播放，更新UX界面。
      break;
    case audio.AudioStreamDeviceChangeReason.REASON_NEW_DEVICE_AVAILABLE:
      // 应用根据业务情况响应设备可用事件。
      break;
    case audio.AudioStreamDeviceChangeReason.REASON_OVERRODE:
      // 应用根据业务情况响应设备强选事件。
      break;
    case audio.AudioStreamDeviceChangeReason.REASON_SESSION_ACTIVATED:
      // 应用根据业务情况响应audioSession激活时的输出设备信息。
      break;
    case audio.AudioStreamDeviceChangeReason.REASON_STREAM_PRIORITY_CHANGED:
      // 应用根据业务情况响应其它更高优先级的音频流触发的设备变更事件。
      break;
    case audio.AudioStreamDeviceChangeReason.REASON_UNKNOWN:
      // 应用根据业务情况响应未知原因事件。
      break;
  }
};
// ...

  try {
    audioSessionManager.on('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to use on function. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
```
