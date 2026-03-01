# ============================================================================
# 文件: src/mcp/README.md
# 描述: MCP 模块说明
#
# 上游依赖: 无
# 下游封装: 无
#
# Bash 快速定位:
#   find . -name "README.md" -path "*/mcp/*"
# ============================================================================

# MCP 模块

## 子模块

| 子模块 | 路径 | 描述 | Bash 定位 |
|--------|------|------|-----------|
| Server | `server.py` | MCP 服务器 | `find . -name "server.py"` |
| Tools | `tools/` | MCP 工具 | `find . -path "*/tools/*"` |
| Transport | `transport/` | 传输层 | `find . -path "*/transport/*"` |

## 结构

```
mcp/
├── README.md              # 本文件
├── server.py              # MCPServer 类
├── server/              # Server 操作
│   └── start.py         # 启动服务器
├── tools/                # MCP 工具
│   ├── README.md
│   ├── claude_meta.py   # Claude Meta 工具
│   ├── academic.py      # Academic 工具
│   ├── vision.py        # Vision 工具
│   └── graphrag.py      # GraphRAG 工具
└── transport/             # 传输层
    ├── README.md
    └── stdio.py         # Stdio 传输
```
