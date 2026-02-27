# ============================================================================
# 文件: src/graphrag/builder/query_graph.py
# 描述: 查询图谱函数
#
# 上游依赖:
#   - graphrag/types.py                       (Graph, Entity, Relation)
#
# 下游封装:
#   - graphrag/builder.py                     (GraphBuilder.query_graph)
#
# Bash 快速定位:
#   find . -name "query_graph.py" -path "*/builder/*"
# ============================================================================

from typing import List, Dict, Any

from graphrag.types import Graph


def query_graph(graph: Graph, query: str) -> List[Dict[str, Any]]:
    """查询图谱

    Args:
        graph: 知识图谱
        query: 查询语句

    Returns:
        查询结果
    """
    results = []

    # 简单的实体匹配查询
    for entity in graph.entities:
        if query.lower() in entity.name.lower():
            results.append({
                "type": "entity",
                "id": entity.id,
                "name": entity.name,
                "description": entity.description,
            })

    # 简单的关系匹配查询
    for relation in graph.relations:
        if query.lower() in relation.type.lower():
            results.append({
                "type": "relation",
                "id": relation.id,
                "source": relation.source_id,
                "target": relation.target_id,
            })

    return results
