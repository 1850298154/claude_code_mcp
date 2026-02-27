# ============================================================================
# 文件: test/unit/utils/string_ops/test_truncate.py
# 描述: 测试 truncate 操作
#
# 测试对象: utils/string_ops/truncate.py
#
# Bash 快速定位:
#   find test -name "test_truncate.py" -path "*/utils/string_ops/*"
# ============================================================================

import pytest

from utils.string_ops.truncate import truncate


class TestTruncate:
    """测试 truncate 操作"""

    def test_truncate_short_string(self):
        """测试截断短字符串"""
        # Given: 短字符串
        text = "Hello"

        # When: 截断（不需要截断）
        result = truncate(text, max_length=20)

        # Then: 返回原字符串
        assert result == "Hello"

    def test_truncate_long_string(self):
        """测试截断长字符串"""
        # Given: 长字符串
        text = "This is a very long string that needs truncation"

        # When: 截断
        result = truncate(text, max_length=20)

        # Then: 返回截断后的字符串
        assert len(result) <= 23  # 20 + "..."
        assert "..." in result

    def test_truncate_custom_ellipsis(self):
        """测试自定义省略号"""
        # Given: 长字符串
        text = "This is a very long string"

        # When: 使用自定义省略号截断
        result = truncate(text, max_length=10, ellipsis="***")

        # Then: 使用自定义省略号
        assert "***" in result
        assert len(result) <= 13  # 10 + "***"

    def test_truncate_exact_length(self):
        """测试精确长度截断"""
        # Given: 刚好等于最大长度的字符串
        text = "HelloWorld"

        # When: 截断
        result = truncate(text, max_length=10)

        # Then: 不需要截断
        assert result == "HelloWorld"
