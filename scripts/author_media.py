#!/usr/bin/env python3
"""Author the media domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "media_pipeline_stage"


def leaf(f, fid, parent, axis, zh, en, definition, includes, excludes, bindings, legacy=None, level="L3", privacy="none"):
    f.append(feature(
        fid, parent=parent, level=level, zh=zh, en=en, definition=definition,
        includes=includes, excludes=excludes, sibling_axis=axis,
        granularity="atomic", bindings=bindings,
        legacy=legacy or {"disposition": "new", "sources": []},
        privacy_class=privacy,
    ))


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "media", parent=None, level="L1",
        zh="媒体", en="Media",
        definition="音视频播放与会话、音频渲染、采集录制、编解码、图像、媒体库、DRM、编辑、元数据与扫码识别。",
        includes=["playback、session、audio、capture、recording、codec、image、library、drm、editing、metadata、scan"],
        excludes=["telecom 通话音频路由业务", "connectivity 蓝牙 A2DP 链路本身", "ui 图像控件展示"],
        legacy={"disposition": "kept", "sources": ["media"]},
    ))

    l2 = [
        ("media.playback", "媒体播放", "Media Playback",
         "音视频播放器、流媒体、字幕与目录播放。",
         ["audio、video、streaming、subtitle、catalog"],
         ["播控会话见 media.session", "编解码管线见 media.codec"],
         ["media.playback"]),
        ("media.session", "播控会话", "Playback Session",
         "媒体会话元数据、远端命令、音频焦点与跨端投播。",
         ["metadata、commands、focus、distributed"],
         ["播放器内核见 media.playback"],
         []),
        ("media.audio", "音频渲染与处理", "Audio Render and Processing",
         "低层音频渲染、短音、音效、空间音频与 MIDI 消息。",
         ["render、short_sounds、effects、spatial、midi"],
         ["播放器见 playback.audio", "麦克风采集见 capture.microphone"],
         []),
        ("media.capture", "媒体采集", "Media Capture",
         "相机管线、麦克风采集与系统相机委托。",
         ["camera、microphone、system_camera"],
         ["录制封装见 media.recording"],
         ["media.capture"]),
        ("media.recording", "媒体录制", "Media Recording",
         "音视频文件录制与屏幕采集录制。",
         ["av、screen"],
         ["相机预览见 capture.camera"],
         []),
        ("media.codec", "编解码", "Codecs",
         "音视频编解码、容器复用/解复用与硬件编解码能力。",
         ["audio、video、container、hardware"],
         ["播放器封装见 playback"],
         ["media.codec"]),
        ("media.image", "图像编解码", "Image Codec",
         "静图/动图编解码、像素缓冲与图像效果。",
         ["decode、encode、pixel、effects"],
         ["图库资产见 media.library", "UI Image 控件见 ui.controls.image"],
         []),
        ("media.library", "媒体库", "Media Library",
         "系统相册浏览、选择器、保存与资产管理。",
         ["browse、picker、save、manage"],
         ["文件通用存储见 storage"],
         ["media.library"]),
        ("media.drm", "数字版权保护", "DRM",
         "许可证获取与受保护内容播放集成。",
         ["license、playback"],
         ["普通播放见 media.playback"],
         []),
        ("media.editing", "媒体编辑", "Media Editing",
         "视频合成编辑与转码导出。",
         ["video、transcode"],
         ["单次编码见 media.codec"],
         []),
        ("media.metadata", "媒体元数据", "Media Metadata",
         "容器元数据提取、缩略图与 EXIF。",
         ["extraction、thumbnail、exif"],
         ["会话 Now Playing 见 media.session.metadata"],
         []),
        ("media.scan", "码与视觉扫描", "Code and Visual Scan",
         "二维码/条码等视觉码识别入口。",
         ["detect"],
         ["通用 ML 视觉见 ai"],
         []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        f.append(feature(
            fid, parent="media", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy={"disposition": "kept" if sources and sources[0] == fid else ("new" if not sources else "merged_from"),
                    "sources": sources},
        ))

    # playback
    leaf(f, "media.playback.audio", "media.playback", "playback_kind",
         "音频播放", "Audio Playback",
         "本地或流式音频的播放器准备、传输控制与音量。",
         ["MediaPlayer/AVPlayer 音频源与 transport"], ["视频见 playback.video", "焦点见 session.focus"],
         merge_bindings(
             A("MediaPlayer", "https://developer.android.com/reference/android/media/MediaPlayer"),
             I("AVAudioPlayer", "https://developer.apple.com/documentation/avfoundation/avaudioplayer", "class"),
             H("AVPlayer", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media"),
         ),
         {"disposition": "kept", "sources": ["media.playback.audio"]}, privacy="runtime_permission")
    leaf(f, "media.playback.video", "media.playback", "playback_kind",
         "视频播放", "Video Playback",
         "视频画面输出、首帧与显示模式控制。",
         ["ExoPlayer/AVPlayer 视频、surface/PlayerView"], ["纯音频见 playback.audio"],
         merge_bindings(
             A("ExoPlayer", "https://developer.android.com/media/media3/exoplayer", "guide"),
             I("AVPlayer", "https://developer.apple.com/documentation/avfoundation/avplayer", "class"),
             H("AVPlayer / Video", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-playback"),
         ),
         {"disposition": "kept", "sources": ["media.playback.video"]})
    leaf(f, "media.playback.streaming", "media.playback", "playback_kind",
         "自适应与流式播放", "Adaptive and Streaming Playback",
         "HLS/DASH 等自适应流与直播/渐进式流播放。",
         ["HlsMediaSource/DashMediaSource、AVPlayer 流 URL"], ["本地文件见 audio/video"],
         merge_bindings(
             A("HlsMediaSource", "https://developer.android.com/media/media3/exoplayer/hls", "guide"),
             I("HTTP Live Streaming", "https://developer.apple.com/documentation/http-live-streaming", "guide"),
             H("AVPlayer 流媒体", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-playback"),
         ))
    leaf(f, "media.playback.subtitle", "media.playback", "playback_kind",
         "字幕与字幕轨", "Subtitles and Caption Tracks",
         "内嵌/外挂字幕轨选择与系统字幕呈现设置。",
         ["subtitle tracks、MediaAccessibility"], ["视频画面见 playback.video"],
         merge_bindings(
             A("Subtitle support (Media3)", "https://developer.android.com/media/media3/exoplayer/subtitles", "guide"),
             I("MediaAccessibility", "https://developer.apple.com/documentation/mediaaccessibility", "framework"),
             H("AVPlayer 字幕", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media"),
         ))
    leaf(f, "media.playback.catalog", "media.playback", "playback_kind",
         "媒体目录播放", "Catalog Playback",
         "系统/平台媒体目录检索授权与目录项播放。",
         ["MusicKit/ApplicationMusicPlayer 等目录播放"], ["通用 URL 播放见 audio"],
         merge_bindings(
             pending("android"),
             I("MusicKit", "https://developer.apple.com/documentation/musickit", "framework"),
             pending("harmonyos"),
         ))

    # session
    leaf(f, "media.session.metadata", "media.session", "session_capability",
         "会话元数据与播放状态", "Session Metadata and State",
         "向系统发布 Now Playing 元数据、队列与播放状态。",
         ["MediaSession metadata、MPNowPlayingInfoCenter、AVSession.setMetadata"],
         ["远端命令见 session.commands"],
         merge_bindings(
             A("MediaSession", "https://developer.android.com/reference/android/media/session/MediaSession"),
             I("MPNowPlayingInfoCenter", "https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter", "class"),
             H("AVSession.setAVMetadata", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-avsession"),
         ))
    leaf(f, "media.session.commands", "media.session", "session_capability",
         "远端播控命令", "Remote Playback Commands",
         "媒体键与会话控制器对播放/暂停等的命令通道。",
         ["MediaSession.Callback、MPRemoteCommandCenter、AVSessionController"],
         ["元数据发布见 metadata"],
         merge_bindings(
             A("MediaButtonReceiver", "https://developer.android.com/reference/androidx/media/session/MediaButtonReceiver"),
             I("MPRemoteCommandCenter", "https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter", "class"),
             H("AVSessionController", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-avsession"),
         ))
    leaf(f, "media.session.focus", "media.session", "session_capability",
         "音频焦点与打断", "Audio Focus and Interruption",
         "请求/放弃音频焦点并处理打断与混音策略。",
         ["AudioFocusRequest、AVAudioSession interruption、StreamUsage"],
         ["播放器本身见 playback"],
         merge_bindings(
             A("AudioFocusRequest", "https://developer.android.com/reference/android/media/AudioFocusRequest"),
             I("AVAudioSession", "https://developer.apple.com/documentation/avfoundation/avaudiosession", "class"),
             H("AudioInterrupt / StreamUsage", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-concurrency"),
         ), privacy="runtime_permission")
    leaf(f, "media.session.distributed", "media.session", "session_capability",
         "投播与分布式播控", "Casting and Distributed Playback",
         "路由到远端设备的投播、共享播放会话。",
         ["MediaRouter/Cast、SharePlay、AVSession 投播"],
         ["本机会话见 metadata/commands"],
         merge_bindings(
             A("MediaRouter", "https://developer.android.com/guide/topics/media/mediarouter", "guide"),
             I("GroupActivities", "https://developer.apple.com/documentation/groupactivities", "framework"),
             H("AVSession 投播", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-overview"),
         ))

    # audio
    leaf(f, "media.audio.render", "media.audio", "audio_capability",
         "PCM音频渲染", "PCM Audio Rendering",
         "低延迟/流式 PCM 音频输出渲染。",
         ["AAudio/Oboe、AVAudioEngine、AudioRenderer"],
         ["高层播放器见 playback.audio"],
         merge_bindings(
             A("AAudio", "https://developer.android.com/ndk/guides/audio/aaudio/aaudio", "guide"),
             I("AVAudioEngine", "https://developer.apple.com/documentation/avfoundation/avaudioengine", "class"),
             H("AudioRenderer", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiorenderer-for-playback"),
         ), privacy="runtime_permission")
    leaf(f, "media.audio.short_sounds", "media.audio", "audio_capability",
         "短音频与音效池", "Short Sounds and Sound Pool",
         "短促音效池与系统提示音生成播放。",
         ["SoundPool、SystemSound、SoundPlayer"],
         ["长音频见 playback.audio"],
         merge_bindings(
             A("SoundPool", "https://developer.android.com/reference/android/media/SoundPool"),
             I("AudioServicesPlaySystemSound", "https://developer.apple.com/documentation/audiotoolbox/1405245-audioservicesplaysystemsound", "function"),
             H("SoundPool", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media"),
         ))
    leaf(f, "media.audio.effects", "media.audio", "audio_capability",
         "音频音效处理", "Audio Effects",
         "均衡、动态范围、回声消除等音频效果链路。",
         ["AudioEffect/Equalizer、AVAudioUnit、音效 API"],
         ["空间音频见 spatial"],
         merge_bindings(
             A("AudioEffect", "https://developer.android.com/reference/android/media/audiofx/AudioEffect"),
             I("AVAudioUnitEffect", "https://developer.apple.com/documentation/avfoundation/avaudiouniteffect", "class"),
             H("音频音效", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-effect-management"),
         ))
    leaf(f, "media.audio.spatial", "media.audio", "audio_capability",
         "空间音频", "Spatial Audio",
         "空间化混音、头部追踪与空间场景查询。",
         ["spatial AudioAttributes、PHASE、空间音频管理"],
         ["普通立体声渲染见 render"],
         merge_bindings(
             A("Spatial audio", "https://developer.android.com/guide/topics/media/spatial-audio", "guide"),
             I("PHASE", "https://developer.apple.com/documentation/phase", "framework"),
             H("空间音频管理", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-audio"),
         ))
    leaf(f, "media.audio.midi", "media.audio", "audio_capability",
         "MIDI消息与端口", "MIDI Messaging and Ports",
         "MIDI 端口连接与消息收发（音频消息面）。",
         ["MidiManager、CoreMIDI、@ohos.multimedia.midi"],
         ["MIDI 设备发现总线见 connectivity.peripherals"],
         merge_bindings(
             A("MidiManager", "https://developer.android.com/reference/android/media/midi/MidiManager"),
             I("CoreMIDI", "https://developer.apple.com/documentation/coremidi", "framework"),
             H("@ohos.multimedia.midi", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-midi"),
         ))

    # capture
    leaf(f, "media.capture.camera", "media.capture", "capture_source",
         "相机捕获管线", "Camera Capture Pipeline",
         "相机设备会话、预览、拍照与视频流控制。",
         ["CameraX/Camera2、AVCaptureSession、@ohos.multimedia.camera"],
         ["系统相机 Intent 见 system_camera", "录制封装见 recording.av"],
         merge_bindings(
             A("CameraX", "https://developer.android.com/media/camera/camerax", "guide"),
             I("AVCaptureSession", "https://developer.apple.com/documentation/avfoundation/avcapturesession", "class"),
             H("@ohos.multimedia.camera", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-camera"),
         ),
         {"disposition": "kept", "sources": ["media.capture.camera"]}, privacy="runtime_permission")
    leaf(f, "media.capture.microphone", "media.capture", "capture_source",
         "麦克风录音采集", "Microphone Capture",
         "麦克风 PCM/音频流采集与预处理入口。",
         ["AudioRecord、AVAudioEngine input、AudioCapturer"],
         ["文件录制见 recording.av"],
         merge_bindings(
             A("AudioRecord", "https://developer.android.com/reference/android/media/AudioRecord"),
             I("AVAudioEngine input", "https://developer.apple.com/documentation/avfoundation/avaudioengine", "class"),
             H("AudioCapturer", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiocapturer-for-recording"),
         ),
         {"disposition": "kept", "sources": ["media.capture.microphone"]}, privacy="runtime_permission")
    leaf(f, "media.capture.system_camera", "media.capture", "capture_source",
         "系统相机委托", "System Camera Delegation",
         "拉起系统相机应用完成拍照/录像并回传结果。",
         ["ACTION_IMAGE_CAPTURE、UIImagePickerController、CameraPicker"],
         ["应用内相机管线见 camera"],
         merge_bindings(
             A("MediaStore.ACTION_IMAGE_CAPTURE", "https://developer.android.com/reference/android/provider/MediaStore#ACTION_IMAGE_CAPTURE", "constant"),
             I("UIImagePickerController", "https://developer.apple.com/documentation/uikit/uiimagepickercontroller", "class"),
             H("CameraPicker", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-camera-picker"),
         ), privacy="runtime_permission")
    leaf(f, "media.capture.camera.photo", "media.capture.camera", "camera_capability",
         "拍照输出", "Still Photo Capture",
         "静止图像捕获与拍照参数控制。",
         ["ImageCapture、AVCapturePhotoOutput"],
         ["视频流见 video_stream"],
         merge_bindings(
             A("ImageCapture", "https://developer.android.com/reference/androidx/camera/core/ImageCapture"),
             I("AVCapturePhotoOutput", "https://developer.apple.com/documentation/avfoundation/avcapturephotooutput", "class"),
             H("PhotoOutput", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-shooting"),
         ), level="L4", privacy="runtime_permission")
    leaf(f, "media.capture.camera.video_stream", "media.capture.camera", "camera_capability",
         "相机视频流", "Camera Video Stream",
         "相机连续视频帧/录像流输出。",
         ["VideoCapture、AVCaptureMovieFileOutput/VideoDataOutput"],
         ["拍照见 photo"],
         merge_bindings(
             A("VideoCapture", "https://developer.android.com/reference/androidx/camera/video/VideoCapture"),
             I("AVCaptureMovieFileOutput", "https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput", "class"),
             H("VideoOutput", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-recording"),
         ), level="L4", privacy="runtime_permission")
    # camera is both kept legacy atomic historically - but now has children so must be branch
    for node in f:
        if node["id"] == "media.capture.camera":
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            node["knowledge_path"] = "knowledge/media/capture/camera/_rollup.yaml"

    # recording
    leaf(f, "media.recording.av", "media.recording", "recording_kind",
         "音视频文件录制", "AV File Recording",
         "将音视频编码写入容器文件的录制控制。",
         ["MediaRecorder、AVRecorder、AVAssetWriter"],
         ["屏幕录制见 recording.screen"],
         merge_bindings(
             A("MediaRecorder", "https://developer.android.com/reference/android/media/MediaRecorder"),
             I("AVAssetWriter", "https://developer.apple.com/documentation/avfoundation/avassetwriter", "class"),
             H("AVRecorder", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media"),
         ), privacy="runtime_permission")
    leaf(f, "media.recording.screen", "media.recording", "recording_kind",
         "屏幕录制与投射", "Screen Recording and Projection",
         "屏幕内容采集授权、虚拟显示与写文件录制。",
         ["MediaProjection、ReplayKit、AVScreenCapture"],
         ["相机录像见 capture.camera"],
         merge_bindings(
             A("MediaProjection", "https://developer.android.com/reference/android/media/projection/MediaProjection"),
             I("RPScreenRecorder", "https://developer.apple.com/documentation/replaykit/rpscreenrecorder", "class"),
             H("AVScreenCapture", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-avscreencapture"),
         ), privacy="runtime_permission")
    # codec
    leaf(f, "media.codec.hardware", "media.codec", "codec_surface",
         "硬件编解码", "Hardware Codec",
         "查询并使用硬件加速的编解码器实例。",
         ["MediaCodecInfo hardware、VT*Session、硬件 AVCodec"],
         ["软件编解码同属 codec 子能力"],
         merge_bindings(
             A("MediaCodec", "https://developer.android.com/reference/android/media/MediaCodec"),
             I("VideoToolbox", "https://developer.apple.com/documentation/videotoolbox", "framework"),
             H("mediaAVCodec", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaavcodec"),
         ),
         {"disposition": "kept", "sources": ["media.codec.hardware"]})
    leaf(f, "media.codec.audio", "media.codec", "codec_surface",
         "音频编解码", "Audio Codec",
         "音频裸流编码与解码。",
         ["MediaCodec audio、AudioEncoder/Decoder"],
         ["容器复用见 container"],
         merge_bindings(
             A("MediaCodec (audio)", "https://developer.android.com/reference/android/media/MediaCodec"),
             I("AVAudioConverter", "https://developer.apple.com/documentation/avfoundation/avaudioconverter", "class"),
             H("AudioEncoder / AudioDecoder", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaavcodec"),
         ))
    leaf(f, "media.codec.video", "media.codec", "codec_surface",
         "视频编解码", "Video Codec",
         "视频裸流编码、解码与能力查询。",
         ["MediaCodec video、VTCompression/DecompressionSession"],
         ["硬件偏好见 hardware"],
         merge_bindings(
             A("MediaCodec (video)", "https://developer.android.com/reference/android/media/MediaCodec"),
             I("VTCompressionSession", "https://developer.apple.com/documentation/videotoolbox/vtcompressionsession", "class"),
             H("VideoEncoder / VideoDecoder", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaavcodec"),
         ))
    leaf(f, "media.codec.container", "media.codec", "codec_surface",
         "容器复用与解复用", "Container Mux and Demux",
         "音视频轨写入/读取容器格式。",
         ["MediaMuxer/MediaExtractor、AVAssetReader/Writer、AVMuxer/AVDemuxer"],
         ["裸流编解码见 audio/video"],
         merge_bindings(
             A("MediaMuxer", "https://developer.android.com/reference/android/media/MediaMuxer"),
             I("AVAssetReader", "https://developer.apple.com/documentation/avfoundation/avassetreader", "class"),
             H("AVMuxer / AVDemuxer", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/native-apis-avmuxer"),
         ))

    # image
    leaf(f, "media.image.decode", "media.image", "image_capability",
         "图像解码", "Image Decode",
         "静图与动图解码为可渲染缓冲。",
         ["BitmapFactory/ImageDecoder、CGImageSource、ImageSource"],
         ["编码见 encode"],
         merge_bindings(
             A("ImageDecoder", "https://developer.android.com/reference/android/graphics/ImageDecoder"),
             I("CGImageSource", "https://developer.apple.com/documentation/imageio/cgimagesource-q0e", "type"),
             H("ImageSource", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-image"),
         ))
    leaf(f, "media.image.encode", "media.image", "image_capability",
         "图像编码", "Image Encode",
         "将像素编码为静图/动图文件或数据。",
         ["Bitmap.compress、CGImageDestination、ImagePacker"],
         ["解码见 decode"],
         merge_bindings(
             A("Bitmap.compress", "https://developer.android.com/reference/android/graphics/Bitmap#compress(android.graphics.Bitmap.CompressFormat,%20int,%20java.io.OutputStream)", "method"),
             I("CGImageDestination", "https://developer.apple.com/documentation/imageio/cgimagedestination-q2e", "type"),
             H("ImagePacker", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-image"),
         ))
    leaf(f, "media.image.pixel", "media.image", "image_capability",
         "像素缓冲访问", "Pixel Buffer Access",
         "像素图读写、变换与跨模块共享。",
         ["Bitmap/PixelMap、CVPixelBuffer、IOSurface"],
         ["编解码见 decode/encode"],
         merge_bindings(
             A("Bitmap", "https://developer.android.com/reference/android/graphics/Bitmap"),
             I("CVPixelBuffer", "https://developer.apple.com/documentation/corevideo/cvpixelbuffer-q2e", "type"),
             H("PixelMap", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-image"),
         ))
    leaf(f, "media.image.effects", "media.image", "image_capability",
         "图像效果处理", "Image Effects",
         "滤镜、色彩转换与增强类图像效果。",
         ["RenderScript/Effect、Core Image、ImageEffect"],
         ["UI 主题模糊见 ui.theme.visual_effects"],
         merge_bindings(
             A("RenderEffect", "https://developer.android.com/reference/android/graphics/RenderEffect"),
             I("Core Image", "https://developer.apple.com/documentation/coreimage", "framework"),
             H("ImageEffect", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-imageeffect"),
         ))

    # library
    leaf(f, "media.library.browse", "media.library", "library_capability",
         "媒体库浏览查询", "Media Library Browse",
         "查询相册集合与资产属性/原始数据。",
         ["MediaStore/PhotoKit fetch、photoAccessHelper query"],
         ["系统选择器 UI 见 picker"],
         merge_bindings(
             A("MediaStore", "https://developer.android.com/reference/android/provider/MediaStore"),
             I("PHAsset", "https://developer.apple.com/documentation/photokit/phasset", "class"),
             H("photoAccessHelper", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-photoaccesshelper"),
         ), privacy="runtime_permission")
    leaf(f, "media.library.picker", "media.library", "library_capability",
         "系统媒体选择器", "System Media Picker",
         "系统提供的照片/视频选择 UI 与结果回传。",
         ["Photo Picker、PHPicker、PhotoViewPicker"],
         ["程序化浏览见 browse"],
         merge_bindings(
             A("Photo picker", "https://developer.android.com/training/data-storage/shared/photopicker", "guide"),
             I("PHPickerViewController", "https://developer.apple.com/documentation/photosui/phpickerviewcontroller", "class"),
             H("PhotoViewPicker", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-photoviewpicker"),
         ),
         {"disposition": "kept", "sources": ["media.library.picker"]}, privacy="runtime_permission")
    leaf(f, "media.library.save", "media.library", "library_capability",
         "保存到媒体库", "Save to Media Library",
         "将新媒体写入系统相册/媒体库并处理授权。",
         ["MediaStore insert、PHPhotoLibrary performChanges、SaveButton"],
         ["选择见 picker"],
         merge_bindings(
             A("MediaStore inserts", "https://developer.android.com/training/data-storage/shared/media#add-item", "guide"),
             I("PHAssetChangeRequest", "https://developer.apple.com/documentation/photokit/phassetchangerequest", "class"),
             H("photoAccessHelper createAsset", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-save"),
         ), privacy="runtime_permission")
    leaf(f, "media.library.manage", "media.library", "library_capability",
         "媒体资产管理", "Media Asset Management",
         "删除、相册成员关系、属性写回与变更观察。",
         ["delete/update assets、change observer"],
         ["只读浏览见 browse"],
         merge_bindings(
             A("ContentResolver.delete", "https://developer.android.com/training/data-storage/shared/media#remove-item", "guide"),
             I("PHPhotoLibrary.performChanges", "https://developer.apple.com/documentation/photokit/phphotolibrary", "class"),
             H("photoAccessHelper 管理", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-management"),
         ), privacy="runtime_permission")

    # drm
    leaf(f, "media.drm.license", "media.drm", "drm_capability",
         "DRM许可证", "DRM License",
         "密钥系统发现、许可证请求与离线密钥。",
         ["MediaDrm、MediaKeySystem"],
         ["受保护播放见 drm.playback"],
         merge_bindings(
             A("MediaDrm", "https://developer.android.com/reference/android/media/MediaDrm"),
             pending("ios", "FairPlay 通常经 AVContentKeySession"),
             H("MediaKeySystem", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-drm"),
         ))
    leaf(f, "media.drm.playback", "media.drm", "drm_capability",
         "受保护内容播放", "Protected Content Playback",
         "将 DRM 会话与播放器/安全解码集成。",
         ["ExoPlayer DRM、AVContentKeySession、AVPlayer DRM"],
         ["许可证获取见 license"],
         merge_bindings(
             A("ExoPlayer DRM", "https://developer.android.com/media/media3/exoplayer/drm", "guide"),
             I("AVContentKeySession", "https://developer.apple.com/documentation/avfoundation/avcontentkeysession", "class"),
             H("AVPlayer DRM", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avplayer-drm"),
         ))
    # editing
    leaf(f, "media.editing.video", "media.editing", "editing_capability",
         "视频合成编辑", "Video Composition Editing",
         "多片段时间线、特效与合成导出。",
         ["Media3 Transformer、AVFoundation composition、视频编辑预研"],
         ["单纯转码见 transcode"],
         merge_bindings(
             A("Transformer", "https://developer.android.com/media/media3/transformer", "guide"),
             I("AVMutableComposition", "https://developer.apple.com/documentation/avfoundation/avmutablecomposition", "class"),
             H("AVEditor / 视频处理", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-processing"),
         ))
    leaf(f, "media.editing.transcode", "media.editing", "editing_capability",
         "媒体转码", "Media Transcode",
         "格式/码率兼容性转码与任务控制。",
         ["compatible media transcoding、AVTranscoder"],
         ["创作型时间线见 video"],
         merge_bindings(
             A("Compatible media transcoding", "https://developer.android.com/guide/topics/media/transcoding", "guide"),
             I("AVAssetExportSession", "https://developer.apple.com/documentation/avfoundation/avassetexportsession", "class"),
             H("AVTranscoder", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media"),
         ))

    # metadata
    leaf(f, "media.metadata.extraction", "media.metadata", "metadata_capability",
         "容器元数据提取", "Container Metadata Extraction",
         "从媒体容器提取时长、封面、网络源与定时元数据。",
         ["MediaMetadataRetriever、AVAsset、AVMetadataExtractor"],
         ["EXIF 静图见 exif"],
         merge_bindings(
             A("MediaMetadataRetriever", "https://developer.android.com/reference/android/media/MediaMetadataRetriever"),
             I("AVAsset", "https://developer.apple.com/documentation/avfoundation/avasset", "class"),
             H("AVMetadataExtractor", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media"),
         ))
    leaf(f, "media.metadata.thumbnail", "media.metadata", "metadata_capability",
         "缩略图生成", "Thumbnail Generation",
         "资产默认缩略图、指定时间帧与缓存。",
         ["ThumbnailUtils、PHCachingImageManager、AVImageGenerator"],
         ["元数据字段见 extraction"],
         merge_bindings(
             A("ThumbnailUtils", "https://developer.android.com/reference/android/media/ThumbnailUtils"),
             I("PHCachingImageManager", "https://developer.apple.com/documentation/photokit/phcachingimagemanager", "class"),
             H("AVImageGenerator", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media"),
         ))
    leaf(f, "media.metadata.exif", "media.metadata", "metadata_capability",
         "EXIF读写", "EXIF Read Write",
         "图像 EXIF/GPS 等元数据读写。",
         ["ExifInterface、ImageIO EXIF、ExifMetadata"],
         ["容器级元数据见 extraction"],
         merge_bindings(
             A("ExifInterface", "https://developer.android.com/reference/androidx/exifinterface/media/ExifInterface"),
             I("ImageIO EXIF", "https://developer.apple.com/documentation/imageio", "framework"),
             H("ExifMetadata", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-image"),
         ))

    # scan
    leaf(f, "media.scan.detect", "media.scan", "scan_capability",
         "码识别检测", "Barcode Detection",
         "相机流或静图上的条码/二维码识别。",
         ["ML Kit barcode、Vision、ScanKit"],
         ["通用相机预览见 capture.camera"],
         merge_bindings(
             A("BarcodeScanning", "https://developers.google.com/ml-kit/vision/barcode-scanning", "guide"),
             I("VNDetectBarcodesRequest", "https://developer.apple.com/documentation/vision/vndetectbarcodesrequest", "class"),
             H("ScanKit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-api"),
         ), privacy="runtime_permission")

    # Expand atomics under branches
    leaf(f, "media.playback.audio.background", "media.playback.audio", "playback_audio_detail",
         "后台音频续播", "Background Audio Continuity",
         "应用退到后台时维持音频播放会话。",
         ["foreground service / background modes / AVSession 续播"],
         ["焦点策略见 session.focus"],
         merge_bindings(
             A("Media playback background", "https://developer.android.com/media/media3/session/background-playback", "guide"),
             I("UIBackgroundModes audio", "https://developer.apple.com/documentation/bundleresources/information-property-list/uibackgroundmodes/audio", "guide"),
             H("AVSession 后台", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-overview"),
         ), level="L4", privacy="runtime_permission")
    leaf(f, "media.playback.audio.transport", "media.playback.audio", "playback_audio_detail",
         "音频播放传输控制", "Audio Transport Controls",
         "播放/暂停/寻道等传输控制。",
         ["start/pause/seek"],
         ["后台续播见 background"],
         merge_bindings(
             A("MediaPlayer.start", "https://developer.android.com/reference/android/media/MediaPlayer#start()", "method"),
             I("AVAudioPlayer.play", "https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389463-play", "method"),
             H("AVPlayer.play / pause", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media"),
         ), level="L4")
    leaf(f, "media.playback.video.surface", "media.playback.video", "playback_video_detail",
         "视频画面输出表面", "Video Surface Output",
         "将解码画面绑定到 Surface/视图输出。",
         ["SurfaceView/PlayerView、AVPlayerLayer、XComponent"],
         ["字幕见 playback.subtitle"],
         merge_bindings(
             A("PlayerView", "https://developer.android.com/reference/androidx/media3/ui/PlayerView"),
             I("AVPlayerLayer", "https://developer.apple.com/documentation/avfoundation/avplayerlayer", "class"),
             H("AVPlayer 画面", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-playback"),
         ), level="L4")
    leaf(f, "media.playback.video.display_mode", "media.playback.video", "playback_video_detail",
         "视频显示模式", "Video Display Mode",
         "缩放填充、裁剪与宽高比显示模式。",
         ["resize mode / videoScaleMode"],
         ["表面绑定见 surface"],
         merge_bindings(
             A("AspectRatioFrameLayout", "https://developer.android.com/reference/androidx/media3/ui/AspectRatioFrameLayout"),
             I("videoGravity", "https://developer.apple.com/documentation/avfoundation/avplayerlayer/1385819-videogravity", "property"),
             H("VideoScaleMode", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media"),
         ), level="L4")
    for node in f:
        if node["id"] in {"media.playback.audio", "media.playback.video"}:
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            parts = node["id"].split(".")
            node["knowledge_path"] = "knowledge/" + "/".join(parts) + "/_rollup.yaml"

    leaf(f, "media.session.metadata.queue", "media.session.metadata", "session_meta_detail",
         "播放队列", "Playback Queue",
         "向系统会话发布可浏览/可跳转的播放队列。",
         ["queue items / now playing queue"],
         ["单条元数据见 now_playing"],
         merge_bindings(
             A("MediaSession.setQueue", "https://developer.android.com/reference/android/media/session/MediaSession#setQueue(java.util.List%3Candroid.media.session.MediaSession.QueueItem%3E)", "method"),
             I("MPMediaItem queue", "https://developer.apple.com/documentation/mediaplayer", "framework"),
             H("AVSession queue", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-avsession"),
         ), level="L4")
    leaf(f, "media.session.metadata.now_playing", "media.session.metadata", "session_meta_detail",
         "正在播放信息", "Now Playing Info",
         "标题/封面等正在播放条目元数据发布。",
         ["setMetadata / nowPlayingInfo"],
         ["队列见 queue"],
         merge_bindings(
             A("MediaMetadataCompat", "https://developer.android.com/reference/android/support/v4/media/MediaMetadataCompat"),
             I("MPNowPlayingInfoCenter.nowPlayingInfo", "https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/1621769-nowplayinginfo", "property"),
             H("AVMetadata", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-avsession"),
         ), level="L4")
    leaf(f, "media.session.focus.interrupt", "media.session.focus", "focus_detail",
         "音频打断处理", "Audio Interrupt Handling",
         "处理来电等导致的音频打断与恢复。",
         ["onAudioFocusChange、interruptionNotification"],
         ["焦点请求见父节点"],
         merge_bindings(
             A("OnAudioFocusChangeListener", "https://developer.android.com/reference/android/media/AudioManager.OnAudioFocusChangeListener"),
             I("AVAudioSession.interruptionNotification", "https://developer.apple.com/documentation/avfoundation/avaudiosession/1616596-interruptionnotification", "type"),
             H("AudioInterrupt", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-concurrency"),
         ), level="L4", privacy="runtime_permission")
    for node in f:
        if node["id"] in {"media.session.metadata", "media.session.focus"}:
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            parts = node["id"].split(".")
            node["knowledge_path"] = "knowledge/" + "/".join(parts) + "/_rollup.yaml"

    leaf(f, "media.library.picker.selection_mode", "media.library.picker", "picker_detail",
         "选择器选择模式", "Picker Selection Mode",
         "单选/多选等选择器模式配置。",
         ["max selection"],
         ["类型过滤见 type_filter"],
         merge_bindings(
             A("PickVisualMediaRequest", "https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.PickVisualMedia"),
             I("PHPickerConfiguration", "https://developer.apple.com/documentation/photosui/phpickerconfiguration", "class"),
             H("PhotoSelectOptions", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-photoviewpicker"),
         ), level="L4", privacy="runtime_permission")
    leaf(f, "media.library.picker.type_filter", "media.library.picker", "picker_detail",
         "选择器类型过滤", "Picker Type Filter",
         "按照片/视频/直播图等类型过滤可选资产。",
         ["mime/type filter、PHPickerFilter"],
         ["选择模式见 selection_mode"],
         merge_bindings(
             A("ActivityResultContracts.PickVisualMedia", "https://developer.android.com/training/data-storage/shared/photopicker", "guide"),
             I("PHPickerFilter", "https://developer.apple.com/documentation/photosui/phpickerfilter", "class"),
             H("PhotoViewMIMETypes", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-photoviewpicker"),
         ), level="L4", privacy="runtime_permission")
    for node in f:
        if node["id"] == "media.library.picker":
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            node["knowledge_path"] = "knowledge/media/library/picker/_rollup.yaml"

    leaf(f, "media.recording.av.profile", "media.recording.av", "recording_detail",
         "录制配置档", "Recording Profiles",
         "编码器、采样率、码率等录制配置档选择。",
         ["CamcorderProfile、AVRecorderConfig"],
         ["启停控制见 control"],
         merge_bindings(
             A("CamcorderProfile", "https://developer.android.com/reference/android/media/CamcorderProfile"),
             I("AVOutputSettingsAssistant", "https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant", "class"),
             H("AVRecorderConfig", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media"),
         ), level="L4", privacy="runtime_permission")
    leaf(f, "media.recording.av.control", "media.recording.av", "recording_detail",
         "录制启停控制", "Recording Start Stop Control",
         "开始/暂停/停止音视频文件录制。",
         ["start/stop recording"],
         ["配置档见 profile"],
         merge_bindings(
             A("MediaRecorder.start", "https://developer.android.com/reference/android/media/MediaRecorder#start()", "method"),
             I("AVAssetWriter.startWriting", "https://developer.apple.com/documentation/avfoundation/avassetwriter/1388232-startwriting", "method"),
             H("AVRecorder.start", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media"),
         ), level="L4", privacy="runtime_permission")
    # remove duplicate profile leaf if earlier version exists — dedup handles
    leaf(f, "media.recording.screen.authorize", "media.recording.screen", "screen_record_detail",
         "屏幕录制授权", "Screen Capture Authorization",
         "请求用户授权捕获屏幕内容。",
         ["MediaProjection intent、ReplayKit permission、AVScreenCapture auth"],
         ["写文件见 to_file"],
         merge_bindings(
             A("MediaProjectionManager", "https://developer.android.com/reference/android/media/projection/MediaProjectionManager"),
             I("RPScreenRecorder", "https://developer.apple.com/documentation/replaykit/rpscreenrecorder", "class"),
             H("AVScreenCapture 授权", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avscreen-capture"),
         ), level="L4", privacy="runtime_permission")
    leaf(f, "media.recording.screen.to_file", "media.recording.screen", "screen_record_detail",
         "屏幕录制写文件", "Screen Record to File",
         "将屏幕采集编码写入媒体文件。",
         ["VirtualDisplay + MediaRecorder、RPScreenRecorder start、AVScreenCaptureRecorder"],
         ["授权见 authorize"],
         merge_bindings(
             A("VirtualDisplay", "https://developer.android.com/reference/android/hardware/display/VirtualDisplay"),
             I("RPScreenRecorder.startRecording", "https://developer.apple.com/documentation/replaykit/rpscreenrecorder", "class"),
             H("AVScreenCaptureRecorder", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-avscreencapture"),
         ), level="L4", privacy="runtime_permission")
    for node in f:
        if node["id"] in {"media.recording.av", "media.recording.screen"}:
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            parts = node["id"].split(".")
            node["knowledge_path"] = "knowledge/" + "/".join(parts) + "/_rollup.yaml"

    leaf(f, "media.drm.license.key_request", "media.drm.license", "drm_license_detail",
         "许可证密钥请求", "License Key Request",
         "生成并向许可证服务器发起密钥请求。",
         ["getKeyRequest / MediaKeySession"],
         ["状态事件见 key_status"],
         merge_bindings(
             A("MediaDrm.getKeyRequest", "https://developer.android.com/reference/android/media/MediaDrm#getKeyRequest(byte[],%20byte[],%20java.lang.String,%20int,%20java.util.HashMap%3Cjava.lang.String,%20java.lang.String%3E)", "method"),
             I("AVContentKeyRequest", "https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest", "class"),
             H("MediaKeySession", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-drm"),
         ), level="L4")
    leaf(f, "media.drm.license.key_status", "media.drm.license", "drm_license_detail",
         "密钥状态事件", "Key Status Events",
         "监听许可证/密钥状态变更事件。",
         ["key status listeners"],
         ["发起请求见 key_request"],
         merge_bindings(
             A("MediaDrm.OnKeyStatusChangeListener", "https://developer.android.com/reference/android/media/MediaDrm.OnKeyStatusChangeListener"),
             I("AVContentKeySessionDelegate", "https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate", "protocol"),
             H("MediaKeySession 事件", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-drm"),
         ), level="L4")
    for node in f:
        if node["id"] == "media.drm.license":
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            node["knowledge_path"] = "knowledge/media/drm/license/_rollup.yaml"

    leaf(f, "media.editing.video.effects", "media.editing.video", "editing_detail",
         "编辑特效轨", "Editing Effects Track",
         "在合成时间线上应用视频特效/滤镜。",
         ["Effects in Transformer、AVVideoComposition"],
         ["多片段见 multiclip"],
         merge_bindings(
             A("Effects (Media3)", "https://developer.android.com/media/media3/transformer/effects", "guide"),
             I("AVVideoComposition", "https://developer.apple.com/documentation/avfoundation/avvideocomposition", "class"),
             pending("harmonyos"),
         ), level="L4")
    leaf(f, "media.editing.video.multiclip", "media.editing.video", "editing_detail",
         "多片段合成", "Multi-clip Composition",
         "多片段时间线拼接与轨编辑。",
         ["EditedMediaItemSequence、AVMutableComposition tracks"],
         ["特效见 effects"],
         merge_bindings(
             A("EditedMediaItemSequence", "https://developer.android.com/media/media3/transformer", "guide"),
             I("AVMutableComposition", "https://developer.apple.com/documentation/avfoundation/avmutablecomposition", "class"),
             pending("harmonyos"),
         ), level="L4")
    for node in f:
        if node["id"] == "media.editing.video":
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            node["knowledge_path"] = "knowledge/media/editing/video/_rollup.yaml"

    leaf(f, "media.scan.detect.live_stream", "media.scan.detect", "scan_mode",
         "实时流扫码", "Live Stream Scan",
         "基于实时相机预览帧的连续扫码。",
         ["live camera barcode scanning"],
         ["静图识别见 static_image"],
         merge_bindings(
             A("BarcodeScanning (camera)", "https://developers.google.com/ml-kit/vision/barcode-scanning/android", "guide"),
             I("AVCaptureMetadataOutput", "https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput", "class"),
             H("customScan", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-guidelines"),
         ), level="L4", privacy="runtime_permission")
    leaf(f, "media.scan.detect.static_image", "media.scan.detect", "scan_mode",
         "静图扫码", "Static Image Scan",
         "对已有图像缓冲执行码识别。",
         ["image buffer barcode detect"],
         ["实时流见 live_stream"],
         merge_bindings(
             A("InputImage.fromBitmap", "https://developers.google.com/ml-kit/vision/barcode-scanning/android", "guide"),
             I("VNImageRequestHandler", "https://developer.apple.com/documentation/vision/vnimagerequesthandler", "class"),
             H("图片扫码", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-guidelines"),
         ), level="L4")
    leaf(f, "media.scan.ui", "media.scan", "scan_capability",
         "系统扫码界面", "System Scan UI",
         "拉起系统提供的扫码用户界面。",
         ["system barcode scanner activity / default UI"],
         ["自定义检测见 detect"],
         merge_bindings(
             pending("android", "可用 ML Kit / GMS barcode UI"),
             I("DataScannerViewController", "https://developer.apple.com/documentation/visionkit/datascannerviewcontroller", "class"),
             H("ScanKit default UI", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-guidelines"),
         ), privacy="runtime_permission")
    for node in f:
        if node["id"] == "media.scan.detect":
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            node["knowledge_path"] = "knowledge/media/scan/detect/_rollup.yaml"

    # additional mid-level atomics for coverage
    leaf(f, "media.audio.render.latency", "media.audio.render", "audio_render_detail",
         "低延迟渲染调优", "Low-latency Render Tuning",
         "缓冲与性能模式等低延迟音频渲染调优。",
         ["performance mode / buffer size"],
         ["通用 PCM 渲染见父节点"],
         merge_bindings(
             A("AAudioStreamBuilder_setPerformanceMode", "https://developer.android.com/ndk/guides/audio/aaudio/aaudio", "guide"),
             I("AVAudioSession setPreferredIOBufferDuration", "https://developer.apple.com/documentation/avfoundation/avaudiosession/1616495-setpreferrediobufferduration", "method"),
             H("AudioRenderer 低延迟", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiorenderer-for-playback"),
         ), level="L4", privacy="runtime_permission")
    leaf(f, "media.audio.render.stream_setup", "media.audio.render", "audio_render_detail",
         "音频流建立", "Audio Stream Setup",
         "创建输出流并配置采样率/声道格式。",
         ["AAudioStreamBuilder、AVAudioEngine attach、AudioRenderer create"],
         ["低延迟调优见 latency"],
         merge_bindings(
             A("AAudioStreamBuilder", "https://developer.android.com/ndk/guides/audio/aaudio/aaudio", "guide"),
             I("AVAudioEngine.attach", "https://developer.apple.com/documentation/avfoundation/avaudioengine", "class"),
             H("AudioRenderer.create", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiorenderer-for-playback"),
         ), level="L4", privacy="runtime_permission")
    leaf(f, "media.session.focus.interrupt", "media.session.focus", "focus_detail",
         "音频打断处理", "Audio Interrupt Handling",
         "处理来电等导致的音频打断与恢复。",
         ["onAudioFocusChange、interruptionNotification"],
         ["焦点请求见 request"],
         merge_bindings(
             A("OnAudioFocusChangeListener", "https://developer.android.com/reference/android/media/AudioManager.OnAudioFocusChangeListener"),
             I("AVAudioSession.interruptionNotification", "https://developer.apple.com/documentation/avfoundation/avaudiosession/1616596-interruptionnotification", "type"),
             H("AudioInterrupt", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-concurrency"),
         ), level="L4", privacy="runtime_permission")
    leaf(f, "media.session.focus.request", "media.session.focus", "focus_detail",
         "音频焦点请求", "Audio Focus Request",
         "请求或放弃音频焦点。",
         ["requestAudioFocus、setActive、interrupt mode"],
         ["打断处理见 interrupt"],
         merge_bindings(
             A("AudioManager.requestAudioFocus", "https://developer.android.com/reference/android/media/AudioManager#requestAudioFocus(android.media.AudioFocusRequest)", "method"),
             I("AVAudioSession.setActive", "https://developer.apple.com/documentation/avfoundation/avaudiosession/1616627-setactive", "method"),
             H("AudioInterruptMode", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-concurrency"),
         ), level="L4", privacy="runtime_permission")
    leaf(f, "media.codec.video.capability_query", "media.codec.video", "codec_video_detail",
         "视频编解码能力查询", "Video Codec Capability Query",
         "查询设备支持的视频编解码器与档次。",
         ["MediaCodecList、VT / AVCodec 能力查询"],
         ["编解码执行见 encode_decode"],
         merge_bindings(
             A("MediaCodecList", "https://developer.android.com/reference/android/media/MediaCodecList"),
             I("VTCopyVideoEncoderList", "https://developer.apple.com/documentation/videotoolbox", "framework"),
             H("AVCodec 能力查询", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaavcodec"),
         ), level="L4")
    leaf(f, "media.codec.video.encode_decode", "media.codec.video", "codec_video_detail",
         "视频编解码执行", "Video Encode Decode Execution",
         "提交输入缓冲并取出编码/解码输出。",
         ["queueInputBuffer / encode frame"],
         ["能力查询见 capability_query"],
         merge_bindings(
             A("MediaCodec.queueInputBuffer", "https://developer.android.com/reference/android/media/MediaCodec#queueInputBuffer(int,%20int,%20int,%20long,%20int)", "method"),
             I("VTCompressionSessionEncodeFrame", "https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionencodeframe", "function"),
             H("VideoEncoder / VideoDecoder", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaavcodec"),
         ), level="L4")
    leaf(f, "media.capture.camera.preview", "media.capture.camera", "camera_capability",
         "相机预览", "Camera Preview",
         "将相机帧实时预览到界面表面。",
         ["PreviewView、AVCaptureVideoPreviewLayer、XComponent preview"],
         ["拍照见 photo"],
         merge_bindings(
             A("PreviewView", "https://developer.android.com/reference/androidx/camera/view/PreviewView"),
             I("AVCaptureVideoPreviewLayer", "https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer", "class"),
             H("PreviewOutput", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preparation"),
         ), level="L4", privacy="runtime_permission")
    leaf(f, "media.image.decode.animated", "media.image.decode", "image_decode_detail",
         "动图解码", "Animated Image Decode",
         "GIF/WebP 等动图逐帧解码。",
         ["AnimatedImageDrawable、CGImageSource 动图、ImageSource 动图"],
         ["静图见 still"],
         merge_bindings(
             A("AnimatedImageDrawable", "https://developer.android.com/reference/android/graphics/drawable/AnimatedImageDrawable"),
             I("CGImageSource", "https://developer.apple.com/documentation/imageio/cgimagesource-q0e", "type"),
             H("ImageSource 动图", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-image"),
         ), level="L4")
    leaf(f, "media.image.decode.still", "media.image.decode", "image_decode_detail",
         "静图解码", "Still Image Decode",
         "JPEG/PNG 等静图解码。",
         ["BitmapFactory、CGImageSource still、ImageSource"],
         ["动图见 animated"],
         merge_bindings(
             A("BitmapFactory", "https://developer.android.com/reference/android/graphics/BitmapFactory"),
             I("CGImageSourceCreateImageAtIndex", "https://developer.apple.com/documentation/imageio/1462092-cgimagesourcecreateimageatindex", "function"),
             H("createImageSource", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-image"),
         ), level="L4")
    for node in f:
        if node["id"] in {
            "media.audio.render", "media.codec.video", "media.image.decode",
            "media.session.focus",
        }:
            node["granularity"] = "branch"
            node["knowledge_role"] = "rollup"
            node.pop("leaf_at_this_level", None)
            parts = node["id"].split(".")
            node["knowledge_path"] = "knowledge/" + "/".join(parts) + "/_rollup.yaml"

    # drop earlier duplicate leaves that conflict — rebuild clean via dedup last-write
    dedup = {}
    for n in f:
        dedup[n["id"]] = n
    return list(dedup.values())

def main():
    nodes = build()
    path = write_domain("media", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
