# ============================================================================
# 文件: test/unit/academic/scholar/test_get_bibtex.py
# 描述: 测试 get_bibtex 函数
#
# 测试对象: academic/scholar/get_bibtex.py
#
# Bash 快速定位:
#   find test -name "test_get_bibtex.py"
# ============================================================================

import pytest
from unittest.mock import Mock

from academic.types import Paper
from academic.semantic.client import SemanticScholarClient
from academic.scholar.get_bibtex import get_bibtex


class TestGetBibtex:
    """测试 get_bibtex 函数"""

    def test_get_bibtex_success(self):
        """测试成功获取 BibTeX"""
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.get_paper.return_value = {
            "paperId": "123",
            "title": "Test Paper",
            "bibtex": "@article{test, title={Test}}",
        }

        bibtex = get_bibtex(mock_client, "123")

        assert bibtex == "@article{test, title={Test}}"

    def test_get_bibtex_not_found(self):
        """测试论文不存在时获取 BibTeX"""
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.get_paper.return_value = None

        bibtex = get_bibtex(mock_client, "nonexistent")

        assert bibtex is None
