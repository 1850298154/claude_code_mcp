# ============================================================================
# 文件: examples/README.md
# 描述: 使用示例模块说明
#
# 上游依赖: 所有模块
# 下游封装: 无
#
# Bash 快速定位:
#   find . -name "README.md" -path "*/examples/*"
# ============================================================================

# 使用示例

## 示例列表

| 示例 | 文件 | 描述 | Bash 定位 |
|------|------|------|-----------|
| claude_meta_usage.py | Claude Meta 使用示例 | `find . -name "claude_meta_usage.py"` |
| academic_usage.py | Academic 使用示例 | `find . -name "academic_usage.py"` |
| vision_usage.py | Vision 使用示例 | `find . -name "vision_usage.py"` |
| graphrag_usage.py | GraphRAG 使用示例 | `find . -name "graphrag_usage.py"` |
| utils_usage.py | Utils 使用示例 | `find . -name "utils_usage.py"` |

## 结构

```
examples/
├── README.md              # 本文件
├── claude_meta_usage.py   # Claude Meta 模块示例
├── academic_usage.py      # Academic 模块示例
├── vision_usage.py        # Vision 模块示例
├── graphrag_usage.py      # GraphRAG 模块示例
└── utils_usage.py         # Utils 模块示例
```

## 运行示例

```bash
# 运行 Claude Meta 示例
python examples/claude_meta_usage.py

# 运行 Academic 示例
python examples/academic_usage.py

# 运行 Vision 示例
python examples/vision_usage.py

# 运行 GraphRAG 示例
python examples/graphrag_usage.py

# 运行 Utils 示例
python examples/utils_usage.py
```
