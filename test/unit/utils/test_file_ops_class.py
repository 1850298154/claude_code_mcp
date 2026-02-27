# ============================================================================
# 文件: test/unit/utils/test_file_ops_class.py
# 描述: 测试 FileOps 类
#
# 测试对象: utils/file_ops.py
#
# Bash 快速定位:
#   find test -name "test_file_ops_class.py"
# ============================================================================

import pytest
from pathlib import Path
from tempfile import TemporaryDirectory

from utils.file_ops import FileOps


class TestFileOpsClass:
    """测试 FileOps 类"""

    def test_file_ops_read_static(self):
        """测试 FileOps.read 静态方法"""
        # Given: 临时文件
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test.txt"
            file_path.write_text("Hello")

            # When: 使用静态方法读取
            content = FileOps.read(file_path)

            # Then: 返回正确内容
            assert content == "Hello"

    def test_file_ops_write_static(self):
        """测试 FileOps.write 静态方法"""
        # Given: 临时目录
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test.txt"

            # When: 使用静态方法写入
            FileOps.write(file_path, "Content")

            # Then: 文件被写入
            assert file_path.exists()
            assert file_path.read_text() == "Content"

    def test_file_ops_list_dir_static(self):
        """测试 FileOps.list_dir 静态方法"""
        # Given: 临时目录
        with TemporaryDirectory() as tmp_dir:
            (Path(tmp_dir) / "file1.txt").write_text("content1")

            # When: 使用静态方法列出
            items = FileOps.list_dir(Path(tmp_dir), recursive=False)

            # Then: 返回文件列表
            assert len(items) >= 1

    def test_file_ops_find_files_static(self):
        """测试 FileOps.find_files 静态方法"""
        # Given: 临时目录
        with TemporaryDirectory() as tmp_dir:
            (Path(tmp_dir) / "test.txt").write_text("content")
            (Path(tmp_dir) / "test.py").write_text("code")

            # When: 使用静态方法查找
            files = FileOps.find_files(Path(tmp_dir), pattern="*.py", recursive=False)

            # Then: 返回匹配文件
            assert len(files) == 1
            assert files[0].suffix == ".py"
