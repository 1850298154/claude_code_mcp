# ============================================================================
# 文件: src/academic/scholar/search_papers.py
# 描述: 搜索论文函数
#
# 上游依赖:
#   - academic/types.py                        (Paper)
#   - academic/semantic/client.py               (SemanticScholarClient)
#
# 下游封装:
#   - academic/scholar.py                     (Scholar.search_papers)
#
# Bash 快速定位:
#   find . -name "search_papers.py" -path "*/scholar/*"
# ============================================================================

from typing import List

from academic.types import Paper
from academic.semantic.client import SemanticScholarClient


def search_papers(
    client: SemanticScholarClient,
    query: str,
    limit: int = 10,
    year: int | None = None,
) -> List[Paper]:
    """搜索论文

    Args:
        client: SemanticScholarClient 客户端
        query: 搜索查询
        limit: 返回结果数量
        year: 年份筛选

    Returns:
        论文列表
    """
    results = client.search_papers(query, limit=limit, year=year)
    papers = []

    for result in results:
        paper = Paper(
            paper_id=result.get("paperId", ""),
            title=result.get("title", ""),
            authors=[a.get("name", "") for a in result.get("authors", [])],
            year=result.get("year"),
            abstract=result.get("abstract"),
            url=result.get("url"),
            citations=result.get("citationCount"),
            venue=result.get("venue"),
        )
        papers.append(paper)

    return papers
