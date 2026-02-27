# ============================================================================
# 文件: test/unit/claude_meta/parser/test_parse_history.py
# 描述: 测试 parse_history 函数
#
# 测试对象: claude_meta/parser/parse_history.py
#
# Bash 快速定位: find test -name "test_parse_history.py"
# ============================================================================

import pytest

from claude_meta.parser.parse_history import parse_history, HistoryEntry


class TestParseHistory:
    """测试 parse_history 函数"""

    def test_parse_history_basic(self):
        """测试基本历史解析"""
        # Given: 历史数据
        data = [
            {
                "query": "测试查询 1",
                "timestamp": "2024-01-01T10:00:00Z",
                "project": "project-1",
            },
            {
                "query": "测试查询 2",
                "timestamp": "2024-01-02T14:30:00Z",
                "project": "project-2",
            },
        ]

        # When: 解析历史
        entries = parse_history(data)

        # Then: 条目正确
        assert len(entries) == 2
        assert entries[0].query == "测试查询 1"
        assert entries[0].project == "project-1"
        assert entries[1].query == "测试查询 2"
        assert entries[1].project == "project-2"

    def test_parse_history_without_project(self):
        """测试无项目的历史解析"""
        # Given: 无项目数据
        data = [
            {
                "query": "测试查询",
                "timestamp": "2024-01-01T10:00:00Z",
            }
        ]

        # When: 解析历史
        entries = parse_history(data)

        # Then: project 为空字符串
        assert len(entries) == 1
        assert entries[0].project == ""

    def test_parse_history_empty(self):
        """测试空历史解析"""
        # Given: 空数据
        data = []

        # When: 解析历史
        entries = parse_history(data)

        # Then: 结果为空列表
        assert entries == []
