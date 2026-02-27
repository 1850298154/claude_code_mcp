# ============================================================================
# 文件: src/utils/file_ops.py
# 描述: FileOps 类定义，用于文件操作
#
# 上游依赖: 无
# 下游封装: file_ops/*
#
# Bash 快速定位:
#   find . -name "file_ops.py" -path "*/utils/*"
# ============================================================================

from pathlib import Path
from typing import List, Optional


class FileOps:
    """File Operations - 文件操作工具

    提供常用的文件操作功能。
    """

    def read(self, file_path: Path | str) -> str:
        """读取文件

        实现位置: file_ops/read.py

        Args:
            file_path: 文件路径

        Returns:
            文件内容
        """
        if isinstance(file_path, Path):
            file_path = str(file_path)

        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def write(self, file_path: Path | str, content: str) -> None:
        """写入文件

        实现位置: file_ops/write.py

        Args:
            file_path: 文件路径
            content: 文件内容
        """
        if isinstance(file_path, Path):
            file_path = str(file_path)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    def list_dir(self, dir_path: Path | str) -> List[str]:
        """列出目录

        实现位置: file_ops/list_dir.py

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

    def find_files(self, pattern: str, dir_path: Path | str = ".") -> List[str]:
        """查找文件

        实现位置: file_ops/find_files.py

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
