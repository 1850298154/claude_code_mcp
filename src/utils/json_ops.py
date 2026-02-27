# ============================================================================
# 文件: src/utils/json_ops.py
# 描述: JSON 操作工具类
#
# 上游依赖: 无
# 下游封装: utils/string_ops/, utils/file_ops/
#
# Bash 快速定位:
#   find . -name "json_ops.py" -path "*/utils/*"
# ============================================================================

"""JSON 操作工具

提供 JSON 文件的读取、写入和解析功能。
"""

import json
from pathlib import Path
from typing import Any, Dict


class JsonOps:
    """JSON 操作类

    提供便捷的 JSON 文件操作方法。
    """

    @staticmethod
    def read(file_path: str | Path) -> Dict[str, Any]:
        """读取 JSON 文件

        Args:
            file_path: JSON 文件路径

        Returns:
            解析后的 JSON 对象

        Raises:
            FileNotFoundError: 文件不存在
            json.JSONDecodeError: JSON 格式错误
        """
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def write(file_path: str | Path, data: Dict[str, Any], indent: int = 2) -> None:
        """写入 JSON 文件

        Args:
            file_path: JSON 文件路径
            data: 要写入的数据
            indent: 缩进空格数
        """
        # 确保父目录存在
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)

    @staticmethod
    def parse(json_str: str) -> Dict[str, Any]:
        """解析 JSON 字符串

        Args:
            json_str: JSON 字符串

        Returns:
            解析后的 JSON 对象

        Raises:
            json.JSONDecodeError: JSON 格式错误
        """
        return json.loads(json_str)

    @staticmethod
    def stringify(data: Dict[str, Any], indent: int = 2) -> str:
        """将对象转换为 JSON 字符串

        Args:
            data: 要转换的数据
            indent: 缩进空格数

        Returns:
            JSON 字符串
        """
        return json.dumps(data, ensure_ascii=False, indent=indent)
