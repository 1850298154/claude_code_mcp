# ============================================================================
# 文件: src/utils/file_ops/read.py
# 描述: 读取文件函数
#
# 上游依赖: 无
# 下游封装: utils/file_ops.py (FileOps.read)
#
# Bash 快速定位:
#   find . -name "read.py" -path "*/file_ops/*"
# ============================================================================

from pathlib import Path


def read(file_path: Path | str) -> str:
    """读取文件

    Args:
        file_path: 文件路径

    Returns:
        文件内容
    """
    if isinstance(file_path, Path):
        file_path = str(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
