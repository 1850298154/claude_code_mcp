# ============================================================================
# 文件: src/cc_mcp/tools/audio_tools.py
# 描述: Audio MCP 工具定义
#
# 上游依赖: audio/speaker/
# 下游封装: cc_mcp/server.py
#
# Bash 快速定位:
#   find src -name "audio_tools.py" -path "*/cc_mcp/tools/*"
# ============================================================================

"""Audio MCP 工具"""

from mcp.types import Tool


AUDIO_TOOLS: list[Tool] = [
    Tool(
        name="speak",
        description="播放语音播报（文本转语音）",
        inputSchema={
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "要播放的文本内容",
                },
                "async": {
                    "type": "boolean",
                    "description": "是否异步播放（默认为 false）",
                },
            },
            "required": ["text"],
        },
    ),
]


__all__ = ["AUDIO_TOOLS"]
