# ============================================================================
# 文件: test/unit/core/types/claude/test_conversation.py
# 描述: 测试 Conversation 类
#
# 测试对象: core/types/claude/conversation.py
#
# Bash 快速定位: find test -name "test_conversation.py"
# ============================================================================

import pytest
from datetime import datetime

from core.types.claude.conversation import Conversation
from core.types.claude.message import Message, Role


class TestConversation:
    """测试 Conversation 类"""

    def test_conversation_creation(self):
        """测试创建 Conversation"""
        # Given: 会话数据
        conv_id = "conv-001"
        title = "测试会话"
        messages = [
            Message(
                id="msg-001",
                role=Role.USER,
                content="测试消息",
                timestamp=datetime.now(),
            )
        ]

        # When: 创建 Conversation
        conversation = Conversation(
            id=conv_id,
            title=title,
            messages=messages,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        # Then: 字段正确
        assert conversation.id == conv_id
        assert conversation.title == title
        assert len(conversation.messages) == 1
        assert conversation.project is None

    def test_conversation_with_project(self):
        """测试带项目的 Conversation"""
        # Given: 会话数据
        project = "my-project"

        # When: 创建 Conversation
        conversation = Conversation(
            id="conv-001",
            title="测试会话",
            messages=[],
            created_at=datetime.now(),
            updated_at=datetime.now(),
            project=project,
        )

        # Then: project 正确
        assert conversation.project == project
