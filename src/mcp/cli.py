# ============================================================================
# 文件: src/mcp/cli.py
# 描述: MCP 服务器 CLI 入口
#
# 上游依赖: mcp/server.py, mcp/transport/stdio.py
# 下游封装: 无（作为 CLI 入口）
#
# Bash 快速定位:
#   find src -name "cli.py" -path "*/mcp/*"
# ============================================================================

"""MCP 服务器 CLI 入口

提供命令行接口启动 MCP 服务器。
"""

import asyncio
import sys

from mcp.server import MCPServer
from mcp.transport.stdio import StdioTransport


async def main():
    """主函数"""
    # 创建 MCP 服务器
    server = MCPServer()

    # 创建 stdio 传输层
    transport = StdioTransport()

    # 启动服务器
    try:
        await server.serve(transport)
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
