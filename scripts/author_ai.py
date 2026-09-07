#!/usr/bin/env python3
"""Author the ai domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "ai_capability_family"


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
        "ai", parent=None, level="L1",
        zh="AI与智能", en="AI and Intelligence",
        definition="端侧模型运行、视觉/语音/自然语言能力、系统意图代理与通用推理执行。",
        includes=['端侧运行时、视觉、语音、NLP、意图、推理'],
        excludes=['云端仅业务后端', '无障碍读屏见 a11y', '搜索索引见 storage'],
        legacy={'disposition': 'kept', 'sources': ['ai']},
    ))
    l2 = [
        ('ai.on_device', '端侧AI运行时', 'On-Device AI Runtime', '设备上加载、更新与管理通用 ML/LLM 运行时。', ['runtime、模型包、版本'], ['具体模态能力见 vision/speech/nlp'], ['ai.on_device']),
        ('ai.vision', '视觉智能', 'Vision Intelligence', '图像/视频理解、检测、识别与增强。', ['OCR、检测、人脸、分割、条码'], ['文档扫描业务编排见 documents'], []),
        ('ai.speech', '语音与声音智能', 'Speech and Sound Intelligence', '语音识别、合成与声音分类。', ['ASR、TTS、声音事件'], ['通话音频路由见 telecom/device'], []),
        ('ai.nlp', '自然语言处理', 'Natural Language Processing', '分词、实体、翻译、智能回复等文本理解生成。', ['tokenize、实体、翻译、回复'], ['系统意图代理见 intents'], []),
        ('ai.intents', '智能意图与代理', 'Intents and Agents', '应用意图声明、系统建议与代理任务入口。', ['App Intents、建议、代理'], ['传统隐式 Intent 见 interop'], []),
        ('ai.inference', '通用模型推理', 'General Model Inference', '张量级模型加载、编译、执行与加速调度。', ['加载、张量IO、NPU/GPU、兼容检查'], ['高层视觉/语音API见对应分支'], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="ai", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- ai.on_device ---
    leaf(f, "ai.on_device.runtime", "ai.on_device", "on_device_operation", "端侧ML运行时", "On-Device ML Runtime",
         "加载并执行端侧机器学习运行时。", ['ML Kit / Core ML / MindSpore Lite'], ['张量推理细节见 inference'],
         B(('ML Kit', 'https://developers.google.com/ml-kit', 'guide'), ('Core ML', 'https://developer.apple.com/documentation/coreml', 'framework'), ('MindSpore Lite', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines', 'guide')), {'disposition': 'kept', 'sources': ['ai.on_device.runtime']}, level="L3", privacy="none")
    leaf(f, "ai.on_device.model_package", "ai.on_device", "on_device_operation", "端侧模型包管理", "On-Device Model Package",
         "下载、缓存与切换端侧模型包。", ['model download/update'], ['推理执行见 inference.execute'],
         B(('ML Model Download', 'https://developers.google.com/ml-kit', 'guide'), ('MLModelCollection', 'https://developer.apple.com/documentation/coreml', 'framework'), ('model management', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.on_device.system_llm", "ai.on_device", "on_device_operation", "系统端侧大模型", "System On-Device LLM",
         "调用系统提供的端侧大语言模型能力。", ['system LLM API'], ['通用推理引擎见 inference'],
         B(('Gemini Nano / AICore', 'https://developer.android.com/ml/aicore', 'guide'), ('Foundation Models', 'https://developer.apple.com/documentation/foundationmodels', 'framework'), ('System LLM', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.on_device.runtime_version", "ai.on_device", "on_device_operation", "AI运行时版本查询", "AI Runtime Version Query",
         "查询端侧 AI 运行时与加速库版本。", ['runtime version'], ['模型加载见 inference.model_loading'],
         B(('AICore', 'https://developer.android.com/ml/aicore', 'guide'), ('Core ML', 'https://developer.apple.com/documentation/coreml', 'framework'), ('MindSpore Lite', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.on_device.personalize", "ai.on_device", "on_device_operation", "端侧模型个性化", "On-Device Model Personalization",
         "在设备上对模型做个性化更新或适配。", ['LoRA/personalize'], ['基础推理见 inference'],
         B(None, ('MLUpdateTask', 'https://developer.apple.com/documentation/coreml', 'framework'), ('model update', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.on_device.compat_check", "ai.on_device", "on_device_operation", "模型设备兼容检查", "Model Device Compatibility",
         "检查模型与当前设备加速能力是否兼容。", ['compat check'], ['加载见 inference.model_loading'],
         B(('AICore availability', 'https://developer.android.com/ml/aicore', 'guide'), ('MLModelConfiguration', 'https://developer.apple.com/documentation/coreml/mlmodelconfiguration', 'class'), ('MindSpore Lite', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- ai.vision ---
    leaf(f, "ai.vision.text_recognition", "ai.vision", "vision_capability", "文字识别OCR", "Text Recognition OCR",
         "从图像中识别文字内容。", ['TextRecognizer / VNRecognizeText'], ['文档分页阅读见 documents'],
         B(('Text Recognition', 'https://developers.google.com/ml-kit/vision/text-recognition', 'guide'), ('VNRecognizeTextRequest', 'https://developer.apple.com/documentation/vision/vnrecognizetextrequest', 'class'), ('textRecognition', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-textrecognition')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.vision.barcode", "ai.vision", "vision_capability", "条码与二维码识别", "Barcode Recognition",
         "识别一维码与二维码。", ['BarcodeScanner'], ['相机预览见 media'],
         B(('Barcode Scanning', 'https://developers.google.com/ml-kit/vision/barcode-scanning', 'guide'), ('VNDetectBarcodesRequest', 'https://developer.apple.com/documentation/vision/vndetectbarcodesrequest', 'class'), ('scanBarcode', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-scan')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.vision.face", "ai.vision", "vision_capability", "人脸检测", "Face Detection",
         "检测人脸位置、关键点与基础属性。", ['FaceDetector'], ['生物识别解锁见 security'],
         B(('Face Detection', 'https://developers.google.com/ml-kit/vision/face-detection', 'guide'), ('VNDetectFaceRectanglesRequest', 'https://developer.apple.com/documentation/vision/vndetectfacerectanglesrequest', 'class'), ('faceDetector', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-faceDetector')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "ai.vision.object_detection", "ai.vision", "vision_capability", "目标检测", "Object Detection",
         "检测图像中的物体类别与边界框。", ['ObjectDetector'], ['分割见 semantic_segmentation'],
         B(('Object Detection', 'https://developers.google.com/ml-kit/vision/object-detection', 'guide'), ('VNRecognizeObjectsRequest', 'https://developer.apple.com/documentation/vision', 'framework'), ('object detection', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.vision.image_classification", "ai.vision", "vision_capability", "图像分类", "Image Classification",
         "对整图进行语义类别分类。", ['ImageLabeler'], ['目标检测见 object_detection'],
         B(('Image Labeling', 'https://developers.google.com/ml-kit/vision/image-labeling', 'guide'), ('VNClassifyImageRequest', 'https://developer.apple.com/documentation/vision/vnclassifyimagerequest', 'class'), ('image classification', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.vision.semantic_segmentation", "ai.vision", "vision_capability", "语义分割", "Semantic Segmentation",
         "对图像像素进行语义分割。", ['segmentation mask'], ['目标检测见 object_detection'],
         B(('Selfie Segmentation', 'https://developers.google.com/ml-kit/vision/selfie-segmentation', 'guide'), ('VNGeneratePersonSegmentationRequest', 'https://developer.apple.com/documentation/vision', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.vision.hand_pose", "ai.vision", "vision_capability", "手势姿态估计", "Hand Pose Estimation",
         "估计手部关键点与姿态。", ['hand pose'], ['通用姿态传感器见 sensors'],
         B(('Pose Detection', 'https://developers.google.com/ml-kit/vision/pose-detection', 'guide'), ('VNDetectHumanHandPoseRequest', 'https://developer.apple.com/documentation/vision', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.vision.image_enhance", "ai.vision", "vision_capability", "图像增强", "Image Enhancement",
         "端侧图像超分、降噪或质量增强。", ['image enhance'], ['创意生成见 gen_image'],
         B(None, ('Core Image', 'https://developer.apple.com/documentation/coreimage', 'framework'), ('image super resolution', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.vision.gen_image", "ai.vision", "vision_capability", "端侧图像生成编辑", "On-Device Image Generation",
         "端侧生成或编辑图像内容。", ['genAI image'], ['图像增强见 image_enhance'],
         B(None, ('Image Playground', 'https://developer.apple.com/documentation/imageplayground', 'framework'), ('genAI image', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.vision.visual_intelligence", "ai.vision", "vision_capability", "视觉智能查询", "Visual Intelligence Query",
         "对屏幕或图像内容做系统级视觉问答/提取。", ['visual intelligence'], ['OCR 见 text_recognition'],
         B(None, ('Visual Intelligence', 'https://developer.apple.com/documentation/visualintelligence', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- ai.speech ---
    leaf(f, "ai.speech.recognition", "ai.speech", "speech_capability", "语音识别", "Speech Recognition",
         "将语音转写为文本。", ['SpeechRecognizer / SFSpeech'], ['TTS 见 tts'],
         B(('SpeechRecognizer', 'https://developer.android.com/reference/android/speech/SpeechRecognizer'), ('SFSpeechRecognizer', 'https://developer.apple.com/documentation/speech/sfspeechrecognizer', 'class'), ('speechRecognizer', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-speechrecognizer')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "ai.speech.tts", "ai.speech", "speech_capability", "语音合成", "Text to Speech",
         "将文本合成为语音播放。", ['TextToSpeech'], ['识别见 recognition'],
         B(('TextToSpeech', 'https://developer.android.com/reference/android/speech/tts/TextToSpeech'), ('AVSpeechSynthesizer', 'https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer', 'class'), ('textToSpeech', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-texttospeech')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.speech.sound_classification", "ai.speech", "speech_capability", "声音事件分类", "Sound Classification",
         "对环境声音事件进行分类识别。", ['sound classifier'], ['语音转写见 recognition'],
         B(('Sound Detection', 'https://developer.android.com/guide/topics/sensors/sound-detection', 'guide'), ('SoundAnalysis', 'https://developer.apple.com/documentation/soundanalysis', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "ai.speech.music_recognition", "ai.speech", "speech_capability", "音乐识别", "Music Recognition",
         "识别正在播放的音乐曲目。", ['music recognizer'], ['声音分类见 sound_classification'],
         B(None, ('ShazamKit', 'https://developer.apple.com/documentation/shazamkit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "ai.speech.language_id_audio", "ai.speech", "speech_capability", "语音语种识别", "Spoken Language Identification",
         "识别语音片段的语种。", ['spoken language id'], ['文本语种见 nlp.language_id'],
         B(None, ('SFSpeechRecognizer', 'https://developer.apple.com/documentation/speech/sfspeechrecognizer', 'class'), ('speechRecognizer', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-speechrecognizer')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.speech.dictation_session", "ai.speech", "speech_capability", "听写会话", "Dictation Session",
         "面向输入场景的连续听写会话。", ['dictation'], ['通用 ASR 见 recognition'],
         B(('RecognizerIntent', 'https://developer.android.com/reference/android/speech/RecognizerIntent'), ('Dictation', 'https://developer.apple.com/documentation/speech', 'framework'), ('speechRecognizer', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-speechrecognizer')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")

    # --- ai.nlp ---
    leaf(f, "ai.nlp.tokenization", "ai.nlp", "nlp_capability", "分词与词法分析", "Tokenization",
         "对文本进行分词与基础词法分析。", ['tokenizer'], ['实体抽取见 entity_extraction'],
         B(('ML Kit NLP', 'https://developers.google.com/ml-kit', 'guide'), ('NLTokenizer', 'https://developer.apple.com/documentation/naturallanguage/nltokenizer', 'class'), ('text processing', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.nlp.language_id", "ai.nlp", "nlp_capability", "文本语种识别", "Language Identification",
         "识别文本语种。", ['LanguageIdentifier'], ['翻译见 translation'],
         B(('Language Identification', 'https://developers.google.com/ml-kit/language/identification', 'guide'), ('NLLanguageRecognizer', 'https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.nlp.entity_extraction", "ai.nlp", "nlp_capability", "实体抽取", "Entity Extraction",
         "从文本抽取人名、地址、日期等实体。", ['EntityExtractor'], ['分词见 tokenization'],
         B(('Entity Extraction', 'https://developers.google.com/ml-kit/language/entity-extraction', 'guide'), ('NLTagger', 'https://developer.apple.com/documentation/naturallanguage/nltagger', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.nlp.translation", "ai.nlp", "nlp_capability", "端侧翻译", "On-Device Translation",
         "在设备上进行文本翻译。", ['Translator'], ['语种识别见 language_id'],
         B(('Translation', 'https://developers.google.com/ml-kit/language/translation', 'guide'), ('TranslationSession', 'https://developer.apple.com/documentation/translation', 'framework'), ('translation', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-translation')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.nlp.smart_reply", "ai.nlp", "nlp_capability", "智能回复建议", "Smart Reply",
         "基于对话上下文生成短回复建议。", ['SmartReply'], ['系统建议见 intents'],
         B(('Smart Reply', 'https://developers.google.com/ml-kit/language/smart-reply', 'guide'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.nlp.summarization", "ai.nlp", "nlp_capability", "文本摘要", "Text Summarization",
         "对长文本生成摘要。", ['summarization'], ['翻译见 translation'],
         B(None, ('Writing Tools', 'https://developer.apple.com/documentation/foundationmodels', 'framework'), ('text summary', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.nlp.sentiment", "ai.nlp", "nlp_capability", "情感分析", "Sentiment Analysis",
         "判断文本情感极性或类别。", ['sentiment'], ['实体见 entity_extraction'],
         B(None, ('NLModel', 'https://developer.apple.com/documentation/naturallanguage/nlmodel', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- ai.intents ---
    leaf(f, "ai.intents.app_intents", "ai.intents", "intent_capability", "应用意图声明", "App Intent Declaration",
         "声明可供系统调用的应用意图与参数。", ['AppIntents / App Actions'], ['传统 deeplink 见 interop'],
         B(('App Actions', 'https://developer.android.com/guide/actions', 'guide'), ('AppIntents', 'https://developer.apple.com/documentation/appintents', 'framework'), ('Intent Framework', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intent-framework-overview')), {'disposition': 'merged_from', 'sources': ['ai.system.suggestions']}, level="L3", privacy="none")
    leaf(f, "ai.intents.voice_shortcuts", "ai.intents", "intent_capability", "语音快捷指令", "Voice Shortcuts",
         "将应用能力注册为语音或系统快捷指令。", ['App Shortcuts / Siri'], ['意图声明见 app_intents'],
         B(('App Shortcuts', 'https://developer.android.com/develop/devices/assistant/app-shortcuts', 'guide'), ('App Shortcuts', 'https://developer.apple.com/documentation/appintents/app-shortcuts', 'guide'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.intents.system_suggestions", "ai.intents", "intent_capability", "系统智能建议", "System Intelligent Suggestions",
         "向系统建议面板贡献或消费建议。", ['suggestions'], ['意图声明见 app_intents'],
         B(('Google Assistant App Actions', 'https://developer.android.com/guide/actions', 'guide'), ('Siri Suggestions', 'https://developer.apple.com/documentation/sirikit', 'framework'), ('Intent suggestions', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intent-framework-overview')), {'disposition': 'renamed_from', 'sources': ['ai.system']}, level="L3", privacy="none")
    leaf(f, "ai.intents.agent_task", "ai.intents", "intent_capability", "代理任务状态", "Agent Task Status",
         "展示或更新智能代理任务执行状态。", ['agent task status'], ['意图声明见 app_intents'],
         B(None, ('AppIntents', 'https://developer.apple.com/documentation/appintents', 'framework'), ('Intent Framework', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intent-framework-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.intents.local_intent", "ai.intents", "intent_capability", "本地意图识别", "Local Intent Recognition",
         "在端侧将自然语言映射为应用意图。", ['local intent'], ['ASR 见 speech.recognition'],
         B(None, ('AppIntents', 'https://developer.apple.com/documentation/appintents', 'framework'), ('local intent', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intent-framework-overview')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.intents.assistant_handoff", "ai.intents", "intent_capability", "助手能力交接", "Assistant Capability Handoff",
         "将用户请求交给系统助手或应用意图处理。", ['assistant handoff'], ['代理状态见 agent_task'],
         B(('Assistant', 'https://developer.android.com/develop/devices/assistant', 'guide'), ('SiriKit', 'https://developer.apple.com/documentation/sirikit', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- ai.inference ---
    leaf(f, "ai.inference.model_loading", "ai.inference", "inference_operation", "模型加载与编译", "Model Loading and Compile",
         "加载模型文件并编译为可执行图。", ['load/compile'], ['执行见 execute'],
         B(('LiteRT / TFLite', 'https://ai.google.dev/edge/litert', 'guide'), ('MLModel', 'https://developer.apple.com/documentation/coreml/mlmodel', 'class'), ('MindSpore Lite', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.inference.tensor_io", "ai.inference", "inference_operation", "张量输入输出", "Tensor Input Output",
         "构造推理输入输出张量缓冲区。", ['tensor IO'], ['加载见 model_loading'],
         B(('TensorImage', 'https://ai.google.dev/edge/litert', 'guide'), ('MLMultiArray', 'https://developer.apple.com/documentation/coreml/mlmultiarray', 'class'), ('MindSpore Lite', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.inference.execute", "ai.inference", "inference_operation", "推理执行", "Inference Execution",
         "执行一次或批量模型推理。", ['run inference'], ['加速调度见 accel_dispatch'],
         B(('Interpreter', 'https://ai.google.dev/edge/litert', 'guide'), ('MLModel.prediction', 'https://developer.apple.com/documentation/coreml/mlmodel', 'class'), ('MindSpore Lite', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.inference.accel_dispatch", "ai.inference", "inference_operation", "异构加速调度", "Heterogeneous Accel Dispatch",
         "在 CPU/GPU/NPU 间调度推理执行。", ['GPU/NPU delegate'], ['执行见 execute'],
         B(('GPU Delegate', 'https://ai.google.dev/edge/litert', 'guide'), ('MLComputeUnits', 'https://developer.apple.com/documentation/coreml/mlcomputeunits', 'enum'), ('NPU execution', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.inference.preprocess", "ai.inference", "inference_operation", "输入预处理", "Input Preprocess",
         "对图像/音频等输入做推理前预处理。", ['preprocess'], ['张量IO见 tensor_io'],
         B(('ImageProcessor', 'https://ai.google.dev/edge/litert', 'guide'), ('VNCoreMLRequest', 'https://developer.apple.com/documentation/vision/vncoremlrequest', 'class'), ('MindSpore Lite', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.inference.profiling", "ai.inference", "inference_operation", "推理性能分析", "Inference Profiling",
         "采集推理耗时与算子级性能数据。", ['profiling'], ['执行见 execute'],
         B(('Benchmark', 'https://ai.google.dev/edge/litert', 'guide'), ('Core ML performance', 'https://developer.apple.com/documentation/coreml', 'framework'), ('MindSpore Lite', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "ai.inference.custom_ops", "ai.inference", "inference_operation", "自定义算子扩展", "Custom Operator Extension",
         "注册或执行自定义推理算子。", ['custom ops'], ['基础执行见 execute'],
         B(('Custom ops', 'https://ai.google.dev/edge/litert', 'guide'), ('MLCustomLayer', 'https://developer.apple.com/documentation/coreml', 'framework'), ('custom operator', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("ai", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
