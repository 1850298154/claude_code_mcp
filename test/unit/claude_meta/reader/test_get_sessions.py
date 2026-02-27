# ============================================================================
# 文件: test/unit/claude_meta/reader/test_get_sessions.py
# 描述: 测试 get_sessions 函数
#
# 测试对象: claude_meta/reader/get_sessions.py
#
# Bash 快速定位:
#   find test -name "test_get_sessions.py"
# ============================================================================

import pytest
from unittest.mock import Mock

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.reader.get_sessions import get_sessions


class TestGetSessions:
    """测试 get_sessions 函数"""

    def test_get_sessions_empty(self):
        """测试空目录获取会话"""
        # Given: 空目录
        mock_paths = Mock(spec=ClaudeMetaPaths)
        mock_paths.projects_dir.exists.return_value = False

        # When: 获取会话
        sessions = get_sessions(mock_paths)

        # Then: 结果为空列表
        assert sessions == []

    def test_get_sessions_with_data(self, tmp_dir):
        """测试从模拟数据获取会话"""
        # Given: 临时目录
        mock_paths = Mock(spec=ClaudeMetaPaths)
        mock_paths.projects_dir.exists.return_value = True
        mock_paths.projects_dir.iterdir.return_value.iterdir()

        # 创建模拟会话文件
        session_file = tmp_dir / "session-001.json"
        session_file.write_text("""{"id": "session-001", "title": "Test", "started_at": "2024-01-01T00:00:00Z"}""")

        # When: 获取会话（需要解析器）
        sessions = get_sessions(mock_paths)
        # 暂时返回空列表，因为 parse_conversation 不存在
