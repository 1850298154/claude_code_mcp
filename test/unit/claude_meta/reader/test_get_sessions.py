# ============================================================================
# 文件: test/unit/claude_meta/reader/test_get_sessions.py
# 描述: 测试 get_sessions 函数
#
# 测试对象: claude_meta/reader/get_sessions.py
#
# Bash 快速定位: find test -name "test_get_sessions.py"
# ============================================================================

import pytest
from pathlib import Path

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.reader.get_sessions import get_sessions


class TestGetSessions:
    """测试 get_sessions 函数"""

    def test_get_sessions_empty(self, temp_dir):
        """测试空目录获取会话"""
        # Given: 空目录
        claude_dir = temp_dir / ".claude"
        claude_dir.mkdir()
        paths = ClaudeMetaPaths(claude_dir)

        # When: 获取会话
        sessions = get_sessions(paths)

        # Then: 结果为空列表
        assert sessions == []

    def test_get_sessions_with_mock_data(self, mock_claude_dir):
        """测试从模拟数据获取会话"""
        # Given: 模拟的 ~/.claude 目录
        paths = ClaudeMetaPaths(mock_claude_dir)

        # When: 获取会话
        sessions = get_sessions(paths)

        # Then: 会话数量正确
        assert len(sessions) >= 1
        assert sessions[0].id in ["session-001", "session-002"]
        assert sessions[0].project == "my-app"

    def test_get_sessions_no_projects_dir(self, temp_dir):
        """测试无 projects 目录"""
        # Given: 无 projects 目录
        claude_dir = temp_dir / ".claude"
        claude_dir.mkdir()
        paths = ClaudeMetaPaths(claude_dir)

        # When: 获取会话
        sessions = get_sessions(paths)

        # Then: 结果为空列表
        assert sessions == []
