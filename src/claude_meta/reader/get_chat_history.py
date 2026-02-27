# ============================================================================
# 文件: claude_meta/reader/get_chat_history.py
# 描述: 获取指定会话的聊天历史
#
# 上游依赖: claude_meta/config/paths.py, claude_meta/parser/parse_conversation.py
# 下游封装: 无
# Bash 快速定位: find . -name "get_chat_history.py"
# ============================================================================

from pathlib import Path
from typing import List

from core.types.claude.message import Message

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.parser.parse_conversation import parse_conversation_from_file


def get_chat_history(paths: ClaudeMetaPaths, session_id: str, project: str | None = None) -> List[Message]:
    """获取指定会话的聊天历史

    Args:
        paths: ClaudeMetaPaths 路径配置
        session_id: 会话 ID
        project: 项目名称（可选，如果不指定则搜索所有项目）

    Returns:
        消息列表
    """
    if project:
        # 指定项目，直接查找
        session_file = paths.get_session_file(project, session_id)
        if not session_file.exists():
            return []
        conversation = parse_conversation_from_file(session_file)
        return conversation.messages
    else:
        # 未指定项目，搜索所有项目
        for project_dir in paths.projects_dir.iterdir():
            if not project_dir.is_dir():
                continue

            session_file = project_dir / f"{session_id}.json"
            if session_file.exists():
                conversation = parse_conversation_from_file(session_file)
                return conversation.messages

        return []
