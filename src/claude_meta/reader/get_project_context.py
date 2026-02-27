# ============================================================================
# 文件: claude_meta/reader/get_project_context.py
# 描述: 获取项目上下文信息
#
# 上游依赖: claude_meta/config/paths.py, claude_meta/reader/get_sessions.py
# 下游封装: 无
# Bash 快速定位: find . -name "get_project_context.py"
# ============================================================================

from typing import List, Dict, Any

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.reader.get_sessions import get_sessions


def get_project_context(paths: ClaudeMetaPaths, project_name: str) -> Dict[str, Any]:
    """获取项目上下文信息

    Args:
        paths: ClaudeMetaPaths 路径配置
        project_name: 项目名称

    Returns:
        项目上下文字典，包含会话列表、消息摘要等
    """
    sessions = get_sessions(paths)

    # 筛选属于指定项目的会话
    project_sessions = [s for s in sessions if s.project == project_name]

    # 统计信息
    total_messages = sum(len(s.messages) for s in project_sessions)
    user_messages = sum(
        1 for s in project_sessions for m in s.messages if m.role.value == "user"
    )

    # 提取最近的消息
    recent_messages = []
    for session in sorted(project_sessions, key=lambda s: s.updated_at, reverse=True):
        recent_messages.extend(session.messages[-5:])  # 每个会话取最后5条消息
        if len(recent_messages) >= 20:
            break

    return {
        "project_name": project_name,
        "total_sessions": len(project_sessions),
        "total_messages": total_messages,
        "user_messages": user_messages,
        "assistant_messages": total_messages - user_messages,
        "recent_messages": recent_messages[:20],
        "session_ids": [s.id for s in project_sessions],
    }
