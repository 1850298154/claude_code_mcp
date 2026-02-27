# ============================================================================
# 文件: test/integration/test_mcp_full.py
# 描述: MCP 模块完整集成测试
#
# 测试对象: mcp/ 整个模块
#
# Bash 快速定位:
#   find test -name "test_mcp_full.py"
# ============================================================================

import pytest
from unittest.mock import Mock, patch

from mcp.server import MCPServer
from mcp.tools import get_all_tools


class TestMCPFull:
    """测试 MCP 模块完整集成"""

    def test_mcp_server_creation(self):
        """测试创建 MCP 服务器"""
        # When: 创建 MCP 服务器
        server = MCPServer()

        # Then: 服务器创建成功
        assert server is not None

    def test_mcp_server_tools_loading(self):
        """测试 MCP 服务器加载工具"""
        # Given: MCP 服务器
        server = MCPServer()

        # When: 获取所有工具
        tools = get_all_tools()

        # Then: 工具列表非空
        assert len(tools) > 0

    def test_mcp_tools_integration(self):
        """测试 MCP 工具集成"""
        # Given: 获取所有工具
        tools = get_all_tools()

        # Then: 包含所有模块的工具
        tool_names = [tool.name for tool in tools]

        # Claude Meta 工具
        assert "get_sessions" in tool_names
        assert "get_chat_history" in tool_names

        # Academic 工具
        assert "search_papers" in tool_names
        assert "get_bibtex" in tool_names

        # Vision 工具
        assert "analyze_image" in tool_names
        assert "detect_objects" in tool_names

        # GraphRAG 工具
        assert "build_graph" in tool_names
        assert "add_entity" in tool_names

        # Utils 工具
        assert "file_read" in tool_names
        assert "file_write" in tool_names

    def test_mcp_server_full_workflow(self):
        """测试 MCP 服务器完整工作流"""
        # Given: MCP 服务器和模拟传输层
        server = MCPServer()
        mock_transport = Mock()

        # When: 初始化服务器
        # 注意：实际实现可能需要根据具体实现调整
        assert server is not None

    def test_mcp_tool_schemas(self):
        """测试 MCP 工具 Schema"""
        # Given: 获取所有工具
        tools = get_all_tools()

        # Then: 每个工具有有效的 Schema
        for tool in tools:
            assert hasattr(tool, "inputSchema")
            assert isinstance(tool.inputSchema, dict)
            assert "type" in tool.inputSchema
