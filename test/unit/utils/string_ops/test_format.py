# ============================================================================
# 文件: test/unit/utils/string_ops/test_format.py
# 描述: 测试 format 操作
#
# 测试对象: utils/string_ops/format.py
#
# Bash 快速定位:
#   find test -name "test_format.py" -path "*/utils/string_ops/*"
# ============================================================================

import pytest

from utils.string_ops.format import format_str


class TestFormat:
    """测试 format 操作"""

    def test_format_title_case(self):
        """测试标题格式化"""
        # Given: 小写字符串
        text = "hello world"

        # When: 格式化为标题
        result = format_str(text, style="title_case")

        # Then: 返回标题格式
        assert result == "Hello World"

    def test_format_snake_case(self):
        """测试蛇形格式化"""
        # Given: 驼峰字符串
        text = "HelloWorld"

        # When: 格式化为蛇形
        result = format_str(text, style="snake_case")

        # Then: 返回蛇形格式
        assert result == "hello_world"

    def test_format_kebab_case(self):
        """测试短横线格式化"""
        # Given: 驼峰字符串
        text = "HelloWorld"

        # When: 格式化为短横线
        result = format_str(text, style="kebab_case")

        # Then: 返回短横线格式
        assert result == "hello-world"

    def test_format_already_snake_case(self):
        """测试已经是蛇形的字符串"""
        # Given: 蛇形字符串
        text = "hello_world"

        # When: 格式化为蛇形
        result = format_str(text, style="snake_case")

        # Then: 返回原字符串
        assert result == "hello_world"
