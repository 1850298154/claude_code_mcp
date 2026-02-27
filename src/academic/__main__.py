# ============================================================================
# 文件: src/academic/__main__.py
# 描述: Academic 模块主入口
#
# Bash 快速定位:
#   find src -name "__main__.py" -path "*/academic/*"
# ============================================================================

"""Academic 模块主入口"""

from academic.scholar import Scholar


def main():
    """主函数"""
    scholar = Scholar(api_key=None)

    # 搜索论文示例
    print("Academic Module - Example Usage")
    print("=" * 50)
    print("\nSearching for papers about 'machine learning'...")
    papers = scholar.search_papers("machine learning", limit=3)
    for paper in papers:
        print(f"\n  {paper.title}")
        print(f"  Authors: {', '.join(paper.authors)}")
        if paper.year:
            print(f"  Year: {paper.year}")


if __name__ == "__main__":
    main()
