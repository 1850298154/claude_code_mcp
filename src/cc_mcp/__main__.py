# ============================================================================
# 文件: src/cc_mcp/__main__.py
# 描述: MCP 模块主入口
#
# 上游依赖: cc_mcp/cli.py
# 下游封装: 无
#
# Bash 快速定位:
#   find src -name "__main__.py" -path "*/cc_mcp/*"
# ============================================================================

"""MCP 模块主入口

通过 `python -m cc_mcp` 启动 MCP 服务器。
"""

from cc_mcp.cli import main
import asyncio

if __name__ == "__main__":
    asyncio.run(main())
