# ============================================================================
# 文件: src/academic/semantic/client.py
# 描述: Semantic Scholar API 客户端
#
# 上游依赖: academic/types.py
# 下游封装: scholar/*
#
# Bash 快速定位:
#   find . -name "client.py" -path "*/semantic/*"
# ============================================================================

import httpx
from typing import List, Optional, Dict, Any

from academic.types import Paper


class SemanticScholarClient:
    """Semantic Scholar API 客户端

    提供对 Semantic Scholar API 的访问。
    """

    BASE_URL = "https://api.semanticscholar.org/graph/v1"

    def __init__(self, api_key: Optional[str] = None):
        """初始化客户端

        Args:
            api_key: Semantic Scholar API 密钥（可选）
        """
        self._api_key = api_key
        self._client = httpx.Client(timeout=30.0)

    def _get_headers(self) -> Dict[str, str]:
        """获取请求头

        Returns:
            请求头字典
        """
        headers = {"Content-Type": "application/json"}
        if self._api_key:
            headers["x-api-key"] = self._api_key
        return headers

    def search_papers(
        self,
        query: str,
        limit: int = 10,
        year: Optional[int] = None,
        fields: Optional[List[str]] = None,
    ) -> List[Dict[str, Any]]:
        """搜索论文

        Args:
            query: 搜索查询
            limit: 返回结果数量
            year: 年份筛选
            fields: 返回字段列表

        Returns:
            论文数据列表
        """
        if fields is None:
            fields = [
                "paperId",
                "title",
                "abstract",
                "authors",
                "year",
                "citationCount",
                "openAccessPdf",
                "url",
                "venue",
            ]

        payload = {
            "query": query,
            "limit": limit,
            "fields": fields,
        }

        if year:
            payload["year"] = year

        response = self._client.post(
            f"{self.BASE_URL}/paper/search",
            headers=self._get_headers(),
            json=payload,
        )
        response.raise_for_status()

        data = response.json()
        return data.get("data", [])

    def get_paper(
        self, paper_id: str, fields: Optional[List[str]] = None
    ) -> Optional[Dict[str, Any]]:
        """获取论文详情

        Args:
            paper_id: 论文 ID
            fields: 返回字段列表

        Returns:
            论文数据字典
        """
        if fields is None:
            fields = [
                "paperId",
                "title",
                "abstract",
                "authors",
                "year",
                "citationCount",
                "references",
                "url",
                "venue",
                "bibtex",
            ]

        params = {"fields": ",".join(fields)}

        response = self._client.get(
            f"{self.BASE_URL}/paper/{paper_id}",
            headers=self._get_headers(),
            params=params,
        )
        response.raise_for_status()

        return response.json()

    def get_bibtex(self, paper_id: str) -> Optional[str]:
        """获取论文的 BibTeX

        Args:
            paper_id: 论文 ID

        Returns:
            BibTeX 字符串
        """
        paper = self.get_paper(
            paper_id, fields=["paperId", "title", "bibtex"]
        )
        if paper and "bibtex" in paper:
            return paper["bibtex"]
        return None

    def get_references(self, paper_id: str, limit: int = 100) -> List[str]:
        """获取论文的参考文献

        Args:
            paper_id: 论文 ID
            limit: 返回结果数量

        Returns:
            参考文献 ID 列表
        """
        response = self._client.get(
            f"{self.BASE_URL}/paper/{paper_id}/references",
            headers=self._get_headers(),
            params={"limit": limit},
        )
        response.raise_for_status()

        data = response.json()
        return data.get("data", [])

    def get_citations(self, paper_id: str, limit: int = 100) -> List[str]:
        """获取论文的引用

        Args:
            paper_id: 论文 ID
            limit: 返回结果数量

        Returns:
            引用论文 ID 列表
        """
        response = self._client.get(
            f"{self.BASE_URL}/paper/{paper_id}/citations",
            headers=self._get_headers(),
            params={"limit": limit},
        )
        response.raise_for_status()

        data = response.json()
        return data.get("data", [])

    def close(self):
        """关闭客户端"""
        self._client.close()

    def __enter__(self):
        """支持上下文管理器"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文管理器"""
        self.close()
