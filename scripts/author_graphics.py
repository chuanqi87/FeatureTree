#!/usr/bin/env python3
"""Author the graphics domain taxonomy (~70-90 nodes)."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "graphics_pipeline_stage"


def leaf(f, fid, parent, axis, zh, en, definition, includes, excludes, bindings,
         legacy=None, level="L3", related=None, privacy="none"):
    f.append(feature(
        fid, parent=parent, level=level, zh=zh, en=en, definition=definition,
        includes=includes, excludes=excludes, sibling_axis=axis,
        granularity="atomic", bindings=bindings,
        legacy=legacy or {"disposition": "new", "sources": []},
        related=related, privacy_class=privacy,
    ))


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "graphics", parent=None, level="L1",
        zh="图形与渲染", en="Graphics and Rendering",
        definition="二维/三维绘制、合成呈现、色彩与 HDR、GPU 接口、图像特效、PDF 渲染、墨迹与截屏类捕获；不含连续屏幕音视频录制主路径。",
        includes=["2d、3d、capture、composite、text、color、gpu、imagefx、pdf、ink"],
        excludes=["media.recording.screen 连续录屏", "ui 控件树与布局", "media.image 编解码容器"],
        legacy={"disposition": "kept", "sources": ["graphics"]},
    ))

    l2 = [
        ("graphics.2d", "二维绘制", "2D Drawing",
         "即时模式画布、矢量形状、位图图元、绘制效果与离屏/2D 场景引擎。",
         ["canvas、shape、bitmap、effects、offscreen、engine"],
         ["3D 场景见 graphics.3d", "GPU 底层见 graphics.gpu"],
         ["graphics.2d"]),
        ("graphics.3d", "三维场景", "3D Scene",
         "三维场景图、资源、动画、空间重建与 AR 叠加渲染入口。",
         ["scene、assets、animation、spatial、ar"],
         ["GPU API 见 graphics.gpu", "传感器位姿见 sensors"],
         ["graphics.3d"]),
        ("graphics.capture", "图形捕获", "Graphics Capture",
         "全屏/组件静帧截取；连续屏幕 AV 录制主能力在 media。",
         ["screenshot、component"],
         ["连续录屏见 media.recording.screen"],
         ["graphics.capture"]),
        ("graphics.composite", "合成与表面", "Composition and Surfaces",
         "原生窗口/表面缓冲队列、跨进程缓冲、同步栅栏与硬件合成协作。",
         ["surface、hwc、fence、custom"],
         ["画布绘制见 graphics.2d.canvas"],
         []),
        ("graphics.text", "文本排版绘制", "Text Layout and Drawing",
         "字体、测量、复杂文本整形与画布文本绘制。",
         ["font、measure、shaping、draw"],
         ["UI 文本控件见 ui.controls"],
         []),
        ("graphics.color", "色彩与HDR", "Color and HDR",
         "色彩空间管理、HDR 显示与单双层 HDR 转换。",
         ["mgmt、hdr_display、hdr_convert"],
         ["媒体 HDR 轨见 media"],
         []),
        ("graphics.gpu", "GPU接口与加速", "GPU APIs and Acceleration",
         "现代 GPU API、上下文、着色器、计算与帧节奏/超分加速。",
         ["api、context、shader、compute、frame_pacing、upscale"],
         ["2D 画布见 graphics.2d", "3D 场景图见 graphics.3d"],
         []),
        ("graphics.imagefx", "图像特效", "Image Effects",
         "静图滤镜链、模糊/调色/风格化与主色提取。",
         ["filter、color_extract"],
         ["绘制态 Paint 效果见 graphics.2d.effects", "媒体图像编解码见 media.image"],
         []),
        ("graphics.pdf", "PDF渲染", "PDF Rendering",
         "PDF 页渲染与基础文档图形呈现。",
         ["page_render、document_view"],
         ["通用文档存储见 storage.document", "打印见 print_scan"],
         []),
        ("graphics.ink", "墨迹绘制", "Ink Drawing",
         "低延迟手写墨迹画布与笔画数据模型。",
         ["canvas、model"],
         ["触控输入事件见 input", "矢量形状见 graphics.2d.shape"],
         []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="graphics", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- 2d ---
    f.append(feature(
        "graphics.2d.bitmap", parent="graphics.2d", level="L3",
        zh="位图图元", en="Bitmap Primitives",
        definition="将位图作为绘制图元绘制，并读写/桥接像素缓冲。",
        includes=["draw、pixel_rw、type_bridge"],
        excludes=["图像编解码见 media.image"],
        sibling_axis="2d_capability",
        legacy={"disposition": "new", "sources": []},
    ))
    f.append(feature(
        "graphics.2d.effects", parent="graphics.2d", level="L3",
        zh="二维绘制效果", en="2D Draw Effects",
        definition="混合、颜色过滤、渐变着色、遮罩与路径效果等画笔级效果。",
        includes=["blend、color_filter、gradient、mask、path、image_filter"],
        excludes=["静图滤镜链见 graphics.imagefx"],
        sibling_axis="2d_capability",
        legacy={"disposition": "new", "sources": []},
    ))

    for fid, parent, axis, zh, en, definition, includes, excludes, bindings, legacy, related, level in [
        ("graphics.2d.canvas", "graphics.2d", "2d_capability",
         "画布绘制", "Canvas Drawing",
         "即时模式二维画布：裁剪、变换、保存/恢复与基础图元绘制。",
         ["clip、save/restore、draw primitives"], ["声明式 Shape 见 2d.shape"],
         merge_bindings(
             A("android.graphics.Canvas", "https://developer.android.com/reference/android/graphics/Canvas"),
             I("CGContext", "https://developer.apple.com/documentation/coregraphics", "class"),
             H("drawing.Canvas", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphic-drawing-overview"),
         ), {"disposition": "kept", "sources": ["graphics.2d.canvas"]}, None, "L3"),
        ("graphics.2d.shape", "graphics.2d", "2d_capability",
         "矢量形状", "Vector Shapes",
         "矩形/圆/路径等矢量形状声明或路径构建。",
         ["path、rect、circle、vector drawable"], ["位图图元见 2d.bitmap"],
         merge_bindings(
             A("VectorDrawable", "https://developer.android.com/guide/topics/graphics/vector-drawable-resources", "guide"),
             I("UIBezierPath", "https://developer.apple.com/documentation/uikit/uibezierpath", "class"),
             H("Shape", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shape-overview"),
         ), {"disposition": "new", "sources": []}, None, "L3"),
        ("graphics.2d.offscreen", "graphics.2d", "2d_capability",
         "离屏绘制", "Offscreen Drawing",
         "离屏画布或图层缓冲上的绘制与回读。",
         ["saveLayer、OffscreenCanvas"], ["表面合成见 graphics.composite"],
         merge_bindings(
             A("Canvas.saveLayer", "https://developer.android.com/reference/android/graphics/Canvas"),
             I("CGBitmapContext", "https://developer.apple.com/documentation/coregraphics", "class"),
             H("OffscreenCanvasRenderingContext2D", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d"),
         ), {"disposition": "new", "sources": []}, None, "L3"),
        ("graphics.2d.engine", "graphics.2d", "2d_capability",
         "二维场景引擎", "2D Scene Engine",
         "精灵/节点式二维场景图与动作驱动渲染。",
         ["scene graph、sprites、actions"], ["3D 场景见 graphics.3d.scene"],
         merge_bindings(
             pending("android", "常见于游戏引擎 SDK，待核系统级入口"),
             I("SpriteKit", "https://developer.apple.com/documentation/spritekit"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}, None, "L3"),
        ("graphics.2d.bitmap.draw", "graphics.2d.bitmap", "bitmap_op",
         "位图图元绘制", "Bitmap Draw",
         "将解码位图按位置/矩形绘制到画布，含采样缩放。",
         ["drawBitmap/drawImage"], ["像素读写见 pixel_rw"],
         merge_bindings(
             A("Canvas.drawBitmap", "https://developer.android.com/reference/android/graphics/Canvas"),
             I("CGContext.draw", "https://developer.apple.com/documentation/coregraphics/cgcontext", "class"),
             H("drawing.Canvas.drawImage", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-drawing-arkts"),
         ), {"disposition": "new", "sources": []}, None, "L4"),
        ("graphics.2d.bitmap.pixel_rw", "graphics.2d.bitmap", "bitmap_op",
         "位图像素读写", "Bitmap Pixel I/O",
         "读写位图像素缓冲或从缓冲区构建位图。",
         ["get/setPixels、buffer copy"], ["绘制见 bitmap.draw"],
         merge_bindings(
             A("Bitmap.setPixels", "https://developer.android.com/reference/android/graphics/Bitmap"),
             I("CGDataProvider", "https://developer.apple.com/documentation/coregraphics", "class"),
             H("PixelMap.writePixelsSync", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-drawing-arkts"),
         ), {"disposition": "new", "sources": []}, None, "L4"),
        ("graphics.2d.bitmap.type_bridge", "graphics.2d.bitmap", "bitmap_op",
         "位图类型桥接", "Bitmap Type Bridge",
         "硬件缓冲/纹理与 CPU 位图类型互转。",
         ["HardwareBuffer wrap、CGImage↔texture"], ["像素读写见 pixel_rw"],
         merge_bindings(
             A("Bitmap.wrapHardwareBuffer", "https://developer.android.com/reference/android/graphics/Bitmap"),
             I("CIContext.createCGImage", "https://developer.apple.com/documentation/coreimage/cicontext", "class"),
             H("OH_Drawing_PixelMapGetFromOhPixelMapNative", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-drawing-arkts"),
         ), {"disposition": "new", "sources": []}, None, "L4"),
        ("graphics.2d.effects.blend", "graphics.2d.effects", "draw_effect",
         "混合模式", "Blend Modes",
         "设置画笔/上下文混合模式控制源与目标合成。",
         ["PorterDuff/BlendMode"], ["颜色矩阵见 color_filter"],
         merge_bindings(
             A("PorterDuff.Mode", "https://developer.android.com/reference/android/graphics/PorterDuff.Mode"),
             I("CGBlendMode", "https://developer.apple.com/documentation/coregraphics/cgblendmode", "type"),
             H("drawing.Brush.setBlendMode", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-drawing-effect-arkts"),
         ), {"disposition": "new", "sources": []}, None, "L4"),
        ("graphics.2d.effects.color_filter", "graphics.2d.effects", "draw_effect",
         "颜色过滤", "Color Filter",
         "矩阵/光照等颜色过滤器作用于绘制内容。",
         ["ColorMatrix、ColorFilter"], ["渐变着色见 gradient_shader"],
         merge_bindings(
             A("ColorMatrixColorFilter", "https://developer.android.com/reference/android/graphics/ColorMatrixColorFilter"),
             I("CIColorMatrix", "https://developer.apple.com/documentation/coreimage/cicolormatrix", "class"),
             H("drawing.ColorFilter", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-drawing-effect-arkts"),
         ), {"disposition": "new", "sources": []}, None, "L4"),
        ("graphics.2d.effects.gradient_shader", "graphics.2d.effects", "draw_effect",
         "渐变着色器", "Gradient Shader",
         "线性/径向/扫描渐变作为画笔着色器。",
         ["Linear/Radial/SweepGradient"], ["图像滤镜见 image_filter"],
         merge_bindings(
             A("LinearGradient", "https://developer.android.com/reference/android/graphics/LinearGradient"),
             I("CGGradient", "https://developer.apple.com/documentation/coregraphics/cggradient", "class"),
             H("drawing.ShaderEffect", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-drawing-effect-arkts"),
         ), {"disposition": "new", "sources": []}, None, "L4"),
        ("graphics.2d.effects.mask_filter", "graphics.2d.effects", "draw_effect",
         "遮罩模糊", "Mask Filter",
         "对描边/填充应用模糊遮罩效果。",
         ["BlurMaskFilter"], ["图像模糊滤镜见 imagefx.filter.blur"],
         merge_bindings(
             A("BlurMaskFilter", "https://developer.android.com/reference/android/graphics/BlurMaskFilter"),
             pending("ios"),
             H("drawing.MaskFilter", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-drawing-effect-arkts"),
         ), {"disposition": "new", "sources": []}, ["graphics.imagefx.filter.blur"], "L4"),
        ("graphics.2d.effects.path_effect", "graphics.2d.effects", "draw_effect",
         "路径效果", "Path Effect",
         "虚线等路径效果作用于描边。",
         ["DashPathEffect、line dash"], ["遮罩见 mask_filter"],
         merge_bindings(
             A("DashPathEffect", "https://developer.android.com/reference/android/graphics/DashPathEffect"),
             I("CGContext.setLineDash", "https://developer.apple.com/documentation/coregraphics/cgcontext", "class"),
             H("drawing.PathEffect", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-drawing-effect-arkts"),
         ), {"disposition": "new", "sources": []}, None, "L4"),
        ("graphics.2d.effects.image_filter", "graphics.2d.effects", "draw_effect",
         "绘制图像滤镜", "Draw-time Image Filter",
         "在绘制管线注入模糊等图像滤镜（RenderEffect/ImageFilter）。",
         ["RenderEffect、ImageFilter"], ["独立静图滤镜链见 graphics.imagefx"],
         merge_bindings(
             A("RenderEffect", "https://developer.android.com/reference/android/graphics/RenderEffect"),
             pending("ios"),
             H("drawing.ImageFilter", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-drawing-effect-arkts"),
         ), {"disposition": "new", "sources": []}, ["graphics.imagefx.filter"], "L4"),
    ]:
        f.append(feature(
            fid, parent=parent, level=level, zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=axis,
            granularity="atomic", bindings=bindings, legacy=legacy, related=related,
        ))

    # --- 3d ---
    for fid, zh, en, definition, includes, excludes, bindings, related in [
        ("graphics.3d.scene", "三维场景图", "3D Scene Graph",
         "加载/构建三维场景节点、相机与灯光。",
         ["Scene、nodes、camera、light"], ["资源加载见 3d.assets"],
         merge_bindings(
             pending("android", "Filament/Sceneform 等生态库为主，待核"),
             I("SceneKit", "https://developer.apple.com/documentation/scenekit"),
             H("@ohos.graphics.scene", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-overview"),
         ), None),
        ("graphics.3d.assets", "三维资产加载", "3D Asset Loading",
         "网格/材质/环境贴图等三维资产加载与工厂创建。",
         ["glTF/USD、mesh、material"], ["场景图管理见 3d.scene"],
         merge_bindings(
             pending("android"),
             I("Model I/O", "https://developer.apple.com/documentation/modelio"),
             H("Scene.load", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-scene"),
         ), None),
        ("graphics.3d.animation", "三维动画", "3D Animation",
         "场景内骨骼/关键帧动画播放与回调。",
         ["clip play、callbacks"], ["2D 精灵动作见 2d.engine"],
         merge_bindings(
             pending("android"),
             I("SCNAnimationPlayer", "https://developer.apple.com/documentation/scenekit", "class"),
             H("ArkGraphics3D Animation", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-animation", "guide"),
         ), None),
        ("graphics.3d.spatial", "空间重建渲染", "Spatial Reconstruction Render",
         "空间重建结果编辑与三维高斯等空间内容渲染。",
         ["spatial recon、spatial render"], ["AR 会话见 3d.ar"],
         merge_bindings(
             pending("android"),
             pending("ios", "RoomPlan/Object Capture 边界待核"),
             H("SpatialRecon", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-introduction", "guide"),
         ), None),
        ("graphics.3d.ar", "增强现实叠加", "AR Overlay Rendering",
         "AR 会话帧与虚拟内容叠加渲染入口。",
         ["AR session、AR view"], ["纯 3D 离线场景见 3d.scene"],
         merge_bindings(
             A("ARCore", "https://developers.google.com/ar/develop", "guide"),
             I("ARKit", "https://developer.apple.com/documentation/arkit"),
             H("arEngine", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine"),
         ), None),
    ]:
        leaf(f, fid, "graphics.3d", "3d_capability", zh, en, definition, includes, excludes, bindings, related=related)

    # --- capture ---
    leaf(f, "graphics.capture.screenshot", "graphics.capture", "capture_kind",
         "全屏截图", "Screenshot",
         "捕获当前显示内容为静帧图像。",
         ["screenshot API"], ["组件截图见 capture.component", "连续录屏见 media.recording.screen"],
         merge_bindings(
             A("PixelCopy", "https://developer.android.com/reference/android/view/PixelCopy"),
             I("UIView.drawHierarchy", "https://developer.apple.com/documentation/uikit/uiview", "class"),
             H("@ohos.screenshot", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screenshot-and-privacy-mode"),
         ),
         legacy={"disposition": "kept", "sources": ["graphics.capture.screenshot"]},
         related=["media.recording.screen"], privacy="runtime_permission")

    f.append(feature(
        "graphics.capture.component", parent="graphics.capture", level="L3",
        zh="组件截图", en="Component Snapshot",
        definition="对界面组件树或离屏构建内容生成静帧快照。",
        includes=["on_tree、offline、long_scroll、surface_source"],
        excludes=["全屏截图见 capture.screenshot", "连续录屏见 media.recording.screen"],
        sibling_axis="capture_kind",
        related=["media.recording.screen"],
        legacy={"disposition": "new", "sources": []},
    ))
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("graphics.capture.component.on_tree", "在树组件截图", "On-Tree Component Snapshot",
         "对已挂载组件按 id 同步/异步生成快照。",
         ["get/getSync、SnapshotOptions"], ["离屏构建见 offline"],
         merge_bindings(
             A("PixelCopy.request", "https://developer.android.com/reference/android/view/PixelCopy"),
             I("UIView.drawHierarchy", "https://developer.apple.com/documentation/uikit/uiview/drawhierarchy(in:afterscreenupdates:)", "method"),
             H("ComponentSnapshot.get", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-component-snapshot"),
         )),
        ("graphics.capture.component.offline", "离屏组件截图", "Offline Component Snapshot",
         "从未挂载构建器/组件内容生成截图。",
         ["createFromBuilder"], ["在树截图见 on_tree"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("componentSnapshot.createFromBuilder", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-component-snapshot"),
         )),
        ("graphics.capture.component.long_scroll", "长列表拼接截图", "Long Scroll Snapshot",
         "滚动容器分页截取并拼接为长图。",
         ["scroll + stitch"], ["单帧组件截图见 on_tree"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("ComponentSnapshot + Scroller", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-component-snapshot", "guide"),
         )),
        ("graphics.capture.component.surface_source", "表面源截图", "Surface Source Snapshot",
         "从 Video/自绘制表面等源生成像素图。",
         ["PixelCopy Surface、createPixelMapFromSurface"], ["窗口全屏见 screenshot"],
         merge_bindings(
             A("PixelCopy.request", "https://developer.android.com/reference/android/view/PixelCopy"),
             I("MTLTexture", "https://developer.apple.com/documentation/metal/mtltexture", "protocol"),
             H("createPixelMapFromSurface", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-component-snapshot"),
         )),
    ]:
        leaf(f, fid, "graphics.capture.component", "component_snapshot_mode",
             zh, en, definition, includes, excludes, bindings, level="L4")

    # Pointer leaf — continuous AV screen record lives under media
    leaf(f, "graphics.capture.screen_record", "graphics.capture", "capture_kind",
         "屏幕录制（见媒体域）", "Screen Record (see Media)",
         "连续屏幕音视频录制交叉引用；原子能力归 media.recording.screen，此处不展开重复叶子。",
         ["cross-ref to media.recording.screen"],
         ["静帧截图见 capture.screenshot", "组件截图见 capture.component",
          "连续录屏原子能力见 media.recording.screen"],
         merge_bindings(
             A("MediaProjection", "https://developer.android.com/reference/android/media/projection/MediaProjection"),
             I("RPScreenRecorder", "https://developer.apple.com/documentation/replaykit/rpscreenrecorder", "class"),
             H("AVScreenCapture", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-avscreencapture"),
         ),
         legacy={"disposition": "kept", "sources": ["graphics.capture.screen_record"]},
         related=["media.recording.screen"], privacy="runtime_permission")

    # --- composite ---
    f.append(feature(
        "graphics.composite.surface", parent="graphics.composite", level="L3",
        zh="表面与缓冲", en="Surfaces and Buffers",
        definition="原生窗口/表面的缓冲申请、属性、队列与跨进程共享。",
        includes=["window_bind、buffer_queue、buffer_props、cross_process、buffer_image_bridge"],
        excludes=["HWC 策略见 composite.hwc"],
        sibling_axis="composite_role",
    ))
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("graphics.composite.surface.window_bind", "窗口表面绑定", "Window Surface Bind",
         "将自绘制内容绑定到系统表面/图层。",
         ["ANativeWindow_fromSurface、CAMetalLayer、XComponent surface"],
         ["缓冲队列操作见 buffer_queue"],
         merge_bindings(
             A("ANativeWindow_fromSurface", "https://developer.android.com/ndk/reference/group/native-window", "function"),
             I("CAMetalLayer", "https://developer.apple.com/documentation/quartzcore/cametallayer", "class"),
             H("OH_NativeWindow", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-window-guidelines"),
         )),
        ("graphics.composite.surface.buffer_queue", "缓冲队列", "Buffer Queue",
         "申请/提交/丢弃表面缓冲帧。",
         ["request/flush buffer、lock/unlock"], ["跨进程共享见 cross_process"],
         merge_bindings(
             A("ANativeWindow_lock", "https://developer.android.com/ndk/reference/group/native-window", "function"),
             I("IOSurfaceLock", "https://developer.apple.com/documentation/iosurface", "function"),
             H("OH_NativeWindow_NativeWindowRequestBuffer", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-window-guidelines"),
         )),
        ("graphics.composite.surface.buffer_props", "缓冲几何属性", "Buffer Geometry Props",
         "设置缓冲宽高、格式等几何与用途属性。",
         ["setBuffersGeometry、IOSurface properties"], ["队列见 buffer_queue"],
         merge_bindings(
             A("ANativeWindow_setBuffersGeometry", "https://developer.android.com/ndk/reference/group/native-window", "function"),
             I("IOSurface", "https://developer.apple.com/documentation/iosurface"),
             H("OH_NativeWindow_NativeWindowHandleOpt", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-window-guidelines"),
         )),
        ("graphics.composite.surface.cross_process", "跨进程缓冲共享", "Cross-Process Buffer Share",
         "跨进程共享硬件缓冲/IOSurface。",
         ["AHardwareBuffer、IOSurface、OH_NativeBuffer"], ["本进程队列见 buffer_queue"],
         merge_bindings(
             A("AHardwareBuffer", "https://developer.android.com/reference/android/hardware/HardwareBuffer"),
             I("IOSurface", "https://developer.apple.com/documentation/iosurface"),
             H("OH_NativeBuffer", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-window-guidelines"),
         )),
        ("graphics.composite.surface.buffer_image_bridge", "缓冲图像桥接", "Buffer-Image Bridge",
         "表面/像素缓冲与 GPU 纹理或 ImageReader 消费桥接。",
         ["ImageReader、CVMetalTextureCache、NativeImage"], ["窗口绑定见 window_bind"],
         merge_bindings(
             A("ImageReader", "https://developer.android.com/reference/android/media/ImageReader"),
             I("CVMetalTextureCache", "https://developer.apple.com/documentation/corevideo/cvmetaltexturecache", "class"),
             H("OH_NativeImage", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-window-guidelines"),
         )),
    ]:
        leaf(f, fid, "graphics.composite.surface", "surface_op", zh, en, definition,
             includes, excludes, bindings, level="L4")

    leaf(f, "graphics.composite.hwc", "graphics.composite", "composite_role",
         "硬件合成协作", "Hardware Composer Collaboration",
         "应用侧与硬件合成器协作的图层策略入口。",
         ["HWC layer tips"], ["表面缓冲见 composite.surface"],
         merge_bindings(
             pending("android", "SurfaceFlinger/HWC 应用侧约束待核"),
             pending("ios"),
             H("HWC collaboration", "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-utilize-hwc-efficiently", "guide"),
         ))
    leaf(f, "graphics.composite.fence", "graphics.composite", "composite_role",
         "同步栅栏", "Native Fence Sync",
         "原生 fence 句柄等待与生命周期管理。",
         ["OH_NativeFence、sync fence"], ["缓冲提交见 surface.buffer_queue"],
         merge_bindings(
             pending("android", "sync_fence / EGL sync 待核"),
             pending("ios"),
             H("OH_NativeFence", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativefence"),
         ))
    leaf(f, "graphics.composite.custom", "graphics.composite", "composite_role",
         "自定义合成层", "Custom Compositor Layer",
         "向系统合成器提供自定义层渲染器。",
         ["CompositorServices LayerRenderer"], ["普通表面见 composite.surface"],
         merge_bindings(
             pending("android"),
             I("LayerRenderer", "https://developer.apple.com/documentation/compositorservices/layer-renderer", "protocol"),
             pending("harmonyos"),
         ))

    # --- text ---
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("graphics.text.font", "字体管理", "Font Management",
         "字体集合注册、可下载字体与主题字体。",
         ["FontCollection、FontsContract"], ["测量见 text.measure"],
         merge_bindings(
             A("FontsContractCompat", "https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts", "guide"),
             I("CTFont", "https://developer.apple.com/documentation/coretext", "class"),
             H("@ohos.graphics.text FontCollection", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme-font-arkts"),
         )),
        ("graphics.text.measure", "文本测量", "Text Measurement",
         "文本宽度、行高与字形/字符范围测量。",
         ["measureText、Paragraph metrics"], ["整形见 text.shaping"],
         merge_bindings(
             A("Paint.measureText", "https://developer.android.com/reference/android/graphics/Paint"),
             I("CTLineGetTypographicBounds", "https://developer.apple.com/documentation/coretext", "function"),
             H("text measure", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/text-measure-arkts", "guide"),
         )),
        ("graphics.text.shaping", "复杂文本整形", "Complex Text Shaping",
         "双向文本、locale 与段落样式整形。",
         ["ParagraphStyle、locale"], ["绘制见 text.draw"],
         merge_bindings(
             A("android.graphics.text", "https://developer.android.com/reference/android/graphics/text/package-summary", "package"),
             I("Core Text", "https://developer.apple.com/documentation/coretext"),
             H("complex text", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-text-arkts", "guide"),
         )),
        ("graphics.text.draw", "文本绘制", "Text Drawing",
         "将整形后的文本/TextBlob 绘制到画布。",
         ["drawText、TextBlob"], ["UI Text 控件见 ui"],
         merge_bindings(
             A("Canvas.drawText", "https://developer.android.com/reference/android/graphics/Canvas"),
             I("CTLineDraw", "https://developer.apple.com/documentation/coretext", "function"),
             H("drawing.Canvas.drawTextBlob", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/textblock-drawing-arkts"),
         )),
    ]:
        leaf(f, fid, "graphics.text", "text_pipeline", zh, en, definition, includes, excludes, bindings)

    # --- color ---
    f.append(feature(
        "graphics.color.hdr_convert", parent="graphics.color", level="L3",
        zh="HDR图层转换", en="HDR Layer Conversion",
        definition="单层/双层 HDR 图像合成与分解及元数据写入。",
        includes=["dual_to_single、single_to_dual、metadata"],
        excludes=["HDR 显示能力查询见 color.hdr_display"],
        sibling_axis="color_capability",
    ))
    leaf(f, "graphics.color.mgmt", "graphics.color", "color_capability",
         "色彩空间管理", "Color Space Management",
         "创建/查询色彩空间并应用于缓冲或窗口。",
         ["ColorSpace、CGColorSpace、ColorSync"], ["HDR 转换见 hdr_convert"],
         merge_bindings(
             A("android.graphics.ColorSpace", "https://developer.android.com/training/wide-color-gamut", "guide"),
             I("ColorSync", "https://developer.apple.com/documentation/colorsync"),
             H("@ohos.graphics.colorSpaceManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativecolorspacemanager"),
         ))
    leaf(f, "graphics.color.hdr_display", "graphics.color", "color_capability",
         "HDR显示能力", "HDR Display Capability",
         "查询/配置显示侧 HDR 能力与 LUT/元数据。",
         ["hdrCapability、DisplayLuts"], ["图层转换见 hdr_convert"],
         merge_bindings(
             A("DisplayLuts", "https://developer.android.com/media/grow/hdr-lut", "guide"),
             pending("ios", "EDR/HDR 显示 API 待核"),
             H("@ohos.graphics.hdrCapability", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics2d-introduction"),
         ))
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("graphics.color.hdr_convert.dual_to_single", "双层合成单层HDR", "Dual-to-Single HDR Compose",
         "将 SDR+增益图合成为单层 HDR。",
         ["IMAGE_PROCESSING_TYPE_COMPOSITION"], ["分解见 single_to_dual"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("OH_ImageProcessing_Compose", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdr-dual-to-single"),
         )),
        ("graphics.color.hdr_convert.single_to_dual", "单层分解双层HDR", "Single-to-Dual HDR Decompose",
         "将单层 HDR 分解为 SDR+增益图。",
         ["IMAGE_PROCESSING_TYPE_DECOMPOSITION"], ["合成见 dual_to_single"],
         merge_bindings(
             pending("android"),
             pending("ios"),
             H("OH_ImageProcessing_Decompose", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageprocessing"),
         )),
        ("graphics.color.hdr_convert.metadata", "HDR元数据", "HDR Metadata",
         "读写像素图/图像的 HDR 元数据键。",
         ["HdrMetadataKey、ImageIO HDR props"], ["合成算法见 dual_to_single"],
         merge_bindings(
             pending("android"),
             I("ImageIO", "https://developer.apple.com/documentation/imageio"),
             H("PixelMap.setMetadata", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdr-dual-to-single"),
         )),
    ]:
        leaf(f, fid, "graphics.color.hdr_convert", "hdr_convert_op", zh, en, definition,
             includes, excludes, bindings, level="L4")

    # --- gpu ---
    leaf(f, "graphics.gpu.api", "graphics.gpu", "gpu_capability",
         "现代GPU图形API", "Modern GPU Graphics API",
         "Metal/Vulkan/OpenGL ES 等现代 GPU 绘制 API 入口。",
         ["Metal、Vulkan、GLES"], ["计算见 gpu.compute", "上下文见 gpu.context"],
         merge_bindings(
             A("OpenGL ES", "https://developer.android.com/guide/topics/graphics/opengl", "guide"),
             I("Metal", "https://developer.apple.com/documentation/metal"),
             H("OpenGL ES / Vulkan", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengles", "guide"),
         ),
         legacy={"disposition": "renamed_from", "sources": ["graphics.3d.gpu_api"]})
    leaf(f, "graphics.gpu.context", "graphics.gpu", "gpu_capability",
         "GPU上下文与表面", "GPU Context and Surface",
         "创建 EGL/EAGL 等图形上下文并关联窗口表面。",
         ["EGL、EAGLContext"], ["命令编码见 gpu.api"],
         merge_bindings(
             A("EGL", "https://developer.android.com/ndk/reference/group/egl", "guide"),
             I("EAGLContext", "https://developer.apple.com/documentation/opengles", "class"),
             H("EGL", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/egl"),
         ))
    f.append(feature(
        "graphics.gpu.shader", parent="graphics.gpu", level="L3",
        zh="着色器", en="Shaders",
        definition="运行时/资源着色器编译与向 UI/3D 管线注入。",
        includes=["runtime_ui、render_effect、engine_3d"],
        excludes=["完整 GPU API 见 gpu.api"],
        sibling_axis="gpu_capability",
    ))
    f.append(feature(
        "graphics.gpu.compute", parent="graphics.gpu", level="L3",
        zh="GPU计算", en="GPU Compute",
        definition="计算管线、性能着色器内核库与图执行。",
        includes=["compute_pipeline、kernel_lib、graph_exec"],
        excludes=["图形渲染 API 见 gpu.api"],
        sibling_axis="gpu_capability",
    ))
    leaf(f, "graphics.gpu.frame_pacing", "graphics.gpu", "gpu_capability",
         "帧节奏与刷新率", "Frame Pacing and Refresh Rate",
         "VSync/DisplayLink、表面期望帧率与刷新率信息。",
         ["Choreographer、CADisplayLink、displaySync、setFrameRate"],
         ["超分/插帧见 gpu.upscale"],
         merge_bindings(
             A("Surface.setFrameRate", "https://developer.android.com/media/optimize/performance/frame-rate", "guide"),
             I("CADisplayLink", "https://developer.apple.com/documentation/quartzcore/cadisplaylink", "class"),
             H("@ohos.graphics.displaySync", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/displaysync-overview"),
         ))
    leaf(f, "graphics.gpu.upscale", "graphics.gpu", "gpu_capability",
         "超分与帧生成", "Upscale and Frame Generation",
         "空间/时间超分与插帧/外推帧生成加速。",
         ["MTLFX、frame generation"], ["帧节奏见 frame_pacing"],
         merge_bindings(
             pending("android", "AGDK/厂商超分待核"),
             I("MetalFX", "https://developer.apple.com/documentation/metalfx"),
             H("frame_generation", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__base_8h"),
         ))

    for fid, zh, en, definition, includes, excludes, bindings in [
        ("graphics.gpu.shader.runtime_ui", "运行时UI着色器", "Runtime UI Shader",
         "在 UI/画布路径编译并应用运行时着色器。",
         ["RuntimeShader、SwiftUI Shader"], ["RenderEffect 注入见 render_effect_inject"],
         merge_bindings(
             A("RuntimeShader", "https://developer.android.com/develop/ui/views/graphics/agsl/using-agsl", "guide"),
             I("Shader", "https://developer.apple.com/documentation/swiftui/shader", "structure"),
             pending("harmonyos"),
         )),
        ("graphics.gpu.shader.render_effect_inject", "渲染效果着色器注入", "Render Effect Shader Inject",
         "经 RenderEffect/layerEffect 将着色器注入视图层。",
         ["createRuntimeShaderEffect、layerEffect"], ["纯 RuntimeShader 画布见 runtime_ui"],
         merge_bindings(
             A("RenderEffect.createRuntimeShaderEffect", "https://developer.android.com/develop/ui/views/graphics/agsl/using-agsl", "guide"),
             I("View.layerEffect", "https://developer.apple.com/documentation/swiftui/view/layereffect(_:maxsampleoffset:isenabled:)", "method"),
             pending("harmonyos"),
         )),
        ("graphics.gpu.shader.engine_3d_resource", "三维引擎着色器资源", "3D Engine Shader Resource",
         "三维引擎自定义着色器资源描述与管线状态。",
         [".shader resource、MSL/SPIR-V"], ["UI 运行时着色器见 runtime_ui"],
         merge_bindings(
             pending("android"),
             I("MTLRenderPipelineState", "https://developer.apple.com/documentation/metal/mtlrenderpipelinestate", "protocol"),
             H("ArkGraphics3D shader resource", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-shader-resource", "guide"),
         )),
        ("graphics.gpu.compute.compute_pipeline", "计算管线", "Compute Pipeline",
         "创建并调度 GPU 计算管线/着色器。",
         ["MTLComputePipeline、Vulkan compute"], ["内核库见 kernel_lib"],
         merge_bindings(
             A("Vulkan compute", "https://developer.android.com/ndk/guides/graphics", "guide"),
             I("MTLComputePipelineState", "https://developer.apple.com/documentation/metal/mtlcomputepipelinestate", "protocol"),
             H("Vulkan", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vulkan-guidelines", "guide"),
         )),
        ("graphics.gpu.compute.kernel_lib", "性能着色器内核库", "Performance Shader Kernels",
         "预置图像/矩阵等 GPU 内核库。",
         ["Metal Performance Shaders"], ["图执行见 graph_exec"],
         merge_bindings(
             pending("android", "RenderScript 已废弃，替代路径待核"),
             I("Metal Performance Shaders", "https://developer.apple.com/documentation/metalperformanceshaders"),
             pending("harmonyos"),
         )),
        ("graphics.gpu.compute.graph_exec", "计算图执行", "Compute Graph Execution",
         "构建并执行 GPU 计算图。",
         ["MPSGraph"], ["单内核见 kernel_lib"],
         merge_bindings(
             pending("android"),
             I("MPSGraph", "https://developer.apple.com/documentation/metalperformanceshaders", "class"),
             pending("harmonyos"),
         )),
    ]:
        parent = "graphics.gpu.shader" if ".shader." in fid else "graphics.gpu.compute"
        axis = "shader_role" if ".shader." in fid else "compute_role"
        leaf(f, fid, parent, axis, zh, en, definition, includes, excludes, bindings, level="L4")

    # --- imagefx ---
    f.append(feature(
        "graphics.imagefx.filter", parent="graphics.imagefx", level="L3",
        zh="图像滤镜", en="Image Filters",
        definition="对静图像素图应用模糊、调色、风格化及滤镜链。",
        includes=["blur、color_adjust、stylize、chain"],
        excludes=["绘制态 ImageFilter 见 2d.effects.image_filter"],
        sibling_axis="imagefx_capability",
        related=["graphics.2d.effects.image_filter"],
    ))
    leaf(f, "graphics.imagefx.color_extract", "graphics.imagefx", "imagefx_capability",
         "主色提取", "Color Extraction",
         "从位图提取调色板/主色。",
         ["Palette"], ["滤镜见 imagefx.filter"],
         merge_bindings(
             A("Palette", "https://developer.android.com/training/material/palette-colors", "guide"),
             I("CIAreaAverage", "https://developer.apple.com/documentation/coreimage", "class"),
             pending("harmonyos"),
         ))
    for fid, zh, en, definition, includes, excludes, bindings in [
        ("graphics.imagefx.filter.blur", "模糊滤镜", "Blur Filter",
         "高斯等模糊半径滤镜。",
         ["gaussian blur"], ["调色见 color_adjust"],
         merge_bindings(
             A("RenderEffect.createBlurEffect", "https://developer.android.com/reference/android/graphics/RenderEffect"),
             I("CIGaussianBlur", "https://developer.apple.com/documentation/coreimage/cigaussianblur", "class"),
             H("OH_Filter_Blur", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/effectkit-filter-c"),
         )),
        ("graphics.imagefx.filter.color_adjust", "颜色调节滤镜", "Color Adjust Filter",
         "亮度/对比度/曝光等颜色调节。",
         ["brighten、ColorControls"], ["风格化见 stylize"],
         merge_bindings(
             pending("android"),
             I("CIColorControls", "https://developer.apple.com/documentation/coreimage/cicolorcontrols", "class"),
             H("OH_Filter_Brighten", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/effectkit-filter-c"),
         )),
        ("graphics.imagefx.filter.stylize", "风格化滤镜", "Stylize Filter",
         "灰度、反色等风格化效果。",
         ["grayScale、invert、photo effects"], ["滤镜链见 chain"],
         merge_bindings(
             pending("android"),
             I("CIColorInvert", "https://developer.apple.com/documentation/coreimage/cicolorinvert", "class"),
             H("OH_Filter_GrayScale", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/effectkit-filter-c"),
         )),
        ("graphics.imagefx.filter.chain", "滤镜链", "Filter Chain",
         "按序组合多个滤镜并输出结果像素。",
         ["chainedEffects、OH_Filter pipeline"], ["单滤镜见 blur/color_adjust"],
         merge_bindings(
             pending("android"),
             I("CIFilter", "https://developer.apple.com/documentation/coreimage/cifilter", "class"),
             H("OH_Filter_CreateEffect", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/effectkit-filter-c"),
         )),
    ]:
        leaf(f, fid, "graphics.imagefx.filter", "filter_kind", zh, en, definition,
             includes, excludes, bindings, level="L4")

    # --- pdf ---
    leaf(f, "graphics.pdf.page_render", "graphics.pdf", "pdf_capability",
         "PDF页渲染", "PDF Page Render",
         "将 PDF 页面渲染为位图或视图内容。",
         ["PdfRenderer、PDFPage render"], ["表单编辑深度见 storage.document"],
         merge_bindings(
             A("PdfRenderer", "https://developer.android.com/reference/android/graphics/pdf/PdfRenderer"),
             I("PDFKit", "https://developer.apple.com/documentation/pdfkit"),
             H("PDF Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-kit-overview", "guide"),
         ))
    leaf(f, "graphics.pdf.document_view", "graphics.pdf", "pdf_capability",
         "PDF文档视图", "PDF Document View",
         "嵌入式 PDF 文档浏览与缩略图视图。",
         ["PDFView、PdfViewerFragment"], ["页渲染原语见 page_render"],
         merge_bindings(
             A("PdfViewerFragment", "https://developer.android.com/reference/android/graphics/pdf/package-summary", "guide"),
             I("PDFView", "https://developer.apple.com/documentation/pdfkit/pdfview", "class"),
             H("PDF Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-kit-overview", "guide"),
         ))

    # --- ink ---
    leaf(f, "graphics.ink.canvas", "graphics.ink", "ink_capability",
         "墨迹画布", "Ink Canvas",
         "低延迟手写/触控笔墨迹绘制画布。",
         ["PKCanvasView、Pen Kit canvas"], ["笔画模型见 ink.model"],
         merge_bindings(
             A("Stylus / Ink", "https://developer.android.com/develop/ui/views/touch-and-input/stylus-input", "guide"),
             I("PKCanvasView", "https://developer.apple.com/documentation/pencilkit", "class"),
             H("Pen Kit", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-kit-overview", "guide"),
         ))
    leaf(f, "graphics.ink.model", "graphics.ink", "ink_capability",
         "墨迹数据模型", "Ink Stroke Model",
         "笔画路径与墨迹文档数据模型。",
         ["PKDrawing、PKStroke"], ["画布交互见 ink.canvas"],
         merge_bindings(
             pending("android"),
             I("PKDrawing", "https://developer.apple.com/documentation/pencilkit/pkdrawing", "class"),
             pending("harmonyos"),
         ))

    dedup = {}
    for node in f:
        dedup[node["id"]] = node
    return list(dedup.values())


def main():
    nodes = build()
    path = write_domain("graphics", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
