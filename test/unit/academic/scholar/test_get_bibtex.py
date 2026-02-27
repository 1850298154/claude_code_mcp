# ============================================================================
# 文件: test/unit/academic/scholar/test_get_bibtex.py
# 描述: 测试 get_bibtex 函数
#
# 测试对象: src/academic/scholar/get_bibtex.py
#
# Bash 快速定位:
#   find test -name "test_get_bibtex.py"
# ============================================================================

import pytest
from unittest.mock import Mock

from academic.semantic.client import SemanticScholarClient
from academic.scholar.get_bibtex import get_bibtex


class TestGetBibtex:
    """测试 get_bibtex 函数"""

    def test_get_bibtex_success(self):
        """测试成功获取 BibTeX"""
        # Given: 模拟客户端
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.get_paper.return_value = {
            "paperId": "123",
            "title": "Test Paper",
            "bibtex": "@article{test, title={Test}}",
        }

        # When: 获取 BibTeX
        bibtex = get_bibtex(mock_client, "123")

        # Then: 结果正确
        assert bibtex == "@article{test, title={Test}}"

    def test_get_bibtex_not_found(self):
        """测试论文不存在时获取 BibTeX"""
        # Given: 模拟客户端返回 None
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.get_paper.return_value = None

        # When: 获取 BibTeX
        bibtex = get_bibtex(mock_client, "nonexistent")

        # Then: 结果为 None
        assert bibtex is None
