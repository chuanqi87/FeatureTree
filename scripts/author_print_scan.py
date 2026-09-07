#!/usr/bin/env python3
"""Author the print_scan domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "print_scan_capability_family"


def B(a=None, i=None, h=None):
    parts = []
    if a:
        parts.append(A(a[0], a[1], a[2] if len(a) > 2 else "class"))
    else:
        parts.append(pending("android"))
    if i:
        parts.append(I(i[0], i[1], i[2] if len(i) > 2 else "framework"))
    else:
        parts.append(pending("ios"))
    if h:
        parts.append(H(h[0], h[1], h[2] if len(h) > 2 else "module"))
    else:
        parts.append(pending("harmonyos"))
    return merge_bindings(*parts)


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
        "print_scan", parent=None, level="L1",
        zh="打印与外部扫描", en="Print and Scan",
        definition="系统打印框架与外部扫描仪/文档扫描入口；不含相机普通拍照。",
        includes=['打印、扫描'],
        excludes=['相机拍照见 media.capture', '文档解析见 documents'],
        legacy={'disposition': 'new', 'sources': []},
    ))
    l2 = [
        ('print_scan.print', '打印', 'Printing', '打印任务、打印机发现与页面渲染到打印管线。', ['打印机发现、任务、渲染'], ['扫描见 scan'], []),
        ('print_scan.scan', '外部扫描', 'External Scanning', '调用系统文档扫描或扫描仪获取影像。', ['文档扫描、扫描仪'], ['打印见 print', 'OCR 见 ai.vision'], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="print_scan", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- print_scan.print ---
    leaf(f, "print_scan.print.job", "print_scan.print", "print_operation", "打印任务提交", "Print Job Submit",
         "创建并提交打印任务到系统打印服务。", ['PrintManager / UIPrintInteraction'], ['打印机发现见 discovery'],
         B(('PrintManager', 'https://developer.android.com/reference/android/print/PrintManager'), ('UIPrintInteractionController', 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller', 'class'), ('print', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-print')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "print_scan.print.discovery", "print_scan.print", "print_operation", "打印机发现", "Printer Discovery",
         "发现可用打印机与能力。", ['PrintServices / UIPrinter'], ['任务见 job'],
         B(('PrinterDiscoverySession', 'https://developer.android.com/reference/android/printservice/PrinterDiscoverySession'), ('UIPrinterPickerController', 'https://developer.apple.com/documentation/uikit/uiprinterpickercontroller', 'class'), ('print', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-print')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "print_scan.print.adapter", "print_scan.print", "print_operation", "打印文档适配", "Print Document Adapter",
         "将应用内容分页渲染为打印文档。", ['PrintDocumentAdapter'], ['任务提交见 job'],
         B(('PrintDocumentAdapter', 'https://developer.android.com/reference/android/print/PrintDocumentAdapter'), ('UIPrintFormatter', 'https://developer.apple.com/documentation/uikit/uiprintformatter', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "print_scan.print.attributes", "print_scan.print", "print_operation", "打印属性协商", "Print Attributes",
         "协商纸张、色彩、双面等打印属性。", ['PrintAttributes'], ['适配器见 adapter'],
         B(('PrintAttributes', 'https://developer.android.com/reference/android/print/PrintAttributes'), ('UIPrintInfo', 'https://developer.apple.com/documentation/uikit/uiprintinfo', 'class'), ('print', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-print')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "print_scan.print.preview", "print_scan.print", "print_operation", "打印预览", "Print Preview",
         "展示系统打印预览界面。", ['print preview UI'], ['任务见 job'],
         B(('PrintManager.print', 'https://developer.android.com/reference/android/print/PrintManager'), ('UIPrintInteractionController', 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "print_scan.print.service_ext", "print_scan.print", "print_operation", "打印服务扩展", "Print Service Extension",
         "实现系统打印服务以对接打印机。", ['PrintService'], ['应用侧任务见 job'],
         B(('PrintService', 'https://developer.android.com/reference/android/printservice/PrintService'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "print_scan.print.pdf_output", "print_scan.print", "print_operation", "打印到PDF", "Print to PDF",
         "将内容渲染输出为 PDF。", ['PrintedPdfDocument'], ['预览见 preview'],
         B(('PrintedPdfDocument', 'https://developer.android.com/reference/android/print/pdf/PrintedPdfDocument'), ('UIGraphicsPDFRenderer', 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- print_scan.scan ---
    leaf(f, "print_scan.scan.document_camera", "print_scan.scan", "scan_operation", "文档相机扫描", "Document Camera Scan",
         "调用系统文档扫描相机获取多页影像。", ['DocumentScanner / VNDocumentCamera'], ['OCR 见 ai.vision'],
         B(('Document Scanner', 'https://developers.google.com/ml-kit/vision/doc-scanner', 'guide'), ('VNDocumentCameraViewController', 'https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontroller', 'class'), ('scan', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-scan')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "print_scan.scan.external_scanner", "print_scan.scan", "scan_operation", "外部扫描仪接入", "External Scanner Access",
         "连接外部扫描仪并获取扫描件。", ['ImageCaptureCore / scanner'], ['文档相机见 document_camera'],
         B(None, ('ImageCaptureCore', 'https://developer.apple.com/documentation/imagecapturecore', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "print_scan.scan.multi_page", "print_scan.scan", "scan_operation", "多页扫描会话", "Multi-Page Scan Session",
         "在一次会话中扫描多页并输出文档。", ['multi-page session'], ['单页相机见 document_camera'],
         B(('GmsDocumentScanning', 'https://developers.google.com/ml-kit/vision/doc-scanner', 'guide'), ('VNDocumentCameraViewController', 'https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontroller', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "print_scan.scan.image_cleanup", "print_scan.scan", "scan_operation", "扫描件透视矫正增强", "Scan Image Cleanup",
         "对扫描件做裁切、透视矫正与增强。", ['perspective correction'], ['OCR 见 ai.vision'],
         B(('Doc scanner filters', 'https://developers.google.com/ml-kit/vision/doc-scanner', 'guide'), ('VisionKit', 'https://developer.apple.com/documentation/visionkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "print_scan.scan.barcode_batch", "print_scan.scan", "scan_operation", "批量条码扫描入口", "Batch Barcode Scan Entry",
         "面向扫描枪/批量条码的系统扫描入口。", ['batch barcode'], ['视觉条码算法见 ai.vision.barcode'],
         B(('ML Kit Barcode', 'https://developers.google.com/ml-kit/vision/barcode-scanning', 'guide'), ('AVCaptureMetadataOutput', 'https://developer.apple.com/documentation/avfoundation', 'framework'), ('scanBarcode', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-scan')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")


    leaf(f, "print_scan.print.range", "print_scan.print", "print_operation", "打印页范围", "Print Page Range",
         "指定打印页范围与副本数。", ["page range / copies"], ["属性协商见 attributes"],
         B(("PrintDocumentInfo", "https://developer.android.com/reference/android/print/PrintDocumentInfo"),
           ("UIPrintInfo", "https://developer.apple.com/documentation/uikit/uiprintinfo", "class"),
           ("print", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-print")))
    leaf(f, "print_scan.print.color_duplex", "print_scan.print", "print_operation", "色彩与双面", "Color and Duplex",
         "设置彩色/黑白与双面打印。", ["color mode / duplex"], ["页范围见 range"],
         B(("PrintAttributes", "https://developer.android.com/reference/android/print/PrintAttributes"),
           ("UIPrintInfo", "https://developer.apple.com/documentation/uikit/uiprintinfo", "class"), None))
    leaf(f, "print_scan.print.media_size", "print_scan.print", "print_operation", "纸张介质尺寸", "Media Size",
         "选择纸张介质尺寸与方向。", ["media size / orientation"], ["色彩见 color_duplex"],
         B(("PrintAttributes.MediaSize", "https://developer.android.com/reference/android/print/PrintAttributes.MediaSize"),
           ("UIPrintInfo", "https://developer.apple.com/documentation/uikit/uiprintinfo", "class"), None))
    leaf(f, "print_scan.print.job_state", "print_scan.print", "print_operation", "打印任务状态", "Print Job State",
         "查询打印任务排队、打印中与完成状态。", ["PrintJob state"], ["提交见 job"],
         B(("PrintJob", "https://developer.android.com/reference/android/print/PrintJob"),
           ("UIPrintInteractionController", "https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller", "class"),
           ("print", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-print")))
    leaf(f, "print_scan.print.cancel", "print_scan.print", "print_operation", "取消打印任务", "Cancel Print Job",
         "取消尚未完成的打印任务。", ["cancel"], ["状态见 job_state"],
         B(("PrintJob.cancel", "https://developer.android.com/reference/android/print/PrintJob"), None, None))
    leaf(f, "print_scan.scan.image_export", "print_scan.scan", "scan_operation", "扫描件导出", "Scan Image Export",
         "将扫描结果导出为图片或 PDF。", ["export scan"], ["多页会话见 multi_page"],
         B(("Document Scanner", "https://developers.google.com/ml-kit/vision/doc-scanner", "guide"),
           ("VNDocumentCameraViewController", "https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontroller", "class"), None))
    leaf(f, "print_scan.scan.auto_capture", "print_scan.scan", "scan_operation", "自动拍边捕获", "Auto Edge Capture",
         "自动检测文档边缘并触发捕获。", ["auto capture"], ["矫正见 image_cleanup"],
         B(("Document Scanner", "https://developers.google.com/ml-kit/vision/doc-scanner", "guide"),
           ("VisionKit", "https://developer.apple.com/documentation/visionkit", "framework"), None), privacy="runtime_permission")
    leaf(f, "print_scan.scan.filter_mode", "print_scan.scan", "scan_operation", "扫描色彩滤镜", "Scan Color Filter",
         "选择彩色、灰度或黑白扫描滤镜。", ["scan filters"], ["导出见 image_export"],
         B(("Doc scanner filters", "https://developers.google.com/ml-kit/vision/doc-scanner", "guide"),
           ("VisionKit", "https://developer.apple.com/documentation/visionkit", "framework"), None))
    leaf(f, "print_scan.scan.resolution", "print_scan.scan", "scan_operation", "扫描分辨率", "Scan Resolution",
         "设置外部扫描或文档扫描输出分辨率。", ["DPI / resolution"], ["外部扫描仪见 external_scanner"],
         B(None, ("ImageCaptureCore", "https://developer.apple.com/documentation/imagecapturecore", "framework"), None))
    leaf(f, "print_scan.scan.progress", "print_scan.scan", "scan_operation", "扫描进度回调", "Scan Progress Callback",
         "接收扫描进度与完成回调。", ["scan progress"], ["导出见 image_export"],
         B(("Document Scanner", "https://developers.google.com/ml-kit/vision/doc-scanner", "guide"),
           ("VNDocumentCameraViewControllerDelegate", "https://developer.apple.com/documentation/visionkit", "framework"), None))

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("print_scan", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
