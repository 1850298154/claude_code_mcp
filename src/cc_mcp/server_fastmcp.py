# ============================================================================
# 文件: src/cc_mcp/server_fastmcp.py
# 描述: 使用 FastMCP 的 MCP 服务器
# ============================================================================

"""
Claude Code MCP Server - 使用官方 FastMCP 实现

启动: python -m cc_mcp

配置: .env 文件或环境变量
  - HOST: 监听地址 (默认: 0.0.0.0)
  - PORT: 监听端口 (默认: 8000)
  - ENABLE_CLAUDE_META: 是否启用 Claude Meta 工具 (默认: true)
  - ENABLE_ACADEMIC: 是否启用 Academic 工具 (默认: true)
  - ENABLE_VISION: 是否启用 Vision 工具 (默认: false)
  - ENABLE_GRAPHRAG: 是否启用 GraphRAG 工具 (默认: false)
  - ENABLE_UTILS: 是否启用 Utils 工具 (默认: true)
  - ENABLE_AUDIO: 是否启用 Audio 工具 (默认: false)

客户端配置:
  {"type": "http", "url": "http://localhost:8000/mcp"}
"""

from mcp.server import FastMCP
from .config import (
    HOST, PORT,
    ENABLE_CLAUDE_META,
    ENABLE_ACADEMIC,
    ENABLE_VISION,
    ENABLE_GRAPHRAG,
    ENABLE_UTILS,
    ENABLE_AUDIO,
)

# 创建 FastMCP 实例
mcp = FastMCP(
    name="claude-code-mcp",
    host=HOST,
    port=PORT,
    sse_path="/sse",
    streamable_http_path="/mcp",
)


# ============================================================================
# Claude Meta 工具
# ============================================================================

if ENABLE_CLAUDE_META:
    def _get_claude_meta_reader():
        """延迟初始化 ClaudeMetaReader"""
        from claude_meta.config.paths import ClaudeMetaPaths
        from claude_meta.reader import ClaudeMetaReader
        try:
            paths = ClaudeMetaPaths()
            return ClaudeMetaReader(paths)
        except Exception:
            return None

    @mcp.tool()
    def get_sessions() -> str:
        """
        获取 Claude Code 所有会话列表

        返回所有可用的会话及其元信息。
        """
        from json import dumps
        reader = _get_claude_meta_reader()
        if not reader:
            return dumps({"error": "Claude Meta not available"}, ensure_ascii=False)
        sessions = reader.get_sessions()
        return dumps({"sessions": sessions}, ensure_ascii=False, indent=2)

    @mcp.tool()
    def get_chat_history(session_id: str) -> str:
        """
        获取指定会话的聊天历史

        Args:
            session_id: 会话 ID

        返回该会话的所有消息历史。
        """
        from json import dumps
        reader = _get_claude_meta_reader()
        if not reader:
            return dumps({"error": "Claude Meta not available"}, ensure_ascii=False)
        messages = reader.get_chat_history(session_id)
        return dumps({"messages": messages}, ensure_ascii=False, indent=2)

    @mcp.tool()
    def get_memory() -> str:
        """
        获取 Claude Code 的记忆内容

        返回所有记忆条目。
        """
        from json import dumps
        reader = _get_claude_meta_reader()
        if not reader:
            return dumps({"error": "Claude Meta not available"}, ensure_ascii=False)
        memory = reader.get_memory()
        return dumps({"memory": memory}, ensure_ascii=False, indent=2)

    @mcp.tool()
    def restore_session(session_id: str) -> str:
        """
        恢复指定会话

        Args:
            session_id: 会话 ID

        将指定会话恢复为当前会话。
        """
        from json import dumps
        reader = _get_claude_meta_reader()
        if not reader:
            return dumps({"error": "Claude Meta not available"}, ensure_ascii=False)
        restored = reader.restore_session(session_id)
        return dumps({"restored": restored}, ensure_ascii=False)

    @mcp.tool()
    def get_project_context(project_name: str) -> str:
        """
        获取指定项目的上下文信息

        Args:
            project_name: 项目名称

        返回项目的会话摘要、文件结构等信息。
        """
        from json import dumps
        reader = _get_claude_meta_reader()
        if not reader:
            return dumps({"error": "Claude Meta not available"}, ensure_ascii=False)
        context = reader.get_project_context(project_name)
        return dumps({"context": context}, ensure_ascii=False, indent=2)


# ============================================================================
# Academic 工具 (Semantic Scholar)
# ============================================================================

if ENABLE_ACADEMIC:
    _scholar = None

    def _get_scholar():
        """延迟初始化 Scholar"""
        global _scholar
        if _scholar is None:
            from academic.scholar_class import Scholar
            _scholar = Scholar(api_key=None)
        return _scholar

    @mcp.tool()
    def search_papers(query: str, limit: int = 10, year: int = None) -> str:
        """
        搜索学术论文

        Args:
            query: 搜索关键词
            limit: 返回结果数量限制 (默认: 10)
            year: 年份过滤 (可选)

        返回搜索到的论文列表。
        """
        from json import dumps
        scholar = _get_scholar()
        papers = scholar.search_papers(query, limit, year)
        return dumps({"papers": papers}, ensure_ascii=False, indent=2)

    @mcp.tool()
    def get_bibtex(paper_id: str) -> str:
        """
        获取论文的 BibTeX 格式引用

        Args:
            paper_id: 论文 ID (S2 API paper ID)

        返回 BibTeX 格式的引用字符串。
        """
        from json import dumps
        scholar = _get_scholar()
        bibtex = scholar.get_bibtex(paper_id)
        return dumps({"bibtex": bibtex}, ensure_ascii=False)

    @mcp.tool()
    def get_abstract(paper_id: str) -> str:
        """
        获取论文摘要

        Args:
            paper_id: 论文 ID

        返回论文的摘要内容。
        """
        from json import dumps
        scholar = _get_scholar()
        abstract = scholar.get_abstract(paper_id)
        return dumps({"abstract": abstract}, ensure_ascii=False)

    @mcp.tool()
    def verify_citations(bibtex: str) -> str:
        """
        验证 BibTeX 引用

        Args:
            bibtex: BibTeX 内容字符串

        验证每条引用是否真实存在，返回验证结果。
        """
        from json import dumps
        scholar = _get_scholar()
        verified = scholar.verify_citations(bibtex)
        return dumps({"verified": verified}, ensure_ascii=False, indent=2)


# ============================================================================
# Vision 工具
# ============================================================================

if ENABLE_VISION:
    _vision_analyzer = None

    def _get_vision_analyzer():
        """延迟初始化 VisionAnalyzer"""
        global _vision_analyzer
        if _vision_analyzer is None:
            from vision.analyzer_class import VisionAnalyzer
            _vision_analyzer = VisionAnalyzer(model="glm4v", api_key=None)
        return _vision_analyzer

    @mcp.tool()
    def analyze_image(image_path: str, prompt: str = "") -> str:
        """
        分析图片内容

        Args:
            image_path: 图片文件路径
            prompt: 分析提示 (可选)

        返回图片的详细描述。
        """
        from json import dumps
        analyzer = _get_vision_analyzer()
        description = analyzer.analyze_image(image_path, prompt)
        return dumps({"description": description}, ensure_ascii=False)

    @mcp.tool()
    def detect_objects(image_path: str) -> str:
        """
        检测图片中的对象

        Args:
            image_path: 图片文件路径

        返回检测到的对象列表。
        """
        from json import dumps
        analyzer = _get_vision_analyzer()
        objects = analyzer.detect_objects(image_path)
        return dumps({"objects": objects}, ensure_ascii=False, indent=2)

    @mcp.tool()
    def extract_text(image_path: str) -> str:
        """
        提取图片中的文本 (OCR)

        Args:
            image_path: 图片文件路径

        返回提取的文本内容。
        """
        from json import dumps
        analyzer = _get_vision_analyzer()
        text = analyzer.extract_text(image_path)
        return dumps({"text": text}, ensure_ascii=False)

    @mcp.tool()
    def describe_scene(image_path: str) -> str:
        """
        描述图片场景

        Args:
            image_path: 图片文件路径

        返回对图片场景的自然语言描述。
        """
        from json import dumps
        analyzer = _get_vision_analyzer()
        description = analyzer.describe_scene(image_path)
        return dumps({"description": description}, ensure_ascii=False)

    @mcp.tool()
    def compare_images(image1_path: str, image2_path: str) -> str:
        """
        比较两张图片

        Args:
            image1_path: 第一张图片路径
            image2_path: 第二张图片路径

        返回两张图片的对比结果。
        """
        from json import dumps
        analyzer = _get_vision_analyzer()
        comparison = analyzer.compare_images(image1_path, image2_path)
        return dumps({"comparison": comparison}, ensure_ascii=False, indent=2)


# ============================================================================
# GraphRAG 工具
# ============================================================================

if ENABLE_GRAPHRAG:
    _graph_builder = None
    _qa_system = None

    def _get_graph_builder():
        """延迟初始化 GraphBuilder"""
        global _graph_builder
        if _graph_builder is None:
            from graphrag.builder_class import GraphBuilder
            _graph_builder = GraphBuilder()
        return _graph_builder

    def _get_qa_system():
        """延迟初始化 QASystem"""
        global _qa_system
        if _qa_system is None:
            from graphrag.qa import QASystem
            from graphrag.types import Graph
            _qa_system = QASystem(Graph(entities=[], relations=[]))
        return _qa_system

    @mcp.tool()
    def build_graph(project_path: str) -> str:
        """
        从项目目录构建知识图谱

        Args:
            project_path: 项目目录路径

        分析代码并构建知识图谱。
        """
        from json import dumps
        builder = _get_graph_builder()
        graph = builder.build_from_project(project_path)
        return dumps({"graph": graph.model_dump() if hasattr(graph, 'model_dump') else str(graph)}, ensure_ascii=False, indent=2)

    @mcp.tool()
    def add_entity(entity_id: str, entity_name: str, entity_type: str) -> str:
        """
        向知识图谱添加实体

        Args:
            entity_id: 实体 ID
            entity_name: 实体名称
            entity_type: 实体类型

        返回添加结果。
        """
        from json import dumps
        from graphrag.types import EntityType, Entity, Graph
        entity = Entity(id=entity_id, name=entity_name, type=EntityType(entity_type))
        builder = _get_graph_builder()
        builder.add_entity(Graph(), entity)
        return dumps({"added": entity_id, "name": entity_name, "type": entity_type}, ensure_ascii=False)

    @mcp.tool()
    def add_relation(relation_id: str, source_id: str, target_id: str, relation_label: str) -> str:
        """
        向知识图谱添加关系

        Args:
            relation_id: 关系 ID
            source_id: 源实体 ID
            target_id: 目标实体 ID
            relation_label: 关系标签

        返回添加结果。
        """
        from json import dumps
        from graphrag.types import Relation, Graph
        relation = Relation(id=relation_id, source=source_id, target=target_id, label=relation_label)
        builder = _get_graph_builder()
        builder.add_relation(Graph(), relation)
        return dumps({"added": relation_id, "source": source_id, "target": target_id, "label": relation_label}, ensure_ascii=False)

    @mcp.tool()
    def query_graph(entity_id: str = None, entity_name: str = None, entity_type: str = None) -> str:
        """
        查询知识图谱

        Args:
            entity_id: 实体 ID (可选)
            entity_name: 实体名称 (可选)
            entity_type: 实体类型 (可选)

        返回查询结果。
        """
        from json import dumps
        builder = _get_graph_builder()
        results = builder.query_graph(None, entity_id, entity_name, entity_type)
        return dumps({"results": results}, ensure_ascii=False, indent=2)

    @mcp.tool()
    def ask_question(question: str) -> str:
        """
        向知识图谱问答系统提问

        Args:
            question: 问题文本

        返回答案和置信度。
        """
        from json import dumps
        qa = _get_qa_system()
        answer = qa.ask(question)
        return dumps({"answer": answer.answer, "confidence": answer.confidence}, ensure_ascii=False)


# ============================================================================
# Utils - File 工具
# ============================================================================

if ENABLE_UTILS:
    @mcp.tool()
    def file_read(file_path: str) -> str:
        """
        读取文件内容

        Args:
            file_path: 文件路径

        返回文件内容。
        """
        from utils.file_ops import FileOps
        from json import dumps
        content = FileOps.read(file_path)
        return dumps({"content": content}, ensure_ascii=False)

    @mcp.tool()
    def file_write(file_path: str, content: str) -> str:
        """
        写入文件内容

        Args:
            file_path: 文件路径
            content: 要写入的内容

        返回写入结果。
        """
        from utils.file_ops import FileOps
        from json import dumps
        FileOps.write(file_path, content)
        return dumps({"written": file_path}, ensure_ascii=False)

    @mcp.tool()
    def file_list_dir(directory: str, recursive: bool = False) -> str:
        """
        列出目录内容

        Args:
            directory: 目录路径
            recursive: 是否递归列出子目录

        返回目录内容列表。
        """
        from utils.file_ops import FileOps
        from json import dumps
        items = FileOps.list_dir(directory, recursive)
        return dumps({"items": items}, ensure_ascii=False, indent=2)

    @mcp.tool()
    def file_find(directory: str, pattern: str = "*", recursive: bool = True) -> str:
        """
        查找文件

        Args:
            directory: 搜索目录
            pattern: 文件匹配模式 (如 "*.py")
            recursive: 是否递归搜索

        返回匹配的文件列表。
        """
        from utils.file_ops import FileOps
        from json import dumps
        files = FileOps.find_files(directory, pattern, recursive)
        return dumps({"files": files}, ensure_ascii=False)

    @mcp.tool()
    def string_truncate(text: str, max_length: int = 100, ellipsis: str = "...") -> str:
        """
        截断字符串

        Args:
            text: 原始文本
            max_length: 最大长度
            ellipsis: 省略符号

        返回截断后的文本。
        """
        from utils.string_ops import StringOps
        from json import dumps
        truncated = StringOps.truncate(text, max_length, ellipsis)
        return dumps({"truncated": truncated}, ensure_ascii=False)

    @mcp.tool()
    def string_format(text: str, style: str) -> str:
        """
        格式化字符串

        Args:
            text: 原始文本
            style: 格式化风格 (如 "upper", "lower", "title", "snake", "camel")

        返回格式化后的文本。
        """
        from utils.string_ops import StringOps
        from json import dumps
        formatted = StringOps.format(text, style)
        return dumps({"formatted": formatted}, ensure_ascii=False)

    @mcp.tool()
    def json_read(file_path: str) -> str:
        """
        读取 JSON 文件

        Args:
            file_path: JSON 文件路径

        返回解析后的数据。
        """
        from utils.json_ops import JsonOps
        from json import dumps
        data = JsonOps.read(file_path)
        return dumps({"data": data}, ensure_ascii=False, indent=2)

    @mcp.tool()
    def json_write(file_path: str, data: str) -> str:
        """
        写入 JSON 文件

        Args:
            file_path: JSON 文件路径
            data: JSON 数据字符串

        返回写入结果。
        """
        from utils.json_ops import JsonOps
        from json import dumps, loads
        parsed_data = loads(data)
        JsonOps.write(file_path, parsed_data)
        return dumps({"written": file_path}, ensure_ascii=False)


# ============================================================================
# Audio 工具
# ============================================================================

if ENABLE_AUDIO:
    _speaker = None

    def _get_speaker():
        """延迟初始化 Speaker"""
        global _speaker
        if _speaker is None:
            from audio.speaker import Speaker
            _speaker = Speaker()
        return _speaker

    @mcp.tool()
    def speak(text: str, async_mode: bool = False) -> str:
        """
        文本转语音播报

        Args:
            text: 要播报的文本
            async_mode: 是否异步播放 (默认: False)

        返回播放结果。
        """
        from audio.speaker import Speaker
        from json import dumps
        speaker = _get_speaker()
        if async_mode:
            success = speaker.speak_async(text)
        else:
            success = speaker.speak(text)
        return dumps({"played": success}, ensure_ascii=False)


# ============================================================================
# 主入口
# ============================================================================

def _get_enabled_modules():
    """获取已启用的模块列表"""
    enabled = []
    if ENABLE_CLAUDE_META:
        enabled.append("Claude Meta")
    if ENABLE_ACADEMIC:
        enabled.append("Academic (Semantic Scholar)")
    if ENABLE_VISION:
        enabled.append("Vision")
    if ENABLE_GRAPHRAG:
        enabled.append("GraphRAG")
    if ENABLE_UTILS:
        enabled.append("Utils")
    if ENABLE_AUDIO:
        enabled.append("Audio")
    return enabled


if __name__ == "__main__":
    enabled_modules = _get_enabled_modules()
    modules_list = "\n    ║    ".join(enabled_modules) if enabled_modules else "    ║    (无)"

    print(f"""
    ╔═══════════════════════════════════════════════════════╗
    ║           Claude Code MCP Server                         ║
    ╠═══════════════════════════════════════════════════════╣
    ║  URL: http://{HOST}:{PORT}/mcp                           ║
    ║  SSE:  http://{HOST}:{PORT}/sse                           ║
    ╠═══════════════════════════════════════════════════════╣
    ║  已启用模块:                                             ║
    ║    {modules_list}                          ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    mcp.run(transport="streamable-http")
