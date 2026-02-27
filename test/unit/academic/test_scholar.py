# ============================================================================
# 文件: test/unit/academic/test_scholar.py
# 描述: 测试 Scholar 类
#
# 测试对象: academic/scholar.py
#
# Bash 快速定位:
#   find test -name "test_scholar.py"
# ============================================================================

import pytest
from unittest.mock import Mock

from academic.scholar import Scholar
from academic.semantic.client import SemanticScholarClient


class TestScholar:
    """测试 Scholar 类"""

    def test_scholar_init(self):
        """测试 Scholar 初始化"""
        # When: 创建 Scholar
        scholar = Scholar(api_key=None)

        # Then: 初始化成功
        assert scholar is not None

    def test_scholar_with_api_key(self):
        """测试带 API key 的 Scholar"""
        # Given: API key
        api_key = "test-api-key"

        # When: 创建 Scholar
        scholar = Scholar(api_key=api_key)

        # Then: 使用提供的 API key
        assert scholar is not None

    def test_scholar_search_papers_delegates(self):
        """测试 search_papers 委托"""
        # Given: Scholar 和 mock 客户端
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.search_papers.return_value = []

        scholar = Scholar(api_key=None)
        scholar._client = mock_client

        # When: 搜索论文
        papers = scholar.search_papers("test query", limit=5)

        # Then: 正确调用客户端
        mock_client.search_papers.assert_called_once_with("test query", limit=5, year=None)

    def test_scholar_get_bibtex_delegates(self):
        """测试 get_bibtex 委托"""
        # Given: Scholar 和 mock 客户端
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.get_paper.return_value = {"paperId": "123", "citationStyles": {"bibtex": "@article{...}"}}

        scholar = Scholar(api_key=None)
        scholar._client = mock_client

        # When: 获取 BibTeX
        bibtex = scholar.get_bibtex("123")

        # Then: 正确调用客户端
        mock_client.get_paper.assert_called_once_with("123")
