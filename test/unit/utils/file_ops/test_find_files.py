# ============================================================================
# 文件: test/unit/utils/file_ops/test_find_files.py
# 描述: 测试 find_files 操作
#
# 测试对象: utils/file_ops/find_files.py
#
# Bash 快速定位:
#   find test -name "test_find_files.py" -path "*/utils/file_ops/*"
# ============================================================================

import pytest
from pathlib import Path
from tempfile import TemporaryDirectory

from utils.file_ops.find_files import find_files


class TestFindFiles:
    """测试 find_files 操作"""

    def test_find_files_with_pattern(self):
        """测试使用模式查找文件"""
        # Given: 临时目录和多种类型文件
        with TemporaryDirectory() as tmp_dir:
            (Path(tmp_dir) / "file1.txt").write_text("content1")
            (Path(tmp_dir) / "file2.py").write_text("content2")
            (Path(tmp_dir) / "file3.txt").write_text("content3")
            (Path(tmp_dir) / "file4.py").write_text("content4")

            # When: 查找 .py 文件
            result = find_files(Path(tmp_dir), pattern="*.py", recursive=False)

            # Then: 只返回 .py 文件
            assert len(result) == 2
            assert all(f.suffix == ".py" for f in result)

    def test_find_files_recursive(self):
        """测试递归查找文件"""
        # Given: 嵌套目录结构
        with TemporaryDirectory() as tmp_dir:
            (Path(tmp_dir) / "file1.txt").write_text("content1")
            subdir = Path(tmp_dir) / "subdir"
            subdir.mkdir()
            (subdir / "file2.txt").write_text("content2")

            # When: 递归查找 .txt 文件
            result = find_files(Path(tmp_dir), pattern="*.txt", recursive=True)

            # Then: 返回所有 .txt 文件
            assert len(result) == 2
            assert any("file1.txt" in str(f) for f in result)
            assert any("file2.txt" in str(f) for f in result)

    def test_find_files_no_matches(self):
        """测试无匹配结果"""
        # Given: 临时目录
        with TemporaryDirectory() as tmp_dir:
            (Path(tmp_dir) / "file.txt").write_text("content")

            # When: 查找不存在的模式
            result = find_files(Path(tmp_dir), pattern="*.xyz", recursive=True)

            # Then: 返回空列表
            assert result == []
