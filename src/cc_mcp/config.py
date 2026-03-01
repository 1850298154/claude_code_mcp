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


__all__ = ["HOST", "PORT"]
