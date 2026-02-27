# ============================================================================
# 文件: src/mcp/tools/claude_meta_tools.py
# 描述: Claude Meta MCP 工具定义
#
# 上游依赖: claude_meta/reader/, claude_meta/analyzer/
# 下游封装: mcp/server.py
#
# Bash 快速定位:
#   find src -name "claude_meta_tools.py" -path "*/mcp/tools/*"
# ============================================================================

"""Claude Meta MCP 工具"""

from mcp.types import Tool, TextContent
from typing import Any


CLAUDE_META_TOOLS: list[Tool] = [
    Tool(
        name="get_sessions",
        description="获取 Claude Code 所有会话列表",
        inputSchema={
            "type": "object",
            "properties": {},
        },
    ),
    Tool(
        name="get_chat_history",
        description="获取指定会话的聊天历史",
        inputSchema={
            "type": "object",
            "properties": {
                "session_id": {
                    "type": "string",
                    "description": "会话 ID",
                },
            },
            "required": ["session_id"],
        },
    ),
    Tool(
        name="get_memory",
        description="获取 Claude Code 记忆内容",
        inputSchema={
            "type": "object",
            "properties": {},
        },
    ),
    Tool(
        name="restore_session",
        description="恢复指定会话",
        inputSchema={
            "type": "object",
            "properties": {
                "session_id": {
                    "type": "string",
                    "description": "会话 ID",
                },
            },
            "required": ["session_id"],
        },
    ),
    Tool(
        name="get_project_context",
        description="获取项目上下文信息",
        inputSchema={
            "type": "object",
            "properties": {
                "project_name": {
                    "type": "string",
                    "description": "项目名称",
                },
            },
        },
    ),
]


__all__ = ["CLAUDE_META_TOOLS"]
