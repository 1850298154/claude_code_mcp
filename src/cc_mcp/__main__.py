# ============================================================================
# 文件: src/cc_mcp/__main__.py
# 描述: cc_mcp 模块入口
# ============================================================================

"""cc_mcp 模块命令行入口

运行: python -m cc_mcp
"""

from .server_fastmcp import mcp

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
