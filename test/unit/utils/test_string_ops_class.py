# ============================================================================
# 文件: test/unit/utils/test_string_ops_class.py
# 描述: 测试 StringOps 类
#
# 测试对象: utils/string_ops.py
#
# Bash 快速定位:
#   find test -name "test_string_ops_class.py"
# ============================================================================

import pytest

from utils.string_ops import StringOps


class TestStringOpsClass:
    """测试 StringOps 类"""

    def test_string_ops_truncate_static(self):
        """测试 StringOps.truncate 静态方法"""
        # Given: 长字符串
        text = "This is a very long string"

        # When: 使用静态方法截断
        result = StringOps.truncate(text, max_length=10)

        # Then: 返回截断后的字符串
        assert len(result) <= 13  # 10 + "..."

    def test_string_ops_escape_static(self):
        """测试 StringOps.escape 静态方法"""
        # Given: 包含特殊字符的字符串
        text = '<script>alert("xss")</script>'

        # When: 使用静态方法转义
        result = StringOps.escape(text, mode="html")

        # Then: 特殊字符被转义
        assert "&lt;" in result
        assert "&gt;" in result

    def test_string_ops_format_static(self):
        """测试 StringOps.format 静态方法"""
        # Given: 驼峰字符串
        text = "HelloWorld"

        # When: 使用静态方法格式化
        result = StringOps.format(text, style="snake_case")

        # Then: 返回蛇形格式
        assert result == "hello_world"

    def test_string_ops_format_title_case(self):
        """测试标题格式化"""
        # Given: 小写字符串
        text = "hello world"

        # When: 格式化为标题
        result = StringOps.format(text, style="title_case")

        # Then: 返回标题格式
        assert result == "Hello World"

    def test_string_ops_format_kebab_case(self):
        """测试短横线格式化"""
        # Given: 驼峰字符串
        text = "HelloWorld"

        # When: 格式化为短横线
        result = StringOps.format(text, style="kebab_case")

        # Then: 返回短横线格式
        assert result == "hello-world"
