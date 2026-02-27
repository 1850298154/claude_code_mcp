# ============================================================================
# 文件: src/utils/__main__.py
# 描述: Utils 模块主入口
#
# Bash 快速定位:
#   find src -name "__main__.py" -path "*/utils/*"
# ============================================================================

"""Utils 模块主入口"""

from utils.file_ops import FileOps
from utils.string_ops import StringOps


def main():
    """主函数"""
    print("Utils Module - Example Usage")
    print("=" * 50)
    print("\nFileOps:")
    print("  FileOps.write('file.txt', 'Hello')")
    print("  content = FileOps.read('file.txt')")
    print("  files = FileOps.list_dir('.', recursive=True)")
    print("  matches = FileOps.find_files('.', '*.py')")
    print("\nStringOps:")
    print("  truncated = StringOps.truncate('long text...', max_length=10)")
    print("  escaped = StringOps.escape('<script>', mode='html')")
    print("  formatted = StringOps.format('HelloWorld', style='snake_case')")


if __name__ == "__main__":
    main()
