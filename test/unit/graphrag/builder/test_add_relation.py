# ============================================================================
# 文件: test/unit/graphrag/builder/test_add_relation.py
# 描述: 测试 add_relation 函数
#
# 测试对象: graphrag/builder/add_relation.py
#
# Bash 快速定位:
#   find test -name "test_add_relation.py"
# ============================================================================

import pytest

from graphrag.types import EntityType, Entity, Relation, Graph
from graphrag.builder.add_relation import add_relation


class TestAddRelation:
    """测试 add_relation 函数"""

    def test_add_relation_to_empty_graph(self):
        """测试向空图添加关系"""
        # Given: 空图和关系
        graph = Graph()
        relation = Relation(
            id="rel1",
            source="entity1",
            target="entity2",
            label="related_to"
        )

        # When: 添加关系
        add_relation(graph, relation)

        # Then: 关系被添加
        assert len(graph.relations) == 1
        assert graph.relations[0].label == "related_to"

    def test_add_relation_with_entities(self):
        """测试添加关系及对应实体"""
        # Given: 图和关系
        graph = Graph()

        entity1 = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        entity2 = Entity(id="e2", name="Django", type=EntityType.FRAMEWORK)

        relation = Relation(
            id="rel1",
            source="e1",
            target="e2",
            label="used_with"
        )

        # When: 添加实体和关系
        graph.entities["e1"] = entity1
        graph.entities["e2"] = entity2
        add_relation(graph, relation)

        # Then: 关系正确关联
        assert len(graph.relations) == 1
        assert graph.relations[0].source == "e1"
        assert graph.relations[0].target == "e2"

    def test_add_relation_duplicate(self):
        """测试添加重复关系"""
        # Given: 图中已有关系
        graph = Graph()
        relation = Relation(
            id="rel1",
            source="e1",
            target="e2",
            label="related_to"
        )
        graph.relations.append(relation)

        # When: 添加相同 ID 的关系
        relation_duplicate = Relation(
            id="rel1",
            source="e1",
            target="e3",
            label="related_to"
        )
        add_relation(graph, relation_duplicate)

        # Then: 关系被更新
        assert len(graph.relations) == 1
        assert graph.relations[0].target == "e3"
