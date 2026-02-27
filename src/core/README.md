# Core Module

> 核心基础设施模块

## 模块说明

提供整个项目的基础设施，包括配置管理、日志系统和类型定义。

## 子模块

| 子模块 | 路径 | 描述 | Bash 定位 |
|--------|------|------|-----------|
| Config | `core/config/` | 配置管理（Settings, Paths） | `find . -path "*/core/config/*"` |
| Logger | `core/logger/` | 日志系统 | `find . -path "*/core/logger/*"` |
| Types | `core/types/` | 类型定义 | `find . -path "*/core/types/*"` |

## 依赖关系

```
core/
├── config/        (无上游依赖，下游：所有模块)
├── logger/        (无上游依赖，下游：所有模块)
└── types/         (无上游依赖，下游：所有模块)
```

## 快速操作

```bash
# 查看配置文件
ls core/config/*.py

# 查看类型定义
ls core/types/**/*.py

# 查看日志相关
ls core/logger/*.py
```

## 结构

```
core/
├── README.md              # 本文件
├── config/                # 配置管理
│   ├── README.md          # Config 模块说明
│   ├── settings.py        # Settings 数据结构定义
│   ├── settings/          # Settings 子操作
│   │   ├── README.md
│   │   ├── load.py        # 加载配置
│   │   ├── save.py        # 保存配置
│   │   └── validate.py    # 验证配置
│   └── paths.py           # Paths 数据结构定义
├── logger/                # 日志系统
│   ├── README.md          # Logger 模块说明
│   └── logger.py          # Logger 数据结构定义
└── types/                 # 类型定义
    ├── README.md          # Types 模块说明
    ├── claude/            # Claude 相关类型
    │   ├── README.md
    │   ├── message.py     # Message 数据结构
    │   ├── conversation.py # Conversation 数据结构
    │   └── session.py     # Session 数据结构
    └── file_info.py       # FileInfo 数据结构
```
