# ============================================================================
# 文件: test/unit/vision/test_analyzer.py
# 描述: 测试 VisionAnalyzer 类
#
# 测试对象: vision/analyzer.py
#
# Bash 快速定位:
#   find test -name "test_analyzer.py" -path "*/vision/*"
# ============================================================================

import pytest
from unittest.mock import Mock

from vision.analyzer import VisionAnalyzer
from vision.models.glm4v import GLM4VModel
from vision.types import ModelType, ModelConfig


class TestVisionAnalyzer:
    """测试 VisionAnalyzer 类"""

    def test_vision_analyzer_init(self):
        """测试 VisionAnalyzer 初始化"""
        # Given: 配置
        config = ModelConfig(model_type=ModelType.GLM4V, api_key=None)

        # When: 创建 VisionAnalyzer
        analyzer = VisionAnalyzer(config)

        # Then: 初始化成功
        assert analyzer is not None

    def test_vision_analyzer_analyze_image_delegates(self):
        """测试 analyze_image 委托"""
        # Given: VisionAnalyzer 和 mock 模型
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = "description: A beautiful scene"

        config = ModelConfig(model_type=ModelType.GLM4V, api_key=None)
        analyzer = VisionAnalyzer(config)
        analyzer._model = mock_model

        # When: 分析图像
        result = analyzer.analyze_image("test.jpg", "What is this?")

        # Then: 正确调用模型
        mock_model.call.assert_called_once()

    def test_vision_analyzer_detect_objects_delegates(self):
        """测试 detect_objects 委托"""
        # Given: VisionAnalyzer 和 mock 模型
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = "detected_objects: ['car', 'person']"

        config = ModelConfig(model_type=ModelType.GLM4V, api_key=None)
        analyzer = VisionAnalyzer(config)
        analyzer._model = mock_model

        # When: 检测对象
        objects = analyzer.detect_objects("test.jpg")

        # Then: 正确调用模型
        mock_model.call.assert_called_once()
        assert len(objects) > 0

    def test_vision_analyzer_extract_text_delegates(self):
        """测试 extract_text 委托"""
        # Given: VisionAnalyzer 和 mock 模型
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = "extracted_text: Hello World"

        config = ModelConfig(model_type=ModelType.GLM4V, api_key=None)
        analyzer = VisionAnalyzer(config)
        analyzer._model = mock_model

        # When: 提取文本
        text = analyzer.extract_text("test.jpg")

        # Then: 正确调用模型
        mock_model.call.assert_called_once()
        assert "Hello World" in text
