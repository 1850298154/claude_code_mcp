# ============================================================================
# 文件: test/run.py
# 描述: 测试运行脚本
#
# Bash 快速定位: find test -name "run.py"
# ============================================================================

#!/usr/bin/env python3
"""测试运行脚本

从 test 目录运行所有测试。
"""

import sys
import subprocess
from pathlib import Path


def main():
    """运行测试"""
    test_dir = Path(__file__).parent

    # 默认运行所有测试
    args = ["pytest", "-v"] + sys.argv[1:]

    # 运行测试
    result = subprocess.run(args, cwd=test_dir)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
