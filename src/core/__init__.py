# ============================================================================
# 文件: src/core/__init__.py
# 描述: Core 模块初始化
#
# 上游依赖: 无
# 下游封装: claude_meta/, test/unit/core/
#
# Bash 快速定位:
#   find src -name "__init__.py" -path "*/core/*"
# ============================================================================

"""Core 模块

提供核心数据类型定义。
"""

from core.types.claude.message import Message, Role
from core.types.claude.conversation import Conversation
from core.types.claude.session import Session

__all__ = [
    "Message",
    "Role",
    "Conversation",
    "Session",
]
