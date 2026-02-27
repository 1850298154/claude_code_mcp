# ============================================================================
# 文件: src/mcp/transport/__init__.py
# 描述: Transport 模块初始化
#
# 上游依赖: 无
# 下游封装: mcp/server/start.py
#
# Bash 快速定位:
#   find . -name "__init__.py" -path "*/transport/*"
# ============================================================================

from .stdio import start_stdio_server

__all__ = ["start_stdio_server"]
