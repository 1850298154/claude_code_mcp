# ============================================================================
# 文件: src/mcp/tools/academic_tools.py
# 描述: Academic MCP 工具定义
#
# 上游依赖: academic/scholar/
# 下游封装: mcp/server.py
#
# Bash 快速定位:
#   find src -name "academic_tools.py" -path "*/mcp/tools/*"
# ============================================================================

"""Academic MCP 工具"""

from mcp.types import Tool
from typing import Any


ACADEMIC_TOOLS: list[Tool] = [
    Tool(
        name="search_papers",
        description="搜索学术论文",
        inputSchema={
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "搜索查询",
                },
                "limit": {
                    "type": "integer",
                    "description": "返回结果数量限制",
                    "default": 10,
                },
                "year": {
                    "type": "integer",
                    "description": "年份筛选",
                },
            },
            "required": ["query"],
        },
    ),
    Tool(
        name="get_bibtex",
        description="获取论文的 BibTeX 引用",
        inputSchema={
            "type": "object",
            "properties": {
                "paper_id": {
                    "type": "string",
                    "description": "论文 ID",
                },
            },
            "required": ["paper_id"],
        },
    ),
    Tool(
        name="get_abstract",
        description="获取论文摘要",
        inputSchema={
            "type": "object",
            "properties": {
                "paper_id": {
                    "type": "string",
                    "description": "论文 ID",
                },
            },
            "required": ["paper_id"],
        },
    ),
    Tool(
        name="verify_citations",
        description="验证 BibTeX 引用",
        inputSchema={
            "type": "object",
            "properties": {
                "bibtex": {
                    "type": "string",
                    "description": "BibTeX 内容",
                },
            },
            "required": ["bibtex"],
        },
    ),
]


__all__ = ["ACADEMIC_TOOLS"]
