# ============================================================================
# 文件: examples/full_example.py
# 描述: 综合使用示例
#
# Bash 快速定位:
#   find . -name "full_example.py"
# ============================================================================

"""
综合使用示例

演示如何组合使用各个模块完成复杂任务。
"""

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.reader import ClaudeMetaReader
from academic.scholar import Scholar
from vision.analyzer import VisionAnalyzer
from vision.types import ModelType, ModelConfig
from graphrag.builder import GraphBuilder
from graphrag.qa import QASystem
from utils.file_ops import FileOps
from utils.string_ops import StringOps


def main():
    """主函数 - 综合示例"""
    print("Claude Code MCP Toolkit - Full Example")
    print("=" * 60)

    # 1. Claude Meta - 读取会话信息
    print("\n1. Claude Meta - 读取会话信息")
    print("-" * 40)
    try:
        paths = ClaudeMetaPaths()
        reader = ClaudeMetaReader(paths)
        sessions = reader.get_sessions()
        print(f"   找到 {len(sessions)} 个会话")
    except Exception as e:
        print(f"   无法读取会话: {e}")

    # 2. Academic - 搜索论文
    print("\n2. Academic - 搜索论文")
    print("-" * 40)
    scholar = Scholar(api_key=None)
    print("   搜索 'machine learning' 相关论文...")
    papers = scholar.search_papers("machine learning", limit=3)
    print(f"   找到 {len(papers)} 篇论文")
    for i, paper in enumerate(papers[:2], 1):
        print(f"   {i}. {paper.title[:50]}...")

    # 3. Vision - 图像分析
    print("\n3. Vision - 图像分析")
    print("-" * 40)
    config = ModelConfig(model_type=ModelType.GLM4V, api_key=None)
    analyzer = VisionAnalyzer(config)
    print("   可用的视觉分析功能:")
    print("   - analyze_image(): 分析图像内容")
    print("   - detect_objects(): 检测图像中的对象")
    print("   - extract_text(): 提取图像中的文本 (OCR)")
    print("   - describe_scene(): 描述图像场景")
    print("   - compare_images(): 比较两幅图像")

    # 4. GraphRAG - 知识图谱和问答
    print("\n4. GraphRAG - 知识图谱和问答")
    print("-" * 40)
    builder = GraphBuilder()
    print("   GraphBuilder 功能:")
    print("   - build_from_project(): 从项目构建知识图谱")
    print("   - add_entity(): 添加实体到图谱")
    print("   - add_relation(): 添加关系到图谱")
    print("   - query_graph(): 查询图谱")

    # 5. Utils - 文件和字符串操作
    print("\n5. Utils - 文件和字符串操作")
    print("-" * 40)
    print("   FileOps 功能:")
    print("   - read(): 读取文件")
    print("   - write(): 写入文件")
    print("   - list_dir(): 列出目录")
    print("   - find_files(): 查找文件")
    print("\n   StringOps 功能:")
    print("   - truncate(): 截断字符串")
    print("   - escape(): 转义特殊字符")
    print("   - format(): 格式化字符串")

    # 示例：字符串操作
    long_text = "这是一个很长的字符串，需要被截断"
    truncated = StringOps.truncate(long_text, max_length=15)
    print(f"\n   截断示例: '{truncated}'")

    formatted = StringOps.format("HelloWorld", style="snake_case")
    print(f"   格式化示例: '{formatted}'")

    # 示例：文件操作
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        test_file = f.name
        FileOps.write(test_file, "Hello from Claude Code MCP Toolkit!")
        content = FileOps.read(test_file)
        print(f"\n   文件操作示例: 写入并读取 '{content}'")

    print("\n" + "=" * 60)
    print("示例完成！")


if __name__ == "__main__":
    main()
