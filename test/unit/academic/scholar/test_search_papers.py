# ============================================================================
# 文件: test/unit/academic/scholar/test_search_papers.py
# 描述: 测试 search_papers 函数
#
# 测试对象: src/academic/scholar/search_papers.py
#
# Bash 快速定位:
#   find test -name "test_search_papers.py"
# ============================================================================

import pytest
from unittest.mock import Mock, patch

from academic.types import Paper
from academic.semantic.client import SemanticScholarClient
from academic.scholar.search_papers import search_papers


class TestSearchPapers:
    """测试 search_papers 函数"""

    def test_search_papers_basic(self):
        """测试基本论文搜索"""
        # Given: 模拟客户端
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.search_papers.return_value = [
            {
                "paperId": "123",
                "title": "Test Paper",
                "authors": [{"name": "Author 1"}, {"name": "Author 2"}],
                "year": 2024,
                "abstract": "Test abstract",
                "url": "https://example.com",
                "citationCount": 10,
                "venue": "Conference",
            }
        ]

        # When: 搜索论文
        papers = search_papers(mock_client, "test query", limit=10)

        # Then: 结果正确
        assert len(papers) == 1
        assert isinstance(papers[0], Paper)
        assert papers[0].title == "Test Paper"
        assert len(papers[0].authors) == 2

    def test_search_papers_with_year(self):
        """测试带年份筛选的论文搜索"""
        # Given: 模拟客户端
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.search_papers.return_value = []

        # When: 搜索论文（带年份）
        papers = search_papers(mock_client, "test query", year=2024)

        # Then: 正确调用
        mock_client.search_papers.assert_called_once_with("test query", limit=10, year=2024)
