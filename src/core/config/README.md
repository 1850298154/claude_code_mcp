# Config Module

> 配置管理模块

## 子模块

| 文件 | 描述 | Bash 定位 |
|------|------|-----------|
| `settings.py` | Settings 数据结构定义 | `find . -name "settings.py" -path "*/core/config/*"` |
| `settings/` | Settings 子操作 | `find . -path "*/core/config/settings/*.py"` |
| `paths.py` | Paths 数据结构定义 | `find . -name "paths.py" -path "*/core/config/*"` |

## 结构

```
config/
├── README.md              # 本文件
├── settings.py            # Settings 数据结构定义
├── settings/              # Settings 子操作
│   ├── README.md
│   ├── load.py            # 加载配置
│   ├── save.py            # 保存配置
│   └── validate.py        # 验证配置
└── paths.py               # Paths 数据结构定义
```
