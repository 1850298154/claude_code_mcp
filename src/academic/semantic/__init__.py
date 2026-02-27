# ============================================================================
# 文件: src/academic/semantic/__init__.py
# 描述: Semantic 模块初始化
#
# 上游依赖: 无
# 下游封装: scholar/*
#
# Bash 快速定位:
#   find . -name "__init__.py" -path "*/semantic/*"
# ============================================================================

from .client import SemanticScholarClient

__all__ = ["SemanticScholarClient"]
