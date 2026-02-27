# ============================================================================
# 文件: CONTRIBUTING.md
# 描述: 贡献指南
#
# Bash 快速定位:
#   find . -name "CONTRIBUTING.md"
# ============================================================================

# 贡献指南

感谢您对 Claude Code MCP Toolkit 的兴趣！

## 开发环境

### 前置要求

- Python >= 3.10
- uv (Python 包管理器)

### 设置开发环境

```bash
# 克隆仓库
git clone https://github.com/1850298154/claude_code_mcp.git
cd claude_code_mcp

# 安装依赖（开发模式）
uv sync --dev

# 运行测试
cd test
PYTHONPATH=".." uv run pytest . -v
```

## 开发规范

### 渐进披露原则

本项目采用渐进披露架构：

- **一个文件只做一件事**：每个文件专注于单一功能
- **原子化组织**：每个函数/类放在独立文件中
- **文件头明确依赖**：使用统一的文件头模板
- **Bash 可定位**：所有文件可通过 bash 命令快速定位

### 文件头模板

源代码文件使用以下模板：

```python
# ============================================================================
# 文件: src/module/submodule/file.py
# 描述: 一句话描述
#
# 上游依赖:
#   - src/other/module.py  (类/函数)
#
# 下游封装:
#   - src/module/submodule/another_op.py
#
# Bash 快速定位:
#   find . -name "file.py" -path "*/src/*"
# ============================================================================
```

测试文件使用以下模板：

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

### 目录结构

```
claude_code_mcp/
├── src/                    # 源代码
│   ├── core/               # 核心类型
│   ├── claude_meta/        # Claude Meta
│   ├── academic/           # 学术搜索
│   ├── vision/             # 视觉分析
│   ├── graphrag/           # 知识图谱
│   ├── mcp/                # MCP 服务器
│   └── utils/              # 通用工具
│
├── test/                   # 测试
│   ├── unit/               # 单元测试
│   ├── integration/        # 集成测试
│   └── conftest.py        # pytest fixtures
│
├── examples/               # 使用示例
├── dev/                    # 开发文档
└── README.md              # 项目文档
```

## 代码风格

- 使用 `|` 语法进行类型注解（Python 3.10+）
- 最大行长度：88 字符
- 使用 4 空格缩进
- 导入按标准库、第三方、本地分组

## 测试规范

### 测试位置

测试应与源代码结构对应：

```
src/module/submodule/file.py  →  test/unit/module/submodule/test_file.py
```

### 测试运行

```bash
# 从 test 目录运行
cd test
PYTHONPATH=".." uv run pytest . -v

# 运行特定模块测试
uv run pytest unit/claude_meta/reader -v

# 运行并生成覆盖率报告
uv run pytest . --cov=../src --cov-report=html
```

## Git 提交规范

### 提交消息格式

```
<type>(<scope>): <description>

# 上游依赖
#   - path/to/file.py  (函数/类)
#
# 下游封装
#   - path/to/file.py  (函数/类)
#
# Bash 快速定位
#   find . -name "file.py" -path "*/path/*"

# 改动内容
#   - 具体改动列表
```

### 提交类型

- `feat`: 新功能
- `fix`: 修复 bug
- `test`: 添加/修改测试
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构（不影响功能）
- `build`: 构建系统或依赖变更
- `chore`: 其他杂项

### 提交示例

```
feat(academic): 添加论文搜索功能

# 上游依赖
#   - academic/semantic/client.py
#   - academic/types.py
#
# 下游封装
#   - examples/academic_usage.py
#
# Bash 快速定位
#   find . -name "search_papers.py" -path "*/academic/*"

# 改动内容
#   - 新增 academic/scholar/search_papers.py
#   - 更新 academic/scholar.py 添加 search_papers 方法
#   - 添加对应测试
```

## 添加新功能

### 1. 创建功能分支

```bash
git checkout -b feat/your-feature-name
```

### 2. 开发和测试

按照开发规范进行开发，确保：

- 添加了相应的单元测试
- 测试全部通过
- 代码符合项目风格

### 3. 提交更改

```bash
git add .
git commit -m "feat(scope): 添加新功能"
```

### 4. 推送并创建 Pull Request

```bash
git push origin feat/your-feature-name
# 然后在 GitHub 上创建 PR
```

## 报告问题

如果您发现 bug 或有功能建议，请：

1. 在 GitHub 上创建 Issue
2. 清晰描述问题
3. 提供复现步骤
4. 附上相关日志或截图

## 许可证

通过提交 PR，您同意您的贡献将在 MIT 许可证下发布。

---

感谢您的贡献！
