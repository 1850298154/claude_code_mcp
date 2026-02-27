# Analyzer Operations Module

> VisionAnalyzer 操作集合

## 操作列表

| 操作 | 文件 | 描述 | Bash 定位 |
|------|------|------|-----------|
| analyze_image | `analyze_image.py` | 分析图像 | `find . -name "analyze_image.py"` |
| detect_objects | `detect_objects.py` | 检测对象 | `find . -name "detect_objects.py"` |
| extract_text | `extract_text.py` | 提取文本（OCR） | `find . -name "extract_text.py"` |
| describe_scene | `describe_scene.py` | 描述场景 | `find . -name "describe_scene.py"` |
| compare_images | `compare_images.py` | 比较图像 | `find . -name "compare_images.py"` |

## 结构

```
analyzer/
├── README.md              # 本文件
├── analyze_image.py       # 分析图像
├── detect_objects.py      # 检测对象
├── extract_text.py        # 提取文本（OCR）
├── describe_scene.py      # 描述场景
└── compare_images.py      # 比较图像
```
