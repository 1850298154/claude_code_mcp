# ============================================================================
# 文件: src/vision/analyzer.py
# 描述: VisionAnalyzer 类定义，用于视觉模型调用
#
# 上游依赖:
#   - vision/types.py                        (ImageAnalysis, ModelType)
#   - vision/models/glm4v.py              (GLM4VModel)
#
# 下游封装:
#   - analyzer/*                               (操作函数)
#   - mcp/tools/vision.py                    (MCP 工具封装)
#
# Bash 快速定位:
#   find . -name "analyzer.py" -path "*/vision/*"
# ============================================================================

from typing import List
from pathlib import Path

from vision.types import ImageAnalysis, ModelConfig, DetectedObject
from vision.models.glm4v import GLM4VModel


class VisionAnalyzer:
    """Vision Analyzer - 视觉模型调用

    提供图像分析、对象检测、OCR 等视觉功能。
    """

    def __init__(self, model: str = "glm4v", api_key: str | None = None):
        """初始化 Analyzer

        Args:
            model: 使用的模型类型
            api_key: API 密钥（如果需要）
        """
        self._model_type = model
        config = ModelConfig(api_key=api_key)
        self._model = GLM4VModel(config)

    def analyze_image(
        self, image_path: Path | str, prompt: str = ""
    ) -> ImageAnalysis:
        """分析图像

        实现位置: analyzer/analyze_image.py

        Args:
            image_path: 图像文件路径
            prompt: 分析提示词

        Returns:
            图像分析结果
        """
        # 转换为字符串
        if isinstance(image_path, Path):
            image_path = str(image_path)

        # 调用模型分析
        description = self._model.analyze_image(image_path, prompt)

        return ImageAnalysis(description=description)

    def detect_objects(self, image_path: Path | str) -> List[DetectedObject]:
        """检测图像中的对象

        实现位置: analyzer/detect_objects.py

        Args:
            image_path: 图像文件路径

        Returns:
            检测到的对象列表
        """
        if isinstance(image_path, Path):
            image_path = str(image_path)

        objects = self._model.detect_objects(image_path)
        return objects

    def extract_text(self, image_path: Path | str) -> str:
        """提取图像中的文本（OCR）

        实现位置: analyzer/extract_text.py

        Args:
            image_path: 图像文件路径

        Returns:
            提取的文本
        """
        if isinstance(image_path, Path):
            image_path = str(image_path)

        return self._model.extract_text(image_path)

    def describe_scene(self, image_path: Path | str) -> str:
        """描述图像场景

        实现位置: analyzer/describe_scene.py

        Args:
            image_path: 图像文件路径

        Returns:
            场景描述
        """
        prompt = "请详细描述这张图片的内容和场景"
        result = self.analyze_image(image_path, prompt)
        return result.description

    def compare_images(
        self, image1_path: Path | str, image2_path: Path | str
    ) -> dict:
        """比较两张图像

        实现位置: analyzer/compare_images.py

        Args:
            image1_path: 第一张图像路径
            image2_path: 第二张图像路径

        Returns:
            比较结果（相似度、差异等）
        """
        # 简单实现：描述两张图像并比较描述
        desc1 = self.describe_scene(image1_path)
        desc2 = self.describe_scene(image2_path)

        return {
            "image1_description": desc1,
            "image2_description": desc2,
            "similarity": 1.0 if desc1 == desc2 else 0.0,
        }

    def close(self):
        """关闭分析器"""
        self._model.close()

    def __enter__(self):
        """支持上下文管理器"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文管理器"""
        self.close()
