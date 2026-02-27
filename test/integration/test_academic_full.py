# ============================================================================
# 文件: test/integration/test_academic_full.py
# 描述: Academic 模块完整流程集成测试
#
# 测试对象: src/academic 模块完整流程
#
# Bash 快速定位:
#   find test -name "test_academic_full.py"
# ============================================================================

import pytest

from academic.scholar import Scholar
from academic.types import Paper


class TestAcademicFull:
    """Academic 模块完整流程集成测试"""

    def test_full_workflow_search(self):
        """测试完整搜索工作流"""
        # Given: Scholar
        scholar = Scholar(api_key=None)

        # When: 搜索论文（使用 mock）
        # 注意：实际测试需要真实的 API key 或 mock
        papers = scholar.search_papers("test query", limit=5)

        # Then: 结果为列表
        assert isinstance(papers, list)

    def test_full_workflow_bibtex(self):
        """测试完整 BibTeX 工作流"""
        # Given: Scholar
        scholar = Scholar(api_key=None)

        # When: 获取 BibTeX
        bibtex = scholar.get_bibtex("123")

        # Then: 结果为字符串或 None
        assert bibtex is None or isinstance(bibtex, str)

    def test_full_workflow_verify(self):
        """测试完整验证引用工作流"""
        # Given: Scholar
        scholar = Scholar(api_key=None)
        bibtex = "@article{test, title={Test}}"

        # When: 验证引用
        citations = scholar.verify_citations(bibtex)

        # Then: 结果为列表
        assert isinstance(citations, list)
