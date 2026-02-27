# ============================================================================
# 文件: test/unit/graphrag/builder/test_add_entity.py
# 描述: 测试 add_entity 函数
#
# 测试对象: graphrag/builder/add_entity.py
#
# Bash 快速定位:
#   find test -name "test_add_entity.py"
# ============================================================================

import pytest

from graphrag.types import EntityType, Entity, Graph
from graphrag.builder.add_entity import add_entity


class TestAddEntity:
    """测试 add_entity 函数"""

    def test_add_entity_to_empty_graph(self):
        """测试向空图添加实体"""
        # Given: 空图和新实体
        graph = Graph()
        entity = Entity(
            id="entity1",
            name="Python",
            type=EntityType.LANGUAGE
        )

        # When: 添加实体
        add_entity(graph, entity)

        # Then: 实体被添加
        assert len(graph.entities) == 1
        assert graph.entities["entity1"].name == "Python"

    def test_add_entity_to_existing_graph(self):
        """测试向现有图添加实体"""
        # Given: 有实体的图
        graph = Graph()
        entity1 = Entity(id="e1", name="Java", type=EntityType.LANGUAGE)
        graph.entities["e1"] = entity1

        entity2 = Entity(id="e2", name="Python", type=EntityType.LANGUAGE)

        # When: 添加新实体
        add_entity(graph, entity2)

        # Then: 两个实体都在图中
        assert len(graph.entities) == 2
        assert "e1" in graph.entities
        assert "e2" in graph.entities

    def test_add_entity_duplicate(self):
        """测试添加重复实体"""
        # Given: 图中已有实体
        graph = Graph()
        entity = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        graph.entities["e1"] = entity

        # When: 添加重复 ID 的实体（应该更新）
        entity_updated = Entity(id="e1", name="Python 3.10", type=EntityType.LANGUAGE)
        add_entity(graph, entity_updated)

        # Then: 实体被更新
        assert len(graph.entities) == 1
        assert graph.entities["e1"].name == "Python 3.10"
