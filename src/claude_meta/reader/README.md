# Reader Operations Module

> ClaudeMetaReader 类定义与操作集合

## 类定义

| 文件 | 类 | Bash 定位 |
|------|------|-----------|
| `__init__.py` | ClaudeMetaReader | `find . -name "__init__.py" -path "*/claude_meta/reader/*"` |

## 操作列表

| 操作 | 文件 | 描述 | Bash 定位 |
|------|------|------|-----------|
| get_sessions | `get_sessions.py` | 获取所有会话 | `find . -name "get_sessions.py"` |
| get_chat_history | `get_chat_history.py` | 获取聊天历史 | `find . -name "get_chat_history.py"` |
| get_project_context | `get_project_context.py` | 获取项目上下文 | `find . -name "get_project_context.py"` |
| get_memory | `get_memory.py` | 获取记忆 | `find . -name "get_memory.py"` |
| restore_session | `restore_session.py` | 恢复指定会话 | `find . -name "restore_session.py"` |

## 结构

```
reader/
├── README.md              # 本文件
├── __init__.py           # ClaudeMetaReader 类定义
├── get_sessions.py        # 获取所有会话
├── get_chat_history.py    # 获取聊天历史
├── get_project_context.py # 获取项目上下文
├── get_memory.py          # 获取记忆
└── restore_session.py     # 恢复指定会话
```
