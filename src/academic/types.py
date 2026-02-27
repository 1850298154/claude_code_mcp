# ============================================================================
# 文件: src/academic/types.py
# 描述: Academic 模块类型定义
#
# 上游依赖: 无
# 下游封装: scholar.py, semantic/*
#
# Bash 快速定位:
#   find . -name "types.py" -path "*/academic/*"
# ============================================================================

from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from datetime import datetime


@dataclass
class Paper:
    """论文数据结构

    Attributes:
        paper_id: 论文唯一标识符
        title: 论文标题
        authors: 作者列表
        year: 发表年份
        abstract: 摘要
        url: 论文链接
        bibtex: BibTeX 引用格式
        citations: 引用数
        references: 参考文献列表
        venue: 发表会议/期刊
    """

    paper_id: str
    title: str
    authors: List[str]
    year: Optional[int] = None
    abstract: Optional[str] = None
    url: Optional[str] = None
    bibtex: Optional[str] = None
    citations: Optional[int] = None
    references: Optional[List[str]] = None
    venue: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class Citation:
    """引用数据结构

    Attributes:
        paper_id: 论文 ID
        text: 引用文本
        source: 引用来源
        verified: 是否已验证
        mismatches: 不匹配详情
    """

    paper_id: str
    text: str
    source: str
    verified: bool
    mismatches: Optional[List[Dict[str, Any]]] = None


@dataclass
class SearchOptions:
    """搜索选项

    Attributes:
        limit: 返回结果数量
        year: 年份筛选
        venue: 会议/期刊筛选
        open_access: 仅开放获取
    """

    limit: int = 10
    year: Optional[int] = None
    venue: Optional[str] = None
    open_access: bool = False
    fields: Optional[List[str]] = None
