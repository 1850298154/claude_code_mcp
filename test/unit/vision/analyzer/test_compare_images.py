# ============================================================================
# 文件: test/unit/vision/analyzer/test_compare_images.py
# 描述: 测试 compare_images 函数
#
# 测试对象: vision/analyzer/compare_images.py
#
# Bash 快速定位:
#   find test -name "test_compare_images.py"
# ============================================================================

import pytest
from pathlib import Path
from unittest.mock import Mock

from vision.models.glm4v import GLM4VModel
from vision.analyzer.compare_images import compare_images


class TestCompareImages:
    """测试 compare_images 函数"""

    def test_compare_images_similar(self):
        """测试比较相似图片"""
        # Given: 模拟模型返回相似结果
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = (
            "comparison: The images are very similar.\n"
            "difference_level: low"
        )

        # When: 比较图片
        result = compare_images(mock_model, "image1.jpg", "image2.jpg")

        # Then: 返回比较结果
        assert "similar" in result
        assert "low" in result

    def test_compare_images_different(self):
        """测试比较不同图片"""
        # Given: 模拟模型返回不同结果
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = (
            "comparison: The images show completely different scenes.\n"
            "difference_level: high"
        )

        # When: 比较图片
        result = compare_images(mock_model, "image1.jpg", "image2.jpg")

        # Then: 返回比较结果
        assert "different" in result
        assert "high" in result

    def test_compare_images_with_paths(self):
        """测试使用 Path 对象比较"""
        # Given: 模拟模型和 Path 对象
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = "comparison: Slight differences in lighting."

        # When: 使用 Path 对象比较
        result = compare_images(
            mock_model,
            Path("image1.jpg"),
            Path("image2.jpg")
        )

        # Then: 成功处理
        assert "lighting" in result
        mock_model.call.assert_called_once()
