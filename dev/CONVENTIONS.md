# 开发规范 (Development Conventions)

> 渐进式披露的 Claude Code MCP Toolkit 开发规范

## 目录结构

```
claude_code_mcp/
├── src/                    # 源代码
│   ├── core/               # 核心模块
│   ├── claude_meta/        # Claude 元信息读取
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
│   ├── CONVENTIONS.md      # 本文件 - 开发规范
│   ├── TEST_PLAN.md       # 测试计划
│   └── TODO.md           # 项目 TODO（渐进披露）
│
├── examples/               # 使用示例
├── README.md              # 项目说明
├── pyproject.toml        # 项目配置（uv）
└── .gitignore
```

---

## 文件命名规则

| 模式 | 说明 | 示例 |
|------|------|------|
| `module.py` | 数据结构/类定义 | `scholar.py` = Scholar 类 |
| `module/` | 子操作集合 | `scholar/` = 操作文件夹 |
| `module/__init__.py` | 模块入口（避免同名冲突） | `reader/__init__.py` = Reader 类定义 |
| `module/op.py` | 具体操作函数 | `reader/get_sessions.py` |
| `test_*.py` | 测试文件 | `test_get_sessions.py` |
| `test_*_full.py` | 集成测试 | `test_claude_meta_full.py` |

---

## 文件头模板

### 源代码文件模板

```python
# ============================================================================
# 文件: src/module/submodule/file.py
# 描述: 一句话描述此文件的功能
#
# 上游依赖:
#   - src/other/module.py  (类/函数)
#   - src/another/module.py (类/函数)
#
# 下游封装:
#   - src/module/submodule/another_op.py (使用此文件的函数)
#   - src/mcp/tools/module.py (MCP 工具封装)
#
# Bash 快速定位:
#   find . -name "file.py" -path "*/src/*"
# ============================================================================
```

### 测试文件模板

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

## 渐进披露原则

### 单一职责
- 一个文件只做一件事
- 一个函数只做一件事
- 一个类只做一件事

### 原子隔离
- 每个函数独立到单独文件
- 子结构独立到子文件夹
- 通过 `__init__.py` 导入模块接口

### 上下文可追溯
- 文件头必须列出上游依赖
- 文件头必须列出下游封装
- 使用 Bash 命令快速定位同类文件

---

## 代码风格

### 类型注解
```python
# 使用 | 语法（Python 3.10+）
def func(x: str | None = None) -> str:
    return x or ""
```

### 导入顺序
```python
# 标准库
from pathlib import Path
from datetime import datetime

# 第三方库
import pytest

# 本地模块
from core.types.claude.message import Message
from claude_meta.config.paths import ClaudeMetaPaths
```

### 文档字符串
```python
def get_sessions(paths: ClaudeMetaPaths) -> List[Conversation]:
    """获取所有会话

    Args:
        paths: ClaudeMetaPaths 路径配置

    Returns:
        会话列表
    """
    # 实现
```

---

## 测试规范

### 测试命名
- 单元测试：`test_<module>.py` 或 `test_<function>.py`
- 集成测试：`test_<module>_full.py`

### 测试结构（Given-When-Then）
```python
def test_get_sessions_empty():
    """测试空目录获取会话"""
    # Given: 设置测试数据
    paths = ClaudeMetaPaths(temp_dir)

    # When: 执行被测函数
    sessions = get_sessions(paths)

    # Then: 验证结果
    assert sessions == []
```

### Fixture 使用
```python
# 使用 conftest.py 中的 fixture
def test_with_mock_data(mock_claude_dir):
    paths = ClaudeMetaPaths(mock_claude_dir)
    # 测试代码
```

---

## Git 提交规范

### 提交消息格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type 类型
- `feat`: 新功能
- `fix`: 修复 bug
- `test`: 添加/修改测试
- `docs`: 文档更新
- `refactor`: 重构
- `style`: 代码风格修改
- `chore`: 构建/工具配置

### 提交原则（渐进披露）

#### 频繁提交
- 每完成一个功能单元立即提交
- 每修复一个问题立即提交
- 每添加一个测试立即提交
- 避免长时间不提交导致代码堆积

#### 清晰的提交消息
```
feat(claude_meta): 添加 get_sessions 函数

- 实现 get_sessions 函数用于获取所有会话
- 添加参数 paths: ClaudeMetaPaths
- 返回 List[Conversation] 类型

上游依赖:
  - src/claude_meta/config/paths.py
  - src/core/types/claude/conversation.py

下游影响:
  - src/claude_meta/reader/__init__.py
  - test/unit/claude_meta/reader/test_get_sessions.py

Bash 快速定位:
  find . -name "get_sessions.py"
```

#### 渐进披露的提交消息
提交消息应包含：
1. **简要标题**：描述做了什么
2. **详细描述**：
   - 实现的功能/修复的问题
   - 使用的参数/返回类型
3. **上下游关系**：
   - 上游依赖的模块
   - 下游影响的模块
4. **快速定位**：Bash 命令找到相关文件

#### 示例
```
feat(claude_meta): 添加 detect_interrupted 函数

实现 detect_interrupted 函数，用于检测 ended_at 为 None 的会话。

上游依赖:
  - src/claude_meta/reader/get_sessions.py
  - src/core/types/claude/conversation.py

下游影响:
  - src/claude_meta/reader/__init__.py
  - test/unit/claude_meta/analyzer/test_detect_interrupted.py

Bash 快速定位:
  find . -name "detect_interrupted.py"

Closes #1
```

```
test(claude_meta): 添加 parse_conversation 单元测试

添加 parse_conversation 函数的单元测试，包括:
- 基本会话解析测试
- 无项目会话解析测试
- 多消息会话解析测试

测试对象: src/claude_meta/parser/parse_conversation.py

Bash 快速定位:
  find test -name "test_parse_conversation.py"
```

```
docs(dev): 更新 TODO.md 标记 Claude Meta 完成状态

- 标记 core/types 完成
- 标记 config/paths 完成
- 标记 parser/* 完成
- 标记 reader/* 完成
- 标记 analyzer/* 完成

上游: src/claude_meta/*
下游: 下一步开始 academic 模块

Bash 快速定位:
  find . -name "TODO.md"
```

---

## 使用 uv 管理项目

### 初始化
```bash
# 项目已使用 uv 初始化
# 所有命令使用 uv python 执行
```

### 运行测试
```bash
cd test
uv run pytest . -v
```

### 运行示例
```bash
uv run python examples/claude_meta_usage.py
```

---

## 开发流程

1. 从 `dev/TODO.md` 选择任务
2. 创建对应的源代码文件（遵循命名规则）
3. 编写对应的测试文件
4. 运行测试：`cd test && uv run pytest`
5. 更新 `dev/TODO.md` 标记任务状态
6. 提交代码（遵循 Git 提交规范）
