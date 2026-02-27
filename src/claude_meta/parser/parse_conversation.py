# ============================================================================
# 文件: claude_meta/parser/parse_conversation.py
# 描述: 解析会话文件，返回 Conversation 对象
#
# 上游依赖: core/types/claude/conversation.py, core/types/claude/message.py
# 下游封装: reader/get_sessions.py, reader/restore_session.py
# Bash 快速定位: find . -name "parse_conversation.py"
# ============================================================================

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

from core.types.claude.conversation import Conversation
from core.types.claude.message import Message, Role


def parse_conversation(data: Dict[str, Any]) -> Conversation:
    """解析会话数据为 Conversation 对象

    Args:
        data: 会话 JSON 数据

    Returns:
        Conversation 对象
    """
    messages = []

    for msg_data in data.get("messages", []):
        role = Role(msg_data["role"])
        message = Message(
            id=msg_data["id"],
            role=role,
            content=msg_data["content"],
            timestamp=datetime.fromisoformat(msg_data["timestamp"].replace("Z", "+00:00")),
            metadata=msg_data.get("metadata"),
        )
        messages.append(message)

    return Conversation(
        id=data["id"],
        title=data.get("title", f"Session {data['id']}"),
        messages=messages,
        created_at=datetime.fromisoformat(data["started_at"].replace("Z", "+00:00")),
        updated_at=datetime.fromisoformat(data.get("ended_at", data["started_at"]).replace("Z", "+00:00")),
        project=data.get("project"),
    )


def parse_conversation_from_file(file_path: Path) -> Conversation:
    """从文件解析会话

    Args:
        file_path: 会话文件路径

    Returns:
        Conversation 对象
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return parse_conversation(data)
