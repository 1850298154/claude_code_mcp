# ============================================================================
# 文件: src/academic/scholar/extract_metadata.py
# 描述: 提取元数据函数
#
# 上游依赖:
#   - academic/types.py                        (Paper)
#   - academic/semantic/client.py               (SemanticScholarClient)
#
# 下游封装:
#   - academic/scholar.py                     (Scholar.extract_metadata)
#
# Bash 快速定位:
#   find . -name "extract_metadata.py" -path "*/scholar/*"
# ============================================================================

from typing import List

from academic.types import Paper
from academic.semantic.client import SemanticScholarClient


def extract_metadata(
    client: SemanticScholarClient, paper_ids: List[str]
) -> List[Paper]:
    """批量提取元数据

    Args:
        client: SemanticScholarClient 客户端
        paper_ids: 论文 ID 列表

    Returns:
        论文元数据列表
    """
    papers = []

    for paper_id in paper_ids:
        paper_data = client.get_paper(paper_id)
        if paper_data:
            paper = Paper(
                paper_id=paper_data.get("paperId", ""),
                title=paper_data.get("title", ""),
                authors=[a.get("name", "") for a in paper_data.get("authors", [])],
                year=paper_data.get("year"),
                abstract=paper_data.get("abstract"),
                url=paper_data.get("url"),
                citations=paper_data.get("citationCount"),
                venue=paper_data.get("venue"),
            )
            papers.append(paper)

    return papers
