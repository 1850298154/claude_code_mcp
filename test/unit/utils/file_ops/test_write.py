# ============================================================================
# 文件: test/unit/utils/file_ops/test_write.py
# 描述: 测试 write 操作
#
# 测试对象: utils/file_ops/write.py
#
# Bash 快速定位:
#   find test -name "test_write.py" -path "*/utils/file_ops/*"
# ============================================================================

import pytest
from pathlib import Path
from tempfile import TemporaryDirectory

from utils.file_ops.write import write


class TestWrite:
    """测试 write 操作"""

    def test_write_file(self):
        """测试写入文件"""
        # Given: 临时目录和内容
        content = "Hello, World!"
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test.txt"

            # When: 写入文件
            write(file_path, content)

            # Then: 文件被写入
            assert file_path.exists()
            assert file_path.read_text() == content

    def test_write_overwrite(self):
        """测试覆盖写入"""
        # Given: 已有文件
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test.txt"
            file_path.write_text("old content")

            # When: 覆盖写入
            write(file_path, "new content")

            # Then: 内容被覆盖
            assert file_path.read_text() == "new content"

    def test_write_create_parent_dirs(self):
        """测试创建父目录"""
        # Given: 不存在的父目录
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "subdir" / "test.txt"

            # When: 写入文件
            write(file_path, "content")

            # Then: 父目录和文件被创建
            assert file_path.exists()
            assert file_path.read_text() == "content"
