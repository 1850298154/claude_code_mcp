# ============================================================================
# 文件: test/unit/academic/scholar/test_extract_metadata.py
# 描述: 测试 extract_metadata 函数
#
# 测试对象: src/academic/scholar/extract_metadata.py
#
# Bash 快速定位:
#   find test -name "test_extract_metadata.py"
# ============================================================================

import pytest
from unittest.mock import Mock

from academic.types import Paper
from academic.semantic.client import SemanticScholarClient
from academic.scholar.extract_metadata import extract_metadata


class TestExtractMetadata:
    """测试 extract_metadata 函数"""

    def test_extract_metadata_single(self):
        """测试提取单个论文元数据"""
        # Given: 模拟客户端
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.get_paper.return_value = {
            "paperId": "123",
            "title": "Test Paper",
            "authors": [{"name": "Author 1"}],
            "year": 2024,
            "abstract": "Test abstract",
            "citationCount": 10,
        }

        # When: 提取元数据
        papers = extract_metadata(mock_client, ["123"])

        # Then: 结果正确
        assert len(papers) == 1
        assert isinstance(papers[0], Paper)
        assert papers[0].title == "Test Paper"

    def test_extract_metadata_multiple(self):
        """测试提取多个论文元数据"""
        # Given: 模拟客户端
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.get_paper.side_effect = [
            {"paperId": "123", "title": "Paper 1"},
            {"paperId": "456", "title": "Paper 2"},
        ]

        # When: 提取元数据
        papers = extract_metadata(mock_client, ["123", "456"])

        # Then: 结果正确
        assert len(papers) == 2
        assert papers[0].title == "Paper 1"
        assert papers[1].title == "Paper 2"
