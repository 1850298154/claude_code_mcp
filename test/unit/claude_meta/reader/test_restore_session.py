# ============================================================================
# 文件: test/unit/claude_meta/reader/test_restore_session.py
# 描述: 测试 restore_session 函数
#
# 测试对象: claude_meta/reader/restore_session.py
#
# Bash 快速定位: find test -name "test_restore_session.py"
# ============================================================================

import pytest

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.reader.restore_session import restore_session


class TestRestoreSession:
    """测试 restore_session 函数"""

    def test_restore_session_with_project(self, mock_claude_dir):
        """测试指定项目恢复会话"""
        # Given: 模拟的 ~/.claude 目录
        paths = ClaudeMetaPaths(mock_claude_dir)
        session_id = "session-001"
        project = "my-app"

        # When: 恢复会话
        session = restore_session(paths, session_id, project)

        # Then: 会话正确
        assert session is not None
        assert session.id == session_id
        assert session.project == project

    def test_restore_session_without_project(self, mock_claude_dir):
        """测试不指定项目恢复会话"""
        # Given: 模拟的 ~/.claude 目录
        paths = ClaudeMetaPaths(mock_claude_dir)
        session_id = "session-001"

        # When: 恢复会话
        session = restore_session(paths, session_id)

        # Then: 会话正确
        assert session is not None
        assert session.id == session_id

    def test_restore_session_not_found(self, mock_claude_dir):
        """测试恢复不存在的会话"""
        # Given: 模拟的 ~/.claude 目录
        paths = ClaudeMetaPaths(mock_claude_dir)
        session_id = "non-existent"

        # When: 恢复会话
        session = restore_session(paths, session_id)

        # Then: 结果为 None
        assert session is None
