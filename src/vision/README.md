# Vision Analyzer Module

> 视觉模型调用模块

## 模块说明

提供图像分析、对象检测、OCR 等视觉功能，主要集成 GLM-4V 和 GPT-4V 模型。

## 子模块

| 子模块 | 路径 | 描述 | Bash 定位 |
|--------|------|------|-----------|
| Analyzer | `vision/analyzer.py` | VisionAnalyzer 数据结构定义 | `find . -name "analyzer.py" -path "*/vision/*"` |
| Analyzer Ops | `vision/analyzer/` | Analyzer 操作集合 | `find . -path "*/vision/analyzer/*.py"` |
| Models | `vision/models/` | 模型封装 | `find . -path "*/vision/models/*.py"` |

## 依赖关系

```
vision/
├── analyzer/
│   ├── 上游依赖: core/types/*, models/glm4v.py
│   └── 下游操作:
│       ├── analyze_image.py      # 分析图像
│       ├── detect_objects.py     # 检测对象
│       ├── extract_text.py      # 提取文本（OCR）
│       ├── describe_scene.py     # 描述场景
│       └── compare_images.py    # 比较图像
└── models/
    ├── 上游依赖: 无
    └── 下游模型:
        ├── glm4v.py             # GLM-4V 模型
        └── gpt4v.py             # GPT-4V 模型（可选）
```

## 快速操作

```bash
# 分析图像
python -m vision.analyzer.analyze_image --image screenshot.png

# 检测对象
python -m vision.analyzer.detect_objects --image photo.jpg

# 提取文本（OCR）
python -m vision.analyzer.extract_text --image document.png
```

## 结构

```
vision/
├── README.md              # 本文件
├── analyzer.py            # VisionAnalyzer 数据结构定义
├── analyzer/              # Analyzer 操作
│   ├── README.md
│   ├── analyze_image.py   # 分析图像
│   ├── detect_objects.py  # 检测对象
│   ├── extract_text.py    # 提取文本（OCR）
│   ├── describe_scene.py  # 描述场景
│   └── compare_images.py  # 比较图像
└── models/                # 模型封装
    ├── README.md
    ├── glm4v.py          # GLM-4V 模型
    └── gpt4v.py          # GPT-4V 模型（可选）
```

## 典型使用场景

1. **分析截图内容**
   ```python
   analyzer = VisionAnalyzer(model="glm4v")
   result = analyzer.analyze_image("screenshot.png")
   ```

2. **提取文档文本**
   ```python
   text = analyzer.extract_text("document.png")
   ```

3. **检测图像中的对象**
   ```python
   objects = analyzer.detect_objects("photo.jpg")
   ```
