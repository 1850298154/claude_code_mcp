# ============================================================================
# 文件: core/types/claude/conversation.py
# 描述: Conversation 数据结构定义，表示一次 Claude 对话会话
#
# 上游依赖:
#   - core/types/claude/message.py  (Message)
#
# 下游封装:
#   - claude_meta/reader/get_chat_history.py  (获取聊天历史)
#   - claude_meta/parser/parse_conversation.py (解析对话文件)
#   - claude_meta/analyzer/extract_context.py (提取上下文)
#
# Bash 快速定位:
#   find . -name "conversation.py" -path "*/claude/*"
# ============================================================================

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Conversation:
    """表示一次 Claude 对话会话的数据结构

    Attributes:
        id: 对话唯一标识符
        title: 对话标题
        messages: 消息列表
        created_at: 创建时间
        updated_at: 最后更新时间
        project: 关联的项目名称（可选）
    """

    id: str
    title: str
    messages: List["Message"]
    created_at: datetime
    updated_at: datetime
    project: Optional[str] = None
