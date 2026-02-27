# ============================================================================
# 文件: test/unit/claude_meta/reader/test_get_project_context.py
# 描述: 测试 get_project_context 函数
#
# 测试对象: claude_meta/reader/get_project_context.py
#
# Bash 快速定位: find test -name "test_get_project_context.py"
# ============================================================================

import pytest

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.reader.get_project_context import get_project_context


class TestGetProjectContext:
    """测试 get_project_context 函数"""

    def test_get_project_context(self, mock_claude_dir):
        """测试获取项目上下文"""
        # Given: 模拟的 ~/.claude 目录
        paths = ClaudeMetaPaths(mock_claude_dir)
        project_name = "my-app"

        # When: 获取项目上下文
        context = get_project_context(paths, project_name)

        # Then: 上下文正确
        assert context["project_name"] == project_name
        assert context["total_sessions"] >= 1
        assert context["total_messages"] >= 1
        assert "session_ids" in context
        assert isinstance(context["recent_messages"], list)

    def test_get_project_context_not_found(self, mock_claude_dir):
        """测试获取不存在的项目上下文"""
        # Given: 模拟的 ~/.claude 目录
        paths = ClaudeMetaPaths(mock_claude_dir)
        project_name = "non-existent"

        # When: 获取项目上下文
        context = get_project_context(paths, project_name)

        # Then: 会话数为 0
        assert context["project_name"] == project_name
        assert context["total_sessions"] == 0
        assert context["total_messages"] == 0
