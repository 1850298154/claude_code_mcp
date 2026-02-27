# ============================================================================
# 文件: src/mcp/server.py
# 描述: MCPServer 类定义，用于 MCP 服务器实现
#
# 上游依赖:
#   - mcp/tools/*                             (MCP 工具定义)
#   - claude_meta/reader                    (ClaudeMetaReader)
#   - academic/scholar                        (Scholar)
#   - vision/analyzer                       (VisionAnalyzer)
#   - graphrag/builder                       (GraphBuilder)
#   - graphrag/qa.qa_system                 (QASystem)
#
# 下游封装:
#   - mcp/cli.py                               (CLI 入口)
#   - mcp/transport/stdio.py                   (传输层)
#
# Bash 快速定位:
#   find . -name "server.py" -path "*/mcp/*"
# ============================================================================

from typing import Dict, Any, List, Optional
import json
import asyncio

from mcp.tools import get_all_tools
from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.reader import ClaudeMetaReader
from academic.scholar import Scholar
from vision.analyzer import VisionAnalyzer
from vision.types import ModelType, ModelConfig
from graphrag.builder import GraphBuilder
from graphrag.qa import QASystem


class MCPServer:
    """MCP Server - MCP 服务器实现

    将所有功能模块暴露为 MCP 工具。
    """

    def __init__(self):
        """初始化 Server"""
        self._claude_meta_reader: Optional[ClaudeMetaReader] = None
        self._scholar: Optional[Scholar] = None
        self._vision_analyzer: Optional[VisionAnalyzer] = None
        self._graph_builder: Optional[GraphBuilder] = None
        self._qa_system: Optional[QASystem] = None
        self._running: bool = False

    def _init_modules(self):
        """延迟初始化各功能模块"""
        if self._claude_meta_reader is None:
            try:
                paths = ClaudeMetaPaths()
                self._claude_meta_reader = ClaudeMetaReader(paths)
            except Exception:
                pass  # ~/.claude 可能不存在

        if self._scholar is None:
            self._scholar = Scholar(api_key=None)  # 使用默认 API key

        if self._vision_analyzer is None:
            config = ModelConfig(model_type=ModelType.GLM4V, api_key=None)
            self._vision_analyzer = VisionAnalyzer(config)

        if self._graph_builder is None:
            self._graph_builder = GraphBuilder()

        if self._qa_system is None:
            from graphrag.types import Graph
            self._qa_system = QASystem(Graph())

    def get_tools(self) -> List[Dict[str, Any]]:
        """获取可用工具列表

        Returns:
            工具定义列表
        """
        return [tool.model_dump() for tool in get_all_tools()]

    def call_tool(self, tool_name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        """调用工具

        Args:
            tool_name: 工具名称
            args: 工具参数

        Returns:
            工具执行结果
        """
        self._init_modules()

        # Claude Meta 工具
        if tool_name == "get_sessions":
            return {"sessions": self._claude_meta_reader.get_sessions()}
        elif tool_name == "get_chat_history":
            session_id = args.get("session_id")
            return {"messages": self._claude_meta_reader.get_chat_history(session_id)}
        elif tool_name == "get_memory":
            return {"memory": self._claude_meta_reader.get_memory()}
        elif tool_name == "restore_session":
            session_id = args.get("session_id")
            return {"restored": self._claude_meta_reader.restore_session(session_id)}
        elif tool_name == "get_project_context":
            project_name = args.get("project_name")
            return {"context": self._claude_meta_reader.get_project_context(project_name)}

        # Academic 工具
        elif tool_name == "search_papers":
            query = args.get("query", "")
            limit = args.get("limit", 10)
            year = args.get("year")
            return {"papers": self._scholar.search_papers(query, limit, year)}
        elif tool_name == "get_bibtex":
            paper_id = args.get("paper_id")
            return {"bibtex": self._scholar.get_bibtex(paper_id)}
        elif tool_name == "get_abstract":
            paper_id = args.get("paper_id")
            return {"abstract": self._scholar.get_abstract(paper_id)}
        elif tool_name == "verify_citations":
            bibtex = args.get("bibtex", "")
            return {"verified": self._scholar.verify_citations(bibtex)}

        # Vision 工具
        elif tool_name == "analyze_image":
            image_path = args.get("image_path", "")
            prompt = args.get("prompt", "")
            return {"description": self._vision_analyzer.analyze_image(image_path, prompt)}
        elif tool_name == "detect_objects":
            image_path = args.get("image_path", "")
            return {"objects": self._vision_analyzer.detect_objects(image_path)}
        elif tool_name == "extract_text":
            image_path = args.get("image_path", "")
            return {"text": self._vision_analyzer.extract_text(image_path)}
        elif tool_name == "describe_scene":
            image_path = args.get("image_path", "")
            return {"description": self._vision_analyzer.describe_scene(image_path)}
        elif tool_name == "compare_images":
            image1_path = args.get("image1_path", "")
            image2_path = args.get("image2_path", "")
            return {"comparison": self._vision_analyzer.compare_images(image1_path, image2_path)}

        # GraphRAG 工具
        elif tool_name == "build_graph":
            project_path = args.get("project_path", "")
            return {"graph": self._graph_builder.build_from_project(project_path)}
        elif tool_name == "add_entity":
            entity_id = args.get("entity_id")
            entity_name = args.get("entity_name")
            entity_type = args.get("entity_type")
            from graphrag.types import EntityType, Entity
            entity = Entity(id=entity_id, name=entity_name, type=EntityType(entity_type))
            from graphrag.types import Graph
            self._graph_builder.add_entity(Graph(), entity)
            return {"added": entity_id}
        elif tool_name == "add_relation":
            relation_id = args.get("relation_id")
            source_id = args.get("source_id")
            target_id = args.get("target_id")
            relation_label = args.get("relation_label")
            from graphrag.types import Relation, Graph
            relation = Relation(id=relation_id, source=source_id, target=target_id, label=relation_label)
            self._graph_builder.add_relation(Graph(), relation)
            return {"added": relation_id}
        elif tool_name == "query_graph":
            entity_id = args.get("entity_id")
            entity_name = args.get("entity_name")
            entity_type = args.get("entity_type")
            from graphrag.types import Graph
            return {"results": self._graph_builder.query_graph(Graph(), entity_id, entity_name, entity_type)}
        elif tool_name == "ask_question":
            question = args.get("question", "")
            answer = self._qa_system.ask(question)
            return {"answer": answer.answer, "confidence": answer.confidence}

        # Utils 工具
        elif tool_name == "file_read":
            file_path = args.get("file_path", "")
            from utils.file_ops import FileOps
            return {"content": FileOps.read(file_path)}
        elif tool_name == "file_write":
            file_path = args.get("file_path", "")
            content = args.get("content", "")
            from utils.file_ops import FileOps
            FileOps.write(file_path, content)
            return {"written": file_path}
        elif tool_name == "file_list_dir":
            directory = args.get("directory", "")
            recursive = args.get("recursive", False)
            from utils.file_ops import FileOps
            return {"items": FileOps.list_dir(directory, recursive)}
        elif tool_name == "file_find":
            directory = args.get("directory", "")
            pattern = args.get("pattern", "*")
            recursive = args.get("recursive", True)
            from utils.file_ops import FileOps
            return {"files": FileOps.find_files(directory, pattern, recursive)}
        elif tool_name == "string_truncate":
            text = args.get("text", "")
            max_length = args.get("max_length", 100)
            ellipsis = args.get("ellipsis", "...")
            from utils.string_ops import StringOps
            return {"truncated": StringOps.truncate(text, max_length, ellipsis)}
        elif tool_name == "string_format":
            text = args.get("text", "")
            style = args.get("style", "")
            from utils.string_ops import StringOps
            return {"formatted": StringOps.format(text, style)}

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

    async def serve(self, transport):
        """启动 MCP 服务器

        Args:
            transport: 传输层对象
        """
        self._running = True
        print("MCP Server started", flush=True)

        while self._running:
            try:
                # 读取请求
                line = await transport.read_line()
                if not line:
                    break

                request = json.loads(line)

                # 处理请求
                if request.get("method") == "initialize":
                    response = {
                        "jsonrpc": "2.0",
                        "id": request.get("id"),
                        "result": {
                            "protocolVersion": "2024-11-05",
                            "serverInfo": {
                                "name": "claude-code-mcp",
                                "version": "0.1.0"
                            },
                            "capabilities": {
                                "tools": {"listChanged": True}
                            }
                        }
                    }
                    await transport.write_line(json.dumps(response))

                elif request.get("method") == "tools/list":
                    response = {
                        "jsonrpc": "2.0",
                        "id": request.get("id"),
                        "result": {"tools": self.get_tools()}
                    }
                    await transport.write_line(json.dumps(response))

                elif request.get("method") == "tools/call":
                    tool_name = request.get("params", {}).get("name")
                    args = request.get("params", {}).get("arguments", {})
                    result = self.call_tool(tool_name, args)
                    response = {
                        "jsonrpc": "2.0",
                        "id": request.get("id"),
                        "result": result
                    }
                    await transport.write_line(json.dumps(response))

            except json.JSONDecodeError:
                continue
            except Exception as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "id": request.get("id"),
                    "error": {
                        "code": -32603,
                        "message": str(e)
                    }
                }
                await transport.write_line(json.dumps(error_response))

    def stop(self):
        """停止服务器"""
        self._running = False
