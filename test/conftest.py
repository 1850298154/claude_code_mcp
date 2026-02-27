# ============================================================================
# 文件: test/conftest.py
# 描述: Pytest 共享 fixture
#
# 上游依赖: pytest
# 下游封装: 所有测试文件
# Bash 快速定位: find . -name "conftest.py" -path "*/test/*"
# ============================================================================

import pytest
from pathlib import Path
from datetime import datetime
import tempfile
import shutil
from typing import Dict, Any


@pytest.fixture
def temp_dir():
    """临时目录 fixture"""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_claude_dir(temp_dir: Path):
    """模拟 ~/.claude 目录结构"""
    claude_dir = temp_dir / ".claude"
    claude_dir.mkdir()

    # 创建 history.json
    history_path = claude_dir / "history.json"
    history_path.write_text("""[
    {"query": "帮我实现一个用户登录功能", "timestamp": "2024-01-01T10:00:00Z", "project": "my-app"},
    {"query": "如何优化数据库查询", "timestamp": "2024-01-02T14:30:00Z", "project": "my-app"}
]""")

    # 创建 projects 目录和会话文件
    projects_dir = claude_dir / "projects"
    projects_dir.mkdir()

    project_dir = projects_dir / "my-app"
    project_dir.mkdir()

    session_dir = project_dir
    session_file = session_dir / "session-001.json"
    session_file.write_text("""{
    "id": "session-001",
    "project": "my-app",
    "working_directory": "/home/user/my-app",
    "started_at": "2024-01-01T10:00:00Z",
    "ended_at": "2024-01-01T11:30:00Z",
    "status": "completed",
    "messages": [
        {
            "id": "msg-001",
            "role": "user",
            "content": "帮我实现一个用户登录功能",
            "timestamp": "2024-01-01T10:00:00Z"
        },
        {
            "id": "msg-002",
            "role": "assistant",
            "content": "我来帮你实现用户登录功能...",
            "timestamp": "2024-01-01T10:01:00Z"
        }
    ]
}""")

    # 创建中断的会话
    session_file_interrupted = session_dir / "session-002.json"
    session_file_interrupted.write_text("""{
    "id": "session-002",
    "project": "my-app",
    "working_directory": "/home/user/my-app",
    "started_at": "2024-01-02T14:30:00Z",
    "ended_at": null,
    "status": "interrupted",
    "messages": [
        {
            "id": "msg-003",
            "role": "user",
            "content": "如何优化数据库查询",
            "timestamp": "2024-01-02T14:30:00Z"
        }
    ]
}""")

    # 创建 debug 目录
    debug_dir = claude_dir / "debug"
    debug_dir.mkdir()

    debug_file = debug_dir / "session-001.txt"
    debug_file.write_text("Debug log for session-001")

    # 创建 session-env 目录
    session_env_dir = claude_dir / "session-env"
    session_env_dir.mkdir()

    env_dir = session_env_dir / "session-001"
    env_dir.mkdir()

    env_file = env_dir / "env.json"
    env_file.write_text("""{
    "session_id": "session-001",
    "model": "claude-opus-4-6",
    "temperature": 0.7
}""")

    # 创建 memory 目录
    memory_dir = claude_dir / "memory"
    memory_dir.mkdir()

    memory_file = memory_dir / "MEMORY.md"
    memory_file.write_text("""# Memory

## Project Context
my-app: 用户登录功能已实现
""")

    yield claude_dir


@pytest.fixture
def sample_conversation():
    """示例会话数据"""
    return {
        "id": "session-001",
        "project": "my-app",
        "working_directory": "/home/user/my-app",
        "started_at": "2024-01-01T10:00:00Z",
        "ended_at": "2024-01-01T11:30:00Z",
        "status": "completed",
        "messages": [
            {
                "id": "msg-001",
                "role": "user",
                "content": "帮我实现一个用户登录功能",
                "timestamp": "2024-01-01T10:00:00Z"
            },
            {
                "id": "msg-002",
                "role": "assistant",
                "content": "我来帮你实现用户登录功能...",
                "timestamp": "2024-01-01T10:01:00Z"
            }
        ]
    }


@pytest.fixture
def sample_message():
    """示例消息数据"""
    return {
        "id": "msg-001",
        "role": "user",
        "content": "帮我实现一个用户登录功能",
        "timestamp": "2024-01-01T10:00:00Z"
    }
