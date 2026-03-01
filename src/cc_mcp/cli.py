# ============================================================================
# 文件: src/cc_mcp/cli.py
# 描述: MCP 服务器 CLI 入口
#
# 上游依赖: cc_mcp/server.py, cc_mcp/transport/stdio.py
# 下游封装: 无（作为 CLI 入口）
#
# Bash 快速定位:
#   find src -name "cli.py" -path "*/cc_mcp/*"
# ============================================================================

"""MCP 服务器 CLI 入口

提供命令行接口启动 MCP 服务器。
"""

import asyncio
import sys

from cc_mcp.server import MCPServer
from cc_mcp.transport.stdio import StdioTransport


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
        print("\nServer stopped by user.", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"Server error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
