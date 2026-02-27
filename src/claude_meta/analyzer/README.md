# Analyzer Module

> 分析器集合

## 子模块

| 分析器 | 文件 | 描述 | Bash 定位 |
|--------|------|------|-----------|
| detect_interrupted | `detect_interrupted.py` | 检测中断的会话 | `find . -name "detect_interrupted.py"` |
| extract_context | `extract_context.py` | 提取上下文关键信息 | `find . -name "extract_context.py"` |
| summarize_progress | `summarize_progress.py` | 总结进度 | `find . -name "summarize_progress.py"` |

## 结构

```
analyzer/
├── README.md              # 本文件
├── detect_interrupted.py # 检测中断的会话
├── extract_context.py     # 提取上下文关键信息
└── summarize_progress.py  # 总结进度
```
