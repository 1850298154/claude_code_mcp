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

支持三种传输模式：
- stdio: 标准输入输出（每次请求启动新进程）
- websocket: WebSocket 持久连接（服务器持续运行，支持状态共享）
- http: HTTP RESTful API（通过 HTTP 调用 MCP）
"""

import asyncio
import sys
import argparse

from cc_mcp.server import MCPServer
from cc_mcp.transport.stdio import StdioTransport
from cc_mcp.transport.websocket import WebSocketTransport
from cc_mcp.transport.http import HTTPTransport


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description="Claude Code MCP Server - 开发工具集",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "--transport", "-t",
        choices=["stdio", "websocket", "http"],
        default="stdio",
        help="传输模式: stdio (每次启动), websocket (持久连接), 或 http (REST API)"
    )

    parser.add_argument(
        "--host", "-H",
        default="127.0.0.1",
        help="监听地址 (仅 websocket/http 模式)"
    )

    parser.add_argument(
        "--port", "-p",
        type=int,
        default=None,
        help="监听端口 (仅 websocket/http 模式，默认: websocket=8765, http=8000)"
    )

    return parser.parse_args()


async def main():
    """主函数"""
    args = parse_args()

    # 创建 MCP 服务器
    server = MCPServer()

    # 根据传输模式创建传输层
    if args.transport == "websocket":
        port = args.port or 8765
        transport = WebSocketTransport(args.host, port)
        print(f"[WebSocket] Starting server on ws://{args.host}:{port}", file=sys.stderr)
        print(f"[WebSocket] Server will keep running, state is preserved", file=sys.stderr)
    elif args.transport == "http":
        port = args.port or 8000
        transport = HTTPTransport(args.host, port)
        print(f"[HTTP] Starting server on http://{args.host}:{port}/mcp", file=sys.stderr)
        print(f"[HTTP] Health check: http://{args.host}:{port}/health", file=sys.stderr)
        print(f"[HTTP] Server will keep running, state is preserved", file=sys.stderr)
    else:  # stdio
        transport = StdioTransport()
        print("[Stdio] Server in stdio mode", file=sys.stderr)
        print("[Stdio] Each request starts a new process", file=sys.stderr)

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
