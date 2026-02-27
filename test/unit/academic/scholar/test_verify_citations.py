# ============================================================================
# 文件: test/unit/academic/scholar/test_verify_citations.py
# 描述: 测试 verify_citations 函数
#
# 测试对象: src/academic/scholar/verify_citations.py
#
# Bash 快速定位:
#   find test -name "test_verify_citations.py"
# ============================================================================

import pytest
from unittest.mock import Mock

from academic.types import Citation
from academic.semantic.client import SemanticScholarClient
from academic.scholar.verify_citations import verify_citations


class TestVerifyCitations:
    """测试 verify_citations 函数"""

    def test_verify_citations_valid(self):
        """测试验证有效引用"""
        # Given: 模拟客户端和 BibTeX
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.get_paper.return_value = {
            "paperId": "123",
            "title": "Test Paper",
        }
        bibtex = "@article{test, title={Test}}"

        # When: 验证引用
        citations = verify_citations(mock_client, bibtex)

        # Then: 结果正确
        assert len(citations) == 1
        assert isinstance(citations[0], Citation)
        assert citations[0].paper_id == "test"
        assert citations[0].verified is True

    def test_verify_citations_invalid(self):
        """测试验证无效引用"""
        # Given: 模拟客户端返回 None
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.get_paper.return_value = None
        bibtex = "@article{test, title={Test}}"

        # When: 验证引用
        citations = verify_citations(mock_client, bibtex)

        # Then: 结果正确
        assert len(citations) == 1
        assert citations[0].verified is False
