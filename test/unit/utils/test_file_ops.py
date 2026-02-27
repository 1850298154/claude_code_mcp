# ============================================================================
# 文件: test/unit/utils/test_file_ops.py
# 描述: 测试 FileOps 类
#
# 测试对象: utils/file_ops.py
#
# Bash 快速定位:
#   find test -name "test_file_ops.py"
# ============================================================================

import pytest
from utils.file_ops import FileOps


class TestFileOps:
    """测试 FileOps 类"""

    def test_read(self, tmp_dir):
        """测试读取文件"""
        # Given: 临时目录和测试文件
        test_file = tmp_dir / "test.txt"
        test_file.write_text("test content")

        # When: 读取文件
        ops = FileOps()
        content = ops.read(test_file)

        # Then: 内容正确
        assert content == "test content"

    def test_write(self, tmp_dir):
        """测试写入文件"""
        # Given: 临时目录
        test_file = tmp_dir / "write_test.txt"

        # When: 写入文件
        ops = FileOps()
        ops.write(test_file, "new content")

        # Then: 内容正确
        assert ops.read(test_file) == "new content"

    def test_list_dir(self, tmp_dir):
        """测试列出目录"""
        # Given: 临时目录和测试文件
        test_file = tmp_dir / "list_test.txt"
        test_file.write_text("test")

        # When: 列出目录
        ops = FileOps()
        files = ops.list_dir(tmp_dir)

        # Then: 包含测试文件
        assert "list_test.txt" in files

    def test_find_files(self, tmp_dir):
        """测试查找文件"""
        # Given: 临时目录
        test_dir = tmp_dir / "find_test.txt"
        test_file.write_text("test")
        (tmp_dir / "match.txt").write_text("match")

        # When: 查找文件
        ops = FileOps()
        files = ops.find_files("*.txt", tmp_dir)

        # Then: 包含匹配文件
        assert len(files) >= 2  # test.txt 和 match.txt
