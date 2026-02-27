# ============================================================================
# 文件: test/unit/utils/test_json_ops.py
# 描述: 测试 JsonOps 类
#
# 测试对象: utils/json_ops.py
#
# Bash 快速定位:
#   find test -name "test_json_ops.py"
# ============================================================================

import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
import json

from utils.json_ops import JsonOps


class TestJsonOps:
    """测试 JsonOps 类"""

    def test_json_read(self):
        """测试读取 JSON 文件"""
        # Given: JSON 文件
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test.json"
            test_data = {"name": "Test", "value": 123}
            file_path.write_text(json.dumps(test_data))

            # When: 读取 JSON
            result = JsonOps.read(file_path)

            # Then: 返回正确数据
            assert result == test_data

    def test_json_write(self):
        """测试写入 JSON 文件"""
        # Given: 数据
        test_data = {"name": "Test", "value": 123}

        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test.json"

            # When: 写入 JSON
            JsonOps.write(file_path, test_data)

            # Then: 文件被写入
            assert file_path.exists()
            result = json.loads(file_path.read_text())
            assert result == test_data

    def test_json_parse(self):
        """测试解析 JSON 字符串"""
        # Given: JSON 字符串
        json_str = '{"name": "Test", "value": 123}'

        # When: 解析 JSON
        result = JsonOps.parse(json_str)

        # Then: 返回正确对象
        assert result == {"name": "Test", "value": 123}

    def test_json_stringify(self):
        """测试转换为 JSON 字符串"""
        # Given: 数据对象
        test_data = {"name": "Test", "value": 123}

        # When: 转换为 JSON 字符串
        result = JsonOps.stringify(test_data)

        # Then: 返回有效 JSON
        parsed = json.loads(result)
        assert parsed == test_data
