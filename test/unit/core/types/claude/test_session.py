# ============================================================================
# 文件: test/unit/core/types/claude/test_session.py
# 描述: 测试 Session 类
#
# 测试对象: core/types/claude/session.py
#
# Bash 快速定位: find test -name "test_session.py"
# ============================================================================

import pytest
from datetime import datetime

from core.types.claude.session import Session, SessionStatus
from core.types.claude.conversation import Conversation


class TestSession:
    """测试 Session 类"""

    def test_session_creation(self):
        """测试创建 Session"""
        # Given: 会话数据
        session_id = "session-001"
        project = "my-project"
        working_directory = "/home/user/my-project"
        conversations = []

        # When: 创建 Session
        session = Session(
            id=session_id,
            project=project,
            working_directory=working_directory,
            conversations=conversations,
            status=SessionStatus.ACTIVE,
            started_at=datetime.now(),
        )

        # Then: 字段正确
        assert session.id == session_id
        assert session.project == project
        assert session.working_directory == working_directory
        assert session.status == SessionStatus.ACTIVE
        assert session.ended_at is None

    def test_session_status_enum(self):
        """测试 SessionStatus 枚举"""
        # Given: 预期的状态值
        expected_values = {"active", "completed", "interrupted", "error"}

        # When: 获取所有状态
        actual_values = {status.value for status in SessionStatus}

        # Then: 值匹配
        assert actual_values == expected_values

    def test_session_with_error(self):
        """测试带错误的 Session"""
        # Given: 错误信息
        error_message = "Connection timeout"

        # When: 创建 Session
        session = Session(
            id="session-001",
            project="my-project",
            working_directory="/home/user/my-project",
            conversations=[],
            status=SessionStatus.ERROR,
            started_at=datetime.now(),
            error_message=error_message,
        )

        # Then: 错误信息正确
        assert session.error_message == error_message
