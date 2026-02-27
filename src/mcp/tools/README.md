# MCP Tools Module

> MCP 工具定义

## 工具列表

| 工具 | 文件 | 描述 | Bash 定位 |
|------|------|------|-----------|
| claude_meta | `claude_meta.py` | ClaudeMeta 工具 | `find . -name "claude_meta.py" -path "*/tools/*"` |
| academic | `academic.py` | Academic 工具 | `find . -name "academic.py" -path "*/tools/*"` |
| vision | `vision.py` | Vision 工具 | `find . -name "vision.py" -path "*/tools/*"` |
| graphrag | `graphrag.py` | GraphRAG 工具 | `find . -name "graphrag.py" -path "*/tools/*"` |

## 结构

```
tools/
├── README.md              # 本文件
├── claude_meta.py         # ClaudeMeta 工具
├── academic.py            # Academic 工具
├── vision.py              # Vision 工具
└── graphrag.py            # GraphRAG 工具
```
