# ============================================================================
# 文件: src/utils/file_ops/find_files.py
# 描述: 查找文件函数
#
# 上游依赖: 无
# 下游封装: utils/file_ops.py (FileOps.find_files)
#
# Bash 快速定位:
#   find . -name "find_files.py" -path "*/file_ops/*"
# ============================================================================

from pathlib import Path
from typing import List


def find_files(pattern: str, dir_path: Path | str = ".") -> List[str]:
    """查找文件

    Args:
        pattern: 文件匹配模式
        dir_path: 搜索目录

    Returns:
        匹配的文件列表
    """
    if isinstance(dir_path, Path):
        dir_path = str(dir_path)

    directory = Path(dir_path)
    if not directory.exists():
            return []

    return [str(f) for f in directory.rglob(pattern) if f.is_file()]
