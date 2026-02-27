# ============================================================================
# 文件: src/utils/file_ops/write.py
# 描述: 写入文件函数
#
# 上游依赖: 无
# 下游封装: utils/file_ops.py (FileOps.write)
#
# Bash 快速定位:
#   find . -name "write.py" -path "*/file_ops/*"
# ============================================================================

from pathlib import Path


def write(file_path: Path | str, content: str) -> None:
    """写入文件

    Args:
        file_path: 文件路径
        content: 文件内容
    """
    if isinstance(file_path, Path):
        file_path = str(file_path)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
