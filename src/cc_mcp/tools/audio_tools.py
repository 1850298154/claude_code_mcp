# ============================================================================
# 文件: src/cc_mcp/tools/audio_tools.py
# 描述: Audio MCP 工具定义
#
# 上游依赖: audio/speaker/, audio/listener/
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
    Tool(
        name="listen_once",
        description="单次录音并识别（语音转文字）",
        inputSchema={
            "type": "object",
            "properties": {
                "timeout": {
                    "type": "number",
                    "description": "等待语音开始的超时时间（秒），默认 5",
                },
                "phrase_time_limit": {
                    "type": "number",
                    "description": "单次录音的最长时间（秒），默认 10",
                },
            },
            "required": [],
        },
    ),
]


__all__ = ["AUDIO_TOOLS"]
