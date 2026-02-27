# ============================================================================
# 文件: test/unit/mcp/tools/test_tools.py
# 描述: 测试 MCP 工具定义
#
# 测试对象: mcp/tools/*.py
#
# Bash 快速定位:
#   find test -name "test_tools.py" -path "*/mcp/tools/*"
# ============================================================================

import pytest

from mcp.tools import get_all_tools


class TestMCPTools:
    """测试 MCP 工具定义"""

    def test_get_all_tools(self):
        """测试获取所有工具"""
        # When: 获取所有工具
        tools = get_all_tools()

        # Then: 返回非空列表
        assert len(tools) > 0
        # Then: 每个工具有 name 和 description
        for tool in tools:
            assert hasattr(tool, "name")
            assert hasattr(tool, "description")
            assert hasattr(tool, "inputSchema")

    def test_claude_meta_tools_present(self):
        """测试 Claude Meta 工具存在"""
        # Given: 获取所有工具
        tools = get_all_tools()

        # Then: 包含 Claude Meta 工具
        tool_names = [tool.name for tool in tools]
        assert "get_sessions" in tool_names
        assert "get_chat_history" in tool_names
        assert "get_memory" in tool_names

    def test_academic_tools_present(self):
        """测试 Academic 工具存在"""
        # Given: 获取所有工具
        tools = get_all_tools()

        # Then: 包含 Academic 工具
        tool_names = [tool.name for tool in tools]
        assert "search_papers" in tool_names
        assert "get_bibtex" in tool_names
        assert "get_abstract" in tool_names

    def test_vision_tools_present(self):
        """测试 Vision 工具存在"""
        # Given: 获取所有工具
        tools = get_all_tools()

        # Then: 包含 Vision 工具
        tool_names = [tool.name for tool in tools]
        assert "analyze_image" in tool_names
        assert "detect_objects" in tool_names
        assert "extract_text" in tool_names

    def test_graphrag_tools_present(self):
        """测试 GraphRAG 工具存在"""
        # Given: 获取所有工具
        tools = get_all_tools()

        # Then: 包含 GraphRAG 工具
        tool_names = [tool.name for tool in tools]
        assert "build_graph" in tool_names
        assert "add_entity" in tool_names
        assert "query_graph" in tool_names

    def test_utils_tools_present(self):
        """测试 Utils 工具存在"""
        # Given: 获取所有工具
        tools = get_all_tools()

        # Then: 包含 Utils 工具
        tool_names = [tool.name for tool in tools]
        assert "file_read" in tool_names
        assert "file_write" in tool_names
        assert "string_truncate" in tool_names
