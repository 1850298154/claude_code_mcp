# ============================================================================
# 文件: test/unit/vision/analyzer/test_describe_scene.py
# 描述: 测试 describe_scene 函数
#
# 测试对象: vision/analyzer/describe_scene.py
#
# Bash 快速定位:
#   find test -name "test_describe_scene.py"
# ============================================================================

import pytest
from pathlib import Path
from unittest.mock import Mock

from vision.models.glm4v import GLM4VModel
from vision.analyzer.describe_scene import describe_scene


class TestDescribeScene:
    """测试 describe_scene 函数"""

    def test_describe_scene_success(self):
        """测试成功描述场景"""
        # Given: 模拟模型返回场景描述
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = (
            "scene_description: A sunny beach with palm trees\n"
            "and blue ocean water."
        )

        # When: 描述场景
        description = describe_scene(mock_model, "test.jpg")

        # Then: 返回正确描述
        assert "sunny beach" in description
        assert "palm trees" in description

    def test_describe_scene_with_details(self):
        """测试详细场景描述"""
        # Given: 模拟模型返回详细描述
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = (
            "scene_description: A modern office space\n"
            "with multiple desks, computers, and large windows\n"
            "letting in natural light."
        )

        # When: 描述场景
        description = describe_scene(mock_model, "test.jpg")

        # Then: 返回完整描述
        assert "modern office" in description
        assert "computers" in description
        assert "windows" in description

    def test_describe_scene_empty(self):
        """测试无场景描述"""
        # Given: 模拟模型返回空结果
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = "Unable to describe scene."

        # When: 描述场景
        description = describe_scene(mock_model, "test.jpg")

        # Then: 返回空字符串
        assert description == ""
