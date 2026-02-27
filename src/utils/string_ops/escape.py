# ============================================================================
# 文件: src/utils/string_ops/escape.py
# 描述: 转义字符串函数
#
# 上游依赖: 无
# 下游封装: utils/string_ops.py (StringOps.escape)
#
# Bash 快速定位:
#   find . -name "escape.py" -path "*/string_ops/*"
# ============================================================================


def escape(text: str) -> str:
    """转义字符串

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
