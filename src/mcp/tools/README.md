# ============================================================================
# 文件: src/mcp/tools/README.md
# 描述: MCP 工具模块说明
#
# 上游依赖:
#   - claude_meta/reader                     (ClaudeMetaReader)
#   - academic/scholar                         (Scholar)
#   - vision/analyzer                        (VisionAnalyzer)
#   - graphrag/builder                       (GraphBuilder)
#   - graphrag/qa.qa_system                     (QASystem)
#
# 下游封装: 无
#
# Bash 快速定位:
#   find . -name "README.md" -path "*/tools/*"
# ============================================================================

# MCP 工具模块

## 工具列表

| 模块 | 工具 | 描述 |
|--------|------|------|
| ClaudeMeta | `claude_meta.py` | Claude Meta 工具 |
| Academic | `academic.py` | Academic 工具 |
| Vision | `vision.py` | Vision 工具 |
| GraphRAG | `graphrag.py` | GraphRAG 工具 |

## 结构

```
tools/
├── README.md              # 本文件
├── claude_meta.py       # Claude Meta 工具
├── academic.py          # Academic 工具
├── vision.py            # Vision 工具
└── graphrag.py          # GraphRAG 工具
```
