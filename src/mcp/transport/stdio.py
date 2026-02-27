# ============================================================================
# 文件: src/mcp/transport/stdio.py
# 描述: Stdio 传输层
#
# 上游依赖: 无
# 下游封装: mcp/server.py, mcp/cli.py
#
# Bash 快速定位:
#   find . -name "stdio.py" -path "*/transport/*"
# ============================================================================

import sys
import asyncio
import json
from typing import Optional


class StdioTransport:
    """Stdio 传输层

    通过标准输入输出进行 MCP 通信。
    """

    def __init__(self):
        """初始化传输层"""
        self._loop: Optional[asyncio.AbstractEventLoop] = None

    async def read_line(self) -> str | None:
        """读取一行输入

        Returns:
            输入行，如果 EOF 则返回 None
        """
        loop = asyncio.get_event_loop()
        line = await loop.run_in_executor(None, sys.stdin.readline)
        if not line:
            return None
        return line.rstrip("\n")

    async def write_line(self, line: str):
        """写入一行输出

        Args:
            line: 要写入的内容
        """
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, lambda: print(line, file=sys.stdout, flush=True))
