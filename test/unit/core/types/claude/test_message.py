# ============================================================================
# 文件: test/unit/core/types/claude/test_message.py
# 描述: 测试 Message 类
#
# 测试对象: core/types/claude/message.py
#
# Bash 快速定位: find test -name "test_message.py"
# ============================================================================

import pytest
from datetime import datetime

from core.types.claude.message import Message, Role


class TestMessage:
    """测试 Message 类"""

    def test_message_creation(self):
        """测试创建 Message"""
        # Given: 消息数据
        msg_id = "msg-001"
        role = Role.USER
        content = "测试消息"
        timestamp = datetime.now()

        # When: 创建 Message
        message = Message(id=msg_id, role=role, content=content, timestamp=timestamp)

        # Then: 字段正确
        assert message.id == msg_id
        assert message.role == role
        assert message.content == content
        assert message.timestamp == timestamp

    def test_role_enum(self):
        """测试 Role 枚举"""
        # Given: 预期的角色值
        expected_values = {"user", "assistant", "system"}

        # When: 获取所有角色
        actual_values = {role.value for role in Role}

        # Then: 值匹配
        assert actual_values == expected_values

    def test_message_with_metadata(self):
        """测试带 metadata 的 Message"""
        # Given: 带元数据的消息
        metadata = {"tool_calls": [{"name": "read_file", "args": {"path": "test.py"}}]}

        # When: 创建 Message
        message = Message(
            id="msg-001",
            role=Role.ASSISTANT,
            content="读取文件",
            timestamp=datetime.now(),
            metadata=metadata,
        )

        # Then: metadata 正确
        assert message.metadata == metadata
