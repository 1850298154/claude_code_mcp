# ============================================================================
# 文件: core/types/claude/session.py
# 描述: Session 数据结构定义，表示 Claude Code 工作会话
#
# 上游依赖:
#   - core/types/claude/conversation.py (Conversation)
#
# 下游封装:
#   - claude_meta/reader/get_sessions.py (获取所有会话)
#   - claude_meta/reader/restore_session.py (恢复会话)
#   - claude_meta/analyzer/detect_interrupted.py (检测中断会话)
#
# Bash 快速定位:
#   find . -name "session.py" -path "*/claude/*"
# ============================================================================

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from enum import Enum


class SessionStatus(Enum):
    """会话状态枚举"""

    ACTIVE = "active"
    COMPLETED = "completed"
    INTERRUPTED = "interrupted"
    ERROR = "error"


@dataclass
class Session:
    """表示 Claude Code 工作会话

    Attributes:
        id: 会话唯一标识符
        project: 项目名称
        working_directory: 工作目录
        conversations: 对话列表
        status: 会话状态
        started_at: 开始时间
        ended_at: 结束时间（可选）
        error_message: 错误信息（如果有）
    """

    id: str
    project: str
    working_directory: str
    conversations: List["Conversation"]
    status: SessionStatus
    started_at: datetime
    ended_at: Optional[datetime] = None
    error_message: Optional[str] = None
