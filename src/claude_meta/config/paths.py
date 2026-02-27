# ============================================================================
# 文件: claude_meta/config/paths.py
# 描述: ClaudeMetaPaths 数据结构定义，管理 ~/.claude 路径
#
# 上游依赖: 无
# 下游封装: claude_meta/reader/*, claude_meta/parser/*
# Bash 快速定位: find . -name "paths.py" -path "*/claude_meta/*"
# ============================================================================

from pathlib import Path
from dataclasses import dataclass


@dataclass
class ClaudeMetaPaths:
    """Claude Meta 路径配置

    管理 ~/.claude 目录下的所有路径。

    Claude Code 历史存储结构:
        ~/.claude/
        ├── history.json                    # 所有用户 query 汇总
        ├── projects/[项目]/[sessionId].json  # 完整对话历史
        ├── debug/[sessionId].txt           # 系统调试日志
        ├── session-env/[sessionId]/       # 会话环境信息
        └── memory/                         # 记忆内容
    """

    claude_dir: Path
    history_file: Path
    projects_dir: Path
    debug_dir: Path
    session_env_dir: Path
    memory_dir: Path

    def __init__(self, claude_path: Path | None = None):
        """初始化路径配置

        Args:
            claude_path: ~/.claude 路径，默认为 ~/.claude
        """
        self.claude_dir = claude_path or Path.home() / ".claude"
        self.history_file = self.claude_dir / "history.json"
        self.projects_dir = self.claude_dir / "projects"
        self.debug_dir = self.claude_dir / "debug"
        self.session_env_dir = self.claude_dir / "session-env"
        self.memory_dir = self.claude_dir / "memory"

    def get_session_file(self, project: str, session_id: str) -> Path:
        """获取会话文件路径

        Args:
            project: 项目名称
            session_id: 会话 ID

        Returns:
            会话文件路径
        """
        return self.projects_dir / project / f"{session_id}.json"

    def get_debug_file(self, session_id: str) -> Path:
        """获取调试日志文件路径

        Args:
            session_id: 会话 ID

        Returns:
            调试日志文件路径
        """
        return self.debug_dir / f"{session_id}.txt"

    def get_session_env_dir(self, session_id: str) -> Path:
        """获取会话环境目录路径

        Args:
            session_id: 会话 ID

        Returns:
            会话环境目录路径
        """
        return self.session_env_dir / session_id

    def get_memory_file(self) -> Path:
        """获取记忆文件路径

        Returns:
            记忆文件路径
        """
        return self.memory_dir / "MEMORY.md"
