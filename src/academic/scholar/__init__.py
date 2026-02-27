# ============================================================================
# 文件: src/academic/scholar/__init__.py
# 描述: Scholar 模块初始化
#
# 上游依赖: academic/scholar.py
# 下游封装: 无
#
# Bash 快速定位:
#   find . -name "__init__.py" -path "*/scholar/*"
# ============================================================================

from .search_papers import search_papers
from .get_bibtex import get_bibtex
from .get_abstract import get_abstract
from .verify_citations import verify_citations
from .extract_metadata import extract_metadata

__all__ = [
    "search_papers",
    "get_bibtex",
    "get_abstract",
    "verify_citations",
    "extract_metadata",
]
