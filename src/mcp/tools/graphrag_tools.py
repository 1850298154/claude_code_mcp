# ============================================================================
# 文件: src/mcp/tools/graphrag_tools.py
# 描述: GraphRAG MCP 工具定义
#
# 上游依赖: graphrag/builder/, graphrag/qa/
# 下游封装: mcp/server.py
#
# Bash 快速定位:
#   find src -name "graphrag_tools.py" -path "*/mcp/tools/*"
# ============================================================================

"""GraphRAG MCP 工具"""

from mcp.types import Tool


GRAPH_RAG_TOOLS: list[Tool] = [
    Tool(
        name="build_graph",
        description="从项目目录构建知识图谱",
        inputSchema={
            "type": "object",
            "properties": {
                "project_path": {
                    "type": "string",
                    "description": "项目目录路径",
                },
            },
            "required": ["project_path"],
        },
    ),
    Tool(
        name="add_entity",
        description="向知识图谱添加实体",
        inputSchema={
            "type": "object",
            "properties": {
                "entity_id": {
                    "type": "string",
                    "description": "实体 ID",
                },
                "entity_name": {
                    "type": "string",
                    "description": "实体名称",
                },
                "entity_type": {
                    "type": "string",
                    "description": "实体类型（CONCEPT, LANGUAGE, FRAMEWORK, PERSON, FILE）",
                },
            },
            "required": ["entity_id", "entity_name", "entity_type"],
        },
    ),
    Tool(
        name="add_relation",
        description="向知识图谱添加关系",
        inputSchema={
            "type": "object",
            "properties": {
                "relation_id": {
                    "type": "string",
                    "description": "关系 ID",
                },
                "source_id": {
                    "type": "string",
                    "description": "源实体 ID",
                },
                "target_id": {
                    "type": "string",
                    "description": "目标实体 ID",
                },
                "relation_label": {
                    "type": "string",
                    "description": "关系标签",
                },
            },
            "required": ["relation_id", "source_id", "target_id", "relation_label"],
        },
    ),
    Tool(
        name="query_graph",
        description="查询知识图谱",
        inputSchema={
            "type": "object",
            "properties": {
                "entity_id": {
                    "type": "string",
                    "description": "实体 ID",
                },
                "entity_name": {
                    "type": "string",
                    "description": "实体名称",
                },
                "entity_type": {
                    "type": "string",
                    "description": "实体类型",
                },
            },
        },
    ),
    Tool(
        name="ask_question",
        description="基于知识图谱回答问题",
        inputSchema={
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "问题",
                },
            },
            "required": ["question"],
        },
    ),
]


__all__ = ["GRAPH_RAG_TOOLS"]
