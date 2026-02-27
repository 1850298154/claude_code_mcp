# ============================================================================
# 文件: src/mcp/tools/utils_tools.py
# 描述: Utils MCP 工具定义
#
# 上游依赖: utils/file_ops/, utils/string_ops/, utils/json_ops/
# 下游封装: mcp/server.py
#
# Bash 快速定位:
#   find src -name "utils_tools.py" -path "*/mcp/tools/*"
# ============================================================================

"""Utils MCP 工具"""

from mcp.types import Tool


UTILS_TOOLS: list[Tool] = [
    Tool(
        name="file_read",
        description="读取文件内容",
        inputSchema={
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "文件路径",
                },
            },
            "required": ["file_path"],
        },
    ),
    Tool(
        name="file_write",
        description="写入文件内容",
        inputSchema={
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "文件路径",
                },
                "content": {
                    "type": "string",
                    "description": "文件内容",
                },
            },
            "required": ["file_path", "content"],
        },
    ),
    Tool(
        name="file_list_dir",
        description="列出目录内容",
        inputSchema={
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "目录路径",
                },
                "recursive": {
                    "type": "boolean",
                    "description": "是否递归列出",
                    "default": False,
                },
            },
            "required": ["directory"],
        },
    ),
    Tool(
        name="file_find",
        description="查找文件",
        inputSchema={
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "搜索目录",
                },
                "pattern": {
                    "type": "string",
                    "description": "文件名模式（如 *.py）",
                },
                "recursive": {
                    "type": "boolean",
                    "description": "是否递归搜索",
                    "default": True,
                },
            },
            "required": ["directory", "pattern"],
        },
    ),
    Tool(
        name="string_truncate",
        description="截断字符串",
        inputSchema={
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "原始文本",
                },
                "max_length": {
                    "type": "integer",
                    "description": "最大长度",
                },
                "ellipsis": {
                    "type": "string",
                    "description": "省略号符号",
                    "default": "...",
                },
            },
            "required": ["text", "max_length"],
        },
    ),
    Tool(
        name="string_format",
        description="格式化字符串",
        inputSchema={
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "原始文本",
                },
                "style": {
                    "type": "string",
                    "description": "格式化风格（snake_case, kebab_case, title_case）",
                },
            },
            "required": ["text", "style"],
        },
    ),
    Tool(
        name="json_read",
        description="读取 JSON 文件",
        inputSchema={
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "JSON 文件路径",
                },
            },
            "required": ["file_path"],
        },
    ),
    Tool(
        name="json_write",
        description="写入 JSON 文件",
        inputSchema={
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "JSON 文件路径",
                },
                "data": {
                    "type": "string",
                    "description": "JSON 数据字符串",
                },
            },
            "required": ["file_path", "data"],
        },
    ),
]


__all__ = ["UTILS_TOOLS"]
