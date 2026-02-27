# TODO (渐进披露)

> 项目任务管理 - 用于开发进展追踪和上下文恢复

## 格式说明

```
## 模块名
- [ ] 任务描述
  - 上游: 依赖的模块/文件
  - 下游: 被此任务影响的模块/文件
  - Bash: find . -name "*.py" -path "*/module/*"
```

---

## Claude Meta 模块

- [x] 核心类型定义
  - 上游: 无
  - 下游: parser, reader, analyzer
  - Bash: find . -name "*.py" -path "*/core/types/*"

- [x] 路径配置 (paths.py)
  - 上游: 无
  - 下游: reader, parser
  - Bash: find . -name "paths.py" -path "*/claude_meta/*"

- [x] 解析器 (parser/)
  - 上游: core/types
  - 下游: reader
  - Bash: find . -name "parse_*.py" -path "*/claude_meta/*"

- [x] Reader 操作 (reader/)
  - 上游: config, parser
  - 下游: analyzer, mcp/tools
  - Bash: find . -name "*.py" -path "*/claude_meta/reader/*"

- [x] Analyzer (analyzer/)
  - 上游: core/types
  - 下游: reader
  - Bash: find . -name "*.py" -path "*/claude_meta/analyzer/*"

- [x] 单元测试 (test/unit/claude_meta/*)
  - 上游: src/claude_meta/*
  - 下游: 无
  - Bash: find test -name "*.py" -path "*/claude_meta/*"

- [x] 集成测试 (test/integration/test_claude_meta_full.py)
  - 上游: src/claude_meta/*
  - 下游: 无
  - Bash: find test -name "test_claude_meta_full.py"

---

## Academic 模块

- [ ] Scholar 类定义 (scholar.py)
  - 上游: core/types
  - 下游: scholar/*
  - Bash: find . -name "scholar.py" -path "*/academic/*"

- [ ] 搜索论文 (scholar/search_papers.py)
  - 上游: semantic/client
  - 下游: mcp/tools/academic
  - Bash: find . -name "search_papers.py"

- [ ] 获取 BibTeX (scholar/get_bibtex.py)
  - 上游: semantic/client
  - 下游: mcp/tools/academic
  - Bash: find . -name "get_bibtex.py"

- [ ] 验证引用 (scholar/verify_citations.py)
  - 上游: semantic/client
  - 下游: mcp/tools/academic
  - Bash: find . -name "verify_citations.py"

- [ ] Semantic Scholar 客户端 (semantic/client.py)
  - 上游: 无
  - 下游: scholar/*
  - Bash: find . -name "client.py" -path "*/semantic/*"

- [ ] 单元测试 (test/unit/academic/*)
  - 上游: src/academic/*
  - 下游: 无
  - Bash: find test -name "*.py" -path "*/academic/*"

- [ ] 集成测试 (test/integration/test_academic_full.py)
  - 上游: src/academic/*
  - 下游: 无
  - Bash: find test -name "test_academic_full.py"

---

## Vision 模块

- [ ] VisionAnalyzer 类定义 (analyzer.py)
  - 上游: core/types, models/*
  - 下游: analyzer/*
  - Bash: find . -name "analyzer.py" -path "*/vision/*"

- [ ] 分析图像 (analyzer/analyze_image.py)
  - 上游: models/*
  - 下游: mcp/tools/vision
  - Bash: find . -name "analyze_image.py"

- [ ] 检测对象 (analyzer/detect_objects.py)
  - 上游: models/*
  - 下游: mcp/tools/vision
  - Bash: find . -name "detect_objects.py"

- [ ] 提取文本 (analyzer/extract_text.py)
  - 上游: models/*
  - 下游: mcp/tools/vision
  - Bash: find . -name "extract_text.py"

- [ ] GLM-4V 模型封装 (models/glm4v.py)
  - 上游: 无
  - 下游: analyzer/*
  - Bash: find . -name "glm4v.py"

- [ ] 单元测试 (test/unit/vision/*)
  - 上游: src/vision/*
  - 下游: 无
  - Bash: find test -name "*.py" -path "*/vision/*"

- [ ] 集成测试 (test/integration/test_vision_full.py)
  - 上游: src/vision/*
  - 下游: 无
  - Bash: find test -name "test_vision_full.py"

---

## GraphRAG 模块

- [ ] GraphBuilder 类定义 (builder.py)
  - 上游: core/types
  - 下游: builder/*
  - Bash: find . -name "builder.py" -path "*/graphrag/*"

- [ ] 从项目构建图谱 (builder/build_from_project.py)
  - 上游: 无
  - 下游: mcp/tools/graphrag
  - Bash: find . -name "build_from_project.py"

- [ ] 添加实体 (builder/add_entity.py)
  - 上游: 无
  - 下游: mcp/tools/graphrag
  - Bash: find . -name "add_entity.py"

- [ ] 查询图谱 (builder/query_graph.py)
  - 上游: 无
  - 下游: mcp/tools/graphrag
  - Bash: find . -name "query_graph.py"

- [ ] QASystem 类定义 (qa/__init__.py)
  - 上游: core/types, builder/*
  - 下游: qa/*
  - Bash: find . -name "__init__.py" -path "*/qa/*"

- [ ] 提问 (qa/ask.py)
  - 上游: builder/*
  - 下游: mcp/tools/graphrag
  - Bash: find . -name "ask.py" -path "*/qa/*"

- [ ] 单元测试 (test/unit/graphrag/*)
  - 上游: src/graphrag/*
  - 下游: 无
  - Bash: find test -name "*.py" -path "*/graphrag/*"

- [ ] 集成测试 (test/integration/test_graphrag_full.py)
  - 上游: src/graphrag/*
  - 下游: 无
  - Bash: find test -name "test_graphrag_full.py"

---

## MCP 模块

- [ ] MCPServer 类定义 (server.py)
  - 上游: claude_meta, academic, vision, graphrag
  - 下游: server/*
  - Bash: find . -name "server.py" -path "*/mcp/*"

- [ ] 启动服务器 (server/start.py)
  - 上游: server.py
  - 下游: 无
  - Bash: find . -name "start.py" -path "*/mcp/*"

- [ ] ClaudeMeta 工具 (tools/claude_meta.py)
  - 上游: claude_meta/reader
  - 下游: 无
  - Bash: find . -name "claude_meta.py" -path "*/tools/*"

- [ ] Academic 工具 (tools/academic.py)
  - 上游: academic/scholar
  - 下游: 无
  - Bash: find . -name "academic.py" -path "*/tools/*"

- [ ] Vision 工具 (tools/vision.py)
  - 上游: vision/analyzer
  - 下游: 无
  - Bash: find . -name "vision.py" -path "*/tools/*"

- [ ] GraphRAG 工具 (tools/graphrag.py)
  - 上游: graphrag/builder, graphrag/qa
  - 下游: 无
  - Bash: find . -name "graphrag.py" -path "*/tools/*"

- [ ] 单元测试 (test/unit/mcp/*)
  - 上游: src/mcp/*
  - 下游: 无
  - Bash: find test -name "*.py" -path "*/mcp/*"

---

## Utils 模块

- [ ] FileOps 类定义 (file_ops.py)
  - 上游: 无
  - 下游: file_ops/*
  - Bash: find . -name "file_ops.py" -path "*/utils/*"

- [ ] 读取文件 (file_ops/read.py)
  - 上游: 无
  - 下游: 所有模块
  - Bash: find . -name "read.py" -path "*/utils/*"

- [ ] 写入文件 (file_ops/write.py)
  - 上游: 无
  - 下游: 所有模块
  - Bash: find . -name "write.py" -path "*/utils/*"

- [ ] 单元测试 (test/unit/utils/*)
  - 上游: src/utils/*
  - 下游: 无
  - Bash: find test -name "*.py" -path "*/utils/*"

---

## 文档

- [ ] 更新 README.md
  - 上游: 所有模块
  - 下游: 用户
  - Bash: find . -maxdepth 1 -name "README.md"

- [ ] 更新各模块 README.md
  - 上游: 各模块源代码
  - 下游: 用户
  - Bash: find . -name "README.md" -path "*/src/*"

- [ ] 添加使用示例 (examples/*)
  - 上游: 所有模块
  - 下游: 用户
  - Bash: find . -name "*.py" -path "*/examples/*"

---

## 开发流程

### 上下文恢复
1. 当对话上下文满时，查看本文件 `dev/TODO.md`
2. 找到正在进行的模块任务
3. 根据 `上游` 和 `下游` 快速定位相关文件
4. 恢复开发状态

### 任务开发流程
1. 从 `dev/TODO.md` 选择一个待完成任务
2. 查看任务的 `上游` 依赖，确保依赖已实现
3. 创建源代码文件（遵循命名规则）
4. 编写对应的测试文件
5. 运行测试：`cd test && uv run pytest`
6. 更新 `dev/TODO.md`，将任务标记为 `[x]`

### Git 提交流程（渐进披露）
1. 每完成一个功能单元立即提交
2. 每添加一个测试立即提交
3. 每修复一个问题立即提交
4. 每次提交都包含：
   - 清晰的标题
   - 详细的描述（做了什么、怎么做的）
   - 上游依赖
   - 下游影响
   - Bash 快速定位命令

### 提交示例
```bash
git add src/claude_meta/reader/get_sessions.py
git add test/unit/claude_meta/reader/test_get_sessions.py
git commit -m "feat(claude_meta): 添加 get_sessions 函数

- 实现 get_sessions 函数用于获取所有会话
- 添加参数 paths: ClaudeMetaPaths
- 返回 List[Conversation] 类型
- 添加单元测试覆盖

上游依赖:
  - src/claude_meta/config/paths.py
  - src/claude_meta/parser/parse_conversation.py

下游影响:
  - src/claude_meta/reader/__init__.py
  - test/unit/claude_meta/reader/test_get_sessions.py

Bash 快速定位:
  find . -name 'get_sessions.py'"

# 更新 TODO.md
git add dev/TODO.md
git commit -m "docs(dev): 标记 get_sessions 任务完成

- 在 dev/TODO.md 中标记 get_sessions 为完成
- 查看上游: config, parser
- 查看下游: reader/__init__.py, test

Bash 快速定位:
  find . -name 'TODO.md'"
```

### 使用 DeepWiki 查询问题
当遇到 Claude Code 相关问题时，使用 deepwiki MCP 查询：
```
https://deepwiki.com/anthropics/claude-code
```
