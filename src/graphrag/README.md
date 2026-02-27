# ============================================================================
# 文件: src/graphrag/README.md
# 描述: GraphRAG 模块说明
#
# 上游依赖: graphrag/types.py
# 下游封装: mcp/tools/graphrag.py
#
# Bash 快速定位:
#   find . -name "README.md" -path "*/graphrag/*"
# ============================================================================

# GraphRAG 模块

## 子模块

| 子模块 | 路径 | 描述 | Bash 定位 |
|--------|------|------|-----------|
| Builder | `builder/` | 图谱构建 | `find . -path "*/builder/*"` |
| QA | `qa/` | 问答系统 | `find . -path "*/qa/*"` |

## 结构

```
graphrag/
├── README.md              # 本文件
├── types.py              # 类型定义
├── builder.py            # GraphBuilder 类
├── builder/              # Builder 操作
│   ├── README.md
│   ├── __init__.py
│   ├── build_from_project.py
│   ├── build_from_docs.py
│   ├── add_entity.py
│   ├── add_relation.py
│   └── query_graph.py
└── qa/                   # 问答系统
    ├── README.md
    ├── __init__.py
    └── qa_system.py
```
