# ============================================================================
# 文件: test/unit/utils/test_string_ops.py
# 描述: 测试 StringOps 类
#
# 测试对象: utils/string_ops.py
#
# Bash 快速定位:
#   find test -name "test_string_ops.py"
# ============================================================================

import pytest

from utils.string_ops import StringOps


class TestStringOps:
    """测试 StringOps 类"""

    def test_truncate_short_string(self):
        """测试截断短字符串"""
        # Given: 短字符串
        text = "Hello"

        # When: 截断（不需要截断）
        result = StringOps.truncate(text, max_length=20)

        # Then: 返回原字符串
        assert result == "Hello"

    def test_truncate_long_string(self):
        """测试截断长字符串"""
        # Given: 长字符串
        text = "This is a very long string that needs to be truncated"

        # When: 截断
        result = StringOps.truncate(text, max_length=20)

        # Then: 返回截断后的字符串
        assert len(result) <= 23  # 20 + "..."

    def test_truncate_with_ellipsis(self):
        """测试截断添加省略号"""
        # Given: 长字符串
        text = "This is a very long string"

        # When: 截断
        result = StringOps.truncate(text, max_length=10, ellipsis="...")

        # Then: 返回带省略号的字符串
        assert len(result) <= 13  # 10 + "..."
        assert result.endswith("...")

    def test_escape_html(self):
        """测试 HTML 转义"""
        # Given: 包含 HTML 特殊字符的字符串
        text = "<script>alert('xss')</script>"

        # When: 转义
        result = StringOps.escape(text, mode="html")

        # Then: 特殊字符被转义
        assert "&lt;" in result
        assert "&gt;" in result
        assert "<script>" not in result

    def test_escape_json(self):
        """测试 JSON 转义"""
        # Given: 包含 JSON 特殊字符的字符串
        text = 'He said "Hello"'

        # When: 转义
        result = StringOps.escape(text, mode="json")

        # Then: 引号被转义
        assert '\\"' in result

    def test_format_title_case(self):
        """测试标题格式化"""
        # Given: 小写字符串
        text = "hello world"

        # When: 格式化为标题
        result = StringOps.format(text, style="title_case")

        # Then: 返回标题格式
        assert result == "Hello World"

    def test_format_snake_case(self):
        """测试蛇形格式化"""
        # Given: 驼峰字符串
        text = "HelloWorld"

        # When: 格式化为蛇形
        result = StringOps.format(text, style="snake_case")

        # Then: 返回蛇形格式
        assert result == "hello_world"

    def test_format_kebab_case(self):
        """测试短横线格式化"""
        # Given: 驼峰字符串
        text = "HelloWorld"

        # When: 格式化为短横线
        result = StringOps.format(text, style="kebab_case")

        # Then: 返回短横线格式
        assert result == "hello-world"
