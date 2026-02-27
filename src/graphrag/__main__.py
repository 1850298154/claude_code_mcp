# ============================================================================
# 文件: src/graphrag/__main__.py
# 描述: GraphRAG 模块主入口
#
# Bash 快速定位:
#   find src -name "__main__.py" -path "*/graphrag/*"
# ============================================================================

"""GraphRAG 模块主入口"""

from graphrag.builder import GraphBuilder
from graphrag.qa import QASystem


def main():
    """主函数"""
    print("GraphRAG Module - Example Usage")
    print("=" * 50)
    print("\nInitialize GraphBuilder:")
    print("  builder = GraphBuilder()")
    print("  graph = builder.build_from_project('project_path')")
    print("\nInitialize QASystem:")
    print("  qa_system = QASystem(graph)")
    print("  answer = qa_system.ask('What is Python?')")


if __name__ == "__main__":
    main()
