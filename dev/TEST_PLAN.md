# 测试计划 (Test Plan)

> 最终测试集 - Claude Code MCP Toolkit

## 测试目标

确保所有功能正确实现，代码原子隔离，同时提供使用示例。

---

## Claude Meta 模块测试集

### 1. 配置测试

| 测试用例 | 描述 | 验证点 |
|---------|------|--------|
| test_paths_default | 测试默认路径初始化 | 路径正确指向 ~/.claude |
| test_paths_custom | 测试自定义路径 | 路径使用自定义值 |
| test_get_session_file | 测试获取会话文件路径 | 路径格式正确 |
| test_get_debug_file | 测试获取调试文件路径 | 路径格式正确 |
| test_get_memory_file | 测试获取记忆文件路径 | 路径格式正确 |

### 2. 解析器测试

| 测试用例 | 描述 | 验证点 |
|---------|------|--------|
| test_parse_conversation_basic | 测试基本会话解析 | 字段正确映射 |
| test_parse_conversation_without_project | 测试无项目会话 | project 为 None |
| test_parse_conversation_multiple_messages | 测试多消息解析 | 所有消息正确解析 |
| test_parse_history_basic | 测试基本历史解析 | 条目正确解析 |
| test_parse_history_without_project | 测试无项目历史 | project 为空字符串 |
| test_parse_memory_from_file | 测试从文件解析记忆 | 内容正确读取 |
| test_parse_memory_empty_file | 测试空文件解析 | 返回空字符串 |

### 3. Reader 测试

| 测试用例 | 描述 | 验证点 |
|---------|------|--------|
| test_get_sessions_empty | 测试空目录获取会话 | 返回空列表 |
| test_get_sessions_with_mock_data | 测试从模拟数据获取会话 | 会话数量和内容正确 |
| test_get_chat_history_with_project | 测试指定项目获取历史 | 消息列表正确 |
| test_get_chat_history_without_project | 测试不指定项目获取历史 | 自动查找项目 |
| test_get_chat_history_not_found | 测试获取不存在的会话 | 返回空列表 |
| test_get_memory_exists | 测试获取存在的记忆 | 记忆内容正确 |
| test_get_memory_not_exists | 测试获取不存在的记忆 | 返回空字符串 |
| test_restore_session_with_project | 测试指定项目恢复会话 | 会话正确恢复 |
| test_restore_session_without_project | 测试不指定项目恢复会话 | 自动查找项目 |
| test_restore_session_not_found | 测试恢复不存在的会话 | 返回 None |
| test_get_project_context | 测试获取项目上下文 | 上下文信息完整 |

### 4. Analyzer 测试

| 测试用例 | 描述 | 验证点 |
|---------|------|--------|
| test_detect_interrupted | 测试检测中断会话 | 返回中断会话列表 |
| test_detect_interrupted_empty | 测试空目录检测中断 | 返回空列表 |
| test_extract_context_basic | 测试基本上下文提取 | 上下文信息完整 |
| test_extract_context_with_files | 测试提取文件引用 | 文件列表正确 |
| test_extract_context_with_keywords | 测试提取任务关键词 | 关键词正确识别 |
| test_summarize_progress_basic | 测试基本进度总结 | 进度信息完整 |
| test_summarize_progress_interrupted | 测试中断会话进度总结 | 状态正确 |

### 5. 集成测试

| 测试用例 | 描述 | 验证点 |
|---------|------|--------|
| test_full_workflow | 测试完整工作流 | 从获取会话到总结进度全程畅通 |
| test_detect_and_summarize_interrupted | 测试检测和总结中断 | 端到端功能正常 |

---

## 使用场景测试集

### 场景 1: 查询指定 ID 的历史对话

```python
from claude_meta.reader import ClaudeMetaReader

reader = ClaudeMetaReader()
messages = reader.get_chat_history(session_id="session-001")
assert len(messages) > 0
assert messages[0].role.value == "user"
```

### 场景 2: 恢复中断的工作会话

```python
reader = ClaudeMetaReader()
interrupted = reader.detect_interrupted()
if interrupted:
    session = reader.restore_session(interrupted[0].id)
    progress = reader.summarize_progress(interrupted[0].id)
    assert progress["status"] == "interrupted"
```

### 场景 3: 获取项目执行信息

```python
reader = ClaudeMetaReader()
context = reader.get_project_context(project_name="my-app")
assert context["total_sessions"] > 0
assert context["total_messages"] > 0
```

### 场景 4: 读取记忆内容

```python
reader = ClaudeMetaReader()
memory = reader.get_memory()
assert len(memory) > 0
```

---

## 运行测试

```bash
# 从 test 目录运行所有测试
cd test
uv run pytest . -v

# 运行特定模块测试
uv run pytest unit/claude_meta/reader -v

# 运行并查看覆盖率
uv run pytest . --cov=../src --cov-report=html
```
