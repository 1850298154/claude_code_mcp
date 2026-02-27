# ============================================================================
# 文件: test/unit/claude_meta/analyzer/test_extract_context.py
# 描述: 测试 extract_context 函数
#
# 测试对象: claude_meta/analyzer/extract_context.py
#
# Bash 快速定位: find test -name "test_extract_context.py"
# ============================================================================

import pytest
from datetime import datetime

from core.types.claude.conversation import Conversation
from core.types.claude.message import Message, Role
from claude_meta.analyzer.extract_context import extract_context


class TestExtractContext:
    """测试 extract_context 函数"""

    def test_extract_context_basic(self):
        """测试基本上下文提取"""
        # Given: 会话数据
        messages = [
            Message(
                id="msg-001",
                role=Role.USER,
                content="帮我实现用户登录功能",
                timestamp=datetime.now(),
            ),
            Message(
                id="msg-002",
                role=Role.ASSISTANT,
                content="我来帮你实现",
                timestamp=datetime.now(),
                metadata={"tool_calls": [{"name": "read_file", "args": {"path": "auth.py"}}]},
            ),
        ]
        conversation = Conversation(
            id="session-001",
            title="登录功能",
            messages=messages,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            project="my-app",
        )

        # When: 提取上下文
        context = extract_context(conversation)

        # Then: 上下文正确
        assert context["session_id"] == "session-001"
        assert context["project"] == "my-app"
        assert context["total_messages"] == 2
        assert context["user_messages"] == 1
        assert context["assistant_messages"] == 1
        assert len(context["tool_calls"]) == 1

    def test_extract_context_with_files(self):
        """测试提取文件引用"""
        # Given: 包含文件引用的会话
        messages = [
            Message(
                id="msg-001",
                role=Role.USER,
                content="修改 auth.py 和 user.py",
                timestamp=datetime.now(),
            )
        ]
        conversation = Conversation(
            id="session-001",
            title="修改文件",
            messages=messages,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            project="my-app",
        )

        # When: 提取上下文
        context = extract_context(conversation)

        # Then: 文件引用正确
        assert "auth.py" in context["file_references"]
        assert "user.py" in context["file_references"]

    def test_extract_context_with_keywords(self):
        """测试提取任务关键词"""
        # Given: 包含任务关键词的会话
        messages = [
            Message(
                id="msg-001",
                role=Role.USER,
                content="帮我实现并测试这个功能",
                timestamp=datetime.now(),
            )
        ]
        conversation = Conversation(
            id="session-001",
            title="任务",
            messages=messages,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            project="my-app",
        )

        # When: 提取上下文
        context = extract_context(conversation)

        # Then: 关键词正确
        assert "实现" in context["task_keywords"]
        assert "测试" in context["task_keywords"]
