# Types Module

> 类型定义模块

## 子模块

| 模块 | 路径 | 描述 | Bash 定位 |
|------|------|------|-----------|
| Claude Types | `core/types/claude/` | Claude 相关类型 | `find . -path "*/core/types/claude/*.py"` |
| FileInfo | `core/types/file_info.py` | FileInfo 数据结构 | `find . -name "file_info.py"` |

## 结构

```
types/
├── README.md              # 本文件
├── claude/                # Claude 相关类型
│   ├── README.md
│   ├── message.py         # Message 数据结构
│   ├── conversation.py    # Conversation 数据结构
│   └── session.py         # Session 数据结构
└── file_info.py           # FileInfo 数据结构
```
