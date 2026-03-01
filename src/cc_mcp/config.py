# ============================================================================
# 文件: src/cc_mcp/config.py
# 描述: MCP 服务器配置
# ============================================================================

"""MCP 服务器配置

从环境变量或默认值加载配置。
"""

import os
from dotenv import load_dotenv

load_dotenv()


HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))


# 模块启用/禁用配置 (默认全部启用)
ENABLE_CLAUDE_META = _parse_bool(os.getenv("ENABLE_CLAUDE_META", "true"))
ENABLE_ACADEMIC = _parse_bool(os.getenv("ENABLE_ACADEMIC", "true"))
ENABLE_VISION = _parse_bool(os.getenv("ENABLE_VISION", "false"))  # 默认关闭
ENABLE_GRAPHRAG = _parse_bool(os.getenv("ENABLE_GRAPHRAG", "false"))  # 默认关闭
ENABLE_UTILS = _parse_bool(os.getenv("ENABLE_UTILS", "true"))
ENABLE_AUDIO = _parse_bool(os.getenv("ENABLE_AUDIO", "false"))  # 默认关闭


def _parse_bool(value: str) -> bool:
    """解析布尔值"""
    return value.lower() in ("true", "1", "yes", "on")


__all__ = [
    "HOST", "PORT",
    "ENABLE_CLAUDE_META",
    "ENABLE_ACADEMIC",
    "ENABLE_VISION",
    "ENABLE_GRAPHRAG",
    "ENABLE_UTILS",
    "ENABLE_AUDIO",
]
