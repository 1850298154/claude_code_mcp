# ============================================================================
# 文件: test/unit/claude_meta/parser/test_parse_memory.py
# 描述: 测试 parse_memory 函数
#
# 测试对象: claude_meta/parser/parse_memory.py
#
# Bash 快速定位: find test -name "test_parse_memory.py"
# ============================================================================

import pytest
from pathlib import Path

from claude_meta.parser.parse_memory import parse_memory


class TestParseMemory:
    """测试 parse_memory 函数"""

    def test_parse_memory_from_file(self, temp_dir):
        """测试从文件解析记忆"""
        # Given: 记忆文件
        memory_file = temp_dir / "MEMORY.md"
        memory_file.write_text("# Memory\n\n## Context\nTest content")

        # When: 解析记忆
        content = parse_memory(memory_file)

        # Then: 内容正确
        assert content == "# Memory\n\n## Context\nTest content"

    def test_parse_memory_empty_file(self, temp_dir):
        """测试空文件解析"""
        # Given: 空文件
        memory_file = temp_dir / "MEMORY.md"
        memory_file.write_text("")

        # When: 解析记忆
        content = parse_memory(memory_file)

        # Then: 内容为空字符串
        assert content == ""

    def test_parse_memory_multiline(self, temp_dir):
        """测试多行记忆解析"""
        # Given: 多行记忆文件
        memory_file = temp_dir / "MEMORY.md"
        content = "# Memory\n\n## Project 1\nDone\n\n## Project 2\nIn progress"
        memory_file.write_text(content)

        # When: 解析记忆
        result = parse_memory(memory_file)

        # Then: 内容正确保留换行
        assert result == content
