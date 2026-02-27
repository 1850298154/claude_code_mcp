# ============================================================================
# 文件: __init__.py
# 描述: Claude Code MCP Toolkit 包初始化
#
# 上游依赖:
#   - 无
#
# 下游封装:
#   - core/          (核心基础设施)
#   - claude_meta/   (Claude 元信息读取)
#   - academic/      (学术搜索)
#   - vision/        (视觉分析)
#   - graphrag/      (知识图谱)
#   - mcp/           (MCP 服务器)
#   - utils/         (通用工具)
#
# Bash 快速定位:
#   find . -name "__init__.py" -maxdepth 1
# ============================================================================

"""
Claude Code MCP Toolkit

渐进式披露的 Claude Code MCP 工具集，用于：
- 读取 ~/.claude 元信息
- 学术搜索与资料获取
- 视觉模型调用
- 知识图谱构建与问答
"""

__version__ = "0.1.0"
__all__ = [
    "core",
    "claude_meta",
    "academic",
    "vision",
    "graphrag",
    "mcp",
    "utils",
]
