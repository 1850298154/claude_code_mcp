# Academic Scholar Module

> 学术搜索与资料获取模块

## 模块说明

提供学术论文搜索、BibTeX 引用获取、引用验证等功能，主要集成 Semantic Scholar API。

## 子模块

| 子模块 | 路径 | 描述 | Bash 定位 |
|--------|------|------|-----------|
| Scholar | `academic/scholar.py` | Scholar 数据结构定义 | `find . -name "scholar.py" -path "*/academic/*"` |
| Scholar Ops | `academic/scholar/` | Scholar 操作集合 | `find . -path "*/academic/scholar/*.py"` |
| Semantic | `academic/semantic/` | Semantic Scholar 集成 | `find . -path "*/academic/semantic/**/*.py"` |

## 依赖关系

```
academic/
├── scholar/
│   ├── 上游依赖: core/types/*, semantic/client.py
│   └── 下游操作:
│       ├── search_papers.py      # 搜索论文
│       ├── get_bibtex.py         # 获取 BibTeX
│       ├── get_abstract.py       # 获取摘要
│       ├── verify_citations.py   # 验证引用
│       └── extract_metadata.py   # 提取元数据
└── semantic/
    ├── 上游依赖: 无
    └── 下游组件:
        ├── client.py             # API 客户端
        └── mapper/
            ├── paper_to_bibtex.py # 论文转 BibTeX
            └── response_to_model.py # 响应转模型
```

## 快速操作

```bash
# 搜索论文
python -m academic.scholar.search_papers --query "attention mechanism"

# 获取 BibTeX
python -m academic.scholar.get_bibtex --paper-id "abc123"

# 验证引用
python -m academic.scholar.verify_citations --file citations.bib
```

## 结构

```
academic/
├── README.md              # 本文件
├── scholar.py             # Scholar 数据结构定义
├── scholar/               # Scholar 操作
│   ├── README.md
│   ├── search_papers.py   # 搜索论文
│   ├── get_bibtex.py      # 获取 BibTeX
│   ├── get_abstract.py    # 获取摘要
│   ├── verify_citations.py # 验证引用
│   └── extract_metadata.py # 提取元数据
└── semantic/              # Semantic Scholar 集成
    ├── README.md
    ├── client.py          # API 客户端
    └── mapper/            # 数据映射
        ├── README.md
        ├── paper_to_bibtex.py # 论文转 BibTeX
        └── response_to_model.py # 响应转模型
```

## 典型使用场景

1. **搜索论文并获取 BibTeX**
   ```python
   scholar = Scholar()
   papers = scholar.search_papers("attention mechanism")
   bibtex = scholar.get_bibtex(papers[0].id)
   ```

2. **验证引用准确性**
   ```python
   with open("citations.bib") as f:
       result = scholar.verify_citations(f.read())
   ```

3. **批量提取元数据**
   ```python
   metadata = scholar.extract_metadata(paper_ids=["id1", "id2", "id3"])
   ```
