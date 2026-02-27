# ============================================================================
# 文件: test/unit/mcp/test_server.py
# 描述: 测试 MCPServer 类
#
# 测试对象: mcp/server.py
#
# Bash 快速定位:
#   find test -name "test_server.py"
# ============================================================================

import pytest
from unittest.mock import Mock

from mcp.server import MCPServer


class TestMCPServer:
    """测试 MCPServer 类"""

    def test_get_tools(self):
        """测试获取工具列表"""
        # Given: MCPServer 实例
        server = MCPServer()

        # When: 获取工具
        tools = server.get_tools()

        # Then: 返回工具列表
        assert isinstance(tools, list)
        assert len(tools) > 0

    def test_call_tool_claude_meta(self):
        """测试调用 ClaudeMeta 工具"""
        # Given: MCPServer 实例
        server = MCPServer()
        server._claude_meta_reader = Mock()
        server._claude_meta_reader.get_sessions.return_value(["session1", "session2"])

        # When: 调用工具
        result = server.call_tool("claude_meta_get_sessions", {})

        # Then: 结果正确
        assert "sessions" in result
        assert len(result["sessions"]) == 2
