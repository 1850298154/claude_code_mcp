# ============================================================================
# 文件: src/cc_mcp/__init__.py
# 描述: MCP 模块初始化
#
# 上游依赖: 无
# 下游封装: 无
#
# Bash 快速定位:
#   find . -name "__init__.py" -path "*/cc_mcp/*"
# ============================================================================

from .server import MCPServer
from .transport.stdio import start_stdio_server

__all__ = ["MCPServer", "start_stdio_server"]
