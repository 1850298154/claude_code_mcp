# ============================================================================
# 文件: src/academic/scholar/verify_citations.py
# 描述: 验证引用函数
#
# 上游依赖:
#   - academic/types.py                        (Citation)
#   - academic/semantic/client.py               (SemanticScholarClient)
#
# 下游封装:
#   - academic/scholar.py                     (Scholar.verify_citations)
#
# Bash 快速定位:
#   find . -name "verify_citations.py" -path "*/scholar/*"
# ============================================================================

import re
from typing import List

from academic.types import Citation
from academic.semantic.client import SemanticScholarClient


def verify_citations(
    client: SemanticScholarClient, bibtex_content: str
) -> List[Citation]:
    """验证引用

    Args:
        client: SemanticScholarClient 客户端
        bibtex_content: BibTeX 内容字符串

    Returns:
        引用验证结果列表
    """
    citations = []
    # 简单的 BibTeX 解析，提取论文 ID
    paper_ids = re.findall(r"@.*?\{(.*?)\}", bibtex_content)

    for paper_id in paper_ids:
        # 验证论文是否存在
        paper = client.get_paper(paper_id.strip())
        citation = Citation(
            paper_id=paper_id.strip(),
            text=f"验证引用 {paper_id}",
            source="bibtex",
            verified=paper is not None,
            mismatches=None,
        )
        citations.append(citation)

    return citations
