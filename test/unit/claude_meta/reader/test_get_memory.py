# ============================================================================
# 文件: test/unit/claude_meta/reader/test_get_memory.py
# 描述: 测试 get_memory 函数
#
# 测试对象: claude_meta/reader/get_memory.py
#
# Bash 快速定位: find test -name "test_get_memory.py"
# ============================================================================

import pytest

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.reader.get_memory import get_memory


class TestGetMemory:
    """测试 get_memory 函数"""

    def test_get_memory_exists(self, mock_claude_dir):
        """测试获取存在的记忆"""
        # Given: 模拟的 ~/.claude 目录
        paths = ClaudeMetaPaths(mock_claude_dir)

        # When: 获取记忆
        memory = get_memory(paths)

        # Then: 记忆内容正确
        assert "Memory" in memory
        assert "my-app" in memory

    def test_get_memory_not_exists(self, temp_dir):
        """测试获取不存在的记忆"""
        # Given: 无记忆目录
        claude_dir = temp_dir / ".claude"
        claude_dir.mkdir()
        paths = ClaudeMetaPaths(claude_dir)

        # When: 获取记忆
        memory = get_memory(paths)

        # Then: 结果为空字符串
        assert memory == ""
