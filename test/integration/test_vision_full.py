# ============================================================================
# 文件: test/integration/test_vision_full.py
# 描述: Vision 模块完整集成测试
#
# 测试对象: vision/ 整个模块
#
# Bash 快速定位:
#   find test -name "test_vision_full.py"
# ============================================================================

import pytest
from pathlib import Path
from unittest.mock import Mock, patch

from vision.analyzer import VisionAnalyzer
from vision.models.glm4v import GLM4VModel
from vision.types import ModelType, ModelConfig


class TestVisionFull:
    """测试 Vision 模块完整集成"""

    def test_vision_analyzer_full_workflow(self):
        """测试 VisionAnalyzer 完整工作流"""
        # Given: 配置和模拟模型
        config = ModelConfig(
            model_type=ModelType.GLM4V,
            api_key="test-key"
        )
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = "description: A beautiful landscape"

        with patch('vision.models.glm4v.GLM4VModel', return_value=mock_model):
            # When: 创建 VisionAnalyzer 并分析图像
            analyzer = VisionAnalyzer(config)
            result = analyzer.analyze_image("test.jpg", "What is in this image?")

            # Then: 返回分析结果
            assert "landscape" in result

    def test_vision_analyzer_detect_objects_workflow(self):
        """测试对象检测工作流"""
        # Given: 配置和模拟模型
        config = ModelConfig(model_type=ModelType.GLM4V)
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = (
            "detected_objects: ['car', 'person', 'road']\n"
            "count: 3"
        )

        with patch('vision.models.glm4v.GLM4VModel', return_value=mock_model):
            # When: 创建 VisionAnalyzer 并检测对象
            analyzer = VisionAnalyzer(config)
            objects = analyzer.detect_objects("test.jpg")

            # Then: 返回检测到的对象
            assert len(objects) == 3

    def test_vision_analyzer_ocr_workflow(self):
        """测试 OCR 工作流"""
        # Given: 配置和模拟模型
        config = ModelConfig(model_type=ModelType.GLM4V)
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = (
            "extracted_text: Hello World\n"
            "This is a test document."
        )

        with patch('vision.models.glm4v.GLM4VModel', return_value=mock_model):
            # When: 创建 VisionAnalyzer 并提取文本
            analyzer = VisionAnalyzer(config)
            text = analyzer.extract_text("test.jpg")

            # Then: 返回提取的文本
            assert "Hello World" in text

    def test_vision_analyzer_compare_workflow(self):
        """测试图片比较工作流"""
        # Given: 配置和模拟模型
        config = ModelConfig(model_type=ModelType.GLM4V)
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = (
            "comparison: The images are similar.\n"
            "difference_level: low"
        )

        with patch('vision.models.glm4v.GLM4VModel', return_value=mock_model):
            # When: 创建 VisionAnalyzer 并比较图片
            analyzer = VisionAnalyzer(config)
            result = analyzer.compare_images("image1.jpg", "image2.jpg")

            # Then: 返回比较结果
            assert "similar" in result

    def test_vision_analyzer_with_path(self):
        """测试使用 Path 对象"""
        # Given: 配置和模拟模型
        config = ModelConfig(model_type=ModelType.GLM4V)
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = "description: Test image"

        with patch('vision.models.glm4v.GLM4VModel', return_value=mock_model):
            # When: 使用 Path 对象分析
            analyzer = VisionAnalyzer(config)
            result = analyzer.analyze_image(Path("test.jpg"))

            # Then: 成功处理
            assert "Test" in result
