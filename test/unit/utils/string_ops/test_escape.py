# ============================================================================
# 文件: test/unit/utils/string_ops/test_escape.py
# 描述: 测试 escape 操作
#
# 测试对象: utils/string_ops/escape.py
#
# Bash 快速定位:
#   find test -name "test_escape.py" -path "*/utils/string_ops/*"
# ============================================================================

import pytest

from utils.string_ops.escape import escape


class TestEscape:
    """测试 escape 操作"""

    def test_escape_html(self):
        """测试 HTML 转义"""
        # Given: 包含 HTML 特殊字符的字符串
        text = '<script>alert("xss")</script>'

        # When: HTML 转义
        result = escape(text, mode="html")

        # Then: 特殊字符被转义
        assert "&lt;" in result
        assert "&gt;" in result
        assert "<script>" not in result
        assert "</script>" not in result

    def test_escape_json(self):
        """测试 JSON 转义"""
        # Given: 包含 JSON 特殊字符的字符串
        text = 'He said "Hello"'

        # When: JSON 转义
        result = escape(text, mode="json")

        # Then: 引号被转义
        assert '\\"' in result
        assert result == 'He said \\"Hello\\"'

    def test_escape_no_special_chars(self):
        """测试无特殊字符转义"""
        # Given: 普通字符串
        text = "Hello World"

        # When: HTML 转义
        result = escape(text, mode="html")

        # Then: 返回原字符串
        assert result == "Hello World"
