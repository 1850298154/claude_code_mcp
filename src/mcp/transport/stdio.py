# ============================================================================
# 文件: src/mcp/transport/stdio.py
# 描述: Stdio 传输层
#
# 上游依赖: 无
# 下游封装: mcp/server/start.py
#
# Bash 快速定位:
#   find . -name "stdio.py" -path "*/transport/*"
# ============================================================================

import sys
import json
from typing import Dict, Any

from mcp.server import MCPServer


def start_stdio_server(server: MCPServer):
    """启动 Stdio MCP 服务器

    Args:
        server: MCP 服务器实例
    """
    while True:
        # 读取请求
        line = sys.stdin.readline()
        if not line:
            break

        request = json.loads(line)

        # 处理请求
        response = {"jsonrpc": "2.0", "id": request.get("id", "1"), "method": request.get("method")}

        if "params" in request:
            result = server.call_tool(request["method"], request["params"])
            response["result"] = result

        # 发送响应
        print(json.dumps(response), flush=sys.stdout)
