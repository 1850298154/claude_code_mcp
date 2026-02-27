# ============================================================================
# 文件: src/academic/scholar/get_bibtex.py
# 描述: 获取 BibTeX 函数
#
# 上游依赖:
#   - academic/types.py                        (Paper)
#   - academic/semantic/client.py               (SemanticScholarClient)
#
# 下游封装:
#   - academic/scholar.py                     (Scholar.get_bibtex)
#
# Bash 快速定位:
#   find . -name "get_bibtex.py" -path "*/scholar/*"
# ============================================================================

from typing import Optional

from academic.semantic.client import SemanticScholarClient


def get_bibtex(client: SemanticScholarClient, paper_id: str) -> Optional[str]:
    """获取论文的 BibTeX

    Args:
        client: SemanticScholarClient 客户端
        paper_id: 论文 ID

    Returns:
        BibTeX 引用格式字符串
    """
    paper = client.get_paper(paper_id, fields=["paperId", "title", "bibtex"])
    if paper and "bibtex" in paper:
        return paper["bibtex"]
    return None
