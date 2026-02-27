# ============================================================================
# 文件: test/integration/test_utils_full.py
# 描述: Utils 模块完整集成测试
#
# 测试对象: utils/ 整个模块
#
# Bash 快速定位:
#   find test -name "test_utils_full.py"
# ============================================================================

import pytest
from pathlib import Path
import tempfile
import shutil

from utils.file_ops import FileOps
from utils.string_ops import StringOps


class TestUtilsFull:
    """测试 Utils 模块完整集成"""

    def test_file_ops_read_write_workflow(self, tmp_path):
        """测试文件读写工作流"""
        # Given: 临时目录和内容
        test_file = tmp_path / "test.txt"
        content = "Hello, World!"

        # When: 写入文件
        FileOps.write(test_file, content)

        # Then: 文件被写入
        assert test_file.exists()

        # When: 读取文件
        read_content = FileOps.read(test_file)

        # Then: 返回正确内容
        assert read_content == content

    def test_file_ops_list_dir_workflow(self, tmp_path):
        """测试目录列表工作流"""
        # Given: 临时目录和文件
        (tmp_path / "file1.txt").write_text("content1")
        (tmp_path / "file2.txt").write_text("content2")
        (tmp_path / "subdir").mkdir()
        (tmp_path / "subdir" / "file3.txt").write_text("content3")

        # When: 列出目录
        items = FileOps.list_dir(tmp_path, recursive=True)

        # Then: 返回所有文件
        assert len(items) >= 3
        assert any("file1.txt" in str(p) for p in items)
        assert any("file2.txt" in str(p) for p in items)
        assert any("file3.txt" in str(p) for p in items)

    def test_file_ops_find_files_workflow(self, tmp_path):
        """测试文件查找工作流"""
        # Given: 临时目录和文件
        (tmp_path / "test1.py").write_text("code1")
        (tmp_path / "test2.txt").write_text("text1")
        (tmp_path / "subdir").mkdir()
        (tmp_path / "subdir" / "test3.py").write_text("code2")

        # When: 查找 .py 文件
        python_files = FileOps.find_files(tmp_path, pattern="*.py")

        # Then: 返回匹配的文件
        assert len(python_files) == 2
        assert all(f.suffix == ".py" for f in python_files)

    def test_string_ops_truncate_workflow(self):
        """测试字符串截断工作流"""
        # Given: 长字符串
        long_text = "This is a very long string that needs truncation"

        # When: 截断字符串
        truncated = StringOps.truncate(long_text, max_length=20)

        # Then: 返回截断后的字符串
        assert len(truncated) <= 23  # 20 + "..."

    def test_string_ops_escape_workflow(self):
        """测试字符串转义工作流"""
        # Given: 包含特殊字符的字符串
        text = '<script>alert("test")</script>'

        # When: HTML 转义
        escaped = StringOps.escape(text, mode="html")

        # Then: 特殊字符被转义
        assert "&lt;" in escaped
        assert "&gt;" in escaped
        assert "<script>" not in escaped

    def test_string_ops_format_workflow(self):
        """测试字符串格式化工作流"""
        # Given: 驼峰字符串
        text = "HelloWorld"

        # When: 格式化为蛇形
        snake_case = StringOps.format(text, style="snake_case")

        # Then: 返回蛇形格式
        assert snake_case == "hello_world"

        # When: 格式化为标题
        text2 = "hello world"
        title_case = StringOps.format(text2, style="title_case")

        # Then: 返回标题格式
        assert title_case == "Hello World"

    def test_utils_full_integration(self, tmp_path):
        """测试 Utils 完整集成"""
        # Given: 临时目录
        test_file = tmp_path / "test.txt"

        # When: 使用 StringOps 处理内容，使用 FileOps 写入
        original = "This is a test content for full integration"
        formatted = StringOps.format(original, style="title_case")
        FileOps.write(test_file, formatted)

        # Then: 文件被写入
        assert test_file.exists()

        # When: 使用 FileOps 读取，使用 StringOps 截断
        read_content = FileOps.read(test_file)
        truncated = StringOps.truncate(read_content, max_length=10)

        # Then: 返回正确结果
        assert "Test" in truncated
        assert len(truncated) <= 13
