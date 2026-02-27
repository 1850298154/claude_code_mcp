# ============================================================================
# 文件: src/utils/string_ops.py
# 描述: StringOps 类定义，用于字符串操作
#
# 上游依赖: 无
# 下游封装: string_ops/*
#
# Bash 快速定位:
#   find . -name "string_ops.py" -path "*/utils/*"
# ============================================================================

from typing import List


class StringOps:
    """String Operations - 字符串操作工具

    提供常用的字符串处理功能。
    """

    def truncate(self, text: str, max_len: int) -> str:
        """截断字符串

        实现位置: string_ops/truncate.py

        Args:
            text: 输入字符串
            max_len: 最大长度

        Returns:
            截断后的字符串
        """
        if len(text) <= max_len:
            return text
        return text[:max_len] + "..."

    def escape(self, text: str) -> str:
        """转义字符串

        实现位置: string_ops/escape.py

        Args:
            text: 输入字符串

        Returns:
            转义后的字符串
        """
        # 简单的 HTML 转义
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
        return text

    def format(self, template: str, **kwargs) -> str:
        """格式化字符串

        实现位置: string_ops/format.py

        Args:
            template: 格式模板
            **kwargs: 格式参数

        Returns:
            格式化后的字符串
        """
        return template.format(**kwargs)
