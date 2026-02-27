# ============================================================================
# 文件: test/unit/vision/analyzer/test_detect_objects.py
# 描述: 测试 detect_objects 函数
#
# 测试对象: vision/analyzer/detect_objects.py
#
# Bash 快速定位:
#   find test -name "test_detect_objects.py"
# ============================================================================

import pytest
from pathlib import Path
from unittest.mock import Mock, patch

from vision.types import DetectedObject
from vision.models.glm4v import GLM4VModel
from vision.analyzer.detect_objects import detect_objects


class TestDetectObjects:
    """测试 detect_objects 函数"""

    def test_detect_objects_success(self):
        """测试成功检测对象"""
        # Given: 模拟模型返回检测结果
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = (
            "detected_objects: ['person', 'car', 'building']\n"
            "count: 3"
        )

        # When: 检测对象
        objects = detect_objects(mock_model, "test.jpg")

        # Then: 返回正确对象列表
        assert len(objects) == 3
        assert all(isinstance(o, DetectedObject) for o in objects)
        mock_model.call.assert_called_once()

    def test_detect_objects_empty(self):
        """测试无对象检测"""
        # Given: 模拟模型返回空结果
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = "No objects detected."

        # When: 检测对象
        objects = detect_objects(mock_model, "test.jpg")

        # Then: 返回空列表
        assert objects == []

    def test_detect_objects_with_file_path(self):
        """测试使用 Path 对象"""
        # Given: 模拟模型和 Path
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = "Object: table"

        # When: 使用 Path 对象
        objects = detect_objects(mock_model, Path("test.jpg"))

        # Then: 成功处理
        assert len(objects) == 1
