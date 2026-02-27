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

- [x] 核心类型定义 (core/types/claude/)
  - 上游: 无
  - 下游: parser, reader, analyzer
  - Bash: find . -name "*.py" -path "*/core/types/*"

- [x] 路径配置 (claude_meta/config/paths.py)
  - 上游: 无
  - 下游: reader, parser
  - Bash: find . -name "paths.py" -path "*/claude_meta/*"

- [x] 解析器 (claude_meta/parser/)
  - 上游: core/types
  - 下游: reader
  - Bash: find . -name "parse_*.py" -path "*/claude_meta/*"

- [x] Reader 操作 (claude_meta/reader/)
  - 上游: config, parser
  - 下游: analyzer, mcp/tools
  - Bash: find . -name "*.py" -path "*/claude_meta/reader/*"

- [x] Analyzer (claude_meta/analyzer/)
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

- [x] Scholar 类定义 (academic/scholar.py)
  - 上游: core/types
  - 下游: scholar/*
  - Bash: find . -name "scholar.py" -path "*/academic/*"

- [x] 搜索论文 (academic/scholar/search_papers.py)
  - 上游: semantic/client
  - 下游: scholar.py, mcp/tools/academic
  - Bash: find . -name "search_papers.py"

- [x] 获取 BibTeX (academic/scholar/get_bibtex.py)
  - 上游: semantic/client
  - 下游: scholar.py, mcp/tools/academic
  - Bash: find . -name "get_bibtex.py"

- [x] 获取摘要 (academic/scholar/get_abstract.py)
  - 上游: semantic/client
  - 下游: scholar.py, mcp/tools/academic
  - Bash: find . -name "get_abstract.py"

- [x] 验证引用 (academic/scholar/verify_citations.py)
  - 上游: semantic/client
  - 下游: scholar.py, mcp/tools/academic
  - Bash: find . -name "verify_citations.py"

- [x] Semantic Scholar 客户端 (academic/semantic/client.py)
  - 上游: academic/types
  - 下游: scholar/*
  - Bash: find . -name "client.py" -path "*/academic/semantic/*"

- [x] 单元测试 (test/unit/academic/scholar/*)
  - 上游: src/academic/scholar, semantic
  - 下游: 无
  - Bash: find test -name "*.py" -path "*/academic/scholar/*"

- [x] 集成测试 (test/integration/test_academic_full.py)
  - 上游: src/academic/scholar, semantic
  - 下游: 无
  - Bash: find test -name "test_academic_full.py"

---

## Vision 模块

- [x] 视觉类型定义 (vision/types.py)
  - 上游: 无
  - 下游: analyzer.py, models/*
  - Bash: find . -name "types.py" -path "*/vision/*"

- [x] GLM-4V 模型封装 (vision/models/glm4v.py)
  - 上游: vision/types
  - 下游: analyzer/*
  - Bash: find . -name "glm4v.py" -path "*/vision/models/*"

- [x] VisionAnalyzer 类定义 (vision/analyzer.py)
  - 上游: vision/types, models/*
  - 下游: analyzer/*
  - Bash: find . -name "analyzer.py" -path "*/vision/*"

- [x] 分析图像 (vision/analyzer/analyze_image.py)
  - 上游: types, models/*
  - 下游: analyzer.py
  - Bash: find . -name "analyze_image.py"

- [x] 检测对象 (vision/analyzer/detect_objects.py)
  - 上游: types, models/*
  - 下游: analyzer.py
  - Bash: find . -name "detect_objects.py"

- [x] 提取文本 (vision/analyzer/extract_text.py)
  - 上游: types, models/*
  - 下游: analyzer.py
  - Bash: find . -name "extract_text.py"

- [x] 单元测试 (test/unit/vision/analyzer/test_analyze_image.py)
  - 上游: src/vision/analyzer.py
  - 下游: 无
  - Bash: find test -name "test_analyze_image.py"

---

## GraphRAG 模块

- [x] 图谱类型定义 (graphrag/types.py)
  - 上游: 无
  - 下游: builder.py, qa/*
  - Bash: find . -name "types.py" -path "*/graphrag/*"

- [x] GraphBuilder 类定义 (graphrag/builder.py)
  - 上游: graphrag/types
  - 下游: builder/*
  - Bash: find . -name "builder.py" -path "*/graphrag/*"

- [x] 从项目构建图谱 (graphrag/builder/build_from_project.py)
  - 上游: graphrag/types
  - 下游: builder.py
  - Bash: find . -name "build_from_project.py"

- [x] 从文档构建图谱 (graphrag/builder/build_from_docs.py)
  - 上游: graphrag/types
  - 下游: builder.py
  - Bash: find . -name "build_from_docs.py"

- [x] 添加实体 (graphrag/builder/add_entity.py)
  - 上游: graphrag/types
  - 下游: builder.py
  - Bash: find . -name "add_entity.py"

- [x] 添加关系 (graphrag/builder/add_relation.py)
  - 上游: graphrag/types
  - 下游: builder.py
  - Bash: find . -name "add_relation.py"

- [x] 查询图谱 (graphrag/builder/query_graph.py)
  - 上游: graphrag/types
  - 下游: builder.py
  - Bash: find . -name "query_graph.py"

- [x] QASystem 类定义 (graphrag/qa/qa_system.py)
  - 上游: graphrag/types, builder/*
  - 下游: qa/*
  - Bash: find . -name "qa_system.py" -path "*/qa/*"

- [x] 提问 (graphrag/qa/qa_system.py)
  - 上游: graphrag/types, builder
  - 下游: qa.py
  - Bash: find . -name "ask.py" -path "*/qa/*"

- [x] 单元测试 (test/unit/graphrag/builder/test_build_from_project.py)
  - 上游: src/graphrag/builder.py
  - 下游: 无
  - Bash: find test -name "test_build_from_project.py"

- [x] 集成测试 (test/integration/test_graphrag_full.py)
  - 上游: src/graphrag/builder.py, qa/*
  - 下游: 无
  - Bash: find test -name "test_graphrag_full.py"

---

## MCP 模块

- [x] MCPServer 类定义 (mcp/server.py)
  - 上游: claude_meta, academic, vision, graphrag
  - 下游: server/*
  - Bash: find . -name "server.py" -path "*/mcp/*"

- [x] 启动服务器 (mcp/server/start.py)
  - 上游: mcp/server.py
  - 下游: 无
  - Bash: find . -name "start.py" -path "*/server/*"

- [x] ClaudeMeta 工具 (mcp/tools/claude_meta.py)
  - 上游: claude_meta/reader
  - 下游: 无
  - Bash: find . -name "claude_meta.py" -path "*/tools/*"

- [x] Academic 工具 (mcp/tools/academic.py)
  - 上游: academic/scholar
  - 下游: 无
  - Bash: find . -name "academic.py" -path "*/tools/*"

- [x] Vision 工具 (mcp/tools/vision.py)
  - 上游: vision/analyzer
  - 下游: 无
  - Bash: find . -name "vision.py" -path "*/tools/*"

- [x] GraphRAG 工具 (mcp/tools/graphrag.py)
  - 上游: graphrag/builder, graphrag/qa
  - 下游: 无
  - Bash: find . -name "graphrag.py" -path "*/tools/*"

---

## Utils 模块

- [x] FileOps 类定义 (utils/file_ops.py)
  - 上游: 无
  - 下游: file_ops/*
  - Bash: find . -name "file_ops.py" -path "*/utils/*"

- [x] 读取文件 (utils/file_ops/read.py)
  - 上游: 无
  - 下游: file_ops.py
  - Bash: find . -name "read.py" -path "*/file_ops/*"

- [x] 写入文件 (utils/file_ops/write.py)
  - 上游: 无
  - 下游: file_ops.py
  - Bash: find . -name "write.py" -path "*/file_ops/*"

- [x] 列出目录 (utils/file_ops/list_dir.py)
  - 上游: 无
  - 下游: file_ops.py
  - Bash: find . -name "list_dir.py" -path "*/file_ops/*"

- [x] 查找文件 (utils/file_ops/find_files.py)
  - 上游: 无
  - 下游: file_ops.py
  - Bash: find . -name "find_files.py" -path "*/file_ops/*"

- [x] StringOps 类定义 (utils/string_ops.py)
  - 上游: 无
  - 下游: string_ops/*
  - Bash: find . -name "string_ops.py" -path "*/utils/*"

- [x] 截断字符串 (utils/string_ops/truncate.py)
  - 上游: 无
  - 下游: string_ops.py
  - Bash: find . -name "truncate.py" -path "*/string_ops/*"

- [x] 转义字符串 (utils/string_ops/escape.py)
  - 上游: 无
  - 下游: string_ops.py
  - Bash: find . -name "escape.py" -path "*/string_ops/*"

- [x] 格式化字符串 (utils/string_ops/format.py)
  - 上游: 无
  - 下游: string_ops.py
  - Bash: find . -name "format.py" -path "*/string_ops/*"

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
# 添加函数并提交
git add src/module/op.py test/unit/module/test_op.py
git commit -m "feat(module): 添加 op 函数

- 实现 op 函数用于功能 X
- 参数 params: Y, Z
- 上游: module/types.py
- 下游: module.py, test/unit/module/test_op.py
"
```

### 使用 DeepWiki 查询问题

当遇到 Claude Code 相关问题时，使用 deepwiki MCP 查询：

```
https://deepwiki.com/anthropics/claude-code
```
