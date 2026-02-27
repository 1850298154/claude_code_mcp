# Claude Meta Reader Module

> ~/.claude 元信息读取模块

## 模块说明

读取 `~/.claude` 下的所有元信息，包括聊天历史、项目上下文、记忆等，用于快速恢复中断/异常停止的工作会话。

## 子模块

| 子模块 | 路径 | 描述 | Bash 定位 |
|--------|------|------|-----------|
| Config | `claude_meta/config/` | 配置管理 | `find . -path "*/claude_meta/config/*.py"` |
| Reader | `claude_meta/reader/` | Reader 类定义与操作 | `find . -path "*/claude_meta/reader/*"` |
| Parser | `claude_meta/parser/` | 解析器集合 | `find . -path "*/claude_meta/parser/*.py"` |
| Analyzer | `claude_meta/analyzer/` | 分析器集合 | `find . -path "*/claude_meta/analyzer/*.py"` |

## 依赖关系

```
claude_meta/
├── config/
│   ├── paths.py                       # ClaudeMetaPaths 类定义
│   └── 下游: reader/*
├── reader/
│   ├── __init__.py                    # ClaudeMetaReader 类定义
│   ├── 上游依赖: core/types/claude/*, config/paths.py
│   └── 下游操作:
│       ├── get_chat_history.py         # 获取聊天历史
│       ├── get_project_context.py      # 获取项目上下文
│       ├── get_memory.py              # 获取记忆
│       ├── get_sessions.py            # 获取所有会话
│       └── restore_session.py         # 恢复指定会话
├── parser/
│   ├── 上游依赖: core/types/claude/*
│   └── 下游操作:
│       ├── parse_conversation.py       # 解析对话文件
│       ├── parse_history.py           # 解析历史文件
│       └── parse_memory.py            # 解析记忆文件
└── analyzer/
    ├── 上游依赖: core/types/claude/*
    └── 下游操作:
        ├── detect_interrupted.py       # 检测中断的会话
        ├── extract_context.py          # 提取上下文关键信息
        └── summarize_progress.py       # 总结进度
```

## 快速操作

```bash
# 导入 Reader
from claude_meta.reader import ClaudeMetaReader

# 获取所有会话
reader = ClaudeMetaReader()
sessions = reader.get_sessions()

# 恢复特定会话
session = reader.restore_session(session_id="abc123")

# 获取项目上下文
context = reader.get_project_context(project_name="my-app")

# 检测中断的会话
interrupted = reader.detect_interrupted()

# 总结进度
progress = reader.summarize_progress(session_id="abc123")
```

## 结构

```
claude_meta/
├── README.md              # 本文件
├── config/               # 配置管理
│   ├── README.md
│   └── paths.py          # ClaudeMetaPaths 类定义
├── reader/               # Reader 类定义与操作
│   ├── README.md
│   ├── __init__.py       # ClaudeMetaReader 类定义
│   ├── get_chat_history.py    # 获取聊天历史
│   ├── get_project_context.py # 获取项目上下文
│   ├── get_memory.py          # 获取记忆
│   ├── get_sessions.py        # 获取所有会话
│   └── restore_session.py     # 恢复指定会话
├── parser/               # 解析器
│   ├── README.md
│   ├── parse_conversation.py # 解析对话文件
│   ├── parse_history.py     # 解析历史文件
│   └── parse_memory.py      # 解析记忆文件
└── analyzer/             # 分析器
    ├── README.md
    ├── detect_interrupted.py # 检测中断的会话
    ├── extract_context.py    # 提取上下文关键信息
    └── summarize_progress.py # 总结进度
```

## 典型使用场景

### 1. 恢复中断的工作会话

```python
from claude_meta.reader import ClaudeMetaReader

reader = ClaudeMetaReader()
sessions = reader.get_sessions()
interrupted = reader.detect_interrupted()
if interrupted:
    session = reader.restore_session(interrupted[0].id)
    # 查看进度
    progress = reader.summarize_progress(interrupted[0].id)
    print(progress["next_steps"])
```

### 2. 获取项目上下文

```python
from claude_meta.reader import ClaudeMetaReader

reader = ClaudeMetaReader()
context = reader.get_project_context(project_name="my-app")
print(f"会话数: {context['total_sessions']}")
print(f"消息数: {context['total_messages']}")
```

### 3. 分析工作进度

```python
from claude_meta.reader import ClaudeMetaReader

reader = ClaudeMetaReader()
progress = reader.summarize_progress(session_id="abc123")
print(f"进度: {progress['total_progress']}")
print(f"下一步: {progress['next_steps']}")
```
