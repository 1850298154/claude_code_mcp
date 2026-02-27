# ============================================================================
# 文件: examples/academic_usage.py
# 描述: Academic 使用示例
#
# Bash 快速定位:
#   find . -name "academic_usage.py"
# ============================================================================

"""
Academic 模块使用示例

演示如何使用 Scholar 进行学术论文搜索。
"""

from academic.scholar import Scholar


def main():
    """主函数"""
    print("Academic Module Usage Example")
    print("=" * 50)

    # 初始化 Scholar（无 API key，仅演示）
    scholar = Scholar(api_key=None)

    # 搜索论文
    print("\n1. 搜索论文")
    papers = scholar.search_papers("machine learning", limit=5)

    for i, paper in enumerate(papers):
        print(f"   {i+1}. {paper.title}")
        print(f"      作者: {', '.join(paper.authors)}")
        if paper.year:
            print(f"      年份: {paper.year}")

    # 获取 BibTeX
    print(f"\n2. 获取 BibTeX")
    bibtex = scholar.get_bibtex("123")  # 使用论文 ID
    if bibtex:
        print(f"   BibTeX:\n{bibtex}")
    else:
        print("   论文不存在")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
