# ============================================================================
# 文件: src/claude_meta/__init__.py
# 描述: Claude Meta 模块初始化
#
# 上游依赖: 无
# 下游封装: examples/claude_meta_usage.py
#
# Bash 快速定位:
#   find src -name "__init__.py" -path "*/claude_meta/*"
# ============================================================================

"""Claude Meta 模块

提供 Claude Code 元数据读取功能，包括会话历史、项目上下文、记忆等。
"""

from claude_meta.reader import ClaudeMetaReader
from claude_meta.config.paths import ClaudeMetaPaths

__all__ = [
    "ClaudeMetaReader",
    "ClaudeMetaPaths",
]
