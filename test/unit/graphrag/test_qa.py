# ============================================================================
# 文件: test/unit/graphrag/test_qa.py
# 描述: 测试 QASystem 类
#
# 测试对象: graphrag/qa/__init__.py, graphrag/qa/qa_system.py
#
# Bash 快速定位:
#   find test -name "test_qa.py" -path "*/graphrag/*"
# ============================================================================

import pytest

from graphrag.qa import QASystem
from graphrag.types import Graph, Entity, EntityType


class TestQASystem:
    """测试 QASystem 类"""

    def test_qa_system_init(self):
        """测试 QASystem 初始化"""
        # Given: 图
        graph = Graph()

        # When: 创建 QASystem
        qa_system = QASystem(graph)

        # Then: 初始化成功
        assert qa_system is not None

    def test_qa_system_ask(self):
        """测试问答功能"""
        # Given: QASystem 和带实体的图
        graph = Graph()
        entity = Entity(id="e1", name="Python", type=EntityType.LANGUAGE)
        graph.entities["e1"] = entity
        qa_system = QASystem(graph)

        # When: 询问问题
        answer = qa_system.ask("What is Python?")

        # Then: 返回回答
        assert answer is not None
        assert hasattr(answer, "answer")

    def test_qa_system_ask_no_match(self):
        """测试无匹配的问题"""
        # Given: QASystem 和空图
        graph = Graph()
        qa_system = QASystem(graph)

        # When: 询问问题
        answer = qa_system.ask("What is X?")

        # Then: 返回回答（可能为空或默认回答）
        assert answer is not None
