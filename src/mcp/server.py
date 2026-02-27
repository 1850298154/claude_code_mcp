# ============================================================================
# 文件: src/mcp/server.py
# 描述: MCPServer 类定义，用于 MCP 服务器实现
#
# 上游依赖:
#   - claude_meta/reader                    (ClaudeMetaReader)
#   - academic/scholar                        (Scholar)
#   - vision/analyzer                       (VisionAnalyzer)
#   - graphrag/builder                       (GraphBuilder)
#   - graphrag/qa.qa_system                 (QASystem)
#
# 下游封装:
#   - server/*                                 (操作函数)
#   - mcp/tools/*                             (MCP 工具封装)
#
# Bash 快速定位:
#   find . -name "server.py" -path "*/mcp/*"
# ============================================================================

from typing import Dict, Any, List
import json
import asyncio

from claude_meta.reader import ClaudeMetaReader
from academic.scholar import Scholar
from vision.analyzer import VisionAnalyzer
from graphrag.builder import GraphBuilder
from graphrag.qa.qa_system import QASystem


class MCPServer:
    """MCP Server - MCP 服务器实现

    将所有功能模块暴露为 MCP 工具。
    """

    def __init__(self):
        """初始化 Server"""
        self._claude_meta_reader: ClaudeMetaReader | None = None
        self._scholar: Scholar | None = None
        self._vision_analyzer: VisionAnalyzer | None = None
        self._graph_builder: GraphBuilder | None = None
        self._qa_system: QASystem | None = None

    def get_tools(self) -> List[Dict[str, Any]]:
        """获取可用工具列表

        Returns:
            工具定义列表
        """
        return [
            {
                "name": "claude_meta_get_sessions",
                "description": "获取所有 Claude 会话",
                "inputSchema": {"type": "object"},
            },
            {
                "name": "claude_meta_get_chat_history",
                "description": "获取指定会话的聊天历史",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "session_id": {"type": "string"},
                        "project": {"type": "string"},
                    },
                },
            },
            {
                "name": "claude_meta_get_memory",
                "description": "获取记忆内容",
                "inputSchema": {"type": "object"},
            },
            {
                "name": "academic_search_papers",
                "description": "搜索学术论文",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "limit": {"type": "integer"},
                    },
                },
            },
            {
                "name": "vision_analyze_image",
                "description": "分析图像",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "image_path": {"type": "string"},
                        "prompt": {"type": "string"},
                    },
                },
            },
            {
                "name": "graphrag_build_from_project",
                "description": "从项目构建知识图谱",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "project_path": {"type": "string"},
                    },
                },
            },
            {
                "name": "graphrag_ask",
                "description": "基于知识图谱问答",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "question": {"type": "string"},
                    },
                },
            },
        ]

    def call_tool(self, tool_name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        """调用工具

        Args:
            tool_name: 工具名称
            args: 工具参数

        Returns:
            工具执行结果
        """
        if tool_name == "claude_meta_get_sessions":
            return {"sessions": self._claude_meta_reader.get_sessions()}
        elif tool_name == "claude_meta_get_chat_history":
            session_id = args.get("session_id")
            project = args.get("project")
            return {"messages": self._claude_meta_reader.get_chat_history(session_id, project)}
        elif tool_name == "claude_meta_get_memory":
            return {"memory": self._claude_meta_reader.get_memory()}
        elif tool_name == "academic_search_papers":
            query = args.get("query", "")
            limit = args.get("limit", 10)
            return {"papers": self._scholar.search_papers(query, limit)}
        elif tool_name == "vision_analyze_image":
            image_path = args.get("image_path", "")
            prompt = args.get("prompt", "")
            result = self._vision_analyzer.analyze_image(image_path, prompt)
            return {"description": result.description}
        elif tool_name == "graphrag_ask":
            question = args.get("question", "")
            answer = self._qa_system.ask(question)
            return {"answer": answer.answer, "confidence": answer.confidence}
        else:
            return {"error": f"Unknown tool: {tool_name}"}

    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """处理 MCP 请求

        Args:
            request: MCP 请求

        Returns:
            MCP 响应
        """
        method = request.get("method")
        params = request.get("params", {})

        try:
            result = self.call_tool(method, params)
            return {"result": result}
        except Exception as e:
            return {"error": str(e)}
