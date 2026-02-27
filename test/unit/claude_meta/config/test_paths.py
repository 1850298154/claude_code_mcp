# ============================================================================
# 文件: test/unit/claude_meta/config/test_paths.py
# 描述: 测试 ClaudeMetaPaths 类
#
# 测试对象: claude_meta/config/paths.py
#
# Bash 快速定位: find test -name "test_paths.py"
# ============================================================================

import pytest
from pathlib import Path

from claude_meta.config.paths import ClaudeMetaPaths


class TestClaudeMetaPaths:
    """测试 ClaudeMetaPaths 类"""

    def test_paths_initialization_default(self):
        """测试默认路径初始化"""
        # When: 创建 ClaudeMetaPaths
        paths = ClaudeMetaPaths()

        # Then: 路径正确
        assert paths.claude_dir == Path.home() / ".claude"
        assert paths.history_file == paths.claude_dir / "history.json"
        assert paths.projects_dir == paths.claude_dir / "projects"
        assert paths.debug_dir == paths.claude_dir / "debug"
        assert paths.session_env_dir == paths.claude_dir / "session-env"
        assert paths.memory_dir == paths.claude_dir / "memory"

    def test_paths_initialization_custom(self, temp_dir):
        """测试自定义路径初始化"""
        # Given: 自定义路径
        custom_path = temp_dir / "custom_claude"

        # When: 创建 ClaudeMetaPaths
        paths = ClaudeMetaPaths(custom_path)

        # Then: 路径正确
        assert paths.claude_dir == custom_path
        assert paths.history_file == custom_path / "history.json"
        assert paths.projects_dir == custom_path / "projects"

    def test_get_session_file(self):
        """测试获取会话文件路径"""
        # Given: ClaudeMetaPaths
        paths = ClaudeMetaPaths()
        project = "my-project"
        session_id = "session-001"

        # When: 获取会话文件路径
        session_file = paths.get_session_file(project, session_id)

        # Then: 路径正确
        expected = paths.projects_dir / project / f"{session_id}.json"
        assert session_file == expected

    def test_get_debug_file(self):
        """测试获取调试日志文件路径"""
        # Given: ClaudeMetaPaths
        paths = ClaudeMetaPaths()
        session_id = "session-001"

        # When: 获取调试日志文件路径
        debug_file = paths.get_debug_file(session_id)

        # Then: 路径正确
        expected = paths.debug_dir / f"{session_id}.txt"
        assert debug_file == expected

    def test_get_memory_file(self):
        """测试获取记忆文件路径"""
        # Given: ClaudeMetaPaths
        paths = ClaudeMetaPaths()

        # When: 获取记忆文件路径
        memory_file = paths.get_memory_file()

        # Then: 路径正确
        expected = paths.memory_dir / "MEMORY.md"
        assert memory_file == expected
