# ============================================================================
# 文件: src/academic/scholar.py
# 描述: Scholar 数据结构定义，用于学术搜索与资料获取
#
# 上游依赖:
#   - academic/types.py                       (Paper, Citation)
#   - academic/semantic/client.py              (SemanticScholarClient)
#
# 下游封装:
#   - scholar/search_papers.py                (搜索论文)
#   - scholar/get_bibtex.py                   (获取 BibTeX)
#   - scholar/get_abstract.py                  (获取摘要)
#   - scholar/verify_citations.py                (验证引用)
#   - scholar/extract_metadata.py                (提取元数据)
#
# Bash 快速定位:
#   find . -name "scholar.py" -path "*/academic/*"
# ============================================================================

from typing import List, Optional

from academic.types import Paper, Citation
from academic.semantic.client import SemanticScholarClient


class Scholar:
    """Scholar - 学术搜索与资料获取

    提供论文搜索、BibTeX 获取、引用验证等功能。
    """

    def __init__(self, api_key: Optional[str] = None):
        """初始化 Scholar

        Args:
            api_key: Semantic Scholar API 密钥（可选）
        """
        self._client = SemanticScholarClient(api_key)

    def search_papers(
        self, query: str, limit: int = 10, year: Optional[int] = None
    ) -> List[Paper]:
        """搜索论文

        实现位置: scholar/search_papers.py

        Args:
            query: 搜索查询
            limit: 返回结果数量
            year: 年份筛选

        Returns:
            论文列表
        """
        results = self._client.search_papers(query, limit=limit, year=year)
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

    def get_bibtex(self, paper_id: str) -> Optional[str]:
        """获取 BibTeX

        实现位置: scholar/get_bibtex.py

        Args:
            paper_id: 论文 ID

        Returns:
            BibTeX 引用格式字符串
        """
        return self._client.get_bibtex(paper_id)

    def get_abstract(self, paper_id: str) -> Optional[str]:
        """获取摘要

        实现位置: scholar/get_abstract.py

        Args:
            paper_id: 论文 ID

        Returns:
            论文摘要
        """
        paper = self._client.get_paper(paper_id)
        if paper:
            return paper.get("abstract")
        return None

    def verify_citations(self, bibtex_content: str) -> list[Citation]:
        """验证引用

        实现位置: scholar/verify_citations.py

        Args:
            bibtex_content: BibTeX 内容字符串

        Returns:
            引用验证结果列表
        """
        import re

        # 简单的 BibTeX 解析
        citations = []
        paper_ids = re.findall(r"@.*?\{(.*?)\}", bibtex_content)

        for paper_id in paper_ids:
            # 验证论文是否存在
            paper = self._client.get_paper(paper_id.strip())

            citation = Citation(
                paper_id=paper_id.strip(),
                text=f"验证引用 {paper_id}",
                source="bibtex",
                verified=paper is not None,
                mismatches=None,
            )
            citations.append(citation)

        return citations

    def extract_metadata(self, paper_ids: List[str]) -> List[Paper]:
        """批量提取元数据

        实现位置: scholar/extract_metadata.py

        Args:
            paper_ids: 论文 ID 列表

        Returns:
            论文元数据列表
        """
        papers = []

        for paper_id in paper_ids:
            paper_data = self._client.get_paper(paper_id)
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

    def close(self):
        """关闭客户端"""
        self._client.close()

    def __enter__(self):
        """支持上下文管理器"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文管理器"""
        self.close()
