# ============================================================================
# 文件: test/unit/claude_meta/parser/test_parse_conversation.py
# 描述: 测试 parse_conversation 函数
#
# 测试对象: claude_meta/parser/parse_conversation.py
#
# Bash 快速定位: find test -name "test_parse_conversation.py"
# ============================================================================

import pytest

from claude_meta.parser.parse_conversation import parse_conversation


class TestParseConversation:
    """测试 parse_conversation 函数"""

    def test_parse_conversation_basic(self):
        """测试基本会话解析"""
        # Given: 会话数据
        data = {
            "id": "session-001",
            "title": "测试会话",
            "started_at": "2024-01-01T10:00:00Z",
            "ended_at": "2024-01-01T11:00:00Z",
            "project": "my-project",
            "messages": [
                {
                    "id": "msg-001",
                    "role": "user",
                    "content": "测试消息",
                    "timestamp": "2024-01-01T10:00:00Z",
                }
            ],
        }

        # When: 解析会话
        conversation = parse_conversation(data)

        # Then: 字段正确
        assert conversation.id == "session-001"
        assert conversation.title == "测试会话"
        assert conversation.project == "my-project"
        assert len(conversation.messages) == 1
        assert conversation.messages[0].role.value == "user"
        assert conversation.messages[0].content == "测试消息"

    def test_parse_conversation_without_project(self):
        """测试无项目的会话解析"""
        # Given: 无项目数据
        data = {
            "id": "session-002",
            "title": "无项目会话",
            "started_at": "2024-01-01T10:00:00Z",
            "messages": [],
        }

        # When: 解析会话
        conversation = parse_conversation(data)

        # Then: project 为 None
        assert conversation.project is None

    def test_parse_conversation_multiple_messages(self):
        """测试多消息会话解析"""
        # Given: 多条消息
        data = {
            "id": "session-003",
            "title": "多消息会话",
            "started_at": "2024-01-01T10:00:00Z",
            "messages": [
                {
                    "id": "msg-001",
                    "role": "user",
                    "content": "第一条消息",
                    "timestamp": "2024-01-01T10:00:00Z",
                },
                {
                    "id": "msg-002",
                    "role": "assistant",
                    "content": "第二条消息",
                    "timestamp": "2024-01-01T10:01:00Z",
                },
                {
                    "id": "msg-003",
                    "role": "system",
                    "content": "系统消息",
                    "timestamp": "2024-01-01T10:02:00Z",
                },
            ],
        }

        # When: 解析会话
        conversation = parse_conversation(data)

        # Then: 消息数量正确
        assert len(conversation.messages) == 3
        assert conversation.messages[0].role.value == "user"
        assert conversation.messages[1].role.value == "assistant"
        assert conversation.messages[2].role.value == "system"
