# ============================================================================
# 文件: src/graphrag/builder/README.md
# 描述: Builder 操作集合
#
# 上游依赖: graphrag/builder.py, graphrag/types.py
# 下游封装: 无
#
# Bash 快速定位:
#   find . -name "README.md" -path "*/builder/*"
# ============================================================================

# Builder 操作模块

## 操作列表

| 操作 | 文件 | 描述 | Bash 定位 |
|------|------|------|-----------|
| build_from_project | `build_from_project.py` | 从项目构建图谱 | `find . -name "build_from_project.py"` |
| build_from_docs | `build_from_docs.py` | 从文档构建图谱 | `find . -name "build_from_docs.py"` |
| add_entity | `add_entity.py` | 添加实体 | `find . -name "add_entity.py"` |
| add_relation | `add_relation.py` | 添加关系 | `find . -name "add_relation.py"` |
| query_graph | `query_graph.py` | 查询图谱 | `find . -name "query_graph.py"` |

## 结构

```
builder/
├── README.md              # 本文件
├── __init__.py           # 模块导出
├── build_from_project.py  # 从项目构建图谱
├── build_from_docs.py     # 从文档构建图谱
├── add_entity.py         # 添加实体
├── add_relation.py       # 添加关系
└── query_graph.py        # 查询图谱
```
