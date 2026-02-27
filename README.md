# Claude Code MCP Toolkit

> 渐进式披露的 Claude Code MCP 工具集

## 目录结构

```
claude_code_mcp/
├── src/                    # 源代码
│   ├── core/               # 核心基础设施
│   ├── claude_meta/        # ~/.claude 元信息读取
│   ├── academic/           # 学术搜索
│   ├── vision/             # 视觉分析
│   ├── graphrag/           # 知识图谱
│   ├── mcp/                # MCP 服务器
│   └── utils/              # 通用工具
│
├── test/                   # 测试
│   ├── unit/               # 单元测试
│   ├── integration/        # 集成测试
│   ├── conftest.py        # Pytest fixture
│   └── run.py             # 测试运行脚本
│
├── dev/                    # 开发相关
│   ├── CONVENTIONS.md      # 开发规范
│   ├── TEST_PLAN.md       # 测试计划
│   └── TODO.md           # 项目 TODO（渐进披露）
│
├── examples/               # 使用示例
├── README.md              # 本文件
├── pyproject.toml        # 项目配置
└── .gitignore
```

---

## 快速开始

### 使用 uv 管理

```bash
# 项目已使用 uv 初始化
# 所有命令使用 uv run 执行
```

### 运行测试

```bash
# 从 test 目录运行所有测试
cd test
uv run pytest . -v

# 只运行单元测试
uv run pytest unit -v

# 只运行集成测试
uv run pytest integration -v

# 运行特定模块测试
uv run pytest unit/claude_meta/reader -v

# 运行并查看覆盖率
uv run pytest . --cov=../src --cov-report=html
```

### 运行示例

```bash
uv run python examples/claude_meta_usage.py
```

---

## 核心理念

### 渐进披露原则

```
Claude Code MCP Toolkit/
├── 原则/
│   ├── 一个文件只做一件事
│   ├── 一个文件只含一个函数/数据结构定义
│   ├── 子结构独立到子文件
│   ├── 文件头明确上游依赖与下游封装
│   └── 同名文件夹 = 子内容（渐进披露）
├── 目标/
│   ├── 快速通过 bash 过滤定位
│   ├── 打开任何文件即知上下文
│   ├── 向上追溯来源与依赖
│   └── 向下查找子结构与操作
└── 用途/
    ├── 读取 ~/.claude 元信息
    ├── 恢复中断的工作会话
    ├── 学术搜索与资料获取
    ├── 视觉模型调用
    └── 项目解析为 QA（通过 deepwiki）
```

---

## 模块说明

### Claude Meta (`src/claude_meta/`)

读取 `~/.claude` 下的所有元信息，用于恢复中断的工作会话。

```python
from claude_meta.reader import ClaudeMetaReader

reader = ClaudeMetaReader()
sessions = reader.get_sessions()
interrupted = reader.detect_interrupted()
context = reader.get_project_context("my-app")
```

### Academic (`src/academic/`)

学术论文搜索、BibTeX 获取、引用验证。

```python
from academic.scholar import Scholar

scholar = Scholar()
papers = scholar.search_papers("attention mechanism")
bibtex = scholar.get_bibtex(paper_id="abc123")
```

### Vision (`src/vision/`)

图像分析、对象检测、OCR。

```python
from vision.analyzer import VisionAnalyzer

analyzer = VisionAnalyzer(model="glm4v")
result = analyzer.analyze_image("screenshot.png")
text = analyzer.extract_text("document.png")
```

### GraphRAG (`src/graphrag/`)

知识图谱构建与问答。

```python
from graphrag.builder import GraphBuilder
from graphrag.qa import QASystem

builder = GraphBuilder()
graph = builder.build_from_project("/path/to/project")
qa = QASystem(graph=graph)
answer = qa.ask("这个项目的核心模块是什么？")
```

---

## Bash 快速定位

```bash
# 查找所有 Reader 操作
find . -path "*/reader/*.py" | grep -v __pycache__

# 查找 ClaudeMeta 相关文件
find . -path "*/claude_meta/*" -type f | grep -v __pycache__

# 查找所有测试文件
find test -name "test_*.py"

# 查找特定函数的测试
find test -name "test_get_sessions.py"

# 查找 Scholar 的所有操作
ls src/academic/scholar/*.py

# 查看 GraphRAG QA 系统结构
tree src/graphrag/qa/
```

---

## 文件头模板

### 源代码文件

```python
# ============================================================================
# 文件: src/module/submodule/file.py
# 描述: 一句话描述
#
# 上游依赖:
#   - src/other/module.py  (类/函数)
#   - src/another/module.py (类/函数)
#
# 下游封装:
#   - src/module/submodule/another_op.py
#
# Bash 快速定位:
#   find . -name "file.py" -path "*/src/*"
# ============================================================================
```

### 测试文件

```python
# ============================================================================
# 文件: test/path/to/test_module.py
# 描述: 测试 module 类/函数
#
# 测试对象: src/path/to/module.py
#
# Bash 快速定位:
#   find test -name "test_module.py"
# ============================================================================
```

---

## 开发规范

详细开发规范请参考 `dev/CONVENTIONS.md`：

- 目录结构
- 文件命名规则
- 渐进披露原则
- 代码风格
- 测试规范
- Git 提交规范

## 测试计划

完整测试计划请参考 `dev/TEST_PLAN.md`：

- Claude Meta 模块测试集
- Academic 模块测试集
- Vision 模块测试集
- GraphRAG 模块测试集
- 使用场景测试集

## 项目进度

项目任务管理请参考 `dev/TODO.md`（渐进披露）：

- 模块任务列表
- 上下游依赖
- Bash 定位命令
- 任务完成状态

---

## License

MIT
