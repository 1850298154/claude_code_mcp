# ============================================================================
# 文件: claude_meta/parser/parse_memory.py
# 描述: 解析记忆文件，返回记忆内容
#
# 上游依赖: 无
# 下游封装: reader/get_memory.py
# Bash 快速定位: find . -name "parse_memory.py"
# ============================================================================

from pathlib import Path


def parse_memory(file_path: Path) -> str:
    """解析记忆文件

    Args:
        file_path: 记忆文件路径

    Returns:
        记忆内容字符串
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
