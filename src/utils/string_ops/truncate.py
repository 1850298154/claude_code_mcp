# ============================================================================
# 文件: src/utils/string_ops/truncate.py
# 描述: 截断字符串函数
#
# 上游依赖: 无
# 下游封装: utils/string_ops.py (StringOps.truncate)
#
# Bash 快速定位:
#   find . -name "truncate.py" -path "*/string_ops/*"
# ============================================================================


def truncate(text: str, max_len: int) -> str:
    """截断字符串

    Args:
        text: 输入字符串
        max_len: 最大长度

    Returns:
        截断后的字符串
    """
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."
