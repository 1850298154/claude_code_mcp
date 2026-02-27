# Utils Module

> 通用工具模块

## 模块说明

提供通用的工具函数，包括文件操作、字符串处理等基础功能。

## 子模块

| 子模块 | 路径 | 描述 | Bash 定位 |
|--------|------|------|-----------|
| File Ops | `utils/file_ops.py` | FileOps 数据结构定义 | `find . -name "file_ops.py" -path "*/utils/*"` |
| File Ops | `utils/file_ops/` | 文件操作集合 | `find . -path "*/utils/file_ops/*.py"` |
| String Ops | `utils/string_ops.py` | StringOps 数据结构定义 | `find . -name "string_ops.py" -path "*/utils/*"` |
| String Ops | `utils/string_ops/` | 字符串操作集合 | `find . -path "*/utils/string_ops/*.py"` |

## 依赖关系

```
utils/
├── file_ops/
│   ├── 上游依赖: 无
│   └── 下游操作:
│       ├── read.py        # 读取文件
│       ├── write.py       # 写入文件
│       ├── list_dir.py    # 列出目录
│       └── find_files.py  # 查找文件
└── string_ops/
    ├── 上游依赖: 无
    └── 下游操作:
        ├── truncate.py    # 截断字符串
        ├── escape.py      # 转义字符串
        └── format.py      # 格式化字符串
```

## 快速操作

```bash
# 读取文件
python -m utils.file_ops.read --path file.txt

# 查找文件
python -m utils.file_ops.find_files --pattern "*.py" --path .

# 截断字符串
python -m utils.string_ops.truncate --text "long text..." --max-len 50
```

## 结构

```
utils/
├── README.md              # 本文件
├── file_ops.py            # FileOps 数据结构定义
├── file_ops/              # 文件操作
│   ├── README.md
│   ├── read.py            # 读取文件
│   ├── write.py           # 写入文件
│   ├── list_dir.py        # 列出目录
│   └── find_files.py      # 查找文件
└── string_ops/            # 字符串操作
    ├── README.md
    ├── string_ops.py      # StringOps 数据结构定义
    ├── truncate.py        # 截断字符串
    ├── escape.py          # 转义字符串
    └── format.py          # 格式化字符串
```
