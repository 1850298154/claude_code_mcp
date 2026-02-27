# ============================================================================
# 文件: test/unit/vision/analyzer/test_extract_text.py
# 描述: 测试 extract_text 函数
#
# 测试对象: vision/analyzer/extract_text.py
#
# Bash 快速定位:
#   find test -name "test_extract_text.py"
# ============================================================================

import pytest
from pathlib import Path
from unittest.mock import Mock

from vision.models.glm4v import GLM4VModel
from vision.analyzer.extract_text import extract_text


class TestExtractText:
    """测试 extract_text 函数"""

    def test_extract_text_success(self):
        """测试成功提取文本"""
        # Given: 模拟模型返回文本
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = (
            "extracted_text: Hello World\n"
            "This is a test document."
        )

        # When: 提取文本
        text = extract_text(mock_model, "test.jpg")

        # Then: 返回正确文本
        assert "Hello World" in text
        assert "test document" in text

    def test_extract_text_empty(self):
        """测试无文本提取"""
        # Given: 模拟模型返回空文本
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = "No text detected."

        # When: 提取文本
        text = extract_text(mock_model, "test.jpg")

        # Then: 返回空字符串
        assert text == ""

    def test_extract_text_multiline(self):
        """测试多行文本提取"""
        # Given: 模拟模型返回多行文本
        mock_model = Mock(spec=GLM4VModel)
        mock_model.call.return_value = (
            "extracted_text:\n"
            "Line 1\n"
            "Line 2\n"
            "Line 3"
        )

        # When: 提取文本
        text = extract_text(mock_model, "test.jpg")

        # Then: 返回完整文本
        assert "Line 1" in text
        assert "Line 2" in text
        assert "Line 3" in text
