# ============================================================================
# 文件: src/cc_mcp/tools/__init__.py
# 描述: MCP 工具定义模块初始化
#
# 上游依赖: claude_meta/, academic/, vision/, graphrag/, utils/
# 下游封装: cc_mcp/server.py
#
# Bash 快速定位:
#   find src -name "__init__.py" -path "*/cc_mcp/tools/*"
# ============================================================================

"""MCP 工具定义

为各个模块定义 MCP 工具。
"""

from mcp.types import Tool

from cc_mcp.tools.claude_meta_tools import CLAUDE_META_TOOLS
from cc_mcp.tools.academic_tools import ACADEMIC_TOOLS
from cc_mcp.tools.vision_tools import VISION_TOOLS
from cc_mcp.tools.graphrag_tools import GRAPH_RAG_TOOLS
from cc_mcp.tools.utils_tools import UTILS_TOOLS
from cc_mcp.tools.audio_tools import AUDIO_TOOLS


def get_all_tools() -> list[Tool]:
    """获取所有 MCP 工具"""
    return [
        *CLAUDE_META_TOOLS,
        *ACADEMIC_TOOLS,
        *VISION_TOOLS,
        *GRAPH_RAG_TOOLS,
        *UTILS_TOOLS,
        *AUDIO_TOOLS,
    ]


__all__ = [
    "CLAUDE_META_TOOLS",
    "ACADEMIC_TOOLS",
    "VISION_TOOLS",
    "GRAPH_RAG_TOOLS",
    "UTILS_TOOLS",
    "AUDIO_TOOLS",
    "get_all_tools",
]
