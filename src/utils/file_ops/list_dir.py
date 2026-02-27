# ============================================================================
# 文件: src/utils/file_ops/list_dir.py
# 描述: 列出目录函数
#
# 上游依赖: 无
# 下游封装: utils/file_ops.py (FileOps.list_dir)
#
# Bash 快速定位:
#   find . -name "list_dir.py" -path "*/file_ops/*"
# ============================================================================

from pathlib import Path
from typing import List


def list_dir(dir_path: Path | str) -> List[str]:
    """列出目录

    Args:
        dir_path: 目录路径

    Returns:
        文件列表
    """
    if isinstance(dir_path, Path):
        dir_path = str(dir_path)

    directory = Path(dir_path)
    if not directory.exists():
            return []

    return [f.name for f in directory.iterdir() if f.is_file()]
