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
  - ENABLE_AUDIO: 是否启用 Audio 工具 (默认: false)

客户端配置:
  {"type": "http", "url": "http://localhost:8000/mcp"}
"""

import os
from mcp.server import FastMCP
from .config import (
    HOST, PORT,
    ENABLE_CLAUDE_META,
    ENABLE_ACADEMIC,
    ENABLE_VISION,
    ENABLE_GRAPHRAG,
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
# 模块资源列表定义
# ============================================================================

CLAUDE_META_RESOURCES = [
    "get_sessions - 获取 Claude Code 所有会话列表",
    "get_chat_history - 获取指定会话的聊天历史",
    "get_memory - 获取 Claude Code 的记忆内容",
    "restore_session - 恢复指定会话",
    "get_project_context - 获取指定项目的上下文信息",
]

ACADEMIC_RESOURCES = [
    "search_papers - 搜索学术论文",
    "get_bibtex - 获取论文的 BibTeX 格式引用",
    "get_abstract - 获取论文摘要",
    "verify_citations - 验证 BibTeX 引用",
]

VISION_RESOURCES = [
    "analyze_image - 图片分析（支持多图、OCR、对象检测、场景描述、图片比较）",
]

GRAPHRAG_RESOURCES = [
    "build_graph - 从项目目录构建知识图谱",
    "add_entity - 向知识图谱添加实体",
    "add_relation - 向知识图谱添加关系",
    "query_graph - 查询知识图谱",
    "ask_question - 向知识图谱问答系统提问",
]

AUDIO_RESOURCES = [
    "speak - 文本转语音播报",
]


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
    _vision_client = None

    def _get_vision_client():
        """延迟初始化 Vision Client"""
        global _vision_client
        if _vision_client is None:
            import base64
            from pathlib import Path
            from openai import OpenAI
            from dotenv import load_dotenv

            # 指定.env文件路径（从项目根目录加载）
            env_path = Path(__file__).parent.parent.parent / ".env"
            load_dotenv(env_path)

            ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")
            api_key = ZHIPU_API_KEY  # 从环境变量获取 API Key

            _vision_client = OpenAI(
                api_key=api_key,
                base_url="https://open.bigmodel.cn/api/paas/v4/"
            )
        return _vision_client

    def _encode_image(image_path: str) -> str:
        """将图片编码为base64字符串"""
        import base64
        from pathlib import Path

        img_path = Path(image_path)
        if not img_path.exists():
            raise FileNotFoundError(f"Image not found: {image_path}")

        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')

    @mcp.tool()
    def analyze_image(image_paths: list[str], prompt: str = "请详细描述这张图片的内容") -> str:
        """
        分析图片内容 - 最牛的图片分析工具

        支持单张或多张图片分析，通过prompt控制分析类型：
        - 提取文字: prompt="请提取图片中的所有文字内容"
        - 检测对象: prompt="请检测并列出图片中的所有物体"
        - 描述场景: prompt="请描述这张图片的场景"
        - 比较图片: prompt="请比较这两张图片的区别"
        - 自定义分析: 任何你想要的分析指令

        Args:
            image_paths: 图片文件路径列表（支持一张或多张）
            prompt: 分析提示词，默认为"请详细描述这张图片的内容"

        Returns:
            分析结果
        """
        from json import dumps

        try:
            client = _get_vision_client()

            # 构建消息内容
            content = [{"type": "text", "text": prompt}]

            # 添加所有图片
            for img_path in image_paths:
                img_base64 = _encode_image(img_path)
                content.append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img_base64}"
                    }
                })

            # 调用API
            response = client.chat.completions.create(
                model="glm-4.6v",
                messages=[{"role": "user", "content": content}],
                temperature=0.7
            )

            result = response.choices[0].message.content
            return dumps({
                "success": True,
                "result": result,
                "images": len(image_paths)
            }, ensure_ascii=False)

        except FileNotFoundError as e:
            return dumps({"success": False, "error": str(e)}, ensure_ascii=False)
        except Exception as e:
            return dumps({"success": False, "error": str(e)}, ensure_ascii=False)


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
# Audio 工具
# ============================================================================

if ENABLE_AUDIO:
    _speaker = None

    def _get_speaker():
        """延迟初始化 Speaker"""
        global _speaker
        if _speaker is None:
            from src.audio.speaker import Speaker
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
        from src.audio.speaker import Speaker
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

def _print_module_banner(title: str, resources: list, enabled: bool):
    """打印模块横幅和资源列表"""
    status = "[ON]" if enabled else "[OFF]"
    header = f"\n    ║ {status} {title}"
    print(header)
    for resource in resources:
        print(f"    ║      - {resource}")


def _get_banner_text() -> str:
    """生成启动横幅文本"""
    banner = f"""
    ╔═══════════════════════════════════════════════════════╗
    ║           Claude Code MCP Server                         ║
    ╠═══════════════════════════════════════════════════════╣
    ║  URL: http://{HOST}:{PORT}/mcp                           ║
    ║  SSE: http://{HOST}:{PORT}/sse                           ║
    ╠═══════════════════════════════════════════════════════╣
    ║  已启用模块:                                             ║"""

    # 添加模块横幅
    if ENABLE_CLAUDE_META:
        _print_module_banner("Claude Meta", CLAUDE_META_RESOURCES, True)
    else:
        _print_module_banner("Claude Meta", CLAUDE_META_RESOURCES, False)

    if ENABLE_ACADEMIC:
        _print_module_banner("Academic (Semantic Scholar)", ACADEMIC_RESOURCES, True)
    else:
        _print_module_banner("Academic (Semantic Scholar)", ACADEMIC_RESOURCES, False)

    if ENABLE_VISION:
        _print_module_banner("Vision", VISION_RESOURCES, True)
    else:
        _print_module_banner("Vision", VISION_RESOURCES, False)

    if ENABLE_GRAPHRAG:
        _print_module_banner("GraphRAG", GRAPHRAG_RESOURCES, True)
    else:
        _print_module_banner("GraphRAG", GRAPHRAG_RESOURCES, False)

    if ENABLE_AUDIO:
        _print_module_banner("Audio", AUDIO_RESOURCES, True)
    else:
        _print_module_banner("Audio", AUDIO_RESOURCES, False)

    footer = f"""
    ╚═══════════════════════════════════════════════════════════╝
    """
    return banner + footer


if __name__ == "__main__":
    # 使用streamable-http模式
    mcp.run(transport="streamable-http")
