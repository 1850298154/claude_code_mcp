# ============================================================================
# 文件: claude_meta/reader/__init__.py
# 描述: ClaudeMetaReader 数据结构定义，用于读取 ~/.claude 元信息
#
# 上游依赖:
#   - claude_meta/config/paths.py          (ClaudeMetaPaths)
#   - claude_meta/reader/get_sessions.py  (get_sessions)
#   - claude_meta/reader/get_chat_history.py (get_chat_history)
#   - claude_meta/reader/get_project_context.py (get_project_context)
#   - claude_meta/reader/get_memory.py     (get_memory)
#   - claude_meta/reader/restore_session.py (restore_session)
#
# 下游封装:
#   - mcp/tools/claude_meta.py            (ClaudeMeta MCP 工具)
#
# Bash 快速定位:
#   find . -name "__init__.py" -path "*/claude_meta/reader/*"
# ============================================================================

from pathlib import Path
from typing import List, Dict, Any

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.reader.get_sessions import get_sessions
from claude_meta.reader.get_chat_history import get_chat_history
from claude_meta.reader.get_project_context import get_project_context
from claude_meta.reader.get_memory import get_memory
from claude_meta.reader.restore_session import restore_session
from claude_meta.analyzer.detect_interrupted import detect_interrupted
from claude_meta.analyzer.summarize_progress import summarize_progress


class ClaudeMetaReader:
    """Claude Meta Reader - 读取 ~/.claude 元信息

    提供访问 Claude Code 存储的所有元信息的能力，
    包括会话、对话、项目上下文和记忆。
    """

    def __init__(self, claude_path: Path | None = None):
        """初始化 Reader

        Args:
            claude_path: ~/.claude 路径，默认为 ~/.claude
        """
        self._paths = ClaudeMetaPaths(claude_path)

    def get_sessions(self) -> List:
        """获取所有会话

        Returns:
            会话列表
        """
        return get_sessions(self._paths)

    def get_chat_history(
        self, session_id: str, project: str | None = None
    ) -> List:
        """获取指定会话的聊天历史

        Args:
            session_id: 会话 ID
            project: 项目名称（可选）

        Returns:
            消息列表
        """
        return get_chat_history(self._paths, session_id, project)

    def get_project_context(self, project_name: str) -> Dict[str, Any]:
        """获取项目上下文

        Args:
            project_name: 项目名称

        Returns:
            项目上下文字典
        """
        return get_project_context(self._paths, project_name)

    def get_memory(self) -> str:
        """获取记忆内容

        Returns:
            记忆内容字符串
        """
        return get_memory(self._paths)

    def restore_session(
        self, session_id: str, project: str | None = None
    ):
        """恢复指定会话

        Args:
            session_id: 会话 ID
            project: 项目名称（可选）

        Returns:
            Conversation 对象，如果找不到则返回 None
        """
        return restore_session(self._paths, session_id, project)

    def detect_interrupted(self) -> List:
        """检测中断的会话

        Returns:
            中断的会话列表
        """
        return detect_interrupted(self._paths)

    def summarize_progress(self, session_id: str, project: str | None = None):
        """总结会话进度

        Args:
            session_id: 会话 ID
            project: 项目名称（可选）

        Returns:
            进度总结字典
        """
        session = self.restore_session(session_id, project)
        if session is None:
            return None
        return summarize_progress(session)


__all__ = ["ClaudeMetaReader"]
