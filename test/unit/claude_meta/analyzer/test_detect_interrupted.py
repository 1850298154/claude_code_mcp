# ============================================================================
# 文件: test/unit/claude_meta/analyzer/test_detect_interrupted.py
# 描述: 测试 detect_interrupted 函数
#
# 测试对象: claude_meta/analyzer/detect_interrupted.py
#
# Bash 快速定位: find test -name "test_detect_interrupted.py"
# ============================================================================

import pytest

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.analyzer.detect_interrupted import detect_interrupted


class TestDetectInterrupted:
    """测试 detect_interrupted 函数"""

    def test_detect_interrupted(self, mock_claude_dir):
        """测试检测中断的会话"""
        # Given: 模拟的 ~/.claude 目录
        paths = ClaudeMetaPaths(mock_claude_dir)

        # When: 检测中断的会话
        interrupted = detect_interrupted(paths)

        # Then: 返回列表
        assert isinstance(interrupted, list)

    def test_detect_interrupted_empty(self, temp_dir):
        """测试空目录检测中断"""
        # Given: 空目录
        claude_dir = temp_dir / ".claude"
        claude_dir.mkdir()
        paths = ClaudeMetaPaths(claude_dir)

        # When: 检测中断的会话
        interrupted = detect_interrupted(paths)

        # Then: 结果为空列表
        assert interrupted == []
