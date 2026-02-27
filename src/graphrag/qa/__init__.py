# ============================================================================
# 文件: src/graphrag/qa/__init__.py
# 描述: QA 模块初始化
#
# 上游依赖: graphrag/types.py
# 下游封装: mcp/tools/graphrag.py
#
# Bash 快速定位:
#   find . -name "__init__.py" -path "*/qa/*"
# ============================================================================

from .qa_system import QASystem

__all__ = ["QASystem"]
