# ============================================================================
# 文件: examples/graphrag_usage.py
# 描述: GraphRAG 使用示例
#
# Bash 快速定位:
#   find . -name "graphrag_usage.py"
# ============================================================================

"""
GraphRAG 模块使用示例

演示如何使用 GraphBuilder 和 QASystem 构建知识图谱和问答系统。
"""

from pathlib import Path
from graphrag.builder import GraphBuilder
from graphrag.qa import QASystem
from graphrag.types import EntityType, Entity, Relation


def main():
    """主函数"""
    print("GraphRAG Module Usage Example")
    print("=" * 50)

    # 初始化 GraphBuilder
    builder = GraphBuilder()

    # 从项目构建知识图谱
    print("\n1. 从项目构建知识图谱")
    print("   graph = builder.build_from_project('project_path')")
    print("   返回: 构建的知识图谱")

    # 手动添加实体
    print("\n2. 添加实体")
    print("   entity = Entity(id='e1', name='Python', type=EntityType.LANGUAGE)")
    print("   builder.add_entity(graph, entity)")
    print("   返回: 实体被添加到图谱")

    # 添加关系
    print("\n3. 添加关系")
    print("   relation = Relation(id='r1', source='e1', target='e2', label='used_with')")
    print("   builder.add_relation(graph, relation)")
    print("   返回: 关系被添加到图谱")

    # 查询图谱
    print("\n4. 查询图谱")
    print("   results = builder.query_graph(graph, entity_type=EntityType.LANGUAGE)")
    print("   返回: 匹配的实体列表")

    # 问答系统
    print("\n5. 问答系统")
    print("   qa_system = QASystem(graph)")
    print("   answer = qa_system.ask('What is Python?')")
    print("   返回: 基于图谱的回答")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
