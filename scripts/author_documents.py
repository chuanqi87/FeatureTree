#!/usr/bin/env python3
"""Author the documents domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "documents_capability_family"


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
        "documents", parent=None, level="L1",
        zh="文档与阅读", en="Documents and Reading",
        definition="文档解析、阅读呈现、批注、生成、预览与分页；不含通用文件选择器。",
        includes=['解析、阅读、批注、生成、预览、分页'],
        excludes=['文件选择见 storage.user_files', 'OCR 算法见 ai.vision', '打印见 print_scan'],
        legacy={'disposition': 'new', 'sources': []},
    ))
    l2 = [
        ('documents.parse', '文档解析', 'Document Parse', '解析 PDF/Office 等文档结构与文本。', ['PDF 解析、文本提取'], ['阅读呈现见 reading'], []),
        ('documents.reading', '阅读呈现', 'Reading Presentation', '阅读器布局、重排与阅读进度。', ['重排、进度、主题'], ['批注见 annotation'], []),
        ('documents.annotation', '文档批注', 'Document Annotation', '高亮、墨迹与评论等批注能力。', ['高亮、墨迹、评论'], ['生成见 generate'], []),
        ('documents.generate', '文档生成', 'Document Generation', '生成 PDF/富文本文档。', ['PDF 生成、导出'], ['解析见 parse'], []),
        ('documents.preview', '文档预览', 'Document Preview', '系统快速预览与缩略图。', ['Quick Look / 预览'], ['完整阅读见 reading'], []),
        ('documents.pagination', '分页与目录', 'Pagination and Outline', '分页模型、目录与页码跳转。', ['分页、大纲、跳转'], ['阅读呈现见 reading'], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="documents", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- documents.parse ---
    leaf(f, "documents.parse.pdf", "documents.parse", "parse_operation", "PDF结构解析", "PDF Structure Parse",
         "解析 PDF 页面、对象与元数据。", ['PdfRenderer / PDFKit'], ['文本提取见 text_extract'],
         B(('PdfRenderer', 'https://developer.android.com/reference/android/graphics/pdf/PdfRenderer'), ('PDFKit', 'https://developer.apple.com/documentation/pdfkit', 'framework'), ('pdfService', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pdfservice')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.parse.text_extract", "documents.parse", "parse_operation", "文档文本提取", "Document Text Extract",
         "从文档提取纯文本与阅读顺序。", ['text extraction'], ['OCR 见 ai.vision'],
         B(('PdfRenderer', 'https://developer.android.com/reference/android/graphics/pdf/PdfRenderer'), ('PDFSelection', 'https://developer.apple.com/documentation/pdfkit/pdfselection', 'class'), ('pdfService', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pdfservice')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.parse.metadata", "documents.parse", "parse_operation", "文档元数据", "Document Metadata",
         "读取标题、作者、页数等元数据。", ['document info'], ['结构解析见 pdf'],
         B(('PdfDocument', 'https://developer.android.com/reference/android/graphics/pdf/PdfDocument'), ('PDFDocument', 'https://developer.apple.com/documentation/pdfkit/pdfdocument', 'class'), ('pdfService', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pdfservice')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.parse.form_fields", "documents.parse", "parse_operation", "表单字段解析", "Form Field Parse",
         "解析 PDF 表单字段结构。", ['AcroForm fields'], ['填写见 annotation'],
         B(None, ('PDFAnnotation widget', 'https://developer.apple.com/documentation/pdfkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.parse.office_open", "documents.parse", "parse_operation", "办公文档打开", "Office Document Open",
         "打开或导入常见办公文档格式入口。", ['office open'], ['PDF 见 pdf'],
         B(None, ('Quick Look', 'https://developer.apple.com/documentation/quicklook', 'framework'), ('file preview', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-preview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.parse.encryption_detect", "documents.parse", "parse_operation", "文档加密检测", "Document Encryption Detect",
         "检测文档是否加密及解锁入口。", ['password PDF'], ['解析见 pdf'],
         B(None, ('PDFDocument unlock', 'https://developer.apple.com/documentation/pdfkit/pdfdocument', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- documents.reading ---
    leaf(f, "documents.reading.reflow", "documents.reading", "reading_operation", "文本重排阅读", "Text Reflow Reading",
         "将固定版式重排为自适应阅读流。", ['reflow'], ['分页见 pagination'],
         B(None, ('PDFView displayMode', 'https://developer.apple.com/documentation/pdfkit/pdfview', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.reading.theme", "documents.reading", "reading_operation", "阅读主题", "Reading Theme",
         "夜间模式、背景与正文字号主题。", ['reader theme'], ['系统深色见 ui'],
         B(None, ('PDFView', 'https://developer.apple.com/documentation/pdfkit/pdfview', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.reading.progress", "documents.reading", "reading_operation", "阅读进度", "Reading Progress",
         "保存与恢复阅读位置。", ['reading progress'], ['书签见 bookmarks'],
         B(None, ('PDFView currentPage', 'https://developer.apple.com/documentation/pdfkit/pdfview', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.reading.bookmarks", "documents.reading", "reading_operation", "书签", "Bookmarks",
         "创建与跳转文档书签。", ['bookmarks'], ['进度见 progress'],
         B(None, ('PDFOutline', 'https://developer.apple.com/documentation/pdfkit/pdfoutline', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.reading.search", "documents.reading", "reading_operation", "文内搜索", "In-Document Search",
         "在文档正文中搜索关键字。", ['find string'], ['文本提取见 parse.text_extract'],
         B(None, ('PDFDocument find', 'https://developer.apple.com/documentation/pdfkit/pdfdocument', 'class'), ('pdfService', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pdfservice')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.reading.selection", "documents.reading", "reading_operation", "文本选择复制", "Text Selection Copy",
         "选择文档文本并复制。", ['selection'], ['批注高亮见 annotation'],
         B(None, ('PDFSelection', 'https://developer.apple.com/documentation/pdfkit/pdfselection', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.reading.tts_read_aloud", "documents.reading", "reading_operation", "朗读阅读", "Read Aloud",
         "将当前阅读内容送入朗读。", ['read aloud'], ['TTS 引擎见 ai.speech.tts'],
         B(('TextToSpeech', 'https://developer.android.com/reference/android/speech/tts/TextToSpeech'), ('AVSpeechSynthesizer', 'https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer', 'class'), ('textToSpeech', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-texttospeech')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- documents.annotation ---
    leaf(f, "documents.annotation.highlight", "documents.annotation", "annotation_operation", "高亮批注", "Highlight Annotation",
         "对文本范围添加高亮批注。", ['highlight'], ['墨迹见 ink'],
         B(None, ('PDFAnnotation', 'https://developer.apple.com/documentation/pdfkit/pdfannotation', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.annotation.ink", "documents.annotation", "annotation_operation", "墨迹批注", "Ink Annotation",
         "手写墨迹批注与笔画存储。", ['ink annotation'], ['高亮见 highlight'],
         B(('pdf Ink', 'https://developer.android.com/jetpack/androidx/releases/pdf', 'guide'), ('PDFAnnotation ink', 'https://developer.apple.com/documentation/pdfkit/pdfannotation', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.annotation.comments", "documents.annotation", "annotation_operation", "评论批注", "Comment Annotation",
         "添加文本评论或便签批注。", ['text note annotation'], ['高亮见 highlight'],
         B(None, ('PDFAnnotation text', 'https://developer.apple.com/documentation/pdfkit/pdfannotation', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.annotation.form_fill", "documents.annotation", "annotation_operation", "表单填写", "Form Fill",
         "填写并保存 PDF 表单字段。", ['form fill'], ['字段解析见 parse.form_fields'],
         B(None, ('PDFAnnotation widget', 'https://developer.apple.com/documentation/pdfkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.annotation.export", "documents.annotation", "annotation_operation", "批注导出合并", "Annotation Export Merge",
         "导出具批注的文档或合并批注层。", ['export annotated PDF'], ['生成见 generate'],
         B(None, ('PDFDocument write', 'https://developer.apple.com/documentation/pdfkit/pdfdocument', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- documents.generate ---
    leaf(f, "documents.generate.pdf_create", "documents.generate", "generate_operation", "PDF创建写入", "PDF Create Write",
         "创建 PDF 并写入页面内容。", ['PdfDocument / UIGraphicsPDFRenderer'], ['打印到 PDF 见 print_scan'],
         B(('PdfDocument', 'https://developer.android.com/reference/android/graphics/pdf/PdfDocument'), ('UIGraphicsPDFRenderer', 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer', 'class'), ('pdfService', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pdfservice')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.generate.from_view", "documents.generate", "generate_operation", "视图导出文档", "Export View to Document",
         "将视图层次导出为 PDF/图片文档。", ['view to PDF'], ['创建写入见 pdf_create'],
         B(('PdfDocument.Page', 'https://developer.android.com/reference/android/graphics/pdf/PdfDocument.Page'), ('UIGraphicsPDFRenderer', 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.generate.html_to_pdf", "documents.generate", "generate_operation", "HTML转PDF", "HTML to PDF",
         "将 HTML/Web 内容渲染为 PDF。", ['print to PDF from web'], ['WebView 见 web'],
         B(('PrintDocumentAdapter', 'https://developer.android.com/reference/android/print/PrintDocumentAdapter'), ('WKWebView createPDF', 'https://developer.apple.com/documentation/webkit/wkwebview', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.generate.image_pdf", "documents.generate", "generate_operation", "图片合成PDF", "Images to PDF",
         "将多张图片合成为 PDF。", ['images to PDF'], ['创建写入见 pdf_create'],
         B(('PdfDocument', 'https://developer.android.com/reference/android/graphics/pdf/PdfDocument'), ('PDFKit', 'https://developer.apple.com/documentation/pdfkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.generate.template_merge", "documents.generate", "generate_operation", "模板合并生成", "Template Merge Generate",
         "基于模板填充生成文档。", ['template merge'], ['表单填写见 annotation.form_fill'],
         B(None, ('PDFKit', 'https://developer.apple.com/documentation/pdfkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- documents.preview ---
    leaf(f, "documents.preview.quick_look", "documents.preview", "preview_operation", "系统快速预览", "System Quick Look",
         "调用系统快速预览呈现文档。", ['QuickLook / Intent.ACTION_VIEW'], ['应用内阅读见 reading'],
         B(('ACTION_VIEW', 'https://developer.android.com/reference/android/content/Intent'), ('QLPreviewController', 'https://developer.apple.com/documentation/quicklook/qlpreviewcontroller', 'class'), ('file preview', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-preview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.preview.thumbnail", "documents.preview", "preview_operation", "文档页缩略图", "Document Page Thumbnail",
         "生成文档页缩略图。", ['thumbnail'], ['快速预览见 quick_look'],
         B(('PdfRenderer.openPage', 'https://developer.android.com/reference/android/graphics/pdf/PdfRenderer'), ('QLThumbnailGenerator', 'https://developer.apple.com/documentation/quicklookthumbnailing', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.preview.in_app", "documents.preview", "preview_operation", "应用内预览组件", "In-App Preview Component",
         "嵌入应用内文档预览组件。", ['PDFView / PdfViewer'], ['系统预览见 quick_look'],
         B(('androidx.pdf', 'https://developer.android.com/jetpack/androidx/releases/pdf', 'guide'), ('PDFView', 'https://developer.apple.com/documentation/pdfkit/pdfview', 'class'), ('pdfService', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pdfservice')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.preview.mime_handler", "documents.preview", "preview_operation", "类型预览处理器", "MIME Preview Handler",
         "按 MIME/UTI 注册预览处理。", ['UTI preview'], ['快速预览见 quick_look'],
         B(('Intent filters', 'https://developer.android.com/guide/components/intents-filters', 'guide'), ('QLPreviewItem', 'https://developer.apple.com/documentation/quicklook/qlpreviewitem', 'protocol'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- documents.pagination ---
    leaf(f, "documents.pagination.page_model", "documents.pagination", "pagination_operation", "分页模型", "Page Model",
         "维护页列表与页尺寸模型。", ['page model'], ['跳转见 goto'],
         B(('PdfRenderer pageCount', 'https://developer.android.com/reference/android/graphics/pdf/PdfRenderer'), ('PDFDocument pageCount', 'https://developer.apple.com/documentation/pdfkit/pdfdocument', 'class'), ('pdfService', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pdfservice')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.pagination.outline", "documents.pagination", "pagination_operation", "目录大纲", "Document Outline",
         "读取并导航文档目录大纲。", ['outline / bookmarks tree'], ['书签见 reading.bookmarks'],
         B(None, ('PDFOutline', 'https://developer.apple.com/documentation/pdfkit/pdfoutline', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.pagination.goto", "documents.pagination", "pagination_operation", "页码跳转", "Go to Page",
         "按页码或目标跳转。", ['go to page'], ['分页模型见 page_model'],
         B(None, ('PDFView go(to:)', 'https://developer.apple.com/documentation/pdfkit/pdfview', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.pagination.links", "documents.pagination", "pagination_operation", "页内链接跳转", "In-Doc Link Navigation",
         "处理文档内链接与交叉引用跳转。", ['internal links'], ['目录见 outline'],
         B(None, ('PDFDestination', 'https://developer.apple.com/documentation/pdfkit/pdfdestination', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "documents.pagination.continuous_scroll", "documents.pagination", "pagination_operation", "连续滚动分页", "Continuous Scroll Pagination",
         "连续滚动与单页模式切换。", ['display mode'], ['分页模型见 page_model'],
         B(None, ('PDFView displayMode', 'https://developer.apple.com/documentation/pdfkit/pdfview', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")


    leaf(f, "documents.parse.attachments", "documents.parse", "parse_operation", "文档内嵌附件", "Embedded Attachments",
         "枚举并提取文档内嵌附件。", ["embedded files"], ["结构解析见 pdf"],
         B(None, ("PDFDocument", "https://developer.apple.com/documentation/pdfkit/pdfdocument", "class"), None))
    leaf(f, "documents.reading.two_page", "documents.reading", "reading_operation", "双页阅读", "Two-Page Reading",
         "双页对开阅读布局。", ["two-up"], ["主题见 theme"],
         B(None, ("PDFView displayMode", "https://developer.apple.com/documentation/pdfkit/pdfview", "class"), None))
    leaf(f, "documents.annotation.stamp", "documents.annotation", "annotation_operation", "图章批注", "Stamp Annotation",
         "添加图章类批注。", ["stamp"], ["高亮见 highlight"],
         B(None, ("PDFAnnotation", "https://developer.apple.com/documentation/pdfkit/pdfannotation", "class"), None))
    leaf(f, "documents.generate.watermark", "documents.generate", "generate_operation", "水印生成", "Watermark Generation",
         "生成带水印的文档输出。", ["watermark"], ["PDF 创建见 pdf_create"],
         B(("PdfDocument", "https://developer.android.com/reference/android/graphics/pdf/PdfDocument"),
           ("UIGraphicsPDFRenderer", "https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer", "class"), None))
    leaf(f, "documents.preview.password_prompt", "documents.preview", "preview_operation", "预览密码提示", "Preview Password Prompt",
         "预览加密文档时的密码提示。", ["password prompt"], ["加密检测见 parse.encryption_detect"],
         B(None, ("QLPreviewController", "https://developer.apple.com/documentation/quicklook/qlpreviewcontroller", "class"), None))
    leaf(f, "documents.pagination.print_layout", "documents.pagination", "pagination_operation", "打印分页布局", "Print Pagination Layout",
         "按打印介质计算分页布局。", ["print layout"], ["分页模型见 page_model"],
         B(("PrintDocumentAdapter", "https://developer.android.com/reference/android/print/PrintDocumentAdapter"),
           ("UIPrintPageRenderer", "https://developer.apple.com/documentation/uikit/uiprintpagerenderer", "class"), None))

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("documents", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
