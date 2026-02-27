# ============================================================================
# 文件: test/unit/utils/file_ops/test_list_dir.py
# 描述: 测试 list_dir 操作
#
# 测试对象: utils/file_ops/list_dir.py
#
# Bash 快速定位:
#   find test -name "test_list_dir.py" -path "*/utils/file_ops/*"
# ============================================================================

import pytest
from pathlib import Path
from tempfile import TemporaryDirectory

from utils.file_ops.list_dir import list_dir


class TestListDir:
    """测试 list_dir 操作"""

    def test_list_dir_non_recursive(self):
        """测试非递归列出目录"""
        # Given: 临时目录和文件
        with TemporaryDirectory() as tmp_dir:
            (Path(tmp_dir) / "file1.txt").write_text("content1")
            (Path(tmp_dir) / "file2.txt").write_text("content2")
            subdir = Path(tmp_dir) / "subdir"
            subdir.mkdir()
            (subdir / "file3.txt").write_text("content3")

            # When: 非递归列出
            result = list_dir(Path(tmp_dir), recursive=False)

            # Then: 只返回顶层文件/目录
            assert len(result) == 3
            assert any("file1.txt" in str(p) for p in result)
            assert any("file2.txt" in str(p) for p in result)
            assert any("subdir" in str(p) for p in result)

    def test_list_dir_recursive(self):
        """测试递归列出目录"""
        # Given: 临时目录和嵌套文件
        with TemporaryDirectory() as tmp_dir:
            (Path(tmp_dir) / "file1.txt").write_text("content1")
            subdir = Path(tmp_dir) / "subdir"
            subdir.mkdir()
            (subdir / "file2.txt").write_text("content2")

            # When: 递归列出
            result = list_dir(Path(tmp_dir), recursive=True)

            # Then: 返回所有文件
            assert len(result) == 3  # 包括目录
            assert any("file1.txt" in str(p) for p in result)
            assert any("file2.txt" in str(p) for p in result)

    def test_list_dir_empty(self):
        """测试列出空目录"""
        # Given: 空目录
        with TemporaryDirectory() as tmp_dir:
            # When: 列出空目录
            result = list_dir(Path(tmp_dir), recursive=False)

            # Then: 返回空列表
            assert result == []
