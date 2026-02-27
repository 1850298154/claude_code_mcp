# ============================================================================
# 文件: claude_meta/reader/get_sessions.py
# 描述: 获取所有会话列表
#
# 上游依赖: claude_meta/config/paths.py, claude_meta/parser/parse_conversation.py
# 下游封装: 无
# Bash 快速定位: find . -name "get_sessions.py"
# ============================================================================

from pathlib import Path
from typing import List

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.parser.parse_conversation import parse_conversation_from_file


def get_sessions(paths: ClaudeMetaPaths) -> List:
    """获取所有会话

    Args:
        paths: ClaudeMetaPaths 路径配置

    Returns:
        会话列表
    """
    sessions = []

    if not paths.projects_dir.exists():
        return sessions

    for project_dir in paths.projects_dir.iterdir():
        if not project_dir.is_dir():
            continue

        for session_file in project_dir.glob("*.json"):
            try:
                session = parse_conversation_from_file(session_file)
                sessions.append(session)
            except Exception:
                # 跳过无法解析的文件
                continue

    return sessions
