# ============================================================================
# 文件: src/utils/string_ops/format.py
# 描述: 格式化字符串函数
#
# 上游依赖: 无
# 下游封装: utils/string_ops.py (StringOps.format)
#
# Bash 快速定位:
#   find . -name "format.py" -path "*/string_ops/*"
# ============================================================================


def format_str(template: str, **kwargs) -> str:
    """格式化字符串

    Args:
        template: 格式模板
        **kwargs: 格式参数

    Returns:
        格式化后的字符串
    """
    return template.format(**kwargs)
