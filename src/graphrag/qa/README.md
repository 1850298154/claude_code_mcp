# QA System Module

> 问答系统模块

## 子模块

| 组件 | 路径 | 描述 | Bash 定位 |
|------|------|------|-----------|
| QA System | `qa_system.py` | QASystem 数据结构定义 | `find . -name "qa_system.py" -path "*/qa/*"` |
| QA Ops | `qa/` | QA 操作集合 | `find . -path "*/qa/qa/*.py"` |

## 操作列表

| 操作 | 文件 | 描述 | Bash 定位 |
|------|------|------|-----------|
| ask | `ask.py` | 提问 | `find . -name "ask.py" -path "*/qa/qa/*"` |
| retrieve | `retrieve.py` | 检索相关内容 | `find . -name "retrieve.py" -path "*/qa/qa/*"` |
| generate_answer | `generate_answer.py` | 生成答案 | `find . -name "generate_answer.py" -path "*/qa/qa/*"` |

## 结构

```
qa/
├── README.md              # 本文件
├── qa_system.py           # QASystem 数据结构定义
└── qa/
    ├── README.md
    ├── ask.py             # 提问
    ├── retrieve.py        # 检索相关内容
    └── generate_answer.py # 生成答案
```
