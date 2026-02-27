# ============================================================================
# 文件: test/unit/claude_meta/analyzer/test_summarize_progress.py
# 描述: 测试 summarize_progress 函数
#
# 测试对象: claude_meta/analyzer/summarize_progress.py
#
# Bash 快速定位: find test -name "test_summarize_progress.py"
# ============================================================================

import pytest
from datetime import datetime

from core.types.claude.conversation import Conversation
from core.types.claude.message import Message, Role
from claude_meta.analyzer.summarize_progress import summarize_progress


class TestSummarizeProgress:
    """测试 summarize_progress 函数"""

    def test_summarize_progress_basic(self):
        """测试基本进度总结"""
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
            )
        ]
        conversation = Conversation(
            id="session-001",
            title="登录功能",
            messages=messages,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            project="my-app",
        )

        # When: 总结进度
        progress = summarize_progress(conversation)

        # Then: 进度正确
        assert progress["session_id"] == "session-001"
        assert progress["project"] == "my-app"
        assert "status" in progress
        assert "completion_score" in progress
        assert "total_progress" in progress
        assert "next_steps" in progress

    def test_summarize_progress_interrupted(self):
        """测试中断会话的进度总结"""
        # Given: 中断的会话（用户最后一条是问题）
        messages = [
            Message(
                id="msg-001",
                role=Role.USER,
                content="如何实现登录？",
                timestamp=datetime.now(),
            )
        ]
        conversation = Conversation(
            id="session-002",
            title="登录功能",
            messages=messages,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            project="my-app",
        )

        # When: 总结进度
        progress = summarize_progress(conversation)

        # Then: 状态为 interrupted
        assert progress["status"] == "interrupted"
        assert "恢复中断的工作" in progress["next_steps"]
