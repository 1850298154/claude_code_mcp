# ============================================================================
# 文件: src/academic/__init__.py
# 描述: Academic 模块初始化
#
# 上游依赖: 无
# 下游封装: mcp/tools/academic.py
#
# Bash 快速定位:
#   find . -name "__init__.py" -path "*/academic/*"
# ============================================================================

from .types import Paper, Citation, SearchOptions
from .scholar import Scholar

__all__ = ["Paper", "Citation", "SearchOptions", "Scholar"]
