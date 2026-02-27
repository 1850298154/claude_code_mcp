# ============================================================================
# 文件: test/unit/utils/file_ops/test_read.py
# 描述: 测试 read 操作
#
# 测试对象: utils/file_ops/read.py
#
# Bash 快速定位:
#   find test -name "test_read.py" -path "*/utils/file_ops/*"
# ============================================================================

import pytest
from pathlib import Path
from tempfile import TemporaryDirectory

from utils.file_ops.read import read


class TestRead:
    """测试 read 操作"""

    def test_read_file(self):
        """测试读取文件"""
        # Given: 临时文件和内容
        content = "Hello, World!"
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test.txt"
            file_path.write_text(content)

            # When: 读取文件
            result = read(file_path)

            # Then: 返回正确内容
            assert result == content

    def test_read_empty_file(self):
        """测试读取空文件"""
        # Given: 空文件
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "empty.txt"
            file_path.write_text("")

            # When: 读取空文件
            result = read(file_path)

            # Then: 返回空字符串
            assert result == ""

    def test_read_with_string_path(self):
        """测试使用字符串路径"""
        # Given: 字符串路径
        with TemporaryDirectory() as tmp_dir:
            file_path = str(Path(tmp_dir) / "test.txt")
            Path(file_path).write_text("content")

            # When: 使用字符串路径读取
            result = read(file_path)

            # Then: 返回正确内容
            assert result == "content"
