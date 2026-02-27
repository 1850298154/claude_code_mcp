# Test Directory

> 渐进式披露的测试目录

## 测试结构

```
test/
├── README.md            # 本文件
├── conftest.py          # Pytest 共享 fixture
├── __init__.py          # 测试包初始化
│
├── unit/                # 单元测试
│   ├── core/            # 核心模块测试
│   ├── claude_meta/     # ClaudeMeta 测试
│   ├── academic/        # Academic 测试
│   ├── vision/          # Vision 测试
│   └── graphrag/        # GraphRAG 测试
│
└── integration/         # 集成测试
```

## 运行测试

```bash
# 从 test 目录启动所有测试
cd test && pytest . -v

# 只运行单元测试
pytest test/unit -v

# 只运行集成测试
pytest test/integration -v

# 运行特定模块测试
pytest test/unit/claude_meta/reader -v

# 运行并查看覆盖率
pytest . --cov=.. --cov-report=html
```

## 测试命名规则

| 模式 | 说明 |
|------|------|
| `test_module.py` | 测试类定义 |
| `test_func_name.py` | 测试单个函数 |
| `test_module_full.py` | 集成测试 |
