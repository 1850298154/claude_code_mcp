# ============================================================================
# 文件: test/integration/test_claude_meta_full.py
# 描述: ClaudeMeta 完整流程集成测试
#
# 测试对象: claude_meta 模块完整流程
#
# Bash 快速定位: find test -name "test_claude_meta_full.py"
# ============================================================================

import pytest

from claude_meta.reader import ClaudeMetaReader


class TestClaudeMetaFull:
    """ClaudeMeta 完整流程集成测试"""

    def test_full_workflow(self, mock_claude_dir):
        """测试完整工作流"""
        # Given: ClaudeMetaReader
        reader = ClaudeMetaReader(mock_claude_dir)

        # When: 获取所有会话
        sessions = reader.get_sessions()

        # Then: 会话数量正确
        assert len(sessions) >= 1

        # When: 恢复第一个会话
        session = reader.restore_session(sessions[0].id, sessions[0].project)

        # Then: 会话正确
        assert session is not None
        assert session.id == sessions[0].id

        # When: 获取聊天历史
        messages = reader.get_chat_history(session.id, session.project)

        # Then: 消息数量正确
        assert len(messages) >= 1

        # When: 获取项目上下文
        context = reader.get_project_context(session.project)

        # Then: 上下文正确
        assert context["project_name"] == session.project
        assert context["total_sessions"] >= 1

        # When: 获取记忆
        memory = reader.get_memory()

        # Then: 记忆不为空
        assert len(memory) > 0

    def test_detect_and_summarize_interrupted(self, mock_claude_dir):
        """测试检测和总结中断会话"""
        # Given: ClaudeMetaReader
        reader = ClaudeMetaReader(mock_claude_dir)

        # When: 检测中断的会话
        interrupted = reader.detect_interrupted()

        # Then: 返回列表
        assert isinstance(interrupted, list)

        # If: 有中断的会话
        if interrupted:
            # When: 总结进度
            progress = reader.summarize_progress(interrupted[0].id, interrupted[0].project)

            # Then: 进度总结正确
            assert progress is not None
            assert "session_id" in progress
            assert "status" in progress
