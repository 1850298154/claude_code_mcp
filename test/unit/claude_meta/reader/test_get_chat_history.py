# ============================================================================
# 文件: test/unit/claude_meta/reader/test_get_chat_history.py
# 描述: 测试 get_chat_history 函数
#
# 测试对象: claude_meta/reader/get_chat_history.py
#
# Bash 快速定位: find test -name "test_get_chat_history.py"
# ============================================================================

import pytest

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.reader.get_chat_history import get_chat_history


class TestGetChatHistory:
    """测试 get_chat_history 函数"""

    def test_get_chat_history_with_project(self, mock_claude_dir):
        """测试指定项目获取聊天历史"""
        # Given: 模拟的 ~/.claude 目录
        paths = ClaudeMetaPaths(mock_claude_dir)
        session_id = "session-001"
        project = "my-app"

        # When: 获取聊天历史
        messages = get_chat_history(paths, session_id, project)

        # Then: 消息数量正确
        assert len(messages) >= 1
        assert messages[0].role.value == "user"

    def test_get_chat_history_without_project(self, mock_claude_dir):
        """测试不指定项目获取聊天历史"""
        # Given: 模拟的 ~/.claude 目录
        paths = ClaudeMetaPaths(mock_claude_dir)
        session_id = "session-001"

        # When: 获取聊天历史
        messages = get_chat_history(paths, session_id)

        # Then: 消息数量正确
        assert len(messages) >= 1

    def test_get_chat_history_not_found(self, mock_claude_dir):
        """测试获取不存在的会话"""
        # Given: 模拟的 ~/.claude 目录
        paths = ClaudeMetaPaths(mock_claude_dir)
        session_id = "non-existent"

        # When: 获取聊天历史
        messages = get_chat_history(paths, session_id)

        # Then: 结果为空列表
        assert messages == []
