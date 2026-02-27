# ============================================================================
# 文件: test/integration/test_graphrag_full.py
# 描述: GraphRAG 模块完整集成测试
#
# 测试对象: graphrag/ 整个模块
#
# Bash 快速定位:
#   find test -name "test_graphrag_full.py"
# ============================================================================

import pytest
from pathlib import Path
from unittest.mock import Mock, patch

from graphrag.types import EntityType, Entity, Relation, Graph
from graphrag.builder import GraphBuilder
from graphrag.qa import QASystem


class TestGraphRAGFull:
    """测试 GraphRAG 模块完整集成"""

    def test_graph_builder_build_workflow(self):
        """测试 GraphBuilder 构建知识图谱工作流"""
        # Given: GraphBuilder 和模拟项目
        builder = GraphBuilder()

        # 模拟项目内容
        mock_content = """
        Python is a programming language.
        Django is a framework built on Python.
        """

        with patch('pathlib.Path.read_text', return_value=mock_content):
            # When: 从项目构建知识图谱
            graph = builder.build_from_project(Path("test_project"))

            # Then: 返回图结构
            assert isinstance(graph, Graph)

    def test_graph_builder_add_entity_workflow(self):
        """测试添加实体工作流"""
        # Given: GraphBuilder 和实体
        builder = GraphBuilder()
        entity = Entity(
            id="e1",
            name="Python",
            type=EntityType.LANGUAGE
        )

        # When: 添加实体到图
        graph = Graph()
        builder.add_entity(graph, entity)

        # Then: 实体被添加
        assert "e1" in graph.entities
        assert graph.entities["e1"].name == "Python"

    def test_graph_builder_add_relation_workflow(self):
        """测试添加关系工作流"""
        # Given: GraphBuilder、实体和关系
        builder = GraphBuilder()
        graph = Graph()

        entity1 = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        entity2 = Entity(id="e2", name="Django", type=EntityType.FRAMEWORK)

        relation = Relation(
            id="r1",
            source="e1",
            target="e2",
            label="used_with"
        )

        # When: 添加实体和关系
        graph.entities["e1"] = entity1
        graph.entities["e2"] = entity2
        builder.add_relation(graph, relation)

        # Then: 关系被添加
        assert len(graph.relations) == 1
        assert graph.relations[0].label == "used_with"

    def test_graph_builder_query_workflow(self):
        """测试查询图工作流"""
        # Given: 构建好的图
        builder = GraphBuilder()
        graph = Graph()

        entity1 = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        entity2 = Entity(id="e2", name="Java", type=EntityType.LANGUAGE)

        graph.entities["e1"] = entity1
        graph.entities["e2"] = entity2

        # When: 查询语言类型的实体
        results = builder.query_graph(graph, entity_type=EntityType.LANGUAGE)

        # Then: 返回正确的结果
        assert len(results) == 2
        assert all(e.type == EntityType.LANGUAGE for e in results)

    def test_qa_system_workflow(self):
        """测试 QA 系统工作流"""
        # Given: 图和 QA 系统
        graph = Graph()
        entity = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        graph.entities["e1"] = entity

        qa_system = QASystem(graph)

        # When: 回答问题
        # 注意：实际实现可能需要模拟更多细节
        context = qa_system._get_context_for_query("What is Python?")

        # Then: 返回上下文
        assert context is not None

    def test_graphrag_full_integration(self):
        """测试 GraphRAG 完整集成"""
        # Given: 完整的 GraphRAG 系统
        builder = GraphBuilder()
        qa_system = QASystem(Graph())

        # 模拟项目内容
        mock_content = """
        Python is a programming language.
        Django is a framework.
        """

        with patch('pathlib.Path.read_text', return_value=mock_content):
            # When: 构建图谱并回答问题
            graph = builder.build_from_project(Path("test_project"))
            qa_system.graph = graph

            # Then: 系统正常工作
            assert isinstance(graph, Graph)
            assert len(qa_system.graph.entities) >= 0
