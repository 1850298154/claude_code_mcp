# GraphRAG QA Module

> 图谱构建与问答系统模块

## 模块说明

提供知识图谱构建、实体关系管理、基于图谱的问答功能，集成 DeepWiki 将项目解析为 QA MCP。

## 子模块

| 子模块 | 路径 | 描述 | Bash 定位 |
|--------|------|------|-----------|
| Builder | `graphrag/builder.py` | GraphBuilder 数据结构定义 | `find . -name "builder.py" -path "*/graphrag/*"` |
| Builder Ops | `graphrag/builder/` | Builder 操作集合 | `find . -path "*/graphrag/builder/*.py"` |
| QA System | `graphrag/qa/` | 问答系统 | `find . -path "*/graphrag/qa/**/*.py"` |
| DeepWiki | `graphrag/deepwiki/` | DeepWiki 集成 | `find . -path "*/graphrag/deepwiki/**/*.py"` |

## 依赖关系

```
graphrag/
├── builder/
│   ├── 上游依赖: core/types/*
│   └── 下游操作:
│       ├── build_from_project.py   # 从项目构建图谱
│       ├── build_from_docs.py      # 从文档构建图谱
│       ├── add_entity.py           # 添加实体
│       ├── add_relation.py         # 添加关系
│       └── query_graph.py          # 查询图谱
├── qa/
│   ├── 上游依赖: core/types/*, builder/*
│   └── 下游操作:
│       ├── ask.py                  # 提问
│       ├── retrieve.py             # 检索相关内容
│       └── generate_answer.py      # 生成答案
└── deepwiki/
    ├── 上游依赖: 无
    └── 下游组件:
        ├── client.py               # API 客户端
        └── indexer/
            ├── index_repository.py # 索引仓库
            └── index_structure.py  # 索引结构
```

## 快速操作

```bash
# 从项目构建图谱
python -m graphrag.builder.build_from_project --path /path/to/project

# 提问
python -m graphrag.qa.ask --question "这个项目是做什么的？"

# 索引仓库到 DeepWiki
python -m graphrag.deepwiki.indexer.index_repository --owner yourname --repo project
```

## 结构

```
graphrag/
├── README.md              # 本文件
├── builder.py             # GraphBuilder 数据结构定义
├── builder/               # Builder 操作
│   ├── README.md
│   ├── build_from_project.py  # 从项目构建图谱
│   ├── build_from_docs.py     # 从文档构建图谱
│   ├── add_entity.py          # 添加实体
│   ├── add_relation.py        # 添加关系
│   └── query_graph.py         # 查询图谱
├── qa/                    # 问答系统
│   ├── README.md
│   ├── qa_system.py       # QASystem 数据结构定义
│   └── qa/
│       ├── README.md
│       ├── ask.py          # 提问
│       ├── retrieve.py     # 检索相关内容
│       └── generate_answer.py # 生成答案
└── deepwiki/              # DeepWiki 集成
    ├── README.md
    ├── client.py          # API 客户端
    └── indexer/            # 索引器
        ├── README.md
        ├── index_repository.py # 索引仓库
        └── index_structure.py  # 索引结构
```

## 典型使用场景

1. **构建项目知识图谱**
   ```python
   builder = GraphBuilder()
   graph = builder.build_from_project("/path/to/project")
   ```

2. **基于图谱问答**
   ```python
   qa = QASystem(graph=graph)
   answer = qa.ask("这个项目的核心模块是什么？")
   ```

3. **索引到 DeepWiki**
   ```python
   indexer = DeepWikiIndexer()
   indexer.index_repository(owner="yourname", repo="project")
   ```
