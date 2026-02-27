# ============================================================================
# 文件: test/unit/graphrag/builder/test_query_graph.py
# 描述: 测试 query_graph 函数
#
# 测试对象: graphrag/builder/query_graph.py
#
# Bash 快速定位:
#   find test -name "test_query_graph.py"
# ============================================================================

import pytest

from graphrag.types import EntityType, Entity, Relation, Graph
from graphrag.builder.query_graph import query_graph


class TestQueryGraph:
    """测试 query_graph 函数"""

    def test_query_graph_by_id(self):
        """测试通过 ID 查询实体"""
        # Given: 有实体的图
        graph = Graph()
        entity = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        graph.entities["e1"] = entity

        # When: 通过 ID 查询
        result = query_graph(graph, entity_id="e1")

        # Then: 返回正确实体
        assert result is not None
        assert result.name == "Python"

    def test_query_graph_by_id_not_found(self):
        """测试查询不存在的 ID"""
        # Given: 有实体的图
        graph = Graph()
        entity = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        graph.entities["e1"] = entity

        # When: 查询不存在的 ID
        result = query_graph(graph, entity_id="e999")

        # Then: 返回 None
        assert result is None

    def test_query_graph_by_name(self):
        """测试通过名称查询实体"""
        # Given: 有实体的图
        graph = Graph()
        entity = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        graph.entities["e1"] = entity

        # When: 通过名称查询
        results = query_graph(graph, entity_name="Python")

        # Then: 返回正确实体
        assert len(results) == 1
        assert results[0].name == "Python"

    def test_query_graph_by_type(self):
        """测试通过类型查询实体"""
        # Given: 有实体的图
        graph = Graph()
        entity1 = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        entity2 = Entity(id="e2", name="Java", type=EntityType.LANGUAGE)
        entity3 = Entity(id="e3", name="Django", type=EntityType.FRAMEWORK)

        graph.entities["e1"] = entity1
        graph.entities["e2"] = entity2
        graph.entities["e3"] = entity3

        # When: 通过类型查询
        results = query_graph(graph, entity_type=EntityType.LANGUAGE)

        # Then: 返回语言类型的实体
        assert len(results) == 2
        assert all(e.type == EntityType.LANGUAGE for e in results)

    def test_query_graph_relations(self):
        """测试查询关系"""
        # Given: 有关系的图
        graph = Graph()
        entity = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        graph.entities["e1"] = entity

        relation = Relation(id="r1", source="e1", target="e2", label="related_to")
        graph.relations.append(relation)

        # When: 查询关系
        results = query_graph(graph, relations=True)

        # Then: 返回关系
        assert len(results) == 1
        assert results[0].label == "related_to"
