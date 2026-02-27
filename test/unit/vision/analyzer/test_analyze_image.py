# ============================================================================
# 文件: test/unit/vision/analyzer/test_analyze_image.py
# 描述: 测试 analyze_image 函数
#
# 测试对象: src/vision/analyzer/analyze_image.py
#
# Bash 快速定位:
#   find test -name "test_analyze_image.py"
# ============================================================================

import pytest
from unittest.mock import Mock

from vision.types import ImageAnalysis
from vision.models.glm4v import GLM4VModel
from vision.analyzer.analyze_image import analyze_image


class TestAnalyzeImage:
    """测试 analyze_image 函数"""

    def test_analyze_image_basic(self):
        """测试基本图像分析"""
        # Given: 模拟模型
        mock_model = Mock(spec=GLM4VModel)
        mock_model.analyze_image.return_value = "这是一张风景图片"

        # When: 分析图像
        result = analyze_image(mock_model, "image.png")

        # Then: 结果正确
        assert isinstance(result, ImageAnalysis)
        assert result.description == "这是一张风景图片"

    def test_analyze_image_with_prompt(self):
        """测试带提示词的图像分析"""
        # Given: 模拟模型
        mock_model = Mock(spec=GLM4VModel)
        mock_model.analyze_image.return_value = "图片中有一只猫"

        # When: 分析图像（带提示词）
        result = analyze_image(mock_model, "image.png", prompt="图片里有什么？")

        # Then: 结果正确
        assert result.description == "图片中有一只猫"
