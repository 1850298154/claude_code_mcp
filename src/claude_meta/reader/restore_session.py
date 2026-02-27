# ============================================================================
# 文件: claude_meta/reader/restore_session.py
# 描述: 恢复指定会话的完整信息
#
# 上游依赖: claude_meta/config/paths.py, claude_meta/parser/parse_conversation.py
# 下游封装: 无
# Bash 快速定位: find . -name "restore_session.py"
# ============================================================================

from pathlib import Path
from typing import Dict, Any

from core.types.claude.conversation import Conversation

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.parser.parse_conversation import parse_conversation_from_file


def restore_session(
    paths: ClaudeMetaPaths,
    session_id: str,
    project: str | None = None,
) -> Conversation | None:
    """恢复指定会话

    Args:
        paths: ClaudeMetaPaths 路径配置
        session_id: 会话 ID
        project: 项目名称（可选，如果不指定则搜索所有项目）

    Returns:
        Conversation 对象，如果找不到则返回 None
    """
    if project:
        session_file = paths.get_session_file(project, session_id)
        if not session_file.exists():
            return None
        return parse_conversation_from_file(session_file)
    else:
        for project_dir in paths.projects_dir.iterdir():
            if not project_dir.is_dir():
                continue

            session_file = project_dir / f"{session_id}.json"
            if session_file.exists():
                return parse_conversation_from_file(session_file)

        return None
