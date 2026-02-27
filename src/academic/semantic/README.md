# ============================================================================
# 文件: src/academic/semantic/README.md
# 描述: Semantic 模块说明
#
# 上游依赖: academic/types.py
# 下游封装: scholar/*
#
# Bash 快速定位:
#   find . -name "README.md" -path "*/semantic/*"
# ============================================================================

# Semantic Scholar 集成

## 子模块

| 文件 | 描述 | Bash 定位 |
|------|------|-----------|
| `client.py` | API 客户端 | `find . -name "client.py" -path "*/semantic/*"` |

## 结构

```
semantic/
├── README.md              # 本文件
├── __init__.py           # 模块导出
└── client.py             # SemanticScholarClient 类
```
