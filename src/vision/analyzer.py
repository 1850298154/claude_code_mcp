# ============================================================================
# 文件: vision/analyzer.py
# 描述: VisionAnalyzer 数据结构定义，用于视觉模型调用
#
# 上游依赖:
#   - core/types/*                (通用类型)
#   - vision/models/glm4v.py     (GLM-4V 模型)
#   - vision/models/gpt4v.py     (GPT-4V 模型，可选)
#
# 下游封装:
#   - analyzer/analyze_image.py      (分析图像)
#   - analyzer/detect_objects.py     (检测对象)
#   - analyzer/extract_text.py      (提取文本 OCR)
#   - analyzer/describe_scene.py     (描述场景)
#   - analyzer/compare_images.py     (比较图像)
#
# Bash 快速定位:
#   find . -name "analyzer.py" -path "*/vision/*"
# ============================================================================

from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from pathlib import Path
from enum import Enum


class ModelType(Enum):
    """支持的视觉模型类型"""

    GLM4V = "glm4v"
    GPT4V = "gpt4v"


@dataclass
class DetectedObject:
    """检测到的对象数据结构

    Attributes:
        label: 对象标签
        confidence: 置信度 (0-1)
        bbox: 边界框 (x1, y1, x2, y2)
    """

    label: str
    confidence: float
    bbox: tuple[int, int, int, int]


@dataclass
class ImageAnalysis:
    """图像分析结果

    Attributes:
        description: 图像描述
        objects: 检测到的对象列表
        text: 提取的文本
        metadata: 额外元数据
    """

    description: str
    objects: Optional[List[DetectedObject]] = None
    text: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class VisionAnalyzer:
    """Vision Analyzer - 视觉模型调用

    提供图像分析、对象检测、OCR 等视觉功能。
    """

    def __init__(self, model: ModelType = ModelType.GLM4V, api_key: Optional[str] = None):
        """初始化 Analyzer

        Args:
            model: 使用的模型类型
            api_key: API 密钥（如果需要）
        """
        self._model = model
        self._api_key = api_key
        # 模型实现在 vision/models/*.py

    def analyze_image(self, image_path: Path, prompt: str = "") -> ImageAnalysis:
        """分析图像

        实现位置: analyzer/analyze_image.py

        Args:
            image_path: 图像文件路径
            prompt: 分析提示词

        Returns:
            图像分析结果
        """
        pass  # 实现在子文件中

    def detect_objects(self, image_path: Path) -> List[DetectedObject]:
        """检测图像中的对象

        实现位置: analyzer/detect_objects.py

        Args:
            image_path: 图像文件路径

        Returns:
            检测到的对象列表
        """
        pass  # 实现在子文件中

    def extract_text(self, image_path: Path) -> str:
        """提取图像中的文本（OCR）

        实现位置: analyzer/extract_text.py

        Args:
            image_path: 图像文件路径

        Returns:
            提取的文本
        """
        pass  # 实现在子文件中

    def describe_scene(self, image_path: Path) -> str:
        """描述图像场景

        实现位置: analyzer/describe_scene.py

        Args:
            image_path: 图像文件路径

        Returns:
            场景描述
        """
        pass  # 实现在子文件中

    def compare_images(self, image1_path: Path, image2_path: Path) -> dict:
        """比较两张图像

        实现位置: analyzer/compare_images.py

        Args:
            image1_path: 第一张图像路径
            image2_path: 第二张图像路径

        Returns:
            比较结果（相似度、差异等）
        """
        pass  # 实现在子文件中
