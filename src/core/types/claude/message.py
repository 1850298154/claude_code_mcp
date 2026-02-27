# ============================================================================
# 文件: core/types/claude/message.py
# 描述: Message 数据结构定义，表示对话中的一条消息
#
# 上游依赖:
#   - 无
#
# 下游封装:
#   - core/types/claude/conversation.py (Conversation 消息列表)
#   - claude_meta/parser/parse_conversation.py (解析消息)
#   - claude_meta/analyzer/extract_context.py (提取消息上下文)
#
# Bash 快速定位:
#   find . -name "message.py" -path "*/claude/*"
# ============================================================================

from dataclasses import dataclass
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum


class Role(Enum):
    """消息角色枚举"""

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


@dataclass
class Message:
    """表示对话中的一条消息

    Attributes:
        id: 消息唯一标识符
        role: 消息角色（user/assistant/system）
        content: 消息内容
        timestamp: 消息时间戳
        metadata: 额外元数据（工具调用、思考时间等）
    """

    id: str
    role: Role
    content: str
    timestamp: datetime
    metadata: Optional[Dict[str, Any]] = None
