# ============================================================================
# 文件: src/academic/scholar/README.md
# 描述: Scholar 操作集合
#
# 上游依赖: academic/scholar.py, academic/semantic/client.py
# 下游封装: 无
#
# Bash 快速定位:
#   find . -name "README.md" -path "*/scholar/*"
# ============================================================================

# Scholar 操作模块

## 操作列表

| 操作 | 文件 | 描述 | Bash 定位 |
|------|------|------|-----------|
| search_papers | `search_papers.py` | 搜索论文 | `find . -name "search_papers.py"` |
| get_bibtex | `get_bibtex.py` | 获取 BibTeX | `find . -name "get_bibtex.py"` |
| get_abstract | `get_abstract.py` | 获取摘要 | `find . -name "get_abstract.py"` |
| verify_citations | `verify_citations.py` | 验证引用 | `find . -name "verify_citations.py"` |
| extract_metadata | `extract_metadata.py` | 提取元数据 | `find . -name "extract_metadata.py"` |

## 结构

```
scholar/
├── README.md              # 本文件
├── __init__.py           # 模块导出
├── search_papers.py       # 搜索论文
├── get_bibtex.py          # 获取 BibTeX
├── get_abstract.py        # 获取摘要
├── verify_citations.py     # 验证引用
└── extract_metadata.py     # 提取元数据
```
