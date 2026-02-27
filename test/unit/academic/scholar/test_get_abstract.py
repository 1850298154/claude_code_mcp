# ============================================================================
# 文件: test/unit/academic/scholar/test_get_abstract.py
# 描述: 测试 get_abstract 函数
#
# 测试对象: academic/scholar/get_abstract.py
#
# Bash 快速定位:
#   find test -name "test_get_abstract.py"
# ============================================================================

import pytest
from unittest.mock import Mock

from academic.types import Paper
from academic.semantic.client import SemanticScholarClient
from academic.scholar.get_abstract import get_abstract


class TestGetAbstract:
    """测试 get_abstract 函数"""

    def test_get_abstract_success(self):
        """测试成功获取摘要"""
        # Given: 模拟客户端返回摘要
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.get_paper.return_value = {
            "paperId": "123",
            "abstract": "This is a test abstract."
        }

        # When: 获取摘要
        abstract = get_abstract(mock_client, "123")

        # Then: 返回正确摘要
        assert abstract == "This is a test abstract."
        mock_client.get_paper.assert_called_once_with("123")

    def test_get_abstract_not_found(self):
        """测试论文不存在"""
        # Given: 模拟客户端返回 None
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.get_paper.return_value = None

        # When: 获取摘要
        abstract = get_abstract(mock_client, "999")

        # Then: 返回空字符串
        assert abstract == ""

    def test_get_abstract_no_abstract(self):
        """测试论文无摘要"""
        # Given: 模拟客户端返回无摘要的论文
        mock_client = Mock(spec=SemanticScholarClient)
        mock_client.get_paper.return_value = {
            "paperId": "123",
            "title": "Test Paper"
            # 无 abstract 字段
        }

        # When: 获取摘要
        abstract = get_abstract(mock_client, "123")

        # Then: 返回空字符串
        assert abstract == ""
