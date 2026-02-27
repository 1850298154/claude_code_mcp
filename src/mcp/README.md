# MCP Server Module

> MCP 服务器实现模块

## 模块说明

将所有功能模块（ClaudeMeta、Academic、Vision、GraphRAG）封装为 MCP 工具，提供 Stdio/SSE 传输层。

## 子模块

| 子模块 | 路径 | 描述 | Bash 定位 |
|--------|------|------|-----------|
| Server | `mcp/server.py` | MCPServer 数据结构定义 | `find . -name "server.py" -path "*/mcp/*"` |
| Server Ops | `mcp/server/` | Server 操作集合 | `find . -path "*/mcp/server/*.py"` |
| Tools | `mcp/tools/` | MCP 工具定义 | `find . -path "*/mcp/tools/*.py"` |
| Transport | `mcp/transport/` | 传输层 | `find . -path "*/mcp/transport/*.py"` |

## 依赖关系

```
mcp/
├── server/
│   ├── 上游依赖: claude_meta/, academic/, vision/, graphrag/
│   └── 下游操作:
│       ├── start.py          # 启动服务器
│       ├── stop.py           # 停止服务器
│       └── register_tool.py  # 注册工具
├── tools/
│   ├── 上游依赖: 各功能模块
│   └── 下游工具:
│       ├── claude_meta.py    # ClaudeMeta 工具
│       ├── academic.py       # Academic 工具
│       ├── vision.py         # Vision 工具
│       └── graphrag.py       # GraphRAG 工具
└── transport/
    ├── 上游依赖: server/
    └── 下游组件:
        ├── stdio.py          # Stdio 传输
        └── sse.py            # SSE 传输（可选）
```

## 快速操作

```bash
# 启动 MCP 服务器
python -m mcp.server.start

# 查看可用工具
python -m mcp.tools.list

# 使用特定工具
python -m mcp.tools.claude_meta --action get_sessions
```

## 结构

```
mcp/
├── README.md              # 本文件
├── server.py              # MCPServer 数据结构定义
├── server/                # Server 操作
│   ├── README.md
│   ├── start.py           # 启动服务器
│   ├── stop.py            # 停止服务器
│   └── register_tool.py   # 注册工具
├── tools/                 # MCP 工具定义
│   ├── README.md
│   ├── claude_meta.py     # ClaudeMeta 工具
│   ├── academic.py        # Academic 工具
│   ├── vision.py          # Vision 工具
│   └── graphrag.py        # GraphRAG 工具
└── transport/             # 传输层
    ├── README.md
    ├── stdio.py           # Stdio 传输
    └── sse.py             # SSE 传输（可选）
```

## 工具注册

### ClaudeMeta 工具
- `claude_meta_get_sessions` - 获取所有会话
- `claude_meta_get_chat_history` - 获取聊天历史
- `claude_meta_get_project_context` - 获取项目上下文
- `claude_meta_restore_session` - 恢复会话

### Academic 工具
- `academic_search_papers` - 搜索论文
- `academic_get_bibtex` - 获取 BibTeX
- `academic_verify_citations` - 验证引用

### Vision 工具
- `vision_analyze_image` - 分析图像
- `vision_detect_objects` - 检测对象
- `vision_extract_text` - 提取文本

### GraphRAG 工具
- `graphrag_build_from_project` - 构建图谱
- `graphrag_ask` - 提问
- `graphrag_query_graph` - 查询图谱
