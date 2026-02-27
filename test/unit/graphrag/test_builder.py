# ============================================================================
# 文件: test/unit/graphrag/test_builder.py
# 描述: 测试 GraphBuilder 类
#
# 测试对象: graphrag/builder.py
#
# Bash 快速定位:
#   find test -name "test_builder.py" -path "*/graphrag/*"
# ============================================================================

import pytest
from pathlib import Path

from graphrag.builder import GraphBuilder
from graphrag.types import EntityType, Entity, Graph


class TestGraphBuilder:
    """测试 GraphBuilder 类"""

    def test_graph_builder_init(self):
        """测试 GraphBuilder 初始化"""
        # When: 创建 GraphBuilder
        builder = GraphBuilder()

        # Then: 初始化成功
        assert builder is not None

    def test_graph_builder_build_from_project_delegates(self):
        """测试 build_from_project 委托"""
        # Given: GraphBuilder
        builder = GraphBuilder()

        # When: 构建图（模拟目录不存在）
        graph = builder.build_from_project("/nonexistent/path")

        # Then: 返回图结构
        assert isinstance(graph, Graph)

    def test_graph_builder_add_entity_delegates(self):
        """测试 add_entity 委托"""
        # Given: GraphBuilder 和实体
        builder = GraphBuilder()
        entity = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        graph = Graph()

        # When: 添加实体
        builder.add_entity(graph, entity)

        # Then: 实体被添加
        assert "e1" in graph.entities

    def test_graph_builder_add_relation_delegates(self):
        """测试 add_relation 委托"""
        # Given: GraphBuilder 和关系
        builder = GraphBuilder()
        from graphrag.types import Relation
        relation = Relation(id="r1", source="e1", target="e2", label="related_to")
        graph = Graph()

        # When: 添加关系
        builder.add_relation(graph, relation)

        # Then: 关系被添加
        assert len(graph.relations) == 1

    def test_graph_builder_query_graph_delegates(self):
        """测试 query_graph 委托"""
        # Given: GraphBuilder 和图
        builder = GraphBuilder()
        entity = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        graph = Graph()
        graph.entities["e1"] = entity

        # When: 查询图
        results = builder.query_graph(graph, entity_name="Python")

        # Then: 返回正确结果
        assert len(results) >= 1
        assert results[0].name == "Python"
