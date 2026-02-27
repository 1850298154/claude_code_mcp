# ============================================================================
# 文件: src/academic/scholar/get_abstract.py
# 描述: 获取摘要函数
#
# 上游依赖:
#   - academic/types.py                        (Paper)
#   - academic/semantic/client.py               (SemanticScholarClient)
#
# 下游封装:
#   - academic/scholar.py                     (Scholar.get_abstract)
#
# Bash 快速定位:
#   find . -name "get_abstract.py" -path "*/scholar/*"
# ============================================================================

from typing import Optional

from academic.semantic.client import SemanticScholarClient


def get_abstract(client: SemanticScholarClient, paper_id: str) -> Optional[str]:
    """获取论文摘要

    Args:
        client: SemanticScholarClient 客户端
        paper_id: 论文 ID

    Returns:
        论文摘要
    """
    paper = client.get_paper(paper_id, fields=["paperId", "abstract"])
    if paper:
        return paper.get("abstract")
    return None
